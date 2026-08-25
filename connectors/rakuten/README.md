# connectors/rakuten

Runtime wrap of a Rakuten item URL into an affiliate tracking URL.

The publisher / affiliate ID is **not stored in this repository**. Wrap happens at process runtime from the environment variable `RAKUTEN_AFFILIATE_ID`. Do not commit `.env` or any real ID.

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

`${RAKUTEN_AFFILIATE_ID}` is read from the environment only. It must not appear in committed files.

## Probe status (2026-08-25-tvshoki-rakuten-aff-probe)

**BLOCKED.** This Cloud Agent process env still has no `RAKUTEN_AFFILIATE_ID` (also checked: `RAKUTEN_AFL_ID`, `AFFILIATE_ID`). No wrapped URL was generated. `PROBE.md` is not created.

Grant the secret in the Cursor UI only. Do not put the value in Slack, GitHub, or this repo.

1. If this run shows an Add secrets / setup-action prompt, grant `RAKUTEN_AFFILIATE_ID` there as a Runtime Secret, then restart or send a follow-up on a new agent.
2. If that prompt is not shown: open the Cloud Agents environment Secrets tab for `[6bc96506-a079-11f1-b532-320a589b8025](https://cursor.com/dashboard/cloud-agents/environments/e/6bc96506-a079-11f1-b532-320a589b8025)`, add a Runtime Secret named exactly `RAKUTEN_AFFILIATE_ID`, then start a **new** Cloud Agent on this branch (`cursor/rakuten-aff-probe-59c7`). A secret added after this VM booted is not injected into the current process.
