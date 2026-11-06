# Origin-map discipline — ci-cd / machine

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-origin-map-discipline.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **ci-cd** · auth **machine** · chain role **pivot**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- **`curl --resolve` is SILENTLY IGNORED under `socks5h`** — the proxy does remote DNS resolution and the IP pin never applies: every "vhost on the origin" answer is actually the REAL destination site. A whole false infra-map (sibling-brand vhosts, a payment processor "hosted by the operator") ships this way. Rule: vhost/origin sweeps with IP literals run DIRECT from the VM with NO proxy env (ssh vermes then curl --resolve, or openssl s_client -connect IP). Cheap tell: response headers — `via: ...cloudfront.net` / `x-cache` on a response you thought came from a bare Apache box = you talked to the wrong host. Same-size/different-hash bodies = same app build (dynamic bytes), which is how a mirrored site looks identical until the headers expose it.
- An infra row built on proxy-resolved answers is a hypothesis until the direct test repeats it — the ledger accepts the wrong proof fine because the estate gate checks the ASSET string, not which host answered. Correct rows with ledger update + a CORRECTED note, never silently.

## Probe adjustment (ci-cd × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
