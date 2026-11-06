# 2. The pivot ladder (run in order; stop at first live surface) — chain composition

- source canon: `holyshit-mode/case-gamdom-adjacent-infra.md`
- base technique: `holyshit-mode-case-gamdom-adjacent-infra-2-the-pivot-ladder-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

1. **CT logs:** `curl "https://crt.sh/?q=%25.<domain>&output=json"` — collect every host
   ever certified. Dedupe, ignore wildcards. Misspelled internal names ("inteligance")
   and infra names ("td", "stagsrv", "incoming-callbacks") are the high-value subset.
2. **Partner brands from the client bundle:** grep the pooled JS for
   `/casino/providers/<brand>-originals` style routes — sister brands ship inside the app.
   Run the SAME ladder against each sister domain's CT logs.
3. **Mirror/entrance sites:** regional gambling pattern — `<tr|giris|m>.<brand>.com`
   on DIFFERENT hosting (different IP range, different server stack, often PHP).
   These host the login funnel for that market. Fingerprint hard.
4. **Passive DNS for dead-certed hosts:** `curl "https://api.hackertarget.com/hostsearch/?q=<domain>"`
   returns historical host→IP pairs. Cross-reference CT hosts with no current DNS.
   A live cert with stripped DNS = decommissioned "internal control panel" — the exact
   artifact the attacker's statement points at. Wayback (`archive.org/wayback/available`)
   and urlscan.io history may hold what it hosted.
5. **Bare origins:** any host resolving to raw cloud IPs (AWS EC2, LeaseWeb) instead of the
   CDN = infrastructure outside the edge rules. Probe its paths directly.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
