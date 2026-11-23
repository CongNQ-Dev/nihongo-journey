"""Bổ sung từ vựng còn thiếu cho Minna bài 1–5 (file 0012–0016), phát hiện bằng tools/check_vocab_coverage.py.

WORDS_ADD[file] = [(kana, kanji, romaji, nghĩa, câu ví dụ, nghĩa câu)] — từ chức năng / câu cố định / đuôi đếm / địa danh.
VOCAB = từ có ảnh (cùng khuôn minna_vocab.py). VOCAB_MOVE = từ đã có nhưng nằm sai bài.
Câu ví dụ chỉ dùng ngữ pháp đã học tới bài đó. Nghĩa và câu tự viết.
"""

WORDS_ADD = {
    12: [  # Minna 1
        ("～ちゃん", "", "-chan", "hậu tố gọi trẻ nhỏ (thay ～さん)", "リンちゃんは ごさいです。", "Bé Linh 5 tuổi."),
        ("～くん", "～君", "-kun", "hậu tố gọi bạn nam, người nhỏ tuổi hơn (thay ～さん)", "ナムくんは がくせいです。", "Cậu Nam là sinh viên."),
        ("きょうし", "教師", "kyoushi", "giáo viên (nghề nghiệp, nói về mình)", "わたしは だいがくの きょうしです。", "Tôi là giáo viên đại học."),
        ("しゃいん", "社員", "shain", "nhân viên (của công ty ~)", "ナムさんは パワーでんきの しゃいんです。", "Anh Nam là nhân viên công ty Power Denki."),
        ("ぎんこういん", "銀行員", "ginkouin", "nhân viên ngân hàng", "たなかさんは ぎんこういんです。", "Anh Tanaka là nhân viên ngân hàng."),
        ("わたしたち", "", "watashitachi", "chúng tôi, chúng ta", "わたしたちは ベトナムじんです。", "Chúng tôi là người Việt Nam."),
        ("みなさん", "皆さん", "minasan", "mọi người, quý vị", "みなさん、はじめまして。", "Xin chào mọi người, rất hân hạnh."),
        ("おなまえは？", "お名前は？", "onamae wa?", "Tên bạn là gì ạ? (lịch sự)", "おなまえは？…ナムです。", "Tên bạn là gì? …Tôi là Nam."),
        ("こちらは ～さんです。", "", "kochira wa ~san desu", "Đây là anh/chị ~ (giới thiệu người)", "こちらは リンさんです。", "Đây là chị Linh."),
        ("でんき", "電気", "denki", "điện, đèn điện (có trong tên công ty パワーでんき)", "あの ひとは でんきの エンジニアです。", "Người kia là kỹ sư điện."),
    ],
    13: [  # Minna 2
        ("えいご／にほんご", "英語／日本語", "eigo / nihongo", "tiếng Anh / tiếng Nhật", "これは えいごの ほんです。", "Đây là sách tiếng Anh."),
        ("えっ", "", "e'", "Hả? Ồ? (ngạc nhiên khi nghe điều bất ngờ)", "えっ、それは だれのですか。", "Hả, đó là của ai vậy?"),
        ("あ", "", "a", "À! Ồ! (chợt nhận ra điều gì)", "あ、これは わたしのです。", "À, cái này là của tôi."),
        ("［どうも］ありがとう［ございます］。", "", "[doumo] arigatou [gozaimasu]", "Xin cảm ơn [rất nhiều].", "これ、どうぞ。…ありがとう ございます。", "Mời bạn cái này. …Xin cảm ơn."),
        ("これから おせわに なります。", "これから お世話に なります。", "kore kara osewa ni narimasu", "Từ nay xin được giúp đỡ (nói khi bắt đầu một mối quan hệ)", "ナムです。これから おせわに なります。", "Tôi là Nam. Từ nay xin được giúp đỡ."),
        ("こちらこそ［どうぞ］よろしく［おねがいします］。", "こちらこそ［どうぞ］よろしく［お願いします］。", "kochira koso [douzo] yoroshiku [onegaishimasu]", "Chính tôi mới xin được giúp đỡ (đáp lại lời chào làm quen)", "どうぞ よろしく おねがいします。…こちらこそ よろしく おねがいします。", "Rất mong được giúp đỡ. …Tôi cũng rất mong được giúp đỡ."),
        ("ほんの きもちです。", "ほんの 気持ちです。", "hon no kimochi desu", "Chỉ là chút lòng thành (nói khi tặng quà)", "これは ベトナムの おみやげです。ほんの きもちです。", "Đây là quà từ Việt Nam. Chỉ là chút lòng thành."),
        ("どうも。", "", "doumo", "Cảm ơn nhé (cách nói ngắn, thân mật)", "これ、どうぞ。…どうも。", "Mời bạn cái này. …Cảm ơn nhé."),
    ],
    14: [  # Minna 3
        ("～かい（～がい）", "～階", "-kai (-gai)", "tầng ~ (さんがい = tầng 3, なんがい = tầng mấy)", "トイレは にかいです。", "Nhà vệ sinh ở tầng hai."),
        ("～えん", "～円", "-en", "~ yên", "この ネクタイは ごひゃくえんです。", "Chiếc cà vạt này 500 yên."),
        ("どうも。", "", "doumo", "Cảm ơn (ngắn gọn)", "これを ください。…はい、どうぞ。…どうも。", "Cho tôi cái này. …Vâng, xin mời. …Cảm ơn."),
        ("［～を］みせて ください。", "［～を］見せて ください。", "[~ o] misete kudasai", "Xin cho tôi xem [~]", "それを みせて ください。", "Xin cho tôi xem cái đó."),
        ("～で ございます。", "", "~ de gozaimasu", "(dạng rất lịch sự của です)", "ここは ロビーで ございます。", "Đây là sảnh ạ."),
        ("いらっしゃいませ。", "", "irasshaimase", "Kính chào quý khách (nhân viên cửa hàng nói)", "いらっしゃいませ。…これを ください。", "Kính chào quý khách. …Cho tôi cái này."),
        ("イタリア／スイス／フランス", "", "Itaria / Suisu / Furansu", "Ý / Thuỵ Sĩ / Pháp", "これは イタリアの くつです。", "Đây là giày của Ý."),
        ("ジャカルタ／バンコク／ベルリン", "", "Jakaruta / Bankoku / Berurin", "Jakarta / Bangkok / Berlin", "ここは バンコクです。", "Đây là Bangkok."),
        ("しんおおさか", "新大阪", "shin-oosaka", "Shin-Osaka (tên một nhà ga ở Osaka)", "あそこは しんおおさかです。", "Chỗ kia là Shin-Osaka."),
    ],
    15: [  # Minna 4
        ("おととい／あさって", "", "ototoi / asatte", "hôm kia / ngày kia", "きょうは げつようびです。あさっては すいようびです。", "Hôm nay là thứ Hai. Ngày kia là thứ Tư."),
        ("なんぷん", "何分", "nanpun", "mấy phút", "いま なんぷんですか。", "Bây giờ là mấy phút?"),
        ("～まで", "", "-made", "đến ~, cho tới ~", "くじから ごじまで はたらきます。", "Tôi làm việc từ 9 giờ đến 5 giờ."),
        ("～から", "", "-kara", "từ ~", "ぎんこうは くじからです。", "Ngân hàng mở cửa từ 9 giờ."),
        ("～と ～", "", "~ to ~", "~ và ~ (nối danh từ)", "やすみは どようびと にちようびです。", "Ngày nghỉ là thứ Bảy và Chủ nhật."),
        ("ばんごう／なんばん", "番号／何番", "bangou / nanban", "số hiệu / số mấy", "でんわばんごうは なんばんですか。", "Số điện thoại là số mấy?"),
        ("バンコク", "", "Bankoku", "Bangkok", "バンコクの ぎんこうは くじからです。", "Ngân hàng ở Bangkok mở từ 9 giờ."),
        ("えーと", "", "eeto", "ừm, để xem nào (khi ngập ngừng)", "えーと、いま くじはんです。", "Ừm, bây giờ là 9 giờ rưỡi."),
        ("１０４", "", "hyaku-yon", "104 (số tổng đài hỏi số điện thoại ở Nhật)", "１０４に でんわします。", "Tôi gọi 104."),
        ("おねがいします。", "お願いします。", "onegaishimasu", "Làm ơn, nhờ anh/chị", "でんわばんごうを おねがいします。", "Xin cho tôi số điện thoại."),
        ("かしこまりました。", "", "kashikomarimashita", "Vâng, tôi hiểu rồi ạ (nhân viên đáp lại khách)", "ぎんこうの ばんごうを おねがいします。…かしこまりました。", "Cho tôi số của ngân hàng. …Vâng ạ."),
        ("おといあわせのばんごう", "お問い合わせの番号", "otoiawase no bangou", "số điện thoại bạn đang hỏi (cách nói của tổng đài)", "おといあわせの ばんごうは ０３－３４５６－７８９０です。", "Số bạn hỏi là 03-3456-7890."),
        ("［どうも］ありがとう ございました。", "", "[doumo] arigatou gozaimashita", "Xin cảm ơn [rất nhiều] (khi việc đã xong)", "ぎんこうの ばんごうは ７３７－１２３４です。…ありがとう ございました。", "Số ngân hàng là 737-1234. …Xin cảm ơn."),
        ("そちら", "", "sochira", "phía đó, chỗ bạn (lịch sự)", "そちらは なんじまでですか。", "Chỗ anh đóng cửa lúc mấy giờ ạ?"),
    ],
    16: [  # Minna 5
        ("ついたち／ふつか／みっか／よっか／いつか", "１日／２日／３日／４日／５日", "tsuitachi / futsuka / mikka / yokka / itsuka", "ngày 1 / 2 / 3 / 4 / 5 trong tháng", "たんじょうびは さんがつ ふつかです。", "Sinh nhật tôi là ngày 2 tháng 3."),
        ("むいか／なのか／ようか／ここのか／とおか", "６日／７日／８日／９日／１０日", "muika / nanoka / youka / kokonoka / tooka", "ngày 6 / 7 / 8 / 9 / 10 trong tháng", "とおかに きょうとへ いきます。", "Ngày 10 tôi đi Kyoto."),
        ("じゅうよっか／はつか／にじゅうよっか", "１４日／２０日／２４日", "juuyokka / hatsuka / nijuuyokka", "ngày 14 / 20 / 24 trong tháng", "はつかに にほんへ きます。", "Ngày 20 tôi đến Nhật."),
        ("～にち", "～日", "-nichi", "ngày ~ (các ngày khác trong tháng); ~ ngày", "じゅうごにちに ともだちと いきます。", "Ngày 15 tôi đi cùng bạn."),
        ("～ねん／なんねん", "～年／何年", "-nen / nannen", "năm ~ / năm nào", "わたしは ２０２６ねんに にほんへ きました。", "Tôi đã đến Nhật vào năm 2026."),
        ("［どうも］ありがとう ございました。", "", "[doumo] arigatou gozaimashita", "Xin cảm ơn [rất nhiều] (khi việc đã xong)", "ありがとう ございました。…どう いたしまして。", "Xin cảm ơn. …Không có gì ạ."),
        ("どう いたしまして。", "", "dou itashimashite", "Không có gì ạ (đáp lại lời cảm ơn)", "ありがとう ございました。…どう いたしまして。", "Xin cảm ơn. …Không có gì ạ."),
        ("～ばんせん", "～番線", "-bansen", "sân ga số ~", "でんしゃは ごばんせんから いきます。", "Tàu điện khởi hành từ sân ga số 5."),
        ("つぎの", "次の", "tsugi no", "tiếp theo, kế tiếp", "つぎの でんしゃは なんじですか。", "Chuyến tàu tiếp theo mấy giờ?"),
        ("ふつう／きゅうこう／とっきゅう", "普通／急行／特急", "futsuu / kyuukou / tokkyuu", "tàu thường / tàu nhanh / tàu tốc hành đặc biệt", "とっきゅうで おおさかへ いきます。", "Tôi đi Osaka bằng tàu tốc hành đặc biệt."),
        ("ひと", "人", "hito", "người", "あの ひとは リンさんです。", "Người kia là chị Linh."),
        ("はかた／ふしみ", "博多／伏見", "hakata / fushimi", "Hakata (thành phố ở Kyushu) / Fushimi (khu phố ở Kyoto)", "でんしゃで はかたへ いきます。", "Tôi đi Hakata bằng tàu điện."),
    ],
}

VOCAB = [
    # ---- 0012 · Minna 1: các nước
    (12, "アメリカ", "", "amerika", "Mỹ, Hoa Kỳ", "Statue of Liberty New York", "ミラーさんは アメリカじんです。", "Anh Miller là người Mỹ."),
    (12, "イギリス", "", "igirisu", "Anh", "Big Ben London", "ブラウンさんは イギリスじんです。", "Anh Brown là người Anh."),
    (12, "インド", "", "indo", "Ấn Độ", "Taj Mahal Agra", "ラオさんは インドじんです。", "Anh Rao là người Ấn Độ."),
    (12, "インドネシア", "", "indoneshia", "Indonesia", "Borobudur temple Indonesia", "あの ひとは インドネシアじんじゃ ありません。", "Người kia không phải người Indonesia."),
    (12, "かんこく", "韓国", "kankoku", "Hàn Quốc", "Gyeongbokgung palace Seoul", "キムさんは かんこくじんです。", "Anh Kim là người Hàn Quốc."),
    (12, "タイ", "", "tai", "Thái Lan", "Wat Arun Bangkok", "ワンさんは タイじんですか。", "Anh Wang là người Thái Lan à?"),
    (12, "ドイツ", "", "doitsu", "Đức", "Brandenburg Gate Berlin", "シュミットさんは ドイツじんです。", "Anh Schmidt là người Đức."),
    (12, "ブラジル", "", "burajiru", "Brazil", "Christ the Redeemer Rio de Janeiro", "サントスさんは ブラジルじんです。", "Anh Santos là người Brazil."),
    (12, "フランス", "", "furansu", "Pháp", "Eiffel Tower Paris", "あの ひとは フランスじんです。", "Người kia là người Pháp."),
    (12, "ちゅうごく", "中国", "chuugoku", "Trung Quốc", "Great Wall of China", "ワンさんも ちゅうごくじんですか。", "Anh Wang cũng là người Trung Quốc à?"),
    # ---- 0013 · Minna 2
    (13, "てちょう", "手帳", "techou", "sổ tay (sổ ghi lịch)", "personal organizer planner notebook", "これは わたしの てちょうです。", "Đây là sổ tay của tôi."),
    (13, "カード", "", "kaado", "thẻ (tín dụng)", "credit cards", "それは だれの カードですか。", "Đó là thẻ của ai vậy?"),
    (13, "シャープペンシル", "", "shaapupenshiru", "bút chì bấm", "mechanical pencil", "これは シャープペンシルですか、ボールペンですか。", "Đây là bút chì bấm hay bút bi?"),
    (13, "シーディー", "CD", "shiidii", "đĩa CD", "compact disc CD", "それは にほんの CDですか。", "Đó là đĩa CD của Nhật phải không?"),
    (13, "ラジオ", "", "rajio", "radio", "portable radio", "あれは ラジオです。", "Kia là cái radio."),
    (13, "カメラ", "", "kamera", "máy ảnh", "camera", "これは リンさんの カメラです。", "Đây là máy ảnh của chị Linh."),
    (13, "コンピューター", "", "konpyuutaa", "máy tính", "desktop computer", "それは だれの コンピューターですか。", "Đó là máy tính của ai?"),
    (13, "くるま", "車", "kuruma", "xe ô tô", "car on street Japan", "あれは たなかさんの くるまです。", "Kia là ô tô của anh Tanaka."),
    (13, "いす", "", "isu", "cái ghế", "wooden chair", "それは わたしの いすです。", "Đó là ghế của tôi."),
    (13, "コーヒー", "", "koohii", "cà phê", "cup of coffee", "これは コーヒーですか。…はい、そうです。", "Đây là cà phê à? …Vâng, đúng thế."),
    (13, "テレホンカード", "", "terehonkaado", "thẻ điện thoại", "telephone card Japan", "これは テレホンカードです。", "Đây là thẻ điện thoại."),
    (13, "テープ", "", "teepu", "băng (cát-xét)", "cassette tape", "それは にほんごの テープですか。", "Đó là băng tiếng Nhật à?"),
    (13, "テープレコーダー", "", "teepurekoodaa", "máy ghi âm", "tape recorder", "あれは だれの テープレコーダーですか。", "Kia là máy ghi âm của ai?"),
    (13, "じどうしゃ", "自動車", "jidousha", "ô tô (cách nói trang trọng)", "automobile Japan Toyota", "これは にほんの じどうしゃです。", "Đây là ô tô của Nhật."),
    # ---- 0014 · Minna 3
    (14, "じむしょ", "事務所", "jimusho", "văn phòng", "office interior desks", "ここは じむしょです。", "Đây là văn phòng."),
    (14, "かいぎしつ", "会議室", "kaigishitsu", "phòng họp", "conference room", "かいぎしつは どこですか。…あそこです。", "Phòng họp ở đâu? …Ở kia."),
    (14, "ロビー", "", "robii", "sảnh", "hotel lobby", "ロビーは あちらです。", "Sảnh ở phía kia."),
    (14, "へや", "部屋", "heya", "căn phòng", "room interior", "ここは ナムさんの へやです。", "Đây là phòng của anh Nam."),
    (14, "エレベーター", "", "erebeetaa", "thang máy", "elevator", "エレベーターは そこです。", "Thang máy ở chỗ đó."),
    (14, "ネクタイ", "", "nekutai", "cà vạt", "necktie", "この ネクタイは いくらですか。", "Chiếc cà vạt này bao nhiêu tiền?"),
    (14, "たばこ", "", "tabako", "thuốc lá", "cigarette pack", "この たばこは ごひゃくえんです。", "Gói thuốc lá này 500 yên."),
    # ---- 0015 · Minna 4
    (15, "ニューヨーク", "", "nyuuyooku", "New York", "New York skyline Manhattan", "ニューヨークは いま ごぜん ごじです。", "Bây giờ ở New York là 5 giờ sáng."),
    (15, "ロンドン", "", "rondon", "Luân Đôn", "London Tower Bridge", "ロンドンは いま ごご くじです。", "Bây giờ ở Luân Đôn là 9 giờ tối."),
    (15, "ペキン", "北京", "pekin", "Bắc Kinh", "Beijing Forbidden City", "ペキンの ぎんこうは くじから ごじまでです。", "Ngân hàng ở Bắc Kinh làm từ 9 giờ đến 5 giờ."),
    (15, "ロサンゼルス", "", "rosanzerusu", "Los Angeles", "Los Angeles downtown skyline", "ロサンゼルスは いま ごぜん じゅうじです。", "Bây giờ ở Los Angeles là 10 giờ sáng."),
    # ---- 0016 · Minna 5
    (16, "えき", "駅", "eki", "nhà ga", "Japanese train station platform", "あした えきへ いきます。", "Ngày mai tôi đi ra ga."),
    (16, "おおさかじょう", "大阪城", "oosakajou", "lâu đài Osaka", "Osaka Castle", "おおさかじょうへ ともだちと いきます。", "Tôi đi lâu đài Osaka cùng bạn."),
    (16, "こうしえん", "甲子園", "koushien", "sân vận động Koshien", "Koshien Stadium", "こうしえんへ でんしゃで いきます。", "Tôi đi Koshien bằng tàu điện."),
]

# Từ đã có nhưng nằm sai bài → chuyển về đúng bài, kèm câu ví dụ hợp ngữ pháp bài đó.
VOCAB_MOVE = {
    "v-kagi": (13, "これは わたしの かぎです。", "Đây là chìa khoá của tôi."),
    "v-kasa": (13, "それは だれの かさですか。", "Đó là ô của ai vậy?"),
    "v-terebi": (13, "それは わたしの テレビです。", "Đó là tivi của tôi."),
}
