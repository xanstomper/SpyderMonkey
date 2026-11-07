# 3. Handoff-code flow = credential minting without gates — api / federated

- source canon: `holyshit-mode/web-llm-proxy-auth-bypasses.md`
- base technique: `holyshit-mode-web-llm-proxy-auth-bypasses-3-handoff-code-flo.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **api** · auth **federated** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- `POST /api/auth/platform-handoff/start` with body `{refresh_token, next, target}` +
  Bearer session accepts ANY target (`admin`, `platform`, `chat`, `sillytavern`, ...).
- Returns 32-hex one-time codes, 60s TTL, redirect to subdomain you may not have recon'd
  (chat./platform./sillytavern. subdomains appeared here — always enumerate from handoff targets).
- Exchange: `POST /api/auth/platform-handoff/exchange {code}` — works cross-host, is
  unthrottled, and DOES NOT check email verification. Replay works within TTL, single-use after.
- Codes look UUIDv4 (128-bit) — not brute-forceable; value is the bypass + new hosts.

## Probe adjustment (api × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
