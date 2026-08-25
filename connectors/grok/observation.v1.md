# tvshoki.grok.observation.v1

Channel-owned observation contract for TV商機. This file is the inlet schema Grok emits into tvshoki. It encodes Media Brain's split: **observation vs match/publish**.

Grok **observes** and stops at **product candidates**. Matching to Rakuten, scoring, and publishing are out of scope of this contract and must not appear in an observation payload.

## Schema id

```
tvshoki.grok.observation.v1
```

JSON object. `additionalProperties: false` at every object. Unknown keys are invalid.

## Required keys

| Key | Type | Notes |
| --- | --- | --- |
| `schema` | string | Must be exactly `tvshoki.grok.observation.v1` |
| `observed_at` | string | ISO-8601 datetime with timezone (e.g. `2026-08-25T07:00:00+09:00`) |
| `source` | object | Provenance of the observation. `additionalProperties: false` |
| `raw_text` | string | Verbatim observed text (caption, post body, page extract, transcript snippet). Do not rewrite into a claim |

All other top-level keys are optional. Omit unknowns. Do not invent values to fill the shape.

## `source`

Required on `source`: `kind`.

`source.kind` (enum, exactly one):

| Value | Meaning |
| --- | --- |
| `tv` | On-air / broadcast capture (primary program evidence when independently confirmed) |
| `x` | X (Twitter) post |
| `web` | General web page |
| `news` | News article |
| `search` | Search-result snippet or SERP extract |
| `sns_reaction` | SNS reaction other than `x` (comments, quote-posts treated as reaction, etc.) |

Optional on `source` (include only what is known):

| Key | Type | Notes |
| --- | --- | --- |
| `url` | string | Source URL. **Forbidden:** Rakuten URLs (see Forbidden) |
| `title` | string | Page / post / segment title as observed |
| `account` | string | Handle or publisher name if present on the source |
| `retrieved_at` | string | ISO-8601 retrieval time if distinct from `observed_at` |

## `program`

Optional object. Include **only fields that are known**. `additionalProperties: false`. Do not guess network, air time, or episode title.

| Key | Type | Notes |
| --- | --- | --- |
| `name` | string | Official program name only (see below) |
| `network` | string | Broadcaster / network as known |
| `aired_at` | string | ISO-8601 air datetime |
| `episode_title` | string | Episode or corner title if known |

### Official program names

Use these strings when the program is one of the channel's owned shows. Do not substitute nicknames, hashtags, or unofficial shortenings in `program.name`:

- `シューイチ`
- `サタデープラス`

If the source is not clearly one of these programs, omit `program` or omit `name` rather than approximating.

## `product_candidates[]`

Optional array of **candidates**, not identities. An observation must **not** assert Rakuten identity (no item URL, no shop, no SKU-as-Rakuten, no "this is the Rakuten product"). Downstream matching is a different stage.

Each element is an object, `additionalProperties: false`. Include only known fields.

| Key | Type | Notes |
| --- | --- | --- |
| `brand` | string | Brand as observed or clearly named |
| `product_name` | string | Product name as observed |
| `model_number` | string | Model number if stated |
| `jan` | string | JAN if stated on the source |
| `category` | string | Coarse category (e.g. kitchen, beauty) if stated or obvious from the source |
| `claim_level` | string | Enum: `confirmed_on_air` \| `weak_confirmation` \| `inferred` |
| `confidence` | number | Closed interval **0–1** (inclusive). Observation confidence only — not an OS score |
| `evidence` | string | Why this candidate exists: quote, timestamp, or page locus. No Rakuten URLs |

Empty array is valid when nothing product-like was observed. Omit the key if not used.

### `claim_level`

| Value | When it is allowed |
| --- | --- |
| `confirmed_on_air` | **Only** with primary on-air evidence or an official program-page statement that the product was shown / named on that airing. Captions, recap blogs, and third-party lists are not primary |
| `weak_confirmation` | Posts, roundups, recap articles, SNS, search snippets that mention the product in connection with the program but are not primary on-air / official program-page evidence |
| `inferred` | Speculation, guesswork, "maybe this product", visual similarity without a named product, or any chain that is not even a weak confirmation |

Do not upgrade `claim_level` because the writer is confident. Upgrade only when the evidence class changes.

### 愛用 (habitual-use claims)

Never write `愛用` (or equivalent habitual-use wording) in `raw_text` paraphrases, `evidence`, or candidate fields unless **primary** on-air or official program-page evidence supports that exact claim. A post, roundup, or rumor that someone "uses" a product is not primary evidence of 愛用.

## Forbidden

The following must **not** appear anywhere in an observation payload (keys, values, `raw_text`, `evidence`, URLs, comments):

- Rakuten URLs
- OS scores
- `公開してよい`
- EPC
- click counts

This contract does **not** include matching, scoring, or publishing. Do not add fields, side-channel notes, or "next step" flags for those stages.

## JSON Schema

```json
{
  "$id": "tvshoki.grok.observation.v1",
  "type": "object",
  "additionalProperties": false,
  "required": ["schema", "observed_at", "source", "raw_text"],
  "properties": {
    "schema": {
      "type": "string",
      "const": "tvshoki.grok.observation.v1"
    },
    "observed_at": {
      "type": "string",
      "format": "date-time"
    },
    "source": {
      "type": "object",
      "additionalProperties": false,
      "required": ["kind"],
      "properties": {
        "kind": {
          "type": "string",
          "enum": ["tv", "x", "web", "news", "search", "sns_reaction"]
        },
        "url": { "type": "string" },
        "title": { "type": "string" },
        "account": { "type": "string" },
        "retrieved_at": { "type": "string", "format": "date-time" }
      }
    },
    "raw_text": { "type": "string" },
    "program": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "name": { "type": "string" },
        "network": { "type": "string" },
        "aired_at": { "type": "string", "format": "date-time" },
        "episode_title": { "type": "string" }
      }
    },
    "product_candidates": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "brand": { "type": "string" },
          "product_name": { "type": "string" },
          "model_number": { "type": "string" },
          "jan": { "type": "string" },
          "category": { "type": "string" },
          "claim_level": {
            "type": "string",
            "enum": ["confirmed_on_air", "weak_confirmation", "inferred"]
          },
          "confidence": {
            "type": "number",
            "minimum": 0,
            "maximum": 1
          },
          "evidence": { "type": "string" }
        }
      }
    }
  }
}
```

## Shape (illustration only)

Field names and types only. Not a live sample. Not a product identity.

```json
{
  "schema": "tvshoki.grok.observation.v1",
  "observed_at": "<ISO-8601>",
  "source": {
    "kind": "tv | x | web | news | search | sns_reaction"
  },
  "raw_text": "<verbatim observed text>",
  "program": {
    "name": "シューイチ | サタデープラス",
    "network": "<only if known>",
    "aired_at": "<only if known>",
    "episode_title": "<only if known>"
  },
  "product_candidates": [
    {
      "brand": "<only if known>",
      "product_name": "<only if known>",
      "model_number": "<only if known>",
      "jan": "<only if known>",
      "category": "<only if known>",
      "claim_level": "confirmed_on_air | weak_confirmation | inferred",
      "confidence": 0.0,
      "evidence": "<quote / timestamp / page locus; no Rakuten URL>"
    }
  ]
}
```
