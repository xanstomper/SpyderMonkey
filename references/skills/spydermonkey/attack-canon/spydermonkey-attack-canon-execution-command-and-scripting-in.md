# Execution Command and Scripting Interpreter (T1059)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **WSTG-INPV** · **CWE-74** · **ATT&CK T1190**
- generated: 2026-11-04

## The technique

- class: shell/powershell/python interpreters as the execution primitive
- probe: the cmd-injection battery (`;id`, `$(id)`, backticks) — echo differential only
- wall: proof = a benign marker echoed; never a destructive command

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
