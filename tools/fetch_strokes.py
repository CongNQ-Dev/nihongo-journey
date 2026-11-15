"""Tải thứ tự nét kanji từ KanjiVG (CC BY-SA 3.0) và gộp vào assets/strokes.js.
Chỉ tải chữ chưa có. Chạy: python3 -I tools/fetch_strokes.py"""
import json, os, re, sys, time, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kanji_data import KANJI

PATH = os.path.join(ROOT, "assets", "strokes.js")
src = open(PATH, encoding="utf-8").read()
head, body = src.split("window.STROKES = ", 1)
strokes = json.loads(body.strip().rstrip(";"))
added = 0
for k in KANJI:
    ch = k[1]
    if ch in strokes:
        continue
    url = f"https://raw.githubusercontent.com/KanjiVG/kanjivg/master/kanji/{ord(ch):05x}.svg"
    svg = urllib.request.urlopen(url, timeout=20).read().decode("utf-8")
    paths = re.findall(r'<path id="kvg:[0-9a-f]+-s\d+"[^>]*? d="([^"]+)"', svg)
    if not paths:
        sys.exit(f"Không đọc được nét của {ch}")
    strokes[ch] = paths
    added += 1
    time.sleep(0.3)
open(PATH, "w", encoding="utf-8").write(head + "window.STROKES = " + json.dumps(strokes, ensure_ascii=False, separators=(",", ":")) + ";\n")
print(f"Đã thêm {added} chữ, tổng {len(strokes)}")
