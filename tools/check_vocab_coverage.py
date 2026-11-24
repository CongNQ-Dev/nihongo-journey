"""Kiểm tra độ phủ từ vựng của khoá so với danh sách từ vựng Minna no Nihongo Shokyu I & II.

    python3 -I tools/check_vocab_coverage.py            # mọi bài đã soạn
    python3 -I tools/check_vocab_coverage.py 31-35      # chỉ các bài này (số bài Minna)
    python3 -I tools/check_vocab_coverage.py --all      # tính cả tên hư cấu của sách
    python3 -I tools/check_vocab_coverage.py --show 0   # chỉ in tổng kết từng bài

Nguồn tham chiếu: bộ dữ liệu cộng đồng MinnaNoDS (github.com/vitto4/MinnaNoDS). Danh sách từ chọn lọc và
bản dịch của nó thuộc quyền 3A Corporation, nên script chỉ TẢI TẠM ĐỂ ĐỐI CHIẾU, không lưu vào repo
và không chép nghĩa của nó vào bài học. Cần mạng tới raw.githubusercontent.com và gói PyYAML.

Quy ước: một từ của sách coi là "có" khi kana (hoặc kanji) của nó xuất hiện trong bảng từ vựng có ảnh
(minna_vocab.py) hoặc bảng từ chức năng / câu cố định (LESSONS[..]["words"]) CỦA ĐÚNG BÀI đó.
"Ở bài khác" = có trong khoá nhưng nằm sai bài. Thoát mã 1 nếu còn từ thiếu, để dùng làm cổng kiểm.
"""
import os, re, sys, tempfile, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
URL = "https://raw.githubusercontent.com/vitto4/MinnaNoDS/main/minna-no-ds.yaml"


def load_reference():
    import yaml
    path = os.path.join(tempfile.gettempdir(), "minna-no-ds.yaml")
    if not os.path.exists(path):
        urllib.request.urlretrieve(URL, path)
    return yaml.safe_load(open(path, encoding="utf-8"))


def variants(s):
    """Các dạng chuẩn hoá của một mục: bỏ dấu ～ － khoảng trắng; ngoặc [..] hoặc bỏ cả nội dung, hoặc chỉ bỏ ký hiệu."""
    s = s or ""
    out = set()
    drop = re.sub(r"[\[\(（［].*?[\]\)）］]", "", s)
    keep = re.sub(r"[\[\]\(\)（）［］]", "", s)
    for t in (drop, keep):
        t = re.sub(r"[～〜~－\-‐・\s　、。，．！？!?「」『』]", "", t)
        if t:
            out.add(t)
    return out


def course_index():
    from minna_data import LESSONS
    from minna_vocab import VOCAB
    by = {}
    for n, L in LESSONS.items():
        st = by.setdefault(L["minna"], set())
        for w in L["words"]:
            for part in re.split(r"[／/]", w[0]) + re.split(r"[／/]", w[1] or ""):
                st |= variants(part)
            st |= variants(w[0])
    for v in VOCAB:
        st = by.setdefault(v[0] - 11, set())
        st |= variants(v[1]) | variants(v[2])
    return by


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    show = 10 ** 9
    if "--show" in sys.argv:
        show = int(sys.argv[sys.argv.index("--show") + 1]); args = [a for a in args if a != str(show)]
    include_fic = "--all" in sys.argv
    ds = load_reference()
    by = course_index()
    made = sorted(by)
    lo, hi = min(made), max(made)
    if args:
        a, _, b = args[0].partition("-"); lo, hi = int(a), int(b or a)
    anywhere = set().union(*by.values())
    tot = have = 0; miss_all = 0
    for m in range(lo, hi + 1):
        key = "lesson-%02d" % m
        if key not in ds or m not in by:
            continue
        mine = by[m]; miss = []; moved = []; n = 0
        for w in ds[key]:
            if not include_fic and "fictitious" in (w["meaning"].get("en") or ""):
                continue
            n += 1
            cand = variants(w["kana"]) | variants(w.get("kanji"))
            if cand & mine:
                continue
            (moved if cand & anywhere else miss).append(w)
        tot += n; have += n - len(miss) - len(moved); miss_all += len(miss) + len(moved)
        print(f"bài {m:2d}: sách {n:3d} từ | đủ {n - len(miss) - len(moved):3d} | thiếu hẳn {len(miss):3d} | sai bài {len(moved):2d}")
        for tag, lst in (("THIẾU", miss), ("SAI BÀI", moved)):
            for w in lst[:show]:
                print(f"    {tag}: {w['kana']}  {w.get('kanji') or ''}  ({(w['meaning'].get('en') or '')[:50]})")
    print(f"TỔNG: {tot} từ, đủ {have}, còn thiếu hoặc sai bài {miss_all}")
    sys.exit(1 if miss_all else 0)


if __name__ == "__main__":
    main()
