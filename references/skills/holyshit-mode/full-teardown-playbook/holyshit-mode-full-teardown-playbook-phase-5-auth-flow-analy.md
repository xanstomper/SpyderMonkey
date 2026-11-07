# PHASE 5 — AUTH & FLOW ANALYSIS

- source canon: `holyshit-mode/full-teardown-playbook.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- **Session model**: where tokens live (cookie vs localStorage), flags (HttpOnly/Secure/
  SameSite), rotation on privilege change, fixation vectors, ?token= URL params (HOLY SHIT:
  session fixation via referrer/history).
- **OAuth flows**: state validation, redirect_uri validation, token-in-fragment leakage,
  PKCE enforcement.
- **Password/account flows**: enumeration via response/timing divergence, reset-token
  entropy and single-use enforcement.
- **Verification gates**: server-side verification or stateless claim gate? (hash-verify →
  empty-body claim + no server-to-server callback = farm hypothesis; CVSS ~7.5 documented).
- Deliverable: session/OAuth/reset findings, stateless-verification hypotheses.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
