/* Đề thi thử kiểu 文字・語彙 (cách đọc chữ Hán, cách viết, nghĩa), TỰ SINH từ từ vựng của khoá.
   KHÔNG phải đề JLPT chính thức. Mức N5 ≈ Minna 1–25, N4 ≈ Minna 26–50 chỉ là ước lượng theo thứ tự giáo trình.
   Cần nạp sau cards.js và nihongo.js. Không ghi vào lịch ôn Leitner. */
(function () {
  const N = window.Nihongo, esc = N.esc, shuffle = N.shuffle, host = document.querySelector("[data-mock]");
  if (!host || !N) return;
  const HKEY = "nihongo-mock-v1", KANJI = /[一-龥々]/;
  const hist = () => { try { return JSON.parse(localStorage.getItem(HKEY)) || []; } catch { return []; } };
  const pushHist = r => { try { localStorage.setItem(HKEY, JSON.stringify([r, ...hist()].slice(0, 20))); } catch {} };

  /* Từ dùng được: đọc bằng kana thuần, có chữ Hán thuần (không ／ ～ số). */
  const WORDS = (window.CARDS || []).filter(c => c.type === "vocab" && c.kanji && /^[ぁ-ゖァ-ヶー]+$/.test(c.word)
    && /^[぀-ヿ一-龥々ー]+$/.test(c.kanji) && KANJI.test(c.kanji));
  const level = c => (c.lesson <= 36 ? "N5" : "N4");           // file bài = bài Minna + 11

  const sim = (a, b) => { let s = 0; const set = new Set(a); for (const ch of b) if (set.has(ch)) s++; return s - Math.abs(a.length - b.length) * 0.7; };
  function distract(pool, correct, key, n) {
    const seen = new Set([correct]), cand = [];
    for (const c of pool) { const v = c[key]; if (!seen.has(v)) { seen.add(v); cand.push([sim(correct, v) + Math.random(), v]); } }
    cand.sort((x, y) => y[0] - x[0]);
    return shuffle(cand.slice(0, 10).map(x => x[1])).slice(0, n);
  }
  function make(c, type, pool) {
    if (type === "yomi") return { c, type, q: c.kanji, ask: "Chữ Hán này đọc là gì?", ans: c.word, opts: [c.word, ...distract(pool, c.word, "word", 3)], jp: true };
    if (type === "hyouki") return { c, type, q: c.word, ask: "Viết từ này bằng chữ Hán:", ans: c.kanji, opts: [c.kanji, ...distract(pool, c.kanji, "kanji", 3)], jp: true };
    const others = shuffle(pool.filter(x => x.meaning !== c.meaning)).slice(0, 3).map(x => x.meaning);
    return { c, type, q: c.kanji, ask: "Từ này có nghĩa là gì?", ans: c.meaning, opts: [c.meaning, ...others], jp: false };
  }
  const NAMES = { yomi: "Đọc chữ Hán (読み方)", hyouki: "Viết chữ Hán (表記)", imi: "Nghĩa của từ (語彙)" };

  function setup() {
    const h = hist();
    host.innerHTML = `<div class="note"><strong>Đây không phải đề JLPT chính thức.</strong> Đề được máy tự sinh từ từ vựng của khoá, theo dạng câu hỏi phần 文字・語彙 (đọc chữ Hán, viết chữ Hán, nghĩa của từ). Mức N5 ≈ Minna bài 1–25, N4 ≈ bài 26–50 chỉ là ước lượng theo thứ tự giáo trình, không phải danh sách từ chính thức của JLPT. Đáp án sai gần đúng được chọn tự động nên đôi khi dễ hoặc khó hơn đề thật. Chữ Hán đã đối chiếu với JMdict (xem trang Nguồn).</div>
      <p><b>Mức:</b> <label><input type="radio" name="lv" value="N5" checked> N5 (bài 1–25)</label> <label><input type="radio" name="lv" value="N4"> N4 (bài 26–50)</label> <label><input type="radio" name="lv" value="all"> cả hai</label></p>
      <p><b>Dạng câu:</b> ${Object.entries(NAMES).map(([k, v]) => `<label><input type="checkbox" name="ty" value="${k}" checked> ${v}</label>`).join(" ")}</p>
      <p><b>Số câu:</b> <label><input type="radio" name="n" value="20" checked> 20</label> <label><input type="radio" name="n" value="30"> 30</label> <label><input type="radio" name="n" value="50"> 50</label></p>
      <p><button class="btn primary" data-go>Bắt đầu làm bài</button></p>
      ${h.length ? `<p class="hint">Các lần gần đây: ${h.slice(0, 6).map(r => `${r.lv} ${r.ok}/${r.n}`).join(" · ")}</p>` : ""}`;
    host.querySelector("[data-go]").onclick = () => {
      const lv = host.querySelector('[name="lv"]:checked').value, n = +host.querySelector('[name="n"]:checked').value;
      const types = [...host.querySelectorAll('[name="ty"]:checked')].map(x => x.value);
      if (!types.length) return alert("Chọn ít nhất một dạng câu.");
      const pool = WORDS.filter(c => lv === "all" || level(c) === lv);
      if (pool.length < 12) return alert("Chưa đủ từ để ra đề.");
      start(pool, types, Math.min(n, pool.length), lv);
    };
  }

  function start(pool, types, n, lv) {
    const picks = shuffle(pool.slice()).slice(0, n), qs = picks.map((c, i) => make(c, types[i % types.length], pool));
    shuffle(qs); let i = 0, ok = 0; const wrong = [], t0 = Date.now();
    function show() {
      if (i >= qs.length) return done();
      const q = qs[i], opts = shuffle(q.opts.slice());
      host.innerHTML = `<p class="q"><span class="score">Câu ${i + 1}/${qs.length} · đúng ${ok}</span>${esc(q.ask)}</p>
        <p class="word jp" style="font-size:2rem"><u>${esc(q.q)}</u></p>
        <div class="opts">${opts.map(o => `<button class="${q.jp ? "jp" : ""}" data-o="${esc(o)}">${esc(o)}</button>`).join("")}</div><p class="fb"></p>`;
      const fb = host.querySelector(".fb");
      host.querySelectorAll(".opts button").forEach(b => b.onclick = () => {
        if (host.dataset.lock) return; host.dataset.lock = 1;
        const good = b.dataset.o === q.ans; if (good) ok++; else wrong.push(q);
        host.querySelectorAll(".opts button").forEach(x => { if (x.dataset.o === q.ans) x.classList.add("right"); });
        if (!good) b.classList.add("wrong");
        fb.className = "fb " + (good ? "good" : "bad");
        fb.innerHTML = `${good ? "Đúng" : "Chưa đúng"}: <span class="jp">${esc(q.c.kanji)}</span> (${esc(q.c.word)}) — ${esc(q.c.meaning)} <button class="btn primary" data-next>${i + 1 >= qs.length ? "Xem kết quả" : "Câu tiếp →"}</button>`;
        N.speak(q.c.word);
        fb.querySelector("[data-next]").onclick = () => { delete host.dataset.lock; i++; show(); };
      });
    }
    function done() {
      const secs = Math.round((Date.now() - t0) / 1000), pct = Math.round(ok / qs.length * 100);
      pushHist({ lv, ok, n: qs.length, secs, at: Date.now() });
      const by = {}; qs.forEach(q => { const r = by[q.type] || (by[q.type] = [0, 0]); r[1]++; if (!wrong.includes(q)) r[0]++; });
      host.innerHTML = `<p class="fb ${pct >= 80 ? "good" : "bad"}">Kết quả: ${ok}/${qs.length} (${pct}%) · ${Math.floor(secs / 60)} phút ${secs % 60} giây.</p>
        <ul>${Object.entries(by).map(([k, [a, b]]) => `<li>${NAMES[k]}: ${a}/${b}</li>`).join("")}</ul>
        ${wrong.length ? `<p><b>Các câu sai (${wrong.length}):</b></p><ul>${wrong.map(q => `<li><span class="jp">${esc(q.c.kanji)}</span> (${esc(q.c.word)}) — ${esc(q.c.meaning)} <small>(bài ${q.c.lesson - 11})</small></li>`).join("")}</ul>` : "<p>Không sai câu nào.</p>"}
        <p class="hint">Tỉ lệ này chỉ cho biết bạn nhớ từ của khoá đến đâu, không dự đoán điểm JLPT thật.</p>
        <p><button class="btn primary" data-again>Làm đề mới</button></p>`;
      host.querySelector("[data-again]").onclick = setup;
    }
    show();
  }
  setup();
})();
