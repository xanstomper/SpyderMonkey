# Custom admin panels (React-rebuilt on legacy control planes) — chain composition

- source canon: `holyshit-mode/web-integrity-masking-leaks.md`
- base technique: `holyshit-mode-web-integrity-masking-leaks-custom-admin-panel.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Mine the panel's OWN client bundle for the full custom API surface — a
  React rebuild exposes paths the stock panel never had
  (`/api/v1/{login,reset,list,edit,delete,upload,view-file,bulk/*}`).
- A pre-auth GET on the login endpoint may disclose full system config
  (panel version + complete stack map + cert identity string) — log as a
  disclosure finding with the exact fields.
- A `?user=` param on the mint endpoint is usually IGNORED: it still mints the
  anonymous shell, not that user's session.
- Gated endpoints usually still reject the minted shell (302/SPA-shell or an
  error field) — the mint is a design flaw, not privilege escalation.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
