# Breach context (why the engagement) — chain composition

- source canon: `holyshit-mode/case-gamdom-com.md`
- base technique: `holyshit-mode-case-gamdom-com-breach-context-why-the-engagem.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
