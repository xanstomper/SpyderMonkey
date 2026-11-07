# R1 — Webhook replay → duplicate effect (payments/integrations) — browser / root

- source canon: `undercroft/undercroft-playbook.md`
- base technique: `undercroft-undercroft-playbook-r1-webhook-replay-duplicate-e.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **browser** · auth **root** · chain role **pivot**

## Route

- probes: `httpx`, `whatweb`, `webanalyze`, `nmap-waf-fingerprint`, `katana`, `gospider`, `hakrawler`
- chains: `recon`, `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the CLIENT is the boundary — same-origin, extension, and postMessage trust are the probe shape
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

1. Trigger ONE legitimate event on your own account (e.g. a test payment/callback).
2. Capture the outbound callback the platform sent your endpoint (request log,
   webhook debugger, or your own receiver log): full method+headers+body.
3. `undercroft replay --url <your-endpoint> --method POST --header "X-Sig: <as captured>" --body '<captured>' --times 3 --confirm`
4. Check: one effect or N? (order created once vs N; ledger entry duplicated).
5. CONFIRMED when the platform's own dedup key fails to gate the replay. Reverse:
   refund/delete the duplicates immediately (NO-GAIN).
6. `craft` as STATE; `export` → 3AM.

## Probe adjustment (browser × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
