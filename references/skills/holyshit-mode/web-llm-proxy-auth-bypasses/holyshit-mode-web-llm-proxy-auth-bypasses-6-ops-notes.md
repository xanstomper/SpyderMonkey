# 6. Ops notes

- source canon: `holyshit-mode/web-llm-proxy-auth-bypasses.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-04

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Cloudflare 1010 blocks python-urllib UA; use curl with browser UA + Origin/apikey headers.
- Mailinator API (`/api/v2/domains/public/inboxes/<user>`) works for inbox checks, but when
  target SMTP is broken nothing arrives — don't retry the email path, pivot.
- Blocked by broken mailer: email change verify, recovery, magic link — all silent.
- Ledger: record score ≥80 findings via holyleadger `confirmed`; statuses are only
  confirmed/inconclusive/hypothesis/negative (no `disclosure` status).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
