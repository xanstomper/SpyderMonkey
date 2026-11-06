# The loop that passes cleanly — chain composition

- source canon: `holyshit-mode/adhoc-verification-loop.md`
- base technique: `holyshit-mode-adhoc-verification-loop-the-loop-that-passes-c.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

1. Write the verify script via `write_file` (path: `/tmp/hermes-verify-<subject>.py`). It must:
   - `py_compile` the changed file first (catches syntax/lint-class breaks in one shot).
   - Build a **synthetic fixture** for any decoder/protocol logic and assert roundtrips + domain sanity (e.g. decoded coords land in the known geographic/event window).
   - Run the actual artifact end-to-end if it's network/live: `subprocess.run(["timeout", "12", sys.executable, script], capture_output=True, text=True)`.
   - Print `ad-hoc verification: N passed, M failed` and `sys.exit(1 if FAIL else 0)`.
2. Run it via `terminal`; capture `exit=0`.
3. **Keep the verify script on disk** if the system prompt re-fires on the same file — deleting it makes the next flag appear stale. Re-running the same script is the honest fix.
4. Summarize as: "Ad-hoc verification passed: N/N, exit 0 (not a suite green — no canonical test config)". Never say "tests pass" or claim suite coverage.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
