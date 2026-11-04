# Kill Chain — chain composition

- source canon: `holyshit-mode/case-freeinference-org.md`
- base technique: `holyshit-mode-case-freeinference-org-kill-chain.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

1. **Recon**: `dig TXT freeinference.org` → no SPF leak. TLS SAN reveals `openinfra.freeinference.org` + `*.opendata.freeinference.org`.
2. **Surface Discovery**: `/api/dashboard` returns 200 unauth with 55KB GPU telemetry (stale cache). JS bundle (`app.js`) reveals two password-gated endpoints:
   - `x-refresh-password` → `/api/dashboard?refresh=1` (cache-bust)
   - `x-export-password` → `/api/export?days=N` (full data export)
3. **Vector**: Both endpoints use single shared secrets, stored in sessionStorage, with **ZERO rate limiting** (20 rapid wrong-password attempts → all 401, zero 429 on each).
4. **Exploitation**: Brute-forced `x-export-password` with trivial wordlist. Password `madsys` matched on 7th attempt.
5. **Exfiltration**: `GET /api/export?days=30` with `x-export-password: madsys` → **6.3MB JSON** of live telemetry. Verified with days=90 (same volume, 720-hour retention).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
