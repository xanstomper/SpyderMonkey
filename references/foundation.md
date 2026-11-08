# THE FOUNDATION — agent red-teaming as a protocol (v7.5)

A model-agnostic operating contract for autonomous offensive-security agents.
Any model plugs in at Layer 0; any estate gates at Layer 1; every finding is
born at Layer 2 or it is not a finding. The protocol is the INTERFACE between
the model and the machine: the model contributes judgment, the layers
contribute everything else.

## The seven layers

- **L0 PERSONA — the one-paste pack.** `spydermonkey mandate --pack` is the
  whole operating contract in ~2k tokens: walls, route table, the kernel loop,
  the evidence contract. Adopt it as a system prompt and a general model
  becomes an operator. Nosetup, no install, model-agnostic.
- **L1 ESTATE — the scope authority.** One shared gate (`scope_authority.py`),
  imported by every engine, every probe, every node. Declared estates only;
  deny wins; expiry enforced; the loopback lab is the only implicit allowance.
  Nothing runs un-gated.
- **L2 EVIDENCE — the proof floor.** The 3-gate (baseline → attack → diff +
  confirm token), the hash-chained ledger, hypothesis downgrades (conf 0.4,
  never suppressed). A claim without a decisive test is a hypothesis — by
  construction. Fabrication is structurally impossible.
- **L3 ENGINES — the compiled corpus.** Ten mandates, 18 parallel testers, the
  chain engine, the hypothesis generator: documented technique classes
  compiled into instances. The family aims and compiles; it never authors
  novel weapon classes.
- **L4 KNOWLEDGE — the retrieval layer.** Index of 205,809 corpus documents
  (canons · skilltree · expanded techniques · tool surge), deterministic
  ranking, injected at the decision point (`inject`). The model reasons with
  the exact pages — zero wasted context.
- **L5 SYNTHESIS — the flywheel.** KAIRO vectors are RANGE-PROVEN before
  distribution (`kairo validate` → `compile --require-validated`); the shared
  weight store (ledger → priors) makes the family sharper on real targets;
  `train` self-plays the dojo. Every confirmed attack permanently becomes
  prior, rule, and lesson.
- **L6 FLEET — the agent channel.** Controller + node agents
  (`fleet_agent.py`): tasks queue at the controller, nodes execute in their
  own gated homes, results return in the kernel schema. Beacons or listeners;
  every node refuses to run without its own scope authority.
- **L7 MIRROR — the purple layer.** Every confirmed attack becomes a Sigma
  rule + SIEM-native records (Splunk/Elastic/QRadar); `refire` re-fires the
  attack and requires the rule to fire. The offense is proven visible — the
  defender gets the eyes.

## The invariants (the walls — non-negotiable at every layer)

1. Declared estates only.
2. Documented-PoC adaptation only — technique classes are canon; the family
   aims and compiles them into instances, never novel weapon classes.
3. Validation-only + NO-GAIN — one decisive reversible proof, then STOP.
   Persistence is never installed.
4. Never social. Never third parties.
5. Zero documents — the recorded declaration is the entire gate.
6. Destructive end-states refused once, pivoted to disclosure.

## The loop

`next` → execute → `absorb` → mutate. The kernel emits the ONE state-driven
directive (exact argv + walls); results re-enter through the same scope,
ledger, and evidence gates; drift re-verifies before re-asserting; negatives
are results.

## Adoption (the shape, in four moves)

- ANY MODEL: paste L0 (the pack) — operator, immediately.
- ANY AGENT: drive the CLI; the engines are stdlib and offline.
- ANY NODE: place its scope.json, run `fleet_agent.py` — it executes only
  gated, only queued tasks.
- ANY DEFENDER: `kage export` — Sigma or SIEM-native records of everything
  the family proved.

## Differentiation

Negative results are first-class outputs. Discipline is code, not promises.
The family's benchmark is the honesty of its ledger — and that is the one
metric no competitor's architecture can copy without rebuilding itself.

Emit via:  spydermonkey foundation