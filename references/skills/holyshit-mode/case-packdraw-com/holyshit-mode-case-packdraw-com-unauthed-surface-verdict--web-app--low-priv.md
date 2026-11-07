# Unauthed-surface verdict — web-app / low-priv

- source canon: `holyshit-mode/case-packdraw-com.md`
- base technique: `holyshit-mode-case-packdraw-com-unauthed-surface-verdict.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **web-app** · auth **low-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- Thin by design: SSR-only product data (full odds tables public = fine), checkpoint +
  reCAPTCHA on all interactive planes, realtime gated. No unauth data plane leak found.
- Negatives: /api/pusher/auth 403; tokenize config 404 GET; /pusher/* ghosts; VM fully
  checkpoint-walled; wayback has HTML shells only (NO JS chunks archived — bundle mining
  there is a dead end; 2026 shell = current-ish build references only); Elavon/Tokex
  vendor config untested.

## Probe adjustment (web-app × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
