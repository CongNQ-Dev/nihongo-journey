"""Sinh trang cho giai đoạn Minna (bài 0012+), bảng ngữ pháp và bảng số đếm. Gọi từ tools/build.py."""
import html, json, random, re, zlib

from minna_data import LESSONS, C
from minna_vocab import VOCAB, vocab_id
from minna_word_ex import WORD_EX

J = lambda x: html.escape(json.dumps(x, ensure_ascii=False), quote=True)  # noqa: E731
E = lambda s: html.escape(s, quote=True)  # noqa: E731


HAVE_CARDS = set()   # số bài (file) đã có ít nhất một thẻ ảnh


def vocab_cards(images):
    out = []
    HAVE_CARDS.clear()
    for v in VOCAB:
        vid = vocab_id(v)
        im = images.get(vid)
        if not im:  # ảnh chưa duyệt / chưa tải → chưa có thẻ
            continue
        HAVE_CARDS.add(v[0])
        out.append(dict(id=vid, lesson=v[0], type="vocab", word=v[1], kanji=v[2], romaji=v[3], meaning=v[4],
                        ex=v[6], exvn=v[7], img=im["file"], credit=f'{im["artist"][:40]} · {im["license"]}'))
    return out


def section(num, title):
    return f'<h2><span class="n">{num:02d}</span>{title}</h2>'


def mix(key, opts, ans):
    """Xáo thứ tự đáp án — cố định theo câu hỏi (sinh lại không đổi), để vị trí đáp án đúng không lộ."""
    order = list(range(len(opts)))
    random.Random(zlib.crc32(key.encode())).shuffle(order)
    return [opts[i] for i in order], order.index(ans - 1) + 1


def mc_html(items):
    out = []
    for q, opts, ans, exp, jp in items:
        opts, ans = mix(q, opts, ans)
        cls = ' class="jp long"' if jp else ' class="vn"'
        out.append(f'<div class="quiz" data-answer="{ans}" data-explain="{E(exp)}"><p class="q">{q}</p><div class="opts">'
                   + "".join(f"<button{cls}>{o}</button>" for o in opts) + "</div></div>")
    return "\n".join(out)


def jp_cell(s):
    return f'<span class="jp">{s}</span>'


def lesson_html(n, files, page):
    L = LESSONS[n]
    m = L["minna"]
    vocab = [v for v in VOCAB if v[0] == n]
    out = [f"""<header class="lesson-head">
  <div class="kicker">Bài {n:04d} · Minna no Nihongo bài {m} · khoảng 60–75 phút, chia 2 buổi cũng được</div>
  <h1>{L['title']} <span class="jp">{L['jp']}</span></h1>
  <p class="lede">{L['lede']}</p>
</header>
<div class="win"><strong>Thành quả của bài này</strong>{L['win']}</div>"""]
    s = 1
    out.append(section(s, "Ôn lại trước khi học"))
    out.append('<p>Làm hết thẻ đến hạn ở <a href="../flashcards.html">trang ôn flashcard</a> trước. Rồi trả lời 3 câu này <strong>từ trí nhớ</strong> — đừng mở lại bài cũ.</p>')
    out.append(mc_html(L["review"]))

    s += 1
    out.append(section(s, "Từ vựng có ảnh"))
    out.append(f'<p>{len(vocab)} từ dưới đây' + (' có thẻ ảnh. ' if n in HAVE_CARDS else ' (thẻ ảnh sẽ được thêm sau). ') + 'Nghe, nhại theo <strong>thành tiếng</strong>, rồi học bằng thẻ: ảnh bị che cho tới khi bạn tự nói ra nghĩa.</p>')
    out.append('<p>Với mỗi từ: (1) bấm <strong>▶ từ + câu</strong> — máy đọc từ, dừng, rồi đọc câu ví dụ có từ đó; (2) nhại lại cả từ lẫn câu thành tiếng; (3) che cột nghĩa, đọc câu và tự dịch. Hoặc nghe cả danh sách một lượt.</p>')
    seq_all = [x for v in vocab for x in (v[1], v[6])]
    out.append(f'<p><button class="btn primary" data-say-seq="{J(seq_all)}">▶ Nghe cả danh sách (từ → câu)</button> <button class="btn" data-say-stop>Dừng</button></p>')
    rows = "".join(
        f'<tr><td>{jp_cell(v[1])}<br><small>{v[2] + " · " if v[2] else ""}{v[3]}</small></td><td>{v[4]}</td>'
        f'<td>{jp_cell(v[6])}<br><small>{v[7]}</small></td>'
        f'<td><button class="say" data-say="{v[1]}">từ</button><br><button class="say" data-say="{E(v[6])}">câu</button><br>'
        f'<button class="say" data-say-seq="{J([v[1], v[6]])}">từ + câu</button></td></tr>' for v in vocab)
    out.append(f'<div class="table-wrap"><table class="vocab-table"><tr><th>Từ</th><th>Nghĩa</th><th>Câu ví dụ</th><th>Nghe</th></tr>{rows}</table></div>')
    out.append('<h3>Nghe từ — chọn đúng</h3><p>Máy đọc một từ, bạn chọn từ vừa nghe. Mục tiêu 9/10.</p>'
               f'<div data-listen="{" ".join(v[1] for v in vocab)}" data-rounds="10"></div>')
    out.append('<h3>Thẻ ảnh</h3>')
    out.append(f'<div data-deck data-lesson="{n}"></div>' if n in HAVE_CARDS else '<div class="note"><strong>Chưa có thẻ ảnh</strong>Ảnh cho từ vựng bài này chưa được tải về, nên chưa có bộ thẻ. Học bằng bảng từ và phần luyện đọc / nghe ở trên; thẻ sẽ xuất hiện khi ảnh được thêm.</div>')
    out.append('<h3>Tự đặt câu</h3><p>Chọn 5 từ ở bảng trên, mỗi từ <strong>tự đặt một câu về chính bạn</strong> (dùng ngữ pháp đã học), viết ra giấy rồi đọc to. Gửi giáo viên trong phiên chat để được sửa.</p>')
    out.append('<h3>Từ chức năng và câu cố định (không có ảnh)</h3><p>Những từ này không chụp ảnh được — mỗi từ có một câu ví dụ để nghe và nhại theo, giống bảng trên.</p>')
    wex = WORD_EX[n]
    assert len(wex) == len(L["words"]), f"WORD_EX[{n}] lệch số dòng với words"
    say_word = lambda w: w.replace("～", "").replace("／", "、").strip()  # noqa: E731
    seq_w = [x for w, ex in zip(L["words"], wex) for x in (say_word(w[0]), ex[0])]
    out.append(f'<p><button class="btn primary" data-say-seq="{J(seq_w)}">▶ Nghe cả danh sách (từ → câu)</button> <button class="btn" data-say-stop>Dừng</button></p>')
    rows = "".join(
        f'<tr><td>{jp_cell(w[0])}<br><small>{w[1] + " · " if w[1] else ""}{w[2]}</small></td><td>{w[3]}</td>'
        f'<td>{jp_cell(ex[0])}<br><small>{ex[1]}</small></td>'
        f'<td><button class="say" data-say="{E(say_word(w[0]))}">từ</button><br><button class="say" data-say="{E(ex[0])}">câu</button><br>'
        f'<button class="say" data-say-seq="{J([say_word(w[0]), ex[0]])}">từ + câu</button></td></tr>' for w, ex in zip(L["words"], wex))
    out.append(f'<div class="table-wrap"><table class="vocab-table"><tr><th>Từ</th><th>Nghĩa</th><th>Câu ví dụ</th><th>Nghe</th></tr>{rows}</table></div>')
    read = [[v[1], v[3], v[4]] for v in vocab] + [[re.sub(r"\[.*?\]", "", w[0]), w[2], w[3]] for w in L["words"] if "／" not in w[0] and "～" not in w[0]]
    out.append('<h3>Luyện đọc từ vựng</h3><p>Từ của bài được xáo trộn. <strong>Đọc to trước</strong>, rồi gõ cách đọc bằng romaji — máy đọc lại để bạn so phát âm. Mục tiêu: 90% trở lên. Làm lại vào hôm sau trước khi sang bài mới.</p>'
               f'<div data-read="{J(read)}"></div>')
    out.append('<p class="note"><strong>Kanji</strong>Cột kanji để bạn nhận mặt chữ khi đọc sách Minna (sách in kanji kèm furigana). Chưa cần nhớ cách viết — kanji sẽ có lộ trình riêng.</p>')

    s += 1
    out.append(section(s, "Ngữ pháp"))
    for pat, pvn, exp, exs in L["grammar"]:
        out.append(f'<div class="pattern"><span class="jp">{pat}</span><span class="vn">{pvn}</span></div>{exp}')
        if exs:
            out.append('<ul class="ex">' + "".join(
                f'<li>{jp_cell(j)} <button class="say" data-say="{E(j.lstrip("…"))}">nghe</button><span class="vn">{v}</span></li>' for j, v in exs) + "</ul>")

    s += 1
    out.append(section(s, "Luyện: chọn đúng"))
    out.append(mc_html(L["drill"]))

    s += 1
    out.append(section(s, "Luyện: ghép câu"))
    out.append('<p>Bấm các ô theo đúng thứ tự. Nói to câu trước khi bấm “Kiểm tra” — máy sẽ đọc lại để bạn so.</p>')
    out.append(f'<div data-build="{J(L["build"])}"></div>')

    s += 1
    out.append(section(s, "Nghe hiểu"))
    out.append('<p>Bấm nghe (bao nhiêu lần cũng được), <strong>không nhìn chữ</strong> — che dòng chữ Nhật bằng tay nếu cần — rồi chọn nghĩa.</p>')
    for jp, opts, ans in L["hear"]:
        opts, ans = mix(jp, opts, ans)
        out.append(f'<div class="quiz" data-answer="{ans}" data-explain="{E(jp)}"><p class="q"><button class="btn primary" data-say="{E(jp)}">▶ Nghe</button></p><div class="opts">'
                   + "".join(f'<button class="vn">{o}</button>' for o in opts) + "</div></div>")
    for k in L.get("num", []):
        name = dict(price="giá tiền", time="giờ", date="ngày tháng", count="số đếm và tuổi", floor="số tầng")[k]
        out.append(f'<h3>Nghe {name}</h3><div data-num="{k}" data-rounds="10"></div>')

    s += 1
    out.append(section(s, "Hội thoại"))
    out.append('<p>Một đoạn hội thoại tự soạn, chỉ dùng từ và ngữ pháp đến bài này. Nghe cả đoạn trước khi đọc nghĩa. Rồi bấm <strong>Nói đuổi</strong>: máy dừng sau mỗi câu, bạn nói lại y hệt — nhịp và ngữ điệu quan trọng hơn tốc độ.</p>')
    out.append(f'<div data-dialog="{J(L["dialog"])}"></div>')

    s += 1
    out.append(section(s, f"Với sách Minna bài {m}"))
    out.append(f"""<ol>
<li>Đọc phần 文型 và 例文 của bài {m} trong sách chính. Mỗi câu đọc to hai lần; câu nào không hiểu, tra trong <strong>bản dịch tiếng Việt</strong> bài {m}.</li>
<li>Nghe phần 会話 bài {m} trong file nghe của sách: lần 1 không nhìn chữ, lần 2 nhìn chữ, lần 3 nói đuổi.</li>
<li>Làm 練習 A (chia dạng) và 練習 B (ghép câu) — viết ra giấy.</li>
<li>Làm phần 問題 bài {m}, đặc biệt các câu nghe. Chấm bằng đáp án trong sách; câu sai đem hỏi giáo viên.</li>
</ol>""")

    s += 1
    out.append(section(s, "Viết tay"))
    out.append('<p>Viết <strong>ra giấy</strong> bằng hiragana / katakana, bằng câu thật về bạn. Viết xong mới mở câu mẫu để so.</p><ol>'
               + "".join(f"<li>{p}</li>" for p, _ in L["write"]) + "</ol>")
    out.append('<details class="answers"><summary>Xem câu mẫu</summary><ol>' + "".join(f"<li>{jp_cell(a)}</li>" for _, a in L["write"]) + "</ol></details>")
    out.append('<p>Chụp ảnh trang viết và gửi giáo viên trong phiên chat nếu muốn được sửa.</p>')

    s += 1
    out.append(section(s, "Nói"))
    out.append(f"<p>{L['speak']}</p>")

    s += 1
    out.append(section(s, "Kiểm tra nhanh"))
    out.append(mc_html(L["mc"]))

    s += 1
    out.append(section(s, "Nhớ lại từ trí nhớ"))
    out.append('<div class="recall">Nghỉ 5 phút, rồi không nhìn màn hình:<ol>' + "".join(f"<li>{r}</li>" for r in L["recall"])
               + '</ol>Tự chấm bằng bài này và <a href="../reference/minna-grammar.html">bảng ngữ pháp</a>. Chỗ phải cố mới nhớ ra chính là chỗ đang được ghi vào trí nhớ dài hạn.</div>')

    s += 1
    u, t, d = L["primary"]
    out.append(section(s, "Nguồn nên đọc"))
    out.append(f'<p><strong>Chính:</strong> phần giải thích ngữ pháp bài {m} trong <em>bản dịch & giải thích ngữ pháp tiếng Việt</em> của Minna no Nihongo I (3A Corporation) — bạn đã có sách. '
               f'<strong>Đọc thêm trực tuyến:</strong> <a href="{u}">{t}</a> — {d}</p>')
    used = sorted({k for k in C if C[k][0] in "".join(g[2] for g in L["grammar"])})
    if used:
        out.append('<ol class="sources">' + "".join(f'<li><a href="{C[k][0]}">{C[k][1]}</a></li>' for k in used) + "</ol>")
    out.append('<div class="ask"><strong>Hỏi lại giáo viên</strong>Mình (Claude) là giáo viên của bạn. Chỗ nào chưa rõ — trợ từ, ngữ điệu, câu trong sách, muốn đổi ảnh thẻ — cứ hỏi trong phiên chat. Làm xong phần “Nhớ lại”, báo kết quả để mình ghi nhận tiến độ.</div>')
    out.append(f'<p class="hint"><a href="../kanji.html#bai-{n}">Kanji của bài này →</a> · <a href="../practice.html">Luyện tự chọn: bốc từ vựng ngẫu nhiên →</a></p>')
    p, nx = files.get(n - 1), files.get(n + 1)
    left = f'<a href="{p[0]}.html">← {n - 1:04d} · {p[1]}</a>' if p else '<a href="../index.html">← Mục lục</a>'
    right = f'<a href="{nx[0]}.html">{n + 1:04d} · {nx[1]} →</a>' if nx else f'<span>Tiếp theo: Minna bài {m + 1} (chưa soạn)</span>'
    out.append(f'<nav class="next">{left}<a href="../index.html">Mục lục</a>{right}</nav>')
    return page(f"{n:04d} · Minna {m} · {L['title']}", "\n".join(out))


def grammar_reference(page, files):
    LAST = max(L["minna"] for L in LESSONS.values())
    body = [f"""<header class="lesson-head">
  <div class="kicker">Tra cứu · Minna no Nihongo bài 1–{LAST}</div>
  <h1>Bảng ngữ pháp sơ cấp</h1>
  <p class="lede">Mọi mẫu câu của bài 1–{LAST} trên một trang, kèm thuật ngữ và bảng trợ từ. Bấm câu ví dụ để nghe.</p>
</header>""", """<h2>Thuật ngữ dùng trong khoá</h2><div class="table-wrap"><table>
<tr><th>Thuật ngữ</th><th>Ký hiệu</th><th>Nghĩa trong khoá này</th></tr>
<tr><td>Danh từ</td><td>N</td><td>người, vật, nơi chốn, thời gian: がくせい, えき, あした</td></tr>
<tr><td>Động từ thể ます</td><td>V</td><td>thể lịch sự: たべます / たべません / たべました / たべませんでした</td></tr>
<tr><td>Tính từ い</td><td>い-adj</td><td>tận cùng bằng い, phủ định ～くない: たかい → たかくない</td></tr>
<tr><td>Tính từ な</td><td>な-adj</td><td>thêm な trước danh từ, phủ định như danh từ: しずかな まち</td></tr>
<tr><td>Trợ từ</td><td>—</td><td>chữ nhỏ đứng <em>sau</em> từ, cho biết vai trò của từ đó: は, を, に, で…</td></tr>
<tr><td>Chủ đề</td><td>は</td><td>điều câu đang nói tới (“còn về…”), không hẳn là chủ ngữ</td></tr>
<tr><td>Tân ngữ</td><td>を</td><td>thứ chịu tác động của động từ</td></tr>
<tr><td>Câu S</td><td>S</td><td>một mệnh đề trọn vẹn: S1 から、S2</td></tr>
</table></div>"""]
    body.append("""<h2>Trợ từ — chức năng đã học</h2><div class="table-wrap"><table>
<tr><th>Trợ từ</th><th>Chức năng</th><th>Ví dụ</th><th>Bài</th></tr>
<tr><td class="jp">は</td><td>chủ đề (đọc “wa”)</td><td class="jp">わたしは がくせいです</td><td>1</td></tr>
<tr><td class="jp">も</td><td>cũng</td><td class="jp">リンさんも がくせいです</td><td>1</td></tr>
<tr><td class="jp">の</td><td>của, thuộc, về, xuất xứ; vị trí</td><td class="jp">だいがくの がくせい・つくえの うえ</td><td>1–3, 10</td></tr>
<tr><td class="jp">か</td><td>câu hỏi; ～か、～か lựa chọn</td><td class="jp">がくせいですか</td><td>1–2</td></tr>
<tr><td class="jp">から／まで</td><td>từ / đến</td><td class="jp">くじから ごじまで</td><td>4</td></tr>
<tr><td class="jp">と</td><td>và (nối danh từ); cùng với; trích dẫn; hễ ~ thì</td><td class="jp">パンと たまご・ともだちと・～と おもいます</td><td>4–5, 21, 23</td></tr>
<tr><td class="jp">に</td><td>thời điểm; người nhận / người cho; nơi tồn tại</td><td class="jp">ろくじに・ははに・へやに</td><td>4, 7, 10</td></tr>
<tr><td class="jp">へ</td><td>hướng di chuyển (đọc “e”)</td><td class="jp">きょうとへ いきます</td><td>5</td></tr>
<tr><td class="jp">で</td><td>phương tiện; nơi hành động; công cụ, ngôn ngữ</td><td class="jp">でんしゃで・えきで・はしで</td><td>5–7</td></tr>
<tr><td class="jp">を</td><td>tân ngữ (đọc “o”)</td><td class="jp">パンを たべます</td><td>6</td></tr>
<tr><td class="jp">が</td><td>đối tượng của すき／わかる; chủ thể tồn tại; “nhưng” (sau câu)</td><td class="jp">りょうりが すき・いぬが います</td><td>8–10</td></tr>
<tr><td class="jp">や</td><td>liệt kê vài ví dụ (～など)</td><td class="jp">てがみや しゃしん</td><td>10</td></tr>
<tr><td class="jp">ね／よ</td><td>tìm đồng tình / báo điều mới</td><td class="jp">たいへんですね・いきますよ</td><td>4–5</td></tr>
</table></div>""")
    for n, L in sorted(LESSONS.items()):
        body.append(f'<h2>Bài {L["minna"]} · {L["title"]} <small>(<a href="../lessons/{files[n][0]}.html">{n:04d}</a>)</small></h2>')
        rows = []
        for pat, pvn, _, exs in L["grammar"]:
            ex = exs[0] if exs else ("", "")
            rows.append(f'<tr><td class="jp">{pat}</td><td>{pvn}</td><td>' + (f'<span class="jp" data-say="{E(ex[0])}">{ex[0]}</span><br><small>{ex[1]}</small>' if ex[0] else "") + "</td></tr>")
        body.append('<div class="table-wrap"><table>' + "".join(rows) + "</table></div>")
    body.append('<nav class="next"><a href="../index.html">Mục lục</a><a href="numbers-counters.html">Số, giờ, ngày</a><a href="../flashcards.html">Ôn flashcard</a></nav>')
    return page(f"Tra cứu · Ngữ pháp Minna 1–{LAST}", "\n".join(body))


def numbers_reference(page):
    D = ["ゼロ", "いち", "に", "さん", "よん", "ご", "ろく", "なな", "はち", "きゅう", "じゅう"]
    say = lambda s: f'<span class="jp" data-say="{s}">{s}</span>'  # noqa: E731
    t1 = "".join(f"<tr><td>{i}</td><td>{say(D[i])}</td></tr>" for i in range(11))
    big = [(100, "ひゃく"), (200, "にひゃく"), (300, "さんびゃく ★"), (400, "よんひゃく"), (500, "ごひゃく"), (600, "ろっぴゃく ★"),
           (700, "ななひゃく"), (800, "はっぴゃく ★"), (900, "きゅうひゃく"), (1000, "せん"), (3000, "さんぜん ★"), (8000, "はっせん ★"),
           (10000, "いちまん"), (100000, "じゅうまん")]
    t2 = "".join(f'<tr><td>{n:,}</td><td>{say(r.replace(" ★", ""))}{" ★" if "★" in r else ""}</td></tr>'.replace(",", ".") for n, r in big)
    hours = ["いちじ", "にじ", "さんじ", "よじ ★", "ごじ", "ろくじ", "しちじ ★", "はちじ", "くじ ★", "じゅうじ", "じゅういちじ", "じゅうにじ"]
    mins = ["いっぷん", "にふん", "さんぷん", "よんぷん", "ごふん", "ろっぷん", "ななふん", "はっぷん", "きゅうふん", "じゅっぷん"]
    t3 = "".join(f'<tr><td>{i + 1}</td><td>{say(h.replace(" ★", ""))}{" ★" if "★" in h else ""}</td><td>{say(mins[i]) if i < 10 else ""}</td></tr>' for i, h in enumerate(hours))
    months = ["いちがつ", "にがつ", "さんがつ", "しがつ ★", "ごがつ", "ろくがつ", "しちがつ ★", "はちがつ", "くがつ ★", "じゅうがつ", "じゅういちがつ", "じゅうにがつ"]
    days = {1: "ついたち", 2: "ふつか", 3: "みっか", 4: "よっか", 5: "いつか", 6: "むいか", 7: "なのか", 8: "ようか", 9: "ここのか", 10: "とおか",
            14: "じゅうよっか", 17: "じゅうしちにち", 19: "じゅうくにち", 20: "はつか", 24: "にじゅうよっか", 27: "にじゅうしちにち", 29: "にじゅうくにち"}
    special = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 20, 24}

    def dy(d):
        if d in days:
            return days[d]
        t, u = divmod(d, 10)
        return ("" if t == 1 else D[t]) + "じゅう" + (D[u] if u else "") + "にち"
    cells = [f'<td>{d}<br>{say(dy(d))}{" ★" if d in special else ""}</td>' for d in range(1, 32)]
    t5 = "".join("<tr>" + "".join(cells[i:i + 7]) + "</tr>" for i in range(0, 31, 7))
    t4 = "".join(f'<tr><td>{i + 1}</td><td>{say(m.replace(" ★", ""))}{" ★" if "★" in m else ""}</td></tr>' for i, m in enumerate(months))
    week = [("げつようび", "thứ Hai"), ("かようび", "thứ Ba"), ("すいようび", "thứ Tư"), ("もくようび", "thứ Năm"), ("きんようび", "thứ Sáu"), ("どようび", "thứ Bảy"), ("にちようび", "Chủ nhật")]
    t6 = "".join(f"<tr><td>{say(w)}</td><td>{v}</td></tr>" for w, v in week)
    floors = "いっかい にかい さんがい★ よんかい ごかい ろっかい★ ななかい はっかい★ きゅうかい じゅっかい★".split()
    t7 = "".join(f'<td>{i + 1}<br>{say(f.rstrip("★"))}{" ★" if "★" in f else ""}</td>' for i, f in enumerate(floors))
    body = f"""<header class="lesson-head">
  <div class="kicker">Tra cứu · Minna bài 1–5 · bấm chữ để nghe</div>
  <h1>Số, giờ, ngày</h1>
  <p class="lede">★ = cách đọc lệch, phải học thuộc. Luyện nghe có chấm điểm nằm trong bài <a href="../lessons/0014-minna-03-places-prices.html">0014</a> (giá tiền), <a href="../lessons/0015-minna-04-time-verbs.html">0015</a> (giờ), <a href="../lessons/0016-minna-05-going-coming.html">0016</a> (ngày).</p>
</header>
<h2>0 – 10</h2><div class="table-wrap"><table>{t1}</table></div>
<p>4 còn đọc し, 7 còn đọc しち, 9 còn đọc く — gặp lại trong giờ và tháng. Ghép số: 11 じゅういち, 20 にじゅう, 47 よんじゅうなな.</p>
<h2>Hàng trăm, nghìn, vạn</h2><div class="table-wrap"><table>{t2}</table></div>
<p>Tiếng Nhật nhóm số theo <strong>vạn</strong> (4 chữ số): 23.000 = にまん さんぜん; 150.000 = じゅうごまん.<sup class="cite"><a href="{C['num'][0]}">[Tae Kim]</a></sup></p>
<h2>Giờ và phút</h2><div class="table-wrap"><table><tr><th></th><th>giờ</th><th>phút</th></tr>{t3}</table></div>
<p>Phút 20, 30…: にじゅっぷん, さんじゅっぷん; 30 phút còn nói <span class="jp">はん</span>. Sáng / chiều: ごぜん／ごご đứng trước giờ.</p>
<h2>Thứ trong tuần</h2><div class="table-wrap"><table>{t6}</table></div>
<h2>Tháng</h2><div class="table-wrap"><table>{t4}</table></div>
<h2>Ngày trong tháng</h2><div class="table-wrap"><table class="grid-table">{t5}</table></div>
<h2>Tầng</h2><div class="table-wrap"><table class="grid-table"><tr>{t7}</tr></table></div>
<nav class="next"><a href="../index.html">Mục lục</a><a href="minna-grammar.html">Ngữ pháp Minna</a><a href="../flashcards.html">Ôn flashcard</a></nav>"""
    return page("Tra cứu · Số, giờ, ngày", body)
