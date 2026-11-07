# PHASE 4 — API SURFACE ASSAULT (read-only oracles)

- source canon: `holyshit-mode/full-teardown-playbook.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- **405-matrix route verification**: wrong-method everything; real routes answer 405,
  ghosts answer 200 text/html. Build the true endpoint map.
- **Auth-seam taxonomy**: classify 401/403 error strings per endpoint — diverging strings =
  separate auth layers = prime bypass candidates.
- **IDOR/BOLA sweep**: on any owned test account, enumerate object IDs on every GET.
  Cross-tenant probes only with a second test account, never production users' data.
- **Type-coercion probes**: object-where-string (`{"param":{"a":1}}`), array smuggling,
  null/absent-field variation. Watch for 500s (disclose class) AND rate-limit dodges.
- **Rate-limit scope mapping**: which endpoints limited, per-IP keying basis, IPv4 vs IPv6
  pools, malformed-payload counting.
- **Mass assignment**: send extra fields (is_admin, role, credits, price) on POST/PUT to
  owned accounts — watch for acceptance.
- **GraphQL**: introspection enabled? depth/alias abuse, field-level auth gaps.
- Deliverable: true route map, seam-classified auth, coercion/500 classes, IDOR/assignment findings.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
