# Host-header routing at the edge (vhost collision) — ci-cd / low-priv

- source canon: `spydermonkey/technique-canon-7.md`
- base technique: `spydermonkey-technique-canon-7-host-header-routing-at-the-ed.md`
- bindings: **WSTG-PARA** · **CWE-113** · **ATT&CK T1190**
- context: **ci-cd** · auth **low-priv** · chain role **pivot**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

Default/catch-all vhosts serving sibling brands (the oncasi :80 catch-all class). Decisive test: Host: sibling-brand on the origin IP — the wrong-site response = shared-origin evidence.

## Probe adjustment (ci-cd × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
