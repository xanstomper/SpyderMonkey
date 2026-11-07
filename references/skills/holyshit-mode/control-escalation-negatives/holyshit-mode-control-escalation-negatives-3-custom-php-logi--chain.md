# 3. Custom-PHP login/control-center (luxeindubai.com) — chain composition

- source canon: `holyshit-mode/control-escalation-negatives.md`
- base technique: `holyshit-mode-control-escalation-negatives-3-custom-php-logi.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `gobuster`, `ffuf`, `dirsearch`, `dirb`, `feroxbuster`, `wfuzz`, `dirhunt`
- chains: `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
