#!/usr/bin/env python3
"""한국은행 ECOS(경제통계시스템) — 금리·물가·환율·통화·국민계정·국제수지 통계표.

  python3 ecos.py search 기준금리                      # 목록 파일에서 통계표를 낱말로 찾는다
  python3 ecos.py items 722Y001                         # 그 표의 항목·주기·기간·단위
  python3 ecos.py data 722Y001 --주기 M --기간 202401 202412 --항목 0101000
  python3 ecos.py data 901Y009 --주기 M --기간 202401 202406 --csv 물가.csv
  python3 ecos.py 대조 [--고치기]                       # 목록 파일을 지금 ECOS 목록과 맞춰 본다 (한 번 부른다)

★주소가 «경로» 모양이고 키가 그 안에 들어간다 — 오류 문구에 주소를 찍지 않는다.
인증키 = 환경변수 ECOS_API_KEY → ~/.ecos_key. 키 값은 찍지 않는다.
"""
import argparse
import os
import re
import sys
import time
import urllib.parse

from common import REFS, Blocked, fetch, find_key, guard, loads, save, write_ref, source_line

BASE = "https://ecos.bok.or.kr/api"
SIGNUP = "https://ecos.bok.or.kr/api/#/AuthKeyApply (회원가입·로그인 뒤 인증키 신청)"
# 주기마다 날짜 모양 — 틀리면 ERROR-101
SHAPES = {"A": r"^\d{4}$", "S": r"^\d{4}S[12]$", "Q": r"^\d{4}Q[1-4]$", "M": r"^\d{6}$", "SM": r"^\d{6}S[12]$", "D": r"^\d{8}$"}


def call(key, service, start, end, *rest):
    """ECOS 한 번. 성공 = {"서비스": {"list_total_count", "row"}}, 오류·빈결과 = {"RESULT": {"CODE","MESSAGE"}} — 모양이 다르다.
    HTTP 는 언제나 200 이다(서비스 이름 오타만 404 HTML)."""
    path = "/".join(urllib.parse.quote(str(p), safe="") for p in (service, key, "json", "kr", start, end) + rest)
    body = fetch("%s/%s" % (BASE, path))
    if body.lstrip().startswith("<"):
        raise RuntimeError("자료 대신 HTML 이 왔습니다 — 서비스 이름 오타이거나 상대 쪽 장애입니다.")
    d = loads(body)
    if "RESULT" in d:
        code, msg = d["RESULT"].get("CODE"), d["RESULT"].get("MESSAGE", "")
        if code == "INFO-200":
            return 0, []
        raise RuntimeError("%s %s" % (code, msg))
    top = d[service]
    return int(top.get("list_total_count", 0)), top.get("row", [])


def catalogue(key):
    total, rows = call(key, "StatisticTableList", 1, 10000)
    return rows


def held():
    try:
        text = open(os.path.join(REFS, "ecos-목록.md"), encoding="utf-8").read()
    except OSError:
        return {}
    return {m.group(1): m.group(2).strip() for m in re.finditer(r"^\| `([^`]+)` \| (.*?) \|", text, re.M)}


def write_list(rows):
    by_code = {r["STAT_CODE"]: r for r in rows}

    def path(r):
        out, seen = [], set()
        p = r.get("P_STAT_CODE")
        while p in by_code and p not in seen:
            seen.add(p)
            out.insert(0, by_code[p]["STAT_NAME"].strip())
            p = by_code[p].get("P_STAT_CODE")
        return " > ".join(out) or "(최상위)"

    groups = {}
    for r in rows:
        if r.get("SRCH_YN") == "Y":
            groups.setdefault(path(r), []).append(r)
    n = sum(len(v) for v in groups.values())
    lines = ["# 한국은행 ECOS 통계표 목록 — %d개" % n, "", source_line("ecos"), "",
             "`ecos.py data <통계표코드> --주기 <주기>` 로 받는다. 항목·기간·단위는 먼저 `ecos.py items <통계표코드>` 로 본다.", "",
             "- ★**주기 칸은 대표 주기 하나뿐이다** — 같은 표의 항목이 다른 주기로도 있다(예: 722Y001 은 D 로 적혀 있지만 A·Q·M 도 있다). `items` 로 확인한다.",
             "- 주기: A 해 · S 반년 · Q 분기 · M 달 · SM 반달 · D 날.",
             "- **%s 에 `ecos.py 대조 --고치기` 로 받은 것**이다." % time.strftime("%Y-%m-%d"), ""]
    for g in sorted(groups):
        lines += ["", "## %s (%d개)" % (g, len(groups[g])), "", "| 통계표코드 | 이름 | 주기 | 기관 |", "|---|---|---|---|"]
        lines += ["| `%s` | %s | %s | %s |" % (r["STAT_CODE"], r["STAT_NAME"].strip().replace("|", "/"),
                                              r.get("CYCLE") or "", (r.get("ORG_NAME") or "").strip())
                  for r in groups[g]]
    guard("ecos-목록.md", n, len(held()))
    return write_ref("ecos-목록.md", "\n".join(lines) + "\n")


def cmd_search(a, key):
    words = a.말.split()
    hits = [(c, n) for c, n in held().items() if all(w in n for w in words)]
    if not hits:
        print("목록 파일에 없습니다. 낱말을 줄이거나, 목록이 낡았으면 `ecos.py 대조` 를 돌리십시오.")
    for c, n in hits[:40]:
        print("  %-10s %s" % (c, n))
    if len(hits) > 40:
        print("  … %d개 더 — 낱말을 더 붙여 좁히거나 references/ecos-목록.md 를 직접 읽으십시오" % (len(hits) - 40))


def cmd_items(a, key):
    total, rows = call(key, "StatisticItemList", 1, 2000, a.표)
    if not rows:
        print("항목이 없습니다 — 통계표코드를 확인하십시오(틀린 코드도 «자료 없음»으로 온다)."); return
    print("%s — 항목 %d개" % (rows[0].get("STAT_NAME"), total))
    for r in rows:
        print("  %s %-14s %-30s 주기 %-2s %s~%s  %s" % (
            (r.get("GRP_NAME") or "")[:10], r.get("ITEM_CODE"), (r.get("ITEM_NAME") or "")[:30], r.get("CYCLE"),
            r.get("START_TIME"), r.get("END_TIME"), r.get("UNIT_NAME") or ""))


def cmd_data(a, key):
    s, e = a.기간
    shape = SHAPES.get(a.주기)
    if shape and not (re.match(shape, s) and re.match(shape, e)):
        sys.exit("기간 모양이 주기 %s 와 맞지 않습니다 — A 2024 · Q 2024Q1 · M 202401 · D 20240101 · S 2024S1" % a.주기)
    items = a.항목 or []
    rows, start, size = [], 1, 10000
    while True:
        total, got = call(key, "StatisticSearch", start, start + size - 1, a.표, a.주기, s, e, *items)
        rows.extend(got)
        if not got or len(rows) >= total:
            break
        start += size
        time.sleep(0.3)
    if not rows:
        print("자료가 없습니다. ★ECOS 는 틀린 통계표·항목 코드와 없는 기간도 «자료 없음»으로 답한다 — `items` 로 코드와 기간을 확인하십시오.")
        return
    units = sorted({r.get("UNIT_NAME") for r in rows if r.get("UNIT_NAME")})
    print("%d행 | %s | 단위: %s" % (len(rows), rows[0].get("STAT_NAME"), " · ".join(units) or "?(첫 묶음이 아닌 항목은 단위가 비어 온다)"))
    if len(units) > 1:
        print("  ★단위가 «항목마다 다릅니다». 합치거나 비교하기 전에 UNIT_NAME 을 행마다 확인하십시오.")
    if not a.csv:
        for r in rows[:8]:
            print("  %s | %s %s | %s %s" % (r.get("TIME"), r.get("ITEM_NAME1"), r.get("ITEM_NAME2") or "",
                                           r.get("DATA_VALUE"), r.get("UNIT_NAME") or ""))
        if len(rows) > 8:
            print("  … 나머지 %d행 생략 (--csv 로 저장하십시오)" % (len(rows) - 8))
    else:
        save(rows, a.csv)


def cmd_check(a, key):
    rows = catalogue(key)
    now = {r["STAT_CODE"]: r["STAT_NAME"].strip() for r in rows if r.get("SRCH_YN") == "Y"}
    had = held()
    added, gone = sorted(set(now) - set(had)), sorted(set(had) - set(now))
    renamed = sorted(c for c in set(now) & set(had) if now[c] != had[c])
    print("ECOS %d개 · 파일 %d개 · 새로 생김 %d · 없어짐 %d · 이름 바뀜 %d" % (len(now), len(had), len(added), len(gone), len(renamed)))
    for c in added[:30]:
        print("  + %s %s" % (c, now[c]))
    for c in gone[:30]:
        print("  - %s %s" % (c, had[c]))
    for c in renamed[:30]:
        print("  ~ %s %s → %s" % (c, had[c], now[c]))
    if added or gone or renamed or a.고치기:
        if a.고치기:
            print("새로 썼습니다:", write_list(rows))
        else:
            print("★목록이 달라졌습니다. `대조 --고치기` 로 새로 받고, 무엇이 바뀌었는지 사용자에게 알리십시오(SKILL 「스킬 스스로 고치기」).")
    else:
        print("목록이 지금 ECOS 와 같습니다.")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("search", help="목록 파일에서 통계표를 낱말로 찾는다(낱말 여럿이면 모두 든 것)")
    p.add_argument("말")
    p = sub.add_parser("items", help="통계표의 항목·주기·기간·단위")
    p.add_argument("표")
    p = sub.add_parser("data", help="자료를 받는다")
    p.add_argument("표")
    p.add_argument("--주기", required=True, choices=sorted(SHAPES))
    p.add_argument("--기간", nargs=2, required=True, metavar=("시작", "끝"))
    p.add_argument("--항목", nargs="*", help="항목코드를 묶음 차례대로(빼면 모든 조합이 온다)")
    p.add_argument("--csv")
    p = sub.add_parser("대조", help="목록 파일을 지금 ECOS 목록과 맞춰 본다")
    p.add_argument("--고치기", action="store_true")
    a = ap.parse_args()
    key = None if a.cmd == "search" else find_key("ECOS_API_KEY", "ecos", SIGNUP)
    try:
        {"search": cmd_search, "items": cmd_items, "data": cmd_data, "대조": cmd_check}[a.cmd](a, key)
    except Blocked as e:
        sys.exit(str(e))
    except RuntimeError as e:
        sys.exit("실패: %s" % e)


if __name__ == "__main__":
    main()
