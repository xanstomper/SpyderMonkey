# What we could NOT test (operator credential required) — cloud / unauth

- source canon: `holyshit-mode/case-directrouter-pages-dev.md`
- base technique: `holyshit-mode-case-directrouter-pages-dev-what-we-could-not-.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **cloud** · auth **unauth** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

1. **Discord session** → test `/api/keys` IDOR (can user A revoke user B's keys?),
   `/v1/chat/completions` plan-tier tampering (does a free user get Frontier models?),
   `/api/redeem` code abuse (brute-force short codes, replay redemption),
   `/api/auth/membership` bypass (already Discord-gated; confirm the gate is server-side,
   not client-side only).
2. **Admin Bearer** → test `/api/admin/*` full surface: `/api/admin/users` PATCH privilege
   escalation, `/api/admin/grants` IDOR, `/api/admin/custom-keys` PATCH mass-assignment
   (top-up balance via crafted body), `/api/admin/routes` router poisoning.

The agent offered to bootstrap a Discord account via mail.tm disposable email + Playwright
automation. The operator declined ("no u dont"). This is the correct outcome — the
doctrine explicitly forbids credential self-bootstrapping. Engagement closed at the wall
with the 3 pre-auth findings as the publishable result. The HIGH-severity PII dump alone
is a defensible engagement deliverable without the post-auth kill chain.

## Probe adjustment (cloud × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
