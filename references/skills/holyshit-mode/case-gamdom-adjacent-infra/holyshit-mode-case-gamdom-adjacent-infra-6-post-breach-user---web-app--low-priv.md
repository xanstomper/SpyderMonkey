# 6. Post-breach user-protection checks (do these even when the core is clean) — web-app / low-priv

- source canon: `holyshit-mode/case-gamdom-adjacent-infra.md`
- base technique: `holyshit-mode-case-gamdom-adjacent-infra-6-post-breach-user-.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **web-app** · auth **low-priv** · chain role **pivot**

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- `dig TXT _dmarc.<domain>` — `p=reject; pct=100` = spoofing dead. `p=none` or missing =
  post-breach phishing is trivially easy and becomes a critical finding.
- Full SPF (`-all` vs `~all`) + DKIM selector sweep (`default|google|s1|s2|selector1...`).
- The breach data itself drives phishing lures; the email-auth posture decides whether
  attackers can send AS the domain. This is the live risk while the extortion clock runs.

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
