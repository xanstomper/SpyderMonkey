# Raw-string trap in proxied HTML blobs (cost ~2 restarts) — ci-cd / low-priv

- source canon: `holyshit-mode/case-obsidian-y-api-dataplane.md`
- base technique: `holyshit-mode-case-obsidian-y-api-dataplane-raw-string-trap-.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **ci-cd** · auth **low-priv** · chain role **pivot**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

Wrapping the playground HTML in a Python `r"""..."""` raw string to silence a `\s` SyntaxWarning
BREAKS the embedded JS — the JS needs Python `\n` → newline translation for SSE buffer scanning
(`buf.indexOf('\n\n')`), which a raw string turns into literal backslashes. Fix the warning by
escaping the specific JS regex backslashes (`[\s\S]`→`[\\s\\S]`, `<\/think>`→`<\\/think>`) so
Python emits literal single-escapes to the browser, NOT by raw-stringing the whole blob. A
SyntaxWarning on a JS regex inside an HTML string is harmless; don't degrade correctness to
silence it.

## Probe adjustment (ci-cd × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
