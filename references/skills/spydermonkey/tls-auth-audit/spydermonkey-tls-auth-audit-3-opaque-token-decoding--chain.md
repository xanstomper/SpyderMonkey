# 3. Opaque token decoding — chain composition

- source canon: `spydermonkey/tls-auth-audit.md`
- base technique: `spydermonkey-tls-auth-audit-3-opaque-token-decoding.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
