#!/usr/bin/env python3
"""Generate a 1200×630 original text/shape OG thumbnail (SVG + PNG).

Usage (9/5 and later):
  python3 scripts/generate_og_thumb.py \\
    --slug 2026-09-05-example \\
    --program サタデープラス \\
    --date 2026年9月5日 \\
    --category 生活便利グッズ

Writes site/og/<slug>.svg and site/og/<slug>.png.

Rasterizer: rsvg-convert (librsvg). Japanese glyphs come from Noto Sans CJK JP
when installed (OFL, apt: fonts-noto-cjk), else Noto Sans JP / Hiragino Sans
via fontconfig. The SVG itself names Hiragino Sans / Noto Sans JP so browsers
match the live site stack. Do not invent English-only thumbs.

Brand colors are locked to live site/styles.css until Designer revises:
  bg #faf8f5, text #222, muted #555/#666, hairline #e4dfd6, CTA #1a1a1a.
Wordmark is text only: テレビでみた.
"""

from __future__ import annotations

import argparse
import shutil
import struct
import subprocess
import sys
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT_DIR = ROOT / "site" / "og"
WIDTH = 1200
HEIGHT = 630
FONT_STACK = "Hiragino Sans, Noto Sans JP, Noto Sans CJK JP, sans-serif"


def png_dimensions(path: Path) -> tuple[int, int]:
    with path.open("rb") as fh:
        sig = fh.read(8)
        if sig != b"\x89PNG\r\n\x1a\n":
            raise SystemExit(f"{path} is not a PNG")
        length = struct.unpack(">I", fh.read(4))[0]
        chunk = fh.read(4)
        if chunk != b"IHDR" or length < 8:
            raise SystemExit(f"{path} missing IHDR")
        width, height = struct.unpack(">II", fh.read(8))
    return width, height


def svg_markup(program: str, date: str, category: str) -> str:
    program_xml = escape(program)
    date_xml = escape(date)
    category_xml = escape(category)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">
  <rect width="{WIDTH}" height="{HEIGHT}" fill="#faf8f5"/>
  <rect x="48" y="48" width="1104" height="534" fill="none" stroke="#e4dfd6" stroke-width="2"/>
  <rect x="48" y="48" width="18" height="534" fill="#1a1a1a"/>
  <text x="108" y="228" font-family="{FONT_STACK}" font-size="72" font-weight="700" fill="#222">{program_xml}</text>
  <text x="108" y="318" font-family="{FONT_STACK}" font-size="48" font-weight="500" fill="#555">{date_xml}</text>
  <text x="108" y="422" font-family="{FONT_STACK}" font-size="52" font-weight="700" fill="#222">{category_xml}</text>
  <text x="108" y="528" font-family="{FONT_STACK}" font-size="28" font-weight="500" fill="#666">テレビでみた</text>
</svg>
"""


def rasterize(svg_path: Path, png_path: Path) -> None:
    rsvg = shutil.which("rsvg-convert")
    if not rsvg:
        raise SystemExit(
            "rsvg-convert not found. Install librsvg2-bin "
            "(and fonts-noto-cjk for Japanese glyphs)."
        )
    subprocess.run(
        [
            rsvg,
            "--width",
            str(WIDTH),
            "--height",
            str(HEIGHT),
            "--format",
            "png",
            "--output",
            str(png_path),
            str(svg_path),
        ],
        check=True,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slug", required=True, help="Output basename, e.g. 2026-08-29-hamburg")
    parser.add_argument("--program", required=True, help="番組名")
    parser.add_argument("--date", required=True, help="放送日, e.g. 2026年8月29日")
    parser.add_argument("--category", required=True, help="商品カテゴリ")
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=DEFAULT_OUT_DIR,
        help="Directory for SVG and PNG (default: site/og)",
    )
    args = parser.parse_args()

    out_dir = args.out_dir if args.out_dir.is_absolute() else ROOT / args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    svg_path = out_dir / f"{args.slug}.svg"
    png_path = out_dir / f"{args.slug}.png"

    svg_path.write_text(svg_markup(args.program, args.date, args.category), encoding="utf-8")
    rasterize(svg_path, png_path)

    width, height = png_dimensions(png_path)
    if (width, height) != (WIDTH, HEIGHT):
        raise SystemExit(f"{png_path} is {width}×{height}, expected {WIDTH}×{HEIGHT}")
    print(f"wrote {svg_path.relative_to(ROOT)}")
    print(f"wrote {png_path.relative_to(ROOT)} ({width}×{height})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
