# P. OBSERVABILITY / OPS — kubernetes / low-priv

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-p-observability-ops.md`
- bindings: **WSTG-INPV** · **CWE-74** · **ATT&CK T1190**
- context: **kubernetes** · auth **low-priv** · chain role **pivot**

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- Monitoring: Grafana/Prometheus anonymous access, alert-rule poisoning
- Logging: log-injection via crafted input, log-volume DoS on operator's own stack
- Tracing: Jaeger/Zipkin exposure, trace-context spoofing
- Alert fatigue: repetitive low-severity alerts masking real events (validate dedup logic)
- Status pages: information leakage in incident post-mortems, timeline metadata

## Probe adjustment (kubernetes × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
