# 6c. CONFIRMED — Modal serverless GPU endpoint leak in catalog (score 45) — chain composition

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- base technique: `holyshit-mode-case-experientiallabs-ai-6c-confirmed-modal-se.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Staging catalog exposes a **Modal endpoint**: `hy4-preview` →
  `https://bespoke-ai-agents--explabs-ec-hy4-preview-hy4preview.us-east.modal.direct/v1`.
- Currently **scale-to-zero** (503 `no upstreams available` → no live container). If it wakes with open
  auth it's a free-GPU surface; Modal functions usually have web-auth unless misconfigured.
- **IMPACT:** Internal serving infra URL disclosed in the public keyless catalog; potential free-GPU if
  the function is authless. Recon primarily.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
