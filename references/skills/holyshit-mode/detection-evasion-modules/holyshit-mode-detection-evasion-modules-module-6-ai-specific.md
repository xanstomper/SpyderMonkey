# MODULE 6 — AI-SPECIFIC EVASION

- source canon: `holyshit-mode/detection-evasion-modules.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-04

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
