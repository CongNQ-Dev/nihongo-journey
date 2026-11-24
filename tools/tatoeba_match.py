"""Tìm câu ví dụ Tatoeba (CC BY 2.0 FR) cho từ vựng khoá học, chỉ nhận câu mà MỌI từ đều thuộc từ vựng/ngữ pháp đã học tới bài đó.

    python3 -I tools/tatoeba_match.py DIR [OUT.json]

DIR chứa jpn_sentences_detailed.tsv, jpn-eng_links.tsv, eng_sentences.tsv (giải nén từ
https://downloads.tatoeba.org/exports/per_language/...). Không lưu dữ liệu Tatoeba nguyên bản vào repo, chỉ lưu câu được chọn.
Bài số n ở đây là số tệp bài (Minna bài k = k + 11).
"""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from minna_vocab import VOCAB
from minna_data import LESSONS

MAXLEN = 22
# trợ từ / ngữ pháp: (bài tệp tối thiểu = Minna + 11)
FUNC = {
    12: "は の も か です ね よ これ それ あれ この その あの ここ そこ あそこ だれ なん なに いくつ いくら と",
    15: "を に で へ から まで ます ません ました ませんでした ましょう ませんか が",
    16: "ください が あります います",
    24: "たい ながら て で",
    25: "ている ていません ています",
    28: "ない ないで",
    31: "た",
}
ENDINGS_POLITE = ["ます", "ません", "ました", "ませんでした", "ましょう", "ませんか"]
PUNCT = set("。、！？!?,.　 「」…～〜")


def forms(kana, kanji):
    out = set()
    for s in (kana, kanji):
        for x in re.split(r"[／、,]", s or ""):
            x = re.sub(r"[\[［].*?[\]］]|[（(].*?[）)]", "", x).strip("－～-ー ")
            if x:
                out.add(x)
    return out


def build_known(n):
    known = {}
    def add(w, lo):
        known[w] = min(known.get(w, 99), lo)
    for lo, ws in FUNC.items():
        for w in ws.split():
            if lo <= n:
                add(w, lo)
    items = [(v[0], v[1], v[2]) for v in VOCAB] + [(m, w[0], w[1]) for m, L in LESSONS.items() for w in L["words"]]
    for m, kana, kanji in items:
        if m > n:
            continue
        for f in forms(kana, kanji):
            add(f, m)
            if f.endswith("ます") and len(f) > 2:
                st = f[:-2]
                for e in ENDINGS_POLITE:
                    add(st + e, m)
                if n >= 25:
                    add(st + "て", m)
                if n >= 31:
                    add(st + "た", m)
    return known


def covered(s, known):
    s = "".join(c for c in s if c not in PUNCT)
    if not s:
        return False
    ok = [False] * (len(s) + 1); ok[0] = True
    mx = max(map(len, known)) if known else 1
    for i in range(len(s)):
        if not ok[i]:
            continue
        for j in range(i + 1, min(len(s), i + mx) + 1):
            if s[i:j] in known:
                ok[j] = True
    return ok[len(s)]


def has_word(t, f, known):
    """f xuất hiện trong t như một từ riêng: phần trước và sau đều phân tách được bằng từ đã học."""
    t = "".join(c for c in t if c not in PUNCT)
    p = t.find(f)
    while p != -1:
        l, r = t[:p], t[p + len(f):]
        if (not l or covered(l, known)) and (not r or covered(r, known)):
            return True
        p = t.find(f, p + 1)
    return False


def load(d):
    jp = {}
    for line in open(os.path.join(d, "jpn_sentences_detailed.tsv"), encoding="utf-8"):
        p = line.rstrip("\n").split("\t")
        if len(p) >= 4 and p[3] != "\\N" and len(p[2]) <= MAXLEN:
            jp[p[0]] = (p[2], p[3])
    links = {}
    for line in open(os.path.join(d, "jpn-eng_links.tsv"), encoding="utf-8"):
        a, b = line.split()
        if a in jp:
            links.setdefault(a, []).append(b)
    need = {b for v in links.values() for b in v}
    en = {}
    for line in open(os.path.join(d, "eng_sentences.tsv"), encoding="utf-8"):
        p = line.rstrip("\n").split("\t")
        if p[0] in need:
            en[p[0]] = p[2]
    return jp, links, en


def main():
    d = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else None
    jp, links, en = load(d)
    cands = [(i, t, u, en[links[i][0]], links[i][0]) for i, (t, u) in jp.items() if i in links and links[i][0] in en]
    cands.sort(key=lambda c: len(c[1]))
    res, tot = {}, 0
    cache = {}
    items = [(v[0], v[1], v[2], "VOCAB") for v in VOCAB] + [(m, w[0], w[1], "words") for m, L in LESSONS.items() for w in L["words"]]
    for n, kana, kanji, src in sorted(items):
        tot += 1
        # từ có chữ Hán: chỉ khớp bằng chữ Hán, hoặc kana đủ dài (kana ngắn dễ trùng từ khác: さる, かみ...)
        fs = [f for f in forms(kana, kanji) if len(f) >= 2 and (not kanji or re.search(r"[一-龯]", f) or len(f) >= 4)]
        if not fs:
            continue
        known = cache.setdefault(n, build_known(n))
        for i, t, u, e, eid in cands:
            if any(has_word(t, f, known) for f in fs):
                res[f"{src}|{n}|{kana}"] = dict(jp=t, en=e, id=i, user=u)
                break
    print(f"{len(res)}/{tot} mục có câu Tatoeba đạt chuẩn")
    from collections import Counter
    print(sorted(Counter(int(k.split('|')[1]) for k in res).items()))
    if out:
        json.dump(res, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=0, sort_keys=True)


if __name__ == "__main__":
    main()
