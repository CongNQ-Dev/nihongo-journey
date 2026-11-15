/* Sổ tay viết tay: canvas toàn trang, nét lưu dạng vector trong localStorage "nihongo-notebook-v1"
   (tự nằm trong file sao lưu vì khoá bắt đầu bằng "nihongo-"). */
(function () {
  "use strict";
  const KEY = "nihongo-notebook-v1", W = 1000, H = 1414, SCALE = 2;
  const root = document.querySelector("[data-notebook]");
  if (!root) return;

  const PAPERS = { blank: "Giấy trắng", lined: "Kẻ ngang", grid: "Ô vuông", genkou: "Ô chữ genkou" };
  const COLORS = ["#1d1d1f", "#c0392b", "#1f5fbf", "#2a7a3b"];
  let data = { cur: 0, pages: [{ paper: "lined", strokes: [] }] };
  try { const d = JSON.parse(localStorage.getItem(KEY)); if (d && Array.isArray(d.pages) && d.pages.length) data = d; } catch {}
  data.cur = Math.min(Math.max(+data.cur || 0, 0), data.pages.length - 1);

  const hist = new WeakMap();           // trang → { undo: [], redo: [] } (ảnh chụp mảng nét)
  const hs = p => { let h = hist.get(p); if (!h) hist.set(p, h = { undo: [], redo: [] }); return h; };
  const page = () => data.pages[data.cur];
  let tool = "pen", color = COLORS[0], width = 3, penSeen = false, saveTimer = 0, saveWarned = false;

  root.innerHTML = `
    <div class="nb-bar">
      <div class="nb-group" role="group" aria-label="Công cụ">
        <button class="btn primary" data-tool="pen">Bút</button>
        <button class="btn" data-tool="eraser">Tẩy</button>
      </div>
      <div class="nb-group nb-colors" role="group" aria-label="Màu">${COLORS.map((c, i) => `<button class="nb-sw${i ? "" : " on"}" data-color="${c}" style="background:${c}" aria-label="Màu ${i + 1}"></button>`).join("")}</div>
      <label class="nb-group">Nét <input type="range" min="1" max="10" value="3" data-width></label>
      <label class="nb-group">Giấy <select data-paper>${Object.entries(PAPERS).map(([k, v]) => `<option value="${k}">${v}</option>`).join("")}</select></label>
      <div class="nb-group">
        <button class="btn" data-act="undo">Hoàn tác</button><button class="btn" data-act="redo">Làm lại</button>
        <button class="btn" data-act="clear">Xoá trang</button>
      </div>
      <div class="nb-group">
        <button class="btn" data-act="prev" aria-label="Trang trước">‹</button>
        <span data-pageno>1 / 1</span>
        <button class="btn" data-act="next" aria-label="Trang sau">›</button>
        <button class="btn" data-act="add">+ Trang</button>
        <button class="btn" data-act="del">Xoá trang này</button>
      </div>
      <div class="nb-group"><button class="btn primary" data-act="png">Tải ảnh PNG</button></div>
    </div>
    <p class="hint" data-status></p>
    <div class="nb-sheet"><canvas width="${W * SCALE}" height="${H * SCALE}"></canvas></div>`;

  const cv = root.querySelector("canvas"), ctx = cv.getContext("2d"), status = root.querySelector("[data-status]");
  const $q = s => root.querySelector(s), $all = s => [...root.querySelectorAll(s)];

  /* ---------- Vẽ nền giấy ---------- */
  function paper(kind) {
    ctx.fillStyle = "#fffefa"; ctx.fillRect(0, 0, W, H);
    ctx.lineWidth = 1;
    if (kind === "lined") {
      ctx.strokeStyle = "#cfd8e3";
      for (let y = 110; y < H - 40; y += 56) { ctx.beginPath(); ctx.moveTo(60, y); ctx.lineTo(W - 60, y); ctx.stroke(); }
      ctx.strokeStyle = "#e8b4b4"; ctx.beginPath(); ctx.moveTo(110, 0); ctx.lineTo(110, H); ctx.stroke();
    } else if (kind === "grid") {
      ctx.strokeStyle = "#dde3ea";
      for (let x = 0; x <= W; x += 40) { ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, H); ctx.stroke(); }
      for (let y = 0; y <= H; y += 40) { ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(W, y); ctx.stroke(); }
    } else if (kind === "genkou") {
      const cell = 60, cols = 15, rows = 21, ox = (W - cols * cell) / 2, oy = (H - rows * cell) / 2;
      ctx.strokeStyle = "#c98a8a"; ctx.lineWidth = 1.5;
      ctx.strokeRect(ox, oy, cols * cell, rows * cell);
      for (let c = 1; c < cols; c++) { ctx.beginPath(); ctx.moveTo(ox + c * cell, oy); ctx.lineTo(ox + c * cell, oy + rows * cell); ctx.stroke(); }
      for (let r = 1; r < rows; r++) { ctx.beginPath(); ctx.moveTo(ox, oy + r * cell); ctx.lineTo(ox + cols * cell, oy + r * cell); ctx.stroke(); }
      ctx.setLineDash([4, 5]); ctx.strokeStyle = "#e3c1c1"; ctx.lineWidth = 1;
      for (let c = 0; c < cols; c++) { const x = ox + c * cell + cell / 2; ctx.beginPath(); ctx.moveTo(x, oy); ctx.lineTo(x, oy + rows * cell); ctx.stroke(); }
      for (let r = 0; r < rows; r++) { const y = oy + r * cell + cell / 2; ctx.beginPath(); ctx.moveTo(ox, y); ctx.lineTo(ox + cols * cell, y); ctx.stroke(); }
      ctx.setLineDash([]);
    }
  }

  /* ---------- Vẽ nét ---------- */
  function drawStroke(s) {
    const pts = s.p; if (!pts.length) return;
    ctx.strokeStyle = s.c; ctx.fillStyle = s.c; ctx.lineCap = ctx.lineJoin = "round";
    if (pts.length === 1) { ctx.beginPath(); ctx.arc(pts[0][0], pts[0][1], s.w * (0.4 + pts[0][2]) / 2, 0, 6.2832); ctx.fill(); return; }
    for (let i = 1; i < pts.length; i++) {
      ctx.lineWidth = s.w * (0.4 + (pts[i][2] + pts[i - 1][2]) / 2 * 1.2);
      ctx.beginPath(); ctx.moveTo(pts[i - 1][0], pts[i - 1][1]); ctx.lineTo(pts[i][0], pts[i][1]); ctx.stroke();
    }
  }
  function redraw() {
    ctx.setTransform(SCALE, 0, 0, SCALE, 0, 0);
    paper(page().paper);
    page().strokes.forEach(drawStroke);
  }

  /* ---------- Lưu ---------- */
  function persist() {
    clearTimeout(saveTimer);
    saveTimer = setTimeout(() => {
      try { localStorage.setItem(KEY, JSON.stringify(data)); saveWarned = false; }
      catch { if (!saveWarned) { saveWarned = true; msg("Không lưu được (bộ nhớ trình duyệt đầy). Hãy tải ảnh PNG để giữ lại."); } }
    }, 400);
  }
  const msg = t => { status.textContent = t; };

  /* ---------- Giao diện ---------- */
  function refresh() {
    $q("[data-pageno]").textContent = `${data.cur + 1} / ${data.pages.length}`;
    $q("[data-paper]").value = page().paper;
    const h = hs(page());
    $q('[data-act="undo"]').disabled = !h.undo.length;
    $q('[data-act="redo"]').disabled = !h.redo.length;
    $q('[data-act="prev"]').disabled = data.cur === 0;
    $q('[data-act="next"]').disabled = data.cur === data.pages.length - 1;
    $q('[data-act="del"]').disabled = data.pages.length === 1;
    $all("[data-tool]").forEach(b => b.classList.toggle("primary", b.dataset.tool === tool));
    $all("[data-color]").forEach(b => b.classList.toggle("on", b.dataset.color === color));
  }
  function commit(next) {               // đổi mảng nét, có lưu lịch sử
    const p = page(), h = hs(p);
    h.undo.push(p.strokes); if (h.undo.length > 100) h.undo.shift(); h.redo = [];
    p.strokes = next; redraw(); refresh(); persist();
  }

  root.addEventListener("click", e => {
    const t = e.target.closest("[data-tool]"); if (t) { tool = t.dataset.tool; refresh(); return; }
    const c = e.target.closest("[data-color]"); if (c) { color = c.dataset.color; tool = "pen"; refresh(); return; }
    const a = e.target.closest("[data-act]"); if (!a) return;
    const p = page(), h = hs(p);
    switch (a.dataset.act) {
      case "undo": if (h.undo.length) { h.redo.push(p.strokes); p.strokes = h.undo.pop(); redraw(); refresh(); persist(); } break;
      case "redo": if (h.redo.length) { h.undo.push(p.strokes); p.strokes = h.redo.pop(); redraw(); refresh(); persist(); } break;
      case "clear": if (p.strokes.length && confirm("Xoá toàn bộ nét trên trang này? (Vẫn hoàn tác được.)")) commit([]); break;
      case "prev": data.cur--; redraw(); refresh(); persist(); break;
      case "next": data.cur++; redraw(); refresh(); persist(); break;
      case "add": data.pages.splice(data.cur + 1, 0, { paper: p.paper, strokes: [] }); data.cur++; redraw(); refresh(); persist(); break;
      case "del": if (data.pages.length > 1 && confirm("Xoá hẳn trang này? Không hoàn tác được.")) { data.pages.splice(data.cur, 1); data.cur = Math.min(data.cur, data.pages.length - 1); redraw(); refresh(); persist(); } break;
      case "png": cv.toBlob(b => { const l = document.createElement("a"); l.href = URL.createObjectURL(b); l.download = `nihongo-notebook-${data.cur + 1}.png`; l.click(); setTimeout(() => URL.revokeObjectURL(l.href), 1000); }); break;
    }
  });
  $q("[data-width]").oninput = e => { width = +e.target.value; };
  $q("[data-paper]").onchange = e => { page().paper = e.target.value; redraw(); persist(); };
  document.addEventListener("keydown", e => {
    if (!(e.metaKey || e.ctrlKey) || e.key.toLowerCase() !== "z" || /input|select|textarea/i.test(e.target.tagName)) return;
    e.preventDefault(); $q(`[data-act="${e.shiftKey ? "redo" : "undo"}"]`).click();
  });

  /* ---------- Bút: Apple Pencil / chuột / ngón tay ---------- */
  let cur = null, erasing = null, id = null;
  const pos = e => { const r = cv.getBoundingClientRect(); return [Math.round((e.clientX - r.left) * W / r.width * 10) / 10, Math.round((e.clientY - r.top) * H / r.height * 10) / 10]; };
  const pr = e => e.pointerType === "pen" ? Math.round((e.pressure || 0.5) * 100) / 100 : 0.5;
  function eraseAt(x, y) {
    const R = 22, keep = erasing.keep.filter(s => !s.p.some(q => (q[0] - x) ** 2 + (q[1] - y) ** 2 < R * R));
    if (keep.length !== erasing.keep.length) { erasing.keep = keep; page().strokes = keep; redraw(); }
  }
  cv.addEventListener("pointerdown", e => {
    if (e.pointerType === "pen") penSeen = true;
    if (e.pointerType === "touch" && penSeen) return;       // chặn lòng bàn tay khi đang dùng bút
    if (e.pointerType === "mouse" && e.button !== 0) return;
    e.preventDefault(); cv.setPointerCapture(e.pointerId); id = e.pointerId;
    const [x, y] = pos(e);
    if (tool === "eraser" || (e.pointerType === "pen" && e.buttons === 32)) { erasing = { before: page().strokes, keep: page().strokes }; eraseAt(x, y); }
    else { cur = { c: color, w: width, p: [[x, y, pr(e)]] }; page().strokes = page().strokes.concat([cur]); drawStroke(cur); }
  });
  cv.addEventListener("pointermove", e => {
    if (e.pointerId !== id) return;
    const co = e.getCoalescedEvents ? e.getCoalescedEvents() : [];
    for (const ev of (co.length ? co : [e])) {
      const [x, y] = pos(ev);
      if (erasing) eraseAt(x, y);
      else if (cur) { const last = cur.p[cur.p.length - 1]; if (Math.hypot(x - last[0], y - last[1]) < 0.8) continue; cur.p.push([x, y, pr(ev)]); const n = cur.p.length;
        drawStroke({ ...cur, p: cur.p.slice(n - 2) }); }
    }
  });
  function end(e) {
    if (e.pointerId !== id) return; id = null;
    const p = page(), h = hs(p);
    if (erasing) { if (erasing.keep !== erasing.before) { h.undo.push(erasing.before); h.redo = []; persist(); } erasing = null; }
    else if (cur) { h.undo.push(p.strokes.slice(0, -1)); h.redo = []; cur = null; persist(); }
    refresh();
  }
  cv.addEventListener("pointerup", end); cv.addEventListener("pointercancel", end);
  cv.addEventListener("contextmenu", e => e.preventDefault());

  redraw(); refresh();
})();
