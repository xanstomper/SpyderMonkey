# Negatives — mobile-api / low-priv

- source canon: `holyshit-mode/case-duelbits-com.md`
- base technique: `holyshit-mode-case-duelbits-com-negatives.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **mobile-api** · auth **low-priv** · chain role **pivot**

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- `ephemeral.duelbits.com` = bare nginx default-404 vhost, nothing routed.
- No unauth data plane found before the burn (unlike duel): bet feeds sit behind auth + WAF.
- CMS content = marketing copy/economics, no PII, read-only delivery API.

## Probe adjustment (mobile-api × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
