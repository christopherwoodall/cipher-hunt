#!/usr/bin/env python3
"""Animated decode of the @729-735 clause: cipher -> 'On veut l'en informer, monsieur!'
Frames: cipher context, then cells resolve one by one until the full clause.
Green = confirmed on the stream. Amber = grammatical shape (wording illustrative).
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 900, 560
BG = (12, 14, 20)
DIM = (110, 120, 140)
CIPHER = (150, 170, 200)
GREEN = (80, 220, 130)
AMBER = (255, 190, 90)
WHITE = (235, 238, 245)
ACCENT = (90, 140, 255)

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

def font(sz, bold=False):
    return ImageFont.truetype(FB if bold else FONT, sz)

# clause cells: (global @, cipher, decode word, color)
CELLS = [
    (729, "48", "On", AMBER),
    (730, "88", "veut", AMBER),
    (731, "11", "l'", GREEN),
    (732, "24", "en", GREEN),
    (733, "85", "inform", AMBER),
    (734, "93", "er", AMBER),
    (735, "76", "monsieur", AMBER),
]
# reveal order: la, en, veut, inform+er, On, monsieur
REVEAL = [2, 3, 1, 4, 5, 0, 6]  # indices into CELLS

CONTEXT = [("728", "86"), ("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("736", "18"), ("737", "82"), ("738", "06")]

def draw_frame(revealed):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    y = 40
    d.text((40, y), "R5005  ·  row a5_02  ·  @728–@740", font=font(22, True), fill=WHITE)
    y += 40
    d.text((40, y), "the cipher around the clause", font=font(16), fill=DIM)
    y += 34
    # context strip
    x = 40
    ctx_pairs = ["86", "48", "88", "11", "24", "85", "93", "76", "18", "82", "06", "00", "36"]
    for i, p in enumerate(ctx_pairs):
        hot = 1 <= i <= 7
        d.text((x, y), p, font=font(20, hot), fill=CIPHER if hot else DIM)
        x += 52
    y += 44
    d.text((40, y), "the clause", font=font(16), fill=DIM)
    y += 34
    # clause cipher numbers
    x = 40
    colx = []
    for (at, cp, word, col) in CELLS:
        colx.append(x)
        d.text((x, y), cp, font=font(26, True), fill=CIPHER)
        d.text((x, y + 34), "@%d" % at, font=font(13), fill=DIM)
        x += 108 if len(word) < 6 else 150
    y += 78
    # decode line
    x = 40
    shown = []
    for idx, (at, cp, word, col) in enumerate(CELLS):
        w = 108 if len(word) < 6 else 150
        if idx in revealed:
            d.text((x, y), word, font=font(30, True), fill=col)
            shown.append(word)
        else:
            d.text((x, y), "· ·", font=font(30, True), fill=(60, 66, 80))
        x += w
    y += 70
    # assembled sentence
    if len(revealed) == len(CELLS):
        d.text((40, y), '“On veut l’en informer, monsieur!”', font=font(26, True), fill=WHITE)
        y += 48
        d.text((40, y), "green = confirmed on the stream   ·   amber = grammatical shape, wording illustrative",
               font=font(14), fill=DIM)
        y += 26
        d.text((40, y), "battery verdict: pron730-clause-wide PROMOTE · 1 ungranted assumption (48 = subject)",
               font=font(14), fill=DIM)
    else:
        n = len(revealed)
        total = len(CELLS)
        bar_w = 400
        d.rectangle([40, y, 40 + bar_w, y + 10], fill=(40, 46, 60))
        d.rectangle([40, y, 40 + int(bar_w * n / total), y + 10], fill=ACCENT)
        d.text((460, y - 6), "%d / %d cells" % (n, total), font=font(15), fill=DIM)
    return img

frames = []
revealed = set()
frames.append((draw_frame(revealed), 900))
for idx in REVEAL:
    revealed.add(idx)
    frames.append((draw_frame(set(revealed)), 750))
# hold the finale: lengthen the last frame instead of dupes
last_img, _ = frames[-1]
frames[-1] = (last_img, 3200)

imgs = [f for f, _ in frames]
durations = [ms for _, ms in frames]
imgs[0].save(
    "/home/hatch/workspace/cipher-hunt/lanes/zeschau-seebach-1841/clause-730-decode.gif",
    save_all=True, append_images=imgs[1:], duration=durations, loop=0,
)
print("wrote clause-730-decode.gif", len(imgs), "frames")
