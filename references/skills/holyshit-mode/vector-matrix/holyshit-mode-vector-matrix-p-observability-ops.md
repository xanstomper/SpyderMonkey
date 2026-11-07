# P. OBSERVABILITY / OPS

- source canon: `holyshit-mode/vector-matrix.md`
- bindings: **WSTG-INPV** · **CWE-74** · **ATT&CK T1190**
- generated: 2026-11-04

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Monitoring: Grafana/Prometheus anonymous access, alert-rule poisoning
- Logging: log-injection via crafted input, log-volume DoS on operator's own stack
- Tracing: Jaeger/Zipkin exposure, trace-context spoofing
- Alert fatigue: repetitive low-severity alerts masking real events (validate dedup logic)
- Status pages: information leakage in incident post-mortems, timeline metadata

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
