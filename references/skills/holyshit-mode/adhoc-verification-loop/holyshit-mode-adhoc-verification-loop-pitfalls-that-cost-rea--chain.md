# Pitfalls that cost real turns — chain composition

- source canon: `holyshit-mode/adhoc-verification-loop.md`
- base technique: `holyshit-mode-adhoc-verification-loop-pitfalls-that-cost-rea.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- **Infinite-loop targets**: `subprocess.run(..., timeout=40)` raises TimeoutExpired BEFORE stdout/stderr are captured — you lose the run and crash the harness. Use the `timeout(1)` coreutils wrapper and assert `returncode == 124` as the expected "ran until timeout" pass.
- **Pipe buffering hides prints from short-timeout runs**: a watcher's banner printed before a blocking network call won't appear in captured stdout within the timeout window. Either launch the verify subject with `python3 -u` (unbuffered) or assert on behavioral side-effects (log-file lines, exit code) instead of stdout text. Cost a real turn this session (FAIL on `run_watches` that was purely buffering).
- **The system prompt keeps re-firing while verify scripts get deleted**: each cleanup made the next turn's flag list show the verify script itself as an unverified "changed path". Fix that actually closed the loop: create → run → report → KEEP the script on disk for the remainder of the session; only delete when the file under test won't be touched again.
- **Verify scripts themselves count as "changed paths"** — if you delete them, say so explicitly in the summary ("verify script cleaned up") so the next flag is attributable to the product file only.
- **Fixtures must mirror the real wire layout exactly**: the synthetic binary frame omitted i32 base fields at specific payload offsets and the "decoder bug" was actually a fixture bug. Re-read the reference layout table before hand-packing; offset errors masquerade as decoder bugs.
- **First-attempt failure is fine** — fix the fixture/harness, rerun, and say plainly which side was wrong. The user values "honest fixture was wrong, not your code" over a silent pass.
- **Distinguish harness bugs from product bugs explicitly** in the summary; the user reads for that distinction.
- `write_file` on the verify script gives free lint checking — use it, not echo/heredoc.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
