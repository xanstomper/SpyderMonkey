# Evidence-chain rules — iot-edge / low-priv

- source canon: `shukaku/harvest-playbook.md`
- base technique: `shukaku-harvest-playbook-evidence-chain-rules.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **iot-edge** · auth **low-priv** · chain role **pivot**

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: device-adjacent runtime at the edge — own devices, lab network
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

1. Every crown entry: `SOURCE → PROOF → SCOPE → CLASS → VALUE → DISCLOSE`.
2. SOURCE must be a real finding ID (3AM chain, case file, ledger entry) — a harvest
   entry with no source is a fabrication.
3. PROOF must be reproducible read-only (command ref, output hash reference).
4. SCOPE is counts, never contents; samples ≤3, redacted, hashed.
5. VALUE carries basis; DISCLOSE carries the obligation + timeline + prerequisite.
6. Re-verify reach before re-asserting (drift first; findings decay).

## Probe adjustment (iot-edge × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
