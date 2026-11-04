# SEO-spam botnet discovery pattern — chain composition

- source canon: `holyshit-mode/case-apimart-newapi-fork.md`
- base technique: `holyshit-mode-case-apimart-newapi-fork-seo-spam-botnet-disco.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Sketchy providers seed GitHub with dozens of random-char accounts pushing identical READMEs,
sometimes literally named `*-bypass-guide` — grep those READMEs for the provider domain
(`go.<provider>/k-xxxxx` affiliate links). Identical descriptions + same-day pushes + 0 stars =
same operator. The "bypass-guide" keyword bait tells you the operator KNOWS its surface is weak.
GitHub search queries that surfaced this: `llm api reseller`, `openai compatible api gateway cheap`,
`ai api relay free claude gpt no key`, `openrouter alternative free api key`.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
