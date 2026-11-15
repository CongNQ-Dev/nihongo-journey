/* Trang luyện tự chọn (practice.html): chọn chữ / từ muốn học, bốc ngẫu nhiên N mục,
   rồi luyện bằng flashcard, viết lại từ trí nhớ, gõ cách đọc hoặc nghe chọn. Không thay đổi lịch ôn Leitner.
   Cần nạp sau cards.js và nihongo.js. */
(function () {
  const N = window.Nihongo, CARDS = window.CARDS || [], esc = N.esc;
  const KEY = "nihongo-practice-v1";

  /* ---------- Kho chữ: đủ bảng kana (kể cả chữ chưa có thẻ ảnh) ---------- */
  const ROWS = [
    ["Hàng あ", "あいうえお", "a i u e o"],
    ["Hàng か", "かきくけこ", "ka ki ku ke ko"],
    ["Hàng さ", "さしすせそ", "sa shi su se so"],
    ["Hàng た", "たちつてと", "ta chi tsu te to"],
    ["Hàng な", "なにぬねの", "na ni nu ne no"],
    ["Hàng は", "はひふへほ", "ha hi fu he ho"],
    ["Hàng ま", "まみむめも", "ma mi mu me mo"],
    ["Hàng や", "やゆよ", "ya yu yo"],
    ["Hàng ら", "らりるれろ", "ra ri ru re ro"],
    ["わ・を・ん", "わをん", "wa o n"],
    ["Hàng が", "がぎぐげご", "ga gi gu ge go"],
    ["Hàng ざ", "ざじずぜぞ", "za ji zu ze zo"],
    ["Hàng だ", "だぢづでど", "da ji zu de do"],
    ["Hàng ば", "ばびぶべぼ", "ba bi bu be bo"],
    ["Hàng ぱ", "ぱぴぷぺぽ", "pa pi pu pe po"],
  ];
  const YOON = "き:k し:sh ち:ch に:n ひ:h み:m り:r ぎ:g じ:j び:b ぴ:p".split(" ").map(x => x.split(":"));
  const toKata = s => s.replace(/[ぁ-ゖ]/g, ch => String.fromCharCode(ch.charCodeAt(0) + 0x60));
  const cardByGlyph = {};
  CARDS.forEach(c => { if (c.type === "kana") cardByGlyph[c.glyph] = c; });

  function kanaItems(kata) {
    const out = [], add = (glyph, sound, group) => {
      const g = kata ? toKata(glyph) : glyph, c = cardByGlyph[g];
      out.push({ key: (kata ? "k:" : "h:") + g, label: g, group, read: sound, vn: group,
        card: c ? { ...c } : { id: "p-" + g, type: "kana", glyph: g, sound, vn: group } });
    };
    ROWS.forEach(([name, chars, ro]) => {
      const r = ro.split(" "); [...chars].forEach((ch, i) => add(ch, r[i], name));
    });
    YOON.forEach(([base, c]) => [["ゃ", "a"], ["ゅ", "u"], ["ょ", "o"]].forEach(([s, v]) =>
      add(base + s, (c === "j" || c === "sh" || c === "ch") ? c + v : c + "y" + v, "Âm ghép ゃゅょ")));
    if (kata) "ファ:fa フィ:fi フェ:fe フォ:fo ティ:ti ディ:di シェ:she ジェ:je チェ:che ウィ:wi ウェ:we ウォ:wo ヴ:vu".split(" ")
      .forEach(x => { const [g, s] = x.split(":"), c = cardByGlyph[g];
        out.push({ key: "k:" + g, label: g, group: "Âm ngoại lai", read: s, vn: "âm ngoại lai",
          card: c ? { ...c } : { id: "p-" + g, type: "kana", glyph: g, sound: s, vn: "âm ngoại lai" } }); });
    return out;
  }
  const vocabItems = CARDS.filter(c => c.type === "vocab").map(c => ({
    key: "v:" + c.id, label: c.word, group: "Minna bài " + (c.lesson - 11), read: c.romaji, vn: c.meaning, card: c }));

  const POOLS = { hira: kanaItems(false), kata: kanaItems(true), vocab: vocabItems };
  const ALL = {}; Object.values(POOLS).forEach(list => list.forEach(it => ALL[it.key] = it));

  /* ---------- Trạng thái (nhớ trong trình duyệt này) ---------- */
  let st = { tab: "hira", sel: [], n: 5 };
  try { st = { ...st, ...JSON.parse(localStorage.getItem(KEY)) }; } catch {}
  let sel = new Set(st.sel.filter(k => ALL[k])), picked = [], mode = "cards";
  const save = () => { try { localStorage.setItem(KEY, JSON.stringify({ tab: st.tab, sel: [...sel], n: st.n })); } catch {} };
  const root = document.querySelector("[data-practice]");
  const TABS = { hira: "Hiragana", kata: "Katakana", vocab: "Từ vựng" };
  const clampN = v => Math.max(1, Math.min(Math.round(+v) || 5, 100));
  const tabOf = k => k[0] === "h" ? "hira" : k[0] === "k" ? "kata" : "vocab";
  const chosen = () => [...sel].filter(k => tabOf(k) === st.tab);   // chỉ lấy lựa chọn của tab đang mở
  const pool = () => chosen().length ? chosen().map(k => ALL[k]) : POOLS[st.tab].slice();

  /* ---------- Màn 1: chọn ---------- */
  function setup() {
    const list = POOLS[st.tab], groups = [...new Set(list.map(it => it.group))];
    const p = pool(), n = Math.min(st.n, p.length);
    const nc = chosen().length;
    const summary = nc
      ? `Đã chọn <b>${nc}</b> mục trong ${TABS[st.tab]}`
      : `Chưa chọn riêng mục nào — sẽ bốc từ cả kho <b>${TABS[st.tab]}</b> (${list.length} mục)`;
    root.innerHTML = `
      <div class="pr-tabs" role="tablist">${Object.entries(TABS).map(([k, v]) =>
        `<button data-tab="${k}" class="${k === st.tab ? "on" : ""}">${v}</button>`).join("")}</div>
      <h2 class="pr-h">1. Chọn nhóm muốn học <small>(không bắt buộc)</small></h2>
      <div class="pr-groups">${groups.map(g => {
        const items = list.filter(it => it.group === g), c = items.filter(it => sel.has(it.key)).length;
        const prev = st.tab === "vocab" ? `${items.length} từ` : items.slice(0, 5).map(it => it.label).join(" ");
        return `<button class="gcard${c === items.length ? " on" : c ? " part" : ""}" data-group="${esc(g)}"><b>${esc(g)}</b><span class="jp">${esc(prev)}</span>${c ? `<em>${c}/${items.length}</em>` : ""}</button>`;
      }).join("")}</div>
      <details class="pr-more"><summary>Hoặc chọn từng ${st.tab === "vocab" ? "từ" : "chữ"} một</summary>
        <div class="pr-grid${st.tab === "vocab" ? " words" : ""}">${list.map(it =>
          `<button class="cell jp${sel.has(it.key) ? " on" : ""}" data-key="${esc(it.key)}">${esc(it.label)}${st.tab === "vocab" ? `<small>${esc(it.vn)}</small>` : ""}</button>`).join("")}</div>
      </details>
      <div class="pr-dock">
        <p class="pr-sum">${summary}</p>
        <div class="pr-quick">${nc < list.length ? `<button class="chip" data-selall>Chọn cả ${list.length}</button>` : ""}${nc ? `<button class="chip" data-clear>Bỏ chọn</button>` : ""}</div>
        <div class="pr-row">
          <span class="pr-lbl">2. Số mục mỗi lượt</span>
          <span class="pr-step"><button data-dec aria-label="Giảm">−</button><input type="number" min="1" max="${p.length}" value="${n}" data-n><button data-inc aria-label="Tăng">+</button></span>
          ${[5, 10, 20].filter(v => v < p.length).map(v => `<button class="chip${n === v ? " on" : ""}" data-setn="${v}">${v}</button>`).join("")}
          <span class="pr-max">tối đa ${p.length}</span>
        </div>
        <div class="pr-row">
          <button class="btn primary big" data-draw>Bốc ${n} mục ngẫu nhiên &amp; học</button>
          ${p.length > 1 ? `<button class="btn big" data-all>Học hết ${p.length} mục${nc ? " đã chọn" : ""}</button>` : ""}
        </div>
      </div>`;
    save();
  }

  /* ---------- Màn 2: luyện ---------- */
  function session() {
    root.innerHTML = `
      <div class="pr-sess">
        <div class="pr-sess-head"><button class="btn" data-back>← Chọn lại</button>
          <strong>${picked.length} mục ngẫu nhiên</strong>
          <button class="btn" data-redraw>Bốc lượt khác</button></div>
        <div class="pr-modes">${[["cards", "Flashcard"], ["write", "Viết lại"], ["recog", "Trắc nghiệm"], ["read", "Gõ cách đọc"], ["listen", "Nghe chọn"]].map(([k, v]) =>
          `<button class="btn${k === mode ? " primary" : ""}" data-mode="${k}">${v}</button>`).join("")}</div>
        <div class="pr-stage"></div>
        <details class="pr-more"><summary>Xem ${picked.length} mục vừa bốc</summary>
          <p class="pr-picked-list">${picked.map(it => `<button class="say jp" data-say="${esc(it.label)}">${esc(it.label)}</button> <span class="hint">${esc(it.read)}${st.tab === "vocab" || it.key[0] === "v" ? " · " + esc(it.vn) : ""}</span>`).join("<br>")}</p></details>
      </div>`;
    run();
    window.scrollTo({ top: 0, behavior: "smooth" });
  }
  function run() {
    root.querySelectorAll("[data-mode]").forEach(b => b.classList.toggle("primary", b.dataset.mode === mode));
    const stage = root.querySelector(".pr-stage"); stage.innerHTML = "";
    const el = document.createElement("div"); stage.append(el);
    if (mode === "cards") N.deck(el, { cards: picked.map(it => it.card) });
    if (mode === "write") N.rewrite(el, picked.map(it => ({ text: it.label, prompt: it.read,
      hint: it.key[0] === "v" ? it.vn : (it.key[0] === "k" ? "katakana" : "hiragana") })));
    if (mode === "recog") {
      const conv = it => ({ text: it.label, romaji: it.read, vn: it.vn, kind: it.key[0] === "v" ? "vocab" : "kana" });
      N.recognize(el, picked.map(conv), { pool: POOLS[st.tab].map(conv) });
    }
    if (mode === "read") { el.dataset.read = JSON.stringify(picked.map(it => [it.label, it.read, it.vn])); N.reader(el); }
    if (mode === "listen") {
      if (picked.length < 2) { el.className = "note"; el.textContent = "Cần ít nhất 2 mục để nghe chọn — hãy bốc nhiều hơn."; return; }
      el.dataset.listen = picked.map(it => it.label.replace(/\s+/g, "")).join(" ");
      el.dataset.rounds = Math.min(20, Math.max(8, picked.length * 2)); N.listen(el);
    }
  }
  function draw(all) {
    const p = N.shuffle(pool());
    picked = all ? p : p.slice(0, Math.min(clampN(st.n), p.length)); mode = "cards"; session();
  }

  root.addEventListener("click", e => {
    const b = e.target.closest("button"); if (!b || b.closest(".deck, .quiz, .rewrite, .recog, .pr-picked-list")) return;
    const d = b.dataset;
    if (d.tab) { st.tab = d.tab; setup(); }
    else if (d.key) { sel.has(d.key) ? sel.delete(d.key) : sel.add(d.key); keep(setup); }
    else if (d.group != null) {
      const keys = POOLS[st.tab].filter(it => it.group === d.group).map(it => it.key);
      const allOn = keys.every(k => sel.has(k)); keys.forEach(k => allOn ? sel.delete(k) : sel.add(k)); keep(setup);
    }
    else if (b.hasAttribute("data-clear")) { chosen().forEach(k => sel.delete(k)); keep(setup); }
    else if (d.setn) { st.n = +d.setn; keep(setup); }
    else if (b.hasAttribute("data-dec")) { st.n = clampN(Math.min(st.n, pool().length) - 1); keep(setup); }
    else if (b.hasAttribute("data-inc")) { st.n = Math.min(pool().length, clampN(Math.min(st.n, pool().length) + 1)); keep(setup); }
    else if (b.hasAttribute("data-selall")) { POOLS[st.tab].forEach(it => sel.add(it.key)); keep(setup); }
    else if (b.hasAttribute("data-draw")) draw(false);
    else if (b.hasAttribute("data-all")) draw(true);
    else if (b.hasAttribute("data-redraw")) draw(false);
    else if (b.hasAttribute("data-back")) setup();
    else if (d.mode) { mode = d.mode; run(); }
  });
  root.addEventListener("change", e => { if (e.target.matches("[data-n]")) { st.n = Math.min(clampN(e.target.value), pool().length); keep(setup); } });
  /* Vẽ lại màn chọn mà không làm trang nhảy lên đầu và giữ ô "chọn từng chữ" đang mở. */
  function keep(fn) {
    const y = scrollY, open = !!root.querySelector(".pr-more[open]"); fn();
    if (open) root.querySelector(".pr-more").open = true; scrollTo(0, y);
  }
  setup();
})();
