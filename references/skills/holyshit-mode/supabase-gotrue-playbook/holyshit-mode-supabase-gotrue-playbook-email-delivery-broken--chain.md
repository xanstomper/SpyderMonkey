# Email-delivery-broken targets — chain composition

- source canon: `holyshit-mode/supabase-gotrue-playbook.md`
- base technique: `holyshit-mode-supabase-gotrue-playbook-email-delivery-broken.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Confirm with mailinator public API: `https://www.mailinator.com/api/v2/domains/public/inboxes/<user>` (returns `{"msgs":[]}` — validate the API itself works against a known-active inbox like `test` before concluding). When mail is dead, pivot to attacking the verification check (sibling endpoints, handoff flows) rather than the mail path.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
