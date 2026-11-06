# SEO-spam botnet discovery pattern — grpc / high-priv

- source canon: `holyshit-mode/case-apimart-newapi-fork.md`
- base technique: `holyshit-mode-case-apimart-newapi-fork-seo-spam-botnet-disco.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **grpc** · auth **high-priv** · chain role **pivot**

## Context

- platform: reflection/list methods first; protobuf definitions are the schema oracle
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

Sketchy providers seed GitHub with dozens of random-char accounts pushing identical READMEs,
sometimes literally named `*-bypass-guide` — grep those READMEs for the provider domain
(`go.<provider>/k-xxxxx` affiliate links). Identical descriptions + same-day pushes + 0 stars =
same operator. The "bypass-guide" keyword bait tells you the operator KNOWS its surface is weak.
GitHub search queries that surfaced this: `llm api reseller`, `openai compatible api gateway cheap`,
`ai api relay free claude gpt no key`, `openrouter alternative free api key`.

## Probe adjustment (grpc × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
