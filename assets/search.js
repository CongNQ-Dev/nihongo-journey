/* Tìm kiếm chung trên thẻ (kana, từ vựng, kanji) và mẫu ngữ pháp / câu mẫu. Cần cards.js, nihongo.js, sentences.js. */
(function () {
  const N = window.Nihongo, CARDS = window.CARDS || [], SENT = window.SENTENCES || {}, FILES = window.LESSON_FILES || {}, esc = N.esc;
  const root = document.querySelector("[data-search]"); if (!root) return;
  /* bỏ dấu tiếng Việt + chữ thường; đ → d */
  const fold = s => String(s || "").toLowerCase().replace(/đ/g, "d").normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/ō/g, "ou").replace(/ū/g, "uu");
  const kata2hira = s => s.replace(/[ァ-ヶ]/g, ch => String.fromCharCode(ch.charCodeAt(0) - 0x60));
  const link = n => FILES[n] ? `<a href="lessons/${FILES[n]}.html">bài ${String(n).padStart(4, "0")}</a>` : "";

  const docs = [];
  CARDS.forEach(c => {
    if (c.type === "vocab") docs.push({ kind: "Từ vựng", big: c.word, sub: `${c.romaji}${c.kanji ? " · " + c.kanji : ""} — ${c.meaning}`, say: c.word, n: c.lesson,
      hay: [c.word, c.kanji, c.romaji, c.meaning, c.ex, c.exvn] });
    else if (c.type === "kanji") docs.push({ kind: "Kanji", big: c.glyph, sub: `${c.vn} · ${c.sound} · ${c.word} (${c.romaji}) — ${c.meaning}`, say: c.say || c.glyph, n: c.lesson, hay: [c.glyph, c.vn, c.sound, c.word, c.romaji, c.meaning] });
    else docs.push({ kind: "Kana", big: c.glyph, sub: `${c.sound}${c.word ? " · " + c.word + " — " + c.meaning : ""}`, say: c.glyph, n: c.lesson, hay: [c.glyph, c.sound, c.word, c.meaning, c.romaji] });
  });
  Object.keys(SENT).forEach(k => {
    const n = +k + 11;
    SENT[k].grammar.forEach(g => docs.push({ kind: "Ngữ pháp", big: g[0], sub: g[1] + " — " + g[2].map(x => x[0]).slice(0, 2).join(" / "), n, hay: [g[0], g[1], ...g[2].flat()] }));
  });
  docs.forEach(d => { d.h = fold(kata2hira(d.hay.filter(Boolean).join(" | "))); });
  let q = "";
  root.innerHTML = `<input class="jp" type="search" placeholder="Gõ để tìm…" autofocus style="width:100%;font-size:1.2rem;padding:.6rem .8rem;border:1px solid var(--rule);border-radius:10px;background:var(--card);color:var(--fg)">
    <p class="hint" data-count></p><div data-out></div>`;
  const out = root.querySelector("[data-out]"), cnt = root.querySelector("[data-count]"), input = root.querySelector("input");
  function paint() {
    const t = fold(kata2hira(q.trim()));
    if (!t) { cnt.textContent = `${docs.length} mục để tìm: thẻ kana, từ vựng, kanji và mẫu ngữ pháp.`; out.innerHTML = ""; return; }
    const hit = docs.filter(d => d.h.includes(t));
    hit.sort((a, b) => (b.big === q.trim()) - (a.big === q.trim()) || (a.h.indexOf(t) - b.h.indexOf(t)));
    cnt.textContent = hit.length ? `${hit.length} kết quả${hit.length > 60 ? " (hiện 60 đầu)" : ""}` : "Không thấy. Thử viết không dấu hoặc gõ ngắn hơn.";
    out.innerHTML = hit.slice(0, 60).map(d => `<div class="kanji-item" style="grid-template-columns:5.5rem 1fr;margin:.5rem 0;padding-bottom:.6rem">
      <div class="jp" style="font-size:${[...d.big].length > 4 ? "1rem" : "1.7rem"};word-break:break-all">${esc(d.big)}</div>
      <div><span class="hint">${d.kind}</span> ${link(d.n)}${d.say ? ` <button class="say" data-say="${esc(d.say)}">nghe</button>` : ""}<br>${esc(d.sub)}</div></div>`).join("");
  }
  input.addEventListener("input", () => { q = input.value; paint(); });
  paint();
})();
