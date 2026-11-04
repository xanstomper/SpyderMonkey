# 9.4 CT-log pivot ladder (score 85, zero contact) — chain composition

- source canon: `3am-shinjitsu/arsenal-09-breach-osint.md`
- base technique: `3am-shinjitsu-arsenal-09-breach-osint-9-4-ct-log-pivot-ladde.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- `curl -s 'https://crt.sh/?q=%25.<domain>&output=json' | jq -r '.[].name_value' | sort -u`
- Chain: CT names → partner brands (bundle `/providers/<brand>-originals`) → mirror/entrance
  hosts → passive DNS → bare-AWS origins. Dead DNS ≠ dead server: live cert + stripped DNS =
  "internal control panel" signature (→ §1.7).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
