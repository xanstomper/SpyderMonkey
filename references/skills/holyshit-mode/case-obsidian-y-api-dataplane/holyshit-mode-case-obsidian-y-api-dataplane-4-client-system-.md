# 4. Client `system` role honored on `/pg/chat` (score 45)

- source canon: `holyshit-mode/case-obsidian-y-api-dataplane.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-04

## The technique

Sending `{"role":"system","content":"..."}` in messages works — prompt_tokens jumps 6→19 (system
message added). Client controls the LLM's system context behind the untrusted proxy.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
