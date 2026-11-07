# P. OBSERVABILITY / OPS — iot-edge / high-priv

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-p-observability-ops.md`
- bindings: **WSTG-INPV** · **CWE-74** · **ATT&CK T1190**
- context: **iot-edge** · auth **high-priv** · chain role **pivot**

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: device-adjacent runtime at the edge — own devices, lab network
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- Monitoring: Grafana/Prometheus anonymous access, alert-rule poisoning
- Logging: log-injection via crafted input, log-volume DoS on operator's own stack
- Tracing: Jaeger/Zipkin exposure, trace-context spoofing
- Alert fatigue: repetitive low-severity alerts masking real events (validate dedup logic)
- Status pages: information leakage in incident post-mortems, timeline metadata

## Probe adjustment (iot-edge × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
