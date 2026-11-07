# 6.1 Bucket/backup enumeration (score 85) — iac / low-priv

- source canon: `3am-shinjitsu/arsenal-06-infra-hosting.md`
- base technique: `3am-shinjitsu-arsenal-06-infra-hosting-6-1-bucket-backup-enu.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- context: **iac** · auth **low-priv** · chain role **entry**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: template/state files are the infrastructure inventory — read-only crown of the exposure
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- NAME FAMILIES: `<target>`, `<target>-backup`, `backup-<target>`, `<target>-prod`,
  `<brand>-assets`, `<target>-static`, `s3-<target>`, `<target>.s3.<region>` on S3/GCS/Azure.
- GRADATION: listing (anon GET /) > read > write. Write-probe = FORBIDDEN unless owned
  (revert-map first). Listing+read on sensitive prefixes = CONFIRMED data-at-reach.
- VERIFY BEFORE VERDICT: an exposed archive is a dump only after it's been opened — download,
  `file`, listing, sample (PII minimality). Identical soft-404 shell = absent (§2.2).

## Probe adjustment (iac × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
