# Quy trình khi soạn hoặc sửa bài Minna (đọc trước khi làm)

Bài học đi theo thứ tự và phạm vi của Minna no Nihongo nhưng **không chép nội dung sách** (xem `MISSION.md`, `NOTES.md`).
Từng bị lỗi: soạn từ trí nhớ nên thiếu khoảng một nửa từ vựng của sách, rồi báo "đã đối chiếu" khi mới so một phần.

## Trước khi soạn bài N
1. Lấy **mẫu câu** của bài từ bảng chính thức của Japan Foundation:
   `https://yg.jpf.go.jp/wp-content/uploads/2023/11/Sentence-Patterns-Minna-no-Nihongo-and-IRODORI.20211027.pdf`
   (cần cho phép tên miền `yg.jpf.go.jp`; `pdftotext -layout` rồi đọc cột "みんなの日本語 文型・表現").
2. Lấy **danh sách từ vựng** của bài: `python3 -I tools/check_vocab_coverage.py N --show 100` (in các từ sách có mà khoá chưa có).
   Mọi từ thật phải vào bảng từ của đúng bài: danh từ chụp ảnh được vào `VOCAB`, từ chức năng / cụm cố định / đuôi đếm / câu giao tiếp vào `words` (+ `WORD_EX` khớp 1-1).
3. Không đưa vào: tên hư cấu của sách (công ty IMC, trường Sakura...).

## Sau khi soạn
1. Chạy `python3 -I tools/check_vocab_coverage.py <các bài vừa làm>` đến khi **không còn "THIẾU" và "SAI BÀI"** (mã thoát 0).
2. Chạy `python3 -I tools/build.py`, rồi mở thử các trang (không lỗi JS, không tràn ngang, không hỏng link).
3. Đối chiếu mẫu câu với bảng JF ở bước 1; ghi lại bài nào lệch.
4. Câu ví dụ chỉ dùng ngữ pháp **đã học tới bài đó**.

## Khi báo cáo với người học
- Nói rõ **đã so cái gì với nguồn nào** (mẫu câu / từ vựng / kanji / câu ví dụ) và cái gì **chưa so**. Không viết "đã đối chiếu", "đủ" cho cả bài khi chỉ so một phần.
- Dữ liệu từ vựng của sách chỉ để đối chiếu, **không** chép vào repo; nghĩa và câu ví dụ tự viết.
