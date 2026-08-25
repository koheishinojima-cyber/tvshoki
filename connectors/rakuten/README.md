# connectors/rakuten

Runtime wrap of a Rakuten item URL into an affiliate tracking URL.

Do not commit a raw `RAKUTEN_AFFILIATE_ID=` assignment, `.env`, access key, or application ID. Wrap happens at process runtime from `RAKUTEN_AFFILIATE_ID`. Rakuten's `hgc` tracking URL includes a publisher path segment; that wrap output lives in [PROBE.md](PROBE.md), not as an env assignment.

## Environment

Required name:

```
RAKUTEN_AFFILIATE_ID
```

Template (empty): see [`.env.example`](../../.env.example) at the repo root.

If `RAKUTEN_AFFILIATE_ID` is unset or empty, wrapping is **BLOCKED**. Do not invent an ID.

## Wrap (when the env var is present)

Standard host: `hb.afl.rakuten.co.jp`.

The tracking URL is built at runtime as:

```
https://hb.afl.rakuten.co.jp/hgc/${RAKUTEN_AFFILIATE_ID}/?pc=${urlencoded_item_url}
```

`${RAKUTEN_AFFILIATE_ID}` is read from the environment only. Do not commit a raw ID assignment, `.env`, access key, or application ID.

## Probe status (task_id: 2026-08-25-tvshoki-yotsuba-min-article)

Wrapped at runtime from process env `RAKUTEN_AFFILIATE_ID`. Tracking URL: [PROBE.md](PROBE.md) (URL plus a same-line scanner pragma; no raw ID assignment). No live Ichiba / `openapi.rakuten.co.jp` call.
