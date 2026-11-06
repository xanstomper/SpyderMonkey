# Certificate-transparency intel depth — ci-cd / low-priv

- source canon: `spydermonkey/technique-canon-2.md`
- base technique: `spydermonkey-technique-canon-2-certificate-transparency-inte.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **ci-cd** · auth **low-priv** · chain role **pivot**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

crt.sh/certspotter + live-cert SAN mining (the CT-log lane in the ops canon) — wildcard/SAN/sibling-brand exposure is the inventory crown. Decisive test: SAN list from a live handshake naming hosts DNS never published.

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
