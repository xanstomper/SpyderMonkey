# 2. The pivot ladder (run in order; stop at first live surface)

- source canon: `holyshit-mode/case-gamdom-adjacent-infra.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
