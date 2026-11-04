# Addendum — re-engage #5 (2026-10-06): proxy-fleet build + empty-content hardening

- source canon: `holyshit-mode/case-obsidian-y-api-dataplane.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

The operator shifted from recon to building a USABLE proxy over the unauth `/pg/chat` vector:
`~/obsidian-proxy/obsidian_proxy.py` (port 8620). This is the durable "wrap an unauth upstream
chat vector as a local OpenAI-compatible gateway" pattern (see SKILL.md "Free-AI proxy build
pattern"). Session added:

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
