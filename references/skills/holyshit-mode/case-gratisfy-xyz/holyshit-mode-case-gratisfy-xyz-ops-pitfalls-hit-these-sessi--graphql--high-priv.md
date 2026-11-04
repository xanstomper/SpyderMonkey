# Ops pitfalls hit these sessions — graphql / high-priv

- source canon: `holyshit-mode/case-gratisfy-xyz.md`
- base technique: `holyshit-mode-case-gratisfy-xyz-ops-pitfalls-hit-these-sessi.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **graphql** · auth **high-priv** · chain role **pivot**

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- **holyleadger.py path drift**: SKILL.md cites scripts/holyleadger.py but the active profile's skill dir didn't have it — real file at `~/holyshit-mode/scripts/holyleadger.py`. Verify referenced scripts exist in the ACTIVE skill dir before relying on them (bit twice).
- **holyleadger CLI grammar**: `add <class_id> <status> --target T --score N --technique "..."` — BOTH class_id and status are positional, status SECOND (e.g. `add hypothesis hypothesis --target gratisfy.xyz --score 65 --technique "..."`). Omit positional status → `the following arguments are required: status`, exit 2, entry silently never lands (exit code is the only signal). Statuses lowercase only: confirmed|negative|hypothesis|inconclusive; requires `--target` or `export HOLYSHIT_TARGET`. BLOCKED/RE-VERIFY aren't valid statuses — map BLOCKED→negative. (Bit twice: gratisfy 10-04, iceposeidon 10-20 — check exit code, not stdout.)
- **Asset fetch variant-host trap**: the `www.gratisfy.xyz` variant of an asset URL 404'd silently while apex `gratisfy.xyz` served it — `-o` created an empty file and grep read garbage. Always `-w "%{http_code} %{size_download}"` on every chunk fetch to catch silent 404/empty bodies.

## Probe adjustment (graphql × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
