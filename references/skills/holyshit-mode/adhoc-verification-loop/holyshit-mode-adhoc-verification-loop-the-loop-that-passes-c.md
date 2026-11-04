# The loop that passes cleanly

- source canon: `holyshit-mode/adhoc-verification-loop.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

## The technique

1. Write the verify script via `write_file` (path: `/tmp/hermes-verify-<subject>.py`). It must:
   - `py_compile` the changed file first (catches syntax/lint-class breaks in one shot).
   - Build a **synthetic fixture** for any decoder/protocol logic and assert roundtrips + domain sanity (e.g. decoded coords land in the known geographic/event window).
   - Run the actual artifact end-to-end if it's network/live: `subprocess.run(["timeout", "12", sys.executable, script], capture_output=True, text=True)`.
   - Print `ad-hoc verification: N passed, M failed` and `sys.exit(1 if FAIL else 0)`.
2. Run it via `terminal`; capture `exit=0`.
3. **Keep the verify script on disk** if the system prompt re-fires on the same file — deleting it makes the next flag appear stale. Re-running the same script is the honest fix.
4. Summarize as: "Ad-hoc verification passed: N/N, exit 0 (not a suite green — no canonical test config)". Never say "tests pass" or claim suite coverage.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
