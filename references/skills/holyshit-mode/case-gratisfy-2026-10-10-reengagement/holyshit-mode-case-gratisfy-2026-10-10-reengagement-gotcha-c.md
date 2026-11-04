# Gotcha: cargo env in heredoc scripts

- source canon: `holyshit-mode/case-gratisfy-2026-10-10-reengagement.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- generated: 2026-11-04

## The technique

source ~/.cargo/env in ~/.bashrc causes errors when writing Python via heredoc in terminal.
Use python3 directly or add 2>/dev/null after sourcing.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
