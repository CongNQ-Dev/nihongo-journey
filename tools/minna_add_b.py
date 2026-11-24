"""Bổ sung từ vựng còn thiếu cho Minna bài 6–10 (file 0017–0021). Cùng khuôn với minna_add_a.py."""

WORDS_ADD = {
    17: [  # Minna 6
        ("なんですか。", "何ですか。", "nan desu ka?", "Dạ? Có chuyện gì vậy ạ? (đáp khi được gọi)", "ナムさん。…なんですか。", "Anh Nam. …Dạ, có chuyện gì ạ?"),
        ("じゃ、また［あした］。", "", "ja, mata [ashita]", "Hẹn gặp lại [ngày mai].", "じゃ、また あした。", "Hẹn mai gặp lại."),
        ("CD", "", "shiidii", "đĩa CD", "CDを ききます。", "Tôi nghe đĩa CD."),
        ("たばこ", "", "tabako", "thuốc lá (たばこを すいます = hút thuốc)", "ここで たばこを すいません。", "Tôi không hút thuốc ở đây."),
        ("えいが", "映画", "eiga", "phim, điện ảnh", "あした えいがを みます。", "Ngày mai tôi xem phim."),
        ("レストラン", "", "resutoran", "nhà hàng", "レストランで ごはんを たべます。", "Tôi ăn cơm ở nhà hàng."),
    ],
    18: [  # Minna 7
        ("どうぞ おあがり ください。", "どうぞ お上がり ください。", "douzo oagari kudasai", "Xin mời vào nhà ạ.", "ごめんください。…いらっしゃい。どうぞ おあがり ください。", "Xin lỗi cho tôi vào. …Chào anh. Xin mời vào nhà."),
        ("［～は］いかがですか。", "", "[~ wa] ikaga desu ka?", "Anh/chị dùng [~] nhé? (lời mời lịch sự)", "コーヒーは いかがですか。…ありがとう ございます。", "Anh dùng cà phê nhé? …Xin cảm ơn."),
        ("いただきます。", "", "itadakimasu", "Xin mời (nói trước khi ăn, uống)", "いただきます。…どうぞ。", "Xin phép ăn nhé. …Mời anh."),
        ("ごちそうさま［でした］。", "", "gochisousama [deshita]", "Cảm ơn về bữa ăn (nói sau khi ăn)", "ごちそうさまでした。…どう いたしまして。", "Cảm ơn về bữa ăn. …Không có gì ạ."),
        ("りょこう", "旅行", "ryokou", "chuyến du lịch (りょこうを します = đi du lịch)", "ナムさんは ヨーロッパへ りょこうを しました。", "Anh Nam đã đi du lịch châu Âu."),
        ("［お］みやげ", "［お］土産", "[o]miyage", "quà (mua khi đi xa về)", "ともだちに おみやげを あげました。", "Tôi đã tặng bạn quà."),
        ("ごめんください。", "", "gomen kudasai", "Xin lỗi, có ai ở nhà không ạ? (nói khi đến thăm nhà)", "ごめんください。…いらっしゃい。", "Xin lỗi cho tôi vào. …Chào anh."),
    ],
    19: [  # Minna 8
        ("～が、～", "", "~ ga, ~", "~ nhưng ~", "にほんの たべものは おいしいですが、たかいです。", "Đồ ăn Nhật ngon nhưng đắt."),
        ("おげんきですか。", "お元気ですか。", "ogenki desu ka?", "Anh/chị có khoẻ không ạ?", "おげんきですか。…はい、げんきです。", "Anh có khoẻ không? …Vâng, tôi khoẻ."),
        ("［～、］もう いっぱい いかがですか。", "［～、］もう 一杯 いかがですか。", "[~,] mou ippai ikaga desu ka?", "Anh dùng thêm một ly [~] nữa nhé?", "おちゃ、もう いっぱい いかがですか。…いただきます。", "Trà, anh dùng thêm một ly nữa nhé? …Vâng, xin phép."),
        ("［いいえ、］けっこうです。", "", "[iie,] kekkou desu", "[Không,] không cần ạ, xin cảm ơn.", "コーヒーは いかがですか。…いいえ、けっこうです。", "Anh dùng cà phê nhé? …Không ạ, cảm ơn."),
        ("もう ～です［ね］。", "", "mou ~ desu [ne]", "Đã ~ rồi [nhỉ].", "もう くじですね。", "Đã 9 giờ rồi nhỉ."),
        ("そろそろ しつれいします。", "そろそろ 失礼します。", "sorosoro shitsurei shimasu", "Sắp đến giờ tôi xin phép về.", "もう くじですね。そろそろ しつれいします。", "Đã 9 giờ rồi nhỉ. Tôi xin phép về đây."),
        ("また いらっしゃって ください。", "", "mata irasshatte kudasai", "Lần sau anh lại đến chơi nhé.", "きょうは ありがとう ございました。…また いらっしゃって ください。", "Hôm nay cảm ơn anh. …Lần sau lại đến chơi nhé."),
        ("にほんの せいかつに なれましたか。", "日本の 生活に 慣れましたか。", "nihon no seikatsu ni naremashita ka?", "Anh đã quen với cuộc sống ở Nhật chưa?", "にほんの せいかつに なれましたか。…はい、なれました。", "Anh đã quen cuộc sống ở Nhật chưa? …Vâng, tôi quen rồi."),
        ("「しちにんの さむらい」", "「七人の 侍」", "「shichinin no samurai」", "「Bảy samurai」 (bộ phim kinh điển của đạo diễn Kurosawa Akira)", "「しちにんの さむらい」は ふるいですが、おもしろい えいがです。", "“Bảy samurai” cũ nhưng là phim thú vị."),
        ("べんきょう", "勉強", "benkyou", "việc học", "にほんごの べんきょうは おもしろいです。", "Việc học tiếng Nhật thú vị."),
        ("そうですね。", "", "sou desu ne", "Ừm để xem nào (khi ngẫm nghĩ); đúng thế nhỉ", "にほんの せいかつは どうですか。…そうですね。たのしいです。", "Cuộc sống ở Nhật thế nào? …Ừm, vui."),
        ("いいえ。", "", "iie", "Không (đáp lại lời cảm ơn: không có gì)", "ありがとう ございます。…いいえ。", "Xin cảm ơn. …Không có gì."),
        ("くるま", "車", "kuruma", "ô tô, xe", "この くるまは あたらしいです。", "Chiếc xe này mới."),
    ],
    20: [  # Minna 9
        ("ごしゅじん／おくさん", "ご主人／奥さん", "goshujin / okusan", "chồng / vợ (của người khác)", "ごしゅじんは ぎんこういんですか。…はい、そうです。", "Chồng chị là nhân viên ngân hàng à? …Vâng, đúng thế."),
        ("おっと／しゅじん", "夫／主人", "otto / shujin", "chồng (của mình)", "わたしの おっとは エンジニアです。", "Chồng tôi là kỹ sư."),
        ("つま／かない", "妻／家内", "tsuma / kanai", "vợ (của mình)", "わたしの つまは にほんじんです。", "Vợ tôi là người Nhật."),
        ("かして ください。", "貸して ください。", "kashite kudasai", "Xin cho tôi mượn", "ペンを かして ください。…どうぞ。", "Cho tôi mượn cây bút. …Xin mời."),
        ("いいですよ。", "", "ii desu yo", "Được chứ ạ, vâng được.", "いっしょに いきませんか。…いいですよ。", "Ta cùng đi nhé? …Được chứ."),
        ("ああ", "", "aa", "À (à ra thế)", "ああ、わかりました。", "À, tôi hiểu rồi."),
        ("いっしょに いかがですか。", "", "issho ni ikaga desu ka?", "Anh/chị cùng ~ với chúng tôi nhé?", "あした えいがを みます。いっしょに いかがですか。", "Mai tôi đi xem phim. Anh cùng đi nhé?"),
        ("［～は］ちょっと……。", "", "[~ wa] chotto……", "[~ thì] hơi khó… (cách từ chối nhẹ nhàng)", "あした いっしょに えいがを みませんか。…あしたは ちょっと……。", "Mai cùng xem phim nhé? …Mai thì hơi khó…"),
        ("だめですか。", "", "dame desu ka?", "Không được sao ạ?", "いっしょに いきませんか。…ちょっと……。…だめですか。", "Cùng đi nhé? …Hơi khó… …Không được sao?"),
        ("また こんど おねがいします。", "また 今度 お願いします。", "mata kondo onegaishimasu", "Lần sau lại nhờ anh/chị nhé (khi từ chối lời mời)", "きょうは ちょっと……。また こんど おねがいします。", "Hôm nay hơi khó… Lần sau lại mời tôi nhé."),
        ("もしもし", "", "moshimoshi", "A lô (khi nghe điện thoại)", "もしもし、ナムです。", "A lô, tôi là Nam."),
        ("おざわせいじ", "小澤征爾", "ozawa seiji", "Ozawa Seiji (nhạc trưởng nổi tiếng người Nhật)", "おざわせいじの おんがくが すきです。", "Tôi thích âm nhạc của Ozawa Seiji."),
        ("すみません。", "", "sumimasen", "Xin lỗi; cũng dùng để cảm ơn nhẹ", "すみません、ペンを かして ください。", "Xin lỗi, cho tôi mượn cây bút."),
    ],
    21: [  # Minna 10
        ("けん", "県", "ken", "tỉnh (đơn vị hành chính của Nhật)", "ここは ちばけんです。", "Đây là tỉnh Chiba."),
        ("コーナー／スパイス・コーナー", "", "koonaa / supaisu koonaa", "góc, khu bán hàng / khu gia vị", "スパイス・コーナーは どこに ありますか。…あそこです。", "Khu gia vị ở đâu? …Ở kia."),
        ("いちばん うえ／いちばん した", "いちばん 上／いちばん 下", "ichiban ue / ichiban shita", "trên cùng / dưới cùng", "ナンプラーは いちばん したに あります。", "Nước mắm nằm ở tầng dưới cùng."),
        ("いちばん ～", "", "ichiban ~", "nhất ~ (いちばん うえ = trên cùng)", "つくえの いちばん うえに ほんが あります。", "Trên cùng của bàn có quyển sách."),
        ("おく", "奥", "oku", "phía trong cùng", "トイレは いちばん おくに あります。", "Nhà vệ sinh ở trong cùng."),
        ("～だんめ", "～段目", "-danme", "tầng kệ thứ ~", "ほんは にだんめに あります。", "Sách ở tầng kệ thứ hai."),
        ("［どうも］すみません。", "", "[doumo] sumimasen", "Xin cảm ơn / xin lỗi [nhiều].", "ここに ありますよ。…［どうも］すみません。", "Ở đây có này. …Xin cảm ơn."),
    ],
}

VOCAB = [
    # ---- 0017 · Minna 6
    (17, "おちゃ", "お茶", "ocha", "trà", "green tea cup", "おちゃを のみます。", "Tôi uống trà."),
    (17, "ビデオ", "", "bideo", "video, băng video", "VHS video cassette", "ビデオを みます。", "Tôi xem video."),
    (17, "メキシコ", "", "mekishiko", "Mexico", "Chichen Itza Mexico", "あした メキシコへ いきます。", "Ngày mai tôi đi Mexico."),
    (17, "おおさかじょうこうえん", "大阪城公園", "oosakajoukouen", "công viên lâu đài Osaka", "Osaka Castle Park", "おおさかじょうこうえんで ともだちと あいます。", "Tôi gặp bạn ở công viên lâu đài Osaka."),
    # ---- 0018 · Minna 7
    (18, "パンチ", "", "panchi", "cái bấm lỗ giấy", "paper hole punch", "ナムさんは パンチを かいました。", "Anh Nam đã mua cái bấm lỗ."),
    (18, "ホッチキス", "", "hotchikisu", "cái dập ghim", "stapler", "リンさんに ホッチキスを あげます。", "Tôi tặng chị Linh cái dập ghim."),
    (18, "セロテープ", "", "serotepu", "băng dính trong", "clear adhesive tape dispenser", "もう セロテープを かいました。", "Tôi đã mua băng dính rồi."),
    (18, "けしゴム", "消しゴム", "keshigomu", "cục tẩy", "eraser rubber", "ともだちに けしゴムを あげました。", "Tôi đã tặng bạn cục tẩy."),
    (18, "クリスマス", "", "kurisumasu", "Giáng sinh", "Christmas tree decorations", "クリスマスに ともだちに プレゼントを あげます。", "Giáng sinh tôi tặng quà cho bạn."),
    (18, "ファクス", "", "fakusu", "máy fax", "fax machine", "ファクスで てがみを おくります。", "Tôi gửi thư bằng fax."),
    (18, "ワープロ", "", "waapuro", "máy đánh chữ", "word processor typewriter Japanese", "ワープロで てがみを かきます。", "Tôi viết thư bằng máy đánh chữ."),
    (18, "スペイン", "", "supein", "Tây Ban Nha", "Sagrada Familia Barcelona", "らいしゅう スペインへ いきます。", "Tuần sau tôi đi Tây Ban Nha."),
    (18, "ヨーロッパ", "", "yooroppa", "châu Âu", "European city Europe", "らいねん ヨーロッパへ いきます。", "Sang năm tôi đi châu Âu."),
    # ---- 0019 · Minna 8
    (19, "さくら", "桜", "sakura", "hoa anh đào", "cherry blossoms Japan", "さくらは とても きれいです。", "Hoa anh đào rất đẹp."),
    (19, "やま", "山", "yama", "núi", "mountain landscape Japan", "あの やまは たかいです。", "Ngọn núi kia cao."),
    (19, "まち", "町", "machi", "thị trấn, phố", "small Japanese town street", "この まちは しずかです。", "Thị trấn này yên tĩnh."),
    (19, "りょう", "寮", "ryou", "ký túc xá", "student dormitory Japan", "りょうは ふるいですが、きれいです。", "Ký túc xá cũ nhưng sạch đẹp."),
    (19, "シャンハイ", "上海", "shanhai", "Thượng Hải", "Shanghai Pudong skyline", "シャンハイは にぎやかな まちです。", "Thượng Hải là thành phố náo nhiệt."),
    (19, "きんかくじ", "金閣寺", "kinkakuji", "chùa Kinkaku-ji (Kim Các)", "Kinkakuji Golden Pavilion Kyoto", "きんかくじは とても きれいです。", "Chùa Kinkaku-ji rất đẹp."),
    (19, "ならこうえん", "奈良公園", "narakouen", "công viên Nara", "Nara Park deer", "ならこうえんは ひろいです。", "Công viên Nara rộng."),
    (19, "びわこ", "琵琶湖", "biwako", "hồ Biwa", "Lake Biwa Shiga", "びわこは おおきいです。", "Hồ Biwa lớn."),
    # ---- 0020 · Minna 9
    (20, "クラシック", "", "kurashikku", "nhạc cổ điển", "classical orchestra concert hall", "わたしは クラシックが すきです。", "Tôi thích nhạc cổ điển."),
    (20, "ジャズ", "", "jazu", "nhạc jazz", "jazz band saxophone", "ナムさんは ジャズが すきです。", "Anh Nam thích nhạc jazz."),
    # ---- 0021 · Minna 10
    (21, "ぞう", "象", "zou", "con voi", "elephant", "あそこに ぞうが います。", "Ở đằng kia có con voi."),
    (21, "スイッチ", "", "suicchi", "công tắc", "light switch on wall", "スイッチは ドアの みぎに あります。", "Công tắc ở bên phải cửa."),
    (21, "エーティーエム", "ATM", "eetiiemu", "máy rút tiền ATM", "ATM cash machine Japan", "ぎんこうの まえに ATMが あります。", "Trước ngân hàng có máy ATM."),
    (21, "フィルム", "", "firumu", "cuộn phim (máy ảnh)", "photographic film roll", "かばんの なかに フィルムが あります。", "Trong cặp có cuộn phim."),
    (21, "ほんや", "本屋", "honya", "hiệu sách", "bookstore Japan", "えきの となりに ほんやが あります。", "Cạnh ga có hiệu sách."),
    (21, "チリソース", "", "chirisoosu", "tương ớt", "chili sauce bottle", "れいぞうこの なかに チリソースが あります。", "Trong tủ lạnh có tương ớt."),
    (21, "ナンプラー", "", "nanpuraa", "nước mắm Thái (nam pla)", "fish sauce bottle nam pla", "ナンプラーは いちばん したに あります。", "Nước mắm nằm ở tầng dưới cùng."),
    (21, "とうきょう ディズニーランド", "東京 ディズニーランド", "toukyoudizuniirando", "Tokyo Disneyland", "Tokyo Disneyland castle", "ちばけんに とうきょう ディズニーランドが あります。", "Ở tỉnh Chiba có Tokyo Disneyland."),
]

VOCAB_MOVE = {
    "v-fujisan": (19, "ふじさんは たかいです。", "Núi Phú Sĩ cao."),
}
