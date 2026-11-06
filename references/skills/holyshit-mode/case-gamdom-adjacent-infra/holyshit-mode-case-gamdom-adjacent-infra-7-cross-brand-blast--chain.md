# 7. Cross-brand blast radius — chain composition

- source canon: `holyshit-mode/case-gamdom-adjacent-infra.md`
- base technique: `holyshit-mode-case-gamdom-adjacent-infra-7-cross-brand-blast.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Identical CDN IPs + verbatim-identical error envelopes across sister brands = shared
  backend user/session store hypothesis.
- Ledger a cross-brand session-replay hypothesis (one account on either brand tests it)
  and the credential-reuse angle: attacker leaks of ONE brand's `userid|email|password`
  records degrade the whole family.
- Sister-brand CT logs surface what the main brand's logs hide: staging servers (dead
  503 origin behind a live route) and dangling CDN routes ("unknown domain" errors).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
