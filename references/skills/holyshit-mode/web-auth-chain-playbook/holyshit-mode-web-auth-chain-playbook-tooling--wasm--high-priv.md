# Tooling — wasm / high-priv

- source canon: `holyshit-mode/web-auth-chain-playbook.md`
- base technique: `holyshit-mode-web-auth-chain-playbook-tooling.md`
- bindings: **WSTG-PARA** · **CWE-113** · **ATT&CK T1190**
- context: **wasm** · auth **high-priv** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- Cloudflare 1010 blocks python urllib — use curl with browser User-Agent + Origin headers.
- holyleadger.py: statuses are only {confirmed, hypothesis, inconclusive, negative};
  report flags are `--target X --out file`; needs `HOLYSHIT_SCRIPT_DIR=$HOME/.hermes/scripts`.

## Probe adjustment (wasm × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
