# Breach context (why the engagement)

- source canon: `holyshit-mode/case-gamdom-com.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
