#!/usr/bin/env python3
"""KOSIS(국가통계포털) 공유서비스 호출기 — 표준 라이브러리만 쓴다(설치할 것 없음).

세 가지만 한다.

  찾기   python3 kosis.py search "국세 징세비"
  훑기   python3 kosis.py list 133_13301_200          # 가지 아래를 본다
  받기   python3 kosis.py data 133 TX_13301_A056 --최근 5
         python3 kosis.py data 133 DT_13301_000 --기간 2018 2024 --csv 세수.csv

  대조   python3 kosis.py 대조 [--고치기]               # 국세통계 목록 파일을 지금 KOSIS 와 맞춰 본다(1분쯤)

인증키 = 환경변수 KOSIS_API_KEY → ~/.kosis_key. 키 값은 화면에 찍지 않는다.
"""
import argparse
import csv
import json
import os
import re
import sys
import time
import urllib.parse

from common import REFS, Blocked, fetch, find_key, guard, hide, write_ref, source_line

BASE = "https://kosis.kr/openapi"


def _loads(body):
    """KOSIS 오류 응답은 «따옴표 없는» 엉터리 JSON 으로 오는 갈래가 있다.
    예: {err:"11",errMsg:"유효하지않은 인증KEY입니다."}  ← 그냥 json.loads 하면 죽는다."""
    try:
        return json.loads(body)
    except Exception:
        fixed = re.sub(r"([{,])\s*([A-Za-z_][A-Za-z0-9_]*)\s*:", r'\1"\2":', body)
        try:
            return json.loads(fixed)
        except Exception:
            raise RuntimeError("응답을 읽을 수 없습니다(앞 150자): %s" % hide(body)[:150])


def get(path, **params):
    params.setdefault("format", "json")
    params.setdefault("jsonVD", "Y")
    body = fetch("%s/%s?%s" % (BASE, path, urllib.parse.urlencode(params)), timeout=90)
    d = _loads(body)
    if isinstance(d, dict) and "err" in d:
        raise RuntimeError("err %s — %s" % (d.get("err"), d.get("errMsg")))
    if not isinstance(d, list):
        raise RuntimeError("목록이 올 자리에 «꾸러미»가 왔습니다: %s" % hide(d)[:150])
    return d


def cmd_search(a, key):
    rows = get("statisticsSearch.do", method="getList", apiKey=key, searchNm=a.말,
               startCount=a.건너뛰기, resultCount=a.개수)
    if not rows:
        print("찾은 것이 없습니다. 낱말을 줄여 보십시오."); return
    for r in rows:
        print("%-6s %-18s %s" % (r.get("ORG_ID"), r.get("TBL_ID"), r.get("TBL_NM")))
        print("        %s | 기간 %s~%s" % (r.get("MT_ATITLE", ""),
                                          r.get("STRT_PRD_DE", "?"), r.get("END_PRD_DE", "?")))


def cmd_list(a, key):
    rows = get("statisticsList.do", method="getList", apiKey=key,
               vwCd="MT_OTITLE", parentListId=a.가지)
    for r in rows:
        if "TBL_ID" in r:
            print("표   %-6s %-18s %s" % (r.get("ORG_ID"), r["TBL_ID"], r.get("TBL_NM")))
        else:
            print("가지 %-24s %s" % (r.get("LIST_ID"), r.get("LIST_NM")))


def paths(org, tbl, key):
    """분류 칸마다 «윗 분류까지 이은 이름»을 만든다 — {분류 이름: {칸ID: "국세청 세수 > 내국세 > 소득세"}}.
    (자료 행에는 분류의 ID 가 없고 이름(C1_OBJ_NM)만 있어서 이름으로 잇는다.)
    같은 이름(「소득세」「경기」)이 여러 층에 나오는 표가 많아서, 이름만 보면 합계를 잘못 집는다.
    표 설명(getMeta) 한 번이면 칸마다 윗 칸(UP_ITM_ID)이 나온다. 못 받으면 빈 것을 돌려준다."""
    try:
        meta = get("statisticsData.do", method="getMeta", type="ITM", apiKey=key, orgId=org, tblId=tbl)
    except RuntimeError:
        return {}
    items = {}
    for m in meta:
        items.setdefault(m.get("OBJ_NM"), {})[m.get("ITM_ID")] = (m.get("ITM_NM"), m.get("UP_ITM_ID"))
    out = {}
    for obj, table in items.items():
        def walk(i, seen=()):
            name, up = table.get(i, (i, None))
            if up and up in table and up not in seen:
                return walk(up, seen + (i,)) + [name]
            return [name]
        out[obj] = {i: " > ".join(walk(i)) for i in table}
    return out


def cmd_data(a, key):
    p = dict(method="getList", apiKey=key, orgId=a.기관, tblId=a.표,
             itmId=a.항목, objL1=a.분류1, prdSe=a.주기)
    for i, v in enumerate(a.분류더, start=2):
        p["objL%d" % i] = v
    if a.기간:
        p["startPrdDe"], p["endPrdDe"] = a.기간
    else:
        p["newEstPrdCnt"] = a.최근
    # 분류가 몇 겹인지는 표마다 다르고, 겹 수만큼 objL 을 줘야 한다 — 모자라면 err 20(objL),
    # 넘치면 err 21 이다. 그래서 err 20 이 나면 «ALL» 을 한 겹씩 더해 다시 부른다(최대 8겹).
    while True:
        try:
            rows = get("Param/statisticsParameterData.do", **p)
            break
        except RuntimeError as e:
            n = 1 + sum(1 for k in p if k.startswith("objL") and k != "objL1")
            if not str(e).startswith("err 20") or "objL" not in str(e) or n >= 8:
                raise
            p["objL%d" % (n + 1)] = "ALL"
            print("  (분류가 %d겹 이상인 표라 objL%d=ALL 을 더해 다시 부릅니다 — 그 분류의 합계 행까지 함께 와 행이 늘어납니다)" % (n + 1, n + 1))
    if not rows:
        print("자료가 없습니다. 기간이나 분류를 넓혀 보십시오."); return
    # 칸마다 윗 분류까지 이은 이름을 붙인다(C1_경로, C2_경로 …) — 같은 이름을 가르는 유일한 길이다
    tree = paths(a.기관, a.표, key)
    if not tree:
        print("  ★표 설명(getMeta)을 못 받아 C*_경로 칸에 윗 분류 없이 이름만 넣었습니다 — 같은 이름이 여러 층이면 코드(C1)로 가르십시오.")
    for r in rows:
        for n in range(1, 9):
            obj, cid = r.get("C%d_OBJ_NM" % n), r.get("C%d" % n)
            if obj is None or cid is None:
                continue
            r["C%d_경로" % n] = tree.get(obj, {}).get(cid, r.get("C%d_NM" % n, ""))
    units = sorted({r.get("UNIT_NM") for r in rows if r.get("UNIT_NM")})
    print("%d칸 | 표: %s | 단위: %s" % (len(rows), rows[0].get("TBL_NM"), " · ".join(units) or "?"))
    if len(units) > 1:
        print("  ★단위가 «항목마다 다릅니다». 합치거나 비교하기 전에 UNIT_NM 을 칸마다 확인하십시오.")
    if a.csv:
        cols = sorted({k for r in rows for k in r})
        with open(a.csv, "w", newline="", encoding="utf-8-sig") as f:
            w = csv.DictWriter(f, fieldnames=cols)
            w.writeheader(); w.writerows(rows)
        print("csv 저장:", a.csv)
    else:
        for r in rows[:8]:
            print("  %s | %s | %s = %s %s" % (r.get("PRD_DE"), r.get("C1_경로") or r.get("C1_NM", ""),
                                              r.get("ITM_NM"), r.get("DT"), r.get("UNIT_NM") or ""))
        if len(rows) > 8:
            print("  … 나머지 %d칸 생략 (--csv 로 저장하십시오)" % (len(rows) - 8))


# 국세통계 목록 두 파일이 가리키는 가지 — 파일 이름: (가지 ID, 제목)
TREES = {
    "kosis-국세통계-최근.md": ("133_13301_200", "최근분"),
    "kosis-국세통계-2010이전.md": ("133_13301_100", "2010년 이전분"),
}


def walk(root, key, path=()):
    """가지 아래 표를 전부 모은다 — [(경로, 표번호, 표 이름, 갱신일)]. 가지마다 한 번 부른다."""
    out = []
    for r in get("statisticsList.do", method="getList", apiKey=key, vwCd="MT_OTITLE", parentListId=root):
        if "TBL_ID" in r:
            out.append((path, r["TBL_ID"], r.get("TBL_NM", ""), r.get("SEND_DE", "")))
        else:
            time.sleep(0.2)          # 상대 서버를 몰아치지 않는다
            out.extend(walk(r["LIST_ID"], key, path + (r.get("LIST_NM", "").strip(),)))
    return out


def held_in(fname):
    """레퍼런스 파일에 적힌 {표번호: 표 이름}."""
    try:
        text = open(os.path.join(REFS, fname), encoding="utf-8").read()
    except OSError:
        return {}
    return {m.group(1): m.group(2).strip() for m in re.finditer(r"^\| `([^`]+)` \| (.*?) \| [^|]* \|$", text, re.M)}


def write_list(fname, title, tables, top):
    groups = {}
    for path, tid, name, sent in tables:
        groups.setdefault(" > ".join((top,) + path), []).append((tid, name, sent))
    lines = ["# 국세통계 통계표 목록 — %s" % title, "", source_line("kosis"), "",
             "`orgId` 는 전부 **133**(국세청). 표를 받을 때 `tblId` 자리에 **표번호**를 넣는다.", "",
             "맨 끝 칸은 **마지막 갱신일**이다. 이 목록은 %s 에 `kosis.py 대조 --고치기` 로 받은 것이다." % time.strftime("%Y-%m-%d"), ""]
    for g in sorted(groups):
        rows = sorted(groups[g], key=lambda one: one[1])       # 표 이름 차례 — 받아 둔 목록과 같은 차례
        lines += ["", "## %s (%d개)" % (g, len(rows)), "", "| 표번호 | 통계표 이름 | 갱신 |", "|---|---|---|"]
        lines += ["| `%s` | %s | %s |" % (t, n.replace("|", "/"), d) for t, n, d in rows]
    return write_ref(fname, "\n".join(lines) + "\n")


def cmd_check(a, key):
    """레퍼런스 목록을 지금 KOSIS 목록과 맞춰 본다. --고치기 면 파일을 새로 쓴다."""
    changed = False
    for fname, (root, title) in TREES.items():
        top = get("statisticsList.do", method="getList", apiKey=key, vwCd="MT_OTITLE", parentListId="133_13301")
        top_name = next((r.get("LIST_NM") for r in top if r.get("LIST_ID") == root), title)
        live = walk(root, key)
        now = {t: n for _, t, n, _ in live}
        held = held_in(fname)
        added = sorted(set(now) - set(held))
        gone = sorted(set(held) - set(now))
        renamed = sorted(t for t in set(now) & set(held) if now[t].strip() != held[t])
        print("%s — 지금 %d개 · 파일 %d개 · 새로 생김 %d · 없어짐 %d · 이름 바뀜 %d"
              % (fname, len(now), len(held), len(added), len(gone), len(renamed)))
        for t in added[:30]:
            print("  + %s %s" % (t, now[t]))
        for t in gone[:30]:
            print("  - %s %s" % (t, held[t]))
        for t in renamed[:30]:
            print("  ~ %s %s → %s" % (t, held[t], now[t]))
        if added or gone or renamed:
            changed = True
            if a.고치기:
                guard(fname, len(now), len(held))
                print("  목록을 새로 썼습니다:", write_list(fname, title, live, top_name))
    if changed and not a.고치기:
        print("★목록이 달라졌습니다. `대조 --고치기` 로 파일을 새로 쓰고, 사용자에게 무엇이 바뀌었는지 알리십시오(SKILL 「스킬 스스로 고치기」).")
    elif not changed:
        print("목록이 지금 KOSIS 와 같습니다.")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("search", help="통계표를 낱말로 찾는다(KOSIS 전체)")
    s.add_argument("말")
    s.add_argument("--개수", default="10")
    s.add_argument("--건너뛰기", default="0")

    l = sub.add_parser("list", help="가지 아래를 훑는다")
    l.add_argument("가지", help="예: 133_13301_200 (국세통계 최근분)")

    d = sub.add_parser("data", help="통계표 자료를 받는다")
    d.add_argument("기관", help="기관번호 — 국세청은 133")
    d.add_argument("표", help="표번호 — 예: TX_13301_A056")
    d.add_argument("--항목", default="ALL", dest="항목")
    d.add_argument("--분류1", default="ALL")
    d.add_argument("--분류더", nargs="*", default=[], help="분류2·3… 을 차례로")
    d.add_argument("--주기", default="Y", help="Y 해 · Q 분기 · M 달")
    d.add_argument("--최근", default="5", help="최근 몇 기간")
    d.add_argument("--기간", nargs=2, metavar=("시작", "끝"))
    d.add_argument("--csv")

    c = sub.add_parser("대조", help="국세통계 목록 파일을 지금 KOSIS 목록과 맞춰 본다")
    c.add_argument("--고치기", action="store_true", help="달라졌으면 목록 파일을 새로 쓴다")

    a = ap.parse_args()
    key = find_key("KOSIS_API_KEY", "kosis", "https://kosis.kr/openapi/serviceUse/serviceUseUnityReg_01Detail.do (로그인 뒤 활용신청)")
    try:
        {"search": cmd_search, "list": cmd_list, "data": cmd_data, "대조": cmd_check}[a.cmd](a, key)
    except Blocked as e:
        sys.exit(str(e))
    except RuntimeError as e:
        sys.exit("실패: %s" % e)


if __name__ == "__main__":
    main()
