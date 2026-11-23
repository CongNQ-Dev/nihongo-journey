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
from minna_vocab import VOCAB, vocab_id  # noqa: E402

UA = "nihongo-journey-study/1.0 (educational project; https://github.com/CongNQ-Dev/nihongo-journey)"
API = "https://commons.wikimedia.org/w/api.php"
CAND = os.path.join(ROOT, "tools", "candidates.json")
CHOSEN = os.path.join(ROOT, "tools", "images.json")
LIC_OK = re.compile(r"^(CC0|Public domain|CC BY(-SA)? \d\.\d|CC BY(-SA)? \d)", re.I)

PICK = {  # đã duyệt bằng mắt 2026-11-14
    "h-kuruma": 2, "h-sakura": 5, "h-sushi": 2, "h-nasu": 1, "h-hebi": 1, "h-momo": 2, "h-yama": 1, "h-wani": 4,
    "h-daikon": 3, "h-tenpura": 5, "k-aisu": 2, "k-erebeetaa": 5, "k-orenji": 2, "k-kiui": 3, "k-kukkii": 5,
    "k-keeki": 0, "k-koohii": 0, "k-sarada": 1, "k-shatsu": 3,
    # lượt 2
    "h-tamago": 3, "h-toufu": 2, "k-supuun": 0, "k-seetaa": 4, "k-naifu": 1, 
    "k-masuku": 2, "k-miruku": 0, "k-taiya": 4, "h-koi": 2, "h-noren": 1, "k-pan": 0, "k-gitaa": 1,
    "k-juusu": 4, "h-tegamiokaku": 1, "h-gyuudon": 0,
    # từ vựng Minna 1–4
    "v-sensei": 1, "v-isha": 2, "v-byouin": 5, "v-jisho": 4, "v-enpitsu": 1, "v-omiyage": 1, "v-shokudou": 1,
    "v-uketsuke": 5, "v-toire": 4, "v-kaigi": 5,
    # Minna 5–7
    "v-chikatetsu": 2, "v-tomodachi": 1, "v-kazoku": 1, "v-yomimasu": 2, "v-niku": 3, "v-yasai": 1, "v-fooku": 1,
    "v-keetai": 1, "v-kippu": 3,
    "v-enjinia": 3, "v-betonamu": 2, "v-kaban": 2, "v-tsukue": 1, "v-hatarakimasu": 1, "v-torimasu": 1,
    "v-pasokon": 5, "v-nengajou": 0, "v-kakemasu": 0, "v-kami": 0,
    "v-konsaato": 1, "v-teeburu": 0, "v-tana": 0, "v-posuto": 1, "v-kissaten": 0,
    "v-kaishain": 0, "v-okimasu": 3, "v-nemasu": 2, "v-tabemasu": 0, "v-kaimasu": 3, "v-atsui": 1, "v-ryokou": 5,
    "v-e": 3, "v-arubaito": 0, "v-kodomo": 3, "v-hako": 1, "v-doa": 5, 
    "v-nimotsu": 2, "v-isogashii": 1,
    # rà soát 2026-11-14: thay ảnh sai nghĩa
    "k-terebi": 1, "k-nekutai": 2, "k-paatii": 3, "v-onnanoko": 1, "v-kouen": 0,
}

# Không tìm được ảnh đúng nghĩa → không có thẻ (từ vẫn nằm trong bảng từ vựng của bài).
SKIP = set()

# Thẻ mà kết quả “Quality images” lạc đề: tìm lại bằng query này, chỉ tìm thường.
QUERY_FIX = {
    "v-onnanoko": "little girl smiling",
    "k-paatii": "birthday party celebration friends",
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
    "k-terebi": "flat screen television", "k-naifu": "kitchen knife", "k-nekutai": "silk necktie",
    "k-masuku": "surgical face mask", "k-miruku": "milk bottles", "k-taiya": "car tire tyre",
    "k-pan": "bread loaves bakery", "k-gitaa": "classical guitar", "k-juusu": "orange juice glass",
    "h-koi": "koi fish pond", "h-noren": "noren curtain shop", "h-tegamiokaku": "handwritten letter fountain pen",
    "h-gyuudon": "gyudon beef bowl",
    # từ vựng Minna 1–4
    "v-kaishain": "businessman", "v-enjinia": "engineer hard hat construction site",
    "v-betonamu": "Hoi An ancient town lanterns", "v-kaban": "leather briefcase", "v-tsukue": "wooden writing desk",
    "v-nemasu": "sleeping baby", "v-hatarakimasu": "office workers working computers",
    "v-okimasu": "alarm clock",
    "v-gakkou": "Japanese elementary school building", "v-kaimasu": "shopping",
    "v-torimasu": "photographer holding camera taking picture", "v-kami": "blank white paper sheets stack",
    "v-pasokon": "laptop computer on desk",
    # Minna 7–9
    "v-nengajou": "New Year greeting postcards Japan", "v-nimotsu": "luggage suitcases",
    "v-kakemasu": "man talking on mobile phone", "v-atsui": "blazing sun sky",
    "v-isogashii": "busy restaurant kitchen chefs", "v-ryokou": "backpacker",
    "v-e": "painting canvas", "v-konsaato": "rock concert stage crowd lights",
    # Minna 9–10
    "v-arubaito": "cashier", "v-kodomo": "kids playing",
    "v-hako": "cardboard box", "v-teeburu": "wooden dining table chairs", "v-tana": "wooden shelves storage",
    "v-doa": "door", "v-posuto": "Japanese red mailbox street", "v-kouen": "public park lawn trees bench",
    "v-kissaten": "Japanese coffee shop interior counter", "v-tabemasu": "man eating noodles",
}


def card_id(c):
    prefix = "h" if "぀" <= c[1][0] <= "ゟ" else "k"
    return f"{prefix}-{re.sub(r'[^a-z]', '', c[5].lower())}"


def items():
    """(id, nhãn, query) cho mọi thẻ có ảnh: kana (bài 2–11) + từ vựng Minna (bài 12+)."""
    out = [(card_id(c), c[4], QUERY_FIX.get(card_id(c), c[7])) for c in CARDS]
    out += [(vocab_id(v), v[1], QUERY_FIX.get(vocab_id(v), v[5])) for v in VOCAB]
    return out


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
    for cid, _, q in items():
        if cid in old and old[cid]["query"] == q and old[cid]["cands"]:
            continue
        seen, cands = set(), []
        for extra in ("",):
            for x in search(q, extra):
                if x["title"] not in seen:
                    seen.add(x["title"]); cands.append(x)
            time.sleep(4)
        old[cid] = dict(query=q, cands=cands[:6])
        json.dump(old, open(CAND, "w"), ensure_ascii=False, indent=1)
        print(cid, len(cands), flush=True)


def fetch(url):
    import urllib.error
    url = url.replace("://thumb.wikimedia.org/", "://upload.wikimedia.org/")
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
    rows = [it for it in items() if not ids or it[0] in ids]
    font = ImageFont.truetype("/System/Library/Fonts/Hiragino Sans GB.ttc", 18)
    tw, th = 240, 160
    if alts:
        cols = 6; cells = [(it[0], it, i) for it in rows for i in range(cols)]
    else:
        cols = 6; cells = [(it[0], it, PICK.get(it[0], 0)) for it in rows]
    nrows = (len(cells) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * tw, nrows * (th + 26)), "white")
    d = ImageDraw.Draw(sheet)
    for k, (cid, c, i) in enumerate(cells):
        x, y = (k % cols) * tw, (k // cols) * (th + 26)
        lst = cand.get(cid, {}).get("cands", [])
        label = f"{cid} {c[1]} [{i}]"
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
    for cid, _, _ in items():
        if cid in SKIP:
            continue
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
