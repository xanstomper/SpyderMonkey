# Sister brands have no own files — web-app / low-priv

- source canon: `spydermonkey/ledger-dump.md`
- base technique: `spydermonkey-ledger-dump-sister-brands-have-no-own-files.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- context: **web-app** · auth **low-priv** · chain role **pivot**

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

A sister brand (perabet under gamdom; cocogamebox/dogcrash under bc.game) does
NOT get its own holyleadger file or campaign dir. Its rows live in the parent
brand's ledger + holyleadger JSON. To dump one brand: filter BOTH stores for the
brand string, case-insensitive, across title/asset/proof (holyleadger: class
`technique` too); sort rows by cvss desc; report severity/status counters plus
the chains whose steps/impact mention the brand. Proven scale: perabet = 26
rows, ALL CONFIRMED (4 high / 8 med / 10 low / 4 info), inside gamdom's ledger.

## Probe adjustment (web-app × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
