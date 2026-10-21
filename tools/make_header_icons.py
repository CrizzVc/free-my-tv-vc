"""Renders the header icons (white PNGs): search (magnifying glass) and playstore (Play triangle).
Usage: python tools/make_header_icons.py"""
import os

from PIL import Image, ImageDraw

OUT = os.path.join(os.path.dirname(__file__), "..", "app", "assets", "symbols")


def save(im, name):
    path = os.path.join(OUT, name + ".png")
    im.save(path, optimize=True)
    print(name, im.size)


WHITE = (255, 255, 255, 255)


def search_icon():
    s = 172
    im = Image.new("RGBA", (s, s), (255, 255, 255, 0))
    d = ImageDraw.Draw(im)
    cx, cy, r = s * 0.42, s * 0.42, s * 0.28
    stroke = s * 0.10
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=WHITE, width=int(stroke))
    hx0, hy0 = cx + r * 0.72, cy + r * 0.72
    hx1, hy1 = s * 0.84, s * 0.84
    d.line([hx0, hy0, hx1, hy1], fill=WHITE, width=int(stroke))
    d.ellipse([hx1 - stroke / 2, hy1 - stroke / 2, hx1 + stroke / 2, hy1 + stroke / 2], fill=WHITE)
    d.ellipse([hx0 - stroke / 2, hy0 - stroke / 2, hx0 + stroke / 2, hy0 + stroke / 2], fill=WHITE)
    bbox = im.getbbox()
    pad = 12
    im = im.crop((max(0, bbox[0] - pad), max(0, bbox[1] - pad), min(s, bbox[2] + pad), min(s, bbox[3] + pad)))
    save(im, "search")


def playstore_icon():
    s = 172
    im = Image.new("RGBA", (s, s), (255, 255, 255, 0))
    d = ImageDraw.Draw(im)
    pts = [
        (0.28 * s, 0.10 * s),
        (0.88 * s, 0.50 * s),
        (0.28 * s, 0.90 * s),
        (0.28 * s, 0.62 * s),
        (0.18 * s, 0.50 * s),
        (0.28 * s, 0.38 * s),
    ]
    d.polygon(pts, fill=WHITE)
    bbox = im.getbbox()
    pad = 10
    im = im.crop((max(0, bbox[0] - pad), max(0, bbox[1] - pad), min(s, bbox[2] + pad), min(s, bbox[3] + pad)))
    save(im, "playstore")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    search_icon()
    playstore_icon()
