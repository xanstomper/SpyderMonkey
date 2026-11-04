# USAGE RULES — chain composition

- source canon: `holyshit-mode/detection-evasion-modules.md`
- base technique: `holyshit-mode-detection-evasion-modules-usage-rules.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Every module requires explicit stealth-validation scope in the authorization document.
- Each technique is run once, logged with timestamp, and reverted immediately after
  validation.
- The output is a detection-gap report: technique → expected detection → observed
  detection → proposed analytic (Sigma/KNQL/CloudWatch rule).
- No module is used against production users or data — lab tenants, test accounts, and
  scoped resources only.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
