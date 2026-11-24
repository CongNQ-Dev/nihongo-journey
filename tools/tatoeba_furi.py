"""Thêm furigana (ruby) cho các câu Tatoeba đã chọn trong tools/tatoeba_ex.json.

    python3 -I tools/tatoeba_furi.py DIR      # DIR chứa jpn_transcriptions.tsv (bunzip2 từ
        https://downloads.tatoeba.org/exports/per_language/jpn/jpn_transcriptions.tsv.bz2)

Furigana do Tatoeba tạo (bảng phiên âm Hrkt, định dạng [漢字|かんじ]); không có chuyên gia duyệt, nên đây là gợi ý đọc.
Chỉ lưu phần phiên âm của câu đã chọn vào trường "furi", KHÔNG lưu dữ liệu Tatoeba nguyên bản vào repo.
Câu chỉ được gắn furigana khi chữ sau khi bỏ ký hiệu trùng khớp 100% với câu đã chọn.
"""
import json, os, re, sys

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tatoeba_ex.json")
GROUP = re.compile(r"\[([^\]|]*)((?:\|[^\]|]*)*)\]")


def plain(t):
    return GROUP.sub(lambda m: m.group(1), t)


def main(d):
    tr = {}
    for line in open(os.path.join(d, "jpn_transcriptions.tsv"), encoding="utf-8"):
        a = line.rstrip("\n").split("\t")
        if len(a) >= 5 and a[2] == "Hrkt":
            tr.setdefault(a[0], a[4])
    data = json.load(open(PATH, encoding="utf-8"))
    ok = miss = 0
    for k, v in data.items():
        t = tr.get(v["id"])
        if t and plain(t).replace(" ", "") == v["jp"].replace(" ", ""):
            v["furi"] = t.replace(" ", ""); ok += 1
        else:
            v.pop("furi", None); miss += 1
    json.dump(data, open(PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=0, sort_keys=True)
    print("gắn furigana:", ok, "| không khớp:", miss)


if __name__ == "__main__":
    main(sys.argv[1])
