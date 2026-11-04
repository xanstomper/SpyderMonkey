# 1.8 Mirror/entrance brands (score 70)

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- bindings: **WSTG-ATHN-04** · **CWE-307** · **ATT&CK T1110**
- generated: 2026-11-04

## The technique

- PATTERN: `tr.<brand>`, `giris.<brand>` (TR entrance pattern), `<lang>.<brand>`,
  `<brand>-<market>` — separate hosting from CT logs + passive DNS.
- CONFIRMED WHEN: mirror on different ASN/IP-family than main = un-CDN'd, un-WAF'd surface.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
