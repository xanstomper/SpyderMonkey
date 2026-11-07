# Automated life: the report is the output of `scan` — iot-edge / machine

- source canon: `holyshit-mode/engagement-report-pattern.md`
- base technique: `holyshit-mode-engagement-report-pattern-automated-life-the-r.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **iot-edge** · auth **machine** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: device-adjacent runtime at the edge — own devices, lab network
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

With `HOLYSHIT_TARGET` exported, `holyshit.py scan <task>`:
1. **dispatches** to the models (`holyshit-inject`)
2. **converges** to CONFIRMED/BLOCKED/HYPOTHESIS (`holyconverge`)
3. **auto-persists** the outcome — confirmed → `holyleadger add confirmed` + `chain` (rc 0);
   blocked/exhausted → `holyleadger add hypothesis` (rc 1/3). No `HOLYSHIT_TARGET` → no-op
   (safety + makes offline harnesses deterministic).

So a confirmed finding is guaranteed to land in state (and appear in the next `report`)
with zero manual `add`. The report is thus always current after any `scan`.

## Probe adjustment (iot-edge × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
