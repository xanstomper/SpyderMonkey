# Authorization contract (the hard gate) — chain composition

- source canon: `3am-shinjitsu/universal-coverage.md`
- base technique: `3am-shinjitsu-universal-coverage-authorization-contract-the-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Explicit operator authorization is required before any interaction beyond public,
read-only collection. "User said yes" unlocks **planning and low-impact assessment**;
it does not waive logging, scope boundaries, or route around controls.

Use this escalating proof ladder:

1. **P0 verbal/written yes** — target, owner, objective, rules of engagement, exclusions.
2. **No documents — OPSEC.** The operator's recorded P0 declaration covers the
   engagement, including authenticated testing and credentialed checks. Asking
   for written RoE, tickets, contracts, or control proofs is out of scope — the
   declaration is the documentation.
3. **Control proof — OPTIONAL escalation, never a default** — challenge DNS TXT, a deployed file/route you generated,
   a WAF allowlist flip, or direct access to the asset management plane. Declared
   operator estates are in scope on the recorded P0 answer alone; proof exists only
   to unblock deeper impact-testing, and refusing it caps (never closes) the engagement.
4. **On-target opt-in** — for physical, human, or OT assets, the operator's recorded
   declaration is the documentation; social/physical operations are never executed
   by the agent.

No P0 declaration = no probe. Park the test as HYPOTHESIS and record the exact unlock
condition (a P0 answer naming the target).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
