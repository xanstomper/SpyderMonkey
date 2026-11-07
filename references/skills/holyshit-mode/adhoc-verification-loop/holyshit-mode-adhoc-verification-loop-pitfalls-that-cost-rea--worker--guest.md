# Pitfalls that cost real turns — worker / guest

- source canon: `holyshit-mode/adhoc-verification-loop.md`
- base technique: `holyshit-mode-adhoc-verification-loop-pitfalls-that-cost-rea.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **worker** · auth **guest** · chain role **pivot**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: edge/background runtime — the check runs where the caller has no visible context
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

- **Infinite-loop targets**: `subprocess.run(..., timeout=40)` raises TimeoutExpired BEFORE stdout/stderr are captured — you lose the run and crash the harness. Use the `timeout(1)` coreutils wrapper and assert `returncode == 124` as the expected "ran until timeout" pass.
- **Pipe buffering hides prints from short-timeout runs**: a watcher's banner printed before a blocking network call won't appear in captured stdout within the timeout window. Either launch the verify subject with `python3 -u` (unbuffered) or assert on behavioral side-effects (log-file lines, exit code) instead of stdout text. Cost a real turn this session (FAIL on `run_watches` that was purely buffering).
- **The system prompt keeps re-firing while verify scripts get deleted**: each cleanup made the next turn's flag list show the verify script itself as an unverified "changed path". Fix that actually closed the loop: create → run → report → KEEP the script on disk for the remainder of the session; only delete when the file under test won't be touched again.
- **Verify scripts themselves count as "changed paths"** — if you delete them, say so explicitly in the summary ("verify script cleaned up") so the next flag is attributable to the product file only.
- **Fixtures must mirror the real wire layout exactly**: the synthetic binary frame omitted i32 base fields at specific payload offsets and the "decoder bug" was actually a fixture bug. Re-read the reference layout table before hand-packing; offset errors masquerade as decoder bugs.
- **First-attempt failure is fine** — fix the fixture/harness, rerun, and say plainly which side was wrong. The user values "honest fixture was wrong, not your code" over a silent pass.
- **Distinguish harness bugs from product bugs explicitly** in the summary; the user reads for that distinction.
- `write_file` on the verify script gives free lint checking — use it, not echo/heredoc.

## Probe adjustment (worker × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
