# The five genes — formal table (enforced by `gene --check`) — websocket / low-priv

- source canon: `kairo/synthesis-engine.md`
- base technique: `kairo-synthesis-engine-the-five-genes-formal-table-enforced-.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **websocket** · auth **low-priv** · chain role **final**

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

| Gene | Meaning | Where it comes from | What breaks without it |
|---|---|---|---|
| TRIGGER | the source finding that justifies the vector | ingest (undercroft/3AM/kairo states) | a vector aimed at nothing — fabrication |
| PRECONDITION | declared estate + the access the finding proved | the source finding's declaration | out-of-scope execution |
| PRIMITIVE | the class's mechanism (why it works) | the technique-class canon | a ritual with no theory — cannot adapt |
| IMPACT-GATE | the decisive proof condition | the class's proof shape | no way to tell hit from miss |
| **Δ** | the documented-class adaptation to THIS target | the operator's aiming | novel-weapon authorship (the wall) |

`kairo gene --check --target T` prints the per-vector gene table and exits 1 if
ANY vector misses a gene. NO Δ = NO VECTOR is not advice — it's an exit code.

## Probe adjustment (websocket × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
