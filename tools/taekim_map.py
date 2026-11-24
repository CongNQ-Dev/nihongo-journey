"""Liên kết "đọc thêm" tới đúng mục trong Tae Kim's Guide to Japanese Grammar (guidetojapanese.org, CC BY-NC-SA 3.0; chỉ trỏ link, không chép nội dung).

Mỗi mục được chọn sau khi mở trang Tae Kim và đối chiếu TIÊU ĐỀ các phần trong trang với mẫu câu của bài Minna
(2026-11-24). Chỉ ghi những bài có phần khớp rõ; bài còn lại giữ link mục lục (xem LESSONS[...]["primary"]).
Tae Kim dạy theo thứ tự riêng nên KHÔNG thay cho giải thích trong sách Minna; chỉ là bài đọc thêm bằng tiếng Anh.
"""
TK = "https://guidetojapanese.org/learn/grammar/"

# số bài Minna -> [(slug, tên mục Tae Kim, phần nào của mục khớp với bài)]
MAP = {
    11: [("numbers", "Numbers and Counting", "số đếm và cách đếm"), ("amount", "Expressing Amounts", "phần 「だけ」 và 「しか」")],
    12: [("past_tense", "Past Tense", "quá khứ của です và tính từ"), ("comparison", "Using 「方」 and 「よる」", "so sánh bằng 「より」 và 「方」")],
    13: [("desire", "Desire and Suggestions", "「たい」 và 「欲しい」"), ("verbparticles", "Particles used with verbs", "trợ từ に／へ đi kèm động từ")],
    14: [("requests", "Making Requests", "「～ください」"), ("teform", "Other uses of the te-form", "「～ている」")],
    15: [("must", "Expressing “must” or “have to”", "phần cấm 「～てはいけない」 và phần nói được phép làm"), ("teform", "Other uses of the te-form", "「～ている」 chỉ trạng thái")],
    16: [("compound", "Compound Sentences", "nối câu bằng thể て (chuỗi động từ, chuỗi trạng thái)")],
    17: [("negativeverbs", "Negative Verbs", "thể phủ định ない"), ("must", "Expressing “must” or “have to”", "「～なければならない」")],
    18: [("potential", "Potential Form", "「～ことができる」 và khả năng"), ("genericnouns", "Special Expressions with Generic Nouns", "danh từ hoá bằng 「こと」")],
    19: [("genericnouns", "Special Expressions with Generic Nouns", "「～たことがある」 (kinh nghiệm)"), ("surunaru", "Using する and なる with the に particle", "trở nên (くなる／になる)")],
    20: [("slang", "Casual Patterns and Slang", "nói thân mật"), ("sentence_ending", "Review and more sentence-ending particles", "ね／よ cuối câu")],
    21: [("define", "Defining and Describing", "trích dẫn bằng 「という」"), ("certainty", "Various degrees of certainty", "「でしょう」")],
    22: [("clause", "Relative Clauses and Sentence Order", "mệnh đề bổ nghĩa danh từ"), ("actionclause", "Acting on relative clauses", "mệnh đề làm tân ngữ")],
    23: [("conditionals", "Conditionals", "phần 「と」 (kết quả tất nhiên)")],
    24: [("favors", "Giving and Receiving", "あげる／くれる／もらう")],
    25: [("conditionals", "Conditionals", "phần 「たら」 và các cách nói “nếu”")],
    26: [("nounparticles", "Noun-related Particles", "phần 「の」 dùng để giải thích (「んです」)"), ("requests", "Making Requests", "nhờ vả lịch sự")],
    27: [("potential", "Potential Form", "thể khả năng, 「見える」 và 「聞こえる」"), ("amount", "Expressing Amounts", "phần 「しか」")],
    28: [("timeactions", "Time-specific actions", "phần 「ながら」 (hai việc cùng lúc)")],
    29: [("unintended", "Unintended Actions", "「～てしまう」"), ("in-transitive", "Transitive and Intransitive Verbs", "cặp tha động từ / tự động từ")],
    30: [("teform", "Other uses of the te-form", "「～ている」, 「～てある」, 「～ておく」"), ("in-transitive", "Transitive and Intransitive Verbs", "cặp tha động từ / tự động từ")],
    31: [("desire", "Desire and Suggestions", "thể ý chí (rủ rê, ý định)")],
    32: [("certainty", "Various degrees of certainty", "「かもしれない」, 「でしょう」")],
    33: [("requests", "Making Requests", "phần Command Form (thể mệnh lệnh)")],
    35: [("conditionals", "Conditionals", "phần 「ば」 và 「なら」")],
    36: [("surunaru", "Using する and なる with the に particle", "「なる」 và 「する」 với động từ (「ように なる」)")],
    37: [("causepass", "Causative and Passive Verbs", "phần Passive Verbs")],
    38: [("nounparticles", "Noun-related Particles", "phần 「の」 (danh từ hoá)")],
    39: [("compound", "Compound Sentences", "phần nêu lý do bằng 「から」 và 「ので」")],
    40: [("question", "The Question Marker", "câu hỏi lồng trong câu (「か」)"), ("try", "Trying or attempting something", "「～てみる」")],
    41: [("favors", "Giving and Receiving", "やる／くれる／もらう và dạng lịch sự"), ("honorific", "Honorific and Humble Forms", "いただく／くださる")],
    43: [("similarity", "Similarity or hearsay", "phần 「～そう」 (trông có vẻ)")],
    44: [("easyhard", "Actions that are easy or hard to do", "「～やすい」／「～にくい」"), ("surunaru", "Using する and なる with the に particle", "「～くする」, 「～にする」")],
    46: [("timeactions", "Time-specific actions", "phần 「ばかり」 (vừa mới)"), ("should", "Things that should be a certain way", "phần 「はず」")],
    47: [("similarity", "Similarity or hearsay", "「みたい」, 「よう」, 「そうだ」 (nghe nói)")],
    48: [("causepass", "Causative and Passive Verbs", "phần Causative Verbs")],
    49: [("honorific", "Honorific and Humble Forms", "phần Honorific")],
    50: [("honorific", "Honorific and Humble Forms", "phần Humble")],
}
# Bài chưa có mục khớp xác nhận (giữ link mục lục): 34 (とおりに／あとで), 42 (ために／のに), 45 (ばあい／のに).


def html(m):
    """Danh sách link đọc thêm cho bài Minna m, hoặc '' nếu chưa có mục khớp."""
    if m not in MAP:
        return ""
    return "; ".join(f'<a href="{TK}{s}">Tae Kim — {t}</a> ({d})' for s, t, d in MAP[m])
