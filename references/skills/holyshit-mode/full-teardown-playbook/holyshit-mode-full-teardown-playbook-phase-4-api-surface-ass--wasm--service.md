# PHASE 4 — API SURFACE ASSAULT (read-only oracles) — wasm / service

- source canon: `holyshit-mode/full-teardown-playbook.md`
- base technique: `holyshit-mode-full-teardown-playbook-phase-4-api-surface-ass.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **wasm** · auth **service** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

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
