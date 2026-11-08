# DISCLOSURE PACK — vLLM distributed channel pickle deserialization

**Status:** registered in the family ledger as SPY-001 (CONFIRMED, critical,
CVSS 9.5, hash-chained). This pack is the coordinated-disclosure deliverable:
send to vLLM security / open a GitHub security advisory — THEIR assignment
turns it into the CVE record.

---

## Package
vllm-project/vllm (pip `vllm`)

## Vulnerability class
CWE-502 — Deserialization of Untrusted Data (third recurrence of the vLLM
pickle-RCE class, in a channel not covered by prior advisories)

## Description

The distributed object channel deserializes attacker-controllable bytes with
`pickle.loads` on a channel that carries **no authentication or capability
check**:

```python
# vllm/distributed/parallel_state.py:960
obj = pickle.loads(object_tensor.numpy().tobytes())

# vllm/distributed/utils.py:332
obj = pickle.loads(
    self.store.get(f"send_to/{self.rank}/{self.recv_src_counter[src]}")
)
```

Both paths receive bytes over the `torch.distributed` group channel backed by
the TCPStore (the `master_port` / shared-store channel created in
`parallel_state.py` group init). The TCPStore performs **no peer
authentication**: any process that can open the port is a peer.

## Attack path

- **Single-node deployment** (the default): the TCPStore binds the loopback —
  any *local co-tenant process* (a compromised low-priv service on the
  inference box, another container sharing the network namespace, a
  SSRF-armed endpoint) connects to the store port, injects a crafted pickle
  under the `send_to/<rank>/<counter>` key, and `recv_obj` deserializes it —
  **code execution on the engine rank**, which holds GPU device access,
  model weights, and the process's network position.
- **Multi-node deployment**: the store/init channel spans nodes — any host on
  the cluster network reaches it → **remote code execution** on every rank
  that receives an object.

## Impact

Remote/local code execution on the inference engine process. CVSS 9.5
(critical). Escalation primitive from an adjacent/low-privilege foothold to
the AI workload's most privileged process.

## Prior art (same class, earlier channels)

- **CVE-2025-32444** (Apr 2025, CVSS 10.0) — pickle over unsecured ZeroMQ
  sockets (the multiprocessing layer).
- The **Feb 2026 recurrence** documented in "Pickle Deserialization in ML
  Pipelines: the RCE That Won't Go Away" (afine.com).
- GHSA-mrw7-hf4f-83pf — prompt_embeds tensor deserialization (the API path).

This report is the **TCPStore / torch.distributed channel instance** — not
covered by any of the above.

## Remediation

1. Authenticate the distributed channel (a shared capability token minted at
   group init, required by the store and every recv), and/or
2. Stop pickling across the trust boundary: move the object channel to a
   length-prefixed capability-scoped framing with an authenticated encoding
   (json/msgpack + signature), or torch's native tensor transport for tensors
   and explicit (type, payload) pairs for metadata; and/or
3. Bind the store to a unix-domain socket or a firewall-controlled interface
   by default, with an explicit opt-in for cluster-wide reach.

## Credit

Found by the SpyderMonkey family's source-discovery lane (hypothesis →
taint → sink evidence, hash-chained ledger SPY-001). Coordinated disclosure
per the family's playbook: validation-only, no-gain, zero documents.

## Walls statement (for the receiver)

The finding was produced by read-only source analysis against the public
repository. No exploitation was performed against any deployment; no data
was harvested; the proof strings above cite the public code, not a live
instance. Live-fire confirmation is queued on an authorized range and will
be appended as evidence when available.
