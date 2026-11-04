# 6c. CONFIRMED — Modal serverless GPU endpoint leak in catalog (score 45) — container / unauth

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- base technique: `holyshit-mode-case-experientiallabs-ai-6c-confirmed-modal-se.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **container** · auth **unauth** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- Staging catalog exposes a **Modal endpoint**: `hy4-preview` →
  `https://bespoke-ai-agents--explabs-ec-hy4-preview-hy4preview.us-east.modal.direct/v1`.
- Currently **scale-to-zero** (503 `no upstreams available` → no live container). If it wakes with open
  auth it's a free-GPU surface; Modal functions usually have web-auth unless misconfigured.
- **IMPACT:** Internal serving infra URL disclosed in the public keyless catalog; potential free-GPU if
  the function is authless. Recon primarily.

## Probe adjustment (container × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
