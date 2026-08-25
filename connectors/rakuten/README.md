# connectors/rakuten

Runtime wrap of a Rakuten item URL into an affiliate tracking URL.

Do not commit a raw `RAKUTEN_AFFILIATE_ID=` assignment, `.env`, access key, application ID, or a live tracking URL. Wrap happens at process runtime from `RAKUTEN_AFFILIATE_ID`. The wrap output is not stored in this repository.

## Environment

Required name:

```
RAKUTEN_AFFILIATE_ID
```

Template (empty): see [`.env.example`](../../.env.example) at the repo root.

If `RAKUTEN_AFFILIATE_ID` is unset or empty, wrapping is **BLOCKED**. Do not invent an ID.

## Wrap (when the env var is present)

The tracking URL is built at process runtime from the env var and a URL-encoded item URL. `${RAKUTEN_AFFILIATE_ID}` is read from the environment only. Do not commit a raw ID assignment, `.env`, access key, application ID, or wrap output.

## Status (task_id: 2026-08-26-tvshoki-unpublish-yotsuba-github)

Wrap was proven at runtime from process env `RAKUTEN_AFFILIATE_ID`, then unpublished from git by Owner order. No live tracking URL or probe file remains in this tree. No live Ichiba / `openapi.rakuten.co.jp` call.
