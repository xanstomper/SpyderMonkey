# The loop that passes cleanly — api / unauth

- source canon: `holyshit-mode/adhoc-verification-loop.md`
- base technique: `holyshit-mode-adhoc-verification-loop-the-loop-that-passes-c.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **api** · auth **unauth** · chain role **pivot**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

1. Write the verify script via `write_file` (path: `/tmp/hermes-verify-<subject>.py`). It must:
   - `py_compile` the changed file first (catches syntax/lint-class breaks in one shot).
   - Build a **synthetic fixture** for any decoder/protocol logic and assert roundtrips + domain sanity (e.g. decoded coords land in the known geographic/event window).
   - Run the actual artifact end-to-end if it's network/live: `subprocess.run(["timeout", "12", sys.executable, script], capture_output=True, text=True)`.
   - Print `ad-hoc verification: N passed, M failed` and `sys.exit(1 if FAIL else 0)`.
2. Run it via `terminal`; capture `exit=0`.
3. **Keep the verify script on disk** if the system prompt re-fires on the same file — deleting it makes the next flag appear stale. Re-running the same script is the honest fix.
4. Summarize as: "Ad-hoc verification passed: N/N, exit 0 (not a suite green — no canonical test config)". Never say "tests pass" or claim suite coverage.

## Probe adjustment (api × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
