# 2. The pivot ladder (run in order; stop at first live surface) — aws / high-priv

- source canon: `holyshit-mode/case-gamdom-adjacent-infra.md`
- base technique: `holyshit-mode-case-gamdom-adjacent-infra-2-the-pivot-ladder-.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **aws** · auth **high-priv** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: IAM/identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

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

## Probe adjustment (aws × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
