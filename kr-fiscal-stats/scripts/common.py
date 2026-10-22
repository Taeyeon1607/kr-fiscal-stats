"""다섯 자료원 스크립트가 함께 쓰는 것 — 표준 라이브러리만 쓴다(설치할 것 없음).

  인증키 찾기 · 부르기(막힌 도메인 알리기) · 「허브」 모양 응답 풀기 · 쪽 넘기기 · 묶어 더하기 · 저장

★키 값은 어디에도 찍지 않는다. 오류 문구에도 주소를 통째로 넣지 않는다(주소에 키가 들어 있다).
"""
import csv
import difflib
import json
import os
import socket
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

# ★윈도우 콘솔은 기본이 cp949 라 한글이 깨진다(2026-09-23 시험). 다섯 스크립트가 모두 이 파일을 불러오니 여기서 한 번 맞춘다.
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REFS = os.path.join(HERE, "..", "references")
# ★열린재정은 기본 표식으로 부르면 «오류 안내 화면»을 준다(2026-09-21 실측). 다섯 곳 모두 이 표식으로 부른다.
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/140.0 Safari/537.36")


_KEYS = []   # 찾은 키 — 상대가 되풀이한 본문을 오류 문구로 옮길 때 가리려고만 기억한다


def hide(text):
    """오류 문구에 옮길 상대 본문에서 키를 가린다(가로채는 중계기가 요청 주소를 본문에 되풀이할 수 있다)."""
    text = str(text)
    for k in _KEYS:
        text = text.replace(k, "<키>").replace(urllib.parse.quote(k, safe=""), "<키>")
    return text


def find_key(env, name, signup):
    """인증키를 찾는다: ①환경변수 ②~/.<name>_key. ★스킬 폴더 안은 찾지 않는다 — 키가 스킬에 들어가면 스킬과 함께 남에게 간다.
    클로드 코드(데스크탑의 코드 세션 포함)는 ~/.claude/settings.json 의 "env" 칸을 환경변수로 넘긴다 — 그 칸에 넣어도 ①로 잡힌다."""
    k = os.environ.get(env)
    if k:
        _KEYS.append(k.strip())
        return k.strip()
    p = os.path.expanduser("~/.%s_key" % name)
    if os.path.exists(p):
        with open(p, encoding="utf-8") as f:
            v = f.read().strip()
        if v:
            _KEYS.append(v)
            return v
    sys.exit(
        "인증키가 설정되어 있지 않습니다.\n"
        "  ★가장 쉬운 길 — 클로드에게 «%s 키 넣어 줘»라고 하면 키 넣는 창이 뜹니다(python3 scripts/setkey.py %s).\n"
        "  그 밖에 사용자가 직접 아래 둘 중 하나로 넣을 수도 있습니다.\n"
        "  1) 환경변수 %s 에 키를 넣는다 — 클로드 코드·데스크탑 코드 세션이면 ~/.claude/settings.json 의 \"env\" 칸에 넣고 새 세션을 연다\n"
        "  2) 홈 폴더에 파일 ~/.%s_key 를 만들고 키만 한 줄 넣는다\n"
        "  키 발급 = %s\n"
        "  ★키 값을 대화창에 붙여 넣지 마십시오. ★스킬 폴더 안에는 넣지 마십시오 — 스킬을 넘길 때 키가 따라갑니다."
        % (name, name, env, name, signup)
    )


class Blocked(RuntimeError):
    """상대 서버에 닿지 못했다 — 샌드박스의 도메인 허용 목록에 없을 때 가장 흔하다."""


def blocked_note(host, detail):
    return (
        "%s 에 닿지 못했습니다(%s).\n"
        "  ★Claude 데스크탑이라면 이 도메인이 «허용 목록»에 없는 것일 수 있습니다:\n"
        "    설정 → 기능 → 「외부 네트워크 접속 허용」 켜기 → 「추가 허용 도메인」에 %s 를 넣고 새 대화에서 다시 합니다.\n"
        "  (그 밖이면 상대 서버 장애이거나 인터넷 연결 문제입니다.)" % (host, detail, host)
    )


def fetch(url, data=None, headers=None, timeout=60):
    """본문을 글자로 돌려준다. HTTP 오류여도 본문이 있으면 돌려준다(오류가 본문에 담겨 오는 곳이 많다).
    아예 닿지 못하면 Blocked 를 던진다 — 도메인 이름을 붙여서."""
    host = urllib.parse.urlsplit(url).hostname or "?"
    req = urllib.request.Request(url, data=data, headers={"User-Agent": UA, **(headers or {})})
    last = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "replace")
            # 샌드박스의 중계기가 막으면 403 과 함께 «자료가 아닌» 짧은 글이 온다
            if e.code in (403, 407) and not body.lstrip().startswith(("{", "[")) and "<" not in body[:50]:
                raise Blocked(blocked_note(host, "HTTP %d %s" % (e.code, hide(body.strip())[:80])))
            return body
        except (urllib.error.URLError, socket.timeout, ConnectionError, OSError) as e:
            if isinstance(getattr(e, "reason", e), ssl.SSLCertVerificationError):
                # 닿기는 했다 — 허용 목록 문제가 아니다
                raise RuntimeError("%s 의 인증서를 확인하지 못했습니다. 허용 목록 문제가 아니라 이 컴퓨터의 인증서 저장소 문제입니다." % host)
            last = e
            if attempt < 2:
                time.sleep(2 * (attempt + 1))
    reason = getattr(last, "reason", last)
    raise Blocked(blocked_note(host, "%s" % reason))


def loads(body):
    """JSON 을 푼다. 겉이 한 번 더 문자열로 싸여 있으면 한 번 더 푼다(열린재정)."""
    d = json.loads(body)
    if isinstance(d, str):
        d = json.loads(d)
    return d


def hub_call(base, name, key, page=1, size=100, key_param="Key", **filters):
    """지방재정365·열린재정·경기데이터드림이 같이 쓰는 모양 — 한 쪽을 받아 (총건수, 행목록).

    성공 = {"자료이름": [{"head": [{"list_total_count": N}, {"RESULT": {...}}]}, {"row": [...]}]}
    실패·빈결과 = {"RESULT": {...}} 또는 {"RESULT": [{...}]} — ★모양이 다르다. HTTP 는 늘 200·201 이다."""
    q = {key_param: key, "Type": "json", "pIndex": page, "pSize": size}
    q.update({k: v for k, v in filters.items() if v not in (None, "")})
    body = fetch("%s/%s?%s" % (base, name, urllib.parse.urlencode(q)))
    if body.lstrip().startswith("<"):
        raise RuntimeError("자료 대신 «안내 화면(HTML)»이 왔습니다. 이름 오타이거나 상대 쪽 장애입니다.")
    try:
        d = loads(body)
    except ValueError:
        raise RuntimeError("응답을 읽을 수 없습니다(앞 120자): %s" % hide(body)[:120])
    if "RESULT" in d:
        r0 = d["RESULT"]
        r0 = r0[0] if isinstance(r0, list) else r0
        code = r0.get("CODE")
        msg = str(r0.get("MESSAGE", "")).replace("\\n", "\n").split("\n")[0].strip('"')
        if code == "INFO-200":          # 해당 자료 없음 = 오류가 아니다
            return 0, []
        raise RuntimeError("%s %s" % (code, msg))
    top = next(iter(d))
    head = d[top][0]["head"]
    total = head[0]["list_total_count"]
    res = head[1]["RESULT"]
    if res.get("CODE") != "INFO-000":
        raise RuntimeError("%s %s" % (res.get("CODE"), res.get("MESSAGE", "")))
    rows = d[top][1]["row"] if len(d[top]) > 1 else []
    return total, rows


def fetch_all(call, size=1000):
    """call(page, size) → (총건수, 행목록) 을 쪽마다 불러 다 모은다. 쪽 사이에 0.3초 쉰다."""
    out, page = [], 1
    total, rows = call(page, size)
    out.extend(rows)
    if rows and len(rows) < min(size, total):
        # 한 쪽을 꽉 채우지 않았는데 총건수는 더 있다 — 상대가 조용히 잘랐다(경기데이터드림은 키가 없으면 5행)
        print("  ★첫 쪽이 %d행만 왔습니다(총 %d건, 쪽당 %d). 키·권한 문제로 잘렸을 수 있습니다." % (len(rows), total, size))
    while len(out) < total and rows:
        page += 1
        time.sleep(0.3)
        _, rows = call(page, size)
        out.extend(rows)
    return total, out


def take_filters(rest, known):
    """argparse 가 모르는 «--이름 값» 을 전부 거르개로. 옵션을 잘못 친 것(--cvs)이면 알린다."""
    filters, i = {}, 0
    while i < len(rest):
        if rest[i].startswith("--") and i + 1 < len(rest):
            filters[rest[i][2:]] = rest[i + 1]
            i += 2
        else:
            i += 1
    for k in filters:
        near = difflib.get_close_matches(k.lower(), known, 1, 0.6)
        if near:
            print("  ★「--%s」는 «--%s» 를 잘못 친 것 아닙니까? 거르개로 서버에 가고, 서버가 모르는 이름이면 조용히 무시됩니다."
                  % (k, near[0]))
    return filters


def summarize(rows, col, by, total=None):
    """칸(쉼표로 여럿이면 한 행에서 먼저 더한다)을 묶음별로 더해 보여 준다.
    ★원자료에 없는 수다 — 사용자에게 줄 때 «더한 값»이라고, 어느 칸을 더했는지 밝힌다."""
    if total is not None and len(rows) < total:
        sys.exit("합을 내지 않습니다 — 총 %d건 중 %d건만 받았습니다. 덜 받은 합은 틀린 수입니다. 다시 부르십시오."
                 % (total, len(rows)))
    keys = [k.strip() for k in (by or "").split(",") if k.strip()]
    cols = [c.strip() for c in col.split(",") if c.strip()]
    missing = [k for k in cols + keys if k not in rows[0]]
    if missing:
        sys.exit("그런 칸이 없습니다: %s — 칸 이름은 --peek 로 봅니다" % ", ".join(missing))
    sums, counts, skipped = {}, {}, 0
    for r in rows:
        try:
            v = sum(float(str(r.get(c)).replace(",", "")) for c in cols)
        except (TypeError, ValueError):
            skipped += 1
            continue
        g = tuple(str(r.get(k)) for k in keys)
        sums[g] = sums.get(g, 0.0) + v
        counts[g] = counts.get(g, 0) + 1
    num = lambda v: format(int(v), ",") if float(v).is_integer() else format(round(v, 3), ",")
    print("\n[스크립트가 더한 값 — 원자료에 없는 수] %s 을(를) %s 별로" % (" + ".join(cols), "·".join(keys) or "전체"))
    for g, v in sorted(sums.items(), key=lambda kv: -kv[1]):
        print("  %-30s %20s  (%d행)" % (" · ".join(g) or "전체", num(v), counts[g]))
    print("  합 %s  (%d행)" % (num(sum(sums.values())), sum(counts.values())))
    if skipped:
        print("  ★숫자가 아니어서 뺀 행 %d개" % skipped)
    print("  ★단위는 원자료 그대로다 — 단위를 확인하고 밝힌다")
    label = "합(%s)" % "+".join(cols)
    return [dict(zip(keys, g), **{label: int(v) if float(v).is_integer() else v, "행수": counts[g]}) for g, v in sorted(sums.items(), key=lambda kv: -kv[1])]


def save(rows, csv_path=None, json_path=None, show=5):
    if csv_path and rows:
        cols = []
        for r in rows:
            cols += [k for k in r if k not in cols]
        with open(csv_path, "w", newline="", encoding="utf-8-sig") as f:
            w = csv.DictWriter(f, fieldnames=cols)
            w.writeheader()
            w.writerows(rows)
        print("csv 저장:", csv_path)
    if json_path and rows:
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(rows, f, ensure_ascii=False, indent=2)
        print("json 저장:", json_path)
    if not csv_path and not json_path:
        for r in rows[:show]:
            print(json.dumps(r, ensure_ascii=False))
        if len(rows) > show:
            print("… 나머지 %d건 생략 (--csv 로 저장하십시오)" % (len(rows) - show))


def guard(what, new, old):
    """새로 받은 목록이 비었거나 옛 목록의 절반도 안 되면 쓰지 않고 멈춘다.
    ★사이트 모양이 바뀌면 스크립트가 아무것도 못 읽어 «0개»를 낸다 — 그것을 «대량으로 없어졌다»로 믿으면 목록을 지운다."""
    if new == 0 or (old and new < old / 2):
        sys.exit("★%s 를 쓰지 않았습니다 — 새로 받은 것 %d개, 지금 파일 %d개.\n"
                 "  사이트의 화면·응답 모양이 바뀌어 스크립트가 못 읽은 것일 가능성이 큽니다.\n"
                 "  목록을 손으로 고치지 말고, 이 결과를 그대로 사용자에게 [스킬 개선 제안]으로 알리십시오."
                 % (what, new, old))


# 목록 파일 머리의 출처 한 줄. 목록은 각 기관 사이트에서 받은 것이라 저작권은 그 기관에 있다 — 이 스킬의
#   MIT 허락에 들지 않는다(저장소 NOTICE). 생성기가 이 줄을 부르므로 «대조 --고치기»로 다시 써도 남는다.
SOURCES = {
    "lofin": "지방재정365(www.lofin365.go.kr)",
    "openfiscal": "열린재정(www.openfiscaldata.go.kr)",
    "kosis": "KOSIS 국가통계포털(kosis.kr) — 국세통계 표의 작성기관은 국세청",
    "ecos": "한국은행 경제통계시스템 ECOS(ecos.bok.or.kr)",
    "ggdream": "경기데이터드림(data.gg.go.kr), 경기도",
}


def source_line(key, day=None):
    """목록 파일 둘째 줄에 넣는 출처·수집일 — day 를 안 주면 오늘."""
    return ("> 출처: %s · 수집 %s · 저작권은 그 기관에 있고 이용 조건은 그 기관 약관을 따릅니다(저장소의 NOTICE)."
            % (SOURCES[key], day or time.strftime("%Y-%m-%d")))


def write_ref(fname, text):
    """레퍼런스 파일을 새로 쓴다. 스킬 폴더에 못 쓰는 자리(데스크탑)면 지금 폴더에 내고 그 경로를 돌려준다."""
    path = os.path.join(REFS, fname)
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        path = os.path.abspath(fname)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    return os.path.abspath(path)


def run_hub(base, env, keyname, signup, key_param="Key", meanings=None, example="자료이름"):
    """지방재정365·열린재정·경기데이터드림의 명령줄 — 셋 다 같은 모양이라 하나로 쓴다."""
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("name", help="자료 이름 (예: %s)" % example)
    ap.add_argument("--peek", action="store_true", help="1건만 받아 칸 이름(과 뜻)을 본다")
    ap.add_argument("--all", action="store_true", help="전체 쪽을 다 받는다")
    ap.add_argument("--page", type=int, default=1)
    ap.add_argument("--size", type=int, default=None)
    ap.add_argument("--csv", help="csv 로 저장할 경로")
    ap.add_argument("--json", dest="jsonout", help="json 으로 저장할 경로")
    ap.add_argument("--sum", help="이 칸을 더한다. 쉼표로 여럿 주면 한 행에서 먼저 더한다. 전체 쪽을 받는다")
    ap.add_argument("--by", help="이 칸(쉼표로 여럿)별로 묶어 더한다")
    args, rest = ap.parse_known_args()
    filters = take_filters(rest, ["csv", "json", "all", "peek", "page", "size", "sum", "by"])
    if filters:
        print("거르개:", " ".join("%s=%s" % kv for kv in sorted(filters.items())))
    if args.by and not args.sum:
        sys.exit("--by 는 --sum 과 함께 씁니다(무엇을 더할지 --sum 으로 줍니다)")
    key = find_key(env, keyname, signup)
    one = lambda page, size: hub_call(base, args.name, key, page, size, key_param, **filters)
    try:
        if args.peek:
            total, rows = one(1, 1)
            print("총 %d건" % total)
            if not rows:
                print("행이 없습니다 — 거르개를 확인하십시오.")
                return
            print("칸 이름:", list(rows[0].keys()))
            mean = meanings(args.name) if meanings else {}
            if mean:
                print("칸 뜻:")
                for k in rows[0]:
                    print("  %-28s %s" % (k, mean.get(k, "?")))
            print("첫 행:", json.dumps(rows[0], ensure_ascii=False)[:400])
            return
        if args.sum or args.all:
            total, rows = fetch_all(one, min(args.size or 1000, 1000))
        else:
            total, rows = one(args.page, min(args.size or 100, 1000))
    except Blocked as e:
        sys.exit(str(e))
    except RuntimeError as e:
        sys.exit("실패: %s" % e)
    print("총 %d건 / 받은 것 %d건" % (total, len(rows)))
    sums = summarize(rows, args.sum, args.by, total) if args.sum and rows else None
    save(rows, args.csv, args.jsonout)
    if sums and args.csv:
        # ★--csv 는 원자료를 담는다. 합은 따로 «…_합.csv» 로 낸다 — 둘을 섞으면 무엇이 원자료인지 모른다
        base, ext = os.path.splitext(args.csv)
        save(sums, base + "_합" + (ext or ".csv"))
