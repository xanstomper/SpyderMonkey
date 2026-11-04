# What we could NOT test (operator credential required)

- source canon: `holyshit-mode/case-directrouter-pages-dev.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-04

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
