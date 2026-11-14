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
- Thứ tự ngữ pháp theo sách (đã đối chiếu); câu ví dụ + hội thoại tự viết. Nhân vật riêng: ナム, リン, たなか, すずき
  (không dùng nhân vật của sách).
- Thẻ từ vựng (type "vocab", id "v-<romaji>"): mặt trước chỉ chữ, ảnh bị che (ảnh lộ nghĩa). Chỉ từ chụp ảnh được
  mới có thẻ; từ chức năng (だれ, いくら, とても…) nằm trong bảng + bài tập, không có thẻ.
- Component mới trong `assets/nihongo.js`: data-build (ghép câu), data-dialog (hội thoại + nói đuổi),
  data-num (nghe giá/giờ/ngày/tầng — máy tự sinh cách đọc kana). Reference: `ngu-phap-minna.html`, `so-dem.html`.
- Kanji: mới chỉ hiện để nhận mặt (cột kanji). Chưa có lộ trình kanji — cần bàn với người học trước Minna bài 11.
- Mỗi bài Minna 60–75 phút; khuyên chia 2 buổi. Bài 11+ chưa soạn.
- Người học yêu cầu (2026-11-14): mọi bài có từ vựng phải có phần LUYỆN ĐỌC từ vựng (data-read: nhìn chữ → đọc to →
  gõ romaji, máy đọc lại). Gồm cả từ có ảnh lẫn từ chức năng. Giữ quy tắc này cho bài 11+.
- Người học yêu cầu thêm (2026-11-14): MỖI từ vựng phải có câu ví dụ dùng chính từ đó, nghe được cả từ lẫn câu
  (nút “từ”, “câu”, “từ + câu” và “nghe cả danh sách” dùng data-say-seq), có quiz nghe từ (data-listen) và
  bài “tự đặt câu”. Từ chức năng cũng có câu ví dụ + nút nghe (tools/minna_word_ex.py, khớp 1-1 với words).

## Luyện tự chọn (2026-11-14, người học yêu cầu)
- `luyen-tap.html` + `assets/practice.js`: chọn chữ/từ (hiragana, katakana đủ bảng kể cả âm ghép; từ vựng Minna theo bài),
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
- Có muốn tham gia cộng đồng / luyện nói với người thật không?
- Định thi JLPT kỳ nào đầu tiên (tháng 7 hay tháng 12)?
