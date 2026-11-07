# PHASE 1 — PASSIVE RECON (no target contact)

- source canon: `holyshit-mode/full-teardown-playbook.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
