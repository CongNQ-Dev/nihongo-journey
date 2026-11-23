# Teaching notes

## Learner preferences
- Viết tiếng Việt → bài học tiếng Việt. Cũng đang học khoá full-stack ở `~/Developer/fullstack-journey`.
- Bắt đầu từ số 0 (2026-11-14). 15+ giờ/tuần.
- Trục chính: Minna no Nihongo từ bài 1. Tập trung đủ 4 kỹ năng nghe – nói – đọc – viết.
- Mọi thứ cần ghi nhớ (kana, từ vựng, kanji) → flashcard có **ảnh chụp thật, đẹp, lấy từ mạng**.
  KHÔNG dùng icon / emoji / hình vẽ minh hoạ thay ảnh.
- Lý do học: công việc với công ty Nhật + bằng JLPT + sống/du lịch + sở thích (chọn cả 4).

## Workspace conventions
- Mỗi bài: 1 thành quả cụ thể; đủ 4 góc nghe / nói / đọc / viết ở mức phù hợp; quiz có các đáp án
  dài bằng nhau; khối "nhớ lại từ trí nhớ"; 1 nguồn chính; nhắc hỏi lại giáo viên; link bài sau.
- Từ bài 0002: mở đầu bằng 2–3 câu nhớ lại bài cũ (spacing).
- Ảnh: Wikimedia Commons, tải về `assets/img/`, rộng 960px, ghi công trong `assets/img/CREDITS.md`
  và trong `assets/cards.js`. Tự xem ảnh trước khi dùng (đẹp, đúng nghĩa, không gây hiểu lầm).
- Thẻ mới thêm vào `assets/cards.js` (id không đổi — tiến độ ôn lưu theo id trong localStorage).
- Nét viết: lấy từ KanjiVG, thêm vào `assets/strokes.js`.
- Trang ôn hằng ngày: `flashcards.html` (Leitner 5 hộp: 0/1/3/7/14 ngày).
- Âm thanh: giọng đọc ja-JP của trình duyệt (macOS có Kyoko). Khi vào Minna thì dùng file nghe
  của sách cho bài hội thoại.
- Không chép nội dung sách Minna; dạy theo thứ tự bài của sách bằng lời và ví dụ riêng.

## Giai đoạn kana — ĐÃ SOẠN XONG (2026-11-14, người học yêu cầu soạn hết một lần)
- Hiragana 0001–0007, katakana 0008 ア〜ソ, 0009 タ〜ホ, 0010 マ〜ン, 0011 ゛゜/ッ/ャ/âm ngoại lai.
  Sau 0011 → Minna no Nihongo bài 1 (chưa soạn).
- 0002–0011 SINH TỰ ĐỘNG: sửa `tools/kana_data.py` rồi `python3 -I tools/build.py`. Không sửa tay HTML sinh ra.
  Bài 0001 viết tay. Ảnh: `tools/fetch_images.py` (search → sheet để duyệt → download), lựa chọn ở PICK/QUERY_FIX.
- Wikimedia API giới hạn tốc độ (429): script đã chờ 1,5s/lần gọi và tự thử lại.
- Người học được khuyên tối đa một bài mới mỗi ngày dù đã soạn sẵn; ôn flashcard trước.
- Chưa có learning record về bài nào: chỉ ghi khi người học báo kết quả phần “Nhớ lại”.
- 2026-11-14 (/teach lần 2): người học CHƯA bắt đầu bài 0001 → không soạn bài mới, mở 0001. Soạn Minna bài 1 khi họ gần xong kana.

## Giai đoạn Minna — bài 1–10 ĐÃ SOẠN (2026-11-14, người học yêu cầu soạn trước)
- 0012–0021 = Minna bài 1–10. SINH TỰ ĐỘNG: nội dung ở `tools/minna_data.py`, từ có ảnh ở `tools/minna_vocab.py`,
  HTML ở `tools/minna_pages.py`; chạy `python3 -I tools/build.py`. Không sửa tay HTML sinh ra.
- Thứ tự ngữ pháp theo sách (đối chiếu lần đầu với một trang ghi chú cá nhân, xem mục đối chiếu chính thức ở cuối file); câu ví dụ + hội thoại tự viết. Nhân vật riêng: ナム, リン, たなか, すずき
  (không dùng nhân vật của sách).
- Thẻ từ vựng (type "vocab", id "v-<romaji>"): mặt trước chỉ chữ, ảnh bị che (ảnh lộ nghĩa). Chỉ từ chụp ảnh được
  mới có thẻ; từ chức năng (だれ, いくら, とても…) nằm trong bảng + bài tập, không có thẻ.
- Component mới trong `assets/nihongo.js`: data-build (ghép câu), data-dialog (hội thoại + nói đuổi),
  data-num (nghe giá/giờ/ngày/tầng — máy tự sinh cách đọc kana). Reference: `minna-grammar.html`, `numbers-counters.html`.
- Kanji: mới chỉ hiện để nhận mặt (cột kanji). Chưa có lộ trình kanji — cần bàn với người học trước Minna bài 11.
- Mỗi bài Minna 60–75 phút; khuyên chia 2 buổi. Bài 11+ chưa soạn.
- Người học yêu cầu (2026-11-14): mọi bài có từ vựng phải có phần LUYỆN ĐỌC từ vựng (data-read: nhìn chữ → đọc to →
  gõ romaji, máy đọc lại). Gồm cả từ có ảnh lẫn từ chức năng. Giữ quy tắc này cho bài 11+.
- Người học yêu cầu thêm (2026-11-14): MỖI từ vựng phải có câu ví dụ dùng chính từ đó, nghe được cả từ lẫn câu
  (nút “từ”, “câu”, “từ + câu” và “nghe cả danh sách” dùng data-say-seq), có quiz nghe từ (data-listen) và
  bài “tự đặt câu”. Từ chức năng cũng có câu ví dụ + nút nghe (tools/minna_word_ex.py, khớp 1-1 với words).

## Luyện tự chọn (2026-11-14, người học yêu cầu)
- `practice.html` + `assets/practice.js`: chọn chữ/từ (hiragana, katakana đủ bảng kể cả âm ghép; từ vựng Minna theo bài),
  chọn số N, bốc ngẫu nhiên N mục (từ mục đã chọn, hoặc cả kho nếu chưa chọn) → Flashcard / Gõ cách đọc / Nghe chọn.
  KHÔNG ghi vào lịch Leitner. Lựa chọn lưu ở localStorage `nihongo-practice-v1`. Từ vựng bài mới tự vào kho qua cards.js.
- Luồng 2 màn (sửa 2026-11-14 sau phản hồi UX): màn chọn có thanh Bốc dính đáy; màn luyện ẩn danh sách mục vừa bốc (tránh lộ đáp án). Lựa chọn chỉ áp dụng cho tab đang mở.
- `Nihongo.deck(el, {cards})` = chế độ luyện tự do; thẻ kana không có ảnh hiện chữ to (`.noimg`).

## Notion
- Người học KHÔNG cần ghi chú/tiến độ trên Notion nữa (2026-11-14). Không cập nhật Notion; theo dõi tiến độ bằng `learning-records/`.

## Git
- Repo public trên GitHub (người học yêu cầu). Không commit thông tin cá nhân hay bí mật; ảnh phải có ghi công.

## Việc cần hỏi người học
- (Đã trả lời 2026-11-14: CÓ bộ Minna sơ cấp I, CÓ bản dịch tiếng Việt và file nghe → bài Minna dùng file nghe của sách.)
- (Đã trả lời 2026-11-14) MUỐN tham gia cộng đồng để luyện nói với người Nhật. Chưa chọn nền tảng; xem RESOURCES.md mục Wisdom.
  Chưa quyết: có trả phí gia sư không, và bắt đầu nói với người thật từ lúc nào.
- (Đã trả lời 2026-11-14) ĐỊNH THI JLPT tháng 7 (kỳ đầu tiên 2027, dự kiến 4/7/2027 — chưa xác nhận).
  Lưu ý: mốc N2 trong MISSION chưa khớp với thời gian này (xem mục dưới). Chưa đổi MISSION — cần người học xác nhận.

## Mốc JLPT tháng 7/2027 — ĐÃ CHỐT: N4 (2026-11-14, xem learning-records/0002)
- N3 không khả thi trước 7/2027 (~500 giờ có sẵn). MISSION đã cập nhật.
- N4 cần gần hết 50 bài Minna (sơ cấp II = N4). Trước đó mình nói nhầm "bài 1–25 = N4"; đã sửa trong learning record.
- Giờ học N4 chưa kiểm chứng; cần theo dõi tiến độ thực tế.

## Tiến độ, sao lưu, kanji (2026-11-15)
- Sao lưu: `[data-backup]` (index + flashcards) xuất/nhập mọi khoá localStorage bắt đầu bằng `nihongo-`. Khôi phục ghi đè.
- Tiến độ bài: khoá `nihongo-lessons-v1` {"0012": timestamp}. Nút "Đánh dấu đã học xong" tự chèn trước `nav.next` ở mọi bài (nihongo.js `lessonDone`); index có `[data-progress]` (Minna x/50, số ngày tới 4/7/2027, bài/tuần cần thiết).
- Kanji: `tools/kanji_data.py` (55 chữ N5, gắn bài 0012–0021) → thẻ type "kanji", id `kj-<hex unicode>`, trang `kanji.html`. Nét: `python3 -I tools/fetch_strokes.py` (KanjiVG). Thẻ kanji chỉ vào ôn bằng chế độ Flashcard; KHÔNG có trong Viết lại / Trắc nghiệm / Luyện tự chọn (đọc kanji có nhiều âm, câu hỏi mơ hồ). Deck bài Minna loại thẻ kanji (cần `data-type="kanji"` mới hiện).
- Khi soạn Minna bài 11+: thêm kanji của bài đó vào `kanji_data.py`, chạy fetch_strokes rồi build.
- Chưa làm: đề luyện JLPT, soạn Minna bài 41–50, thẻ ngữ pháp vào lịch ôn (hiện chỉ luyện thêm), chế độ Gõ cách đọc / Nghe chọn chưa chấm vào lịch ôn.

## Sổ tay viết tay (2026-11-15)
- `notebook.html` + `assets/notebook.js` (viết tay, KHÔNG sinh tự động). Canvas 1000×1414 vector, nhiều trang, 4 nền giấy (trắng, kẻ ngang, ô vuông, genkou), bút/tẩy nét, hoàn tác, xuất PNG, chặn lòng bàn tay khi có Apple Pencil.
- Lưu ở localStorage `nihongo-notebook-v1` (nằm trong file sao lưu). Nhiều trang có thể đầy bộ nhớ → nhắc tải PNG.
- Khi sửa notebook.js nhớ tăng `?v=` trong notebook.html.

## Tự động lưu vào file (2026-11-15)
- `nihongo.js`: người học chọn 1 file .json (File System Access API, chỉ Chrome/Edge desktop); mọi thay đổi khoá `nihongo-*` được ghi lại sau ~3 giây. Tay cầm file lưu trong IndexedDB `nihongo-fs`; mở lại trình duyệt có thể cần bấm "Cho phép lại".
- Không ghi file khi không có dữ liệu (tránh ghi đè bản tốt bằng dữ liệu rỗng). Liên kết file đã có dữ liệu → hỏi nạp hay ghi đè.
- Safari/Firefox/iPad: không hỗ trợ → chỉ tải file thủ công + "Nhập từ file…". Nhập chỉ nhận khoá bắt đầu bằng `nihongo-`.
- Đã test bằng file giả lập, chưa thử hộp chọn file thật.

## Dọn dẹp và bổ sung (2026-11-22)
- Thanh điều hướng chung do `nihongo.js` (`siteNav`) tự chèn đầu `<main>` mọi trang có nạp script; không viết tay vào từng trang.
- Hộp sao lưu chỉ còn ở `index.html#sao-luu`; các trang khác dùng `data-backup="mini"` (chỉ nhắc khi quá 7 ngày chưa sao lưu).
- Lịch ôn: `[0,1,3,7,14,30,60,120]` ngày (khoá `nihongo-srs-v1`, thêm trường `miss`). Thống kê theo ngày ở khoá `nihongo-stats-v1`, hiển thị bằng `<div data-stats>` ở `flashcards.html`.
- Kanji vào cả chế độ Viết lại / Trắc nghiệm của trang ôn hằng ngày và có tab Kanji ở `practice.html` (không có "Gõ cách đọc" / "Nghe chọn").
- Mục lục có nút "Học tiếp"; mỗi bài Minna có link tới đúng nhóm kanji (`kanji.html#bai-N`).
- Sửa version asset lên `v=16` (đổi `course.css` / `nihongo.js` nhớ tăng cả ở `tools/build.py` lẫn các trang viết tay).

## Vòng 2 (2026-11-22)
- `Nihongo.modes(el, cards, {graded, tabs, pool})` là nơi duy nhất dựng 5 chế độ ôn; `flashcards.html` (graded, 3 chế độ) và `practice.js` (không graded) cùng dùng. Muốn thêm chế độ thì sửa ở đó.
- `Nihongo.dictation` (nghe chép chính tả) và thẻ ngữ pháp nằm ở tab "Câu & ngữ pháp" của `practice.html`, chọn bài rồi chọn hoạt động.
- Gợi ý ≤ 20 thẻ mới/ngày (`NEW_MAX`): chỉ nhắc ở thanh thẻ bài học và ở thống kê, không chặn.
- `search.html` + `assets/search.js`: tìm trên `CARDS` và `SENTENCES`; `LESSON_FILES` sinh vào `sentences.js` để tạo link bài.
- Offline/PWA: `manifest.webmanifest`, `sw.js` (SINH TỰ ĐỘNG, hash nội dung làm tên cache), icon trong `assets/`. Cần https hoặc localhost. Sửa file viết tay xong nhớ chạy `python3 -I tools/build.py` để sw.js đổi phiên bản.

## Minna bài 11–25 (2026-11-22)
- Nội dung nằm ở `tools/minna_ext_a.py` (bài 11–15), `_b` (16–20), `_c` (21–25). Mỗi file có `LESSONS`, `WORD_EX`, `VOCAB`, `KANJI`; `minna_data.py`, `minna_vocab.py`, `minna_word_ex.py`, `kanji_data.py` nạp chúng qua `EXT_MODULES`. Bài 26+ thì thêm `minna_ext_d.py` và ghi tên vào `EXT_MODULES` ở cả 4 file đó.
- File bài học là 0022–0036 (Minna bài N = file N+11). Kanji mới: 80 chữ, thứ tự nét đã lấy bằng `tools/fetch_strokes.py`.
- **Chưa có ảnh thẻ** cho từ vựng mới (Wikimedia không truy cập được lúc soạn): các bài đó hiện ghi chú "Chưa có thẻ ảnh" và bảng từ vẫn dùng được. Ở máy có mạng chạy `python3 -I tools/fetch_images.py search`, duyệt ảnh, thêm lựa chọn vào `PICK`, rồi `download` và `build`.
- Mục "Nguồn nên đọc" của bài 11–25 trỏ về trang mục lục Tae Kim (`/learn/grammar`) vì không kiểm chứng được URL từng phần. Muốn chính xác hơn thì mở trang đó, chọn đúng mục rồi thay URL trong `primary`.
- Toàn bộ giải thích, câu ví dụ và hội thoại do mình soạn, chưa có người Nhật kiểm tra: nên đối chiếu với sách Minna bài tương ứng và báo chỗ nào sai để sửa.

## Minna bài 26–30 (2026-11-22)
- `tools/minna_ext_d.py` (file 0037–0041), đã ghi vào `EXT_MODULES`. Mục lục có thêm "Giai đoạn 2 · Sơ cấp II" từ bài 26. Cùng lưu ý như bài 11–25: chưa có ảnh thẻ, chưa có người Nhật kiểm tra nội dung, nguồn đọc thêm trỏ về mục lục Tae Kim.

## Đối chiếu với nguồn chính thức (2026-11-23)
- Nguồn: Japan Foundation, bảng "みんなの日本語 文型・表現 ↔ いろどり" (PDF công khai: yg.jpf.go.jp/wp-content/uploads/2023/11/Sentence-Patterns-Minna-no-Nihongo-and-IRODORI.20211027.pdf). Liệt kê mẫu câu từng bài, **không** liệt kê từ vựng hay câu ví dụ.
- Kết quả bài 1–30: thứ tự và phân bổ mẫu câu khớp. Đã bổ sung chỗ thiếu: bài 1 ～さいです; bài 14 V-かた; bài 18 hai nghĩa của ことができます + ～まえに chỉ khoảng thời gian; bài 30 ba nghĩa của ておきます.
- Chưa xác nhận bằng nguồn chính thức: bài 11 ～だけ và bài 21 N でも (PDF không nêu hai mục này). Từ vựng từng bài và câu ví dụ vẫn do mình tự soạn, chưa đối chiếu với sách.

## Đối chiếu từ vựng bài 1–30 (2026-11-23) và quy trình mới
- Phép so với danh sách từ vựng của sách (công cụ `tools/check_vocab_coverage.py`) cho thấy bài 1–30 mới có 751/1475 từ (≈51%); 724 từ còn thiếu hoặc nằm sai bài. Mẫu câu thì khớp, nên lần đối chiếu mẫu câu trước không phát hiện được chỗ thiếu này.
- Nguyên nhân: soạn từ trí nhớ về giáo trình, chỉ kiểm tra mẫu câu, rồi báo "khớp" chung chung. Quy trình sửa nằm ở `CLAUDE.md` (đọc trước khi soạn bài mới): lấy mẫu câu (PDF JF) và danh sách từ (script) **trước** khi soạn; chạy script **sau** khi soạn cho đến khi hết thiếu; báo cáo nói rõ đã so cái gì.
- Tiến độ bổ sung: xem mục cuối file này (cập nhật theo từng nhóm 5 bài).

### Tiến độ bổ sung từ vựng (cập nhật theo từng nhóm)
- Bài 1–5: **xong** (272/272 từ theo `check_vocab_coverage.py`). Từ thêm nằm ở `tools/minna_add_a.py` (cơ chế `WORDS_ADD` / `VOCAB` / `VOCAB_MOVE`, đã ghi vào `EXT_MODULES`). Ảnh thẻ của từ mới chưa tải.
- Bài 6–10: **xong** (bài 1–10: 555/555 từ), từ thêm ở `tools/minna_add_b.py`. Lưu ý rút ra: một từ có thể nằm ở **nhiều bài** của sách (ví dụ おみやげ, えいが, りょこう); `VOCAB_MOVE` chỉ dùng khi từ thực sự sai bài, còn lại thêm hàng `WORDS_ADD` ở bài cần thêm.
- Bài 11–30: **xong** (bài 1–30: 1475/1475 từ theo script), từ thêm ở `tools/minna_add_c.py` … `minna_add_f.py`.

## Minna bài 31–35 (2026-11-23)
- `tools/minna_ext_g.py` (file 0042–0046), soạn theo quy trình `CLAUDE.md`: mẫu câu lấy từ bảng JF (31: thể ý chí…; 32: ほうがいい/でしょう/かもしれません; 33: mệnh lệnh, biển báo, nhắn lời; 34: とおりに/あとで/ないで; 35: thể ば, なら), từ vựng đối chiếu bằng script (bài 31–35: 321/321; toàn khoá bài 1–35: 1796/1796).
- Chưa có ảnh thẻ cho từ mới; nghĩa và câu ví dụ tự soạn, chưa có người Nhật kiểm tra.

## Minna bài 36–40 (2026-11-23)
- `tools/minna_ext_h.py` (file 0047–0051): 36 ようになります/ようにして; 37 thể bị động; 38 の danh từ hoá; 39 ～て/～ので nêu lý do; 40 ～か/～かどうか, ～てみます. Mẫu câu theo bảng JF, từ vựng 336/336 (toàn khoá bài 1–40: 2132/2132 theo script).
- Lỗi đã gặp: một nét kanji (慣) trong KanjiVG bắt đầu bằng `m` thường làm `writer()` lỗi; đã sửa regex ở `nihongo.js` (nhận cả `M` và `m`), nâng version asset lên `v=17`.
