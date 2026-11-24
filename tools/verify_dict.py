"""Xác minh nội dung khoá học bằng từ điển mở của EDRDG (KANJIDIC2, JMdict; CC BY-SA 4.0) và ghi kết quả.

    python3 -I tools/verify_dict.py DIR [kanji|words|all]

DIR chứa kanjidic2.xml và JMdict_e (đã giải nén). Tải từ:
    https://www.edrdg.org/kanjidic/kanjidic2.xml.gz     https://www.edrdg.org/pub/Nihongo/JMdict_e.gz
Không lưu từ điển vào repo. Kết quả in ra màn hình; nội dung sai thì sửa ở tools/*.py rồi build lại.
"""
import os, re, sys, unicodedata
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


def kata2hira(s):
    return "".join(chr(ord(c) - 0x60) if "ァ" <= c <= "ヶ" else c for c in s)


def norm_kun(s):
    return kata2hira(re.sub(r"[-.・\s]", "", s))


def strip_tone(s):
    s = unicodedata.normalize("NFD", s.lower().replace("đ", "d"))
    return "".join(c for c in s if not unicodedata.combining(c))


def load_kanjidic(d):
    out = {}
    for ev, el in ET.iterparse(os.path.join(d, "kanjidic2.xml"), events=("end",)):
        if el.tag != "character":
            continue
        ch = el.findtext("literal")
        on, kun, viet, mean = set(), set(), [], []
        for r in el.iter("reading"):
            t = r.get("r_type")
            if t == "ja_on": on.add(kata2hira(r.text))
            elif t == "ja_kun": kun.add(norm_kun(r.text.split(".")[0] if False else r.text))
            elif t == "vietnam": viet.append(r.text)
        for m in el.iter("meaning"):
            if m.get("m_lang") in (None, "en"):
                mean.append(m.text)
        out[ch] = dict(on=on, kun=kun, viet=viet, mean=mean, strokes=el.findtext("misc/stroke_count"))
        el.clear()
    return out


def check_kanji(d):
    from kanji_data import KANJI
    kd = load_kanjidic(d)
    bad = 0
    for les, ch, on, kun, hv, mean, word, kana, ro, wmean in KANJI:
        e = kd.get(ch)
        if not e:
            print(f"[{les}] {ch}: KHÔNG có trong KANJIDIC2"); bad += 1; continue
        issues = []
        for x in [norm_kun(y) for y in re.split(r"[・,、]", on) if y]:
            if x and x not in {norm_kun(o) for o in e["on"]}:
                issues.append(f"On '{x}' ∉ {sorted(e['on'])}")
        for x in [norm_kun(y) for y in re.split(r"[・,、]", kun) if y]:
            kuns = {k.split('.')[0] if '.' in k else k for k in e["kun"]}
            kuns |= {re.sub(r"[-.]", "", k) for k in e["kun"]}
            if x and not any(x == norm_kun(k) or norm_kun(k).startswith(x) for k in e["kun"]):
                issues.append(f"Kun '{x}' ∉ {sorted(e['kun'])}")
        viets = {strip_tone(v) for v in e["viet"]}
        if hv and strip_tone(hv) not in viets:
            issues.append(f"Hán Việt '{hv}' ∉ {e['viet']}")
        if issues:
            bad += 1
            print(f"[{les}] {ch} (mình: {mean}) | từ điển: {', '.join(e['mean'][:4])}")
            for i in issues: print("     -", i)
    print(f"KANJI: {len(KANJI)} chữ, {bad} chữ có điểm lệch")


def load_jmdict(d):
    """Trả về (tập cặp (kana, kanji), tập kana) của JMdict_e."""
    pairs, rebs = set(), set()
    text = open(os.path.join(d, "JMdict_e"), encoding="utf-8").read()
    for m in re.finditer(r"<entry>(.*?)</entry>", text, re.S):
        blk = m.group(1)
        keb = re.findall(r"<keb>(.*?)</keb>", blk)
        reb = re.findall(r"<reb>(.*?)</reb>", blk)
        for r in reb:
            rebs.add(r)
            for k in keb:
                pairs.add((r, k))
    return pairs, rebs


_U = {"い": "う", "き": "く", "ぎ": "ぐ", "し": "す", "ち": "つ", "に": "ぬ", "び": "ぶ", "み": "む", "り": "る"}


def dict_forms(s):
    """Từ dạng ます/します/[な]... suy ra các dạng từ điển có thể."""
    s = re.sub(r"[\[［].*?[\]］]", "", s)
    s = re.sub(r"[（(].*?[）)]", "", s).strip()
    out = {s}
    if s.endswith("ます"):
        st = s[:-2]
        out.add(st + "る")                      # nhóm II
        if st and st[-1] in _U:
            out.add(st[:-1] + _U[st[-1]])        # nhóm I
        if st.endswith("い"):
            out.add(st[:-1] + "る")              # いらっしゃる, くださる...
        if s.endswith("します"):
            out |= {s[:-3] + "する", s[:-3]}
    elif s.endswith("です"):
        out |= {s[:-2], s[:-2] + "だ"}
    if s in ("きます", "来ます"):
        out |= {"くる", "来る"}
    for x in list(out):
        out.add(x.strip("－～-ー"))
        for suf in ("の", "に", "で"):
            if len(x) > 2 and x.endswith(suf):
                out.add(x[:-1])
        if len(x) > 2 and x.endswith("く"):
            out.add(x[:-1] + "い")
        if len(x) > 2 and x.endswith("て"):
            st = x[:-1]
            out |= {st + "る", st + "う", st + "く", st + "す", st + "つ"}
    for x in list(out):
        for pre in ("お", "ご"):
            if x.startswith(pre) and len(x) > 1:
                out.add(x[1:])
    return out


def check_words(d):
    from minna_vocab import VOCAB
    from minna_data import LESSONS
    pairs = {}
    for v in VOCAB:
        pairs[(v[1], v[2])] = ("VOCAB", v[0], v[4])
    for n, L in LESSONS.items():
        for w in L["words"]:
            if any(c in w[0] for c in "／～［。 "):
                continue
            pairs.setdefault((w[0], w[1]), ("words", n, w[3]))
    jp, jr = load_jmdict(d)
    miss = []
    for (kana, kanji), (src, n, vi) in sorted(pairs.items(), key=lambda x: x[1][1]):
        ok = False
        kfs = dict_forms(kana)
        if kanji:
            for kj in re.split(r"[、,]", kanji):
                for kf in dict_forms(kj.strip()):
                    if any((r, kf) in jp for r in kfs):
                        ok = True
        else:
            ok = any(r in jr for r in kfs)
        if not ok:
            miss.append((n, src, kana, kanji, vi))
    for n, src, kana, kanji, vi in miss:
        print(f"[{n}] {src}: {kana} {kanji} — không khớp JMdict (nghĩa Việt: {vi})")
    print(f"TỪ: {len(pairs)} mục, {len(miss)} mục không khớp JMdict")


if __name__ == "__main__":
    d = sys.argv[1]; what = sys.argv[2] if len(sys.argv) > 2 else "all"
    if what in ("kanji", "all"): check_kanji(d)
    if what in ("words", "all"): check_words(d)
