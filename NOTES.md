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

## Notion
- Người học KHÔNG cần ghi chú/tiến độ trên Notion nữa (2026-11-14). Không cập nhật Notion; theo dõi tiến độ bằng `learning-records/`.

## Git
- Repo public trên GitHub (người học yêu cầu). Không commit thông tin cá nhân hay bí mật; ảnh phải có ghi công.

## Việc cần hỏi người học
- (Đã trả lời 2026-11-14: ĐÃ CÓ bộ Minna sơ cấp I.) Còn cần hỏi: có đủ bản dịch tiếng Việt + file nghe không?
- Có muốn tham gia cộng đồng / luyện nói với người thật không?
- Định thi JLPT kỳ nào đầu tiên (tháng 7 hay tháng 12)?
