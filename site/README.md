# site

消費者向けブランド「テレビでみた」の静的公開ファイル。

想定ドメイン: `https://tv-mita.jp/`
このフォルダをリポジトリに置いただけでは `tv-mita.jp` には公開されない。公開は未実施。

## 構成

HTML / CSS のみ。CMS・ダッシュボード・認証・JS フレームワークは使わない。

- `index.html` — トップ
- `p/index.html` — 商品ミニページの空テンプレート（パス例: `/p/`）
- `styles.css` — 共通スタイル

## デプロイ

未定（TBD）。GitHub Pages を読者向けの公開 URL にしない。GitHub blob URL も読者 URL にしない。

カスタムドメインは `tv-mita.jp`。DNS は Owner の お名前.com Navi（Mac 上）で管理する。ドメイン購入や DNS 変更はこの作業の範囲外。

## 商品ページ

`p/index.html` をコピーしてフィールドを埋める。入れるのは次だけ。

番組名 / 放送日 / 紹介された商品 / 画像（任意） / ブランド / 商品名 / 根拠URL / 価格帯 / 送料事実 / 「商品を見る」CTA

CTA の `href` は公開時に本番の追跡 URL を注入する。このリポジトリでは `href="#"` のままにする。楽天 ID を invent しない。live の `hb.afl` URL を commit しない。

task_id: 2026-08-26-tvshoki-gtm-v1
