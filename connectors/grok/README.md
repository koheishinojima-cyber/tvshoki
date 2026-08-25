# connectors/grok

This directory is the **observation-inlet contract** for TV商機.

Grok writes observations that conform to [`observation.v1.md`](observation.v1.md) / [`observation.v1.schema.json`](observation.v1.schema.json) (`tvshoki.grok.observation.v1`) and **stops at product candidates**. Candidates are not Rakuten identities.

Matching, scoring, and publishing are **out of scope here**. Do not extend this inlet with OS scores, `公開してよい` / publish judgments, EPC, click counts, Rakuten URLs in Grok-generated fields, or any match/publish workflow.

`raw_text` is a verbatim source quote. Do not rewrite it to strip forbidden tokens.

## Machine check

```bash
pip install -r connectors/grok/requirements-test.txt
python3 connectors/grok/test_observation_v1.py
```

Fixtures under `fixtures/` are schema tests only, not live samples.
