# Tooling — chain composition

- source canon: `holyshit-mode/web-auth-chain-playbook.md`
- base technique: `holyshit-mode-web-auth-chain-playbook-tooling.md`
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

- Cloudflare 1010 blocks python urllib — use curl with browser User-Agent + Origin headers.
- holyleadger.py: statuses are only {confirmed, hypothesis, inconclusive, negative};
  report flags are `--target X --out file`; needs `HOLYSHIT_SCRIPT_DIR=$HOME/.hermes/scripts`.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
