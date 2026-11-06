# Recognition recipe — chain composition

- source canon: `holyshit-mode/cookie-toss-and-attribution-gadgets.md`
- base technique: `holyshit-mode-cookie-toss-and-attribution-gadgets-recognitio.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

1. **Find the tracker pages** in the subdomain inventory (passive DNS/CT logs) and fetch each
   with a working browser fingerprint — they are small static pages (1–6 KB) whose only script
   reads `URLSearchParams` and writes `document.cookie`.
2. **Read the write logic**: the domain attribute (main registrable domain = the toss target),
   Max-Age (90d is typical), SameSite/Secure flags, the per-visit param cap, and the
   RESERVED-NAME blocklist.
3. **Blocklists are exact-match Set lookups** — the miss is the finding: prefixed session
   families (`stel_token` vs reserved `token`), identity cookies (`client-context`), and
   attribution cookies (`referralCode`) fall through while the literal names are blocked.
4. **Inventory the SPA's cookie STORES** (React store pattern: `(0,X.N)("name", default)`
   call sites; also `cookie.get(...)` helpers) to map what the app READS from tossable cookies
   — preference stores are noise; identity/attribution/session-adjacent stores are impact.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
