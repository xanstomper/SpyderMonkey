# Breach context (why the engagement) — iot / machine

- source canon: `holyshit-mode/case-gamdom-com.md`
- base technique: `holyshit-mode-case-gamdom-com-breach-context-why-the-engagem.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **iot** · auth **machine** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: radio/serial surface — BLE/NFC/UART classes, lab hardware only
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

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

## Probe adjustment (iot × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
