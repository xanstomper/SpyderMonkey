# 3. Custom-PHP login/control-center (luxeindubai.com) — ci-cd / guest

- source canon: `holyshit-mode/control-escalation-negatives.md`
- base technique: `holyshit-mode-control-escalation-negatives-3-custom-php-logi.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **ci-cd** · auth **guest** · chain role **pivot**

## Route

- probes: `gobuster`, `ffuf`, `dirsearch`, `dirb`, `feroxbuster`, `wfuzz`, `dirhunt`
- chains: `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

- LiteSpeed `/_autoindex/` directory listing enabled site-wide enumerates a bespoke admin tree
  (e.g. `config.php`, `control_center.php`, `add_property.php`, `login_form.php`, `uploads/`,
  `phpmailer/`). Directory listing of an admin source tree = a real control-surface exposure finding.
- Custom login (`login_form.php` POST email+password) rejected SQLi auth-bypass payloads
  (`' OR '1'='1`, `admin' --`, `' OR 1=1-- -`) — all returned the Login Form, no bypass. control_center.php
  correctly gates unauth (serves the login form). Parameterized/hashed.
- **PHP `display_errors` infoleak:** POST to custom register without `g-recaptcha-response` →
  `Notice: Undefined index: g-recaptcha-response in /home/<cpanel-user>/public_html/.../register_form.php`
  on line N. Leaks the hosting account (`<cpanel-user>`) and cPanel `public_html` path = real finding.
  The reCAPTCHA STILL holds (no account created) — do not spend budget defeating captcha to make a
  test account unless the operator explicitly authorizes bootstrapping on that owned service.
- Misleading backup filename: a file named `LXDB-2244(09).zip` looked like a DB dump but the archive
  held only `.jpg` photos. **Always unzip/verify an exposed archive's member names before calling it
  a credential/DB leak** — filename ≠ content.

## Probe adjustment (ci-cd × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
