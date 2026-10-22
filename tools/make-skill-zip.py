"""claude.ai 에 올릴 스킬 ZIP 을 만든다 — 맨 위가 kr-fiscal-stats/SKILL.md 인 꼴.

  python3 tools/make-skill-zip.py                 → dist/kr-fiscal-stats.zip
  python3 tools/make-skill-zip.py --out <파일>     (윈도우는 python)

claude.ai 의 Customize → Skills → «+» → Upload a skill 은 ZIP 맨 위에 스킬 폴더가 하나 있어야 받는다.
GitHub «Download ZIP» 은 맨 위가 kr-fiscal-stats-main/ 이라 그대로는 안 맞는다 — 그래서 이 스크립트가 있다.

★키가 든 파일은 넣지 않는다. 숨은 파일(.<이름>_key 따위)·키 이름 꼴 파일·임시 파일·__pycache__ 는 빼고,
  스킬 폴더 안에 키 이름 꼴 파일이 있으면 ZIP 을 만들지 않고 멈춘다(스킬 폴더에 키를 두면 안 된다).
표준 라이브러리만 쓴다. 종료코드: 0 만듦 · 1 스킬 폴더 안에 키 꼴 파일이 있어 멈춤 · 2 쓰는 법이 틀림
"""
import argparse
import os
import re
import sys
import zipfile

for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL = "kr-fiscal-stats"
# 키 파일 꼴 — 스크립트가 읽는 ~/.<이름>_key, 그 임시 파일, 흔한 키 저장 이름
KEYLIKE = re.compile(r"(^\.?[a-z]+_key(\..*)?$)|(_key\.txt$)|(^\.env)", re.I)
SKIP_DIRS = {"__pycache__", ".git"}


def files(base):
    """(ZIP 안 경로, 실제 경로) 를 이름 순으로. 숨은 파일·임시 파일은 뺀다. 키 꼴 파일은 따로 모은다."""
    out, keylike = [], []
    for d, dirs, names in os.walk(base):
        dirs[:] = sorted(x for x in dirs if x not in SKIP_DIRS and not x.startswith("."))
        for n in sorted(names):
            p = os.path.join(d, n)
            rel = os.path.relpath(p, os.path.dirname(base)).replace(os.sep, "/")
            if KEYLIKE.search(n) or ".tmp-" in n:
                keylike.append(rel)
            elif n.startswith(".") or n.endswith((".pyc", "~")):
                continue
            else:
                out.append((rel, p))
    return out, keylike


def main():
    ap = argparse.ArgumentParser(description="claude.ai 에 올릴 스킬 ZIP 만들기")
    ap.add_argument("--out", default=os.path.join(ROOT, "dist", SKILL + ".zip"))
    a = ap.parse_args()
    base = os.path.join(ROOT, SKILL)
    if not os.path.isfile(os.path.join(base, "SKILL.md")):
        sys.exit("스킬 폴더를 못 찾았습니다: %s" % base)
    items, keylike = files(base)
    if keylike:
        # 이름만 알린다 — 안을 열지 않는다
        print("스킬 폴더 안에 키 파일로 보이는 것이 있어 ZIP 을 만들지 않았습니다:", file=sys.stderr)
        for r in keylike:
            print("  " + r, file=sys.stderr)
        print("스킬 폴더 밖(홈 폴더)으로 옮기거나 지운 뒤 다시 돌리십시오.", file=sys.stderr)
        sys.exit(1)
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    tmp = a.out + ".part"
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
        for rel, p in items:
            z.write(p, rel)
    os.replace(tmp, a.out)
    print("만들었습니다: %s (파일 %d개, 맨 위 %s/SKILL.md)" % (a.out, len(items), SKILL))


if __name__ == "__main__":
    main()
