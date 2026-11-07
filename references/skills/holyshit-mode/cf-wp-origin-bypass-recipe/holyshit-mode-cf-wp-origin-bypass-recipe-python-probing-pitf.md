# Python probing pitfalls (hit this session)

- source canon: `holyshit-mode/cf-wp-origin-bypass-recipe.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- `http.client` over raw sockets auto-de-chunks; raw `recv()` + manual parse does NOT — a
  `10000\r\n{...}\r\n...` prefix on `wp-json` is chunked-transfer remnants, not a malformed
  response. Use `http.client` for anything TCP/IP-based against a vhost origin.
- `re.finditer(...)[:15]` → `TypeError: 'callable_iterator' object is not subscriptable`.
  Wrap with `list()` or use `findall`.
- Don't mix `b'...' in str` — bytes vs str membership raises `TypeError`. Keep body as str or
  decode once.
- `http.client` with a dict split on `':'` for headers is fragile; pass the dict straight to
  the `headers=` kwarg.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
