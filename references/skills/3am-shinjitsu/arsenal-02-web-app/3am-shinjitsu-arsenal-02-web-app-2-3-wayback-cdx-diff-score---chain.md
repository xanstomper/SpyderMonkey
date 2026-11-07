# 2.3 Wayback CDX diff (score 75, zero target traffic) — chain composition

- source canon: `3am-shinjitsu/arsenal-02-web-app.md`
- base technique: `3am-shinjitsu-arsenal-02-web-app-2-3-wayback-cdx-diff-score-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- DECISIVE: `curl -s 'https://web.archive.org/cdx/search/cdx?url=<domain>/*&fl=original&collapse=urlkey'`
- EXTRACT: removed routes vs live; id-format oracle (`user=`, `token=`, `r=`, `stag=` shapes);
  removed auth methods; old affiliate formats. Run BEFORE brute-formatting any id oracle.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
