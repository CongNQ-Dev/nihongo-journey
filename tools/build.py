"""Sinh bài học kana 0002–0011, bài Minna 0012+, bảng tra cứu, trang mục lục và assets/cards.js.

  python3 -I tools/build.py

Nội dung: tools/kana_data.py (kana), tools/minna_data.py + tools/minna_vocab.py (Minna);
ảnh đã chọn trong tools/images.json. Trang Minna sinh bởi tools/minna_pages.py.
Bài 0001 viết tay, không sinh lại.
"""
import html, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from kana_data import CARDS, LESSONS, EXTRA_ROWS  # noqa: E402
from fetch_images import card_id  # noqa: E402
import minna_pages  # noqa: E402
from minna_data import LESSONS as MINNA  # noqa: E402
from minna_vocab import VOCAB, vocab_id  # noqa: E402
from kanji_data import KANJI  # noqa: E402

IMAGES = json.load(open(os.path.join(ROOT, "tools", "images.json")))
STROKES = set()
_s = open(os.path.join(ROOT, "assets", "strokes.js"), encoding="utf-8").read()
STROKES = set(json.loads(_s[_s.index("{"):_s.rindex("}") + 1]).keys())

LESSON1 = [
    dict(id="h-a", lesson=1, type="kana", glyph="あ", sound="a", vn="như “a” tiếng Việt", word="あめ", romaji="ame", meaning="mưa", img="img/ame.jpg", credit="ThisParticularGreg · CC BY-SA 2.0"),
    dict(id="h-i", lesson=1, type="kana", glyph="い", sound="i", vn="như “i” tiếng Việt", word="いぬ", romaji="inu", meaning="con chó", img="img/inu.jpg", credit="Maja Dumat · CC BY 2.0"),
    dict(id="h-u", lesson=1, type="kana", glyph="う", sound="u", vn="gần “ư”, môi không chu tròn", word="うみ", romaji="umi", meaning="biển", img="img/umi.jpg", credit="Mokkie · CC BY-SA 3.0"),
    dict(id="h-e", lesson=1, type="kana", glyph="え", sound="e", vn="gần “ê” tiếng Việt", word="えき", romaji="eki", meaning="nhà ga", img="img/eki.jpg", credit="Alexandr3126 · CC BY-SA 4.0"),
    dict(id="h-o", lesson=1, type="kana", glyph="お", sound="o", vn="gần “ô” tiếng Việt", word="おにぎり", romaji="onigiri", meaning="cơm nắm", img="img/onigiri.jpg", credit="Ocdp · CC0"),
]
LESSON1_CREDITS = [
    ("ame.jpg", "People walking in the rain - historical kyoto photo 2007", "ThisParticularGreg", "CC BY-SA 2.0"),
    ("inu.jpg", "A Shiba Inu head", "Maja Dumat", "CC BY 2.0"),
    ("umi.jpg", "Okinawa beach 3", "Mokkie", "CC BY-SA 3.0"),
    ("eki.jpg", "Tokyo Station (Marunouchi Building)", "Alexandr3126", "CC BY-SA 4.0"),
    ("onigiri.jpg", "Onigiri 001", "Ocdp", "CC0"),
]

# ---------- bảng chữ ----------
ROWS = [  # (hàng, 5 ô theo a i u e o; "" = ô trống)
    ("あ", "あいうえお"), ("か", "かきくけこ"), ("さ", "さしすせそ"), ("た", "たちつてと"), ("な", "なにぬねの"),
    ("は", "はひふへほ"), ("ま", "まみむめも"), ("や", "や ゆ よ"), ("ら", "らりるれろ"), ("わ", "わ   を"),
]
DAK_ROWS = [("が", "がぎぐげご"), ("ざ", "ざじずぜぞ"), ("だ", "だぢづでど"), ("ば", "ばびぶべぼ"), ("ぱ", "ぱぴぷぺぽ")]
YOON_BASE = "きしちにひみりぎじびぴ"
RO = dict(zip(
    "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん"
    "がぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽ",
    "a i u e o ka ki ku ke ko sa shi su se so ta chi tsu te to na ni nu ne no ha hi fu he ho ma mi mu me mo "
    "ya yu yo ra ri ru re ro wa o n ga gi gu ge go za ji zu ze zo da ji zu de do ba bi bu be bo pa pi pu pe po".split()))
YOON_RO = dict(き="ky", し="sh", ち="ch", に="ny", ひ="hy", み="my", り="ry", ぎ="gy", じ="j", び="by", ぴ="py")
EXT = [("ティ", "ti"), ("ディ", "di"), ("トゥ", "tu"), ("ファ", "fa"), ("フィ", "fi"), ("フェ", "fe"), ("フォ", "fo"),
       ("ウィ", "wi"), ("ウェ", "we"), ("ウォ", "wo"), ("シェ", "she"), ("ジェ", "je"), ("チェ", "che"), ("ヴ", "vu")]


def kata(s):
    return "".join(chr(ord(ch) + 0x60) if "ぁ" <= ch <= "ゖ" else ch for ch in s)


def yoon_ro(base, small):
    v = {"ゃ": "a", "ゅ": "u", "ょ": "o"}[small]
    return YOON_RO[base] + v


def cell(g, r):
    if not g.strip():
        return "<td></td>"
    return f'<td data-say="{g}"><span class="jp">{g}</span><small>{r}</small></td>'


def grid(rows, k=False):
    out = ['<div class="table-wrap"><table class="grid-table"><tr><th></th><th>a</th><th>i</th><th>u</th><th>e</th><th>o</th></tr>']
    for head, cells in rows:
        tds = "".join(cell(kata(c) if k else c, RO.get(c, "")) for c in cells)
        out.append(f"<tr><th class=\"jp\">{kata(head) if k else head}</th>{tds}</tr>")
    out.append("</table></div>")
    return "\n".join(out)


def yoon_grid(k=False):
    out = ['<div class="table-wrap"><table class="grid-table"><tr><th></th><th>ゃ / ャ</th><th>ゅ / ュ</th><th>ょ / ョ</th></tr>']
    for b in YOON_BASE:
        tds = "".join(cell(kata(b + s) if k else b + s, yoon_ro(b, s)) for s in "ゃゅょ")
        out.append(f"<tr><th class=\"jp\">{kata(b) if k else b}</th>{tds}</tr>")
    out.append("</table></div>")
    return "\n".join(out)


def ext_grid():
    cells = "".join(f'<td data-say="{g}"><span class="jp">{g}</span><small>{r}</small></td>' for g, r in EXT)
    rows = [cells[i:i] for i in range(0)]  # placeholder (unused)
    tds = [f'<td data-say="{g}"><span class="jp">{g}</span><small>{r}</small></td>' for g, r in EXT]
    body = "".join("<tr>" + "".join(tds[i:i + 7]) + "</tr>" for i in range(0, len(tds), 7))
    return f'<div class="table-wrap"><table class="grid-table">{body}</table></div>'


# ---------- thẻ ----------
def all_cards():
    out = list(LESSON1)
    for c in CARDS:
        cid = card_id(c)
        im = IMAGES[cid]
        out.append(dict(id=cid, lesson=c[0], type="kana", glyph=c[1], sound=c[2], vn=c[3], word=c[4], romaji=c[5],
                        meaning=c[6], img=im["file"], credit=f'{im["artist"][:40]} · {im["license"]}'))
    missing = [vocab_id(v) for v in VOCAB if vocab_id(v) not in IMAGES]
    if missing:
        print("CHƯA CÓ ẢNH (bỏ qua thẻ):", " ".join(missing))
    out += minna_pages.vocab_cards(IMAGES)
    out += kanji_cards()
    return out


def kanji_id(ch):
    return f"kj-{ord(ch):x}"


def kanji_cards():
    """Thẻ kanji: không có ảnh (chữ to ở mặt trước). Id theo mã Unicode nên không đổi."""
    out = []
    for les, ch, on, kun, hv, mean, word, kana, ro, wmean in KANJI:
        yomi = " · ".join(x for x in (f"On: {on}" if on else "", f"Kun: {kun}" if kun else "") if x)
        out.append(dict(id=kanji_id(ch), lesson=les, type="kanji", glyph=ch, sound=yomi, vn=f"Hán Việt: {hv} — {mean}",
                        word=word, romaji=ro, meaning=wmean, say=kana))
    return out


def kanji_html():
    from html import escape as e
    groups = {}
    for k in KANJI:
        groups.setdefault(k[0], []).append(k)
    body = ["""<header class="lesson-head">
  <div class="kicker">Kanji · học song song với Minna</div>
  <h1>Kanji N5 theo từng bài Minna</h1>
  <p class="lede">Mỗi nhóm là các chữ xuất hiện trong từ vựng của bài Minna tương ứng. Với mỗi chữ: xem nét, tập viết, đọc ví dụ, rồi lật thẻ để vào lịch ôn hằng ngày. Người Việt có lợi thế: âm Hán Việt thường gần với âm On.</p>
</header>
<div class="note"><strong>Cách học gọn</strong> Mỗi ngày 3–5 chữ mới, không hơn. Học chữ nào thì đọc to từ ví dụ của chữ đó, không chỉ nhìn chữ.</div>"""]
    for les in sorted(groups):
        lf = LESSON_FILES.get(les)
        body.append(f'<h2 id="bai-{les}">Minna bài {les - 11} · bài {les:04d}</h2>')
        if lf:
            body.append(f'<p class="hint"><a href="lessons/{lf[0]}.html">Mở bài học {les:04d}</a></p>')
        for les_, ch, on, kun, hv, mean, word, kana, ro, wmean in groups[les]:
            body.append(f"""<div class="kanji-item"><div data-write="{ch}"></div>
<div><p class="jp" style="font-size:2rem;margin:0">{ch}</p>
<p><strong>{hv}</strong> — {e(mean)}</p>
<p class="hint">{("On: " + on) if on else ""}{" · " if on and kun else ""}{("Kun: " + kun) if kun else ""}</p>
<p><span class="jp">{word}</span> ({kana}, {ro}) — {e(wmean)} <button class="say" data-say="{kana}">nghe</button></p></div></div>""")
        body.append(f'<p><strong>Lật thẻ nhóm này</strong> (thẻ “nhớ rồi” sẽ vào lịch ôn):</p><div data-deck data-type="kanji" data-lesson="{les}"></div>')
    body.append('<p class="hint">Thứ tự nét: KanjiVG (CC BY-SA 3.0, kanjivg.tagaini.net). Còn thiếu nhiều chữ N5/N4 — nhóm mới được thêm cùng mỗi bài Minna.</p>')
    body.append('<nav class="next"><a href="index.html">Mục lục</a><a href="flashcards.html">Ôn hằng ngày</a><a href="practice.html">Luyện tự chọn</a></nav>')
    return page("Kanji theo bài Minna", "\n".join(body), base="")


def write_cards(cards):
    js = ("/* SINH TỰ ĐỘNG bởi tools/build.py — đừng sửa tay. Id không được đổi (tiến độ ôn lưu theo id).\n"
          "   Ảnh: Wikimedia Commons, xem img/CREDITS.md. */\nwindow.CARDS = "
          + json.dumps(cards, ensure_ascii=False, indent=1) + ";\n")
    open(os.path.join(ROOT, "assets", "cards.js"), "w", encoding="utf-8").write(js)
    rows = [f"| {f} | {t} | {a} | {l} |" for f, t, a, l in LESSON1_CREDITS]
    for cid in [card_id(c) for c in CARDS] + [vocab_id(v) for v in VOCAB if vocab_id(v) in IMAGES]:
        im = IMAGES[cid]
        rows.append(f'| {im["file"][4:]} | [{im["title"][5:]}]({im["page"]}) | {im["artist"]} | {im["license"]} |')
    md = ("# Ghi công ảnh (Wikimedia Commons)\n\nẢnh được thu nhỏ còn 960px. Sinh tự động bởi `tools/build.py`.\n\n"
          "| File | Ảnh gốc | Tác giả | Giấy phép |\n|---|---|---|---|\n" + "\n".join(rows) + "\n")
    open(os.path.join(ROOT, "assets", "img", "CREDITS.md"), "w", encoding="utf-8").write(md)


# ---------- trang ----------
def page(title, body, base="../"):
    return f"""<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="{base}assets/course.css?v=16">
</head>
<body>
<main>
{body}
</main>
<script src="{base}assets/cards.js?v=11"></script>
<script src="{base}assets/strokes.js"></script>
<script src="{base}assets/nihongo.js?v=16" data-base="{base}assets/"></script>
</body>
</html>
"""


LESSON_FILES = {1: ("0001-hiragana-a-i-u-e-o", "Năm nguyên âm", "あいうえお")}
for n, L in LESSONS.items():
    LESSON_FILES[n] = (L["slug"], L["title"], L["jp"])
for n, L in MINNA.items():
    LESSON_FILES[n] = (L["slug"], f'Minna {L["minna"]} · {L["title"]}', L["jp"])


def new_glyphs(n):
    g = [c[1] for c in CARDS if c[0] == n] + [r[0] for r in EXTRA_ROWS.get(n, [])]
    return g


def is_basic(n):
    return "table" not in LESSONS[n]


def listen_set(n):
    if n == 1:
        return "あいうえお"
    L = LESSONS[n]
    if L.get("listen_new"):
        return L["listen_new"]
    return "".join(g for g in new_glyphs(n) if g not in "ヲを")


def section(num, title):
    return f'<h2><span class="n">{num:02d}</span>{title}</h2>'


def lesson_html(n):
    L = LESSONS[n]
    kata_lesson = n >= 8
    out = [f"""<header class="lesson-head">
  <div class="kicker">Bài {n:04d} · {'Katakana' if kata_lesson else 'Hiragana'} · khoảng 40 phút</div>
  <h1>{L['title']} <span class="jp">{L['jp']}</span></h1>
  <p class="lede">{L['lede']}</p>
</header>
<div class="win"><strong>Thành quả của bài này</strong>{L['win']}</div>"""]
    s = 1
    prev = listen_set(n - 1)
    out.append(section(s, "Ôn lại trước khi học"))
    out.append(f"""<p>Mở <a href="../flashcards.html">trang ôn flashcard</a> và làm hết thẻ đến hạn trước. Sau đó nghe 8 câu dưới đây — chữ của bài trước, để não phải gọi lại từ trí nhớ.</p>
<div data-listen="{prev}" data-rounds="8"></div>""")
    s += 1
    out.append(section(s, "Âm mới"))
    out.append(L["intro"])
    tbl = L.get("table")
    if tbl == "DAKUTEN":
        out.append("<p>Bấm vào ô bất kỳ để nghe.</p>" + grid(DAK_ROWS))
    elif tbl == "YOON":
        out.append("<p>Mười một chữ hàng い ghép với ゃ ゅ ょ nhỏ. Bấm ô để nghe.</p>" + yoon_grid())
    elif tbl == "KATA_EXT":
        out.append("<h3>゛ và ゜ — giống hệt hiragana</h3>" + grid(DAK_ROWS, k=True))
        out.append("<h3>Tổ hợp ghi âm ngoại lai</h3>" + ext_grid())
        out.append("<p>Âm ghép キャ, シュ, チョ… y như bài 0007 — xem <a href=\"../reference/katakana.html\">bảng katakana</a>.</p>")
    else:
        rows = [f'<tr><td><span class="jp">{c[1]}</span></td><td>{c[2]}</td><td>{c[3]}</td><td><span class="jp" style="font-size:1.1rem">{c[4]}</span> {c[6]}</td><td><button class="say" data-say="{c[1]}">nghe</button></td></tr>'
                for c in CARDS if c[0] == n]
        rows += [f'<tr><td><span class="jp">{g}</span></td><td>{r}</td><td>{v}</td><td>—</td><td><button class="say" data-say="{g}">nghe</button></td></tr>'
                 for g, r, v in EXTRA_ROWS.get(n, [])]
        out.append('<p>Nghe từng chữ 2–3 lần rồi nhại theo <strong>thành tiếng</strong>.</p><div class="table-wrap"><table><tr><th>Chữ</th><th>Romaji</th><th>Với người Việt</th><th>Từ trên thẻ</th><th>Nghe</th></tr>'
                   + "\n".join(rows) + "</table></div>")
    s += 1
    out.append(section(s, "Điểm cần nhớ"))
    out.append(L["notes"])
    s += 1
    out.append(section(s, "Flashcard"))
    out.append(f'<p>Nhìn chữ, <strong>đọc to trước</strong>, rồi mới lật. Mỗi thẻ gắn chữ với một ảnh thật — nhớ cảnh trong ảnh, nhớ luôn âm.</p>\n<div data-deck data-lesson="{n}"></div>')
    s += 1
    out.append(section(s, "Nghe — chọn đúng"))
    out.append(f'<p>10 câu, mục tiêu 9/10.</p>\n<div data-listen="{listen_set(n)}" data-rounds="10"></div>')
    s += 1
    wr = [g for g in (L.get("writers") or "".join(new_glyphs(n))) if g in STROKES]
    out.append(section(s, "Viết — đúng thứ tự nét"))
    out.append('<p>Bấm “Xem nét”, rồi tô đè bằng chuột hoặc ngón tay. Sau đó <strong>viết ra giấy mỗi chữ 5 lần</strong> — tay viết thật mới nhớ lâu.</p>\n<div class="writers">'
               + "".join(f'<div data-write="{g}"></div>' for g in wr) + "</div>")
    s += 1
    out.append(section(s, "Đọc và nói"))
    note = f'<p class="note">{L["read_note"]}</p>' if L.get("read_note") else ""
    out.append(f"""<p>Từ được xáo trộn. Đọc to <em>trước khi</em> gõ — máy sẽ đọc lại để bạn so.</p>{note}
<div data-read='{html.escape(json.dumps(L["read"], ensure_ascii=False), quote=True)}'></div>
<p>Nói: đọc to cả danh sách, rồi bấm từng từ để so: """
               + " · ".join(f'<button class="say jp" style="font-size:1rem" data-say="{w}">{w}</button>' for w, _, _ in L["read"]) + "</p>")
    s += 1
    out.append(section(s, "Kiểm tra nhanh"))
    for q, opts, ans, exp, jp in L["mc"]:
        cls = ' class="jp"' if jp else ""
        out.append(f'<div class="quiz" data-answer="{ans}" data-explain="{html.escape(exp, quote=True)}"><p class="q">{q}</p><div class="opts">'
                   + "".join(f"<button{cls}>{o}</button>" for o in opts) + "</div></div>")
    s += 1
    out.append(section(s, "Nhớ lại từ trí nhớ"))
    ref = "katakana" if kata_lesson else "hiragana"
    out.append('<div class="recall">Nghỉ 5 phút, rồi không nhìn màn hình:<ol>' + "".join(f"<li>{r}</li>" for r in L["recall"])
               + f'</ol>Tự chấm bằng <a href="../reference/{ref}.html">bảng {ref}</a>. Chỗ phải cố mới nhớ ra chính là chỗ đang được ghi vào trí nhớ dài hạn.</div>')
    s += 1
    t, u, d = L["primary"]
    out.append(section(s, "Nguồn nên đọc"))
    out.append(f'<p><a href="{u}">{t}</a> — {d}</p>')
    out.append('<div class="ask"><strong>Hỏi lại giáo viên</strong>Mình (Claude) là giáo viên của bạn. Chỗ nào chưa rõ — phát âm, nét chữ, muốn đổi ảnh thẻ — cứ hỏi trong phiên chat. Làm xong phần “Nhớ lại”, báo kết quả để mình ghi nhận tiến độ.</div>')
    p = LESSON_FILES.get(n - 1)
    nx = LESSON_FILES.get(n + 1)
    left = f'<a href="{p[0]}.html">← {n - 1:04d} · {p[1]}</a>' if p else '<a href="../index.html">← Mục lục</a>'
    right = f'<a href="{nx[0]}.html">{n + 1:04d} · {nx[1]} →</a>' if nx else '<span>Tiếp theo: Minna no Nihongo bài 1 (chưa soạn)</span>'
    out.append(f'<nav class="next">{left}<a href="../index.html">Mục lục</a>{right}</nav>')
    return page(f"{n:04d} · {L['title']}", "\n".join(out))


def reference(k):
    name = "katakana" if k else "hiragana"
    lessons = range(8, 12) if k else range(1, 8)
    links = " · ".join(f'<a href="../lessons/{LESSON_FILES[i][0]}.html">{i:04d}</a>' for i in lessons)
    body = [f"""<header class="lesson-head">
  <div class="kicker">Tra cứu · bấm ô để nghe</div>
  <h1>Bảng {name}</h1>
  <p class="lede">Toàn bộ {name} trên một trang. Bài học: {links}.</p>
</header>""",
            "<h2>46 chữ cơ bản</h2>", grid(ROWS, k=k),
            f'<p>Và <span class="jp" data-say="{kata("ん") if k else "ん"}">{kata("ん") if k else "ん"}</span> (n) — âm mũi, một nhịp riêng.</p>',
            "<h2>゛ (dakuten) và ゜ (handakuten)</h2>", grid(DAK_ROWS, k=k),
            "<p>じ = ぢ = ji; ず = づ = zu. Thường chỉ dùng じ, ず.</p>",
            "<h2>Âm ghép</h2>", yoon_grid(k=k)]
    if k:
        body += ["<h2>Tổ hợp ghi âm ngoại lai</h2>", ext_grid(),
                 """<h2>Cặp dễ lẫn</h2><div class="table-wrap"><table>
<tr><td><span class="jp">シ ツ</span></td><td>shi “nhìn lên” (chấm ngang, nét hất lên) · tsu “nhìn xuống” (chấm trên, nét kéo xuống)</td></tr>
<tr><td><span class="jp">ン ソ</span></td><td>n “nhìn lên” · so “nhìn xuống” — cùng quy tắc như シ/ツ</td></tr>
<tr><td><span class="jp">ス ヌ</span></td><td>ヌ có thêm nét chéo</td></tr>
<tr><td><span class="jp">ウ ワ フ</span></td><td>ウ có chấm; ワ không chấm; フ chỉ một nét</td></tr>
<tr><td><span class="jp">ル レ</span></td><td>ル hai nét · レ một nét</td></tr>
<tr><td><span class="jp">コ ユ</span></td><td>ユ có nét ngang dưới kéo dài</td></tr>
<tr><td><span class="jp">ア マ</span></td><td>ア có nét phẩy dọc dài hơn</td></tr>
</table></div>"""]
    else:
        body += ["""<h2>Cặp dễ lẫn</h2><div class="table-wrap"><table>
<tr><td><span class="jp">あ お</span></td><td>お có chấm rời góc trên phải</td></tr>
<tr><td><span class="jp">き さ</span></td><td>き hai gạch ngang · さ một</td></tr>
<tr><td><span class="jp">ぬ め</span></td><td>ぬ có vòng ở đuôi</td></tr>
<tr><td><span class="jp">る ろ</span></td><td>る có vòng ở đuôi</td></tr>
<tr><td><span class="jp">ね れ わ</span></td><td>cùng thân trái: ね cuộn vòng, れ hất ra, わ cong vào</td></tr>
<tr><td><span class="jp">は ほ ま</span></td><td>ほ = は + gạch trên; ま không có nét dọc trái</td></tr>
</table></div>"""]
    body.append("""<h2>Quy tắc</h2><ul>
<li>Mỗi chữ cỡ thường = một nhịp, dài đều nhau.</li>
<li>Chữ hàng い + ゃゅょ nhỏ = một nhịp (きゃ = kya). Viết to きや = hai nhịp.</li>
<li>っ / ッ nhỏ = dừng một nhịp, gấp đôi phụ âm sau (きって = kitte).</li>
<li>Trường âm: hiragana dùng nguyên âm (おかあさん, せんせい, とうきょう); katakana dùng ー (ケーキ).</li>
<li>Trợ từ: は đọc “wa”, へ đọc “e”, を đọc “o”.</li>
</ul>""")
    other = "hiragana" if k else "katakana"
    body.append(f'<nav class="next"><a href="../index.html">Mục lục</a><a href="{other}.html">Bảng {other}</a><a href="../flashcards.html">Ôn flashcard</a><a href="../practice.html">Luyện tự chọn</a></nav>')
    return page(f"Tra cứu · Bảng {name}", "\n".join(body))


def index_html():
    li = lambda rng: "".join(f'<li><span class="num">{n:04d}</span><a href="lessons/{f}.html">{t}</a><span class="jp">{jp}</span></li>'
                             for n, (f, t, jp) in sorted(LESSON_FILES.items()) if n in rng)
    items, minna = li(range(1, 12)), li(MINNA)
    body = f"""<header class="lesson-head">
  <div class="kicker">Tiếng Nhật · từ số 0 đến N2, rồi N1</div>
  <h1>Mục lục khoá học</h1>
  <p class="lede">Hôm nay có <span data-due-count>0</span> thẻ cần ôn. Ôn trước, học bài mới sau.</p>
</header>
<div data-progress></div>
<p class="actions"><a class="btn primary" href="flashcards.html" style="text-decoration:none">Ôn flashcard hôm nay</a> <a class="btn" href="practice.html" style="text-decoration:none">Luyện tự chọn</a> <a class="btn" href="kanji.html" style="text-decoration:none">Kanji</a> <a class="btn" href="notebook.html" style="text-decoration:none">Sổ tay viết</a></p>
<h2>Giai đoạn 0 · Bảng chữ cái</h2>
<ol class="lesson-list">{items}</ol>
<p>Học theo thứ tự, mỗi ngày tối đa một bài mới. Xong bài 0011 là đọc được Minna no Nihongo bài 1.</p>
<h2>Giai đoạn 1 · Minna no Nihongo sơ cấp I</h2>
<ol class="lesson-list">{minna}</ol>
<p>Mỗi bài Minna dài hơn bài kana (60–75 phút) — chia hai buổi nếu cần: buổi 1 từ vựng + ngữ pháp, buổi 2 luyện + sách + viết. Cần có sách Minna, bản dịch tiếng Việt và file nghe.</p>
<h2 id="tra-cuu">Tra cứu</h2>
<ul><li><a href="reference/hiragana.html">Bảng hiragana</a></li><li><a href="reference/katakana.html">Bảng katakana</a></li><li><a href="reference/minna-grammar.html">Ngữ pháp Minna</a></li><li><a href="reference/numbers-counters.html">Số, giờ, ngày</a></li><li><a href="reference/roadmap.html">Bản đồ N5 → N1</a></li></ul>
<h2 id="sao-luu">Sao lưu tiến độ</h2>
<div data-backup></div>
<p class="hint">Ảnh thẻ và thứ tự nét lấy từ nguồn mở: <a href="credits.html">xem ghi nguồn</a>.</p>"""
    return page("Mục lục khoá tiếng Nhật", body, base="")


def credits_html(cards):
    """Trang ghi nguồn ảnh (giấy phép CC yêu cầu ghi tác giả); thẻ flashcard không hiện dòng nguồn nữa."""
    from html import escape as e
    rows = []
    for c in cards:
        im = IMAGES.get(c["id"])
        if not im or not c.get("img"):
            continue
        label = (c["glyph"] + " · " + c["word"]) if c["type"] == "kana" else c["word"]
        rows.append(f'<tr><td class="jp">{e(label)}</td><td>{e(im["artist"])}</td><td>{e(im["license"])}</td>'
                    f'<td><a href="{e(im["page"])}" rel="noopener">nguồn</a></td></tr>')
    body = f"""<header class="lesson-head">
  <div class="kicker">Ghi nguồn</div>
  <h1>Nguồn ảnh</h1>
  <p class="lede">Ảnh trên thẻ lấy từ Wikimedia Commons theo giấy phép Creative Commons hoặc phạm vi công cộng. Để thẻ gọn, tên tác giả và giấy phép được ghi ở trang này.</p>
</header>
<div class="table-wrap"><table><thead><tr><th>Thẻ</th><th>Tác giả</th><th>Giấy phép</th><th></th></tr></thead><tbody>{"".join(rows)}</tbody></table></div>
<p class="hint">Thứ tự nét chữ: KanjiVG (CC BY-SA 3.0, kanjivg.tagaini.net).</p>
<nav class="next"><a href="index.html">Mục lục</a><a href="flashcards.html">Ôn hằng ngày</a><a href="practice.html">Luyện tự chọn</a></nav>"""
    return page("Nguồn ảnh", body, base="")


def write_sentence_data():
    """assets/sentences.js: từ vựng + mẫu ngữ pháp từng bài Minna, cho chế độ "Đặt câu" ở practice.html."""
    from minna_word_ex import WORD_EX
    data = {}
    for n, L in MINNA.items():
        words = [[v[1], v[3], v[4], v[6], v[7]] for v in VOCAB if v[0] == n and v[1]]
        for w, ex in zip(L["words"], WORD_EX.get(n, [])):
            if "／" in w[0] or "～" in w[0]:
                continue
            words.append([re.sub(r"\[.*?\]", "", w[0]), w[2], w[3], ex[0], ex[1]])
        data[n - 11] = dict(title=L["title"], words=words,
                            grammar=[[g[0], g[1], [list(e) for e in g[3]]] for g in L["grammar"]])
    js = ("/* SINH TỰ ĐỘNG bởi tools/build.py — đừng sửa tay. Dữ liệu cho chế độ Đặt câu (practice.html). */\n"
          "window.SENTENCES = " + json.dumps(data, ensure_ascii=False, indent=1) + ";\n"
          "window.LESSON_FILES = " + json.dumps({n: f[0] for n, f in LESSON_FILES.items()}, ensure_ascii=False) + ";\n")
    open(os.path.join(ROOT, "assets", "sentences.js"), "w", encoding="utf-8").write(js)


def write_pwa():
    """sw.js: lưu sẵn mọi trang + asset để học khi không có mạng (cần https hoặc localhost). Phiên bản = hash nội dung."""
    import hashlib
    files = []
    for d, _, fs in os.walk(ROOT):
        if any(x in d for x in (".git", "tools", "learning-records", "node_modules")):
            continue
        for f in sorted(fs):
            rel = os.path.relpath(os.path.join(d, f), ROOT).replace(os.sep, "/")
            if rel.endswith((".html", ".js", ".css", ".jpg", ".png", ".svg", ".webmanifest")) and rel != "sw.js":
                files.append(rel)
    files.sort()
    h = hashlib.sha1()
    for rel in files:
        h.update(rel.encode()); h.update(open(os.path.join(ROOT, rel), "rb").read())
    sw = f"""/* SINH TỰ ĐỘNG bởi tools/build.py — đừng sửa tay. */
const VER = "nihongo-{h.hexdigest()[:10]}", FILES = {json.dumps(files, ensure_ascii=False)};
self.addEventListener("install", e => {{
  e.waitUntil(caches.open(VER).then(c => Promise.all(FILES.map(f => c.add(f).catch(() => {{}})))).then(() => self.skipWaiting()));
}});
self.addEventListener("activate", e => {{
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== VER).map(k => caches.delete(k)))).then(() => self.clients.claim()));
}});
/* Ưu tiên bản đã lưu (chạy được khi mất mạng), đồng thời tải bản mới ngầm cho lần sau. */
self.addEventListener("fetch", e => {{
  if (e.request.method !== "GET" || new URL(e.request.url).origin !== location.origin) return;
  e.respondWith(caches.open(VER).then(c => c.match(e.request, {{ ignoreSearch: true }}).then(hit => {{
    const net = fetch(e.request).then(r => {{ if (r.ok) c.put(e.request, r.clone()); return r; }}).catch(() => hit);
    return hit || net;
  }})));
}});
"""
    open(os.path.join(ROOT, "sw.js"), "w", encoding="utf-8").write(sw)


def main():
    cards = all_cards()
    write_cards(cards)
    write_sentence_data()
    for n in LESSONS:
        open(os.path.join(ROOT, "lessons", LESSONS[n]["slug"] + ".html"), "w", encoding="utf-8").write(lesson_html(n))
    for k in (False, True):
        open(os.path.join(ROOT, "reference", ("katakana" if k else "hiragana") + ".html"), "w", encoding="utf-8").write(reference(k))
    for n in MINNA:
        open(os.path.join(ROOT, "lessons", MINNA[n]["slug"] + ".html"), "w", encoding="utf-8").write(minna_pages.lesson_html(n, LESSON_FILES, page))
    open(os.path.join(ROOT, "reference", "minna-grammar.html"), "w", encoding="utf-8").write(minna_pages.grammar_reference(page, LESSON_FILES))
    open(os.path.join(ROOT, "reference", "numbers-counters.html"), "w", encoding="utf-8").write(minna_pages.numbers_reference(page))
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(index_html())
    open(os.path.join(ROOT, "kanji.html"), "w", encoding="utf-8").write(kanji_html())
    open(os.path.join(ROOT, "credits.html"), "w", encoding="utf-8").write(credits_html(cards))
    write_pwa()
    print(f"{len(cards)} thẻ, {len(LESSONS) + len(MINNA)} bài, 4 bảng tra cứu, index.html")


if __name__ == "__main__":
    main()
