# Re-verification ladder (PTOK oracle first)

- source canon: `holyshit-mode/case-obsidian-y-api-reengage5-provider-wiring.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## The technique

- Target live, `/pg/chat` still unauth on BOTH hosts (Render + Vercel), `/v1/models` 200.
- **ling model now STATELESS** (ptok 26 constant across 4 identical requests) — the shared
  cross-user buffer from re-engage #2 is GONE on ling at least. longcat ptok still varies
  (3148→3019) but that's the live-timestamp in its injected Environment, not shared context.
  Prior score-85 shared-context + score-95 poisoning findings should be treated as LIKELY
  PATCHED until a fresh drift test proves otherwise. Finding decay confirmed empirically.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
