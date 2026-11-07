# Exploit-Catalog Maintenance (example-target `opensleuth/exploits.py` truth system) — ios / service

- source canon: `holyshit-mode/lessons-2026-10-06-example-target-catalog.md`
- base technique: `holyshit-mode-lessons-2026-10-06-example-target-catalog-expl.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **ios** · auth **service** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

- **Zero-click/wild-chain class is the BFU layer that local-exploit catalogs miss.** The only
  demonstrated passcode-bypass-adjacent primitives on A12+ arrived as zero-click delivery chains:
  FORCEDENTRY (CVE-2021-30860), BLASTPASS (CVE-2023-41061/41064), Operation Triangulation
  (CVE-2023-41990/41991/38606/32434/38599), KISMET (CVE-2025-24085), CVE-2024-23225/23296,
  CVE-2025-31200/31201, CVE-2024-44308/09. Catalog as a distinct `zero-click` layer with per-entry
  public attribution (Citizen Lab / Google TAG / Kaspersky / Apple advisories) and DOCUMENTED-only
  status — no public tooling exists for any; entries must say so. Fabricated executors are exactly
  the failure the integrity rule forbids.
- **iOS-window format invariant bites immediately:** catalog tests assert every `ios` field parses
  to a version range. Free-text `"14.x (patched 14.7...; design fixed in 15.x)"` parses to nothing —
  write `"14.0-14.6, 14.8-14.8.1 (patched 14.7; design fixed in 15.x)"`. Run the invariant tests
  immediately after insertion.
- **Chip-name matching is case/alias-trappy:** entries store mixed-case `"A17 Pro"` while
  `routes_for` uppercases the query → 0 results. Fix with case-insensitive superset match:
  `chip == str(c).upper() or chip in str(c).upper() or str(c).upper() in chip`.
- **CI red-for-weeks is itself a finding:** `gh run list` showed the repo red since September —
  nobody checked. On any push, watch the run to conclusion (`gh run watch <id> --exit-status`)
  before claiming green. Fix infra failures with per-package apt fallbacks
  (`for pkg in a b; do apt-get install -y "$pkg" || echo "skip $pkg"; done`) so one package rename
  can't kill the step. CI-exposed failures (error-check ordering in `icloud.acquire`, a
  missing-binary crash killing the acquire journal thread in `studio_web/server.py`) were REAL
  product bugs, not harness artifacts — triage before dismissing.
- **`terminal`-piped V4A patch content fails** ("Only garbage was found") — use the `patch` tool
  with mode=replace, or Python string-replace in a heredoc for multi-line inserts into large Python
  literal lists.

## Probe adjustment (ios × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
