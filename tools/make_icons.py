"""アプリアイコンを作る：濃紺の地に地球儀とオレンジの旗。"""
from PIL import Image, ImageDraw

INK, OCEAN, LAND, HI = (23, 38, 46), (199, 217, 224), (244, 241, 232), (227, 102, 42)

def icon(size, out):
    s = 4  # 4倍で描いて縮小（なめらかに）
    S = size * s
    im = Image.new("RGB", (S, S), INK)
    d = ImageDraw.Draw(im)
    cx, cy, r = S * 0.47, S * 0.54, S * 0.27   # マスカブル用の安全域（中央80%）に収める
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=OCEAN)
    # 大陸っぽい形
    d.ellipse([cx - r * .62, cy - r * .55, cx + r * .05, cy + r * .25], fill=LAND)
    d.ellipse([cx - r * .05, cy - r * .2, cx + r * .6, cy + r * .62], fill=LAND)
    lw = max(2, int(S * 0.008))
    for k in (-.5, 0, .5):  # 緯線
        y = cy + k * r
        w = (r * r - (k * r) ** 2) ** .5
        d.line([cx - w, y, cx + w, y], fill=INK, width=lw)
    for k in (.45, .85):     # 経線
        d.ellipse([cx - r * k, cy - r, cx + r * k, cy + r], outline=INK, width=lw)
    d.line([cx, cy - r, cx, cy + r], fill=INK, width=lw)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=LAND, width=lw * 2)
    # 旗
    px, top = cx + r * .62, cy - r * 1.45
    d.line([px, top, px, cy - r * .55], fill=LAND, width=lw * 2)
    d.polygon([(px, top), (px + r * .8, top + r * .22), (px, top + r * .44)], fill=HI)
    im.resize((size, size), Image.LANCZOS).save(out)

for size, name in [(192, "icon-192.png"), (512, "icon-512.png"), (180, "apple-touch-icon.png"), (32, "favicon-32.png")]:
    icon(size, f"icons/{name}")
