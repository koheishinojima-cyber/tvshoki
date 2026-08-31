# OG thumbs (1200×630)

Original text/shape thumbnails for 速報 article OGP and list cards.

WEB Designer lock (hamburg pilot visual — reuse this template forever):

- Same PNG is `og:image`, `twitter:image`, and the `.og-card` date-index card that links to the article.
- Paper white `#faf8f5`. Text + simple geometric shapes only.
- Small **テレビでみた** at the top. Center, large, short three lines: 番組名 / 短い日付 / 短い主題.
  Hamburg: `サタデープラス` / `8月29日` / `ハンバーグ`.
- Do not put お取り寄せ食品, product SKU names, ranking, 予告, prices, or buy CTAs on the thumb.
- No program logo, TV screenshot, manufacturer photo, or licensed artwork.
- SKU photos on the article stay Rakuten listing photos. OGP does not switch to those.

## Generate / regenerate

From the repo root:

```bash
python3 scripts/generate_og_thumb.py \
  --slug 2026-08-29-hamburg \
  --program サタデープラス \
  --date 8月29日 \
  --topic ハンバーグ
```

For a later date (e.g. 9/5), change `--slug`, `--program`, `--date`, and `--topic`. Keep the third line short so it stays readable when the card is shrunk on a phone. Do not publish a new product URL until the name is confirmed.

Needs `rsvg-convert` (`librsvg2-bin`) and a Japanese-capable font:

- Preferred: **Noto Sans CJK JP** (OFL) via `fonts-noto-cjk`, or **Noto Sans JP**
- SVG `font-family` is `Hiragino Sans, Noto Sans JP, Noto Sans CJK JP, sans-serif` so macOS browsers match the live site. Rasterization on Linux uses Noto CJK when Hiragino is absent.
- Fallback if those are missing: any fontconfig CJK face (e.g. WenQuanYi Micro Hei). Do not ship English-only thumbs.

Output: `site/og/<slug>.svg` (source) and `site/og/<slug>.png` (exactly 1200×630).

OG PNG paths are static assets. They do not need to be added to `sitemap.xml`.
