# 7. Frame-capture integrity (evidence hygiene) — host / unauth

- source canon: `holyshit-mode/engineio-socketio-testing.md`
- base technique: `holyshit-mode-engineio-socketio-testing-7-frame-capture-inte.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **host** · auth **unauth** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- ALWAYS reassemble continuation frames: large events arrive as op=1 + op=0 fragments (~4KB each); naive per-frame saves split JSON mid-object and corrupt evidence files. Read each header, honor the `fin` bit, merge fin=0 payloads; skip pongs (op=10) instead of writing them as text junk.
- Sanitize control bytes (`[\x00-\x08\x0b\x0c\x0e-\x1f]`) before json-parsing saved captures, and parse arrays with `json.JSONDecoder().raw_decode` rather than regexing field ORDER (field order varies between event types).
- Re-run a second capture and confirm stable IDs/values before calling a leaked field real — a finding that does not reproduce across captures is a parse artifact.
- The masking may exist on SOME feed paths and not others (leaderboard masked, game-detail/crash rows unmasked-with-flag) — audit every path independently.

## Probe adjustment (host × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
