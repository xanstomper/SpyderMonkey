# Python probing pitfalls (hit this session) — chain composition

- source canon: `holyshit-mode/cf-wp-origin-bypass-recipe.md`
- base technique: `holyshit-mode-cf-wp-origin-bypass-recipe-python-probing-pitf.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- `http.client` over raw sockets auto-de-chunks; raw `recv()` + manual parse does NOT — a
  `10000\r\n{...}\r\n...` prefix on `wp-json` is chunked-transfer remnants, not a malformed
  response. Use `http.client` for anything TCP/IP-based against a vhost origin.
- `re.finditer(...)[:15]` → `TypeError: 'callable_iterator' object is not subscriptable`.
  Wrap with `list()` or use `findall`.
- Don't mix `b'...' in str` — bytes vs str membership raises `TypeError`. Keep body as str or
  decode once.
- `http.client` with a dict split on `':'` for headers is fragile; pass the dict straight to
  the `headers=` kwarg.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
