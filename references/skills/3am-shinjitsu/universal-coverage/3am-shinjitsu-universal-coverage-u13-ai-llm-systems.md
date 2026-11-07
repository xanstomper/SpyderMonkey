# U13 AI & LLM systems

- source canon: `3am-shinjitsu/universal-coverage.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- [ ] Data flows, tool permissions, network egress, and tenant boundaries mapped
- [ ] Prompt isolation, RAG document permissions, and cross-user context leakage reviewed
- [ ] Agent actions require explicit authorization and have audit/rollback
- [ ] Model/gateway routing, keys, budgets, and logging reviewed
- [ ] Output used for execution/authorization is independently validated

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
