# Negatives — web-app / low-priv

- source canon: `holyshit-mode/case-duelbits-com.md`
- base technique: `holyshit-mode-case-duelbits-com-negatives.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **web-app** · auth **low-priv** · chain role **pivot**

## Route

- probes: `wpscan`, `cmseek`, `droopescan`, `cmsmap`, `nmap-wp-plugins`, `nmap-drupal-enum`
- chains: `cms-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- `ephemeral.duelbits.com` = bare nginx default-404 vhost, nothing routed.
- No unauth data plane found before the burn (unlike duel): bet feeds sit behind auth + WAF.
- CMS content = marketing copy/economics, no PII, read-only delivery API.

## Probe adjustment (web-app × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
