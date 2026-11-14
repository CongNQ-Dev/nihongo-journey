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
  function speak(text) {
    if (!("speechSynthesis" in window)) return alert("Trình duyệt này không có giọng đọc. Hãy mở bằng Chrome hoặc Safari.");
    speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(text);
    u.lang = "ja-JP"; if (voice) u.voice = voice; u.rate = 0.8;
    speechSynthesis.speak(u);
  }
  document.addEventListener("click", e => { const b = e.target.closest("[data-say]"); if (b) speak(b.dataset.say); });

  /* ---------- Lịch ôn Leitner ---------- */
  const DAYS = [0, 1, 3, 7, 14], DAY = 864e5, KEY = "nihongo-srs-v1";
  const load = () => { try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch { return {}; } };
  const save = s => { try { localStorage.setItem(KEY, JSON.stringify(s)); } catch {} };
  function grade(id, ok) {
    const s = load(), cur = s[id] || { box: 0 };
    const box = ok ? Math.min(cur.box + 1, DAYS.length - 1) : 0;
    s[id] = { box, due: Date.now() + DAYS[box] * DAY }; save(s);
  }
  const isDue = id => { const c = load()[id]; return !!c && c.due <= Date.now(); };
  const isNew = id => !load()[id];

  /* ---------- Flashcard ---------- */
  function deck(el) {
    const review = el.hasAttribute("data-due");
    let queue = (window.CARDS || []).filter(c => review ? isDue(c.id) : String(c.lesson) === el.dataset.lesson);
    if (review) queue.sort(() => Math.random() - .5);
    const total = queue.length; let done = 0;
    el.classList.add("deck");
    function show() {
      el.innerHTML = "";
      if (!queue.length) {
        const fresh = (window.CARDS || []).filter(c => isNew(c.id)).length;
        el.append($("div", "deck-done", review && !total
          ? `Hôm nay không có thẻ nào đến hạn.${fresh ? ` Còn ${fresh} thẻ chưa học — mở bài học tương ứng để học lần đầu.` : ""}`
          : `Xong ${total} thẻ. Thẻ “nhớ rồi” sẽ quay lại sau 1, 3, 7, 14 ngày ở trang ôn tập.`));
        return;
      }
      const c = queue[0];
      const hl = c.word.replace(c.glyph, `<b>${c.glyph}</b>`);
      el.append($("div", "deck-bar", `<span>Thẻ ${done + 1} / ${total}</span><span>${review ? "Ôn tập" : "Học mới"}</span>`));
      const card = $("div", "fc");
      const photo = $("figure", "fc-photo" + (review ? " veiled" : ""));
      photo.style.margin = 0;
      photo.innerHTML = `<img src="${BASE}${c.img}" alt="${review ? "" : c.meaning}"><div class="fc-glyph">${c.glyph}</div><figcaption>Ảnh: ${c.credit}</figcaption>`;
      const body = $("div", "fc-body");
      body.innerHTML = `<p class="fc-prompt">Chữ này đọc là gì? Đọc to lên, rồi lật thẻ.</p>
        <div class="fc-actions"><button class="btn primary" data-act="flip">Lật thẻ</button></div>`;
      card.append(photo, body); el.append(card);
      body.addEventListener("click", e => {
        const act = e.target.dataset.act; if (!act) return;
        if (act === "flip") {
          photo.classList.remove("veiled"); speak(c.glyph);
          body.innerHTML = `<p class="fc-answer"><span class="sound">${c.sound}</span><span class="hint">${c.vn}</span>
              <button class="say" data-say="${c.glyph}">nghe lại</button></p>
            <p class="fc-word"><span class="jp">${hl}</span> &nbsp;${c.romaji} — ${c.meaning}
              <button class="say" data-say="${c.word}">nghe từ</button></p>
            <div class="fc-actions"><button class="btn again" data-act="no">Chưa nhớ</button>
              <button class="btn ok" data-act="yes">Nhớ rồi</button></div>`;
        } else {
          const ok = act === "yes"; grade(c.id, ok); queue.shift();
          if (ok) done++; else queue.push(c);
          show();
        }
      });
    }
    show();
  }

  /* ---------- Quiz nghe ---------- */
  function listen(el) {
    const items = [...el.dataset.listen], rounds = +el.dataset.rounds || 10;
    let n = 0, score = 0, target = null, locked = false;
    el.classList.add("quiz");
    el.innerHTML = `<p class="q"><span class="score"></span>Bấm nghe, rồi chọn chữ vừa nghe được.</p>
      <p><button class="btn primary" data-play>▶ Nghe</button></p>
      <div class="opts">${items.map(k => `<button class="jp" data-k="${k}">${k}</button>`).join("")}</div><p class="fb"></p>`;
    const fb = el.querySelector(".fb"), sc = el.querySelector(".score");
    const next = () => {
      locked = false;
      el.querySelectorAll(".opts button").forEach(b => b.className = "jp");
      if (n >= rounds) { fb.className = "fb " + (score >= rounds * .9 ? "good" : "bad"); fb.textContent = `Kết quả: ${score}/${rounds}. ${score >= rounds * .9 ? "Tai bạn đã phân biệt được 5 âm này." : "Bấm “Nghe” để làm lại một lượt nữa."}`; n = 0; score = 0; target = null; return; }
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

  function init() {
    document.querySelectorAll("[data-deck]").forEach(deck);
    document.querySelectorAll("[data-listen]").forEach(listen);
    document.querySelectorAll(".quiz[data-answer]").forEach(quiz);
    document.querySelectorAll("[data-write]").forEach(writer);
    document.querySelectorAll("[data-due-count]").forEach(e => e.textContent = (window.CARDS || []).filter(c => isDue(c.id)).length);
  }
  document.readyState === "loading" ? document.addEventListener("DOMContentLoaded", init) : init();
  window.Nihongo = { speak };
})();
