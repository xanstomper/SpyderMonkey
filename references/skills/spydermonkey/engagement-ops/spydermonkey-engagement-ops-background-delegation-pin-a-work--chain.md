# Background delegation: pin a working provider or the fan-out dies silently — chain composition

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-background-delegation-pin-a-work.md`
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

When dispatching parallel hunting subagents on an engagement, the children INHERIT the parent's
model provider by default. If that provider's key is expired/invalid (502 `Unauthorized` returned
before any tool call), every child fails identically and produces ZERO findings — a whole parallel
lane silently wasted. Mitigation: pin delegation to a known-good provider and VERIFY it completes a
chat call first. `delegate_task action=list` shows running children; a child whose transcript shows
only the kickoff then `status=failed` with a provider 502 within seconds is a provider-routing
failure, not a probe failure — re-dispatch to the working provider or run that lane yourself
directly instead of re-using the dead provider.

**The pin is CONFIG-LEVEL — a provider note in the task's `context` prose does nothing.** The only
thing that routes child traffic is `delegation.provider` / `delegation.model` in `~/.hermes/config.yaml`
(the child inherits the parent's effective delegation config at dispatch time, not anything you pass
per-task). Check `delegation.provider` in config.yaml FIRST when a fan-out dies — a default of a
broken/expired provider (e.g. `freeforge` with an invalid key) explains every child failing
identically. Set the working provider with `hermes config set delegation.provider <provider>`
and `hermes config set delegation.model <model>` (never hand-edit config.yaml), then re-dispatch.
A freshly-configured working provider still lists as `deepseek-v4-pro` on the child header unless the
model is also switched — confirm the child's reported model matches what you pinned. Known-good
fallback on this estate: VyceAI (`https://vyceai.com/v1`, key `VYCEAI_API_KEY`, models incl.
`glm-5.3-flash` / `claude-sonnet-4-6`) — verify with a `chat/completions` call before relying on it.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
