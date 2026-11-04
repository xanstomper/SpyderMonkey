# 1. GoTrue redirect_uri full override — CONFIRMED (score 85)

- source canon: `holyshit-mode/case-gratisfy-2026-10-10-reengagement.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

GET /auth/v1/authorize?provider=discord&redirect_uri=<attacker_url forwards attacker URI verbatim to Discord OAuth. No HTTPS enforcement, no path normalization.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
