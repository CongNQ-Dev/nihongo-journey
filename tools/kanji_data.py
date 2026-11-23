"""Kanji N5 khởi đầu, gắn với bài Minna (0012 = Minna bài 1). Sửa ở đây rồi chạy:
    python3 -I tools/fetch_strokes.py   (tải thứ tự nét từ KanjiVG, chỉ khi thêm chữ mới)
    python3 -I tools/build.py

KANJI: (bài, chữ, âm On, âm Kun, Hán Việt, nghĩa, từ (kanji), cách đọc từ (kana), romaji từ, nghĩa từ)
- `bài` = số file bài học nơi chữ này xuất hiện đầu tiên trong từ vựng.
- Id thẻ = "kj-" + mã Unicode (hex). Không đổi chữ sau khi đã học — tiến độ ôn lưu theo id.
- Cột âm On/Kun để trống "" khi không có.
"""

KANJI = [
    # ---- 0012 · Minna 1
    (12, "先", "セン", "さき", "Tiên", "trước, đi trước", "先生", "せんせい", "sensei", "giáo viên"),
    (12, "生", "セイ・ショウ", "い-きる・う-まれる", "Sinh", "sống, sinh ra", "学生", "がくせい", "gakusei", "học sinh, sinh viên"),
    (12, "学", "ガク", "まな-ぶ", "Học", "học", "大学", "だいがく", "daigaku", "trường đại học"),
    (12, "会", "カイ", "あ-う", "Hội", "họp, gặp", "会社員", "かいしゃいん", "kaishain", "nhân viên công ty"),
    (12, "社", "シャ", "やしろ", "Xã", "công ty, đền", "会社", "かいしゃ", "kaisha", "công ty"),
    (12, "大", "ダイ・タイ", "おお-きい", "Đại", "to, lớn", "大学", "だいがく", "daigaku", "trường đại học"),
    (12, "日", "ニチ・ジツ", "ひ・か", "Nhật", "ngày; mặt trời", "日本", "にほん", "nihon", "Nhật Bản"),
    (12, "本", "ホン", "もと", "Bản", "sách; gốc", "日本", "にほん", "nihon", "Nhật Bản"),
    (12, "人", "ジン・ニン", "ひと", "Nhân", "người", "日本人", "にほんじん", "nihonjin", "người Nhật"),
    # ---- 0013 · Minna 2
    (13, "新", "シン", "あたら-しい", "Tân", "mới", "新聞", "しんぶん", "shinbun", "tờ báo"),
    (13, "聞", "ブン・モン", "き-く", "Văn", "nghe, hỏi", "新聞", "しんぶん", "shinbun", "tờ báo"),
    (13, "書", "ショ", "か-く", "Thư", "viết; sách", "辞書", "じしょ", "jisho", "từ điển"),
    (13, "時", "ジ", "とき", "Thời", "giờ, thời gian", "時計", "とけい", "tokei", "đồng hồ"),
    # ---- 0014 · Minna 3
    (14, "教", "キョウ", "おし-える", "Giáo", "dạy", "教室", "きょうしつ", "kyoushitsu", "phòng học"),
    (14, "室", "シツ", "", "Thất", "phòng", "教室", "きょうしつ", "kyoushitsu", "phòng học"),
    (14, "食", "ショク", "た-べる", "Thực", "ăn", "食堂", "しょくどう", "shokudou", "nhà ăn"),
    (14, "電", "デン", "", "Điện", "điện", "電話", "でんわ", "denwa", "điện thoại"),
    (14, "話", "ワ", "はな-す", "Thoại", "nói chuyện", "電話", "でんわ", "denwa", "điện thoại"),
    (14, "下", "カ・ゲ", "した", "Hạ", "dưới", "地下鉄", "ちかてつ", "chikatetsu", "tàu điện ngầm"),
    (14, "売", "バイ", "う-る", "Mại", "bán", "売り場", "うりば", "uriba", "quầy bán hàng"),
    # ---- 0015 · Minna 4
    (15, "休", "キュウ", "やす-む", "Hưu", "nghỉ", "休みます", "やすみます", "yasumimasu", "nghỉ"),
    (15, "行", "コウ・ギョウ", "い-く", "Hành", "đi; hàng", "銀行", "ぎんこう", "ginkou", "ngân hàng"),
    (15, "銀", "ギン", "", "Ngân", "bạc", "銀行", "ぎんこう", "ginkou", "ngân hàng"),
    (15, "強", "キョウ", "つよ-い", "Cường", "mạnh", "勉強します", "べんきょうします", "benkyoushimasu", "học"),
    (15, "勉", "ベン", "", "Miễn", "cố gắng", "勉強します", "べんきょうします", "benkyoushimasu", "học"),
    # ---- 0016 · Minna 5
    (16, "車", "シャ", "くるま", "Xa", "xe", "電車", "でんしゃ", "densha", "tàu điện"),
    (16, "友", "ユウ", "とも", "Hữu", "bạn", "友達", "ともだち", "tomodachi", "bạn bè"),
    (16, "家", "カ", "いえ・うち", "Gia", "nhà", "家族", "かぞく", "kazoku", "gia đình"),
    (16, "校", "コウ", "", "Hiệu", "trường học", "学校", "がっこう", "gakkou", "trường học"),
    (16, "鉄", "テツ", "", "Thiết", "sắt", "地下鉄", "ちかてつ", "chikatetsu", "tàu điện ngầm"),
    # ---- 0017 · Minna 6
    (17, "飲", "イン", "の-む", "Ẩm", "uống", "飲みます", "のみます", "nomimasu", "uống"),
    (17, "見", "ケン", "み-る", "Kiến", "nhìn, xem", "見ます", "みます", "mimasu", "xem, nhìn"),
    (17, "読", "ドク", "よ-む", "Độc", "đọc", "読みます", "よみます", "yomimasu", "đọc"),
    (17, "買", "バイ", "か-う", "Mãi", "mua", "買います", "かいます", "kaimasu", "mua"),
    (17, "肉", "ニク", "", "Nhục", "thịt", "肉", "にく", "niku", "thịt"),
    (17, "魚", "ギョ", "さかな", "Ngư", "cá", "魚", "さかな", "sakana", "cá"),
    (17, "花", "カ", "はな", "Hoa", "hoa", "花見", "はなみ", "hanami", "ngắm hoa anh đào"),
    # ---- 0018 · Minna 7
    (18, "紙", "シ", "かみ", "Chỉ", "giấy", "紙", "かみ", "kami", "giấy"),
    (18, "切", "セツ", "き-る", "Thiết", "cắt", "切符", "きっぷ", "kippu", "vé"),
    (18, "金", "キン", "かね", "Kim", "vàng; tiền", "お金", "おかね", "okane", "tiền"),
    (18, "年", "ネン", "とし", "Niên", "năm", "年賀状", "ねんがじょう", "nengajou", "thiệp chúc Tết"),
    # ---- 0019 · Minna 8
    (19, "小", "ショウ", "ちい-さい", "Tiểu", "nhỏ", "小さい", "ちいさい", "chiisai", "nhỏ, bé"),
    (19, "高", "コウ", "たか-い", "Cao", "cao; đắt", "高い", "たかい", "takai", "cao; đắt"),
    (19, "古", "コ", "ふる-い", "Cổ", "cũ", "古い", "ふるい", "furui", "cũ, cổ"),
    # ---- 0020 · Minna 9
    (20, "音", "オン", "おと", "Âm", "âm thanh", "音楽", "おんがく", "ongaku", "âm nhạc"),
    (20, "楽", "ガク・ラク", "たの-しい", "Nhạc", "nhạc; vui", "音楽", "おんがく", "ongaku", "âm nhạc"),
    (20, "歌", "カ", "うた", "Ca", "hát, bài hát", "歌", "うた", "uta", "bài hát"),
    (20, "絵", "カイ", "え", "Hội", "tranh", "絵", "え", "e", "tranh, bức vẽ"),
    (20, "子", "シ", "こ", "Tử", "con", "子ども", "こども", "kodomo", "trẻ con"),
    # ---- 0021 · Minna 10
    (21, "男", "ダン", "おとこ", "Nam", "đàn ông", "男の人", "おとこのひと", "otoko no hito", "người đàn ông"),
    (21, "女", "ジョ", "おんな", "Nữ", "phụ nữ", "女の人", "おんなのひと", "onna no hito", "người phụ nữ"),
    (21, "木", "モク", "き", "Mộc", "cây, gỗ", "木", "き", "ki", "cây"),
    (21, "店", "テン", "みせ", "Điếm", "cửa hàng", "喫茶店", "きっさてん", "kissaten", "quán cà phê"),
    (21, "公", "コウ", "", "Công", "công cộng", "公園", "こうえん", "kouen", "công viên"),
    (21, "園", "エン", "その", "Viên", "vườn", "公園", "こうえん", "kouen", "công viên"),
]


# ---- Bài mở rộng (Minna 11+): mỗi file minna_ext_*.py có LESSONS / VOCAB / WORD_EX / KANJI ----
EXT_MODULES = ("minna_ext_a", "minna_ext_b", "minna_ext_c", "minna_ext_d", "minna_ext_g", "minna_ext_h")
import importlib as _il
for _name in EXT_MODULES:
    try:
        _m = _il.import_module(_name)
    except ModuleNotFoundError:
        continue
    KANJI.extend(_m.KANJI)
