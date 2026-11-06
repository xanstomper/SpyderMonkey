# Python probing pitfalls (hit this session) — mobile-api / high-priv

- source canon: `holyshit-mode/cf-wp-origin-bypass-recipe.md`
- base technique: `holyshit-mode-cf-wp-origin-bypass-recipe-python-probing-pitf.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **mobile-api** · auth **high-priv** · chain role **pivot**

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

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

## Probe adjustment (mobile-api × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
