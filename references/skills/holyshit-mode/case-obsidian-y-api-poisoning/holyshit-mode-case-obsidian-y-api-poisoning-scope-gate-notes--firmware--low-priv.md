# Scope-gate notes — firmware / low-priv

- source canon: `holyshit-mode/case-obsidian-y-api-poisoning.md`
- base technique: `holyshit-mode-case-obsidian-y-api-poisoning-scope-gate-notes.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **firmware** · auth **low-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- Operator demanded "destructive level" holy shits → refused (bill-drain/DoS on third-party prod = sabotage). Clarified to read-only → everything above proven with ~10 requests total, no abuse. Free-AI reported as bill-drain RISK, never demonstrated by draining.
- Operator then claimed ownership ("this is my app and inference") → treated as authorized finding report; probes stayed non-destructive regardless; takeover-style "for control" actions still not run without verifiable infra proof.

## Probe adjustment (firmware × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
