# The World in One Image — 20 November 2026

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/dgse8785/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/dgse8785/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

My entry for the make.fun competition **news-image-20261120**,
"Sum up 20 November's world news in one image"
(https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120).

## What the poster shows

One 1024x1024 front page for Friday 20 November 2026, set in dark
navy with a gold rule under the masthead:

- **Lead** — the joint "peace declaration" from Trump, Xi and Putin
  after the Shenzhen summit, Europe's Berlin meeting and its call
  for a winter energy ceasefire, Macron's pushback, and the promised
  Kim meeting.
- **Ukraine** — four ballistic missiles on Kyiv, another strike on
  the Crimea Bridge, no truce from Putin, and the Dutch summoning
  Russia's ambassador.
- **Middle East** — tanker attacks around Hormuz, a mine strike east
  of the Strait, and Houthi strikes on Saudi targets.
- **Climate** — COP31 ending in rancour after the fossil-fuel
  transition was dropped from the draft deal.
- **AI & markets** — Anthropic's record Nasdaq debut, Meta
  rethinking its 2030 net-zero target, and California's probe of
  Nvidia.
- **United Nations** — the stalled race to succeed Guterres.
- An **Also Today** strip: the first US deep-sea mining leases,
  Cyclone Akvan's landfall in India, and Fiona the hippo.

## How it is built

`build_poster.py` draws the poster with Pillow — masthead, lead
panel, a 2x2 grid of story cards, the full-width UN card and the
closing strip — and saves it as `entry.png` beside itself. The
drawing is fixed, so the PNG comes out the same every time.

## How to run it

The submitted program is `main.py`. It uses only the Python standard
library and copies the bundled `entry.png` to `/output/entry.png`:

```sh
python3 main.py
```

Set `MAKEFUN_OUTPUT_DIR` to write somewhere else instead:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

To redraw the poster from scratch, run `python3 build_poster.py`
(requires Pillow), then `python3 main.py` again. The finished
`entry.png` is 1024x1024 and about 116 KB — well under the
competition's 1 MiB limit — and two runs of `main.py` produce
byte-identical output, which you can confirm with `md5sum`.

## License

MIT — see `LICENSE`.
