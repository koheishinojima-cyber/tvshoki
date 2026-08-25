# connectors/grok

This directory is the **observation-inlet contract** for TV商機.

Grok writes observations that conform to [`observation.v1.md`](observation.v1.md) (`tvshoki.grok.observation.v1`) and **stops at product candidates**. Candidates are not Rakuten identities.

Matching, scoring, and publishing are **out of scope here**. Do not extend this inlet with Rakuten URLs, OS scores, `公開してよい`, EPC, click counts, or any match/publish workflow.
