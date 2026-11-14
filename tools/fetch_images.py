"""Tìm ảnh Wikimedia Commons cho mỗi thẻ trong kana_data.CARDS.

  python3 -I tools/fetch_images.py search     # tìm ứng viên -> tools/candidates.json
  python3 -I tools/fetch_images.py sheet OUT  # ảnh liên hệ (contact sheet) để duyệt
  python3 -I tools/fetch_images.py download   # tải ảnh đã chọn -> assets/img/, ghi tools/images.json

Chọn ứng viên khác: sửa PICK bên dưới (id thẻ -> chỉ số ứng viên), hoặc đổi query trong kana_data.
Chỉ nhận giấy phép tự do: CC0, Public domain, CC BY, CC BY-SA.
"""
import json, os, re, sys, time, urllib.parse, urllib.request, io

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from kana_data import CARDS  # noqa: E402

UA = "kana-flashcards-study/1.0 (personal learning project)"
API = "https://commons.wikimedia.org/w/api.php"
CAND = os.path.join(ROOT, "tools", "candidates.json")
CHOSEN = os.path.join(ROOT, "tools", "images.json")
LIC_OK = re.compile(r"^(CC0|Public domain|CC BY(-SA)? \d\.\d|CC BY(-SA)? \d)", re.I)

PICK = {  # đã duyệt bằng mắt 2026-11-14
    "h-kuruma": 2, "h-sakura": 5, "h-sushi": 2, "h-nasu": 1, "h-hebi": 1, "h-momo": 2, "h-yama": 1, "h-wani": 4,
    "h-daikon": 3, "h-tenpura": 5, "k-aisu": 2, "k-erebeetaa": 5, "k-orenji": 2, "k-kiui": 3, "k-kukkii": 5,
    "k-keeki": 0, "k-koohii": 0, "k-sarada": 1, "k-shatsu": 3,
    # lượt 2
    "h-tamago": 3, "h-toufu": 2, "k-supuun": 0, "k-seetaa": 4, "k-terebi": 3, "k-naifu": 1, "k-nekutai": 0,
    "k-masuku": 2, "k-miruku": 0, "k-taiya": 4, "h-koi": 2, "h-noren": 1, "k-pan": 0, "k-gitaa": 1,
    "k-juusu": 4, "h-tegamiokaku": 1, "h-gyuudon": 0,
}

# Thẻ mà kết quả “Quality images” lạc đề: tìm lại bằng query này, chỉ tìm thường.
QUERY_FIX = {
    "h-kuruma": "sedan car", "h-kome": "uncooked white rice grains", "h-sakura": "cherry blossoms Tokyo",
    "h-sushi": "nigirizushi", "h-chizu": "paper map hand", "h-nasu": "eggplants vegetable",
    "h-nori": "dried nori seaweed sheets", "h-hebi": "grass snake", "h-momo": "peach fruit",
    "h-yama": "mountain range snow Japan", "h-wani": "crocodile basking", "h-mizuonomu": "glass of water",
    "h-daikon": "daikon radish vegetable", "h-tenpura": "shrimp tempura", "h-gyuunyuu": "glass of milk",
    "k-aisu": "ice cream cone", "k-erebeetaa": "elevator doors",
    "k-orenji": "orange fruit sliced", "k-kiui": "kiwifruit sliced", "k-kukkii": "chocolate chip cookies",
    "k-keeki": "strawberry cake slice", "k-koohii": "cup of coffee", "k-sarada": "green salad bowl",
    "k-shatsu": "dress shirt",
    # lượt 2
    "h-toufu": "hiyayakko", "h-tamago": "brown eggs", "k-supuun": "spoons cutlery", "k-seetaa": "pullover sweater",
    "k-terebi": "television set living room", "k-naifu": "kitchen knife", "k-nekutai": "neckties",
    "k-masuku": "surgical face mask", "k-miruku": "milk bottles", "k-taiya": "car tire tyre",
    "k-pan": "bread loaves bakery", "k-gitaa": "classical guitar", "k-juusu": "orange juice glass",
    "h-koi": "koi fish pond", "h-noren": "noren curtain shop", "h-tegamiokaku": "handwritten letter fountain pen",
    "h-gyuudon": "gyudon beef bowl",
}


def card_id(c):
    prefix = "h" if "぀" <= c[1][0] <= "ゟ" else "k"
    return f"{prefix}-{re.sub(r'[^a-z]', '', c[5].lower())}"


def get(params):
    url = API + "?" + urllib.parse.urlencode(params)
    return json.loads(fetch(url))


def search(q, extra=""):
    d = get(dict(action="query", format="json", generator="search", gsrnamespace=6, gsrlimit=25,
                 gsrsearch=f"{q} filetype:bitmap {extra}".strip(), prop="imageinfo",
                 iiprop="url|size|mime|extmetadata", iiurlwidth=330))
    pages = sorted(d.get("query", {}).get("pages", {}).values(), key=lambda p: p.get("index", 0))
    out = []
    for p in pages:
        ii = (p.get("imageinfo") or [{}])[0]
        m = ii.get("extmetadata", {})
        lic = m.get("LicenseShortName", {}).get("value", "")
        w, h = ii.get("width", 0), ii.get("height", 1)
        if ii.get("mime") not in ("image/jpeg", "image/png") or w < 1000 or not (1.15 <= w / h <= 2.1):
            continue
        if not LIC_OK.match(lic):
            continue
        artist = re.sub(r"<[^>]+>", "", m.get("Artist", {}).get("value", "")).strip() or "không rõ"
        out.append(dict(title=p["title"], thumb=ii["thumburl"].split("?")[0], page=ii["descriptionurl"],
                        license=lic, artist=re.sub(r"\s+", " ", artist)[:60]))
    return out


def cmd_search():
    old = json.load(open(CAND)) if os.path.exists(CAND) else {}
    for c in CARDS:
        cid = card_id(c)
        q = QUERY_FIX.get(cid, c[7])
        if cid in old and old[cid]["query"] == q and old[cid]["cands"]:
            continue
        seen, cands = set(), []
        for extra in (("",) if cid in QUERY_FIX else ("incategory:Quality_images", "")):
            for x in search(q, extra):
                if x["title"] not in seen:
                    seen.add(x["title"]); cands.append(x)
            time.sleep(1.5)
        old[cid] = dict(query=q, cands=cands[:6])
        json.dump(old, open(CAND, "w"), ensure_ascii=False, indent=1)
        print(cid, len(cands), flush=True)


def fetch(url):
    import urllib.error
    for attempt in range(6):
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code != 429 or attempt == 5:
                raise
            wait = int(e.headers.get("Retry-After") or 0) or 10 * (attempt + 1)
            print(f"  429, chờ {wait}s", flush=True)
            time.sleep(wait)


def cmd_sheet(out, ids=None, alts=False):
    from PIL import Image, ImageDraw, ImageFont
    cand = json.load(open(CAND))
    rows = [c for c in CARDS if not ids or card_id(c) in ids]
    font = ImageFont.truetype("/System/Library/Fonts/Hiragino Sans GB.ttc", 18)
    tw, th = 240, 160
    if alts:
        cols = 6; cells = [(card_id(c), c, i) for c in rows for i in range(cols)]
    else:
        cols = 6; cells = [(card_id(c), c, PICK.get(card_id(c), 0)) for c in rows]
    nrows = (len(cells) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * tw, nrows * (th + 26)), "white")
    d = ImageDraw.Draw(sheet)
    for k, (cid, c, i) in enumerate(cells):
        x, y = (k % cols) * tw, (k // cols) * (th + 26)
        lst = cand.get(cid, {}).get("cands", [])
        label = f"{cid} {c[4]} [{i}]"
        if i < len(lst):
            try:
                im = Image.open(io.BytesIO(fetch(lst[i]["thumb"]))).convert("RGB")
                im.thumbnail((tw - 6, th - 4)); sheet.paste(im, (x + 3, y + 2))
            except Exception as e:  # noqa: BLE001
                label += " ERR"
        else:
            label += " —"
        d.text((x + 4, y + th + 2), label, fill="black", font=font)
    sheet.save(out, quality=80)
    print(out, sheet.size)


def cmd_download():
    cand = json.load(open(CAND))
    chosen = {}
    os.makedirs(os.path.join(ROOT, "assets", "img"), exist_ok=True)
    for c in CARDS:
        cid = card_id(c)
        x = cand[cid]["cands"][PICK.get(cid, 0)]
        url = re.sub(r"/330px-", "/960px-", x["thumb"])
        dest = os.path.join(ROOT, "assets", "img", cid + ".jpg")
        if not (os.path.exists(dest) and json.load(open(CHOSEN)).get(cid, {}).get("title") == x["title"]
                if os.path.exists(CHOSEN) else False):
            data = fetch(url)
            if url.lower().endswith(".png"):
                from PIL import Image
                Image.open(io.BytesIO(data)).convert("RGB").save(dest, quality=85)
            else:
                open(dest, "wb").write(data)
            time.sleep(0.3)
        chosen[cid] = dict(x, file=f"img/{cid}.jpg")
        print(cid, x["title"], flush=True)
    json.dump(chosen, open(CHOSEN, "w"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "search": cmd_search()
    elif cmd == "sheet": cmd_sheet(sys.argv[2], sys.argv[3].split(",") if len(sys.argv) > 3 else None,
                                   alts=len(sys.argv) > 3)
    elif cmd == "download": cmd_download()
