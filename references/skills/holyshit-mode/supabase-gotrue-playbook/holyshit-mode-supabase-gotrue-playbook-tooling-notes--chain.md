# Tooling notes — chain composition

- source canon: `holyshit-mode/supabase-gotrue-playbook.md`
- base technique: `holyshit-mode-supabase-gotrue-playbook-tooling-notes.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- holyleadger.py: `add <name> <confirmed|inconclusive|hypothesis|negative> --score N --technique "..." --target X`; report via `report --target X --out path`. Invalid status/class values exit 2 silently — stick to the four.
- Cloudflare 1010 WAF blocks python urllib — use curl with browser UA + `Origin` + `apikey` headers.
- Common failure: calling the wrong tool name (`shell` vs `terminal`) wastes turns. Be deliberate.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
