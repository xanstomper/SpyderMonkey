# Breach context (why the engagement) — firmware / hardened

- source canon: `holyshit-mode/case-gamdom-com.md`
- base technique: `holyshit-mode-case-gamdom-com-breach-context-why-the-engagem.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **firmware** · auth **hardened** · chain role **pivot**

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

WhiteArmor extortion 2026-10-26/27: claims 15,420,003 accounts × 146 fields, $15M BTC ransom.
Attacker-stated initial access: aged internal machine account, creds never rotated, admin
privileges for years → internal control panels + data stores. Founder confirmed DB WRITE access
(unauthorized withdrawal INSERTs) during the 2026-10-13 wallet event (~$4.2M total loss).
Holdings claim: support chats+photos (Intercom — `intercom_hmac_hash` ships on the authed user
object = the impersonation-credential class), Perabet records (userid|email|password), founder's
admin record + last IP. Infostealer angle: Breachsense indexes 42,928 gamdom credentials +
13,552 stealer logins (some staff) — the credential-source class. The public wire is CLEAN on
outcome timing (crash point first appears in `game_crash` only) — their dice "prediction" claim
requires DB-level access, matching their own "any staff member with read access" wording.

## Probe adjustment (firmware × hardened)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
