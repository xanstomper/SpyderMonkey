# 2026-11-03 3AM keep-going round: routes complete + drift oracle armed — grpc / machine

- source canon: `holyshit-mode/case-packdraw-com.md`
- base technique: `holyshit-mode-case-packdraw-com-2026-11-03-3am-keep-going-ro.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **grpc** · auth **machine** · chain role **pivot**

## Context

- platform: reflection/list methods first; protobuf definitions are the schema oracle
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- Drift baseline: chunk 0lvv874ns6o2c.js sha1 = 0d48fa724bf3 (re-arm before any future
  re-probe); checkpoint shell byte-stable (17385B 429 from VM).
- /draw, /deals (10,905 products to $350K), /events (Daily Raffle $2,500 pool; winners
  list PUBLIC with masked handles first3+last3, exact ticket counts, payouts; raffle RNG
  not covered by the PF doc), /rewards (login-gated ladder: daily/weekly/monthly + free
  packs L2-L100).
- Google/Apple OAuth = server-action start (no client-side client_id/redirect_uri);
  CORS clean (403 no reflection). OAuth/raffle-RNG items = operator-plane/inconclusive.

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
