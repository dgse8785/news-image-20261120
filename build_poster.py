"""Poster generator for the news-image-20261120 entry.

Draws a single 1024x1024 front page that sums up the world news of
Friday 20 November 2026: a masthead, one lead story about the joint
peace declaration that followed the Shenzhen summit, four smaller
story cards, a full-width United Nations card and a closing strip
of brief items. Running this file writes entry.png next to it.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

SIZE = 1024
MARGIN = 40
CONTENT_W = SIZE - 2 * MARGIN

BG = (9, 20, 38)
PANEL = (17, 34, 58)
PANEL_EDGE = (43, 66, 99)
INK = (242, 245, 249)
SOFT = (168, 182, 200)
GOLD = (232, 179, 60)
RED = (228, 87, 77)
TEAL = (63, 182, 178)
SKY = (91, 141, 239)
LEAF = (111, 191, 115)
PLUM = (176, 140, 232)

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")


def load(name, size):
    return ImageFont.truetype(str(FONT_DIR / name), size)


def serif(size):
    return load("DejaVuSerif-Bold.ttf", size)


def bold(size):
    return load("DejaVuSans-Bold.ttf", size)


def plain(size):
    return load("DejaVuSans.ttf", size)


def wrap(draw, text, font, limit):
    """Split text into lines that each fit within limit pixels."""
    lines = []
    current = ""
    for word in text.split():
        trial = word if not current else current + " " + word
        if draw.textlength(trial, font=font) <= limit:
            current = trial
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_block(draw, xy, text, font, fill, limit, leading):
    """Draw wrapped text from xy and return the y just below it."""
    x, y = xy
    for line in wrap(draw, text, font, limit):
        draw.text((x, y), line, font=font, fill=fill)
        y += leading
    return y


def panel(draw, box, accent):
    draw.rounded_rectangle(box, radius=14, fill=PANEL, outline=PANEL_EDGE, width=2)
    x0, y0, x1, _ = box
    draw.rounded_rectangle((x0, y0, x0 + 10, y0 + 44), radius=5, fill=accent)
    return x0 + 26, y0 + 20


def story_card(draw, box, accent, label, body):
    inner_x, inner_y = panel(draw, box, accent)
    inner_w = box[2] - box[0] - 52
    draw.text((inner_x, inner_y), label, font=bold(17), fill=accent)
    draw_block(draw, (inner_x, inner_y + 30), body, plain(18), INK, inner_w, 25)


def build():
    img = Image.new("RGB", (SIZE, SIZE), BG)
    draw = ImageDraw.Draw(img)

    # Masthead
    draw.text((MARGIN, 34), "THE WORLD IN ONE IMAGE", font=serif(50), fill=INK)
    draw.text(
        (MARGIN, 98),
        "FRIDAY · 20 NOVEMBER 2026 — THE DAY ON ONE POSTER",
        font=bold(19),
        fill=GOLD,
    )
    draw.line((MARGIN, 130, SIZE - MARGIN, 130), fill=GOLD, width=3)

    # Lead story: the Shenzhen summit peace declaration and its fallout
    lead_box = (MARGIN, 146, SIZE - MARGIN, 382)
    lx, ly = panel(draw, lead_box, RED)
    lead_w = lead_box[2] - lead_box[0] - 52
    draw.text((lx, ly), "LEAD · AFTER THE SHENZHEN SUMMIT", font=bold(18), fill=RED)
    hy = draw_block(
        draw,
        (lx, ly + 30),
        "Trump, Xi and Putin sign a joint 'peace declaration' — and the world reacts",
        serif(31),
        INK,
        lead_w,
        38,
    )
    draw_block(
        draw,
        (lx, hy + 6),
        "Their call — UN reform, nuclear restraint, oil, law — "
        "reverberates. Europe meets in Berlin seeking a winter energy "
        "ceasefire. Macron: it will not reorganise the world. Trump "
        "promises a Kim meeting 'at some point', amid pushback at home.",
        plain(20),
        SOFT,
        lead_w,
        28,
    )

    # Four story cards in a 2x2 grid
    gap = 12
    card_w = (CONTENT_W - gap) // 2
    card_h = 176
    top = 394
    cards = [
        (
            RED,
            "UKRAINE",
            "Kyiv hit by four ballistic missiles; Ukraine strikes the "
            "Crimea Bridge again. Putin rules out any sea or energy "
            "truce. The Netherlands summons Russia's envoy over its "
            "damaged Kyiv embassy.",
        ),
        (
            TEAL,
            "MIDDLE EAST",
            "Iran steps up tanker attacks around Hormuz as oil slides. "
            "A tanker ablaze after a mine strike east of the Strait. "
            "Houthi drones hit Saudi targets, damaging Riyadh's "
            "tallest building.",
        ),
        (
            LEAF,
            "CLIMATE · COP31",
            "COP31 wraps up in rancour. The near-final texts are "
            "branded an 'outrage' after the fossil-fuel transition "
            "was cut from the draft deal.",
        ),
        (
            SKY,
            "AI & MARKETS",
            "Anthropic jumps 17% on its record Nasdaq debut, the "
            "first pure-AI listing. Meta rethinks its 2030 net-zero "
            "target amid the AI buildout. California probes Nvidia "
            "over China AI chips.",
        ),
    ]
    for idx, (accent, label, body) in enumerate(cards):
        col, row = idx % 2, idx // 2
        x0 = MARGIN + col * (card_w + gap)
        y0 = top + row * (card_h + gap)
        story_card(draw, (x0, y0, x0 + card_w, y0 + card_h), accent, label, body)

    # Full-width card: the United Nations succession race
    un_box = (MARGIN, 766, SIZE - MARGIN, 886)
    ux, uy = panel(draw, un_box, PLUM)
    draw.text((ux, uy), "UNITED NATIONS", font=bold(17), fill=PLUM)
    draw_block(
        draw,
        (ux, uy + 30),
        "The race to succeed Guterres stalls — with no successor in "
        "sight, the United Nations could soon find itself leaderless.",
        plain(20),
        INK,
        un_box[2] - un_box[0] - 52,
        29,
    )

    # Closing strip of brief items
    draw.line((MARGIN, 902, SIZE - MARGIN, 902), fill=PANEL_EDGE, width=2)
    draw.text((MARGIN, 914), "ALSO TODAY", font=bold(16), fill=GOLD)
    draw_block(
        draw,
        (MARGIN, 940),
        "US auctions its first deep-sea mining leases despite a court "
        "ruling  •  Cyclone Akvan makes landfall on India's "
        "Andhra–Odisha coast  •  Fiona, Cincinnati Zoo's beloved "
        "hippo, dies after swallowing a hat",
        plain(17),
        SOFT,
        CONTENT_W,
        23,
    )

    out = Path(__file__).with_name("entry.png")
    img.save(out, format="PNG", optimize=True)
    return out


if __name__ == "__main__":
    print(build())
