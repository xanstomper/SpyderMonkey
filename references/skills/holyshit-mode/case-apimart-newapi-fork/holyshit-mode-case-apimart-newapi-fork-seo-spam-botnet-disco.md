# SEO-spam botnet discovery pattern

- source canon: `holyshit-mode/case-apimart-newapi-fork.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

## The technique

Sketchy providers seed GitHub with dozens of random-char accounts pushing identical READMEs,
sometimes literally named `*-bypass-guide` — grep those READMEs for the provider domain
(`go.<provider>/k-xxxxx` affiliate links). Identical descriptions + same-day pushes + 0 stars =
same operator. The "bypass-guide" keyword bait tells you the operator KNOWS its surface is weak.
GitHub search queries that surfaced this: `llm api reseller`, `openai compatible api gateway cheap`,
`ai api relay free claude gpt no key`, `openrouter alternative free api key`.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
