# Recognition recipe

- source canon: `holyshit-mode/cookie-toss-and-attribution-gadgets.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
