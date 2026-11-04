# Rate limits & rotation

- source canon: `holyshit-mode/supabase-gotrue-playbook.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-04

## The technique

Per-account ~6 req/min on media endpoints, but with phone_autoconfirm signup, rotation is trivial: mint fresh account on 429 (2s per account). Also retry "exhausted" upstream models on fresh accounts — some 429s are per-session.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
