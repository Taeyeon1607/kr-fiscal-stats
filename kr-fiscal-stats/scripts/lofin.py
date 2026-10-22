#!/usr/bin/env python3
"""지방재정365(lofin365.go.kr) — 지방자치단체 재정 자료 146종.

  python3 lofin.py RHJDKD --peek                      # 1건만 받아 칸 이름과 «뜻»을 본다 (첫 걸음)
  python3 lofin.py RHJDKD --fyr 2024 --all --csv 결과.csv
  python3 lofin.py AIDFA --fyr 2025 --wa_laf_hg_nm 경기 --sum biz_bdg_tott_amt --by laf_hg_nm,fld_nm
  python3 lofin.py 대조                               # 레퍼런스 목록이 지금 포털과 같은지 (키 불필요, 한 번 부른다)
  python3 lofin.py 대조 --고치기                      # 다르면 목록·칸뜻 파일을 포털에서 다시 만든다 (2분쯤)

인증키 = 환경변수 LOFIN_API_KEY → ~/.lofin_key. 키 값은 찍지 않는다.
"""
import html
import json
import os
import re
import sys
import time
import urllib.parse

from common import REFS, fetch, guard, run_hub, write_ref, Blocked, source_line

BASE = "https://www.lofin365.go.kr/lf/hub"
PORTAL = "https://www.lofin365.go.kr/lf/pfinDtaOpen/dtst/dtstSvi"
XHR = {"X-Requested-With": "XMLHttpRequest"}
# 포털 「출력값」 표가 틀린 것 — 값으로 재서 바로잡았다(2026-09-23, 2025 경기본청).
# fin_acv_* 는 모든 분야에 값이 있는 행정운영경비, padm_oper_* 는 「기타」 분야에만 있는 재무활동이다.
FIXES = {("AIDFA", "fin_acv_prsm_amt"): "행정운영경비순계", ("AIDFA", "padm_oper_prsm_exps"): "재무활동순계"}


def meanings(hub):
    """lofin-칸뜻.md 에서 이 자료의 «칸 이름 → 뜻»."""
    out = {}
    try:
        with open(os.path.join(REFS, "lofin-칸뜻.md"), encoding="utf-8") as f:
            for line in f:
                cells = [c.strip().strip("`") for c in line.strip().strip("|").split("|")]
                if len(cells) >= 3 and cells[0] == hub:
                    out[cells[1]] = cells[2]
    except OSError:
        pass
    return out


def clean(s):
    s = re.sub(r"<br\s*/?>|</br>", " ", s or "", flags=re.I)
    s = html.unescape(re.sub(r"<[^>]+>", "", s))
    return re.sub(r"\s+", " ", s).strip()


def portal_list():
    """포털 데이터셋 목록(키 불필요) — 엑셀 내려받기 단추가 부르는 것. 146종이 한 번에 온다."""
    body = fetch(PORTAL + "/retvLstDtstExcelDown.do", headers=XHR, data=urllib.parse.urlencode(
        {"menuId": "LF5100000", "curPage": 1, "pageSize": 1000}).encode())
    return json.loads(body)["resultList"]


def portal_detail(pdta_id):
    """자료 하나의 OpenAPI 상세 화면 — 요청주소(자료코드)·적재주기·검색 요청인자·출력값 표."""
    t = fetch(PORTAL + "/retvDtstDtsApi.do", headers=XHR, data=urllib.parse.urlencode(
        {"menuId": "LF5120000", "uprMenuId": "LF5100000", "pdtaId": pdta_id}).encode())

    def table(cap):
        m = re.search(r"<caption>\s*" + re.escape(cap) + r"\s*</caption>(.*?)</table>", t, re.S)
        if not m:
            return []
        body = re.sub(r"<thead.*?</thead>", "", m.group(1), flags=re.S)
        rows = []
        for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", body, re.S):
            tds = [clean(c) for c in re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S)]
            if tds:
                rows.append(tds)
        return rows

    hub = re.search(r"요청주소 : https://(?:www\.)?lofin365\.go\.kr/lf/hub/([A-Za-z0-9_]+)", t)
    cycle = re.search(r">\s*적재주기\s*</div>\s*<div[^>]*>(.*?)</div>", t, re.S)
    return (hub.group(1) if hub else None, clean(cycle.group(1)) if cycle else "",
            table("검색 요청인자"), table("출력값"))


def held_titles():
    """파일에 적힌 (이름, 자료코드) 목록. ★이름이 같은 자료가 둘 있어서 사전이 아니라 목록이다."""
    try:
        text = open(os.path.join(REFS, "lofin-목록.md"), encoding="utf-8").read()
    except OSError:
        return []
    return [(m.group(2).strip(), m.group(1)) for m in re.finditer(r"^\| `([A-Za-z0-9_]+)` \| (.*?) \|", text, re.M)]


def rebuild(listed):
    """포털에서 상세를 전부 받아 lofin-목록.md · lofin-칸뜻.md 를 새로 쓴다."""
    cell = lambda s: (s or "").replace("|", "/").strip()
    cats, fields = {}, {}
    for n, x in enumerate(listed, 1):
        hub, cycle, params, outs = portal_detail(x["pdtaId"])
        if hub is None:
            print("  ★상세에서 자료코드를 못 찾았습니다 — 건너뜀:", clean(x.get("pdtaNm")))
            continue
        cats.setdefault(clean(x.get("menuAtcClsNm")) or "(분류없음)", []).append(
            (hub, clean(x.get("pdtaNm")), clean(x.get("pdtaInfoCntt")), cycle,
             " ".join(r[2] for r in params if len(r) >= 3), " ".join(r[2] for r in outs if len(r) >= 3)))
        fields[hub] = [(r[1], FIXES.get((hub, r[1]), r[2]), r[3] if len(r) > 3 else "") for r in outs if len(r) >= 3]
        if n % 20 == 0:
            print("  … %d/%d" % (n, len(listed)))
        time.sleep(0.6)
    day = time.strftime("%Y-%m-%d")
    total = sum(len(v) for v in cats.values())
    lines = ["# 지방재정365 OpenAPI 목록 — %d개" % total, "", source_line("lofin", day), "",
             "각 줄의 **자료코드**를 `https://www.lofin365.go.kr/lf/hub/{자료코드}` 의 자리에 넣는다.", "",
             "- **검색조건** = 거르개 항목의 한글 이름. 실제 인자 이름은 응답의 칸 이름이다(`references/lofin.md` 「거르개 이름」).",
             "- **출력항목** = 한글 이름. 응답 칸 이름(`pfa_amt1` 따위)과 뜻의 대응은 **`lofin-칸뜻.md`**.",
             "- ★**같은 주제가 여러 분류에 흩어져 있다** — 분류 제목만 보지 말고 낱말로 파일 전체를 훑는다.",
             "- **%s 에 `lofin.py 대조 --고치기` 로 포털에서 받은 것**이다. 자료 연도는 그 뒤 늘었을 수 있다." % day, ""]
    for cat in sorted(cats):
        rows = sorted(cats[cat], key=lambda r: r[1])
        lines += ["", "## %s (%d개)" % (cat, len(rows)), "",
                  "| 자료코드 | 이름 | 자료 연도 | 갱신 | 검색조건 | 출력항목 |", "|---|---|---|---|---|---|"]
        lines += ["| `%s` | %s | %s | %s | %s | %s |" % tuple([r[0]] + [cell(v) for v in r[1:]]) for r in rows]
    guard("lofin-목록.md", total, len(held_titles()))
    p1 = write_ref("lofin-목록.md", "\n".join(lines) + "\n")
    lines = ["# 지방재정365 — 응답 칸 이름과 뜻 (%d개 자료 · %d칸)" % (len(fields), sum(len(v) for v in fields.values())), "", source_line("lofin", day), "",
             "출처는 포털의 자료별 OpenAPI 상세 화면 「출력값」 표(%s 받음)." % day, "",
             "- ★**칸은 «이름»으로 맞춘다. 순서로 맞추지 않는다** — 포털 표와 실제 응답의 순서가 다른 자료가 있다.",
             "- ★**금액 단위는 거의 안 적혀 있다.** 뜻 칸에 `(천원)`·`(원)`·`(%)` 로 적힌 것만 공식 표기다. 나머지는 크기로 맞춰 보고 «추정»이라고 밝힌다.",
             "- ★**`AIDFA` 순계 두 칸은 포털 표가 거꾸로 적었다** — 값으로 재서 바로잡았다(`lofin.py` 의 `FIXES`). 총계 두 칸은 포털 표가 맞다.", "",
             "| 자료코드 | 칸 | 뜻 | 포털 설명 |", "|---|---|---|---|"]
    for hub in sorted(fields):
        lines += ["| `%s` | `%s` | %s | %s |" % (hub, c, cell(l), cell(d)) for c, l, d in fields[hub]]
    p2 = write_ref("lofin-칸뜻.md", "\n".join(lines) + "\n")
    print("새로 썼습니다:", p1, "·", p2)


def check(fix):
    try:
        listed = portal_list()
    except Blocked as e:
        sys.exit(str(e))
    from collections import Counter
    held = held_titles()
    now, had = Counter(clean(x.get("pdtaNm")) for x in listed), Counter(t for t, _ in held)
    added, gone = sorted((now - had).elements()), sorted((had - now).elements())
    print("포털 %d종 · 파일 %d종 · 새로 생김 %d · 없어짐(또는 이름 바뀜) %d" % (len(listed), len(held), len(added), len(gone)))
    for t in added:
        print("  + %s" % t)
    for t in gone:
        print("  - %s  (%s)" % (t, ", ".join(c for n, c in held if n == t)))
    if not added and not gone:
        print("목록이 지금 포털과 같습니다. (자료 연도·칸은 이 대조가 안 본다 — --고치기 는 그것까지 새로 받는다)")
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
        run_hub(BASE, "LOFIN_API_KEY", "lofin", "https://www.lofin365.go.kr 회원가입·로그인 → 위 메뉴 「재정데이터개방」 → 인증키 신청",
                meanings=meanings, example="RHJDKD")
