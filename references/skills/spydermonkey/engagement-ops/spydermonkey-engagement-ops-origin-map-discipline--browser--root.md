# Origin-map discipline — browser / root

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-origin-map-discipline.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **browser** · auth **root** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the CLIENT is the boundary — same-origin, extension, and postMessage trust are the probe shape
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

- **`curl --resolve` is SILENTLY IGNORED under `socks5h`** — the proxy does remote DNS resolution and the IP pin never applies: every "vhost on the origin" answer is actually the REAL destination site. A whole false infra-map (sibling-brand vhosts, a payment processor "hosted by the operator") ships this way. Rule: vhost/origin sweeps with IP literals run DIRECT from the VM with NO proxy env (ssh vermes then curl --resolve, or openssl s_client -connect IP). Cheap tell: response headers — `via: ...cloudfront.net` / `x-cache` on a response you thought came from a bare Apache box = you talked to the wrong host. Same-size/different-hash bodies = same app build (dynamic bytes), which is how a mirrored site looks identical until the headers expose it.
- An infra row built on proxy-resolved answers is a hypothesis until the direct test repeats it — the ledger accepts the wrong proof fine because the estate gate checks the ASSET string, not which host answered. Correct rows with ledger update + a CORRECTED note, never silently.

## Probe adjustment (browser × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
