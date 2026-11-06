# The dual-route decoy (biggest time sink — learn it) — grpc / high-priv

- source canon: `holyshit-mode/case-atessa-top.md`
- base technique: `holyshit-mode-case-atessa-top-the-dual-route-decoy-biggest-t.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **grpc** · auth **high-priv** · chain role **pivot**

## Context

- platform: reflection/list methods first; protobuf definitions are the schema oracle
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- Bare paths (`/auth/login`, `/vouchers/redeem`) 422 with `"input":null` on EVERY field despite valid JSON = SPA-fallback router where the body never reaches Pydantic. Looks like "captcha strips the body" — it isn't.
- Real API lives under `/api/*`: `/api/auth/login` → `CAPTCHA verification required`; `/api/auth/signup` 422 echoes `input:{...your body...}` back.
- **Rule:** any 422 with `input:null` on all fields → immediately re-probe the same path under `/api` + `/api/v1` prefixes.

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
