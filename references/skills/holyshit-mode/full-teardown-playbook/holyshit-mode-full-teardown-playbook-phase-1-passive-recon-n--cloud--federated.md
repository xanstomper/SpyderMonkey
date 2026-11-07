# PHASE 1 — PASSIVE RECON (no target contact) — cloud / federated

- source canon: `holyshit-mode/full-teardown-playbook.md`
- base technique: `holyshit-mode-full-teardown-playbook-phase-1-passive-recon-n.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **cloud** · auth **federated** · chain role **entry**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- **Certificate transparency**: crt.sh / censys on `%.target.tld` — subdomains the operator forgot.
- **ASN/whois**: netblocks, hosting provider, named orgs, corporate acronyms.
- **Wayback CDX**: `/cdx/search/cdx?url=<host>*&output=json&collapse=urlkey` — full asset
  history. Old bundles, .well-known/, old ?v= query strings, deleted pages.
- **Search-engine dorking**: site:, filetype:, inurl: — exposed configs, dumps, admin panels.
- **GitHub/org leak hunting**: API keys, internal hostnames, CI configs, .env patterns in
  operator-visible repos and gists referencing the target.
- **Artifact-first**: operator's own vault/notes/baselines before anything else.
- Deliverable: target map + forgotten-asset list. Forgotten assets = highest-yield entry.

## Probe adjustment (cloud × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
