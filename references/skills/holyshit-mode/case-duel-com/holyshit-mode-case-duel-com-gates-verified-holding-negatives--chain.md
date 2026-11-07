# Gates verified holding (negatives) — chain composition

- source canon: `holyshit-mode/case-duel-com.md`
- base technique: `holyshit-mode-case-duel-com-gates-verified-holding-negatives.md`
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

`dev/staging/uat` = Cloudflare Access SSO; `capi-automation` S3 = AccessDenied both regions; live-stream S3 = AccessDenied; all sensitive `/api/v2/*` 401 unauth; pvp `/api/v1|v2` = geo-403; pvp arena socket disconnects anon AND user:null-token connects at the namespace gate; `duel.getid.ee` = GetId KYC dashboard login (hypothesis 30).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
