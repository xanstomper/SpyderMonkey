# Background delegation: pin a working provider or the fan-out dies silently — android / machine

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-background-delegation-pin-a-work.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **android** · auth **machine** · chain role **pivot**

## Context

- platform: the check often lives client-side — frida/objection at the runtime, MASTG methodology
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

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

## Probe adjustment (android × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
