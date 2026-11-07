# P. OBSERVABILITY / OPS — wasm / service

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-p-observability-ops.md`
- bindings: **WSTG-INPV** · **CWE-74** · **ATT&CK T1190**
- context: **wasm** · auth **service** · chain role **pivot**

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

- Monitoring: Grafana/Prometheus anonymous access, alert-rule poisoning
- Logging: log-injection via crafted input, log-volume DoS on operator's own stack
- Tracing: Jaeger/Zipkin exposure, trace-context spoofing
- Alert fatigue: repetitive low-severity alerts masking real events (validate dedup logic)
- Status pages: information leakage in incident post-mortems, timeline metadata

## Probe adjustment (wasm × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
