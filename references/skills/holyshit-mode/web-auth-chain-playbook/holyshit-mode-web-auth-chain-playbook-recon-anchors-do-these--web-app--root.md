# Recon anchors (do these first) — web-app / root

- source canon: `holyshit-mode/web-auth-chain-playbook.md`
- base technique: `holyshit-mode-web-auth-chain-playbook-recon-anchors-do-these.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **web-app** · auth **root** · chain role **entry**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

- `GET /auth/v1/settings` — provider map, `phone_autoconfirm`, `mailer_autoconfirm`, `sms_provider`.
- `GET /api/status`, `GET /api/providers` — many SPAs expose fleet/config disclosure unauthenticated.
- SPA bundle: enumerate lazy route chunks (grep main.js for `./XxxPage-*.js`, fetch `/assets/<name>.js`)
  — the settings/keys route chunk holds the API surface (`/api/account/platform-keys`, etc.).
  Endpoint lists extracted from the landing chunks only are INCOMPLETE.

## Probe adjustment (web-app × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
