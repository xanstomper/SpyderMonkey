# 6.1 Bucket/backup enumeration (score 85)

- source canon: `3am-shinjitsu/arsenal-06-infra-hosting.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- generated: 2026-11-04

## The technique

- NAME FAMILIES: `<target>`, `<target>-backup`, `backup-<target>`, `<target>-prod`,
  `<brand>-assets`, `<target>-static`, `s3-<target>`, `<target>.s3.<region>` on S3/GCS/Azure.
- GRADATION: listing (anon GET /) > read > write. Write-probe = FORBIDDEN unless owned
  (revert-map first). Listing+read on sensitive prefixes = CONFIRMED data-at-reach.
- VERIFY BEFORE VERDICT: an exposed archive is a dump only after it's been opened — download,
  `file`, listing, sample (PII minimality). Identical soft-404 shell = absent (§2.2).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
