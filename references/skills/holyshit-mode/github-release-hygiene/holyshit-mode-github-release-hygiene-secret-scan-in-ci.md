# Secret Scan in CI

- source canon: `holyshit-mode/github-release-hygiene.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- generated: 2026-11-04

## The technique

The workflow greps for `sk-[a-z0-9]{20,}`, `gho_[a-z0-9]{20,}`, `api_key = '<20+ chars>'`,
`Bearer <20+ chars>` on every push. Exclusions: `.env.example` (placeholder values only)
and env-var NAMES like `HOLYSHIT_API_KEY` (no value).

**Rule:** never put real key material in any repo file, even "temporarily". CI catches it.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
