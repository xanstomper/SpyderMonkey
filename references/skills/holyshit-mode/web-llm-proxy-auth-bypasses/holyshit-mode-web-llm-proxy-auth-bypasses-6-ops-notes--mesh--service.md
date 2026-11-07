# 6. Ops notes — mesh / service

- source canon: `holyshit-mode/web-llm-proxy-auth-bypasses.md`
- base technique: `holyshit-mode-web-llm-proxy-auth-bypasses-6-ops-notes.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **mesh** · auth **service** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: service-mesh sidecar surface — own mesh, read-only mTLS posture
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

- Cloudflare 1010 blocks python-urllib UA; use curl with browser UA + Origin/apikey headers.
- Mailinator API (`/api/v2/domains/public/inboxes/<user>`) works for inbox checks, but when
  target SMTP is broken nothing arrives — don't retry the email path, pivot.
- Blocked by broken mailer: email change verify, recovery, magic link — all silent.
- Ledger: record score ≥80 findings via holyleadger `confirmed`; statuses are only
  confirmed/inconclusive/hypothesis/negative (no `disclosure` status).

## Probe adjustment (mesh × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
