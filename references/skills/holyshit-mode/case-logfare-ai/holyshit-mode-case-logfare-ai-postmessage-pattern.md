# postMessage Pattern

- source canon: `holyshit-mode/case-logfare-ai.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- generated: 2026-11-04

## The technique

- Callback uses: `window.opener.postMessage(data, window.location.origin)`
- This is CORRECT (targets sender origin)
- Not a vulnerability

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
