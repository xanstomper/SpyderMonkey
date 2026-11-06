# Fleet probe discipline

- source canon: `holyshit-mode/case-obsidian-y-api-dataplane.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- generated: 2026-11-04

## The technique

Before wiring anything, live-probe EVERY model in `/v1/models` in parallel (submit with a
`tools` payload). Output per model: does it return real content? does it emit native
`tool_calls`? what `served_by` shows. On obsidian: 30/38 models live, 27 with native
tool-calling — the fleet is mixed. Models that live-probe 502 / empty get pruned, not assumed.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
