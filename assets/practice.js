/* Trang luyện tự chọn (luyen-tap.html): chọn chữ / từ muốn học, bốc ngẫu nhiên N mục,
   rồi luyện bằng flashcard, gõ cách đọc hoặc nghe chọn. Không thay đổi lịch ôn Leitner.
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
  let sel = new Set(st.sel.filter(k => ALL[k])), picked = [];
  const save = () => { try { localStorage.setItem(KEY, JSON.stringify({ tab: st.tab, sel: [...sel], n: st.n })); } catch {} };

  const root = document.querySelector("[data-practice]");
  root.innerHTML = `
    <div class="pr-tabs" role="tablist">
      <button data-tab="hira">Hiragana</button><button data-tab="kata">Katakana</button><button data-tab="vocab">Từ vựng</button>
    </div>
    <p class="pr-help">Bấm từng ô để chọn. Bấm tên nhóm để chọn / bỏ cả nhóm. Có thể chọn lẫn cả ba kho.</p>
    <div class="pr-groups"></div>
    <div class="pr-grid"></div>
    <div class="pr-bar">
      <span class="pr-count"></span>
      <button class="btn" data-clear>Bỏ chọn hết</button>
    </div>
    <div class="pr-draw">
      <label>Bốc ngẫu nhiên <input type="number" min="1" max="200" step="1" data-n> mục</label>
      <span class="pr-from"></span>
      <button class="btn primary" data-draw>Bốc</button>
      <button class="btn" data-all>Học hết mục đã chọn</button>
    </div>
    <div class="pr-picked" hidden>
      <p class="pr-picked-list"></p>
      <div class="pr-modes">
        <button class="btn primary" data-mode="cards">Flashcard</button>
        <button class="btn" data-mode="read">Gõ cách đọc</button>
        <button class="btn" data-mode="listen">Nghe chọn</button>
        <button class="btn" data-draw>Bốc lại</button>
      </div>
      <div class="pr-stage"></div>
    </div>`;
  const q = s => root.querySelector(s);
  const nInput = q("[data-n]"); nInput.value = st.n;

  function render() {
    root.querySelectorAll("[data-tab]").forEach(b => b.classList.toggle("on", b.dataset.tab === st.tab));
    const list = POOLS[st.tab], groups = [...new Set(list.map(it => it.group))];
    q(".pr-groups").innerHTML = groups.map(g => {
      const keys = list.filter(it => it.group === g).map(it => it.key), n = keys.filter(k => sel.has(k)).length;
      return `<button class="chip${n === keys.length ? " on" : n ? " part" : ""}" data-group="${esc(g)}">${esc(g)}${n ? ` · ${n}` : ""}</button>`;
    }).join("");
    q(".pr-grid").className = "pr-grid" + (st.tab === "vocab" ? " words" : "");
    q(".pr-grid").innerHTML = list.map(it =>
      `<button class="cell jp${sel.has(it.key) ? " on" : ""}" data-key="${esc(it.key)}" title="${esc(it.read + " · " + it.vn)}">${esc(it.label)}${st.tab === "vocab" ? `<small>${esc(it.vn)}</small>` : ""}</button>`).join("");
    const by = { hira: 0, kata: 0, vocab: 0 };
    sel.forEach(k => by[k[0] === "h" ? "hira" : k[0] === "k" ? "kata" : "vocab"]++);
    q(".pr-count").textContent = sel.size
      ? `Đã chọn ${sel.size} mục (hiragana ${by.hira}, katakana ${by.kata}, từ vựng ${by.vocab})`
      : "Chưa chọn mục nào — sẽ bốc từ toàn bộ kho đang mở.";
    q(".pr-from").textContent = sel.size ? `trong ${sel.size} mục đã chọn` : `trong ${list.length} mục của kho này`;
    q("[data-all]").disabled = !sel.size;
    save();
  }

  function pool() { return sel.size ? [...sel].map(k => ALL[k]) : POOLS[st.tab].slice(); }
  function draw(all) {
    const p = N.shuffle(pool());
    st.n = Math.max(1, Math.min(+nInput.value || 5, 200)); nInput.value = st.n; save();
    picked = all ? p : p.slice(0, st.n);
    q(".pr-picked").hidden = false;
    q(".pr-picked-list").innerHTML = `<strong>${picked.length} mục:</strong> ` +
      picked.map(it => `<button class="say jp" data-say="${esc(it.label)}">${esc(it.label)}</button>`).join(" ");
    start("cards");
    q(".pr-picked").scrollIntoView({ behavior: "smooth", block: "start" });
  }

  function start(mode) {
    root.querySelectorAll("[data-mode]").forEach(b => b.classList.toggle("primary", b.dataset.mode === mode));
    const stage = q(".pr-stage"); stage.innerHTML = "";
    const el = document.createElement("div"); stage.append(el);
    if (mode === "cards") N.deck(el, { cards: picked.map(it => it.card) });
    if (mode === "read") { el.dataset.read = JSON.stringify(picked.map(it => [it.label, it.read, it.vn])); N.reader(el); }
    if (mode === "listen") {
      if (picked.length < 2) { el.className = "note"; el.textContent = "Cần ít nhất 2 mục để nghe chọn — hãy bốc nhiều hơn."; return; }
      el.dataset.listen = picked.map(it => it.label.replace(/\s+/g, "")).join(" ");
      el.dataset.rounds = Math.min(20, Math.max(10, picked.length * 2)); N.listen(el);
    }
  }

  root.addEventListener("click", e => {
    const b = e.target.closest("button"); if (!b) return;
    if (b.dataset.tab) { st.tab = b.dataset.tab; render(); }
    else if (b.dataset.key) { sel.has(b.dataset.key) ? sel.delete(b.dataset.key) : sel.add(b.dataset.key); render(); }
    else if (b.dataset.group != null) {
      const keys = POOLS[st.tab].filter(it => it.group === b.dataset.group).map(it => it.key);
      const allOn = keys.every(k => sel.has(k)); keys.forEach(k => allOn ? sel.delete(k) : sel.add(k)); render();
    }
    else if (b.hasAttribute("data-clear")) { sel.clear(); render(); }
    else if (b.hasAttribute("data-draw")) draw(false);
    else if (b.hasAttribute("data-all")) draw(true);
    else if (b.dataset.mode) start(b.dataset.mode);
  });
  nInput.addEventListener("change", () => { st.n = Math.max(1, +nInput.value || 5); save(); });
  render();
})();
