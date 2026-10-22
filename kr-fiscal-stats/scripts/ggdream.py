#!/usr/bin/env python3
"""경기데이터드림(data.gg.go.kr) — 경기도 공공데이터 OPEN API.

  python3 ggdream.py search 버스정류소                 # 목록 파일에서 서비스를 낱말로 찾는다
  python3 ggdream.py <서비스명> --peek                  # 칸 이름·총건수 (칸 뜻 목록은 없다 — 1건을 보고 판단)
  python3 ggdream.py <서비스명> --SIGUN_NM 수원시 --all --csv 결과.csv
  python3 ggdream.py 대조 [--고치기]                    # 목록 파일을 지금 목록(opendatalist)과 맞춰 본다 (세 번 부른다)

★«키 없이» 부르면 오류 없이 총건수는 그대로 주면서 «5행만» 준다 — 스크립트는 키 없이는 부르지 않는다.
★curl·wget 표식은 「보안 정책에 의해 차단」 화면을 받는다 — 스크립트는 브라우저 표식으로 부른다.
인증키 = 환경변수 GGDREAM_API_KEY → ~/.ggdream_key. 키 값은 찍지 않는다.
"""
import os
import re
import sys
import time

from common import REFS, Blocked, fetch_all, find_key, guard, hub_call, run_hub, write_ref, source_line

BASE = "https://openapi.gg.go.kr"
SIGNUP = "https://data.gg.go.kr/portal/openapi/insertApikeyPage.do (회원가입·로그인 뒤 인증키 발급)"


def held():
    try:
        text = open(os.path.join(REFS, "ggdream-목록.md"), encoding="utf-8").read()
    except OSError:
        return {}
    return {m.group(1): m.group(2).strip() for m in re.finditer(r"^\| `([^`]+)` \| (.*?) \|", text, re.M)}


def service_of(row):
    return (row.get("URL") or "").rstrip("/?").split("/")[-1] or None


def write_list(rows):
    groups = {}
    for r in rows:
        s = service_of(r)
        if s:
            cat = " > ".join(x for x in (r.get("CATE_NM"), r.get("CATE_NM2")) if x) or "(분류 없음)"
            groups.setdefault(cat, []).append((s, r.get("INF_NM") or "", r.get("INF_TAG") or ""))
    n = sum(len(v) for v in groups.values())
    cell = lambda v: str(v).replace("|", "/").replace("\n", " ").strip()
    lines = ["# 경기데이터드림 OPEN API 목록 — %d개" % n, "", source_line("ggdream"), "",
             "`ggdream.py <서비스명> --peek` 로 칸 이름을 먼저 본다. ★칸 뜻 표는 없다 — 1건을 보고 판단하고, 모르면 모른다고 말한다.", "",
             "- 거르개는 칸 이름 그대로다(예: `--SIGUN_NM 수원시`). 모르는 이름은 조용히 무시되니 **총건수가 줄었는지** 본다.",
             "- **%s 에 `ggdream.py 대조 --고치기` 로 받은 것**이다." % time.strftime("%Y-%m-%d"), ""]
    for g in sorted(groups):
        rows_g = sorted(groups[g], key=lambda x: x[1])
        lines += ["", "## %s (%d개)" % (g, len(rows_g)), "", "| 서비스명 | 이름 | 꼬리표 |", "|---|---|---|"]
        lines += ["| `%s` | %s | %s |" % (s, cell(nm), cell(tag)[:80]) for s, nm, tag in rows_g]
    guard("ggdream-목록.md", n, len(held()))
    return write_ref("ggdream-목록.md", "\n".join(lines) + "\n")


def check(fix):
    key = find_key("GGDREAM_API_KEY", "ggdream", SIGNUP)
    try:
        total, rows = fetch_all(lambda page, size: hub_call(BASE, "opendatalist", key, page, size, "KEY"))
    except Blocked as e:
        sys.exit(str(e))
    except RuntimeError as e:
        sys.exit("실패: %s" % e)
    if len(rows) < total:
        sys.exit("★목록이 덜 왔습니다(%d / %d행). 키 권한이나 상대 서버 문제일 수 있습니다 — 대조하지 않고 멈춥니다." % (len(rows), total))
    now = {service_of(r): (r.get("INF_NM") or "").strip() for r in rows if service_of(r)}
    had = held()
    added, gone = sorted(set(now) - set(had)), sorted(set(had) - set(now))
    print("지금 %d개(목록 %d행) · 파일 %d개 · 새로 생김 %d · 없어짐 %d" % (len(now), total, len(had), len(added), len(gone)))
    for s in added[:30]:
        print("  + %s %s" % (s, now[s]))
    for s in gone[:30]:
        print("  - %s %s" % (s, had[s]))
    if fix:
        print("새로 썼습니다:", write_list(rows))
    elif added or gone:
        print("★목록이 달라졌습니다. `대조 --고치기` 로 새로 받고, 무엇이 바뀌었는지 사용자에게 알리십시오(SKILL 「스킬 스스로 고치기」).")
    else:
        print("목록이 지금과 같습니다.")


def search(words):
    hits = [(s, n) for s, n in held().items() if all(w in n for w in words)]
    if not hits:
        print("목록 파일에 없습니다. 낱말을 줄이거나, 목록이 낡았으면 `ggdream.py 대조` 를 돌리십시오.")
    for s, n in hits[:40]:
        print("  %-28s %s" % (s, n))
    if len(hits) > 40:
        print("  … %d개 더 — 낱말을 더 붙여 좁히거나 references/ggdream-목록.md 를 직접 읽으십시오" % (len(hits) - 40))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "대조":
        check("--고치기" in sys.argv[2:])
    elif len(sys.argv) > 2 and sys.argv[1] == "search":
        search(sys.argv[2:])
    else:
        run_hub(BASE, "GGDREAM_API_KEY", "ggdream", SIGNUP, key_param="KEY", example="opendatalist")
