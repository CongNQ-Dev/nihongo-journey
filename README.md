# nihongo-journey

Khoá tự học tiếng Nhật từ số 0 đến JLPT N2, rồi N1 (đủ 4 kỹ năng nghe – nói – đọc – viết), dùng Minna no Nihongo làm trục chính. Bài học viết bằng tiếng Việt.

Mở `index.html` bằng Chrome hoặc Safari: mục lục gồm 11 bài bảng chữ cái (0001–0011) và Minna no Nihongo bài 1–50 (0012–0061, trọn bộ sơ cấp; bài 1–25 là trọn bộ Shokyu I), kèm thanh tiến độ tới kỳ N4. `flashcards.html` là trang ôn hằng ngày (có nút sao lưu/khôi phục tiến độ), `practice.html` luyện tự chọn, `kanji.html` kanji N5 theo từng bài Minna, `search.html` tìm nhanh từ/kanji/ngữ pháp. Chạy qua https hoặc `python3 -m http.server` thì dùng được offline và cài lên màn hình chính.

Bài 0002–0021, `assets/cards.js`, `kanji.html`, hai bảng tra cứu và `index.html` được sinh từ `tools/kana_data.py`, `tools/minna_*.py`, `tools/kanji_data.py` bằng `python3 -I tools/build.py`. Ảnh thẻ được tìm bằng `tools/fetch_images.py`. Mục tiêu và ghi chú giảng dạy nằm ở `MISSION.md` và `NOTES.md`.

Repo này không chứa nội dung sách Minna no Nihongo (có bản quyền). Bài học chỉ đi theo thứ tự của sách.

## Ghi công

- Ảnh flashcard: Wikimedia Commons, tác giả và giấy phép ở `assets/img/CREDITS.md`.
- Dữ liệu thứ tự nét (`assets/strokes.js`): [KanjiVG](https://kanjivg.tagaini.net/), CC BY-SA 3.0.
