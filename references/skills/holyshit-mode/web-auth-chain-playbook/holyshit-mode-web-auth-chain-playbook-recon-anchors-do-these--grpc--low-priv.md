# Recon anchors (do these first) — grpc / low-priv

- source canon: `holyshit-mode/web-auth-chain-playbook.md`
- base technique: `holyshit-mode-web-auth-chain-playbook-recon-anchors-do-these.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **grpc** · auth **low-priv** · chain role **entry**

## Context

- platform: reflection/list methods first; protobuf definitions are the schema oracle
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- `GET /auth/v1/settings` — provider map, `phone_autoconfirm`, `mailer_autoconfirm`, `sms_provider`.
- `GET /api/status`, `GET /api/providers` — many SPAs expose fleet/config disclosure unauthenticated.
- SPA bundle: enumerate lazy route chunks (grep main.js for `./XxxPage-*.js`, fetch `/assets/<name>.js`)
  — the settings/keys route chunk holds the API surface (`/api/account/platform-keys`, etc.).
  Endpoint lists extracted from the landing chunks only are INCOMPLETE.

## Probe adjustment (grpc × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
