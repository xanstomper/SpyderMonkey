# DEEP DIVE — holyshit-mode depth (load on confirm) — chain composition

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- base technique: `3am-shinjitsu-arsenal-01-network-edge-deep-dive-holyshit-mod.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- → holyshit `references/wordpress-cloudflare-origin-bypass.md` + `cf-wp-origin-bypass-recipe.md` — origin-leak→direct-origin full ladder
- → holyshit `references/case-g***REDACTED***-adjacent-infra.md` — era-stack fingerprint recipe (VestaCP 301 path leak, :8083/:3306 banners)
- → holyshit `references/recon-quick-checks.md` — CF-origin leak, engine.io sid, SPA ghost discriminator batteries
- → holyshit `references/engagement-vantage-policy.md` — probe from the VM vantage, never the home IP (attribution law)
```

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
