# MODULE 6 — AI-SPECIFIC EVASION — mesh / machine

- source canon: `holyshit-mode/detection-evasion-modules.md`
- base technique: `holyshit-mode-detection-evasion-modules-module-6-ai-specific.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **mesh** · auth **machine** · chain role **pivot**

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: service-mesh sidecar surface — own mesh, read-only mTLS posture
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

**Objective**: validate detection of AI-targeted attacks.

**Techniques**:
- **Prompt-injection obfuscation**: encode payloads in base64/rot13/unicode, split across
  turns, embed in markdown images. Validate: does the guardrail inspect decoded content or
  only surface strings?
- **Token-smuggling**: use homoglyphs, zero-width chars, or split tokens to evade keyword
  filters. Validate: does the filter normalize unicode or only ASCII?
- **Model-extraction pacing**: vary query timing and phrasing to avoid rate-limit-based
  extraction detection. Validate: does the API flag semantic similarity across queries or
  only volume?
- **Embedding inversion pacing**: query embeddings with noise, reconstruct via nearest-
  neighbor. Validate: does the system flag embedding-anomaly patterns or only direct text?

**Detection surface to report**: Guardrail/normalization coverage, semantic-similarity
analytics, API-abuse detection, embedding-anomaly baselines.

---

## Probe adjustment (mesh × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
