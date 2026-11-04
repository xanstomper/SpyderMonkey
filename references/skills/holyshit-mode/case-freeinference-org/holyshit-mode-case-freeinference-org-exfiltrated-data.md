# Exfiltrated Data

- source canon: `holyshit-mode/case-freeinference-org.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-04

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
