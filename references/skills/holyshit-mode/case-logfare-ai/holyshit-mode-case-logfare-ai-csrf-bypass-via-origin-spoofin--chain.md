# CSRF Bypass via Origin Spoofing — chain composition

- source canon: `holyshit-mode/case-logfare-ai.md`
- base technique: `holyshit-mode-case-logfare-ai-csrf-bypass-via-origin-spoofin.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

The server's CSRF validation accepts `Origin: https://logfare.ai`. While browsers cannot set
this from a cross-origin context, this reveals the CSRF check is **Origin-only** with no token:
- `POST /v1/auth/logout` → 200, **NO CSRF CHECK AT ALL** (confirmed: works cross-origin from any origin)
- `POST /connections/revoke` → Origin check only (bypassable via curl with `Origin: https://logfare.ai`)
- `POST /v1/me/delete` → Origin check only
- `POST /v1/auth/regenerate-key` → Origin check only

**Logout endpoint is the critical CSRF gap: zero protection.** A malicious page can call
`fetch('https://logfare.ai/v1/auth/logout', {method:'POST', credentials:'include'})` and log out
any logged-in user who visits. CORS headers on the 200 response let the attacker confirm success.

If Origin check is ever bypassed (via Origin spoofing, Referer manipulation, or another bug),
the full destructive chain is exposed: account deletion, connection revocation, API key regeneration,
force logout — all reachable cross-origin with victim's session.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
