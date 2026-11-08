# Findings — vllm-oss-hunt

_generated 2026-11-08T20:02:29.017536+00:00 · 1 finding(s)_

| id | severity | cvss | status | class | title | asset |
|---|---|---|---|---|---|---|
| SPY-001 | critical | 9.5 | CONFIRMED | DESERIALIZATION | Unauthenticated pickle deserialization on the torch.distributed object channel (third recurrence of the vLLM pickle-RCE class) | vllm/distributed/parallel_state.py:960 + vllm/distributed/utils.py:332 |
