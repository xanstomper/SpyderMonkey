# 7.3 Framework-default admin planes (score 75) — chain composition

- source canon: `3am-shinjitsu/arsenal-07-supply-chain.md`
- base technique: `3am-shinjitsu-arsenal-07-supply-chain-7-3-framework-default-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- SET: Spring `/actuator/*` (env, heapdump, jolokia), Django admin `/admin/` (title oracle),
  Laravel `/telescope`, `/horizon`, Strapi admin, `/debug/vars` (expvar), `/_debug/bar`,
  phpLiteAdmin/Adminer, phpMyAdmin paths, `/console` (WERKZEUG debugger PIN page).
- DISCRIMINATOR: status + content-type pair (§2.2) + a title/body fingerprint, once each.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
