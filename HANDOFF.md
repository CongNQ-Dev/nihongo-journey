# Bàn giao: chuyển từ phiên cloud sang Mac

Nhánh: `claude/busy-hopper-o86n4r` (repo `CongNQ-Dev/nihongo-journey`). Đọc thêm `CLAUDE.md` (quy trình soạn bài) và `NOTES.md`.

```
git fetch origin && git checkout claude/busy-hopper-o86n4r && git pull
```

## Đã làm

**Nội dung khoá học**
- Soạn bài Minna 11–50 (tệp bài 22–61; tệp bài n = Minna n−11). Mẫu câu đã so với bảng chính thức của Japan Foundation (PDF `yg.jpf.go.jp`).
- Bổ sung từ vựng bài 1–30 và 31–50: `tools/check_vocab_coverage.py` báo **2652/2652 từ**, không còn "THIẾU" hay "SAI BÀI" (đối chiếu với bộ MinnaNoDS, chỉ để kiểm tra, không chép vào repo).
- Sửa lỗi trang: tách "Giai đoạn 2 · Sơ cấp II" từ bài 26, thông báo hoàn thành ở bài cuối, ghi chú "Chưa có thẻ ảnh", sửa regex `writer()` cho nét kanji bắt đầu bằng `m` (asset `v=17`).

**Đối chiếu nguồn mở** (`tools/verify_dict.py`)
- Kanji: 251 chữ so với KANJIDIC2 (On/Kun/Hán Việt/nghĩa). Sửa 4 chỗ: 絵, 政, 中, 着 (着 ghi "(chưa xác minh)").
- Từ vựng: 1450 cặp (cách đọc, chữ viết) so với JMdict: 1386 khớp. 64 không khớp là tên riêng, thương hiệu, viết tắt, câu giao tiếp, cụm đếm, vài dạng chia (không phải lỗi).
- Đã ghi nguồn EDRDG (CC BY-SA 4.0) ở trang ghi nguồn, README, NOTES.

**Chuẩn bị cho hai việc dưới đây**
- Ảnh: `tools/candidates.json` đã có ứng viên cho **707/707 thẻ**; 473 thẻ chưa có ảnh, trong đó 28 thẻ không có ứng viên nào.
- Câu Tatoeba: `tools/tatoeba_match.py` (lọc câu chỉ gồm từ đã học tới bài đó) và `tools/tatoeba_apply.py` (thay câu tự soạn khi có `tools/tatoeba_ex.json`). Phần móc ở cuối `minna_vocab.py` và `minna_word_ex.py` hiện không làm gì vì chưa có json. Build và kiểm tra từ vựng vẫn chạy bình thường.

## Cần làm tiếp (trên Mac)

### 1. Ảnh cho 473 thẻ mới
Lý do dừng ở cloud: Wikimedia trả 429 liên tục khi tải ảnh từ IP cloud. Trên Mac thường không bị.
1. `pip install pillow`.
2. Tải thumbnail đi qua `upload.wikimedia.org` (`fetch()` đã tự đổi `thumb.wikimedia.org`).
3. Duyệt ảnh bằng `python3 -I tools/fetch_images.py sheet OUT.jpg ID1,ID2,...` (xem ảnh tổng hợp, chọn ứng viên đúng nghĩa). Font Hiragino trong script có sẵn trên macOS.
4. Điền lựa chọn vào `PICK` (id thẻ → chỉ số ứng viên); thẻ nào không có ảnh đúng nghĩa thì thêm vào `SKIP`, đừng chọn bừa. Lần trước chọn đầu danh sách đã sai nghĩa nhiều chỗ.
5. `python3 -I tools/fetch_images.py download` (có sẵn xử lý 429), rồi `python3 -I tools/build.py`.
6. Lưu ý: `cmd_download` đọc `cand[cid]["cands"][PICK.get(cid, 0)]`, sẽ lỗi với thẻ chưa có ứng viên. Cần đưa các thẻ đó vào `SKIP` trước.
7. Ghi công: `assets/img/CREDITS.md` và trang nguồn ảnh do build sinh ra từ `tools/images.json`.

### 2. Thay câu ví dụ tự soạn bằng câu Tatoeba (có nguồn)
1. Tải về một thư mục riêng, rồi giải nén (không đưa vào repo):
   - `https://downloads.tatoeba.org/exports/per_language/jpn/jpn_sentences_detailed.tsv.bz2`
   - `https://downloads.tatoeba.org/exports/per_language/jpn/jpn-eng_links.tsv.bz2`
   - `https://downloads.tatoeba.org/exports/per_language/eng/eng_sentences.tsv.bz2`
2. `python3 -I tools/tatoeba_match.py <thư mục> tools/tatoeba_ex.json` (chạy khoảng 2–5 phút; trong thử nghiệm ở cloud được khoảng 1530/2590 mục).
3. Xem mẫu kết quả bằng mắt trước khi tin. Đã thấy một số lỗi cần để ý: từ kana ngắn khớp nhầm (ví dụ さる), từ nhiều nghĩa. Có thể sửa điều kiện lọc trong `tatoeba_match.py` hoặc loại tay vài mục khỏi json.
4. `python3 -I tools/build.py`, rồi mở thử vài trang bài, thẻ ôn và chế độ "Đặt câu" (đảm bảo không lỗi JS, không tràn ngang).
5. Câu Tatoeba chỉ có bản dịch tiếng Anh (không có tiếng Việt), kèm "(Tatoeba #id, tác giả, CC BY 2.0 FR)". Câu chứa chữ Hán nên người học thấy chữ Hán trong ví dụ; xem có cần furigana không.
6. Thêm ghi nguồn Tatoeba (CC BY 2.0 FR) vào trang ghi nguồn (`tools/build.py`), `README.md`, `NOTES.md`.

### 3. Việc còn lại sau hai bước trên
Những phần này vẫn do người soạn tự viết, **chưa có nguồn**, và phải nói rõ khi báo cáo với người học:
- Nghĩa tiếng Việt của từ vựng.
- Hội thoại và giải thích ngữ pháp.
- Việc chọn chữ Hán đưa vào bài.
- Các câu ví dụ không tìm được câu Tatoeba (khoảng 40% mục).
- Mục "Nguồn nên đọc" của bài 11–50 mới chỉ trỏ tới mục lục Tae Kim.
- Hán Việt của 着 chưa xác minh.

## Quy trình sau mỗi thay đổi (theo `CLAUDE.md`)
```
python3 -I tools/check_vocab_coverage.py     # phải thoát 0
python3 -I tools/build.py                    # sinh lại trang và sw.js
```
Rồi mở thử các trang: không lỗi JS, không tràn ngang, không hỏng link. Khi báo cáo, ghi rõ **đã so cái gì với nguồn nào** và cái gì **chưa so**.

## Công cụ và nguồn
- `tools/verify_dict.py DIR [kanji|words|all]`: DIR chứa `kanjidic2.xml` và `JMdict_e` (tải từ `https://www.edrdg.org/kanjidic/kanjidic2.xml.gz` và `https://www.edrdg.org/pub/Nihongo/JMdict_e.gz`, giải nén).
- Nguồn: JF Sentence Patterns (mẫu câu), MinnaNoDS (chỉ kiểm tra từ vựng), KANJIDIC2/JMdict (EDRDG, CC BY-SA 4.0), KanjiVG (thứ tự nét, CC BY-SA 3.0), Wikimedia Commons (ảnh), Tatoeba (câu ví dụ, CC BY 2.0 FR).
