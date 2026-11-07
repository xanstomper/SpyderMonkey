# Origin-map discipline

- source canon: `spydermonkey/engagement-ops.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-06

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- **`curl --resolve` is SILENTLY IGNORED under `socks5h`** — the proxy does remote DNS resolution and the IP pin never applies: every "vhost on the origin" answer is actually the REAL destination site. A whole false infra-map (sibling-brand vhosts, a payment processor "hosted by the operator") ships this way. Rule: vhost/origin sweeps with IP literals run DIRECT from the VM with NO proxy env (ssh vermes then curl --resolve, or openssl s_client -connect IP). Cheap tell: response headers — `via: ...cloudfront.net` / `x-cache` on a response you thought came from a bare Apache box = you talked to the wrong host. Same-size/different-hash bodies = same app build (dynamic bytes), which is how a mirrored site looks identical until the headers expose it.
- An infra row built on proxy-resolved answers is a hypothesis until the direct test repeats it — the ledger accepts the wrong proof fine because the estate gate checks the ASSET string, not which host answered. Correct rows with ledger update + a CORRECTED note, never silently.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
