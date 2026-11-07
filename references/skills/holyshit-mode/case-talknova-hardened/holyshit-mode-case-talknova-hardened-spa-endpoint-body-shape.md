# SPA endpoint + body-shape mining (minified bundle)

- source canon: `holyshit-mode/case-talknova-hardened.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

1. `grep -oE '"/[a-zA-Z0-9_/.-]{2,60}"' app.js | sort -u` → route + endpoint list.
2. All fetch calls: `grep -oE 'fetch\("[a-z0-9/_-]+"' app.js | sort -u`.
3. Body shapes live at CALL SITES of the wrapper fn, not the fetch itself — find the wrapper
   (e.g. `async function Y8(e,t){fetch("/api/chat"...}`), then grep its callers:
   `grep -oE 'Y8\(\{[^}]{0,150}' app.js` → reveals real body keys (`{modelId, message}` not
   the guessed `{model, messages}`). Server error strings are the oracle.
4. **Code-split chunk discovery**: `grep -oE '"\./[A-Za-z0-9_-]+\.js"' app.js` → fetch each chunk, mine for endpoints.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
