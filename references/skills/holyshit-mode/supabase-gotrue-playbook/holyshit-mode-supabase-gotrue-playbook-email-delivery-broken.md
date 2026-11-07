# Email-delivery-broken targets

- source canon: `holyshit-mode/supabase-gotrue-playbook.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-07

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Confirm with mailinator public API: `https://www.mailinator.com/api/v2/domains/public/inboxes/<user>` (returns `{"msgs":[]}` — validate the API itself works against a known-active inbox like `test` before concluding). When mail is dead, pivot to attacking the verification check (sibling endpoints, handoff flows) rather than the mail path.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
