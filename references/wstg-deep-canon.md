# The WSTG Deep Canon — per-test detail the families run as probes

> The OWASP WSTG tests the batteries exercise, one entry per test,
> family-native: the differential, the proof, the wall.

## WSTG-ATHN-04 Password Reset Flow

- class: predictable reset tokens, host-header poisoning of reset links
- probe: request TWO resets on the lab replica, diff token entropy; replay the Host header
- wall: lab replica only — no real reset emails are ever triggered

## WSTG-ATHN-05 Logout and Browser Cache

- class: session data alive in browser cache after logout
- probe: cache-control header inventory on the lab replica's authed pages
- wall: read-only headers

## WSTG-SESS-02 Cookies Attribute Flags

- class: missing Secure/HttpOnly/SameSite on session cookies
- probe: Set-Cookie header inventory across the lab replica's flows
- wall: read-only

## WSTG-SESS-03 Session Fixation

- class: session id accepted BEFORE authentication (fixation class)
- probe: pre-auth token vs post-auth token differential on the lab replica
- wall: lab replica

## WSTG-SESS-08 Per-Session Weakness

- class: same session id across concurrent logins (non-unique)
- probe: two parallel logins on the lab replica, diff ids
- wall: lab replica

## WSTG-CLNT-04 Client-side URL Redirect

- class: fragment/JS-driven redirects attacker-controllable
- probe: the REDIRECT battery + location header differential
- wall: benign evil.example marker only

## WSTG-CLNT-07 Cross Origin Resource Sharing

- class: ACAO: * with credentials, reflected origins
- probe: Origin header differentials on the lab replica
- wall: read-only headers

## WSTG-CLNT-09 Frame Isolation (Clickjacking)

- class: missing X-Frame-Options/frame-ancestors
- probe: header inventory — the crown is the missing header, no live framing
- wall: read-only

## WSTG-CLNT-12 WebSocket Hijack

- class: ws endpoints without origin checks
- probe: origin header differential on the lab ws endpoint
- wall: lab replica

## WSTG-BUSL-02 Discount and Refund Logic

- class: negative/refund abuse in order flows
- probe: the BIZLOGIC battery — negative/zero/overflow on the lab checkout replica
- wall: lab replica; live order flows are inventory-only

## WSTG-BUSL-05 Currency and Rounding

- class: rounding direction, currency confusion
- probe: boundary quantities on the lab replica; the math differential is the proof
- wall: lab replica

## WSTG-INPT-04 HTTP Parameter Pollution

- class: duplicate params — parser disagreement between tiers
- probe: duplicated keys with different values; the DIFFERENT parsed value is the proof
- wall: lab replica

## WSTG-INPT-07 XPath Injection

- class: user input reaching XPath
- probe: the quote/syntax markers from the INJECTION battery
- wall: reflected markers only

## WSTG-INPT-10 SMTP/IMAP Injection

- class: header injection into mail flows
- probe: CRLF markers in the lab replica's mailer form
- wall: lab replica; no real mail is ever sent

## WSTG-INPT-13 XSLT Injection

- class: xslt transforms on user input
- probe: document() and system-property markers on the lab replica
- wall: reflected markers only

## WSTG-ERRH-01 Error Code and Message Analysis

- class: stack traces, sql fragments, paths in errors
- probe: malformed inputs forcing 500s on the lab replica; harvest the trace class
- wall: read-only

## WSTG-ATHZ-04 Insecure Direct Object References

- class: the IDOR core
- probe: the IDOR battery — ±1/0/-1/999999 with the declared principal
- wall: upward-only; foreign data beyond the marker is never read

## WSTG-APIT-02 Rate Limiting

- class: missing/naive rate limits
- probe: 3-request timing differential on the lab replica — the limit SHAPE, never a flood
- wall: proof is the missing counter, not an outage

## WSTG-APIT-04 GraphQL

- class: introspection open, field-level authz gaps, batching abuse
- probe: introspection query + aliased duplicate fields on the lab endpoint
- wall: lab replica
