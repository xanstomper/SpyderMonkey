# Exfiltrated Data — firmware / federated

- source canon: `holyshit-mode/case-freeinference-org.md`
- base technique: `holyshit-mode-case-freeinference-org-exfiltrated-data.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **firmware** · auth **federated** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- **Nodes (4)**: h200a, h200b, rtx6000b, spark2 — all online
- **GPUs (11)**: H100/H200 + RTX 6000B, with utilization curves
- **Inference Servers (6)**: deepseek-v4-flash, glm-5.3-flash, Qwen3.3-35B, diffusiongemma-26B, bge-m3
- **Live Metrics (13,027 data points)**:
  - 6,548 GPU telemetry points (memory %, temp °C, power W, PCIe/NVLink bandwidth)
  - 3,942 sglang request metrics (throughput, cache-hit rate, TTFT, speculation ratio)
  - 2,537 CPU utilization samples
- **Traffic Volumes**: 
  - Day: 277,985 requests, 20.5B cache tokens, 793M prefill tokens, 121M decode tokens
  - Hour: 5,853 requests, 744M cache tokens

## Probe adjustment (firmware × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
