"""Thay câu ví dụ tự soạn bằng câu Tatoeba (CC BY 2.0 FR) nếu có trong tools/tatoeba_ex.json.

File json do `tools/tatoeba_match.py` sinh ra; khoá: "VOCAB|<bài>|<kana>" hoặc "words|<bài>|<kana>".
Bản dịch kèm theo là tiếng Anh của Tatoeba (không có tiếng Việt), ghi rõ số câu và tác giả để truy nguồn.
"""
import json, os

_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tatoeba_ex.json")
try:
    _D = json.load(open(_PATH, encoding="utf-8"))
except FileNotFoundError:
    _D = {}


def override(src, n, kana, ex, exvn):
    r = _D.get(f"{src}|{n}|{kana}")
    if not r:
        return ex, exvn
    return r["jp"], f'{r["en"]} (Tatoeba #{r["id"]}, {r["user"]}, CC BY 2.0 FR)'


def is_tatoeba(src, n, kana):
    return f"{src}|{n}|{kana}" in _D


import re as _re
_G = _re.compile(r"\[([^\]|]*)((?:\|[^\]|]*)*)\]")
_FURI = {v["jp"]: v["furi"] for v in _D.values() if v.get("furi")}


def _ruby_group(m):
    kan, rd = m.group(1), [x for x in m.group(2).split("|") if x]
    if len(rd) == len(kan) and len(kan) > 1:
        return "".join(f"<ruby>{c}<rt>{r}</rt></ruby>" for c, r in zip(kan, rd))
    return f"<ruby>{kan}<rt>{''.join(rd)}</rt></ruby>"


def ruby(jp):
    """HTML ruby cho câu Tatoeba đã chọn (furigana của Tatoeba); '' nếu câu không phải câu Tatoeba hoặc không có kanji."""
    f = _FURI.get(jp)
    return _G.sub(_ruby_group, f) if f and "[" in f else ""
