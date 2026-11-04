# SSE `[DONE]` guarantee — chain composition

- source canon: `holyshit-mode/case-obsidian-y-api-dataplane.md`
- base technique: `holyshit-mode-case-obsidian-y-api-dataplane-sse-done-guarant.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Upstream SSE streams can truncate without `data: [DONE]`. A browser reader loop that waits for
the terminator hangs forever. The proxy's `sse_wrap` must gated-yield `data: [DONE]\n\n` in a
`finally` when the upstream didn't. (For the browser half: a `finalize()` guard that always runs
on stream end / error / catch, so the meta/status line always renders.)

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
