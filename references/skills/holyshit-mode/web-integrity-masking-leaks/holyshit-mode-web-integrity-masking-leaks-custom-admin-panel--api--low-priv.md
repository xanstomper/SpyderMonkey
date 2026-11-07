# Custom admin panels (React-rebuilt on legacy control planes) — api / low-priv

- source canon: `holyshit-mode/web-integrity-masking-leaks.md`
- base technique: `holyshit-mode-web-integrity-masking-leaks-custom-admin-panel.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **api** · auth **low-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

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

## Probe adjustment (api × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
