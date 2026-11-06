# Origin-map discipline — chain composition

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-origin-map-discipline.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- **`curl --resolve` is SILENTLY IGNORED under `socks5h`** — the proxy does remote DNS resolution and the IP pin never applies: every "vhost on the origin" answer is actually the REAL destination site. A whole false infra-map (sibling-brand vhosts, a payment processor "hosted by the operator") ships this way. Rule: vhost/origin sweeps with IP literals run DIRECT from the VM with NO proxy env (ssh vermes then curl --resolve, or openssl s_client -connect IP). Cheap tell: response headers — `via: ...cloudfront.net` / `x-cache` on a response you thought came from a bare Apache box = you talked to the wrong host. Same-size/different-hash bodies = same app build (dynamic bytes), which is how a mirrored site looks identical until the headers expose it.
- An infra row built on proxy-resolved answers is a hypothesis until the direct test repeats it — the ledger accepts the wrong proof fine because the estate gate checks the ASSET string, not which host answered. Correct rows with ledger update + a CORRECTED note, never silently.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
