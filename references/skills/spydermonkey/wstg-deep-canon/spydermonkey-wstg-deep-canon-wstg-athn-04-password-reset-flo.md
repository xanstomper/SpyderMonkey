# WSTG-ATHN-04 Password Reset Flow

- source canon: `spydermonkey/wstg-deep-canon.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-04

## The technique

- class: predictable reset tokens, host-header poisoning of reset links
- probe: request TWO resets on the lab replica, diff token entropy; replay the Host header
- wall: lab replica only — no real reset emails are ever triggered

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
