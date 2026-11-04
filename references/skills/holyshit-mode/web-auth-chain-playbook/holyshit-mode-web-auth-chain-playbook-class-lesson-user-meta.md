# Class lesson: user_metadata persistence ≠ authorization

- source canon: `holyshit-mode/web-auth-chain-playbook.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

Admin-claim injection into JWT `user_metadata` (role/is_admin/credits persist verbatim through
phone signup) is a finding only if a BACKEND endpoint trusts the claim. gratisfy.xyz's backend
gates on its own DB (`profiles.email_verified` middleware on all /api/account/*) — dead end
despite full claim persistence. Locate the real gate before scoring JWT-claim escalation.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
