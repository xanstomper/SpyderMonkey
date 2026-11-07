# harakirimail public-inbox chain (mailinator blocked here) — chain composition

- source canon: `holyshit-mode/case-gonka-api.md`
- base technique: `holyshit-mode-case-gonka-api-harakirimail-public-inbox-chain.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- List: `GET https://harakirimail.com/api/v1/inbox/<name>` (metadata only).
- Full body: `GET https://harakirimail.com/api/v1/email/<_id>` (`bodyhtmltext`).
- Extract `token=([a-f0-9]{40,})` from the confirm link; consume ONCE.
- Confirm: `GET /auth/v1/verify?token=...&type=signup&email=...` → 303 with
  `#access_token` fragment. Take a stable session via password grant afterward.
- Bonus leak: the confirm email's `redirect_to` exposed the Lovable mirror host.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
