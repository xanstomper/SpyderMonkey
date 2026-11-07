# Custom admin panels (React-rebuilt on legacy control planes)

- source canon: `holyshit-mode/web-integrity-masking-leaks.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Mine the panel's OWN client bundle for the full custom API surface — a
  React rebuild exposes paths the stock panel never had
  (`/api/v1/{login,reset,list,edit,delete,upload,view-file,bulk/*}`).
- A pre-auth GET on the login endpoint may disclose full system config
  (panel version + complete stack map + cert identity string) — log as a
  disclosure finding with the exact fields.
- A `?user=` param on the mint endpoint is usually IGNORED: it still mints the
  anonymous shell, not that user's session.
- Gated endpoints usually still reject the minted shell (302/SPA-shell or an
  error field) — the mint is a design flaw, not privilege escalation.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
