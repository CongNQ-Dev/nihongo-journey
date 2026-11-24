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
- Chưa làm: đề luyện JLPT, đề JLPT N4/N3 và các chặng sau Minna 50, thẻ ngữ pháp vào lịch ôn (hiện chỉ luyện thêm), chế độ Gõ cách đọc / Nghe chọn chưa chấm vào lịch ôn.

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
- Mục "Nguồn nên đọc": ban đầu trỏ mục lục Tae Kim. Từ 2026-11-24 `tools/taekim_map.py` gán đúng mục Tae Kim cho 37/40 bài (đã mở từng trang, đối chiếu TIÊU ĐỀ các phần với mẫu câu); bài 34, 42, 45 chưa có mục khớp nên giữ link mục lục.
- Toàn bộ giải thích, câu ví dụ và hội thoại do mình soạn, chưa có người Nhật kiểm tra: nên đối chiếu với sách Minna bài tương ứng và báo chỗ nào sai để sửa.

## Minna bài 26–30 (2026-11-22)
- `tools/minna_ext_d.py` (file 0037–0041), đã ghi vào `EXT_MODULES`. Mục lục có thêm "Giai đoạn 2 · Sơ cấp II" từ bài 26. Cùng lưu ý như bài 11–25: chưa có ảnh thẻ, chưa có người Nhật kiểm tra nội dung, nguồn đọc thêm trỏ về mục lục Tae Kim.

## Đối chiếu với nguồn chính thức (2026-11-23)
- Nguồn: Japan Foundation, bảng "みんなの日本語 文型・表現 ↔ いろどり" (PDF công khai: yg.jpf.go.jp/wp-content/uploads/2023/11/Sentence-Patterns-Minna-no-Nihongo-and-IRODORI.20211027.pdf). Liệt kê mẫu câu từng bài, **không** liệt kê từ vựng hay câu ví dụ.
- Kết quả bài 1–30: thứ tự và phân bổ mẫu câu khớp. Đã bổ sung chỗ thiếu: bài 1 ～さいです; bài 14 V-かた; bài 18 hai nghĩa của ことができます + ～まえに chỉ khoảng thời gian; bài 30 ba nghĩa của ておきます.
- Bài 11 ～だけ: PDF JF không nêu, nhưng có phần 「だけ」 trong mục "Expressing Amounts" của Tae Kim (đã gắn link). Bài 21 N でも: vẫn chưa xác nhận bằng nguồn nào. Từ vựng từng bài và câu ví dụ vẫn do mình tự soạn, chưa đối chiếu với sách.

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

## Minna bài 41–45 (2026-11-23)
- `tools/minna_ext_i.py` (file 0052–0056): 41 いただく/くださる/やる; 42 ために/のに; 43 ～そうです, ～てきます; 44 ～すぎる/やすい/にくい/～にする; 45 ばあいは/のに. Mẫu câu theo bảng JF, từ vựng 272/272 (toàn khoá bài 1–45: 2404/2404 theo script).

## Minna bài 46–50 (2026-11-23) — hoàn tất bộ sơ cấp
- `tools/minna_ext_j.py` (file 0057–0061): 46 ところ/ばかり/はず; 47 そうです(truyền đạt)/ようです; 48 thể sai khiến; 49 kính ngữ; 50 khiêm nhường ngữ. Mẫu câu theo bảng JF, từ vựng 248/248.
- **Toàn bộ bài 1–50: 2.652/2.652 từ vựng** theo `check_vocab_coverage.py`, mẫu câu khớp bảng JF.
- Việc còn lại của dự án: ảnh thẻ cho từ mới (cần mạng tới Wikimedia), người Nhật kiểm tra câu ví dụ, đề luyện JLPT N5/N4, chặng N3+.

## Đối chiếu từ điển mở (`tools/verify_dict.py`)
- Chạy: `python3 -I tools/verify_dict.py DIR [kanji|words|all]` (DIR chứa `kanjidic2.xml`, `JMdict_e` đã giải nén; tải từ edrdg.org, cần cho phép `www.edrdg.org`, `ftp.edrdg.org`).
- Đã so: 251 chữ Hán (On/Kun/Hán Việt vs KANJIDIC2; sửa 4 chỗ: 絵, 政, 中, 着) và 1450 cặp (cách đọc, chữ viết) của từ vựng vs JMdict: 1386 khớp, 64 không khớp là tên riêng, thương hiệu, viết tắt, câu giao tiếp, cụm đếm, một vài dạng chia (công cụ không tra được, không phải lỗi).
- 着: KANJIDIC2 không có Hán Việt. Đã lấy "trước" từ mục tiếng Việt của Wiktionary (CC BY-SA; trang liệt kê trước, trứ, chốc, trốc) ngày 2026-11-24; vẫn nên đối chiếu từ điển Hán Việt giấy.
- CHƯA có nguồn: nghĩa tiếng Việt, câu ví dụ, hội thoại, giải thích ngữ pháp, chọn chữ Hán (do người soạn viết). Bước kế tiếp đã bàn: thay/bổ sung câu ví dụ bằng câu Tatoeba (CC BY 2.0 FR, cần ghi nguồn).

## Câu ví dụ Tatoeba (2026-11-24)
- Chạy `tools/tatoeba_match.py` trên Mac: 1299 mục khớp, lọc tiếp bằng tay (bỏ mục có ～／ trong khoá, câu <5 chữ, kana ≤2 ký tự) còn **882** mục, rồi đọc lại toàn bộ bằng mắt và loại 33 câu khớp nhầm từ/nghĩa (つまみ↔おつまみ, かります↔分かります, やさしい↔優しい…), còn **849** mục trong `tools/tatoeba_ex.json`; `tatoeba_apply.py` thay câu tự soạn khi build.
- Bản dịch chỉ có tiếng Anh, ghi "(Tatoeba #id, tác giả, CC BY 2.0 FR)". Furigana: `tools/tatoeba_furi.py DIR` (DIR chứa `jpn_transcriptions.tsv`, bunzip2 từ downloads.tatoeba.org/exports/per_language/jpn/) ghi trường `furi` vào `tatoeba_ex.json`; cả 849 câu khớp chữ 100%. Furigana do Tatoeba tạo tự động (không chuyên gia duyệt). Thẻ có thêm trường `exf` (HTML ruby) để hiện furigana ở mặt sau; `ex` giữ chữ thuần cho giọng đọc. Đã đọc cả 882 câu một lượt (chỉ xét khớp từ/nghĩa, không phải người Nhật kiểm).
- Khoảng 1700 mục còn lại vẫn là câu tự soạn, chưa có nguồn.

## Đối chiếu với giáo trình Minna (2026-11-24, người học yêu cầu: mọi thứ phải có nguồn uy tín và chuẩn Minna)
- Không chép nội dung sách vào repo. Cách làm: `python3 -I tools/doi_chieu.py DIR` (DIR chứa `JMdict_e`) sinh `reference/doi-chieu/bai-NN.md` (từ, nghĩa VN của khoá, nghĩa EN từ JMdict tra tự động, cột trống để người học so với sách).
- Trạng thái từng bài ở `tools/source_status.json` ({"<bài Minna>": {"verified": "YYYY-MM-DD"}}). CHỈ ghi khi người học xác nhận đã so xong bài đó; mặc định mọi bài là "chưa đối chiếu với sách". Trang bài hiện nhãn nguồn (`source_note` trong `tools/minna_pages.py`) lấy từ file này.
- Khi người học báo chỗ sai trong bảng: sửa ở `tools/minna_*.py`, chạy lại `doi_chieu.py` và `build.py`.
- Nghĩa EN trong bảng tra tự động nên có thể lệch (từ nhiều nghĩa) hoặc trống (câu giao tiếp, tên riêng, từ ghép).

## Thẻ chữ (2026-11-24, người học yêu cầu)
- Quy ước cũ "mọi thẻ có ảnh" nới ra: từ vựng KHÔNG có ảnh (104 từ chưa tìm được ảnh đúng nghĩa) và từ chức năng / câu cố định (bảng `words`) có **thẻ chữ**: mặt trước chỉ chữ to, mặt sau nghĩa + câu ví dụ. Vẫn không dùng icon / emoji / hình vẽ thay ảnh.
- `vocab_cards()` (minna_pages.py): thẻ từ VOCAB giữ id `v-...` (khi có ảnh thì tự có ảnh, không mất tiến độ ôn); thẻ từ `words` có id `w<số bài file>-<romaji>`; từ lặp ở bài sau không tạo thẻ mới. Tổng 2409 thẻ.
- Cẩn thận khi đổi romaji của từ trong `words`: id thẻ chữ lấy từ romaji, đổi là mất tiến độ ôn của thẻ đó.
- Service worker có thể giữ bản cũ: tải lại hai lần (hoặc xoá dữ liệu trang) mới thấy thẻ mới.

## Cải tiến 2026-11-24 (mục 3 của danh sách việc còn lại)
- **Từ có ／ (nhiều biến thể, 308 thẻ)**: giọng đọc đọc từng biến thể có nghỉ; chế độ "Gõ cách đọc" nhận romaji của BẤT KỲ biến thể nào (bộ chuyển kana→romaji `kanaRomaji` trong `assets/nihongo.js`); chế độ "Viết lại" bỏ ký hiệu ／ ～ … (không có nét) nên không còn ô viết thừa.
- **Chia phần thẻ bài học**: bài > 20 thẻ chia thành các phần ≤ ~20 thẻ (`deck()` trong nihongo.js), mở phần đầu còn thẻ chưa học; nhớ phần đang chọn trong sessionStorage. Thứ tự thẻ trong phần giữ nguyên thứ tự bài.
- **Furigana Tatoeba**: xem mục "Câu ví dụ Tatoeba".
- **Nguồn nên đọc**: `tools/taekim_map.py`.
- **Đề thử kiểu JLPT** (`jlpt.html`, `assets/mock.js`): đề 文字・語彙 TỰ SINH từ 946 từ có chữ Hán đã đối chiếu JMdict (đọc chữ Hán, viết chữ Hán, nghĩa). Không phải đề chính thức; N5 ≈ Minna 1–25, N4 ≈ 26–50 chỉ là ước lượng theo thứ tự giáo trình. Chưa có phần ngữ pháp, đọc hiểu, nghe hiểu: không có nguồn đề chính thức dùng được và câu hỏi tự soạn sẽ lại là nội dung chưa có nguồn.
- **N3 trở lên: chưa làm**. Cần cả bộ bài mới (từ vựng, mẫu câu, chữ Hán) theo một giáo trình/nguồn N3 cụ thể (ví dụ Shin Kanzen / Soumatome / Minna Chukyu), cần người học chọn giáo trình rồi mới đối chiếu được. Không soạn từ trí nhớ (xem CLAUDE.md).
- `tools/build.py` có `V_CSS/V_CARDS/V_JS` và `sync_versions()`: tăng số khi sửa `course.css`, `cards.js` (khi dữ liệu thẻ đổi), `nihongo.js`; build tự đồng bộ `?v=` sang các trang viết tay (practice, flashcards, notebook, search, jlpt, roadmap, bài 0001).
