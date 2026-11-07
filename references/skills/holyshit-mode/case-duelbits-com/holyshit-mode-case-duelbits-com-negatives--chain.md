# Negatives — chain composition

- source canon: `holyshit-mode/case-duelbits-com.md`
- base technique: `holyshit-mode-case-duelbits-com-negatives.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `wpscan`, `cmseek`, `droopescan`, `cmsmap`, `nmap-wp-plugins`, `nmap-drupal-enum`
- chains: `cms-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- `ephemeral.duelbits.com` = bare nginx default-404 vhost, nothing routed.
- No unauth data plane found before the burn (unlike duel): bet feeds sit behind auth + WAF.
- CMS content = marketing copy/economics, no PII, read-only delivery API.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
