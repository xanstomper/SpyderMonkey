# 3. Opaque token decoding — iot / expired

- source canon: `spydermonkey/tls-auth-audit.md`
- base technique: `spydermonkey-tls-auth-audit-3-opaque-token-decoding.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **iot** · auth **expired** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: radio/serial surface — BLE/NFC/UART classes, lab hardware only
- auth state: the credential/session has lapsed — the class probes reuse, reactivation, and the no-revoke gap

## The technique

- base64url-decode the first bytes of custom tokens; many schemes expose
  version/route/type prefixes in cleartext (e.g. 3-byte ASCII codes that map
  1:1 to endpoint families). Correlate prefix ↔ endpoint across several
  responses to map the scheme.
- Read `Max-Age`/`Expires` + rotation: per-response re-issue, HTTPOnly,
  SameSite. A multi-year Max-Age on a session bearer = matching replay window
  per stolen cookie.
- **Session-ID adoption test (fixation prep)**: send a well-formed but
  attacker-chosen session cookie value on a plain GET. A response with NO
  Set-Cookie = the server silently adopted your ID (CI3-style) — fixation prep
  is viable, and whether login regenerates the ID is the untested half (needs a
  session to verify). A rejection or forced re-issue = fixation closed.
  Register adoption as a SESSION low with the adopted-ID request/response pair
  in the proof.

## Probe adjustment (iot × expired)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
