# OG thumbs (1200×630)

Original text/shape thumbnails for 速報 article OGP and list cards.

- Same PNG is `og:image`, `twitter:image`, and the `.og-card` list image.
- Brand wordmark is the text **テレビでみた** only (no program logo, TV screenshot, manufacturer photo, or licensed artwork).
- Colors match live `styles.css`: bg `#faf8f5`, text `#222`, muted `#555`/`#666`, hairline `#e4dfd6`, CTA `#1a1a1a`.

## Generate / regenerate

From the repo root:

```bash
python3 scripts/generate_og_thumb.py \
  --slug 2026-08-29-hamburg \
  --program サタデープラス \
  --date 2026年8月29日 \
  --category お取り寄せ食品
```

For a later date (e.g. 9/5), change `--slug`, `--program`, `--date`, and `--category`. Do not publish a new product URL until the name is confirmed.

Needs `rsvg-convert` (`librsvg2-bin`) and a Japanese-capable font:

- Preferred: **Noto Sans CJK JP** (OFL) via `fonts-noto-cjk`, or **Noto Sans JP**
- SVG `font-family` is `Hiragino Sans, Noto Sans JP, Noto Sans CJK JP, sans-serif` so macOS browsers match the live site. Rasterization on Linux uses Noto CJK when Hiragino is absent.
- Fallback if those are missing: any fontconfig CJK face (e.g. WenQuanYi Micro Hei). Do not ship English-only thumbs.

Output: `site/og/<slug>.svg` (source) and `site/og/<slug>.png` (exactly 1200×630).

OG PNG paths are static assets. They do not need to be added to `sitemap.xml`.
