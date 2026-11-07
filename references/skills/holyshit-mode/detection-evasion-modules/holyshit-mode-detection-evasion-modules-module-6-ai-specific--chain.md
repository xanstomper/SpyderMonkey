# MODULE 6 — AI-SPECIFIC EVASION — chain composition

- source canon: `holyshit-mode/detection-evasion-modules.md`
- base technique: `holyshit-mode-detection-evasion-modules-module-6-ai-specific.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
