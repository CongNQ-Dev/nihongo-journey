"""Dữ liệu nguồn cho các bài kana (0002–0011). Sửa ở đây rồi chạy tools/build.py.

CARDS: (lesson, glyph, sound, vn_note, word, romaji, meaning, commons_query)
Ảnh của thẻ được chọn bởi tools/fetch_images.py (lưu ở tools/images.json).
"""

PH = "https://en.wikipedia.org/wiki/Japanese_phonology"
HIRA = "https://en.wikipedia.org/wiki/Hiragana"
KATA = "https://en.wikipedia.org/wiki/Katakana"
TOFU_H = "https://www.tofugu.com/japanese/learn-hiragana/"
TOFU_K = "https://www.tofugu.com/japanese/learn-katakana/"

CARDS = [
    # ---- 0002 か行・さ行
    (2, "か", "ka", "giữa “ca” và “kha”", "かさ", "kasa", "cái ô (dù)", "umbrella rain"),
    (2, "き", "ki", "như “ki”", "きつね", "kitsune", "con cáo", "red fox"),
    (2, "く", "ku", "“kư”, môi không tròn", "くるま", "kuruma", "ô tô", "car parked street"),
    (2, "け", "ke", "như “kê”", "けしごむ", "keshigomu", "cục tẩy", "eraser"),
    (2, "こ", "ko", "như “cô”", "こい", "koi", "cá chép koi", "koi fish pond"),
    (2, "さ", "sa", "như “xa”", "さくら", "sakura", "hoa anh đào", "cherry blossom"),
    (2, "し", "shi", "“shi” — không phải “si”", "しか", "shika", "con hươu", "sika deer Nara"),
    (2, "す", "su", "“xư”, môi không tròn", "すし", "sushi", "sushi", "sushi nigiri"),
    (2, "せ", "se", "như “xê”", "せみ", "semi", "con ve sầu", "cicada"),
    (2, "そ", "so", "như “xô”", "そら", "sora", "bầu trời", "blue sky clouds"),
    # ---- 0003 た行・な行
    (3, "た", "ta", "giữa “ta” và “tha”", "たまご", "tamago", "quả trứng", "eggs"),
    (3, "ち", "chi", "“chi” — không phải “ti”", "ちず", "chizu", "bản đồ", "paper map"),
    (3, "つ", "tsu", "“ts” + “ư” — âm mới", "つき", "tsuki", "mặt trăng", "full moon"),
    (3, "て", "te", "giữa “tê” và “thê”", "てら", "tera", "ngôi chùa", "Buddhist temple Kyoto"),
    (3, "と", "to", "giữa “tô” và “thô”", "とり", "tori", "con chim", "bird on branch"),
    (3, "な", "na", "như “na”", "なす", "nasu", "cà tím", "eggplant"),
    (3, "に", "ni", "như “ni”", "にわとり", "niwatori", "con gà", "hen chicken"),
    (3, "ぬ", "nu", "“nư”, môi không tròn", "ぬいぐるみ", "nuigurumi", "thú nhồi bông", "teddy bear"),
    (3, "ね", "ne", "như “nê”", "ねこ", "neko", "con mèo", "cat portrait"),
    (3, "の", "no", "như “nô”", "のれん", "noren", "rèm vải trước cửa tiệm", "noren curtain shop"),
    # ---- 0004 は行・ま行
    (4, "は", "ha", "như “ha”; làm trợ từ thì đọc “wa”", "はな", "hana", "bông hoa", "flowers bouquet"),
    (4, "ひ", "hi", "như “hi”", "ひこうき", "hikouki", "máy bay", "airliner sky"),
    (4, "ふ", "fu", "thổi hơi qua hai môi, răng không chạm môi", "ふじさん", "fujisan", "núi Phú Sĩ", "Mount Fuji"),
    (4, "へ", "he", "như “hê”; làm trợ từ thì đọc “e”", "へび", "hebi", "con rắn", "snake"),
    (4, "ほ", "ho", "như “hô”", "ほし", "hoshi", "ngôi sao", "starry night sky"),
    (4, "ま", "ma", "như “ma”", "まつり", "matsuri", "lễ hội", "matsuri festival Japan"),
    (4, "み", "mi", "như “mi”", "みかん", "mikan", "quả quýt", "mandarin oranges"),
    (4, "む", "mu", "“mư”, môi không tròn", "むし", "mushi", "côn trùng", "beetle"),
    (4, "め", "me", "như “mê”", "めがね", "megane", "kính mắt", "eyeglasses"),
    (4, "も", "mo", "như “mô”", "もも", "momo", "quả đào", "peaches"),
    # ---- 0005 や行・ら行・わ・を・ん
    (5, "や", "ya", "“ia” đọc nhanh thành một tiếng", "やま", "yama", "ngọn núi", "mountain landscape Japan"),
    (5, "ゆ", "yu", "“iư” đọc nhanh", "ゆき", "yuki", "tuyết", "snow landscape"),
    (5, "よ", "yo", "“iô” đọc nhanh", "よる", "yoru", "ban đêm", "Tokyo at night"),
    (5, "ら", "ra", "đầu lưỡi vỗ nhẹ một lần: giữa “r”, “l”, “đ”", "らくだ", "rakuda", "con lạc đà", "camel"),
    (5, "り", "ri", "lưỡi vỗ nhẹ + “i”", "りんご", "ringo", "quả táo", "red apples"),
    (5, "る", "ru", "lưỡi vỗ nhẹ + “ư”", "さる", "saru", "con khỉ", "Japanese macaque"),
    (5, "れ", "re", "lưỡi vỗ nhẹ + “ê”", "れいぞうこ", "reizouko", "tủ lạnh", "refrigerator"),
    (5, "ろ", "ro", "lưỡi vỗ nhẹ + “ô”", "ろうそく", "rousoku", "cây nến", "candles"),
    (5, "わ", "wa", "như “oa”", "わに", "wani", "con cá sấu", "crocodile"),
    (5, "を", "o", "đọc như お; chỉ dùng làm trợ từ", "てがみを かく", "tegami o kaku", "viết thư", "handwritten letter fountain pen"),
    (5, "ん", "n", "âm mũi, đứng riêng một nhịp", "ほん", "hon", "quyển sách", "books"),
    # ---- 0006 ゛ và ゜
    (6, "ぎ", "gi", "か行 + ゛ → が行", "かぎ", "kagi", "chìa khoá", "keys"),
    (6, "ぞ", "zo", "さ行 + ゛ → ざ行", "ぞう", "zou", "con voi", "elephant"),
    (6, "だ", "da", "た行 + ゛ → だ行", "だいこん", "daikon", "củ cải trắng", "daikon radish"),
    (6, "ば", "ba", "は行 + ゛ → ば行", "ばら", "bara", "hoa hồng", "red rose"),
    (6, "ぶ", "bu", "は行 + ゛ → ば行", "ぶどう", "budou", "quả nho", "grapes"),
    (6, "ぷ", "pu", "は行 + ゜ → ぱ行", "てんぷら", "tenpura", "tempura", "tempura"),
    # ---- 0007 âm ghép, っ, trường âm
    (7, "きゅ", "kyu", "き + ゅ nhỏ = một nhịp", "きゅうり", "kyuuri", "dưa chuột", "cucumbers"),
    (7, "しゃ", "sha", "し + ゃ nhỏ = một nhịp", "じてんしゃ", "jitensha", "xe đạp", "bicycle"),
    (7, "ちゃ", "cha", "ち + ゃ nhỏ = một nhịp", "おちゃ", "ocha", "trà", "Japanese green tea cup"),
    (7, "ぎゅ", "gyu", "ぎ + ゅ nhỏ = một nhịp", "ぎゅうどん", "gyuudon", "cơm thịt bò", "gyudon beef bowl"),
    (7, "っ", "(ngắt)", "dừng một nhịp, gấp đôi phụ âm sau", "きって", "kitte", "con tem", "postage stamps"),
    (7, "とう", "tō", "お段 + う = “ô” kéo dài hai nhịp", "とうふ", "toufu", "đậu phụ", "tofu"),
    # ---- 0008 katakana ア〜ソ
    (8, "ア", "a", "= あ", "アイス", "aisu", "kem", "ice cream cone"),
    (8, "イ", "i", "= い", "イルカ", "iruka", "cá heo", "dolphin"),
    (8, "ウ", "u", "= う", "ウサギ", "usagi", "con thỏ", "rabbit"),
    (8, "エ", "e", "= え", "エレベーター", "erebeetaa", "thang máy", "elevator"),
    (8, "オ", "o", "= お", "オレンジ", "orenji", "quả cam", "oranges"),
    (8, "カ", "ka", "= か (gần giống hệt)", "カメラ", "kamera", "máy ảnh", "camera"),
    (8, "キ", "ki", "= き", "キウイ", "kiui", "quả kiwi", "kiwifruit"),
    (8, "ク", "ku", "= く", "クッキー", "kukkii", "bánh quy", "cookies"),
    (8, "ケ", "ke", "= け", "ケーキ", "keeki", "bánh kem", "strawberry shortcake"),
    (8, "コ", "ko", "= こ", "コーヒー", "koohii", "cà phê", "coffee cup"),
    (8, "サ", "sa", "= さ", "サラダ", "sarada", "rau trộn", "salad"),
    (8, "シ", "shi", "= し; dễ lẫn với ツ", "シャツ", "shatsu", "áo sơ mi", "shirts"),
    (8, "ス", "su", "= す", "スプーン", "supuun", "cái thìa", "spoons"),
    (8, "セ", "se", "= せ (gần giống hệt)", "セーター", "seetaa", "áo len", "knitted sweater"),
    (8, "ソ", "so", "= そ; dễ lẫn với ン", "ソファー", "sofaa", "ghế sofa", "sofa"),
    # ---- 0009 katakana タ〜ホ
    (9, "タ", "ta", "= た", "タクシー", "takushii", "xe taxi", "taxi Tokyo"),
    (9, "チ", "chi", "= ち", "チーズ", "chiizu", "phô mai", "cheese"),
    (9, "ツ", "tsu", "= つ; dễ lẫn với シ", "ツリー", "tsurii", "cây thông Noel", "Christmas tree"),
    (9, "テ", "te", "= て", "テレビ", "terebi", "tivi", "television set"),
    (9, "ト", "to", "= と", "トマト", "tomato", "cà chua", "tomatoes"),
    (9, "ナ", "na", "= な", "ナイフ", "naifu", "con dao", "knife"),
    (9, "ニ", "ni", "= に", "テニス", "tenisu", "quần vợt", "tennis"),
    (9, "ヌ", "nu", "= ぬ; dễ lẫn với ス", "ヌードル", "nuudoru", "mì (noodle)", "noodles bowl"),
    (9, "ネ", "ne", "= ね", "ネクタイ", "nekutai", "cà vạt", "necktie"),
    (9, "ノ", "no", "= の", "ノート", "nooto", "quyển vở", "notebook"),
    (9, "ハ", "ha", "= は", "ハンバーガー", "hanbaagaa", "bánh hamburger", "hamburger"),
    (9, "ヒ", "hi", "= ひ", "ヒマワリ", "himawari", "hoa hướng dương", "sunflowers"),
    (9, "フ", "fu", "= ふ", "フルーツ", "furuutsu", "trái cây", "fruit"),
    (9, "ヘ", "he", "= へ (gần giống hệt)", "ヘリコプター", "herikoputaa", "trực thăng", "helicopter"),
    (9, "ホ", "ho", "= ほ", "ホテル", "hoteru", "khách sạn", "hotel"),
    # ---- 0010 katakana マ〜ン
    (10, "マ", "ma", "= ま; dễ lẫn với ア", "マスク", "masuku", "khẩu trang", "surgical mask"),
    (10, "ミ", "mi", "= み", "ミルク", "miruku", "sữa", "milk bottle"),
    (10, "ム", "mu", "= む", "ハム", "hamu", "giăm bông", "ham slices"),
    (10, "メ", "me", "= め; dễ lẫn với ナ", "メロン", "meron", "dưa lưới", "melon"),
    (10, "モ", "mo", "= も", "レモン", "remon", "quả chanh vàng", "lemons"),
    (10, "ヤ", "ya", "= や", "タイヤ", "taiya", "lốp xe", "tire"),
    (10, "ユ", "yu", "= ゆ; dễ lẫn với コ", "ユリ", "yuri", "hoa loa kèn", "lily flower"),
    (10, "ヨ", "yo", "= よ", "ヨット", "yotto", "thuyền buồm", "sailboat"),
    (10, "ラ", "ra", "= ら", "ラーメン", "raamen", "mì ramen", "ramen"),
    (10, "リ", "ri", "= り", "リス", "risu", "con sóc", "squirrel"),
    (10, "ル", "ru", "= る; dễ lẫn với レ", "ボール", "booru", "quả bóng", "soccer ball"),
    (10, "レ", "re", "= れ", "レストラン", "resutoran", "nhà hàng", "restaurant interior"),
    (10, "ロ", "ro", "= ろ", "ロボット", "robotto", "người máy", "robot"),
    (10, "ワ", "wa", "= わ; dễ lẫn với ウ, フ", "ワイン", "wain", "rượu vang", "wine glass"),
    (10, "ン", "n", "= ん; dễ lẫn với ソ", "パン", "pan", "bánh mì", "bread loaves"),
    # ---- 0011 katakana ゛゜, ッ, ャュョ, âm ngoại lai
    (11, "ギ", "gi", "キ + ゛", "ギター", "gitaa", "đàn ghi-ta", "acoustic guitar"),
    (11, "バ", "ba", "ハ + ゛", "バス", "basu", "xe buýt", "bus Japan"),
    (11, "ピ", "pi", "ヒ + ゜", "ピアノ", "piano", "đàn piano", "grand piano"),
    (11, "ジュ", "ju", "ジ + ュ nhỏ = một nhịp", "ジュース", "juusu", "nước ép", "orange juice"),
    (11, "ッ", "(ngắt)", "giống っ: dừng một nhịp", "ベッド", "beddo", "cái giường", "bedroom bed"),
    (11, "ティ", "ti", "テ + ィ nhỏ — âm chỉ có ở từ ngoại lai", "パーティー", "paatii", "bữa tiệc", "party balloons"),
    (11, "フェ", "fe", "フ + ェ nhỏ — âm ngoại lai", "カフェ", "kafe", "quán cà phê", "cafe interior"),
    (11, "チョ", "cho", "チ + ョ nhỏ = một nhịp", "チョコレート", "chokoreeto", "sô-cô-la", "chocolate"),
]

# Chữ không có thẻ nhưng vẫn nằm trong bảng của bài.
EXTRA_ROWS = {10: [("ヲ", "o", "= を; gần như không dùng trong văn bản hiện đại")]}

LESSONS = {
 2: dict(slug="0002-hiragana-ka-sa", title="Hàng か và hàng さ", jp="かきくけこ さしすせそ",
   lede="Mười chữ mới, và lần đầu tiên bạn đọc được những từ thật như すし, かさ, おかし.",
   win="Đọc, nghe và viết tay được 10 chữ hàng か và さ; đọc được 12 từ chỉ gồm các chữ đã học.",
   intro=f"""<p>Từ đây trở đi, mỗi hàng trong bảng hiragana là <strong>một phụ âm + năm nguyên âm theo đúng thứ tự a – i – u – e – o</strong>. Thuộc あいうえお là đã thuộc thứ tự của mọi hàng.<sup class="cite"><a href="{HIRA}">[wiki]</a></sup></p>""",
   notes=f"""<ul>
<li><strong>か行 = ka ki ku ke ko.</strong> Phụ âm “k” ở đầu từ có bật hơi nhẹ, nghe giữa “c” và “kh” tiếng Việt.<sup class="cite"><a href="{PH}">[phonology]</a></sup> Bấm nghe để so — tai bạn là chuẩn.</li>
<li><strong>さ行 = sa <em>shi</em> su se so.</strong> し là ngoại lệ đầu tiên: đọc “shi”, không phải “si”. Cố ý tròn môi nhẹ và đưa lưỡi lùi về sau như khi nói “suỵt”.</li>
<li><strong>く và す</strong> giữ nguyên âm “ư” của う: môi không chu ra.</li>
</ul>
<h3>Chữ dễ lẫn</h3>
<ul>
<li><span class="jp">き</span> có <em>hai</em> gạch ngang, <span class="jp">さ</span> chỉ có <em>một</em>.</li>
<li><span class="jp">こ</span> là hai nét <em>ngang</em>; <span class="jp">い</span> là hai nét <em>dọc</em>.</li>
<li><span class="jp">く</span> giống dấu “nhỏ hơn” &lt; — một nét duy nhất.</li>
</ul>""",
   read=[("あき","aki","mùa thu"),("いけ","ike","cái ao"),("うし","ushi","con bò"),("かお","kao","khuôn mặt"),("かさ","kasa","cái ô"),("すし","sushi","sushi"),("せかい","sekai","thế giới"),("あさ","asa","buổi sáng"),("いす","isu","cái ghế"),("おかし","okashi","bánh kẹo"),("しお","shio","muối"),("えき","eki","nhà ga")],
   mc=[("Chữ nào đọc là “shi”?", ["さ","し","き","す"], 2, "し — ngoại lệ của hàng さ.", True),
       ("Từ <span class=\"jp\">せかい</span> đọc là gì?", ["sekai","sakai","sekei","sikai"], 1, "せ = se, か = ka, い = i.", False)],
   recall=["Viết ra giấy cả hàng か và hàng さ theo đúng thứ tự.", "Viết bằng hiragana: “sushi”, “cái ô”, “bánh kẹo”.", "Chữ nào trong hàng さ không đọc theo quy luật? Nó đọc thế nào?"],
   primary=("Tofugu — Learn Hiragana: The Ultimate Guide", TOFU_H, "Đọc phần か行 và さ行, nghe giọng người thật.")),
 3: dict(slug="0003-hiragana-ta-na", title="Hàng た và hàng な", jp="たちつてと なにぬねの",
   lede="Hai ngoại lệ mới — ち và つ — và một âm tiếng Việt không có.",
   win="Đọc, nghe và viết tay được 10 chữ hàng た và な; phát âm được つ (tsu).",
   intro="<p>Hàng た có hai chữ không theo quy luật romaji; hàng な thì hoàn toàn đều.</p>",
   notes=f"""<ul>
<li><strong>た行 = ta <em>chi</em> <em>tsu</em> te to.</strong> ち đọc “chi”, つ đọc “tsu”.<sup class="cite"><a href="{PH}">[phonology]</a></sup></li>
<li><strong>Cách nói つ:</strong> đặt lưỡi như khi nói “t”, rồi nhả ra thành tiếng xì “s”, cuối cùng là “ư”. Tiếng Việt không có âm “ts” — nói chậm “t-s-ư” vài lần rồi nhanh dần thành một tiếng.</li>
<li><strong>な行 = na ni nu ne no</strong>, đều như tiếng Việt.</li>
</ul>
<h3>Chữ dễ lẫn</h3>
<ul>
<li><span class="jp">ぬ</span> có <em>vòng nhỏ</em> ở đuôi; <span class="jp">め</span> thì không.</li>
<li><span class="jp">た</span> và <span class="jp">な</span>: cùng bắt đầu bằng một chữ thập; phần phải của な có vòng xoắn.</li>
<li><span class="jp">ね</span> có vòng ở đuôi — bài 0005 sẽ gặp hai “anh em” れ và わ.</li>
</ul>""",
   read=[("たこ","tako","bạch tuộc"),("くつ","kutsu","đôi giày"),("ちかてつ","chikatetsu","tàu điện ngầm"),("いぬ","inu","con chó"),("ねこ","neko","con mèo"),("なつ","natsu","mùa hè"),("あなた","anata","bạn (ngôi thứ hai)"),("にく","niku","thịt"),("こたえ","kotae","câu trả lời"),("した","shita","bên dưới"),("きた","kita","phía bắc"),("おとこ","otoko","đàn ông")],
   mc=[("Chữ nào đọc là “tsu”?", ["ち","つ","う","し"], 2, "つ = tsu.", True),
       ("Chữ nào đọc là “nu”?", ["ぬ","め","ね","の"], 1, "ぬ có vòng nhỏ ở đuôi.", True)],
   recall=["Viết hàng た và hàng な theo thứ tự.", "Viết bằng hiragana: “con mèo”, “mùa hè”, “tàu điện ngầm”.", "Nói to つ, ち, す ba lần — có phân biệt được không?"],
   primary=("Tofugu — Learn Hiragana: The Ultimate Guide", TOFU_H, "Đọc phần た行 và な行.")),
 4: dict(slug="0004-hiragana-ha-ma", title="Hàng は và hàng ま", jp="はひふへほ まみむめも",
   lede="ふ là âm “f” thổi bằng môi, và は có lúc đọc là “wa”.",
   win="Đọc, nghe và viết tay được 10 chữ hàng は và ま; biết khi nào は đọc “wa”, へ đọc “e”.",
   intro="<p>Sau bài này bạn đã có 30 chữ — hơn nửa bảng.</p>",
   notes=f"""<ul>
<li><strong>は行 = ha hi <em>fu</em> he ho.</strong> ふ không giống “ph” tiếng Việt: răng <em>không</em> chạm môi dưới, chỉ thổi hơi qua khe hai môi như thổi nến nhẹ.<sup class="cite"><a href="{PH}">[phonology]</a></sup></li>
<li><strong>Trợ từ:</strong> khi は làm trợ từ chủ đề thì đọc “wa” — <span class="jp">わたしは</span> = watashi <em>wa</em>. Khi へ chỉ hướng thì đọc “e”.<sup class="cite"><a href="{HIRA}">[wiki]</a></sup> Bạn sẽ gặp わたしは ngay ở Minna bài 1.</li>
<li><strong>ま行 = ma mi mu me mo</strong>, đều.</li>
</ul>
<h3>Chữ dễ lẫn</h3>
<ul>
<li><span class="jp">は</span> → thêm gạch ngang trên = <span class="jp">ほ</span>. Bỏ nét dọc bên trái của ほ = gần giống <span class="jp">ま</span>.</li>
<li><span class="jp">め</span> (không vòng) / <span class="jp">ぬ</span> (có vòng) — đã gặp ở bài 0003.</li>
<li><span class="jp">も</span> giống lưỡi câu có hai gạch ngang.</li>
</ul>""",
   read=[("はな","hana","bông hoa"),("ひと","hito","người"),("ふね","fune","con thuyền"),("ほし","hoshi","ngôi sao"),("はは","haha","mẹ (của mình)"),("ひま","hima","rảnh rỗi"),("みみ","mimi","cái tai"),("むすめ","musume","con gái"),("もの","mono","đồ vật"),("あたま","atama","cái đầu"),("さかな","sakana","con cá"),("みせ","mise","cửa hàng"),("へた","heta","kém, dở")],
   mc=[("Trong <span class=\"jp\">わたしは</span>, chữ は đọc là gì?", ["ha","wa","ba","he"], 2, "は làm trợ từ chủ đề thì đọc “wa”.", False),
       ("Chữ nào đọc là “ho”?", ["ま","は","も","ほ"], 4, "ほ = は + một gạch ngang trên.", True)],
   recall=["Viết hàng は và hàng ま theo thứ tự.", "Viết bằng hiragana: “bông hoa”, “con cá”, “núi Phú Sĩ”.", "Khi nào は đọc là “wa”? Khi nào へ đọc là “e”?"],
   primary=("Tofugu — Learn Hiragana: The Ultimate Guide", TOFU_H, "Đọc phần は行 và ま行.")),
 5: dict(slug="0005-hiragana-ya-ra-wa-n", title="Hàng や, ら, わ và ん", jp="やゆよ らりるれろ わをん",
   lede="Mười một chữ cuối cùng. Xong bài này là xong 46 chữ hiragana cơ bản.",
   win="Đọc, nghe và viết tay được cả 46 chữ hiragana cơ bản; đọc được cụm ほんを よむ.",
   intro="<p>Hàng や chỉ còn 3 chữ, hàng わ chỉ còn わ và を — các ô khác đã bị bỏ khỏi chữ viết hiện đại.<sup class=\"cite\"><a href=\"" + HIRA + "\">[wiki]</a></sup></p>",
   notes=f"""<ul>
<li><strong>ら行 = ra ri ru re ro.</strong> “r” tiếng Nhật là âm vỗ: đầu lưỡi chạm nhẹ lợi trên đúng <em>một</em> lần rồi rời ra — nghe giữa “r”, “l” và “đ”. Không rung lưỡi như “r” tiếng Việt miền Nam.<sup class="cite"><a href="{PH}">[phonology]</a></sup></li>
<li><strong>を</strong> đọc “o” giống hệt お, nhưng chỉ dùng làm trợ từ đánh dấu tân ngữ: <span class="jp">ほんを よむ</span> = đọc sách.</li>
<li><strong>ん</strong> không bao giờ đứng đầu từ, và chiếm trọn <em>một nhịp</em>: <span class="jp">ほん</span> = ho-n (2 nhịp), <span class="jp">にほん</span> = ni-ho-n (3 nhịp). Nói đều từng nhịp.</li>
</ul>
<h3>Chữ dễ lẫn</h3>
<ul>
<li><span class="jp">る</span> có vòng ở đuôi; <span class="jp">ろ</span> thì không.</li>
<li><span class="jp">ね・れ・わ</span>: cùng thân trái, khác đuôi — ね cuộn vòng, れ hất ra ngoài, わ cong tròn vào trong.</li>
<li><span class="jp">ゆ</span> là một vòng lớn có nét dọc cắt giữa.</li>
</ul>""",
   read=[("やま","yama","núi"),("ゆき","yuki","tuyết"),("よる","yoru","ban đêm"),("さくら","sakura","hoa anh đào"),("くすり","kusuri","thuốc"),("くるま","kuruma","ô tô"),("れきし","rekishi","lịch sử"),("ろく","roku","số sáu"),("わたし","watashi","tôi"),("にほん","nihon","Nhật Bản"),("ほん","hon","quyển sách"),("みかん","mikan","quả quýt"),("ほんを よむ","hon o yomu","đọc sách")],
   mc=[("Chữ nào đọc là “ru”?", ["ろ","る","ら","れ"], 2, "る có vòng ở đuôi.", True),
       ("<span class=\"jp\">にほん</span> có mấy nhịp?", ["3 nhịp","2 nhịp","4 nhịp","1 nhịp"], 1, "に・ほ・ん — ん là một nhịp riêng.", False)],
   recall=["Viết ra giấy toàn bộ 46 chữ hiragana theo bảng — không nhìn.", "Viết bằng hiragana: “tôi”, “Nhật Bản”, “đọc sách”.", "を đọc thế nào và dùng khi nào?"],
   primary=("Tofugu — Learn Hiragana: The Ultimate Guide", TOFU_H, "Đọc phần や, ら, わ, ん và làm bài tự kiểm tra cuối.")),
 6: dict(slug="0006-hiragana-dakuten", title="Hai chấm ゛ và vòng tròn ゜", jp="がざだばぱ",
   lede="Không cần chữ mới: hai dấu nhỏ biến 20 chữ đã học thành 25 âm mới.",
   win="Đọc và viết được toàn bộ が・ざ・だ・ば・ぱ行; nghe phân biệt được か/が, た/だ, は/ば/ぱ.",
   intro=f"""<p><strong>゛ (dakuten)</strong> làm phụ âm “rung cổ”: k→g, s→z, t→d, h→b. <strong>゜ (handakuten)</strong> chỉ đi với hàng は: h→p.<sup class="cite"><a href="https://en.wikipedia.org/wiki/Dakuten_and_handakuten">[wiki]</a></sup> Đặt ngón tay lên cổ, nói “ka” rồi “ga”: âm sau rung.</p>""",
   table="DAKUTEN",
   notes=f"""<ul>
<li><strong>じ và ぢ</strong> đều đọc “ji”; <strong>ず và づ</strong> đều đọc “zu”. Hầu như luôn viết じ, ず — ぢ, づ chỉ gặp trong vài từ.<sup class="cite"><a href="https://en.wikipedia.org/wiki/Dakuten_and_handakuten">[wiki]</a></sup></li>
<li><strong>ざ行</strong> không giống “d” giọng Nam hay “r”: đầu lưỡi gần lợi trên, có tiếng “z” rung. Nghe kỹ trước khi nhại.</li>
<li><strong>ぱ行</strong> có “p” bật hơi nhẹ — tiếng Việt chỉ có “p” đầu từ trong từ mượn như “pin”.</li>
</ul>""",
   read=[("かぎ","kagi","chìa khoá"),("ぞう","zou","con voi"),("だいがく","daigaku","đại học"),("ばら","bara","hoa hồng"),("ぶどう","budou","quả nho"),("てんぷら","tenpura","tempura"),("がくせい","gakusei","sinh viên"),("ごはん","gohan","cơm"),("でんわ","denwa","điện thoại"),("みず","mizu","nước"),("かぜ","kaze","gió"),("じかん","jikan","thời gian"),("えんぴつ","enpitsu","bút chì"),("かばん","kaban","cái cặp")],
   mc=[("Thêm ゛ vào た được chữ gì?", ["ざ","ば","だ","ぱ"], 3, "た → だ (t → d).", True),
       ("<span class=\"jp\">ぱ</span> đọc là gì?", ["ba","pa","ha","wa"], 2, "゜ biến h thành p.", False)],
   listen_new="か が さ ざ た だ は ば ぱ",
   writers="がざだばぱ",
   recall=["Viết cả năm hàng が ざ だ ば ぱ.", "Viết bằng hiragana: “sinh viên”, “điện thoại”, “cơm”.", "Hai cặp chữ nào đọc giống hệt nhau?"],
   primary=("Tofugu — Learn Hiragana: The Ultimate Guide", TOFU_H, "Đọc phần dakuten và handakuten.")),
 7: dict(slug="0007-hiragana-yoon-sokuon-long", title="Âm ghép, っ nhỏ và trường âm", jp="きゃ っ ー",
   lede="Ba quy tắc cuối của hiragana — và từ nay độ dài âm làm đổi nghĩa từ.",
   win="Đọc đúng nhịp những từ như とうきょう, きって, びょういん; tự giới thiệu một câu bằng tiếng Nhật.",
   intro="<p>Tiếng Nhật đếm âm theo <strong>nhịp</strong> (mora): mỗi chữ hiragana cỡ thường là một nhịp, nói dài đều nhau. Ba quy tắc dưới đây đều là chuyện “mấy nhịp”.</p>",
   table="YOON",
   notes=f"""<ul>
<li><strong>Âm ghép (yōon):</strong> chữ hàng い (き, し, ち, に, ひ, み, り, ぎ, じ, び, ぴ) + ゃ ゅ ょ <em>viết nhỏ</em> = <em>một</em> nhịp: き+ゃ = kya. Viết cỡ thường きや = ki-ya, hai nhịp.<sup class="cite"><a href="https://en.wikipedia.org/wiki/Y%C5%8Don">[wiki]</a></sup></li>
<li><strong>っ nhỏ (sokuon):</strong> dừng lại một nhịp rồi bật phụ âm sau: きって = ki-(dừng)-te, 3 nhịp; romaji viết gấp đôi phụ âm: kitte.<sup class="cite"><a href="https://en.wikipedia.org/wiki/Sokuon">[wiki]</a></sup></li>
<li><strong>Trường âm:</strong> nguyên âm kéo dài thành 2 nhịp. Cách viết: cột あ + あ (おかあさん), cột い + い (おにいさん), cột う + う (くうき), cột え + い (せんせい — thường đọc “sensē”), cột お + う (とうきょう; một số từ dùng お: おおきい).<sup class="cite"><a href="{HIRA}">[wiki]</a></sup></li>
</ul>
<h3>Ngắn hay dài làm đổi nghĩa</h3>
<div class="table-wrap"><table>
<tr><th>Từ</th><th>Nghĩa</th><th>Nghe</th></tr>
<tr><td><span class="jp">びょういん</span></td><td>bệnh viện</td><td><button class="say" data-say="びょういん">byōin</button></td></tr>
<tr><td><span class="jp">びよういん</span></td><td>tiệm làm tóc</td><td><button class="say" data-say="びよういん">biyōin</button></td></tr>
<tr><td><span class="jp">おばさん</span></td><td>cô, dì</td><td><button class="say" data-say="おばさん">obasan</button></td></tr>
<tr><td><span class="jp">おばあさん</span></td><td>bà</td><td><button class="say" data-say="おばあさん">obāsan</button></td></tr>
<tr><td><span class="jp">きて</span></td><td>hãy đến</td><td><button class="say" data-say="きて">kite</button></td></tr>
<tr><td><span class="jp">きって</span></td><td>con tem</td><td><button class="say" data-say="きって">kitte</button></td></tr>
</table></div>
<h3>Nói: câu tự giới thiệu đầu tiên</h3>
<p class="jp" style="font-size:1.5rem;line-height:1.7">はじめまして。わたしは ＿＿＿ です。どうぞ よろしく。</p>
<p>“Rất vui được gặp. Tôi là ＿＿. Rất mong được giúp đỡ.” Điền tên bạn, nói to 5 lần cho trôi. Cả câu chỉ dùng chữ bạn đã học. <button class="say" data-say="はじめまして。わたしは たなかです。どうぞ よろしく。">nghe mẫu</button> (mẫu dùng tên たなか — bạn thay bằng tên mình).</p>""",
   read=[("きゅうり","kyuuri","dưa chuột"),("じてんしゃ","jitensha","xe đạp"),("おちゃ","ocha","trà"),("ぎゅうにゅう","gyuunyuu","sữa bò"),("きって","kitte","con tem"),("がっこう","gakkou","trường học"),("とうきょう","toukyou","Tokyo"),("おかあさん","okaasan","mẹ (người khác)"),("くうき","kuuki","không khí"),("せんせい","sensei","giáo viên"),("おおきい","ookii","to, lớn"),("きょう","kyou","hôm nay"),("しゃしん","shashin","bức ảnh"),("びょういん","byouin","bệnh viện"),("びよういん","biyouin","tiệm làm tóc")],
   read_note="Gõ trường âm bằng cách lặp nguyên âm như khi gõ bàn phím Nhật: とうきょう = toukyou, おかあさん = okaasan.",
   mc=[("<span class=\"jp\">きって</span> có mấy nhịp?", ["2 nhịp","4 nhịp","3 nhịp","1 nhịp"], 3, "き・っ・て — っ cũng là một nhịp.", False),
       ("<span class=\"jp\">びょういん</span> nghĩa là gì?", ["tiệm tóc","nhà ga","bệnh viện","trường học"], 3, "びょういん (byō-in) = bệnh viện; びよういん = tiệm làm tóc.", False)],
   listen_new="びょういん びよういん おばさん おばあさん きて きって",
   writers="ゃゅょっ",
   recall=["Viết ba từ: “Tokyo”, “con tem”, “giáo viên”.", "Giải thích khác nhau giữa きや và きゃ, きて và きって.", "Nói to câu tự giới thiệu với tên của bạn."],
   primary=("Tofugu — Learn Hiragana: The Ultimate Guide", TOFU_H, "Đọc phần chữ nhỏ ゃゅょ, っ và trường âm.")),
 8: dict(slug="0008-katakana-a-so", title="Katakana: ア đến ソ", jp="アイウエオ カキクケコ サシスセソ",
   lede="Cùng âm thanh bạn đã biết, nét chữ khác. Katakana đi nhanh hơn nhiều.",
   win="Đọc và viết tay được 15 chữ katakana đầu tiên; đọc được từ ngoại lai như ケーキ, アイス.",
   intro=f"""<p>Katakana ghi <strong>đúng những âm của hiragana</strong>, nhưng dùng cho từ ngoại lai (コーヒー, カメラ), tên người và địa danh nước ngoài — kể cả tên bạn — tên động thực vật trong văn bản khoa học, và để nhấn mạnh.<sup class="cite"><a href="{KATA}">[wiki]</a></sup> Nét katakana thẳng và góc cạnh hơn.</p>""",
   notes=f"""<ul>
<li><strong>ー (dấu kéo dài)</strong> chỉ dùng trong katakana: nhân đôi nguyên âm đứng trước. <span class="jp">ケーキ</span> = ke-e-ki (3 nhịp).</li>
<li><strong>Chữ “quen mặt”:</strong> <span class="jp">カ/か, キ/き, セ/せ</span> gần giống bản hiragana — học nhanh.</li>
<li><strong>シ (shi)</strong>: hai chấm xếp gần <em>ngang</em> bên trái, nét dài hất <em>lên</em> từ dưới. Bài sau sẽ gặp ツ — cặp dễ lẫn nhất của katakana.</li>
<li><strong>ソ (so)</strong>: một chấm và một nét kéo <em>xuống</em> từ trên — bài 0010 so với ン.</li>
<li><strong>ウ/ワ/フ</strong>, <strong>ク/ケ</strong>, <strong>ス/ヌ</strong> sẽ được so sánh dần ở các bài sau.</li>
</ul>""",
   read=[("アイス","aisu","kem"),("ケーキ","keeki","bánh kem"),("ココア","kokoa","ca cao"),("スキー","sukii","trượt tuyết"),("ソース","soosu","nước sốt"),("シーソー","shiisoo","bập bênh"),("ケース","keesu","cái hộp, vỏ"),("キス","kisu","nụ hôn"),("アクセス","akusesu","truy cập"),("オアシス","oashisu","ốc đảo")],
   read_note="Gõ ー bằng cách lặp nguyên âm: ケーキ = keeki.",
   mc=[("Chữ katakana nào là “ke”?", ["キ","コ","ケ","ク"], 3, "ケ = ke (giống け).", True),
       ("<span class=\"jp\">ケーキ</span> đọc là gì?", ["kooki","keeki","kaaki","kuuki"], 2, "ケ + ー + キ = keeki.", False)],
   recall=["Viết 15 chữ katakana ア → ソ theo thứ tự.", "Viết bằng katakana: “kem”, “bánh kem”, “trượt tuyết”.", "ー có tác dụng gì?"],
   primary=("Tofugu — Learn Katakana: The Ultimate Guide", TOFU_K, "Đọc phần ア〜ソ.")),
 9: dict(slug="0009-katakana-ta-ho", title="Katakana: タ đến ホ", jp="タチツテト ナニヌネノ ハヒフヘホ",
   lede="Cặp chữ khó nhất của katakana: シ và ツ.",
   win="Đọc và viết tay được 15 chữ タ〜ホ; luôn phân biệt được シ/ツ, ス/ヌ.",
   intro="<p>Sau bài này bạn có 30/46 chữ katakana. Hầu hết từ ngoại lai trong menu quán cà phê đã đọc được.</p>",
   notes="""<ul>
<li><strong>シ vs ツ:</strong> シ — hai chấm xếp <em>ngang</em>, nét dài hất <em>lên</em> từ dưới trái. ツ — hai chấm xếp <em>trên</em>, nét dài kéo <em>xuống</em> từ trên phải. Mẹo: シ “nhìn lên”, ツ “nhìn xuống”.</li>
<li><strong>ス vs ヌ:</strong> ヌ có thêm một nét chéo cắt qua giữa.</li>
<li><strong>チ vs テ:</strong> チ có nét phẩy ở đầu; テ có hai gạch ngang song song.</li>
<li><strong>ヘ</strong> gần như giống hệt へ. <strong>ハ</strong> là hai nét như chữ “bát” 八. <strong>ノ</strong> chỉ một nét phẩy.</li>
<li><strong>フ (fu)</strong> giống phần trên của ふ; đọc như ふ — thổi hơi bằng môi.</li>
</ul>""",
   read=[("テニス","tenisu","quần vợt"),("タクシー","takushii","taxi"),("トースト","toosuto","bánh mì nướng"),("ネクタイ","nekutai","cà vạt"),("ノート","nooto","quyển vở"),("ナイフ","naifu","con dao"),("コーヒー","koohii","cà phê"),("テスト","tesuto","bài kiểm tra"),("ツアー","tsuaa","chuyến du lịch"),("ハート","haato","hình trái tim"),("ヒーター","hiitaa","máy sưởi"),("ソフト","sofuto","phần mềm")],
   mc=[("Chữ nào là “tsu”?", ["シ","ツ","ソ","ン"], 2, "ツ: chấm ở trên, nét dài kéo xuống.", True),
       ("Chữ nào là “nu”?", ["ス","メ","ヌ","ナ"], 3, "ヌ = ス + một nét chéo.", True)],
   recall=["Viết 15 chữ タ → ホ theo thứ tự.", "Viết シ và ツ năm lần mỗi chữ, nói to tên chữ khi viết.", "Viết bằng katakana: “taxi”, “cà phê”, “quần vợt”."],
   primary=("Tofugu — Learn Katakana: The Ultimate Guide", TOFU_K, "Đọc phần タ〜ホ, đặc biệt mục シ/ツ.")),
 10: dict(slug="0010-katakana-ma-n", title="Katakana: マ đến ン", jp="マミムメモ ヤユヨ ラリルレロ ワヲン",
   lede="Mười sáu chữ cuối — và cặp dễ lẫn thứ hai: ソ và ン.",
   win="Đọc và viết tay được cả 46 chữ katakana; phân biệt được ソ/ン, ウ/ワ/フ, ル/レ.",
   intro="<p>Xong bài này bạn đọc được mọi từ ngoại lai không có dấu ゛゜ hay chữ nhỏ.</p>",
   notes="""<ul>
<li><strong>ソ vs ン:</strong> ソ — hai nét đều đi <em>xuống</em>, chấm đứng gần như song song nét dài. ン — chấm nằm <em>ngang</em> bên trái, nét dài hất <em>lên</em>. Giống quy tắc シ/ツ: ン và シ “nhìn lên”.</li>
<li><strong>ウ / ワ / フ:</strong> ウ có chấm trên đầu và nét trái; ワ có nét trái nhưng không chấm; フ chỉ một nét.</li>
<li><strong>ル vs レ:</strong> ル là hai nét (một phẩy + một nét hất), レ là một nét.</li>
<li><strong>ユ vs コ:</strong> ユ có nét ngang dưới kéo dài ra ngoài. <strong>マ vs ア:</strong> ア có nét dọc phẩy xuống dài hơn.</li>
<li><strong>ヲ</strong> tồn tại trong bảng nhưng gần như không dùng — trợ từ “o” luôn viết bằng hiragana を.</li>
</ul>""",
   read=[("ラーメン","raamen","mì ramen"),("ホテル","hoteru","khách sạn"),("メロン","meron","dưa lưới"),("ミルク","miruku","sữa"),("レモン","remon","chanh vàng"),("ワイン","wain","rượu vang"),("ハム","hamu","giăm bông"),("マスク","masuku","khẩu trang"),("リス","risu","con sóc"),("カメラ","kamera","máy ảnh"),("トマト","tomato","cà chua"),("タオル","taoru","khăn tắm"),("メール","meeru","email"),("ヨーヨー","yooyoo","con yo-yo")],
   mc=[("Chữ nào là “n”?", ["ン","ソ","ツ","シ"], 1, "ン: chấm ngang bên trái, nét dài hất lên.", True),
       ("Chữ nào là “ru”?", ["レ","ル","ロ","リ"], 2, "ル có hai nét; レ một nét.", True)],
   recall=["Viết toàn bộ 46 chữ katakana theo bảng — không nhìn.", "Viết シ ツ ソ ン cạnh nhau, đọc to từng chữ.", "Viết bằng katakana: “ramen”, “khách sạn”, “email”."],
   primary=("Tofugu — Learn Katakana: The Ultimate Guide", TOFU_K, "Đọc phần マ〜ン và bài tự kiểm tra.")),
 11: dict(slug="0011-katakana-dakuten-extended", title="Katakana: ゛゜, chữ nhỏ và âm ngoại lai", jp="ガ ッ ャ ティ ファ",
   lede="Mọi quy tắc của hiragana áp dụng y hệt — cộng thêm vài tổ hợp chỉ có trong từ ngoại lai.",
   win="Đọc được mọi từ katakana thông dụng, kể cả ベトナム, パーティー, コンピューター; viết tên mình bằng katakana.",
   intro=f"""<p>゛, ゜, ッ nhỏ và ャュョ nhỏ hoạt động y như bài 0006–0007. Điểm mới duy nhất: katakana ghép thêm chữ nhỏ ァィゥェォ để ghi âm nước ngoài mà tiếng Nhật vốn không có.<sup class="cite"><a href="{KATA}">[wiki]</a></sup></p>""",
   table="KATA_EXT",
   notes=f"""<ul>
<li><strong>ティ</strong> (ti) khác <strong>チ</strong> (chi): パーティー = pātī. <strong>ディ</strong> = di.</li>
<li><strong>ファ フィ フェ フォ</strong> = fa fi fe fo; <strong>ウィ ウェ ウォ</strong> = wi we wo; <strong>シェ ジェ チェ</strong> = she je che.</li>
<li><strong>ヴ</strong> ghi âm “v”, nhưng phần lớn từ dùng バ行 thay: ベトナム (Việt Nam).</li>
<li><strong>Tên của bạn:</strong> tên người Việt được viết bằng katakana theo âm nghe được, không có một cách duy nhất.<sup class="cite"><a href="https://en.wikipedia.org/wiki/Transcription_into_Japanese">[wiki]</a></sup> Ví dụ địa danh: <span class="jp">ハノイ</span> (Hà Nội), <span class="jp">ホーチミン</span> (Hồ Chí Minh). Thử tự viết tên mình, rồi hỏi giáo viên để kiểm tra.</li>
</ul>""",
   read=[("ギター","gitaa","đàn ghi-ta"),("バス","basu","xe buýt"),("ピアノ","piano","đàn piano"),("ジュース","juusu","nước ép"),("ベッド","beddo","cái giường"),("パーティー","paatii","bữa tiệc"),("カフェ","kafe","quán cà phê"),("チョコレート","chokoreeto","sô-cô-la"),("ロボット","robotto","người máy"),("コンピューター","konpyuutaa","máy tính"),("ベトナム","betonamu","Việt Nam"),("ハノイ","hanoi","Hà Nội"),("ホーチミン","hoochimin","Hồ Chí Minh"),("スマートフォン","sumaatofon","điện thoại thông minh")],
   read_note="Gõ ー bằng cách lặp nguyên âm, ッ bằng cách gấp đôi phụ âm: ベッド = beddo.",
   mc=[("<span class=\"jp\">パーティー</span> đọc là gì?", ["baatii","paatii","paatei","paatai"], 2, "パ = pa, ティ = ti, ー kéo dài.", False),
       ("<span class=\"jp\">ベトナム</span> là gì?", ["Nhật Bản","Hàn Quốc","Việt Nam","Hà Nội"], 3, "ベトナム = Việt Nam.", False)],
   listen_new="テ ティ フ フェ チ チョ ジ ジュ",
   writers="ガパッャー",
   recall=["Viết bằng katakana: “Việt Nam”, “bữa tiệc”, “máy tính”.", "ティ và チ khác nhau thế nào?", "Viết tên của bạn bằng katakana và gửi cho giáo viên kiểm tra."],
   primary=("Tofugu — Learn Katakana: The Ultimate Guide", TOFU_K, "Đọc phần dakuten, chữ nhỏ và tổ hợp âm ngoại lai.")),
}
