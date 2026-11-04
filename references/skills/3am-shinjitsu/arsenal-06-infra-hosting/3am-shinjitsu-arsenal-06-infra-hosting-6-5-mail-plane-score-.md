# 6.5 Mail plane (score 70)

- source canon: `3am-shinjitsu/arsenal-06-infra-hosting.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

## The technique

- SPF/DKIM/DMARC gaps (`dig TXT` all three) → spoofing exposure (document, don't send).
- Subdomain takeover: orphaned MX/CNAME to NXDOMAIN'd services = registration takeover
  executable same-day (verify the provider's "domain not found" page fingerprint).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
