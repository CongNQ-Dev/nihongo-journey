"""Sinh bảng đối chiếu từng bài Minna để người học so với cuốn Minna no Nihongo của mình.

    python3 -I tools/doi_chieu.py DIR        # DIR chứa JMdict_e đã giải nén (https://www.edrdg.org/pub/Nihongo/JMdict_e.gz)

Ghi reference/doi-chieu/bai-NN.md (NN = số bài Minna) và reference/doi-chieu/README.md.
Mỗi bảng có: từ, nghĩa tiếng Việt của khoá (tự soạn, CHƯA có nguồn), nghĩa tiếng Anh trích từ JMdict (EDRDG, CC BY-SA 4.0)
và cột trống để người học ghi kết quả đối chiếu với sách. Không chép nội dung sách vào repo.
Trạng thái đối chiếu của từng bài lưu ở tools/source_status.json (chỉ đổi khi người học xác nhận).
"""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from verify_dict import dict_forms
from minna_data import LESSONS
from minna_vocab import VOCAB

OUT = os.path.join(HERE, "..", "reference", "doi-chieu")
STATUS = os.path.join(HERE, "source_status.json")


def load_gloss(d):
    """(reb) -> list[(set(keb), gloss_str)]"""
    idx = {}
    text = open(os.path.join(d, "JMdict_e"), encoding="utf-8").read()
    for m in re.finditer(r"<entry>(.*?)</entry>", text, re.S):
        blk = m.group(1)
        keb = set(re.findall(r"<keb>(.*?)</keb>", blk))
        senses = re.findall(r"<sense>(.*?)</sense>", blk, re.S)
        gl = []
        for s in senses[:2]:
            g = re.findall(r"<gloss>(.*?)</gloss>", s)[:3]
            if g:
                gl.append(", ".join(g))
        if not gl:
            continue
        g = " / ".join(gl).replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
        for r in re.findall(r"<reb>(.*?)</reb>", blk):
            idx.setdefault(r, []).append((keb, g))
    return idx


def lookup(idx, kana, kanji):
    kana_forms = dict_forms(kana.split("／")[0])
    kanji_forms = dict_forms(kanji.split("／")[0]) if kanji else set()
    best = None
    for f in kana_forms | kanji_forms:
        for keb, g in idx.get(f, []):
            score = 2 if (kanji_forms & keb) else 1
            if best is None or score > best[0]:
                best = (score, g)
    return best[1] if best else ""


def esc(s):
    return (s or "").replace("|", "\\|").replace("\n", " ")


def main(d):
    idx = load_gloss(d)
    status = json.load(open(STATUS, encoding="utf-8")) if os.path.exists(STATUS) else {}
    os.makedirs(OUT, exist_ok=True)
    rows_idx = []
    for n in range(1, 51):
        L = next(v for v in LESSONS.values() if v["minna"] == n)
        rows = []
        for v in VOCAB:
            if v[0] - 11 == n:
                rows.append((v[1], v[2], v[4]))
        for w in L["words"]:
            rows.append((w[0], w[1], w[3]))
        md = [f"# Đối chiếu Minna bài {n}: {L['title']}", "",
              "Cách dùng: mở sách Minna bài này, so từng dòng. Ghi ✓ nếu khớp, hoặc ghi cách sửa vào cột cuối.",
              "Nghĩa tiếng Anh tra tự động nên có thể lệch nghĩa hoặc để trống (từ ghép, câu giao tiếp, tên riêng).", "",
              "## Mẫu câu của bài (khoá đang dạy)", ""]
        for g in L["grammar"]:
            md.append(f"- {g[0]} — {g[1]}")
        md += ["", "Đối chiếu mẫu câu với bảng Japan Foundation: xem NOTES.md. Ghi ✓ nếu sách có đủ các mẫu trên: ____", "",
               "## Từ vựng", "", "| # | Từ | Chữ Hán | Nghĩa VN | Nghĩa EN | Khớp sách? |", "|---|---|---|---|---|---|"]
        for i, (kana, kanji, vn) in enumerate(rows, 1):
            md.append(f"| {i} | {esc(kana)} | {esc(kanji)} | {esc(vn)} | {esc(lookup(idx, kana, kanji))} |  |")
        md += ["", f"Tổng: {len(rows)} từ.", ""]
        open(os.path.join(OUT, f"bai-{n:02d}.md"), "w", encoding="utf-8").write("\n".join(md))
        st = status.get(str(n), {})
        rows_idx.append(f"| {n} | [{L['title']}](bai-{n:02d}.md) | {len(rows)} | {st.get('verified') or 'chưa đối chiếu'} |")
    open(os.path.join(OUT, "README.md"), "w", encoding="utf-8").write(
        "# Bảng đối chiếu với giáo trình Minna no Nihongo\n\n"
        "Mỗi bài có một bảng để người học so với sách. Cột 'Trạng thái' lấy từ `tools/source_status.json`; "
        "chỉ ghi ngày khi người học đã đối chiếu xong bài đó.\n\n"
        "| Bài | Tên | Số từ | Trạng thái |\n|---|---|---|---|\n" + "\n".join(rows_idx) + "\n")
    print("đã ghi", len(rows_idx), "bảng vào", os.path.normpath(OUT))


if __name__ == "__main__":
    main(sys.argv[1])
