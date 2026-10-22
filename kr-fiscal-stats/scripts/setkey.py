"""인증키 넣는 창 — 명령줄·json 을 몰라도 키를 넣게 한다.

  python3 scripts/setkey.py lofin        (윈도우는 python)
  자료원: lofin · openfiscal · kosis · ecos · ggdream

창 하나에 «발급 받으러 가기» 단추, 키 붙여넣기 칸(가려서 보임), 저장 단추가 있다.
저장하면 홈 폴더의 ~/.<이름>_key 에 키만 한 줄 쓴다 — 스크립트들이 찾는 그 자리다(common.find_key).

★키 값은 어디에도 찍지 않는다. 표준출력에는 «저장했습니다: ~/.lofin_key» 한 줄만 낸다.
★창을 못 띄우는 자리(tkinter 가 없음·화면이 없음)에서는 그렇다고만 알리고 멈춘다.
  대화창에 키를 붙여 넣으라고 안내하지 않는다 — 그 대화 기록에 키가 남는다.

종료코드: 0 저장함 · 1 저장 안 하고 닫음 · 2 자료원 이름이 틀림 · 3 창을 못 띄움 · 4 파일을 못 씀
표준 라이브러리만 쓴다(설치할 것 없음).
"""
import os
import sys
import webbrowser

# ★윈도우 콘솔은 기본이 cp949 라 한글이 깨진다 — common.py 와 같은 처리
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8")

# 이름 → (보이는 이름, 환경변수, 발급 주소). 주소는 설치와-사용.md 「1) 인증키 받기」 표 그대로다.
# ★지방재정365 는 메뉴를 스크립트로 그려서 바로 가는 주소가 없다 — 첫 화면으로 보내고 메뉴를 적어 준다.
SOURCES = {
    "lofin": ("지방재정365", "LOFIN_API_KEY", "https://www.lofin365.go.kr",
              "회원가입·로그인 → 위 메뉴 「재정데이터개방」 → 인증키 신청"),
    "openfiscal": ("열린재정", "OPENFISCAL_API_KEY", "https://www.openfiscaldata.go.kr/op/ko/ds/UOPKODSA01.do",
                   "로그인 뒤 인증키 발급"),
    "kosis": ("KOSIS 국가통계포털", "KOSIS_API_KEY", "https://kosis.kr/openapi/serviceUse/serviceUseUnityReg_01Detail.do",
              "로그인 뒤 활용신청"),
    "ecos": ("한국은행 ECOS", "ECOS_API_KEY", "https://ecos.bok.or.kr/api/#/AuthKeyApply",
             "회원가입·로그인 뒤 인증키 신청"),
    "ggdream": ("경기데이터드림", "GGDREAM_API_KEY", "https://data.gg.go.kr/portal/openapi/insertApikeyPage.do",
                "회원가입·로그인 뒤 인증키 발급"),
}


# ★가림 글자는 «*» — «•» 는 글꼴에 따라 이상한 글자로 그려졌다(리눅스 시험)
MASK = "*"


def key_path(name):
    return os.path.join(os.path.expanduser("~"), ".%s_key" % name)


def shown(path):
    """사람에게 보일 경로 — 홈은 ~ 로 줄인다(윈도우는 C:\\Users\\<이름> 그대로가 더 알기 쉬워 그대로 둔다)."""
    home = os.path.expanduser("~")
    if os.name != "nt" and path.startswith(home + os.sep):
        return "~" + path[len(home):]
    return path


def clean(raw):
    """붙여 넣은 글자를 키 한 줄로 — 앞뒤 빈칸·줄바꿈만 걷는다. 가운데 빈칸이 있으면 키가 아닌 것으로 본다."""
    v = (raw or "").strip()
    if not v or any(c.isspace() for c in v):
        return None
    return v


def save_key(name, value):
    """~/.<이름>_key 에 키만 한 줄. 맥·리눅스는 주인만 읽게(600). 옆 파일에 쓰고 바꿔 끼운다.

    ★쓰다가 오류가 나면 옆 파일을 지우고 옛 키 파일은 그대로 둔다. 강제 종료·전원 차단 때는 그 정리가 못 돌아
      `.<이름>_key.tmp-<번호>` 가 남을 수 있다(그 안에 키 전부나 일부) — 보이면 지우면 된다.
    """
    path = key_path(name)
    tmp = path + ".tmp-%d" % os.getpid()
    fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(value + "\n")
        os.replace(tmp, path)
    except BaseException:
        if os.path.exists(tmp):
            os.remove(tmp)
        raise
    if os.name != "nt":
        os.chmod(path, 0o600)
    return path


def no_window(why):
    print("이 자리에서는 창을 못 띄웁니다(%s)." % why, file=sys.stderr)
    print("키는 설치와-사용.md 「키 세팅」 절의 «그 밖에» 길로 넣어 주십시오. 키를 대화창에 붙여 넣지는 마십시오.", file=sys.stderr)
    sys.exit(3)


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in SOURCES:
        print("쓰는 법: python3 scripts/setkey.py <%s>" % "|".join(SOURCES), file=sys.stderr)
        sys.exit(2)
    name = sys.argv[1]
    title, env, url, how = SOURCES[name]
    try:
        import tkinter as tk
        from tkinter import font as tkfont, messagebox
    except ImportError:
        no_window("이 파이썬에 tkinter 가 없습니다")
    try:
        root = tk.Tk()
    except tk.TclError:
        no_window("화면이 없습니다")

    result = {"code": 1}
    root.title("%s 인증키 넣기" % title)
    root.resizable(False, False)
    pad = {"padx": 16, "pady": 4}

    # ★글꼴 이름을 «TkDefaultFont» 문자열로 주면 그 이름의 글꼴을 찾다가 한글이 없는 글꼴로 떨어진다(리눅스 시험에서 네모) —
    #   기본 글꼴을 복사해 크기만 키운다
    big = tkfont.nametofont("TkDefaultFont").copy()
    big.configure(size=14, weight="bold")
    tk.Label(root, text="%s 인증키 넣기" % title, font=big).pack(anchor="w", padx=16, pady=(14, 4))
    tk.Label(root, text="① 아래 단추로 발급 화면을 엽니다 — %s.\n② 받은 키를 복사해 칸에 붙여 넣고 «저장»을 누릅니다." % how,
             justify="left").pack(anchor="w", **pad)
    tk.Button(root, text="발급 받으러 가기", command=lambda: webbrowser.open(url)).pack(anchor="w", **pad)

    row = tk.Frame(root)
    row.pack(fill="x", padx=16, pady=(10, 4))
    var = tk.StringVar()
    entry = tk.Entry(row, textvariable=var, show=MASK, width=44)
    entry.pack(side="left", fill="x", expand=True)

    def paste():
        try:
            var.set(root.clipboard_get())
        except tk.TclError:
            messagebox.showinfo("붙여넣기", "복사해 둔 글자가 없습니다. 발급 화면에서 키를 먼저 복사해 주십시오.", parent=root)

    tk.Button(row, text="붙여넣기", command=paste).pack(side="left", padx=(6, 0))
    see = tk.BooleanVar(value=False)
    tk.Checkbutton(root, text="키 글자 보기", variable=see,
                   command=lambda: entry.config(show="" if see.get() else MASK)).pack(anchor="w", **pad)

    path = key_path(name)
    tk.Label(root, text="저장할 곳: %s" % shown(path), fg="#555").pack(anchor="w", **pad)
    if os.environ.get(env):
        # ★스크립트는 환경변수를 파일보다 먼저 본다 — 여기 저장해도 그 값이 계속 쓰인다는 것을 미리 알린다
        tk.Label(root, text="★환경변수 %s 가 이미 있어 그 값이 먼저 쓰입니다.\n  새 키를 쓰려면 그 환경변수를 지우거나 바꿔 주십시오." % env,
                 fg="#a33", justify="left").pack(anchor="w", **pad)

    def do_save():
        value = clean(var.get())
        if value is None:
            messagebox.showwarning("저장 안 함", "키가 비었거나 가운데에 빈칸이 있습니다. 키만 다시 붙여 넣어 주십시오.", parent=root)
            return
        if os.path.exists(path) and not messagebox.askyesno(
                "덮어쓸까요", "%s 에 키가 이미 있습니다. 새 키로 바꿀까요?" % shown(path), parent=root):
            return
        try:
            save_key(name, value)
        except OSError as e:
            messagebox.showerror("저장 못 함", "%s 에 쓰지 못했습니다(%s)." % (shown(path), e.strerror), parent=root)
            result["code"] = 4
            return
        result["code"] = 0
        messagebox.showinfo("저장했습니다", "저장했습니다: %s\n이제 클로드에게 다시 부탁하시면 됩니다." % shown(path), parent=root)
        root.destroy()

    btns = tk.Frame(root)
    btns.pack(fill="x", padx=16, pady=(10, 14))
    tk.Button(btns, text="저장", width=10, command=do_save).pack(side="right")
    tk.Button(btns, text="닫기", width=10, command=root.destroy).pack(side="right", padx=(0, 6))
    root.bind("<Return>", lambda _e: do_save())
    root.bind("<Escape>", lambda _e: root.destroy())
    entry.focus_set()
    root.mainloop()

    if result["code"] == 0:
        print("저장했습니다: %s" % shown(path))
    elif result["code"] == 4:
        print("저장하지 못했습니다: %s" % shown(path), file=sys.stderr)
    else:
        print("저장하지 않고 닫았습니다.", file=sys.stderr)
    sys.exit(result["code"])


if __name__ == "__main__":
    main()
