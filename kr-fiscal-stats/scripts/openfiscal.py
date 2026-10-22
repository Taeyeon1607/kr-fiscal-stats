#!/usr/bin/env python3
"""열린재정(openfiscaldata.go.kr) — 중앙정부 재정 OPEN API.

  python3 openfiscal.py GovernmentDebtYear --peek
  python3 openfiscal.py GovernmentDebtYear --all --csv 국가채무.csv
  python3 openfiscal.py TotalExpenditure5 --FSCL_YY 2025 --BDG_FND_DIV_CD 0 --ANEXP_INQ_STND_CD 1 \\
      --sum Y_YY_DFN_MEDI_KCUR_AMT --by FLD_NM
  python3 openfiscal.py 대조                 # 레퍼런스 목록이 지금 포털과 같은지 (키 불필요, 한 번 부른다)
  python3 openfiscal.py 대조 --고치기        # 다르면 목록 파일을 포털에서 다시 만든다 (서비스마다 두 번 — 4분쯤)

★이 API 는 «부르는 쪽»을 가린다 — 브라우저 표식이 없으면 오류 안내 화면을 준다. 스크립트가 표식을 단다.
★성공이 HTTP 201 이고, JSON 이 문자열로 한 번 더 싸여 온다 — 스크립트가 두 번 푼다.
인증키 = 환경변수 OPENFISCAL_API_KEY → ~/.openfiscal_key. 키 값은 찍지 않는다.
"""
import json
import os
import re
import sys
import time
import urllib.parse
from collections import Counter

from common import REFS, Blocked, fetch, guard, run_hub, write_ref, source_line

BASE = "https://openapi.openfiscaldata.go.kr"
PORTAL = "https://www.openfiscaldata.go.kr/op/ko"
JSON = {"Content-Type": "application/json", "Referer": "https://www.openfiscaldata.go.kr/op/ko/sd/UOPKOSDA01"}
# 포털의 적재주기 코드 — 2026-09-23 옛 목록의 103종과 맞춰 읽은 것
CYCLES = {"RECY00": "일간", "RECY02": "월간", "RECY03": "분기", "RECY05": "연간", "RECY06": "연간", "RECY07": "수시"}


def portal_list():
    """포털 OPEN API 목록 — 한 번에 온다(키 불필요). 서비스이름(영문)은 없고 한글 이름·기관·주기가 있다."""
    body = fetch(PORTAL + "/ds/selectOpenApiList.do",
                 data=urllib.parse.urlencode({"ofdSysDivCd": "K", "page": 1, "rowPerPage": 1000}).encode())
    return json.loads(body)


def portal_detail(odt_id):
    """서비스 하나 — (분류 경로, 서비스이름, 검색인자, 출력칸). 두 번 부른다.
    ★서비스 순번은 목록의 「A-숫자」가 아니라 여기서 받는다(그 숫자는 보이는 차례라 두 곳에서 틀렸다)."""
    d = json.loads(fetch(PORTAL + "/sd/dtsStats/selectSrvDtlInfoList.do", headers=JSON,
                         data=json.dumps({"opKoSdDtsStatsDVO": {"odtId": odt_id}}).encode()))
    seq = next((s["odtSvSeq"] for s in d.get("selectSrvInfoList") or [] if s.get("rlsSvTyCd") == "A"), None)
    cls = (d.get("selectSrvDtlInfo") or {}).get("allDtaClsNm") or ""
    if seq is None:
        return cls, None, [], []
    time.sleep(0.5)
    a = json.loads(fetch(PORTAL + "/sd/dtsStatsAcol/selectAcolViewList.do", headers=JSON, data=json.dumps(
        {"odtId": odt_id, "rlsSvTyCd": "A", "odtSvSeq": seq, "paramVO": {"odtNm": ""}}).encode()))
    url = (a.get("selectApiRes") or {}).get("dmndUrl") or ""
    service = url.rstrip("?/").split("/")[-1] or None
    params = [(p.get("dsColId"), p.get("colEpl") or p.get("dpColHgNm") or "", p.get("dmndParaEsntlYn") == "Y")
              for p in a.get("selectApiTestList") or [] if p.get("dsColId")]
    outs = [(o.get("dsColId"), o.get("dpColHgNm") or o.get("colEpl") or "")
            for o in sorted(a.get("selectApiOutputValList") or [], key=lambda o: o.get("otptOrd") or 0) if o.get("dsColId")]
    return cls, service, params, outs


def held_names():
    try:
        text = open(os.path.join(REFS, "openfiscal-목록.md"), encoding="utf-8").read()
    except OSError:
        return []
    return [(m.group(1).strip(), m.group(2)) for m in
            re.finditer(r"^### (.+?)\n\n- \*\*서비스이름\*\* `([^`]+)`", text, re.M)]


def rebuild(listed):
    groups, skipped = {}, []
    for n, x in enumerate(listed, 1):
        cls, service, params, outs = portal_detail(x["odtId"])
        if service is None:
            skipped.append(x.get("odtNm"))
        else:
            groups.setdefault(cls or "(분류 없음 — 예산편성 OPEN API 묶음)", []).append((x, service, params, outs))
        if n % 25 == 0:
            print("  … %d/%d" % (n, len(listed)))
        time.sleep(0.5)
    total = sum(len(v) for v in groups.values())
    lines = ["# 열린재정 OPEN API 목록 — %d종" % total, "", source_line("openfiscal"), "",
             "**서비스이름**을 `https://openapi.openfiscaldata.go.kr/{서비스이름}` 의 자리에 넣는다.", "",
             "- **검색인자** = 그대로 주소에 붙이는 이름이다(`OJ_YY=2024` 처럼). `★필수` 가 붙은 것은 반드시 준다. 코드 값(`BDG_FND_DIV_CD` 등)은 `references/openfiscal.md` 4절 표.", "",
             "- **출력칸** = 돌아오는 자료의 칸 이름이다.", "",
             "- ★**금액 단위는 이 목록에 없다** — 서비스마다 조원·억원·천원·원이 다르다. `references/openfiscal.md` 함정 ⑥ 의 표를 보고, 표에 없으면 크기로 맞춰 보고 「추정」이라고 밝힌다.", "",
             "- ★**예산인지 결산인지도 이름으로 가르지 않는다** — `DIV_NM`·`STL_BDG_DIV_NM` 같은 구분 칸을 본다(함정 ⑦).", "",
             "- **%s 에 `openfiscal.py 대조 --고치기` 로 포털에서 받은 것**이다." % time.strftime("%Y-%m-%d"), ""]
    for g in sorted(groups):
        rows = sorted(groups[g], key=lambda r: r[0].get("odtNm", ""))
        lines += ["", "## %s (%d종)" % (g, len(rows))]
        for x, service, params, outs in rows:
            lines += ["", "### %s" % x.get("odtNm", "").strip(), "",
                      "- **서비스이름** `%s`" % service,
                      "- 기관: %s · 갱신: %s" % (x.get("ofdMngOgNm", ""), CYCLES.get(x.get("dtaLoadPrdCd"), x.get("dtaLoadPrdCd", "")))]
            if params:
                lines.append("- **검색인자**: " + ", ".join("`%s`(%s%s)" % (p, l, " ★필수" if req else "") for p, l, req in params))
            if outs:
                lines.append("- 출력칸: " + ", ".join("`%s` %s" % (c, l) for c, l in outs))
    guard("openfiscal-목록.md", total, len(held_names()))
    print("새로 썼습니다:", write_ref("openfiscal-목록.md", "\n".join(lines) + "\n"))
    if skipped:
        print("  ★OPEN API 상세를 못 찾아 뺀 것 %d종: %s" % (len(skipped), ", ".join(skipped[:10])))


def check(fix):
    try:
        listed = portal_list()
    except Blocked as e:
        sys.exit(str(e))
    held = held_names()
    now, had = Counter(x.get("odtNm", "").strip() for x in listed), Counter(t for t, _ in held)
    added, gone = sorted((now - had).elements()), sorted((had - now).elements())
    print("포털 %d종 · 파일 %d종 · 새로 생김 %d · 없어짐(또는 이름 바뀜) %d" % (len(listed), len(held), len(added), len(gone)))
    for t in added[:40]:
        print("  + %s" % t)
    if len(added) > 40:
        print("  + … %d종 더" % (len(added) - 40))
    for t in gone:
        print("  - %s  (%s)" % (t, ", ".join(s for n, s in held if n == t)))
    if not added and not gone:
        print("목록이 지금 포털과 같습니다. (인자·칸은 이 대조가 안 본다 — --고치기 는 그것까지 새로 받는다)")
        if not fix:
            return
    if fix:
        rebuild(listed)
    else:
        print("★목록이 달라졌습니다. `대조 --고치기` 로 새로 받고, 무엇이 바뀌었는지 사용자에게 알리십시오(SKILL 「스킬 스스로 고치기」).")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "대조":
        check("--고치기" in sys.argv[2:])
    else:
        run_hub(BASE, "OPENFISCAL_API_KEY", "openfiscal", "https://www.openfiscaldata.go.kr/op/ko/ds/UOPKODSA01.do (로그인 뒤 인증키 발급)",
                example="GovernmentDebtYear")
