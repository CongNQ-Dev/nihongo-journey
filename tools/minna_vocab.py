"""Từ vựng có ảnh cho các bài Minna (0012–0021). Sửa ở đây rồi chạy tools/build.py.

VOCAB: (bài, kana, kanji, romaji, nghĩa, query Commons, câu ví dụ, nghĩa câu ví dụ)
- `bài` là số file bài học (0012 = Minna bài 1).
- Câu ví dụ chỉ dùng ngữ pháp đã học tới bài đó. Câu tự viết, không lấy từ sách.
- Id thẻ = "v-" + romaji (chỉ chữ cái). Đừng đổi romaji sau khi đã học — tiến độ ôn lưu theo id.
"""

import re

VOCAB = [
    # ---- 0012 · Minna 1
    (12, "せんせい", "先生", "sensei", "giáo viên, thầy/cô", "teacher at blackboard classroom", "たなかさんは せんせいです。", "Anh Tanaka là giáo viên."),
    (12, "がくせい", "学生", "gakusei", "học sinh, sinh viên", "university students lecture hall", "わたしは がくせいです。", "Tôi là sinh viên."),
    (12, "かいしゃいん", "会社員", "kaishain", "nhân viên công ty", "office workers business suits Tokyo", "すずきさんは かいしゃいんです。", "Chị Suzuki là nhân viên công ty."),
    (12, "いしゃ", "医者", "isha", "bác sĩ", "doctor with stethoscope", "わたしは いしゃじゃ ありません。", "Tôi không phải bác sĩ."),
    (12, "エンジニア", "", "enjinia", "kỹ sư", "engineer working factory", "ナムさんは エンジニアです。", "Anh Nam là kỹ sư."),
    (12, "けんきゅうしゃ", "研究者", "kenkyuusha", "nhà nghiên cứu", "scientist laboratory microscope", "リンさんも けんきゅうしゃですか。", "Chị Linh cũng là nhà nghiên cứu à?"),
    (12, "だいがく", "大学", "daigaku", "trường đại học", "University of Tokyo Yasuda Auditorium", "さくらだいがくの がくせいです。", "Tôi là sinh viên trường đại học Sakura."),
    (12, "びょういん", "病院", "byouin", "bệnh viện", "hospital building Japan", "すずきさんは みどりびょういんの いしゃです。", "Chị Suzuki là bác sĩ của bệnh viện Midori."),
    (12, "ベトナム", "", "betonamu", "Việt Nam", "Hoan Kiem Lake Hanoi", "ナムさんは ベトナムじんです。", "Anh Nam là người Việt Nam."),
    (12, "にほん", "日本", "nihon", "Nhật Bản", "Kiyomizu-dera Kyoto", "たなかさんは にほんじんです。", "Anh Tanaka là người Nhật."),
    # ---- 0013 · Minna 2
    (13, "ほん", "本", "hon", "quyển sách", "stack of books", "これは にほんごの ほんです。", "Đây là sách tiếng Nhật."),
    (13, "じしょ", "辞書", "jisho", "từ điển", "open dictionary pages", "それは わたしの じしょです。", "Đó là từ điển của tôi."),
    (13, "ざっし", "雑誌", "zasshi", "tạp chí", "magazines rack", "あれは くるまの ざっしです。", "Kia là tạp chí về ô tô."),
    (13, "しんぶん", "新聞", "shinbun", "tờ báo", "man reading newspaper", "この しんぶんは だれのですか。", "Tờ báo này là của ai?"),
    (13, "ノート", "", "nooto", "vở ghi", "open notebook pen", "その ノートは リンさんのです。", "Quyển vở đó là của chị Linh."),
    (13, "めいし", "名刺", "meishi", "danh thiếp", "business cards", "これは わたしの めいしです。", "Đây là danh thiếp của tôi."),
    (13, "えんぴつ", "鉛筆", "enpitsu", "bút chì", "wooden pencils", "これは えんぴつですか、ボールペンですか。", "Cái này là bút chì hay bút bi?"),
    (13, "ボールペン", "", "boorupen", "bút bi", "ballpoint pen", "この ボールペンは わたしのじゃ ありません。", "Cây bút bi này không phải của tôi."),
    (13, "とけい", "時計", "tokei", "đồng hồ", "wristwatch", "その とけいは だれのですか。", "Cái đồng hồ đó là của ai?"),
    (13, "かばん", "", "kaban", "cặp, túi xách", "leather bag", "あの かばんは せんせいのです。", "Cái cặp kia là của thầy giáo."),
    (13, "つくえ", "机", "tsukue", "bàn (học, làm việc)", "wooden desk", "これは わたしの つくえです。", "Đây là bàn của tôi."),
    (13, "チョコレート", "", "chokoreeto", "sô-cô-la", "chocolate bar", "これは ベトナムの チョコレートです。", "Đây là sô-cô-la Việt Nam."),
    (13, "おみやげ", "お土産", "omiyage", "quà mang về từ nơi mình đi", "omiyage souvenir shop Japan", "これ、おみやげです。どうぞ。", "Đây là quà, mời anh nhận."),
    # ---- 0014 · Minna 3
    (14, "きょうしつ", "教室", "kyoushitsu", "phòng học", "empty classroom desks", "きょうしつは あそこです。", "Phòng học ở đằng kia."),
    (14, "しょくどう", "食堂", "shokudou", "nhà ăn", "university cafeteria", "しょくどうは どこですか。", "Nhà ăn ở đâu ạ?"),
    (14, "うけつけ", "受付", "uketsuke", "quầy lễ tân", "reception desk lobby", "うけつけは いっかいです。", "Quầy lễ tân ở tầng một."),
    (14, "トイレ", "", "toire", "nhà vệ sinh", "restroom sign", "すみません、トイレは どこですか。", "Xin lỗi, nhà vệ sinh ở đâu ạ?"),
    (14, "かいだん", "階段", "kaidan", "cầu thang", "staircase", "かいだんは そちらです。", "Cầu thang ở phía đó ạ."),
    (14, "エスカレーター", "", "esukareetaa", "thang cuốn", "escalator", "エスカレーターは あちらです。", "Thang cuốn ở phía kia ạ."),
    (14, "じどうはんばいき", "自動販売機", "jidouhanbaiki", "máy bán hàng tự động", "vending machines Japan", "じどうはんばいきは あそこです。", "Máy bán hàng tự động ở đằng kia."),
    (14, "でんわ", "電話", "denwa", "điện thoại", "telephone", "でんわは どこですか。", "Điện thoại ở đâu ạ?"),
    (14, "くつ", "靴", "kutsu", "giày", "leather shoes", "これは イタリアの くつです。", "Đây là giày (của) Ý."),
    (14, "ワイン", "", "wain", "rượu vang", "red wine glass bottle", "この ワインは フランスのです。", "Chai vang này là của Pháp."),
    (14, "うりば", "売り場", "uriba", "quầy bán hàng (trong cửa hàng)", "department store sales floor", "くつの うりばは なんがいですか。", "Quầy giày ở tầng mấy ạ?"),
    (14, "かいしゃ", "会社", "kaisha", "công ty", "office building Tokyo", "かいしゃは どちらですか。", "Anh làm ở công ty nào ạ?"),
    # ---- 0015 · Minna 4
    (15, "おきます", "起きます", "okimasu", "thức dậy", "woman waking up stretching bed", "まいあさ ろくじに おきます。", "Sáng nào tôi cũng dậy lúc 6 giờ."),
    (15, "ねます", "寝ます", "nemasu", "ngủ, đi ngủ", "person sleeping in bed", "きのう じゅういちじに ねました。", "Hôm qua tôi đi ngủ lúc 11 giờ."),
    (15, "はたらきます", "働きます", "hatarakimasu", "làm việc", "office workers at desks", "くじから ごじまで はたらきます。", "Tôi làm việc từ 9 giờ đến 5 giờ."),
    (15, "やすみます", "休みます", "yasumimasu", "nghỉ, nghỉ ngơi", "person relaxing hammock", "にちようびは やすみます。", "Chủ nhật thì tôi nghỉ."),
    (15, "べんきょうします", "勉強します", "benkyoushimasu", "học", "student studying at desk", "まいばん べんきょうします。", "Tối nào tôi cũng học."),
    (15, "デパート", "", "depaato", "bách hoá", "Mitsukoshi Nihonbashi department store", "デパートは じゅうじから はちじまでです。", "Bách hoá mở từ 10 giờ đến 8 giờ."),
    (15, "ぎんこう", "銀行", "ginkou", "ngân hàng", "bank branch building", "ぎんこうは さんじまでです。", "Ngân hàng mở đến 3 giờ."),
    (15, "ゆうびんきょく", "郵便局", "yuubinkyoku", "bưu điện", "Japan Post office building", "ゆうびんきょくは なんじまでですか。", "Bưu điện mở đến mấy giờ?"),
    (15, "としょかん", "図書館", "toshokan", "thư viện", "library reading room bookshelves", "としょかんの やすみは げつようびです。", "Thư viện nghỉ vào thứ Hai."),
    (15, "びじゅつかん", "美術館", "bijutsukan", "bảo tàng mỹ thuật", "art museum gallery", "びじゅつかんは なんじからですか。", "Bảo tàng mỹ thuật mở từ mấy giờ?"),
    (15, "えいが", "映画", "eiga", "phim điện ảnh", "movie theater audience screen", "えいがは しちじからです。", "Phim bắt đầu từ 7 giờ."),
    (15, "しけん", "試験", "shiken", "kỳ thi", "students taking exam", "しけんは あしたです。", "Kỳ thi là ngày mai."),
    (15, "かいぎ", "会議", "kaigi", "cuộc họp", "business meeting room", "かいぎは にじから よじまでです。", "Cuộc họp từ 2 giờ đến 4 giờ."),
    # ---- 0016 · Minna 5
    (16, "でんしゃ", "電車", "densha", "tàu điện", "Tokyo commuter train", "でんしゃで かいしゃへ いきます。", "Tôi đi làm bằng tàu điện."),
    (16, "ちかてつ", "地下鉄", "chikatetsu", "tàu điện ngầm", "Tokyo Metro subway platform", "ちかてつで ぎんこうへ いきました。", "Tôi đã đi tàu điện ngầm đến ngân hàng."),
    (16, "しんかんせん", "新幹線", "shinkansen", "tàu cao tốc Shinkansen", "Shinkansen N700", "しんかんせんで きょうとへ いきます。", "Tôi đi Kyoto bằng Shinkansen."),
    (16, "バス", "", "basu", "xe buýt", "city bus Japan", "バスで うちへ かえります。", "Tôi về nhà bằng xe buýt."),
    (16, "タクシー", "", "takushii", "taxi", "Tokyo taxi", "タクシーで えきへ いきました。", "Tôi đã đi taxi ra ga."),
    (16, "ふね", "船", "fune", "tàu thuỷ, thuyền", "passenger ferry ship sea", "ふねで おきなわへ いきます。", "Tôi đi Okinawa bằng tàu thuỷ."),
    (16, "スーパー", "", "suupaa", "siêu thị", "supermarket aisle", "ともだちと スーパーへ いきます。", "Tôi đi siêu thị với bạn."),
    (16, "ともだち", "友達", "tomodachi", "bạn bè", "friends laughing together", "ともだちと きょうとへ いきました。", "Tôi đã đi Kyoto với bạn."),
    (16, "かぞく", "家族", "kazoku", "gia đình", "family portrait park", "かぞくと にほんへ きました。", "Tôi đã đến Nhật cùng gia đình."),
    (16, "たんじょうび", "誕生日", "tanjoubi", "sinh nhật", "birthday cake candles", "たんじょうびは いつですか。", "Sinh nhật bạn là khi nào?"),
    (16, "がっこう", "学校", "gakkou", "trường học", "Japanese school building", "あるいて がっこうへ いきます。", "Tôi đi bộ đến trường."),
    # ---- 0017 · Minna 6
    (17, "たべます", "食べます", "tabemasu", "ăn", "eating ramen chopsticks", "まいあさ パンを たべます。", "Sáng nào tôi cũng ăn bánh mì."),
    (17, "のみます", "飲みます", "nomimasu", "uống", "woman drinking glass of water", "いっしょに おちゃを のみませんか。", "Uống trà với tôi không?"),
    (17, "みます", "見ます", "mimasu", "xem, nhìn", "people watching fireworks", "うちで えいがを みます。", "Tôi xem phim ở nhà."),
    (17, "ききます", "聞きます", "kikimasu", "nghe", "listening to music headphones", "まいばん ラジオを ききます。", "Tối nào tôi cũng nghe đài."),
    (17, "よみます", "読みます", "yomimasu", "đọc", "woman reading a book", "でんしゃで しんぶんを よみます。", "Tôi đọc báo trên tàu."),
    (17, "かきます", "書きます", "kakimasu", "viết", "handwriting in notebook", "うちで てがみを かきます。", "Tôi viết thư ở nhà."),
    (17, "かいます", "買います", "kaimasu", "mua", "grocery shopping basket", "デパートで くつを かいました。", "Tôi đã mua giày ở bách hoá."),
    (17, "とります", "撮ります", "torimasu", "chụp (ảnh)", "tourist taking photo camera", "きょうとで しゃしんを とりました。", "Tôi đã chụp ảnh ở Kyoto."),
    (17, "ごはん", "", "gohan", "cơm; bữa ăn", "bowl of steamed rice", "いっしょに ごはんを たべましょう。", "Mình cùng ăn cơm nhé."),
    (17, "にく", "肉", "niku", "thịt", "raw beef meat", "わたしは にくを たべません。", "Tôi không ăn thịt."),
    (17, "さかな", "魚", "sakana", "cá", "fresh fish market", "スーパーで さかなを かいます。", "Tôi mua cá ở siêu thị."),
    (17, "やさい", "野菜", "yasai", "rau", "fresh vegetables market", "まいにち やさいを たべます。", "Ngày nào tôi cũng ăn rau."),
    (17, "くだもの", "果物", "kudamono", "trái cây", "fruit stand market", "くだものを かいましょう。", "Mình mua trái cây đi."),
    (17, "はなみ", "花見", "hanami", "ngắm hoa anh đào", "hanami picnic cherry blossoms", "こんしゅう はなみを しませんか。", "Tuần này đi ngắm hoa không?"),
    (17, "テニス", "", "tenisu", "quần vợt", "tennis player", "にちようびに テニスを しませんか。", "Chủ nhật chơi quần vợt không?"),
    # ---- 0018 · Minna 7
    (18, "はし", "箸", "hashi", "đũa", "chopsticks", "はしで ごはんを たべます。", "Tôi ăn cơm bằng đũa."),
    (18, "フォーク", "", "fooku", "nĩa, dĩa", "fork cutlery", "フォークで ケーキを たべます。", "Tôi ăn bánh bằng nĩa."),
    (18, "はさみ", "", "hasami", "cái kéo", "scissors", "はさみで かみを きります。", "Tôi cắt giấy bằng kéo."),
    (18, "かみ", "紙", "kami", "giấy", "stack of paper sheets", "かみと えんぴつを ください。", "Cho tôi giấy và bút chì."),
    (18, "きります", "切ります", "kirimasu", "cắt", "cutting vegetables kitchen knife", "ナイフで パンを きります。", "Tôi cắt bánh mì bằng dao."),
    (18, "パソコン", "", "pasokon", "máy tính cá nhân", "laptop computer", "パソコンで レポートを かきます。", "Tôi viết báo cáo bằng máy tính."),
    (18, "ケータイ", "", "keetai", "điện thoại di động", "smartphone in hand", "ケータイで しゃしんを とります。", "Tôi chụp ảnh bằng điện thoại."),
    (18, "プレゼント", "", "purezento", "quà tặng", "gift box ribbon", "たんじょうびに プレゼントを もらいました。", "Tôi đã nhận quà vào sinh nhật."),
    (18, "おかね", "お金", "okane", "tiền", "Japanese yen banknotes coins", "ちちに おかねを もらいました。", "Tôi đã nhận tiền từ bố."),
    (18, "きっぷ", "切符", "kippu", "vé (tàu, xe)", "Japanese train ticket", "もう きっぷを かいましたか。", "Bạn đã mua vé chưa?"),
    (18, "ねんがじょう", "年賀状", "nengajou", "thiệp chúc Tết", "nengajo New Year card", "ともだちに ねんがじょうを おくります。", "Tôi gửi thiệp Tết cho bạn."),
    (18, "にもつ", "荷物", "nimotsu", "hành lý, bưu kiện", "parcels cardboard packages", "ははに にもつを おくりました。", "Tôi đã gửi bưu kiện cho mẹ."),
    (18, "おしえます", "教えます", "oshiemasu", "dạy", "teacher teaching students", "リンさんに にほんごを おしえます。", "Tôi dạy tiếng Nhật cho chị Linh."),
    (18, "かけます", "", "kakemasu", "gọi (điện thoại)", "man talking on phone", "かぞくに でんわを かけます。", "Tôi gọi điện cho gia đình."),
    # ---- 0019 · Minna 8
    (19, "おおきい", "大きい", "ookii", "to, lớn", "Great Buddha of Kamakura", "かまくらの だいぶつは おおきいです。", "Tượng Đại Phật ở Kamakura rất to."),
    (19, "ちいさい", "小さい", "chiisai", "nhỏ, bé", "tiny kitten in hand", "この ねこは ちいさいです。", "Con mèo này nhỏ."),
    (19, "ふるい", "古い", "furui", "cũ, cổ", "old wooden house Japan", "この うちは ふるいです。", "Căn nhà này cũ."),
    (19, "あつい", "暑い", "atsui", "nóng (thời tiết)", "hot summer sun", "ベトナムは とても あついです。", "Việt Nam rất nóng."),
    (19, "さむい", "寒い", "samui", "lạnh (thời tiết)", "snowy street winter Hokkaido", "ほっかいどうは さむいです。", "Hokkaido lạnh."),
    (19, "たかい", "高い", "takai", "cao; đắt", "Tokyo Skytree", "スカイツリーは たかいです。", "Tháp Skytree cao."),
    (19, "おいしい", "", "oishii", "ngon", "ramen bowl", "この ラーメンは おいしいです。", "Bát ramen này ngon."),
    (19, "しずか", "静か", "shizuka", "yên tĩnh", "Ryoan-ji rock garden", "きょうとは しずかな まちです。", "Kyoto là thành phố yên tĩnh."),
    (19, "にぎやか", "", "nigiyaka", "náo nhiệt, đông vui", "Shibuya crossing crowd", "しぶやは にぎやかです。", "Shibuya náo nhiệt."),
    (19, "きれい", "", "kirei", "đẹp; sạch", "Japanese garden pond autumn", "この にわは きれいですね。", "Khu vườn này đẹp nhỉ."),
    (19, "いそがしい", "忙しい", "isogashii", "bận", "busy commuters rush hour station", "しごとは いそがしいですが、おもしろいです。", "Công việc bận nhưng thú vị."),
    (19, "レストラン", "", "resutoran", "nhà hàng", "restaurant interior", "あれは どんな レストランですか。", "Kia là nhà hàng như thế nào?"),
    # ---- 0020 · Minna 9
    (20, "りょうり", "料理", "ryouri", "món ăn; nấu ăn", "Japanese cuisine kaiseki", "にほんの りょうりが すきです。", "Tôi thích món Nhật."),
    (20, "やきゅう", "野球", "yakyuu", "bóng chày", "baseball game stadium Japan", "やきゅうが すきですか。", "Bạn có thích bóng chày không?"),
    (20, "ダンス", "", "dansu", "nhảy, khiêu vũ", "dancers dancing stage", "リンさんは ダンスが じょうずです。", "Chị Linh nhảy giỏi."),
    (20, "りょこう", "旅行", "ryokou", "du lịch", "tourists with suitcase", "りょこうが すきです。", "Tôi thích du lịch."),
    (20, "おんがく", "音楽", "ongaku", "âm nhạc", "orchestra concert", "どんな おんがくが すきですか。", "Bạn thích loại nhạc nào?"),
    (20, "うた", "歌", "uta", "bài hát", "singer singing microphone", "わたしは うたが へたです。", "Tôi hát dở."),
    (20, "カラオケ", "", "karaoke", "karaoke", "karaoke room", "カラオケは あまり すきじゃ ありません。", "Tôi không thích karaoke lắm."),
    (20, "かぶき", "歌舞伎", "kabuki", "kịch Kabuki", "kabuki actor", "かぶきが わかりますか。", "Bạn có hiểu Kabuki không?"),
    (20, "え", "絵", "e", "tranh, bức vẽ", "painting on easel", "ナムさんは えが じょうずです。", "Anh Nam vẽ giỏi."),
    (20, "かんじ", "漢字", "kanji", "chữ Hán (kanji)", "kanji calligraphy brush", "かんじが すこし わかります。", "Tôi hiểu chút ít chữ Hán."),
    (20, "コンサート", "", "konsaato", "buổi hoà nhạc", "rock concert crowd", "コンサートの チケットが あります。", "Tôi có vé buổi hoà nhạc."),
    (20, "アルバイト", "", "arubaito", "việc làm thêm", "convenience store clerk", "アルバイトが ありますから、かえります。", "Tôi có việc làm thêm nên về đây."),
    (20, "こども", "子ども", "kodomo", "trẻ con; con cái", "children playing park", "こどもは やさいが きらいです。", "Con tôi ghét rau."),
    # ---- 0021 · Minna 10
    (21, "おとこのひと", "男の人", "otokonohito", "người đàn ông", "man portrait outdoors", "あそこに おとこのひとが います。", "Ở đằng kia có một người đàn ông."),
    (21, "おんなのひと", "女の人", "onnanohito", "người phụ nữ", "woman portrait smiling", "あの おんなのひとは だれですか。", "Người phụ nữ kia là ai?"),
    (21, "おとこのこ", "男の子", "otokonoko", "bé trai", "boy portrait", "こうえんに おとこのこが います。", "Trong công viên có một bé trai."),
    (21, "おんなのこ", "女の子", "onnanoko", "bé gái", "girl portrait", "おんなのこは きの したに います。", "Bé gái ở dưới gốc cây."),
    (21, "パンダ", "", "panda", "gấu trúc", "giant panda eating bamboo", "うえのに パンダが います。", "Ở Ueno có gấu trúc."),
    (21, "き", "木", "ki", "cây", "big old tree", "きの したに ねこが います。", "Dưới gốc cây có con mèo."),
    (21, "はこ", "箱", "hako", "cái hộp", "cardboard box", "はこの なかに なにが ありますか。", "Trong hộp có gì?"),
    (21, "テーブル", "", "teeburu", "cái bàn", "dining table", "テーブルの うえに りんごが あります。", "Trên bàn có quả táo."),
    (21, "たな", "棚", "tana", "cái kệ, giá", "wooden shelves", "たなの うえに なにが ありますか。", "Trên kệ có gì?"),
    (21, "まど", "窓", "mado", "cửa sổ", "window", "まどの ちかくに つくえが あります。", "Gần cửa sổ có cái bàn."),
    (21, "ドア", "", "doa", "cửa ra vào", "front door", "ドアの まえに にもつが あります。", "Trước cửa có bưu kiện."),
    (21, "ポスト", "", "posuto", "hòm thư", "Japanese red post box", "ゆうびんきょくの まえに ポストが あります。", "Trước bưu điện có hòm thư."),
    (21, "コンビニ", "", "konbini", "cửa hàng tiện lợi", "Japanese convenience store exterior", "えきの となりに コンビニが あります。", "Cạnh ga có cửa hàng tiện lợi."),
    (21, "こうえん", "公園", "kouen", "công viên", "park Japan", "こうえんに きが たくさん あります。", "Trong công viên có nhiều cây."),
    (21, "きっさてん", "喫茶店", "kissaten", "quán cà phê", "kissaten coffee shop Japan", "ぎんこうと ゆうびんきょくの あいだに きっさてんが あります。", "Giữa ngân hàng và bưu điện có quán cà phê."),
]


# ---- Bài mở rộng (Minna 11+): mỗi file minna_ext_*.py có LESSONS / VOCAB / WORD_EX / KANJI ----
EXT_MODULES = ("minna_ext_a", "minna_ext_b", "minna_ext_c", "minna_ext_d", "minna_add_a", "minna_add_b", "minna_add_c", "minna_add_d", "minna_add_e")
import importlib as _il
for _name in EXT_MODULES:
    try:
        _m = _il.import_module(_name)
    except ModuleNotFoundError:
        continue
    VOCAB.extend(getattr(_m, "VOCAB", []))
    for _rid, (_les, _ex, _exvn) in getattr(_m, "VOCAB_MOVE", {}).items():   # chuyển từ về đúng bài (kèm câu ví dụ hợp ngữ pháp bài đó)
        for _i, _v in enumerate(VOCAB):
            if "v-" + re.sub(r"[^a-z0-9]", "", _v[3].lower()) == _rid:
                VOCAB[_i] = (_les, _v[1], _v[2], _v[3], _v[4], _v[5], _ex, _exvn)


def vocab_id(v):
    import re
    return "v-" + re.sub(r"[^a-z0-9]", "", v[3].lower())
