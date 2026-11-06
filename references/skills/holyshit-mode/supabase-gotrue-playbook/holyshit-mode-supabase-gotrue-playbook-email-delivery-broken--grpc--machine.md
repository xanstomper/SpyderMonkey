# Email-delivery-broken targets — grpc / machine

- source canon: `holyshit-mode/supabase-gotrue-playbook.md`
- base technique: `holyshit-mode-supabase-gotrue-playbook-email-delivery-broken.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **grpc** · auth **machine** · chain role **pivot**

## Context

- platform: reflection/list methods first; protobuf definitions are the schema oracle
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

Confirm with mailinator public API: `https://www.mailinator.com/api/v2/domains/public/inboxes/<user>` (returns `{"msgs":[]}` — validate the API itself works against a known-active inbox like `test` before concluding). When mail is dead, pivot to attacking the verification check (sibling endpoints, handoff flows) rather than the mail path.

## Probe adjustment (grpc × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
