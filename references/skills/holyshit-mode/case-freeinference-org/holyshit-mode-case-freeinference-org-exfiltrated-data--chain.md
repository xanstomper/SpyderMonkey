# Exfiltrated Data — chain composition

- source canon: `holyshit-mode/case-freeinference-org.md`
- base technique: `holyshit-mode-case-freeinference-org-exfiltrated-data.md`
- chain role: **final — this CLOSES a chain: shukaku prices what it reaches; chain detect looks for the entries that feed it**

## Chain roles

- final — this CLOSES a chain: shukaku prices what it reaches; chain detect looks for the entries that feed it

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
