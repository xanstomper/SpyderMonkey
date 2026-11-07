# 3. Opaque token decoding

- source canon: `spydermonkey/tls-auth-audit.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-06

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
