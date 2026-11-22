/* Component dùng chung. Nạp sau cards.js và strokes.js.
   <script src="../assets/nihongo.js" data-base="../assets/"></script>

   Nghe:        <button class="say" data-say="あめ">nghe</button>
   Flashcard:   <div data-deck data-lesson="1"></div>          (học: hiện mọi thẻ của bài)
                <div data-deck data-due></div>                 (ôn: chỉ thẻ đến hạn, che ảnh)
   Quiz nghe:   <div data-listen="あいうえお" data-rounds="10"></div>
   Quiz chọn:   <div class="quiz" data-answer="2" data-explain="..."><p class="q">…</p>
                  <div class="opts"><button>…</button>…</div></div>
   Tập viết:    <div data-write="あ"></div>
*/
(function () {
  const BASE = (document.currentScript && document.currentScript.dataset.base) || "assets/";
  const $ = (tag, cls, html) => { const e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; };

  /* ---------- Giọng đọc ---------- */
  let voice = null;
  function pickVoice() {
    const vs = speechSynthesis.getVoices().filter(v => v.lang.replace("_", "-").startsWith("ja"));
    voice = vs.find(v => /Kyoko|Google 日本語/.test(v.name)) || vs[0] || null;
  }
  if ("speechSynthesis" in window) { pickVoice(); speechSynthesis.onvoiceschanged = pickVoice; }
  function speak(text, onend, rate) {
    if (!("speechSynthesis" in window)) return alert("Trình duyệt này không có giọng đọc. Hãy mở bằng Chrome hoặc Safari.");
    speechSynthesis.cancel();
    // Bỏ ký hiệu chỉ để hiển thị: [な], （よい）, ～ ; … và ／ thành chỗ ngắt.
    text = String(text).replace(/\[[^\]]*\]|［[^］]*］|（[^）]*）|\([^)]*\)/g, "").replace(/[～〜]/g, "")
      .replace(/…/g, "、").replace(/／/g, "、").replace(/[＿_]+/g, "").replace(/^[、\s]+/, "");
    const u = new SpeechSynthesisUtterance(text);
    u.lang = "ja-JP"; if (voice) u.voice = voice; u.rate = rate || 0.8;
    if (onend) u.onend = onend;
    speechSynthesis.speak(u);
  }
  const shuffle = a => { for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  const esc = s => String(s).replace(/[&<>"']/g, ch => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[ch]));
  document.addEventListener("click", e => { const b = e.target.closest("[data-say]"); if (b) speak(b.dataset.say); });
  /* Đọc nối tiếp: <button data-say-seq='["えき","えきは あそこです。"]'> — dừng giữa các phần để nhại theo. */
  let seqRun = 0;
  function speakSeq(list, token) {
    if (!list.length || token !== seqRun) return;
    const [t, ...rest] = list;
    speak(t, () => setTimeout(() => speakSeq(rest, token), 700 + t.length * 180));
  }
  document.addEventListener("click", e => {
    const b = e.target.closest("[data-say-seq]");
    if (b) { try { speakSeq(JSON.parse(b.dataset.saySeq), ++seqRun); } catch {} }
    if (e.target.closest("[data-say-stop]")) { seqRun++; speechSynthesis.cancel(); }
  });

  /* ---------- Lịch ôn Leitner ---------- */
  const DAYS = [0, 1, 3, 7, 14, 30, 60, 120], DAY = 864e5, KEY = "nihongo-srs-v1", SKEY = "nihongo-stats-v1";
  const load = () => { try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch { return {}; } };
  const save = s => { try { localStorage.setItem(KEY, JSON.stringify(s)); } catch {} };
  const dayKey = t => { const d = new Date(t || Date.now()); return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0"); };
  const loadStats = () => { try { return JSON.parse(localStorage.getItem(SKEY)) || {}; } catch { return {}; } };
  function logStat(ok, fresh) {
    try { const s = loadStats(), k = dayKey(), r = s[k] || { ok: 0, bad: 0 }; ok ? r.ok++ : r.bad++; if (fresh) r.fresh = (r.fresh || 0) + 1; s[k] = r; localStorage.setItem(SKEY, JSON.stringify(s)); } catch {}
  }
  const NEW_MAX = 20;                                                  // gợi ý, không chặn cứng
  const newToday = () => (loadStats()[dayKey()] || {}).fresh || 0;
  function grade(id, ok) {
    const s = load(), cur = s[id] || { box: 0 }, fresh = !s[id];
    const box = ok ? Math.min(cur.box + 1, DAYS.length - 1) : 0;
    s[id] = { box, due: Date.now() + DAYS[box] * DAY, miss: (cur.miss || 0) + (ok ? 0 : 1) }; save(s); logStat(ok, fresh);
  }
  const isDue = id => { const c = load()[id]; return !!c && c.due <= Date.now(); };
  const isNew = id => !load()[id];

  /* ---------- Video khẩu hình ----------
     Mỗi mục: chars = các chữ kana dùng chung video này; id = mã YouTube (nhúng qua youtube-nocookie).
     Thêm hàng khác (か, さ…) bằng cách thêm một dòng vào VIDEOS. */
  const kata = t => t.replace(/[ぁ-ゖ]/g, ch => String.fromCharCode(ch.charCodeAt(0) + 0x60));
  const both = t => t + kata(t);
  const VIDEOS = [
    { chars: both("あいうえお"), id: "D6CtlZEpXQk", title: "Japanese Vowel Pronunciation (A I U E O)", by: "Hana Japanese" },
    { chars: both("たちつてとだぢづでどなにぬねのらりるれろ"), id: "UV1AGFOeCHU", title: "た行だ行な行ら行の発音 子音発音法", by: "日本語発音塾" },
  ];
  const videoFor = g => VIDEOS.find(v => [...v.chars].includes(g));
  function openVideo(v) {
    const m = $("div", "vid-modal", `<div class="vid-box" role="dialog" aria-label="Video khẩu hình">
      <button class="vid-x" aria-label="Đóng">×</button>
      <div class="vid-frame"><iframe src="https://www.youtube-nocookie.com/embed/${v.id}?rel=0&playsinline=1" title="${esc(v.title)}" allow="accelerometer; encrypted-media; picture-in-picture" allowfullscreen loading="lazy"></iframe></div>
      <p class="vid-cap">${esc(v.title)} · ${esc(v.by)} (YouTube)</p></div>`);
    const close = () => m.remove();
    m.addEventListener("click", e => { if (e.target === m || e.target.closest(".vid-x")) close(); });
    document.addEventListener("keydown", function k(e) { if (e.key === "Escape") { close(); document.removeEventListener("keydown", k); } });
    document.body.append(m);
  }
  document.addEventListener("click", e => { const b = e.target.closest("[data-video]"); if (b) { const v = VIDEOS.find(x => x.id === b.dataset.video); if (v) openVideo(v); } });

  /* ---------- Flashcard ---------- */
  /* Luyện tự do: Nihongo.deck(el, { cards: [...], onDone }) — không ghi vào lịch ôn. Thẻ kana không có ảnh vẫn chạy. */
  function deck(el, opt) {
    const practice = !!(opt && opt.cards), review = !practice && el.hasAttribute("data-due");
    let queue = practice ? opt.cards.slice() : (window.CARDS || []).filter(c => review ? isDue(c.id) : String(c.lesson) === el.dataset.lesson && (el.dataset.type ? c.type === el.dataset.type : c.type !== "kanji"));
    if (review || practice) shuffle(queue);
    const total = queue.length; let done = 0;
    const mode = practice ? (opt.graded ? "Ôn tập" : "Luyện tự chọn") : review ? "Ôn tập" : "Học mới";
    const mark = (c, ok) => { if (!practice || opt.graded) grade(c.id, ok); queue.shift(); if (ok) done++; else queue.push(c); show(); };
    el.classList.add("deck");
    function show() {
      el.innerHTML = "";
      if (!queue.length && practice) {
        const d = $("div", "deck-done", `Xong ${total} thẻ. ${opt.graded ? "Kết quả đã ghi vào lịch ôn." : "Luyện tự chọn không thay đổi lịch ôn hằng ngày."} <button class="btn primary" data-again>Làm lại lượt này</button>`);
        d.querySelector("[data-again]").onclick = () => deck(el, opt);
        el.append(d); if (opt.onDone) opt.onDone(); return;
      }
      if (!queue.length) {
        const fresh = (window.CARDS || []).filter(c => isNew(c.id)).length;
        el.append($("div", "deck-done", review && !total
          ? `Hôm nay không có thẻ nào đến hạn.${fresh ? ` Còn ${fresh} thẻ chưa học — mở bài học tương ứng để học lần đầu.` : ""}`
          : `Xong ${total} thẻ. Thẻ “nhớ rồi” sẽ quay lại sau 1, 3, 7, 14… ngày ở trang ôn tập.`));
        return;
      }
      const c = queue[0], vocab = c.type === "vocab", big = vocab ? c.word : c.glyph;
      el.append($("div", "deck-bar", `<span>Thẻ ${done + 1} / ${total}</span><span>${mode}${vocab ? " · từ vựng" : ""}${!practice && !review && newToday() >= NEW_MAX ? ` · <b>hôm nay đã ${newToday()} thẻ mới, nên dừng</b>` : ""}</span>`));
      /* Hai mặt xếp chồng trong cùng một ô lưới nên luôn cao bằng nhau; lật bằng xoay 3D. */
      const face = (cls, veil, body) => {
        const photo = c.img
          ? `<figure class="fc-photo${veil ? " veiled" : ""}" style="margin:0"><img src="${BASE}${c.img}" alt=""><div class="fc-glyph${[...big].length > 1 ? " long" : ""}">${big}</div></figure>`
          : `<figure class="fc-photo noimg" style="margin:0"><div class="fc-big jp">${big}</div></figure>`;
        return `<div class="fc ${cls}">${photo}<div class="fc-body">${body}</div></div>`;
      };
      const hl = !vocab && c.word ? c.word.replace(c.glyph, `<b>${c.glyph}</b>`) : "";
      const front = `<p class="fc-prompt">${vocab ? "Đọc to từ này, nói nghĩa tiếng Việt." : "Chữ này đọc là gì? Đọc to lên."}</p>
        <p class="fc-tap">Chạm vào thẻ để lật${vocab ? ` <button class="say" data-say="${c.word}">nghe</button>` : ""}</p>`;
      const back = (vocab
        ? `<p class="fc-answer"><span class="sound">${c.meaning}</span><span class="hint">${c.romaji}${c.kanji ? ` · <span class="jp">${c.kanji}</span>` : ""}</span>
            <button class="say" data-say="${c.word}">nghe lại</button></p>
          <p class="fc-word"><span class="jp">${c.ex}</span> <button class="say" data-say="${c.ex}">nghe câu</button><br><span class="hint">${c.exvn}</span></p>`
        : `<p class="fc-answer"><span class="sound">${c.sound}</span><span class="hint">${c.vn || ""}</span>
            <button class="say" data-say="${c.say || c.glyph}">nghe lại</button>${videoFor(c.glyph) ? ` <button class="say" data-video="${videoFor(c.glyph).id}">▶ xem khẩu hình</button>` : ""}</p>
          ${c.word ? `<p class="fc-word"><span class="jp">${hl}</span> &nbsp;${c.romaji} — ${c.meaning}
            <button class="say" data-say="${c.word}">nghe từ</button></p>` : ""}`)
        + `<p class="fc-tap">Chạm vào thẻ để lật lại</p><div class="fc-actions"><button class="btn again" data-act="no">Chưa nhớ</button><button class="btn ok" data-act="yes">Nhớ rồi</button></div>`;
      const wrap = $("div", "fc3d", `<div class="fc-inner">${face("fc-front", review || practice, front)}${face("fc-back", false, back)}</div>`);
      el.append(wrap);
      /* Kiểu Quizlet: chạm vào thẻ để lật qua lại; nút chấm và nút nghe không làm thẻ lật. */
      wrap.tabIndex = 0; wrap.setAttribute("role", "button"); wrap.setAttribute("aria-label", "Lật thẻ");
      const flip = () => { const on = wrap.classList.toggle("flipped"); if (on) speak(c.say || big); };
      wrap.addEventListener("click", e => {
        const act = e.target.closest("[data-act]");
        if (act) { mark(c, act.dataset.act === "yes"); return; }
        if (e.target.closest("button, a")) return;
        flip();
      });
      wrap.addEventListener("keydown", e => { if (e.target === wrap && (e.key === " " || e.key === "Enter" || e.key === "ArrowUp" || e.key === "ArrowDown")) { e.preventDefault(); flip(); } });
    }
    show();
  }

  /* ---------- Ghép câu ----------
     <div data-build='[["Tôi là sinh viên.","わたし は がくせい です"], ...]'></div>
     Ô chữ = các phần cách nhau bởi dấu cách. Đáp án thứ 3 (tuỳ chọn) = một thứ tự khác cũng đúng. */
  function builder(el) {
    let items; try { items = shuffle(JSON.parse(el.dataset.build)); } catch { return; }
    let i = 0, score = 0;
    el.classList.add("quiz", "builder");
    function show() {
      if (i >= items.length) {
        el.innerHTML = `<p class="fb ${score >= items.length * .8 ? "good" : "bad"}">Kết quả: ${score}/${items.length}. ${score >= items.length * .8 ? "Bạn đã nắm được trật tự câu." : "Làm lại một lượt — thứ tự sẽ khác."}</p><p><button class="btn primary" data-again>Làm lại</button></p>`;
        el.querySelector("[data-again]").onclick = () => { shuffle(items); i = 0; score = 0; show(); };
        return;
      }
      const [vn, ans, alt] = items[i], tiles = shuffle(ans.split(" ").map((t, k) => ({ t, k })));
      el.innerHTML = `<p class="q"><span class="score">Câu ${i + 1}/${items.length} · đúng ${score}</span>Xếp thành câu tiếng Nhật: <strong>${esc(vn)}</strong></p>
        <div class="line jp"></div><div class="tiles"></div><p class="fb"></p>
        <p class="row"><button class="btn" data-clear>Xếp lại</button> <button class="btn primary" data-check>Kiểm tra</button></p>`;
      const line = el.querySelector(".line"), pool = el.querySelector(".tiles"), fb = el.querySelector(".fb");
      tiles.forEach(x => { const b = $("button", "tile jp", esc(x.t)); b.dataset.t = x.t; pool.append(b); });
      el.onclick = e => {
        const t = e.target.closest(".tile");
        if (t && !el.dataset.lock) { (t.parentElement === pool ? line : pool).append(t); return; }
        if (e.target.matches("[data-clear]")) { [...line.children].forEach(b => pool.append(b)); fb.textContent = ""; }
        if (e.target.matches("[data-check]")) {
          if (el.dataset.lock) { delete el.dataset.lock; i++; return show(); }
          if (pool.children.length) { fb.className = "fb bad"; fb.textContent = "Còn ô chưa dùng."; return; }
          const got = [...line.children].map(b => b.dataset.t).join(" "), ok = got === ans || (alt && got === alt);
          if (ok) score++;
          fb.className = "fb " + (ok ? "good" : "bad");
          fb.innerHTML = ok ? `Đúng: <span class="jp">${esc(ans)}</span>` : `Chưa đúng. Đáp án: <span class="jp">${esc(ans)}</span>`;
          speak(ans.replace(/ /g, "")); el.dataset.lock = 1; e.target.textContent = "Câu tiếp →";
        }
      };
    }
    show();
  }

  /* ---------- Hội thoại ----------
     <div data-dialog='[["A","はじめまして。","Rất hân hạnh."], ...]'></div> */
  function dialog(el) {
    let lines; try { lines = JSON.parse(el.dataset.dialog); } catch { return; }
    el.classList.add("dialog");
    el.innerHTML = `<p class="row"><button class="btn primary" data-all>▶ Nghe cả đoạn</button> <button class="btn" data-shadow>Nói đuổi (dừng sau mỗi câu)</button> <button class="btn" data-vn>Hiện / ẩn nghĩa</button> <button class="btn" data-stop>Dừng</button></p>
      <ol>${lines.map(([sp, jp, vn], k) => `<li data-k="${k}"><span class="sp">${esc(sp)}</span><span class="jp">${esc(jp)}</span> <button class="say" data-say="${esc(jp)}">nghe</button><span class="vn">${esc(vn)}</span></li>`).join("")}</ol>`;
    const lis = [...el.querySelectorAll("li")]; let run = 0;
    const mark = k => lis.forEach((li, j) => li.classList.toggle("now", j === k));
    function play(k, pause, token) {
      if (token !== run || k >= lines.length) { mark(-1); return; }
      mark(k);
      const txt = lines[k][1];
      speak(txt, () => setTimeout(() => play(k + 1, pause, token), pause ? 900 + txt.length * 260 : 450));
    }
    el.querySelector("[data-all]").onclick = () => play(0, false, ++run);
    el.querySelector("[data-shadow]").onclick = () => play(0, true, ++run);
    el.querySelector("[data-stop]").onclick = () => { run++; speechSynthesis.cancel(); mark(-1); };
    el.querySelector("[data-vn]").onclick = () => el.classList.toggle("show-vn");
  }

  /* ---------- Nghe số: giá tiền, giờ, ngày ----------
     <div data-num="price|time|date|month|count"></div> — máy đọc, bạn gõ số. */
  const D = ["", "いち", "に", "さん", "よん", "ご", "ろく", "なな", "はち", "きゅう"];
  function yomi(n) {
    if (n === 0) return "ゼロ";
    let s = "";
    const man = Math.floor(n / 10000); if (man) { s += yomi(man) + "まん"; n %= 10000; }
    const sen = Math.floor(n / 1000); n %= 1000;
    if (sen) s += ({ 1: "せん", 3: "さんぜん", 8: "はっせん" })[sen] || D[sen] + "せん";
    const hyaku = Math.floor(n / 100); n %= 100;
    if (hyaku) s += ({ 1: "ひゃく", 3: "さんびゃく", 6: "ろっぴゃく", 8: "はっぴゃく" })[hyaku] || D[hyaku] + "ひゃく";
    const ju = Math.floor(n / 10); n %= 10;
    if (ju) s += (ju === 1 ? "" : D[ju]) + "じゅう";
    return s + D[n];
  }
  const HOUR = { 4: "よじ", 7: "しちじ", 9: "くじ" };
  const MIN1 = ["", "いっぷん", "にふん", "さんぷん", "よんぷん", "ごふん", "ろっぷん", "ななふん", "はっぷん", "きゅうふん"];
  function minYomi(m) {
    const t = Math.floor(m / 10), u = m % 10;
    if (!u) return (t === 1 ? "" : D[t]) + "じゅっぷん";
    return (t ? (t === 1 ? "" : D[t]) + "じゅう" : "") + MIN1[u];
  }
  const MONTH = { 4: "しがつ", 7: "しちがつ", 9: "くがつ" };
  const DAYS_ = { 1: "ついたち", 2: "ふつか", 3: "みっか", 4: "よっか", 5: "いつか", 6: "むいか", 7: "なのか", 8: "ようか", 9: "ここのか", 10: "とおか", 14: "じゅうよっか", 17: "じゅうしちにち", 19: "じゅうくにち", 20: "はつか", 24: "にじゅうよっか", 27: "にじゅうしちにち", 29: "にじゅうくにち" };
  const NUM = {
    price: { hint: "Gõ số tiền bằng chữ số (vd 350).", gen() { const pool = [80, 100, 120, 300, 350, 600, 680, 800, 1000, 1500, 3000, 3800, 6000, 8000, 8500, 12000, 25000]; const n = Math.random() < .5 ? pool[Math.floor(Math.random() * pool.length)] : (Math.floor(Math.random() * 99) + 1) * (Math.random() < .5 ? 10 : 100); return { say: yomi(n) + "えん", ans: String(n) }; } },
    time: { hint: "Gõ giờ dạng 7:15 (giờ 1–12).", gen() { const h = Math.floor(Math.random() * 12) + 1, m = Math.random() < .25 ? 0 : Math.floor(Math.random() * 12) * 5 || 30; return { say: (HOUR[h] || yomi(h) + "じ") + (m ? minYomi(m) : ""), ans: `${h}:${String(m).padStart(2, "0")}`, alt: m ? null : String(h) }; } },
    date: { hint: "Gõ ngày dạng tháng/ngày (vd 4/8 = ngày 8 tháng 4).", gen() { const mo = Math.floor(Math.random() * 12) + 1, d = Math.random() < .6 ? [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 20, 24][Math.floor(Math.random() * 13)] : Math.floor(Math.random() * 31) + 1; return { say: (MONTH[mo] || yomi(mo) + "がつ") + " " + (DAYS_[d] || yomi(d) + "にち"), ans: `${mo}/${d}` }; } },
    count: { hint: "Gõ số bằng chữ số (vd 47).", gen() { const n = Math.floor(Math.random() * 100); return { say: yomi(n), ans: String(n) }; } },
    floor: { hint: "Gõ số tầng (vd 3).", gen() { const n = Math.floor(Math.random() * 9) + 1; return { say: ({ 1: "いっかい", 3: "さんがい", 6: "ろっかい", 8: "はっかい" })[n] || D[n] + "かい", ans: String(n) }; } },
  };
  function numDrill(el) {
    const kind = NUM[el.dataset.num] || NUM.count, rounds = +el.dataset.rounds || 10;
    let n = 0, score = 0, cur = null, answered = false;
    el.classList.add("quiz", "reader");
    el.innerHTML = `<p class="q"><span class="score"></span>Bấm nghe, rồi gõ con số bạn nghe được. ${kind.hint}</p>
      <p><button class="btn primary" data-play>▶ Nghe</button> <input type="text" inputmode="numeric" autocomplete="off" placeholder="…"> <button class="btn" data-go>Kiểm tra</button></p><p class="fb"></p>`;
    const inp = el.querySelector("input"), fb = el.querySelector(".fb"), sc = el.querySelector(".score");
    const next = () => { answered = false; inp.value = ""; cur = kind.gen(); sc.textContent = `Câu ${n + 1}/${rounds} · đúng ${score}`; speak(cur.say); inp.focus(); };
    function check() {
      if (!cur) return next();
      if (answered) { if (n >= rounds) { n = 0; score = 0; fb.textContent = ""; } return next(); }
      const v = inp.value.trim().replace(/[：]/g, ":").replace(/[／]/g, "/").replace(/^0+(\d)/, "$1");
      answered = true; n++;
      const ok = v === cur.ans || (cur.alt && v === cur.alt);
      if (ok) score++;
      fb.className = "fb " + (ok ? "good" : "bad");
      fb.innerHTML = `${ok ? "Đúng" : "Chưa đúng"}: <strong>${cur.ans}</strong> — <span class="jp">${cur.say}</span>` +
        (n >= rounds ? `<br>Kết quả: ${score}/${rounds}. Nhấn Enter để làm lượt mới.` : " · Enter để nghe câu tiếp.");
    }
    el.querySelector("[data-play]").onclick = () => cur && !answered ? speak(cur.say) : check();
    el.querySelector("[data-go]").onclick = check;
    inp.onkeydown = e => { if (e.key === "Enter") check(); };
  }

  /* ---------- Quiz nghe ---------- */
  function listen(el) {
    const raw = el.dataset.listen.trim();
    const items = raw.includes(" ") ? raw.split(/\s+/) : [...raw], rounds = +el.dataset.rounds || 10;
    let n = 0, score = 0, target = null, locked = false;
    el.classList.add("quiz");
    el.innerHTML = `<p class="q"><span class="score"></span>Bấm nghe, rồi chọn chữ vừa nghe được.</p>
      <p><button class="btn primary" data-play>▶ Nghe</button></p>
      <div class="opts">${items.map(k => `<button class="jp${k.length > 2 ? " long" : ""}" data-k="${k}">${k}</button>`).join("")}</div><p class="fb"></p>`;
    const fb = el.querySelector(".fb"), sc = el.querySelector(".score");
    const next = () => {
      locked = false;
      el.querySelectorAll(".opts button").forEach(b => b.classList.remove("right", "wrong"));
      if (n >= rounds) { fb.className = "fb " + (score >= rounds * .9 ? "good" : "bad"); fb.textContent = `Kết quả: ${score}/${rounds}. ${score >= rounds * .9 ? "Tai bạn đã phân biệt được các âm này." : "Bấm “Nghe” để làm lại một lượt nữa."}`; n = 0; score = 0; target = null; return; }
      let t; do { t = items[Math.floor(Math.random() * items.length)]; } while (t === target && items.length > 1);
      target = t; sc.textContent = `Câu ${n + 1}/${rounds} · đúng ${score}`; speak(target);
    };
    el.querySelector("[data-play]").onclick = () => target ? speak(target) : (fb.textContent = "", next());
    el.querySelector(".opts").onclick = e => {
      const b = e.target.closest("button"); if (!b || !target || locked) return;
      locked = true; n++;
      if (b.dataset.k === target) { score++; b.classList.add("right"); fb.className = "fb good"; fb.textContent = "Đúng."; }
      else { b.classList.add("wrong"); el.querySelector(`[data-k="${target}"]`).classList.add("right"); fb.className = "fb bad"; fb.textContent = `Chưa đúng — đó là ${target}.`; }
      setTimeout(next, 900);
    };
  }

  /* ---------- Luyện đọc: nhìn chữ, gõ romaji ---------- */
  // <div data-read='[["かさ","kasa","cái ô"], ...]'></div>
  function norm(s) {
    s = s.toLowerCase().replace(/ā/g, "aa").replace(/ī/g, "ii").replace(/ū/g, "uu").replace(/ē/g, "ee").replace(/ō/g, "ou")
      .replace(/[^a-z]/g, "");
    [["tch", "tty"], ["sh", "sy"], ["ch", "ty"], ["j", "zy"], ["syi", "si"], ["tyi", "ti"], ["zyi", "zi"], ["tsu", "tu"],
     ["fu", "hu"], ["wo", "o"], ["nn", "n"], ["mp", "np"], ["mb", "nb"], ["oo", "ou"]].forEach(([a, b]) => { s = s.split(a).join(b); });
    return s;
  }
  function reader(el) {
    let items; try { items = JSON.parse(el.dataset.read); } catch { return; }
    items = items.map(x => x).sort(() => Math.random() - .5);
    let i = 0, score = 0, answered = false;
    el.classList.add("quiz", "reader");
    el.innerHTML = `<p class="q"><span class="score"></span>Đọc to từ dưới đây, rồi gõ cách đọc bằng romaji và nhấn Enter.</p>
      <p class="word jp"></p><p><input type="text" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="romaji…">
      <button class="btn primary" data-go>Kiểm tra</button></p><p class="fb"></p>`;
    const w = el.querySelector(".word"), inp = el.querySelector("input"), fb = el.querySelector(".fb"), sc = el.querySelector(".score"), go = el.querySelector("[data-go]");
    function show() {
      answered = false; inp.value = ""; fb.textContent = ""; fb.className = "fb"; go.textContent = "Kiểm tra";
      if (i >= items.length) {
        w.textContent = "おわり"; sc.textContent = "";
        fb.className = "fb " + (score >= items.length * .9 ? "good" : "bad");
        fb.textContent = `Kết quả: ${score}/${items.length}. Nhấn Enter để làm lại theo thứ tự mới.`;
        i = -1; answered = true; return;
      }
      w.textContent = items[i][0]; sc.textContent = `Từ ${i + 1}/${items.length} · đúng ${score}`;
    }
    function check() {
      if (answered) { if (i === -1) { items.sort(() => Math.random() - .5); score = 0; } i++; show(); inp.focus(); return; }
      const [jp, ro, vn] = items[i]; answered = true; speak(jp);
      if (norm(inp.value) === norm(ro)) { score++; fb.className = "fb good"; fb.textContent = `Đúng: ${ro} — ${vn}.`; }
      else { fb.className = "fb bad"; fb.textContent = `Chưa đúng: ${ro} — ${vn}. Đọc to lại một lần.`; }
      go.textContent = "Từ tiếp →";
    }
    go.onclick = check; inp.onkeydown = e => { if (e.key === "Enter") check(); };
    show();
  }

  /* ---------- Quiz chọn đáp án ---------- */
  function quiz(el) {
    const ans = +el.dataset.answer, btns = [...el.querySelectorAll(".opts button")];
    const fb = el.querySelector(".fb") || el.appendChild($("p", "fb"));
    btns.forEach((b, i) => b.onclick = () => {
      btns.forEach(x => x.classList.remove("right", "wrong"));
      const ok = i + 1 === ans; b.classList.add(ok ? "right" : "wrong");
      fb.className = "fb " + (ok ? "good" : "bad");
      fb.textContent = ok ? "Đúng. " + (el.dataset.explain || "") : "Chưa đúng — thử lại.";
    });
  }

  /* ---------- Tập viết ---------- */
  function writer(el) {
    const ch = el.dataset.write, paths = (window.STROKES || {})[ch] || [];
    el.classList.add("writer");
    const svgPaths = cls => paths.map(d => `<path class="${cls}" d="${d}"/>`).join("");
    const nums = paths.map((d, i) => { const m = d.match(/M\s*([\d.]+)[ ,]([\d.]+)/); return `<text x="${+m[1] - 7}" y="${+m[2] + 1}">${i + 1}</text>`; }).join("");
    el.innerHTML = `<div class="pad"><svg viewBox="0 0 109 109">${svgPaths("guide")}${svgPaths("ink")}${nums}</svg><canvas></canvas></div>
      <div class="row"><button class="btn" data-a="anim">Xem nét</button><button class="btn" data-a="clear">Xoá</button><button class="say" data-say="${ch}">nghe</button></div>`;
    const inks = [...el.querySelectorAll("path.ink")], cv = el.querySelector("canvas"), ctx = cv.getContext("2d");
    inks.forEach(p => { const L = p.getTotalLength(); p.style.strokeDasharray = L; p.style.strokeDashoffset = L; });
    let timers = [];
    function animate() {
      timers.forEach(clearTimeout); timers = []; let t = 0;
      inks.forEach(p => { p.style.transition = "none"; p.style.strokeDashoffset = p.getTotalLength(); });
      inks.forEach(p => { const L = p.getTotalLength(), dur = 350 + L * 9;
        timers.push(setTimeout(() => { p.style.transition = `stroke-dashoffset ${dur}ms ease-in-out`; p.style.strokeDashoffset = 0; }, t + 60)); t += dur + 250; });
      timers.push(setTimeout(() => inks.forEach(p => { p.style.transition = "none"; p.style.strokeDashoffset = p.getTotalLength(); }), t + 1200));
    }
    function fit() { const r = cv.getBoundingClientRect(), d = devicePixelRatio || 1; cv.width = r.width * d; cv.height = r.height * d; ctx.scale(d, d); ctx.lineWidth = Math.max(5, r.width / 24); ctx.lineCap = ctx.lineJoin = "round"; ctx.strokeStyle = getComputedStyle(el).getPropertyValue("--fg") || "#222"; }
    fit(); addEventListener("resize", fit);
    let down = false;
    const pos = e => { const r = cv.getBoundingClientRect(); return [e.clientX - r.left, e.clientY - r.top]; };
    cv.onpointerdown = e => { down = true; cv.setPointerCapture(e.pointerId); ctx.beginPath(); ctx.moveTo(...pos(e)); };
    cv.onpointermove = e => { if (!down) return; ctx.lineTo(...pos(e)); ctx.stroke(); };
    cv.onpointerup = cv.onpointercancel = () => down = false;
    el.querySelector(".row").onclick = e => { const a = e.target.dataset.a; if (a === "anim") animate(); if (a === "clear") { ctx.save(); ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.clearRect(0, 0, cv.width, cv.height); ctx.restore(); } };
  }

  /* ---------- Viết lại từ trí nhớ ----------
     items: [{ text: "せんせい", prompt: "sensei", hint: "giáo viên" }, ...]
     Mỗi mục: nhìn romaji + nghĩa (hoặc nghe), tự viết từng chữ vào ô trống, rồi bấm
     "Xem đáp án" để nét chuẩn hiện chồng lên chữ mình viết, tự chấm Nhớ / Chưa nhớ. */
  function rewrite(el, items, opt) {
    opt = opt || {};
    const S = window.STROKES || {};
    let order = shuffle(items.slice()), i = 0, ok = 0, missed = [], shown = false, faint = false;
    el.classList.add("quiz", "rewrite");
    /* Ẩn/hiện gợi ý: romaji và tiếng Việt đều có thể làm lộ đáp án, nên cho tắt riêng từng cái. Nhớ lựa chọn trong trình duyệt. */
    const HKEY = "nihongo-rewrite-hide-v1"; let hide = { ro: false, vn: false };
    try { hide = { ...hide, ...JSON.parse(localStorage.getItem(HKEY)) }; } catch {}
    const applyHide = () => { el.classList.toggle("hide-ro", hide.ro); el.classList.toggle("hide-vn", hide.vn); };
    const tglLabel = () => `<button class="chip${hide.ro ? "" : " on"}" data-a="t-ro">Romaji: ${hide.ro ? "ẩn" : "hiện"}</button><button class="chip${hide.vn ? "" : " on"}" data-a="t-vn">Tiếng Việt: ${hide.vn ? "ẩn" : "hiện"}</button>`;
    function pad(ch) {
      const paths = S[ch] || [];
      const g = paths.length ? paths.map(d => `<path class="guide" d="${d}"/>`).join("") + paths.map(d => `<path class="ink" d="${d}"/>`).join("")
        : `<text class="glyph" x="54.5" y="80" text-anchor="middle">${esc(ch)}</text>`;
      return `<div class="pad"><svg viewBox="0 0 109 109">${g}</svg><canvas></canvas></div>`;
    }
    function wire(p) {
      const cv = p.querySelector("canvas"), ctx = cv.getContext("2d");
      const r = cv.getBoundingClientRect(), d = devicePixelRatio || 1;
      cv.width = r.width * d; cv.height = r.height * d; ctx.scale(d, d);
      ctx.lineWidth = Math.max(4, r.width / 22); ctx.lineCap = ctx.lineJoin = "round";
      ctx.strokeStyle = getComputedStyle(el).getPropertyValue("--fg").trim() || "#222";
      let down = false; p.strokes = [];
      const pos = e => { const b = cv.getBoundingClientRect(); return [e.clientX - b.left, e.clientY - b.top]; };
      const norm = e => { const b = cv.getBoundingClientRect(), q = pos(e); return [q[0] / b.width * 109, q[1] / b.height * 109]; };
      cv.onpointerdown = e => { if (shown) return; down = true; cv.setPointerCapture(e.pointerId); ctx.beginPath(); ctx.moveTo(...pos(e)); ctx.lineTo(...pos(e)); ctx.stroke(); p.strokes.push([norm(e)]); };
      cv.onpointermove = e => { if (!down) return; ctx.lineTo(...pos(e)); ctx.stroke(); p.strokes[p.strokes.length - 1].push(norm(e)); };
      cv.onpointerup = cv.onpointercancel = () => down = false;
      p.clear = () => { ctx.save(); ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.clearRect(0, 0, cv.width, cv.height); ctx.restore(); p.strokes = []; };
    }
    /* Chấm gần đúng: so nét mình viết với nét chuẩn KanjiVG (độ phủ + độ chính xác trong dung sai ±8/109, trừ điểm nếu lệch số nét).
       Không xét thứ tự nét; chỉ là gợi ý. */
    function scorePad(p, ch) {
      const paths = S[ch], used = (p.strokes || []).filter(s => s.length);
      if (!paths) return null;
      if (!used.length) return 0;
      const K = 2, W = 109 * K;
      const mk = () => { const c = document.createElement("canvas"); c.width = c.height = W; const x = c.getContext("2d"); x.scale(K, K); x.lineCap = x.lineJoin = "round"; return x; };
      const ref = w => { const x = mk(); x.lineWidth = w; paths.forEach(d => x.stroke(new Path2D(d))); return x; };
      const usr = w => { const x = mk(); x.lineWidth = w; used.forEach(s => { x.beginPath(); x.moveTo(...s[0]); s.forEach(q => x.lineTo(...q)); x.lineTo(s[s.length - 1][0] + .1, s[s.length - 1][1]); x.stroke(); }); return x; };
      const px = x => x.getImageData(0, 0, W, W).data;
      const rt = px(ref(3)), rf = px(ref(16)), ut = px(usr(3)), uf = px(usr(16));
      let nr = 0, hit = 0, nu = 0, good = 0;
      for (let i = 3; i < rt.length; i += 4) {
        if (rt[i] > 40) { nr++; if (uf[i] > 40) hit++; }
        if (ut[i] > 40) { nu++; if (rf[i] > 40) good++; }
      }
      const cov = nr ? hit / nr : 0, pre = nu ? good / nu : 0, f1 = cov + pre ? 2 * cov * pre / (cov + pre) : 0;
      return Math.max(0, f1 - Math.min(.3, Math.abs(used.length - paths.length) * .08));
    }
    /* Ẩn/hiện nét mình viết (không xoá hẳn) để xem nét chuẩn cho rõ. */
    function setMine(off) {
      const box = el.querySelector(".rw-pads"), b = el.querySelector('[data-a="mine"]'); if (!box) return;
      box.classList.toggle("mine-off", off); if (b) b.textContent = off ? "Hiện nét mình viết" : "Ẩn nét mình viết";
    }
    function animate(hideMine) {
      if (hideMine) setMine(true);
      let t = 0;
      el.querySelectorAll(".pad").forEach(p => p.querySelectorAll("path.ink").forEach(path => {
        const L = path.getTotalLength(), dur = 300 + L * 7;
        path.style.transition = "none"; path.style.strokeDasharray = L; path.style.strokeDashoffset = L;
        setTimeout(() => { path.style.transition = `stroke-dashoffset ${dur}ms ease-in-out`; path.style.strokeDashoffset = 0; }, t + 40);
        t += dur + 150;
      }));
    }
    function show() {
      shown = false; el.classList.remove("revealed"); applyHide();
      if (i >= order.length) return done();
      const it = order[i], chars = [...it.text.replace(/\s+/g, "")];
      el.innerHTML = `<p class="q"><span class="score">Mục ${i + 1}/${order.length} · nhớ ${ok}</span>Viết lại bằng tay, không nhìn đáp án:</p>
        <div class="rw-tgl">${tglLabel()}</div>
        <p class="rw-prompt"><b class="rw-ro">${esc(it.prompt)}</b>${it.hint ? ` <span class="rw-vn">— ${esc(it.hint)}</span>` : ""}
          <button class="say" data-say="${esc(it.text)}">nghe</button></p>
        <div class="rw-pads${faint ? " faint" : ""}${chars.length > 4 ? " many" : ""}">${chars.map(pad).join("")}</div>
        <p class="rw-count">${chars.length} chữ</p>
        <div class="row rw-act">
          <button class="btn" data-a="clear">Xoá</button>
          <button class="btn" data-a="faint">${faint ? "Tắt" : "Bật"} nét mờ</button>
          <button class="btn primary" data-a="reveal">Xem đáp án</button>
        </div><p class="fb"></p>`;
      el.querySelectorAll(".pad").forEach(wire);
      if (hide.ro && hide.vn) speak(it.text);   // ẩn hết: chỉ còn nghe để viết
    }
    function reveal() {
      shown = true; const it = order[i]; el.classList.add("revealed");
      el.querySelector(".rw-pads").classList.add("shown");
      el.querySelector(".rw-count").innerHTML = `<span class="jp rw-answer">${esc(it.text)}</span>`;
      el.querySelector(".rw-act").innerHTML = `<button class="btn" data-a="anim">Xem lại thứ tự nét</button><button class="btn" data-a="mine">Ẩn nét mình viết</button>
        <button class="btn again" data-a="miss">Chưa nhớ</button><button class="btn primary" data-a="ok">Nhớ đúng</button>`;
      const chars = [...it.text.replace(/\s+/g, "")], pads = [...el.querySelectorAll(".pad")];
      const sc = pads.map((p, k) => { const v = scorePad(p, chars[k]);
        if (v != null) p.insertAdjacentHTML("beforeend", `<span class="rw-score ${v >= .55 ? "good" : "bad"}">${Math.round(v * 100)}%</span>`); return v; }).filter(v => v != null);
      const fb = el.querySelector(".fb");
      if (sc.length) {
        const avg = sc.reduce((a, b) => a + b, 0) / sc.length, good = avg >= .55;
        fb.className = "fb " + (good ? "good" : "bad");
        fb.textContent = `Máy chấm: ${Math.round(avg * 100)}% — gợi ý "${good ? "Nhớ đúng" : "Chưa nhớ"}". Đây chỉ là ước lượng (không xét thứ tự nét), bạn tự quyết định.`;
        el.querySelector(good ? '[data-a="ok"]' : '[data-a="miss"]').classList.add("suggest");
      } else fb.textContent = "So chữ của bạn (nét đen) với nét chuẩn (màu), rồi tự chấm.";
      speak(it.text); animate();
    }
    function next(good) { if (opt.onGrade) opt.onGrade(order[i], good); if (good) ok++; else missed.push(order[i]); i++; show(); }
    function done() {
      const n = order.length;
      el.innerHTML = `<p class="q">Xong lượt viết.</p>
        <p class="fb ${ok >= n * .9 ? "good" : "bad"}">Nhớ đúng ${ok}/${n}.${missed.length ? " Cần viết lại: " : ""}<span class="jp">${missed.map(m => esc(m.text)).join("、")}</span></p>
        <div class="row">${missed.length ? `<button class="btn primary" data-a="again-miss">Viết lại ${missed.length} mục sai</button>` : ""}
          ${opt.onGrade ? "" : `<button class="btn${missed.length ? "" : " primary"}" data-a="again">Viết lại tất cả</button>`}</div>`;
    }
    el.onclick = e => {
      const b = e.target.closest("[data-a]"); if (!b) return; const a = b.dataset.a;
      if (a === "t-ro" || a === "t-vn") {
        const k = a.slice(2); hide[k] = !hide[k]; try { localStorage.setItem(HKEY, JSON.stringify(hide)); } catch {}
        applyHide(); el.querySelector(".rw-tgl").innerHTML = tglLabel();
      }
      else if (a === "clear") el.querySelectorAll(".pad").forEach(p => p.clear());
      else if (a === "faint") { faint = !faint; el.querySelector(".rw-pads").classList.toggle("faint", faint); b.textContent = (faint ? "Tắt" : "Bật") + " nét mờ"; }
      else if (a === "reveal") reveal();
      else if (a === "anim") animate(true);
      else if (a === "mine") setMine(!el.querySelector(".rw-pads").classList.contains("mine-off"));
      else if (a === "ok" || a === "miss") next(a === "ok");
      else if (a === "again" || a === "again-miss") { order = shuffle((a === "again" ? items : missed).slice()); i = ok = 0; missed = []; show(); }
    };
    show();
  }

  /* ---------- Trắc nghiệm ----------
     items: [{ text, romaji, vn, kind }]; opt.pool = kho lấy đáp án nhiễu; opt.onGrade(item, ok).
     Câu hỏi và đáp án chọn tự do trong Nhật / Romaji / Việt (kana không có nghĩa tiếng Việt).
     Thời gian mỗi câu (tuỳ chọn): hết giờ tính là sai và tự qua câu sau. */
  function recognize(el, items, opt) {
    opt = opt || {};
    const pool = (opt.pool && opt.pool.length >= 4) ? opt.pool : items;
    const canVn = items.every(x => x.kind === "vocab" && x.vn);
    const KINDS = canVn ? ["jp", "ro", "vn"] : ["jp", "ro"], NAME = { jp: "Nhật", ro: "Romaji", vn: "Việt" };
    const QKEY = "nihongo-quiz-v1";
    let cfg = { q: "jp", a: canVn ? "vn" : "ro", t: 0 };
    try { cfg = { ...cfg, ...JSON.parse(localStorage.getItem(QKEY)) }; } catch {}
    if (!KINDS.includes(cfg.q)) cfg.q = "jp";
    if (!KINDS.includes(cfg.a) || cfg.a === cfg.q) cfg.a = KINDS.find(k => k !== cfg.q);
    if (![0, 5, 10, 20].includes(cfg.t)) cfg.t = 0;
    const val = (x, k) => k === "jp" ? x.text : k === "ro" ? x.romaji : x.vn;
    let order = shuffle(items.slice()), i = 0, ok = 0, missed = [], locked = false, opts = [], tick = null, nextT = null, deadline = 0;
    el.classList.add("quiz", "recog");
    const stop = () => { clearInterval(tick); clearTimeout(nextT); };
    const keep = () => { try { localStorage.setItem(QKEY, JSON.stringify(cfg)); } catch {} };
    const chips = (key, label) => `<span class="qz-row"><b>${label}</b>${KINDS.filter(k => key === "q" || k !== cfg.q).map(k =>
      `<button class="chip${cfg[key] === k ? " on" : ""}" data-c="${key}:${k}">${NAME[k]}</button>`).join("")}</span>`;
    function startTimer() {
      deadline = Date.now() + cfg.t * 1000; const bar = el.querySelector(".qz-bar i");
      tick = setInterval(() => {
        if (!el.isConnected) return stop();
        const left = deadline - Date.now(); if (bar) bar.style.width = Math.max(0, left / (cfg.t * 1000)) * 100 + "%";
        if (left <= 0) answer(-1);
      }, 100);
    }
    function show() {
      stop(); locked = false;
      if (i >= order.length) {
        el.innerHTML = `<p class="q">Xong lượt này.</p><p class="fb ${ok >= order.length * .9 ? "good" : "bad"}">Đúng ${ok}/${order.length}.${missed.length ? " Cần xem lại: " : ""}<span class="jp">${missed.map(m => esc(m.text)).join("、")}</span></p>
          <div class="row">${missed.length ? `<button class="btn primary" data-r="again-miss">Làm lại ${missed.length} mục sai</button>` : ""}<button class="btn${missed.length ? "" : " primary"}" data-r="again">Làm lại tất cả</button></div>`;
        return;
      }
      const it = order[i], right = val(it, cfg.a);
      const wrong = shuffle(pool.map(x => val(x, cfg.a)).filter((v, k, arr) => v && v !== right && arr.indexOf(v) === k)).slice(0, 3);
      opts = shuffle([right, ...wrong]);
      const ask = { jp: "chữ Nhật", ro: "cách đọc (romaji)", vn: "nghĩa tiếng Việt" }[cfg.a];
      el.innerHTML = `<div class="qz-cfg">${chips("q", "Câu hỏi")}${chips("a", "Đáp án")}
          <span class="qz-row"><b>Thời gian</b>${[0, 5, 10, 20].map(t => `<button class="chip${cfg.t === t ? " on" : ""}" data-c="t:${t}">${t ? t + " giây" : "Tắt"}</button>`).join("")}</span></div>
        <p class="q"><span class="score">Mục ${i + 1}/${order.length} · đúng ${ok}</span>Chọn ${ask} đúng:</p>
        ${cfg.t ? `<div class="qz-bar"><i></i></div>` : ""}
        <p class="word${cfg.q === "jp" ? " jp" : " sm"}">${esc(val(it, cfg.q))}</p>
        ${cfg.q === "jp" ? `<p class="rw-count"><button class="say" data-say="${esc(it.text)}">nghe</button></p>` : ""}
        <div class="opts rc-opts${cfg.a === "jp" ? " jpopts" : ""}">${opts.map((o, k) => `<button data-o="${k}"${cfg.a === "jp" ? ' class="jp"' : ""}>${esc(o)}</button>`).join("")}</div>
        <p class="fb"></p><div class="row" data-nextrow hidden><button class="btn primary" data-r="next">Tiếp →</button></div>`;
      if (cfg.q === "jp") speak(it.text);
      if (cfg.t) startTimer();
    }
    function answer(k) {
      if (locked) return; locked = true; stop();
      const it = order[i], right = val(it, cfg.a), good = k >= 0 && opts[k] === right;
      el.querySelectorAll("[data-o]").forEach(x => { if (opts[+x.dataset.o] === right) x.classList.add("right"); });
      if (k >= 0 && !good) el.querySelector(`[data-o="${k}"]`).classList.add("wrong");
      if (good) ok++; else missed.push(it);
      if (opt.onGrade) opt.onGrade(it, good);
      const fb = el.querySelector(".fb"); fb.className = "fb " + (good ? "good" : "bad");
      fb.textContent = `${good ? "Đúng" : k < 0 ? "Hết giờ" : "Chưa đúng"}: ${it.text} · ${it.romaji}${it.kind === "vocab" && it.vn ? " — " + it.vn : ""}`;
      if (cfg.q !== "jp") speak(it.text);
      el.querySelector("[data-nextrow]").hidden = false;
      if (cfg.t) nextT = setTimeout(() => { if (el.isConnected) { i++; show(); } }, 1800);
    }
    el.onclick = e => {
      const b = e.target.closest("button"); if (!b) return;
      if (b.dataset.o != null) return answer(+b.dataset.o);
      if (b.dataset.c) {
        if (locked) return;
        const [key, v] = b.dataset.c.split(":"); cfg[key] = key === "t" ? +v : v;
        if (cfg.a === cfg.q) cfg.a = KINDS.find(k => k !== cfg.q);
        keep(); return show();
      }
      const r = b.dataset.r; if (!r) return;
      if (r === "next") { stop(); i++; show(); }
      else if (r === "again" || r === "again-miss") { order = shuffle((r === "again" ? items : missed).slice()); i = ok = 0; missed = []; show(); }
    };
    show();
  }

  /* ---------- Chép chính tả: nghe câu, gõ lại ----------
     Nihongo.dictation(el, [["わたしは ナムです。", "Tôi là Nam."], ...]) */
  function dictation(el, items) {
    const clean = t => String(t).replace(/^[…\s]+/, "").replace(/[\s、。，．,.!?！？…・「」『』（）()～〜ー-]/g, "");
    let order = shuffle(items.slice()), i = 0, ok = 0, missed = [];
    el.classList.add("quiz", "dict");
    function show() {
      if (i >= order.length) {
        el.innerHTML = `<p class="q">Xong lượt chép chính tả.</p><p class="fb ${ok >= order.length * .8 ? "good" : "bad"}">Đúng ${ok}/${order.length}.</p>
          <div class="row">${missed.length ? `<button class="btn primary" data-r="miss">Làm lại ${missed.length} câu sai</button>` : ""}<button class="btn${missed.length ? "" : " primary"}" data-r="all">Làm lại tất cả</button></div>`;
        return;
      }
      const it = order[i];
      el.innerHTML = `<p class="q"><span class="score">Câu ${i + 1}/${order.length} · đúng ${ok}</span>Nghe rồi gõ lại câu bạn nghe được (kana hoặc kanji đều được):</p>
        <p class="row"><button class="btn primary" data-r="play">▶ Nghe</button> <button class="btn" data-r="slow">Nghe chậm</button></p>
        <textarea class="jp" rows="2" style="width:100%;font-size:1.2rem" placeholder="Gõ câu bạn nghe được"></textarea>
        <p class="row"><button class="btn primary" data-r="check">Kiểm tra</button> <button class="btn" data-r="reveal">Xem đáp án</button></p><div class="fb" data-fb></div>`;
      speak(it[0]);
    }
    function finish(good) { if (good) ok++; else missed.push(order[i]); i++; show(); }
    el.onclick = e => {
      const b = e.target.closest("button"); if (!b || !order[i] && !b.dataset.r) return;
      const r = b.dataset.r, it = order[i], fb = el.querySelector("[data-fb]"), ta = el.querySelector("textarea");
      if (r === "play") speak(it[0]);
      else if (r === "slow") speak(it[0], null, 0.55);
      else if (r === "check" || r === "reveal") {
        const good = r === "check" && clean(ta.value) === clean(it[0]);
        if (good) { fb.className = "fb good"; fb.innerHTML = `Đúng: <span class="jp">${esc(it[0])}</span><br><span class="hint">${esc(it[1] || "")}</span> <button class="btn primary" data-r="good">Câu tiếp →</button>`; }
        else {
          fb.className = "fb bad";
          fb.innerHTML = `Đáp án: <span class="jp">${esc(it[0])}</span><br><span class="hint">${esc(it[1] || "")}</span><br>
            ${r === "check" ? `<button class="btn" data-r="good">Tôi viết đúng (chỉ khác cách viết)</button> ` : ""}<button class="btn primary" data-r="bad">Câu tiếp →</button>`;
        }
      }
      else if (r === "good") finish(true);
      else if (r === "bad") finish(false);
      else if (r === "all" || r === "miss") { order = shuffle((r === "all" ? items : missed).slice()); i = ok = 0; missed = []; show(); }
    };
    show();
  }

  /* ---------- Gộp chế độ ôn: Flashcard / Viết lại / Trắc nghiệm / Gõ cách đọc / Nghe chọn ----------
     Nihongo.modes(el, cards, { graded: true|false, pool: [thẻ gây nhiễu], tabs: ["deck", ...] })
     graded = kết quả ghi vào lịch ôn (trang ôn hằng ngày); không graded = luyện tự do. */
  const hvOf = c => { const m = /^Hán Việt:\s*([^—]+?)\s*—\s*(.*)$/.exec(c.vn || ""); return { name: m ? m[1] : (c.vn || ""), mean: m ? m[2] : "" }; };
  function cardItem(c) {
    if (c.type === "vocab") return { id: c.id, text: c.word, romaji: c.romaji, vn: c.meaning, kind: "vocab" };
    if (c.type === "kanji") { const h = hvOf(c); return { id: c.id, text: c.glyph, romaji: h.name, vn: h.mean, kind: "vocab", say: c.say }; }
    return { id: c.id, text: c.glyph, romaji: c.sound, vn: c.vn || "", kind: "kana" };
  }
  function modes(el, cards, opt) {
    opt = opt || {};
    const ALL = [["deck", "Flashcard"], ["write", "Viết lại"], ["recog", "Trắc nghiệm"], ["read", "Gõ cách đọc"], ["listen", "Nghe chọn"]];
    const noText = cards.some(c => c.type === "kanji");              // kanji: không có kiểu gõ romaji / nghe chọn
    const list = ALL.filter(([k]) => (opt.tabs ? opt.tabs.includes(k) : true) && !(noText && (k === "read" || k === "listen")));
    let mode = (opt.mode && list.some(([k]) => k === opt.mode)) ? opt.mode : "deck";
    el.innerHTML = ""; el.classList.add("modes");
    if (!cards.length) { el.append($("div", "note", opt.empty || "Không có thẻ nào.")); return; }
    const bar = $("div", "mode-switch"), stage = $("div"); el.append(bar, stage);
    const items = cards.map(cardItem), grade_ = it => { if (opt.graded) grade(it.id, true); };
    function run() {
      [...bar.children].forEach(b => b.classList.toggle("primary", b.dataset.m === mode));
      const host = $("div"); stage.innerHTML = ""; stage.append(host);
      const onGrade = opt.graded ? (it, ok) => grade(it.id, ok) : null;
      if (mode === "deck") deck(host, { cards, graded: !!opt.graded });
      else if (mode === "write") rewrite(host, items.map(it => ({ id: it.id, text: it.text, prompt: it.romaji, hint: it.kind === "vocab" ? it.vn : (it.vn || "") })), { onGrade });
      else if (mode === "recog") {
        const kinds = new Set(items.map(x => x.kind)), pool = (opt.pool || cards).map(cardItem);
        recognize(host, items, { pool: pool.filter(x => kinds.size > 1 || kinds.has(x.kind)), onGrade });
      }
      else if (mode === "read") { host.dataset.read = JSON.stringify(items.map(it => [it.text, it.romaji, it.vn])); reader(host); }
      else if (mode === "listen") {
        if (items.length < 2) { host.className = "note"; host.textContent = "Cần ít nhất 2 mục để nghe chọn."; return; }
        host.dataset.listen = items.map(it => it.text.replace(/\s+/g, "")).join(" ");
        host.dataset.rounds = Math.min(20, Math.max(8, items.length * 2)); listen(host);
      }
    }
    list.forEach(([k, v]) => { const b = $("button", "btn", v); b.dataset.m = k; b.onclick = () => { mode = k; run(); }; bar.append(b); });
    run();
  }

  /* ---------- Tiến độ bài học, sao lưu ---------- */
  const LKEY = "nihongo-lessons-v1", EXAM = new Date(2027, 6, 4);
  const lessons = () => { try { return JSON.parse(localStorage.getItem(LKEY)) || {}; } catch { return {}; } };
  const setLesson = (n, on) => { const s = lessons(); if (on) s[n] = Date.now(); else delete s[n]; try { localStorage.setItem(LKEY, JSON.stringify(s)); } catch {} };

  function lessonDone() {
    const m = location.pathname.match(/\/lessons\/(\d{4})-/), nav = document.querySelector("main nav.next");
    if (!m || !nav) return;
    const n = m[1], box = $("div", "note lesson-done", "");
    const paint = () => {
      const on = !!lessons()[n];
      box.innerHTML = on ? `<strong>Bài ${n} đã đánh dấu hoàn thành.</strong> <button class="btn" data-undo>Bỏ đánh dấu</button>`
        : `<strong>Xong bài này?</strong> Làm hết phần “Nhớ lại” rồi bấm để ghi tiến độ. <button class="btn primary" data-done>Đánh dấu đã học xong</button>`;
    };
    box.onclick = e => { if (e.target.closest("[data-done]")) setLesson(n, true); else if (e.target.closest("[data-undo]")) setLesson(n, false); else return; paint(); };
    paint(); nav.before(box);
  }

  function progress(el) {
    const done = lessons(), items = [...document.querySelectorAll(".lesson-list li")];
    items.forEach(li => { const n = li.querySelector(".num").textContent; if (done[n]) li.classList.add("done"); });
    const kana = Object.keys(done).filter(n => +n <= 11).length, minna = Object.keys(done).filter(n => +n >= 12).length;
    const days = Math.ceil((EXAM - Date.now()) / DAY), left = Math.max(0, 50 - minna);
    const pace = days > 0 ? (left / (days / 7)).toFixed(1) : "—";
    const composed = Math.max(0, items.length - 11);
    el.innerHTML = `<div class="progress"><div class="bar"><i style="width:${Math.round(minna / 50 * 100)}%"></i></div>
      <p>Đã học xong <strong>${minna}/50 bài Minna</strong> và ${kana}/11 bài kana. Khoá hiện có ${composed}/50 bài Minna.<br>
      Còn <strong>${days > 0 ? days : 0} ngày</strong> tới kỳ N4 dự kiến 4/7/2027 (chưa xác nhận trên jlpt.jp): cần khoảng <strong>${pace} bài Minna/tuần</strong> để kịp.</p></div>`;
    const next = items.find(li => !li.classList.contains("done")), box = document.querySelector(".actions");
    if (next && box) {
      const a = $("a", "btn", "Học tiếp: " + next.querySelector(".num").textContent + " · " + esc(next.querySelector("a").textContent));
      a.href = next.querySelector("a").getAttribute("href"); a.style.textDecoration = "none"; box.firstElementChild ? box.firstElementChild.after(a) : box.prepend(a);
    }
  }

  /* ---------- Thống kê ôn tập: <div data-stats></div> ---------- */
  function stats(el) {
    const srs = load(), st = loadStats(), today = dayKey(), cards = {};
    (window.CARDS || []).forEach(c => cards[c.id] = c);
    const t = st[today] || { ok: 0, bad: 0 };
    let streak = 0, d = new Date(); if (!st[dayKey(d)]) d.setDate(d.getDate() - 1);
    while (st[dayKey(d)] && st[dayKey(d)].ok + st[dayKey(d)].bad > 0) { streak++; d.setDate(d.getDate() - 1); }
    const ids = Object.keys(srs), start = new Date(); start.setHours(0, 0, 0, 0);
    const days = Array.from({ length: 7 }, () => 0);
    ids.forEach(id => { const off = Math.floor((srs[id].due - start.getTime()) / DAY); if (off <= 0) days[0]++; else if (off < 7) days[off]++; });
    const max = Math.max(1, ...days), names = ["Hôm nay", "Mai", ...Array.from({ length: 5 }, (_, i) => { const x = new Date(start); x.setDate(x.getDate() + i + 2); return ["CN", "T2", "T3", "T4", "T5", "T6", "T7"][x.getDay()]; })];
    const mature = ids.filter(id => srs[id].box >= 4).length;
    const hard = ids.filter(id => srs[id].miss > 1 && cards[id]).sort((a, b) => srs[b].miss - srs[a].miss).slice(0, 6);
    const label = c => esc(c.type === "vocab" ? c.word : c.glyph);
    el.innerHTML = `<div class="stats"><div class="stat-row">
      <div><b>${t.ok + t.bad}</b><span>thẻ đã ôn hôm nay${t.bad ? ` (${t.bad} chưa nhớ)` : ""}</span></div>
      <div><b>${streak}</b><span>ngày học liên tục</span></div>
      <div><b>${t.fresh || 0}/${NEW_MAX}</b><span>thẻ mới hôm nay (mức nên học)</span></div>
      <div><b>${ids.length}</b><span>thẻ đang học, ${mature} đã chắc (≥14 ngày)</span></div></div>
      <p class="hint">Thẻ đến hạn 7 ngày tới</p>
      <div class="stat-bars">${days.map((n, i) => `<div><i style="height:${Math.round(n / max * 48)}px"></i><b>${n}</b><span>${names[i]}</span></div>`).join("")}</div>
      ${hard.length ? `<p class="hint">Hay quên nhất: ${hard.map(id => `<span class="jp">${label(cards[id])}</span> ×${srs[id].miss}`).join(" · ")}</p>` : ""}</div>`;
  }

  /* ---------- Thanh điều hướng chung ---------- */
  function siteNav() {
    const main = document.querySelector("main"); if (!main || document.querySelector(".site-nav")) return;
    const root = BASE.replace(/assets\/$/, ""), path = location.pathname;
    const links = [["index.html", "Mục lục"], ["flashcards.html", "Ôn hằng ngày"], ["practice.html", "Luyện tự chọn"], ["kanji.html", "Kanji"], ["search.html", "Tìm"], ["notebook.html", "Sổ tay"], ["index.html#tra-cuu", "Tra cứu"]];
    const nav = $("nav", "site-nav", links.map(([h, t]) => {
      const file = h.split("#")[0], here = !h.includes("#") && (path.endsWith("/" + file) || (file === "index.html" && /\/$/.test(path)));
      return `<a href="${root}${h}"${here ? ' aria-current="page"' : ""}>${t}</a>`;
    }).join(""));
    main.prepend(nav);
  }

  /* ---------- Tự động lưu vào file (Chrome/Edge trên máy tính) ----------
     Người học chọn một file .json một lần; mỗi khi dữ liệu "nihongo-*" đổi, ghi lại file sau ~3 giây.
     Tay cầm file giữ trong IndexedDB; sau khi mở lại trình duyệt có thể cần bấm "Cho phép lại" (một cú bấm). */
  const FS = { ok: !!window.showSaveFilePicker, handle: null, state: "off", last: 0, err: "" };
  const FSKEY = "nihongo-lastbackup", fsTell = () => document.dispatchEvent(new Event("nihongo-fs"));
  const idb = (mode, fn) => new Promise((res, rej) => {
    const r = indexedDB.open("nihongo-fs", 1);
    r.onupgradeneeded = () => r.result.createObjectStore("h");
    r.onerror = () => rej(r.error);
    r.onsuccess = () => { try { const t = r.result.transaction("h", mode), q = fn(t.objectStore("h")); t.oncomplete = () => res(q && q.result); t.onerror = t.onabort = () => rej(t.error); } catch (e) { rej(e); } };
  });
  const dataKeys = () => Object.keys(localStorage).filter(k => k.startsWith("nihongo-") && k !== FSKEY);
  const snapshot = () => { const d = {}; Object.keys(localStorage).filter(k => k.startsWith("nihongo-")).forEach(k => d[k] = localStorage.getItem(k)); return d; };
  const perm = async (prompt) => {
    if (!FS.handle) return false;
    const o = { mode: "readwrite" };
    try { return (await FS.handle.queryPermission(o)) === "granted" || (prompt && (await FS.handle.requestPermission(o)) === "granted"); } catch { return false; }
  };
  async function fsWrite(prompt) {
    if (!FS.handle) return;
    if (!dataKeys().length) return;                                   // không ghi đè file tốt bằng dữ liệu rỗng
    if (!(await perm(prompt))) { FS.state = "perm"; return fsTell(); }
    try {
      const w = await FS.handle.createWritable(); await w.write(JSON.stringify(snapshot(), null, 1)); await w.close();
      FS.last = Date.now(); FS.state = "on"; FS.err = ""; localStorage.setItem(FSKEY, String(FS.last));
    } catch (e) { FS.state = "error"; FS.err = String(e && e.message || e); }
    fsTell();
  }
  let fsTimer = 0;
  const fsSchedule = () => { if (!FS.handle) return; clearTimeout(fsTimer); fsTimer = setTimeout(() => fsWrite(false), 3000); };
  if (FS.ok) {
    const origSet = Storage.prototype.setItem, origDel = Storage.prototype.removeItem;
    Storage.prototype.setItem = function (k, v) { origSet.call(this, k, v); if (this === localStorage && String(k).startsWith("nihongo-") && k !== FSKEY) fsSchedule(); };
    Storage.prototype.removeItem = function (k) { origDel.call(this, k); if (this === localStorage && String(k).startsWith("nihongo-") && k !== FSKEY) fsSchedule(); };
    idb("readonly", st => st.get("backup")).then(async h => {
      if (!h) return; FS.handle = h; FS.state = (await perm(false)) ? "on" : "perm"; fsTell();
    }).catch(() => {});
  }
  function applyBackup(txt) {                                          // trả về thông báo
    let d; try { d = JSON.parse(txt); } catch { return { ok: false, msg: "File không đọc được." }; }
    const ks = Object.keys(d || {}).filter(k => k.startsWith("nihongo-") && typeof d[k] === "string");
    if (!ks.length) return { ok: false, msg: "File này không phải bản sao lưu của khoá học." };
    if (!confirm(`Khôi phục ${ks.length} mục? Tiến độ hiện tại trong trình duyệt sẽ bị ghi đè.`)) return { ok: false, msg: "" };
    ks.forEach(k => { try { localStorage.setItem(k, d[k]); } catch {} });
    return { ok: true, msg: `Đã khôi phục ${ks.length} mục. Đang tải lại trang…` };
  }

  function backup(el) {
    const when = t => new Date(t).toLocaleString("vi-VN", { dateStyle: "short", timeStyle: "short" });
    let note = "";
    const mini = el.dataset.backup === "mini";
    const paint = () => {
      const t = +localStorage.getItem(FSKEY) || 0, stale = dataKeys().length && !FS.handle && (!t || Date.now() - t > 7 * DAY);
      if (mini) { el.innerHTML = stale ? `<div class="note"><strong>Nên sao lưu tiến độ.</strong> Đã hơn 7 ngày chưa sao lưu. <a href="${BASE.replace(/assets\/$/, "")}index.html#sao-luu">Mở phần sao lưu</a></div>` : ""; return; }
      let auto;
      if (!FS.ok) auto = `<p class="hint">Trình duyệt này (Safari, Firefox, iPad) chưa hỗ trợ tự động lưu vào file. Hãy dùng Chrome hoặc Edge trên máy tính, hoặc tải file sao lưu thủ công bên dưới.</p>`;
      else if (!FS.handle) auto = `<p><button class="btn primary" data-link>Bật tự động lưu vào file…</button> <span class="hint">Chọn một file .json (nên đặt trong iCloud Drive/Google Drive để có bản sao ngoài máy).</span></p>`;
      else auto = `<p>Tự động lưu: <strong>${esc(FS.handle.name)}</strong>${FS.state === "on" ? ` · lần cuối ${FS.last ? when(FS.last) : "chưa ghi"}` : FS.state === "perm" ? " · <b>cần cấp quyền lại</b>" : FS.state === "error" ? ` · lỗi: ${esc(FS.err)}` : ""}<br>
        ${FS.state === "perm" ? `<button class="btn primary" data-allow>Cho phép lại</button> ` : ""}<button class="btn" data-now>Lưu ngay</button> <button class="btn" data-load>Nạp từ file này</button> <button class="btn" data-unlink>Tắt tự động lưu</button></p>`;
      el.innerHTML = `<div class="note"><strong>Sao lưu tiến độ</strong> Tiến độ chỉ nằm trong trình duyệt này; xoá dữ liệu duyệt web là mất hết.
        ${t && !FS.handle ? `Lần sao lưu cuối: ${when(t)}.` : ""}${stale ? " <b>Nên sao lưu ngay.</b>" : ""}
        ${auto}
        <p><button class="btn" data-exp>Tải file sao lưu</button> <label class="btn" style="cursor:pointer">Nhập từ file…<input type="file" accept="application/json,.json" hidden data-imp></label>
        ${note ? `<span class="fb">${note}</span>` : ""}</p></div>`;
    };
    const say = m => { note = m; paint(); };
    document.addEventListener("nihongo-fs", paint);
    const reloadSoon = () => setTimeout(() => location.reload(), 900);
    el.addEventListener("click", async e => {
      const b = e.target.closest("button"); if (!b) return;
      if (b.hasAttribute("data-exp")) {
        try { localStorage.setItem(FSKEY, String(Date.now())); } catch {}
        const a = document.createElement("a"); a.href = URL.createObjectURL(new Blob([JSON.stringify(snapshot(), null, 1)], { type: "application/json" }));
        a.download = `nihongo-backup-${new Date().toISOString().slice(0, 10)}.json`; a.click(); setTimeout(() => URL.revokeObjectURL(a.href), 1000);
        say("Đã tải file sao lưu (xem thư mục Tải xuống).");
      } else if (b.hasAttribute("data-link")) {
        let h; try { h = await showSaveFilePicker({ suggestedName: "nihongo-backup.json", types: [{ description: "Sao lưu khoá học", accept: { "application/json": [".json"] } }] }); } catch { return; }
        FS.handle = h; await idb("readwrite", st => st.put(h, "backup")).catch(() => {});
        let existing = ""; try { existing = await (await h.getFile()).text(); } catch {}
        if (existing.trim()) {                                         // file đã có dữ liệu: hỏi nạp hay ghi đè
          const has = dataKeys().length;
          if (!has || confirm("File này đã có dữ liệu sao lưu.\nOK = nạp dữ liệu từ file vào trình duyệt.\nHuỷ = ghi đè file bằng tiến độ hiện tại.")) {
            const r = applyBackup(existing); FS.state = "on"; say(r.msg); if (r.ok) reloadSoon(); return;
          }
        }
        FS.state = "on"; await fsWrite(true); say("Đã bật tự động lưu.");
      } else if (b.hasAttribute("data-allow")) { await fsWrite(true); say(""); }
      else if (b.hasAttribute("data-now")) { await fsWrite(true); say(FS.state === "on" ? "Đã lưu." : ""); }
      else if (b.hasAttribute("data-load")) {
        if (!(await perm(true))) return say("Chưa được cấp quyền đọc file.");
        try { const r = applyBackup(await (await FS.handle.getFile()).text()); say(r.msg); if (r.ok) reloadSoon(); } catch (err) { say("Không đọc được file: " + err.message); }
      } else if (b.hasAttribute("data-unlink")) {
        FS.handle = null; FS.state = "off"; await idb("readwrite", st => st.delete("backup")).catch(() => {}); say("Đã tắt tự động lưu (file cũ vẫn còn trên máy).");
      }
    });
    el.addEventListener("change", e => {
      const f = e.target.closest("[data-imp]") && e.target.files[0]; if (!f) return;
      f.text().then(txt => { const r = applyBackup(txt); say(r.msg); if (r.ok) reloadSoon(); });
      e.target.value = "";
    });
    paint();
  }

  /* ---------- Cài lên màn hình chính + chạy offline (cần https hoặc localhost) ---------- */
  function pwa() {
    const root = BASE.replace(/assets\/$/, "");
    if (!document.querySelector('link[rel=manifest]')) {
      const l = $("link"); l.rel = "manifest"; l.href = root + "manifest.webmanifest"; document.head.append(l);
      const a = $("link"); a.rel = "apple-touch-icon"; a.href = root + "assets/icon-192.png"; document.head.append(a);
      const m = $("meta"); m.name = "theme-color"; m.content = "#243b6b"; document.head.append(m);
    }
    if ("serviceWorker" in navigator && /^https?:$/.test(location.protocol)) navigator.serviceWorker.register(root + "sw.js").catch(() => {});
  }

  function init() {
    document.querySelectorAll("[data-deck]").forEach(deck);
    document.querySelectorAll("[data-listen]").forEach(listen);
    document.querySelectorAll(".quiz[data-answer]").forEach(quiz);
    document.querySelectorAll("[data-write]").forEach(writer);
    document.querySelectorAll("[data-read]").forEach(reader);
    document.querySelectorAll("[data-rewrite]").forEach(el => { try { rewrite(el, JSON.parse(el.dataset.rewrite)); } catch {} });
    document.querySelectorAll("[data-build]").forEach(builder);
    document.querySelectorAll("[data-dialog]").forEach(dialog);
    document.querySelectorAll("[data-num]").forEach(numDrill);
    document.querySelectorAll("[data-progress]").forEach(progress);
    document.querySelectorAll("[data-stats]").forEach(stats);
    siteNav(); pwa();
    document.querySelectorAll("[data-backup]").forEach(backup);
    lessonDone();
    document.querySelectorAll("[data-due-count]").forEach(e => e.textContent = (window.CARDS || []).filter(c => isDue(c.id)).length);
  }
  document.readyState === "loading" ? document.addEventListener("DOMContentLoaded", init) : init();
  window.Nihongo = { speak, stats, dictation, modes, cardItem, newToday, deck, reader, listen, rewrite, recognize, shuffle, esc, grade, isDue };
})();
