# SPYDERMONKEY performance study — v5.18.0 "efficiency pass"

Measured on this host (Linux, Python 3.12.3, local SSD, warm page cache unless
labelled cold). Commands were timed with `/usr/bin/time`; figures are
representative medians of 2-3 runs, not synthetic microbenchmarks. The full
correctness gates stayed green: 63 tests, `ci_smoke` ALL PASS, ledger
integrity/dedupe, scope walls, engine walls.

## What was slow (and why)

| Path | Before | After | Lever |
|---|---:|---:|---|
| Module import | 0.19 s | 0.05 s | `urllib.request` / `tarfile` / `csv` only at call sites; lazy HTTP opener |
| Light CLI (`version`, `route`, `bench`) | 0.38-0.56 s | 0.20-0.29 s | removes ~140 ms of unused ssl/http/email import per process |
| MCP read-only tool call | 0.47-0.67 s | 1-30 ms warm (85 ms first) | in-process dispatch + cached argparse parser |
| Tester requests, demo range | 670 | 319 (238 unique) | shared memoized control baselines |
| Ledger add @ 10k rows | 0.89 s avg (1.74 s first) | 0.32 s | append-only new rows; rewrite only duplicates/legacy chains |
| `status` (engine verify) | ~5.2 s | ~0.3 s warm | successful verify cached by script mtime+size (10 min TTL) |
| `doctor` | 7.5 s warm / 23 s first observed | 0.7 s warm / 6.3 s cold | verify cache + in-process compile + 5x corpus walk |
| `skilltree --verify` | ~5.5 s | 1.1-1.6 s | `os.walk` + string relative paths instead of rglob/Path.relative_to |
| Test suite (`pytest -q`) | 37.9 s | 22.2 s | the startup + I/O wins above compound |

Cold means no engine-verify cache. The first-ever `doctor` run still pays the
ten real engine self-checks (~6 s); only repeated checks are cheap. `--refresh`
forces a live re-check, and failed checks are never cached.

## The changes

1. **Lazy heavy imports** (`scripts/spydermonkey.py`). `urllib.request` pulls
   ssl/http.client/email and initializes the cert store; `tarfile` pulls
   copy/email. Most commands never touch them. The HTTP opener is built on the
   first live request instead of at import.
2. **In-process MCP dispatch** (`scripts/mcp_server.py`). A long-lived MCP
   server now calls the dispatcher directly for offline/read-only tools
   (version, route, catalog, capabilities, ledger, scope, campaign, report,
   phases, next, chain, hypothesis gen/brief, status --fast, etc.). A cached
   parser removes ~25 ms per call. Commands that fire live traffic or can hang
   (testers, gate, mission, loop, fleet, arsenal run, scan, verify, doctor,
   selftest) still go through a subprocess with a hard timeout.
   `SPYDERMONKEY_MCP_INPROC=0` disables the fast path.
3. **Control-baseline memoization** (`cmd_testers`). Each unique baseline URL
   is fetched once as a stability pair, then reused by every payload in that
   tester and by every other tester that needs the same control. REPLAY still
   intentionally fires twice; POST/MASSASSIGN baselines are memoized too.
4. **Append-only ledger** (`_ledger_register`). New findings append one
   hash-chained row (`O_APPEND`, mode 0600) instead of re-reading/re-hashing
   /rewriting the whole JSONL. Duplicates and broken/legacy chains fall back to
   the rewrite path, so integrity and dedupe semantics are unchanged.
5. **Engine verify cache** (`_engine_status_all`). Successful engine
   self-checks are stored under `$SPYDERMONKEY_HOME/cache/engine-verify.json`,
   keyed by engine entry-script mtime and size. Failures are re-probed every
   time. `status --refresh` / `doctor --refresh` bypass the cache.
6. **Doctor and corpus walk** (`_doctor_compile`, `_doctor_skilltree`,
   `_doctor_mcp`, `skilltree.py`). Compile with the builtin `compile()` instead
   of six `py_compile` subprocesses; count 33k corpus files with `os.walk`;
   test the MCP surface by importing it; use `os.walk` plus a known prefix
   instead of `Path.rglob` + `Path.relative_to` (the latter is superlinear on
   Python 3.12).

## Remaining upside (ranked, with expected leverage)

1. **Bounded probe concurrency inside testers (2-4x wall on loopback).**
   Today 18 tester threads issue their payloads serially. A shared,
   `--concurrency N` executor (default conservative) would keep total requests
   identical but overlap latency; remote estates remain capped by the shared
   rate limiter. Keep REPLAY and state-changing POSTs serial.
2. **Ledger sidecar index (10x at 100k rows).** A `dedupe -> id` map plus the
   tail hash, validated against ledger size/mtime, turns duplicate detection
   into O(1) and removes the remaining full-file read per add. Rebuild the
   sidecar whenever the ledger changes out of band.
3. **Corpus search index (10-50x).** The 33,687-file / 139 MB corpus is only
   read one file at a time. A SQLite FTS index (or a single JSONL catalog)
   built by `skilltree --expand` would make technique search and citations
   instant and cut inode pressure; files stay as the lazy-load surface.
4. **Engine liveness mode (4x cold status).** `status` runs each engine's full
   `verify`. A `--fast-live` mode could import the engine or run `--version`
   plus a one-command smoke, reserving full verify for `verify`/`doctor
   --refresh`.
5. **Incremental doctor for campaigns.** At 43 campaigns it is fine; at
   hundreds, cache per-campaign JSON parse + ledger integrity by directory
   mtime and only re-check changed campaigns.
6. **MCP surface grouping (context efficiency).** 86 tools is a large tool
   schema for a model. A namespaced surface (`ledger.*`, `scope.*`,
   `arsenal.*`) or a `toolsets` capability would cut prompt tokens without
   reducing capability.
7. **Skip `site` for the stdlib-only CLI.** A `python3 -S` wrapper (or a
   console entrypoint) avoids ~70 ms of site/editable-install work per CLI
   process. This is environment-specific; test it before shipping.

## Reproduce

```bash
# cold vs warm engine checks (isolated cache)
SPYDERMONKEY_HOME=/tmp/sm-perf python3 scripts/spydermonkey.py doctor
SPYDERMONKEY_HOME=/tmp/sm-perf python3 scripts/spydermonkey.py doctor
python3 scripts/spydermonkey.py doctor --refresh

# MCP call latency (read-only tools)
printf '%s\n' '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"version","arguments":{}}}' \
  | python3 scripts/mcp_server.py

# request count / scan time
python3 scripts/spydermonkey.py testers --target perf --demo --json

# corpus verify
python3 scripts/skilltree.py --verify

# full gates
python3 -m pytest -q
bash scripts/ci_smoke.sh
```

## Note found during the study

The v5.17 HWDEV dojo class scores `surface=1 identify=1 confirm=0 detect=1`
in the public self-bench (63/64, 98.44%), not 100%. The IDOR battery sees the
swapped `id` and the body differential but its verdict requires `user/org/email`
style fields, so it records a hypothesis instead of CONFIRMED on a device
registry shape (`master_key`). That is a capability/verdict gap, not a
performance regression; it is left untouched here so this pass stays
behavior-preserving. A generic "sensitive object content served at the
original id" branch (or a sibling-id control) is the likely fix, then re-run
Range B to prove no false-positive inflation.
