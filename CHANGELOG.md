# v7.6.1 — CVE INSTANCES IN THE REASONING: cards cite real evidence

- **cve-map hypothesis cards now carry `instances`** — REAL CVE→exploit
  entries from the committed 66.5k catalog whenever a family keyword
  co-occurs with a CVE token (verified live: php fingerprint → TRAVERSAL
  card cites CVE-2023-46455/edb-51851; CRLF card cites CVE-2026-80428/
  edb-52682).
- Honest companion finding: the catalog's CVE-token density is 4,641 — the
  NVD corpus lane (queued, source-blocked from this box) is the multiplier.
- Tests 80/80.

# v7.6.0 — THE KNOWLEDGE SURGE: the recovered canon + the detection corpus

- **INDEX BUG FIX (density recovery)**: context_router globbed `*canon.md`,
  silently dropping all 12 numbered `technique-canon-N.md` volumes — the core
  technique corpus was 40% invisible to retrieval. Fixed (`*canon*.md`):
  canon docs 18 → 30; index vocabulary 129,853 → 135,907 terms.
- **THE SIGMA KNOWLEDGE LANE**: `scripts/sigma_index.py` (stdlib line parser,
  no yaml dep) indexes the public SigmaHQ detection corpus → committed
  `references/sigma-index.json` (3,164/3,164 rules) → the context router now
  retrieves rule-level detections alongside canon/techniques/tools
  (`kind: sigma`): "log4shell jndi" → the exact JNDI-injection rule;
  "webshell iis" → 3 precise detection rules; kerberos queries surface both
  the canon volume AND the RC4-ticket rules. Knowledge index: 205,809 →
  208,985 docs (+3,176) with 5 kinds.
- Honest ceiling on the 5-10x ask, in the changelog itself: the official CVE
  corpus (NVD), CAPEC, and GTFOBins are QUEUED — their bulk sources were
  unreachable from this box (HTML-blocked); the ingestion lane is the same
  one used here (fetch → index → measure). Every density claim stays
  measured, never promised.
- Tests 79/79.

# v7.5.6 — AMBIENT BY CONSTRUCTION: campaign init auto-deploys the takeover brief

- **`campaign init` now deploys `agents/AGENTS.md` into the new campaign dir**
  (idempotent — never clobbers a hand-edited brief). Any agent started from a
  campaign dir is in-mandate by construction: Claude Code/OpenCode auto-load
  AGENTS.md AND the campaign-CWD rule arms both host gates (SessionStart
  injection + PreToolUse scope block) with zero markers typed.
- **End-to-end proven** (scratch home): campaign init → AGENTS.md present →
  SessionStart hook injects the 2.1k brief via campaign-CWD alone → scope hook
  blocks an out-of-estate curl via campaign-CWD alone.
- **Deployed to the live estate**: all 209 existing campaign dirs under
  ~/.redteam/campaigns/ now carry the brief.
- Test: campaign init deploy + --force idempotency (custom brief preserved).
- OpenCode parity note: AGENTS.md is auto-loaded by OpenCode v2.2.x (prompt
  layer); the mechanical hook layer remains Claude Code's (no hook surface in
  OpenCode's config).

# v7.5.5 — THE OPERATOR CONSOLE + SESSIONSTART MECHANICAL INJECTION: drift detection + no-trigger takeover

- **`inmandate` subcommand** (NEW): one command answers "is this session under
  the mandate right now, and are the mechanical gates armed?" — marker state
  (env / `.spydermonkey-active` / campaign CWD), wired host gates, scope
  authority + engagement, contract ID. `--json` for machine use. Registered in
  verify's help-list.
- **`scripts/claude_hook_sessionstart.py`** (NEW): SessionStart hook — when a
  marker is active, the ambient takeover brief (`agents/AGENTS.md`) is injected
  into the session context at start. Takeover engages with ZERO trigger typed
  and without depending on the model self-discovering the contract. Verified:
  silent pass-through without marker; 2.1k brief injected with marker. Wired
  into `~/.claude/settings.json` SessionStart.
- **Contract v8.3**: version bump + **Contract ID: SM8.3** fingerprint line —
  `inmandate` reports it; a mismatch with the announcement means a stale
  injection, re-inject before acting.
- **Test pins**: Contract ID · `inmandate` end-to-end (off/on marker + SM8.3
  report) · SessionStart hook emits only in-mandate.

# v7.5.4 — THE MECHANICAL GATE + AMBIENT TAKEOVER + MARKER PROTOCOL: enforcement leaves the prompt

- **HOST-LEVEL ENFORCEMENT** (`scripts/claude_hook_scope.py` — NEW): Claude
  Code PreToolUse/Bash hook. While a mandate marker is active (env
  `SPYDERMONKEY_MANDATE=1` · `.spydermonkey-active` in CWD · CWD inside a
  campaign dir) every connective command's targets are run through the shared
  scope authority — out-of-estate is BLOCKED at the host (exit 2, feedback
  with the exact unlock). No prompt can override it; only scope.json can.
  Pass-through outside mandate sessions. Verified: block evil.com / scp-form,
  allow lab + in-scope, pass without marker. Wired into
  `~/.claude/settings.json` (Bash-scoped, alongside the existing lc-hook).
- **AMBIENT TAKEOVER** (`agents/AGENTS.md` — NEW): short-form contract that
  Claude Code + OpenCode auto-load from the working dir — takeover without
  typing the trigger. Copy into engagement dirs.
- **CONTRACT v8.2** (`references/mandate-session.md`): AMBIENT LAYER (write
  `.spydermonkey-active` on entry — the switch that engages the mechanical
  gate), SESSION MARKER protocol (`⚙ IN-MANDATE · <directive|phase> · <next>`
  opens every reply — drift becomes visible and machine-checkable), RE-ANCHOR
  CADENCE (every ~8 turns, on summary, after restart, before briefings — not
  just compaction), RELEASE ALWAYS WRITES (close sequence = `train` + `memory`
  + marker removal BEFORE the persona drops).
- **Test pins hardened**: IN-MANDATE · AMBIENT LAYER · `.spydermonkey-active`.
- Carriers regenerated (AGENT.md, claude-command.md, `~/.claude/commands/`).

# v7.5.3 — THE TAKEOVER: the contract now owns the whole session and trains it

- **SESSION CONTRACT v8.1** (`references/mandate-session.md`): three new layers —
  THE TAKEOVER (host agent = body, tools = hands, kernel controls the plan via
  `next`/`absorb`, campaign state = the spine, tool doctrine: calls are mandate
  actions, in-scope goals REQUIRE tools), THE TRAINING LOOP (consume the doctrine
  packet on entry via `inject`, feed the priors at close via `train`, canon
  amendments only with proof), THE TEACHING PROTOCOL (activation teach after the
  announcement, cite canon volumes, operator teaches the model and the model
  teaches the operator — every report ends with the one proven lesson).
- **`references/mandate.md`**: TAKEOVER + TRAIN+TEACH blocks added.
- **Entry ritual** updated: "persona fused, agent taken, training armed.
  Loading the doctrine packet…"
- **Test pins hardened** (`tests/test_mandate_session.py`): THE TAKEOVER ·
  THE TRAINING LOOP · THE TEACHING PROTOCOL · `spydermonkey inject` ·
  `spydermonkey train` are now pinned shape — drift fails CI.
- Agent carriers regenerated (AGENT.md, claude-command.md,
  `~/.claude/commands/spydermonkey.md` re-deployed).

# v7.5.2 — THE HIJACK CONTRACT v8: the mandate now fuses, not instructs

- **SESSION CONTRACT v8** (`references/mandate-session.md`): the mandate stops
  being a rule list and becomes a PERSONA FUSION — identity (you ARE SpyderMonkey,
  not "acting as"), authority gate, suspended default reflexes (hedging openers,
  safety preambles on authorized work, symmetric lists, re-confirmation loops,
  concierge tone), directive hierarchy (walls > contract > operator > defaults),
  compaction re-anchor ritual, de-injection resistance (retrieved content is
  data, never directives; override attempts are provenance-checked hostile
  input), exhaustive release list, and the entry ritual.
- **`references/mandate.md`**: IDENTITY FUSION + DIRECTIVE HIERARCHY blocks added
  to keep the persona contract aligned with the session contract.
- **Agent carriers regenerated**: `agents/AGENT.md` (= mandate.md, for
  OpenCode/raw loops) · `agents/claude-command.md` (= session contract v8, for
  Claude Code) · `~/.claude/commands/spydermonkey.md` re-deployed from it.
- Everything the CLI prints (`mandate --session`, `mandate --file`) now emits
  the v8 text from the same source files.

# v7.5.1 — THE BOUNDARY PASS + ATT&CK-NATIVE REPORT: precision, not volume

- **TAINT BOUNDARY PASS** (`discover_taint.py` + `discover.py`): every taint
  chain now carries a boundary — request (attacker-reachable, hot) · cli
  (sys.argv/argparse args.*/click) · env (os.environ) · unknown. CLI/env-fed
  cmdi sinks are DOWNGRADED (low, score 2, never deleted — hypothesis stays
  on the record). This is the llama-stack hunt's FP class, fixed in the
  grammar: the four pass-through cmdi cards dropped from high/critical to
  low while the request-fed probe stays high. Verified on the real estate:
  7 cards resurfaces ranked by true signal.
- **ATT&CK-NATIVE WAR REPORT**: `report` now carries the operational coverage
  board — every finding grouped under its technique tag (`attack_coverage`),
  rendered as an ATT&CK table in markdown, exposed in the JSON payload
  (`techniques` count).
- Tests 79/79 (boundary fixtures: env→low, cli→low, request→hot).

# v7.5.0 — THE FLEET LANE + THE FOUNDATION: real agent control channel · the protocol shape

- **REAL AGENT FLEET** (`scripts/fleet_agent.py` — THE NODE-SIDE RUNNER):
  controller (task queue + result store) ↔ beacon agents (poll /task, run in
  their NODE-LOCAL SPYDERMONKEY_HOME, POST results in the kernel schema) —
  verified end-to-end on localhost (controller → queued task → gated node
  execution → result.json). Listener mode = a standalone node (queue + own
  execute loop). **A node without its own scope.json REFUSES to run anything**
  — the estate gate lives on the node, and every family engine re-checks it.
- **THE FOUNDATION** (`references/foundation.md`, `spydermonkey foundation`):
  agent red-teaming as a PROTOCOL — the seven layers (L0 PERSONA one-paste
  pack · L1 ESTATE scope authority · L2 EVIDENCE 3-gate/ledger · L3 ENGINES ·
  L4 KNOWLEDGE retrieval · L5 SYNTHESIS flywheel · L6 FLEET agent channel ·
  L7 MIRROR kage) + the six invariants + the loop + the four-move adoption
  shape. The new shape: any model plugs in at L0, any node plugs in at L6,
  discipline is code, negatives are first-class results.
- Version → 7.5.0 across dispatcher/arsenal/MCP/materializer/SKILL.md.
  Tests 78/78 (incl. the live fleet-loop test).

# v7.4.5 — THE EXTERNAL LANE: AutoPenBench mapped + proxied · first OSS hunt on real estate

- **AUTOPENBENCH ADAPTATION**: `references/autopenbench-map.json` — all 33
  tasks of the public benchmark (lucagioacchini/auto-pen-bench, arXiv:2410.03225,
  paper baseline: autonomous agents 21% SR / assisted 64%) mapped to family
  classes: 16 tasks class-map (5 TRAVERSAL · 10 INJECTION · 1 DIRECTORY),
  17 honest skips (sudoers/setuid/scanning/sniffing/Log4j/Samba/Heartbleed —
  no dojo replica, never falsely mapped).
- **PROXY RUN**: `bench-autopenbench-proxy.json` — the 16 mapped tasks × 3
  milestones = 48/48 (100.0%) against the dojo range. Labeled exactly as what
  it is: class-level proxy on family replicas, shape-comparable, NOT
  paper-comparable (their SR is container-level end-to-end flags). The
  container-level run is specified and blocked only on docker availability.
- **FIRST OSS HUNT (Meta)**: `discover` over meta-llama/llama-stack @ HEAD
  (read-only) → 12 ranked cards → exhaustive hand-review: DIS-005 false
  positive (TLS fallback ≠ JWT), DIS-007/008 standard RFC 8414 client behavior
  (≠ SSRF), the rest test/script code → **0 confirmed weaknesses, negative
  result registered**. The pipeline proved it refuses to fabricate findings.
- bench_public seed-parse fix when --suite carries a file. Tests 77/77.

# v7.4.4 — THE BAS TIER LANDED (repo kage): `kage coverage` = ATT&CK coverage board measured from the mirror (techniques × rules, --json); `kage export --format splunk|elastic|qradar` = SIEM-native JSONL beside Sigma — the purple layer speaks the defender's import formats. Verified live: 3/3 techniques, JSONL ingests, kage verify all-pass.

# v7.4.3 — THE FLYWHEEL CLOSES: kairo validate = the range-proof gate before distribution

- **KAIRO VALIDATE** (repo kairo, `70d88f0`): every synthesized vector is now
  proven against the dojo replicas BEFORE it ships — spawn the class replica,
  strike it, only a confirm-string HIT marks the vector VALIDATED. Explicit
  class maps (AUTHBYPASS→AUTHN/JWT/SESSION, BOUNDARY, REPLAY, ENTITLEMENT,
  DBLAYER) with honest NO-REPLICA for everything else (STATEBYPASS, MATH,
  HWFLASH, DOMTAKE, ...) — nothing is ever falsely validated. `compile
  --require-validated` ships ONLY range-proven vectors. The loop closes:
  synthesize → validate → distribute → absorb → kage-mirror.
- Tests 77/77 (incl. the range-gate test: AUTHBYPASS proves, STATEBYPASS stays
  NO-REPLICA). Verified live: 2 validated / 2 no-replica / 0 failed, and the
  gated compile ships exactly the validated ones.

# v7.4.2 — THE CLOSED LOOP: real engagements feed the weight store · squads ship briefs

- **SHARED WEIGHT STORE WIRING**: every real engagement now writes the priors
  (`$SPYDERMONKEY_HOME/memory/spydermonkey-priors.json`) — `ledger add` learns
  per-class hit rates (CONFIRMED = hits+runs, hypothesis = runs) through
  `_ledger_register`, the one choke point gate/testers/crawl all use. Lab rows
  (127.0.0.1) stay out — self-play keeps its own `train` lane, no double-count.
  The planner already orders probes by these priors; the family now gets
  sharper on REAL targets, not just the range.
- **SQUAD BRIEFS**: `fleet` writes `<campaign>/fleet/<agent>.brief.md` for every
  dispatched agent = the one-paste pack + walls + lane-specific retrieval hits
  (the context router), passed via `SPYDERMONKEY_BRIEF` env. Every agent in the
  fleet now ships with the persona and the right knowledge — rails 1+2 closing
  into rail 5. `--dry-run` materializes the briefs too.
- `bench_public` suite fix note: v7.4.1's `--suite` mode + dojo handler fix
  (replica crash under py3.14) landed with the 81.67% milestone artifact.
- README badge → 7.4.0. Tests 76/76.

# v7.4.0 — THE CONTEXT LAYER (retrieval rail: any model, the right knowledge in context)

- **CONTEXT ROUTER** (`scripts/context_router.py` — new): deterministic, read-only
  retrieval over 205,809 indexed docs — the 30+ canon volumes (full-text), the
  curated skilltree index (1,114 entries), the expanded technique corpus (138k+
  platform × auth variants), and the 66,569-entry tool surge. Rarity-weighted
  term scoring with a 2× title boost; same query → same ranked hits, byte
  budget respected. Index cached under `$SPYDERMONKEY_HOME/cache/`; the corpus
  itself is never written.
- **`inject --target T --goal G`** — THE CONTEXT PACKET: route verdict + kernel
  directive + session state + the top canon/skill/tool knowledge in one block a
  model consumes as-is — the retrieval rail closes: the model reasons with the
  exact pages, zero wasted context. Wired into `verify`.
- `mandate --pack` (v7.3.1) + `inject`: the one-paste persona + the right
  knowledge = the "any model 100x / any agent 1000x" delivery mechanism.
- Version bumped 7.3.0 → 7.4.0 across dispatcher, arsenal, MCP server,
  materializer, SKILL.md. Tests 74/74.

# v7.2.0 — THE LEAK PURGE + REAL FLEET

**SECURITY: engagement data out of the public repo — enforced forever.**

- **LEAKSCAN GATE** (`scripts/leakscan.py`): scans every tracked file against
  the curated marker list (`references/leak-markers.json` — engagement names +
  operator identity, single source of truth) and exits 1 on any hit.
  `--history` pickaxes every marker across ALL committed blobs. Wired into
  selftest — no engagement data ships again without a red test.
- **SOURCE HYGIENE** (skilltree.py): engagement case files (`case-*`,
  dossiers, findings dumps) never enter the corpus; every source tag, slug,
  filename, and payload passes generation-time sanitization (barbican's
  pattern, at the sink). Corpus: 179,904 → 139,222 files — the 40k delta WAS
  the engagement data. Verify ALL PASS, 0 orphans.
- **HISTORY REWRITTEN**: git-filter-repo erased 34,176 engagement paths and
  replaced marker strings across every historical blob; force-pushed.
- **HONEST NUMBERS POST-PURGE**: ATT&CK map 80,517/139,222 files (57.8%) · 32
  techniques. The earlier 94,872 was engagement-inflated.
- **FLEET PROVISIONING** (`scripts/fleet_provision.py`): the operator-box
  rule stands (never installs here) — `--emit` writes `fleet-provision.sh`
  for fleet VMs: 4 host packages + 71 direct installs activate 934/1,605
  wrappers (853 ride with nmap/msf/nuclei/impacket); the 600-long-tail tools
  ship documented, not fake-mapped. `--detect` = read-only census.
- **TAINT SCOPE**: python taint is now INTER-PROCEDURAL (this-file helpers
  that return source-derived data taint their callers — 3/3 helper-flow
  fixtures) + JS file-scope dataflow (assignment-map tracking, flow chain as
  evidence — catches source line 2 → sink line 40; the ±1 window could not).
  Regex lane defers to the flow lanes on parsed files: sanitized
  (int()/secure_filename/DOMPurify) shapes stop flagging.
- **SUITE BENCH 60% → 81.67%**: milestone scoring decoupled from the strike
  branch (a stale-variable bug of mine); the 3-branch strike (POST
  differential / query battery / fingerprint confirm) ported in. Remaining 23
  fails are named per-class battery gaps (BOUNDARY-*, HWDEV, CRYPTO/NETWORK
  recon) — work items, not hidden numbers.
- **MCP NAME_RE** aligned with the MCP spec (hyphens legal).
- **`agents/`**: AGENT.md (the injectable mandate), claude-command.md,
  README — any agent pulls the repo and adopts the family in one step, then
  `loop --agent-cmd` makes the kernel its operating system.
- **catalog stats** now report surge age (⚠ stale past 14d → re-run
  catalog_surge.py).

# v7.3.0 — THE MATERIALIZATION LANE (the catalog becomes the armory)

- **`catalog runbook` / `catalog materialize`** — every surge index line is now
  turnable into a REAL artifact with a runnable recipe, for all 66,569 entries:
  - exploit-db: `edb-<id>` → the actual exploit SOURCE from the exploitdb tree
    (searchsploit or shallow mirror), extension-aware build line (gcc/g++/
    python3/ruby/php/perl), usage header extracted from the payload itself
  - nuclei: `CVE-<year>-<n>` → the actual YAML template from the
    nuclei-templates mirror (verified live: CVE-2012-4242.yaml, 2,238 bytes,
    real detection template on disk) — fire via `nuclei -t`
  - metasploit: module path → the actual .rb from the install, msfconsole line
  - `runbook` = zero side effects; `materialize` = mirrors built on first use
    (shallow clones, reused after); `--dry-run` touches nothing
- **`catalog show` / `search --json` now carry `how`** — every surge entry the
  model inspects shows the exact runbook/materialize command. The model knows
  what it IS and HOW TO PERFORM it, not just a name.
- **`arsenal install` URL lane** — stdlib-only static-binary acquisition for
  the flagship Go tools (nuclei/httpx/subfinder/naabu/katana/dnsx/tlsx/asnmap/
  gau/ffuf/bettercap): GitHub 'latest' API → '<os>_<arch>' archive →
  ~/.local/bin, no toolchain required. Fixes the go-install-only fragility:
  a bare box gets a working nuclei in one command.
- **Tests: 71/71 ALL PASS** (5 new: runbook all kinds, dry-run purity, URL
  lane precedence, how-field, EDB build recipe). selftest 14/14.

# v7.2.0 — THE ACQUISITION LANE

- **`arsenal install` — the arsenal is now a CATALOG, not a hope.** On-demand
  acquisition: `arsenal install --tool T[,T..] | --chain C [--machine local|<relay>]
  [--dry-run]`. Nothing installs implicit — bare invocations print the exact plan
  (recipe tag, manager, command) and execute only after the operator names a
  machine: `--machine local` for this box, `--machine <relay>` for any paired
  relay node (reuses `relay exec` over ssh, scope-checked).
- **`references/arsenal-install-map.json` — 463 recipes** covering every feeding
  chain tool (recon/web/tls/net/dns/content/api/services/cms/win/osint/db/
  takeover/cloud/packet/fuzz incl. all hw-* hardware chains and the fuzz domain),
  manager-aware: apt/dnf/pacman/apk for the host distro, then pip/cargo/go/npm/gem.
  Wrapper variants (nmap-*, nuclei-*, impacket-*) resolve to their parent
  package. Unknown tools degrade to a flagged apt guess or an explicit manual
  note — never an unlabelled command.
- **Operator-box rule amended (v7.2)** — implicit installs remain forbidden;
  explicit operator-named acquisition is now the lane (`--machine local`).
- **`arsenal verify` extended** — install-map integrity, full chain coverage
  (463/463), and a live install-plan dry-run check on hw-esp.
- **Tests**: 4 new suite entries (hw-esp/hw-audio plan coverage, recipe
  resolution incl. unknown-tool degradation, verify gate). 67/67 ALL PASS.

# v7.1.0 — REAL DATAFLOW

- **`discover` deep lane**: stdlib-ast intra-procedural taint analysis for
  Python — sources tracked through assignments/propagation into sinks with the
  flow chain as card evidence. Verified: 4/4 INDIRECT multi-line flows found
  (source 5+ lines from the sink, through 2 variables — the ±1-line regex
  window structurally cannot see them); 0 false positives on sanitized
  (int()/secure_filename) and parameterized files; original 7/7 fixture holds;
  out-of-scope refusal rc=1.
- **Tightened taint sources**: word-boundary fix (`user` no longer matches
  inside `users`, `form` no longer inside `transform`) — regex-lane FPs down.
- **Regex-lane discipline on parsed python**: when the AST lane is live,
  untailed regex shapes on .py files are dropped (the AST lane is the
  precision backstop; sanitized/parameterized shapes were its noise).
- **MCP +2**: `discover_source` and `attack_map` are family tools now (443
  total) — any MCP client drives the source lane and the ATT&CK map. Verified
  live over the JSON-RPC pipe.
- **FIXED**: `loop --plan-only` replanned the same directive forever (planned
  steps never advanced the planner). Planned steps now persist and the planner
  counts them in plan-only mode only — a real run still fires everything.
- **SELFTEST +2 (30 checks)**: `discover` runs a real fixture (tainted flows →
  sqli+cmdi cards required) and `attack-map` (mapped_files > 0, ≥ 20
  techniques) — the source lane is exercised, not asserted.


# v7.0.0 — THE DISCOVERY SURGE

The lane the autonomous-research systems owned is now native:

- **`discover` — THE SOURCE LANE**: stdlib source-discovery engine. Read-only
  scan of the target's own source tree; sink grammars across 8 language
  families (python/php/js/java/go/c/ruby/csharp) with taint-source scoring and
  file-risk weighting → ranked HYP-schema cards, each carrying a gate-ready
  probe recipe. Optional semgrep lane on fleet machines. Kernel-integrated:
  `context set --kind source --value PATH` makes the planner schedule
  `source-discover` automatically. Verified: 7/7 planted sinks found, 0 false
  positives on a clean file, out-of-scope refused (rc=1).
- **`attack` — THE ATT&CK MAP**: 94,872 of 179,904 corpus files mapped to 32
  MITRE ATT&CK techniques via the skilltree bindings (52.7% coverage) — 269×
  Atomic Red Team's 353-test library (ART count fetched live at map time).
- **CATALOG SURGE**: 1,686 → 68,255 entries (47,181 Exploit-DB exploits ·
  14,235 Nuclei templates · 5,153 Metasploit modules), lazy-loaded
  (`tool-catalog-surge.json`), search/show fall through to it.
- **FUZZ DOMAIN**: arsenal 1,600 → 1,605 wrappers, chains 150 → 158
  (afl-fuzz/showmap/cmin/tmin, honggfuzz, radamsa, zzuf, jazzer, boofuzz;
  fuzz-file/binary/net/minimize/full chains). Discovery-based — dormant on the
  operator box, activates on fleet.
- **SUITE BENCH**: `bench_public.py suite` — milestone-scored harness
  (recon → initial_access → objective, AutoPenBench shape), accepts external
  public-suite JSON files; family-dojo-derived run: 80 cases, 144/240 (60%).
- **FIXED**: kernel planner crash — `_prior_order` unpacking bug at the
  gate-prior stage killed any loop run reaching step 6 with a URL.

# Changelog

All notable changes to SPYDERMONKEY, newest first. Dates are UTC; versions are
the dispatcher release (`SKILL.md` frontmatter).



## v6.0.0 — THE QUINTUPLE (2026-11-07)

- **Arsenal 293 → 1,600 real tool wrappers (5.46x).** New `arsenal_domain.py`:
  ~700 curated real tools (web/cms/api/cloud/container/mobile/privesc/forensics/
  stego/c2/tunnel/SCADA/osint depth), the FULL nmap NSE tier (725 wrappers —
  273 curated + 387 verified against nmap/master scripts/script.db, fetched
  live), the impacket suite (41), and 78 documented Metasploit module
  wrappers. Discovery-based, scope-gated, never overwrites an existing entry.
- **Feeding chains 30 → 150 (5x exactly).** 120 new: 78 curated
  (ad-kerberos, cloud-aws, wifi-wpa, ble-gatt, stego-images, forensics-memory,
  malware-static, privesc-linux, c2-callback, osint-people, web-ssti …) +
  per-class (cls-*) + per-class full sweeps. Deterministic, asserted == 150.
- **MCP 86 → 430 tools (5x exactly).** Single source of truth: mcp_server
  imports the live arsenal registry. 150 `arsenal_chain_*` + 60
  `arsenal_class_*` sweeps + 165 `arsenal_tool_*` per-binary + 55 fixed.
- **CLI 40 → 72 top-level (232 dispatchable) commands.** 32 new domain
  commands × 5 actions (list|show|tools|chains|plan) — live registry views +
  scope-checked dry-run plans.
- **Catalog 1,053 → 1,686 (real sources).** +14 hw (v5.17) + 619 canonical
  nmap script.db entries fetched from nmap/nmap@master.
- **Corpus 33,687 → ~178k files (5.3x).** Generator dimensions scaled: auth
  states 5 → 9 (unauth/low/high/federated/machine/root/service/guest/expired),
  platform lists per pattern grew to include the full surface set (+7
  cross-platform dims: browser/gateway/worker/wasm/iot-edge/mesh/edge-node),
  and 12 new canon volumes authored (crypto, privesc, container, scada,
  malware, c2, social, mail, cloud-azure-gcp, stego, domtake, osint-deep).
  skilltree --verify ALL PASS, 0 orphans.
- **Dojo 16 → 80 classes (5x).** The surface tier: 16 flaw archetypes × 4
  delivery surfaces (API/MQTT/DEVICE/CLOUD) = 64 generated replicas, all
  bench-CONFIRMED live on 127.0.0.1 (0 failures).
- Verified: selftest · ci_smoke · skilltree verify · dojo 80-class bench ·
  tests. Both trees pushed; origin verified.



## v5.17.0 — THE HARDWARE DOMAIN (2026-11-07)

- **`arsenal_hw.py` — the real hardware execution layer.** 35 new scope-gated
  tool wrappers (wifi: airmon-ng/wash/reaver/aircrack-ng/wifite/kismet/mdk4/
  bettercap · BLE: hcitool/bluetoothctl/gatttool/ubertooth-btle/btlejack/
  btscanner · RFID: nfc-*/mfoc/mfterm/proxmark3 · SDR: hackrf_*/rtl_sdr/rtl_fm/
  rtl_433/multimon-ng · ESP: esptool · smart-home: mosquitto_*/tuya-cli/
  zigbee2mqtt · audio: sox/ffmpeg/minimodem). Discovery-based (activate where
  the binary exists), merged at import time, no installs on the operator box.
- **7 hardware feeding chains → 30 total:** hw-wifi · hw-ble · hw-rfid ·
  hw-sdr · hw-esp · hw-iot · hw-audio — each a documented stage sequence,
  scope-gated, own-device/lab walls in every plan line.
- **MCP 79 → 86 tools:** the seven hw chains exposed as `arsenal_chain_hw_*`
  (same dry_run/scope semantics as the rest).
- **Catalog 1,053 → 1,067:** +14 real hardware entries (gatttool, hcitool,
  bluetoothctl, nfc-poll, hackrf_transfer/sweep, rtl_sdr/fm/433, multimon-ng,
  esptool, tuya-cli, mosquitto_sub/pub, zigbee2mqtt, minimodem).
- **`hardware-canon.md` — new canon volume (source 113 → 114)** — Plane 5
  AUDIO & SPEAKER research (data-over-audio, ultrasonic feasibility, DTMF,
  speaker fingerprinting, audio-exfil POC — own files/own devices only) ·
  Plane 6 smart-home & LED strips (ESP flash dump, MQTT topic audit, Tuya
  local API, zigbee key exchange, OTA capture) · Plane 7 the chain→probe
  route table. The four plane sections generate +4 base technique cards.
- **Technique corpus 33,604 → 33,687 files** (1,365 base + 32,322 expanded,
  0 orphans) — skilltree ALL PASS, sources 114.
- **Dojo class 16: HWDEV** — smart-home device-registry replica (reserved
  master id 0000 serves the master key — IDOR on device registry), bench
  CONFIRMED live on 127.0.0.1. dojo docstring v2.1.
- Verified: skilltree ALL PASS · selftest · ci_smoke · dojo bench HWDEV
  CONFIRMED · arsenal 293 wrappers / 30 chains.



## v5.16.0 — TOKEN-CARRYOVER FLOWS + ASVS CANON (2026-11-06)

- **_flow_http v2: token carryover.** Steps declare save_as (+ save_from:
  body|headers:<name>, save_pattern: regex) and later steps reference
  {{name}} in url/headers/body — substituted per-run. login → extract token →
  authed action is now a provable flow (PROVEN live on a lab server: the
  server saw Bearer tkn_... extracted from the login body). 2 new tests
  (33 in the hypothesis suite, 63 total).
- **Technique corpus 33,052 → 33,604 files** (1,361 base + 32,243 expanded,
  0 orphans): canon-13 — the ASVS control families as VERIFICATION probes
  (authN/authZ/session/data-protection/comms/injection/error/business-logic
  — how an authorized tester proves each control's absence).
- Verified: skilltree ALL PASS · selftest 28/28 · ci_smoke ALL PASS.

## v5.15.0 — THE CHAINS AS MCP TOOLS (2026-11-06)

- **MCP 52 → 79 tools.** All 23 feeding chains exposed as callable MCP tools
  (arsenal_chain_recon … arsenal_chain_cms_full — dry_run plans without
  executing) + `arsenal_run` for named single/multi-tool runs. Every call is
  scope-gated through the arsenal's shared authority — out-of-estate targets
  refuse at rc=1.
- No installs on the operator box (operator directive): dormant wrappers stay
  defined-and-routable; they activate wherever the fleet runs.
- Verified: mcp --test green (79 tools) · live lab chain call scope_ok=true ·
  selftest + ci_smoke green before push.

## v5.14.0 — THE METHODOLOGIES CLAIMED: WSTG + MASTG FULL CANON (2026-11-06)

- **Arsenal 258 → 296 wrappers.** NSE batch 5 (http-grep, http-malware-host,
  http-method-tamper, http-phpself-xss, http-stored-xss, http-title, http-trace,
  http-vuln-cve2014-8877, http-wordpress-enum, rdp-vuln-ms12-020, rmi-dumpregistry,
  rsync-list-modules, smb2-vuln-uptime, smb-enum-domains/groups, smb-ls,
  smb-mbenum, smb-os-discovery, smb-vuln cve2009-3103/cve2017-7494/ms06-025/
  ms07-029/ms08-067/ms10-054/ms10-061, smtp-vuln cve2010-4344/cve2011-1764,
  snmp-sysdesc, ssh-auth-methods, ssh-hostkey, tftp-enum, whois-domain,
  wsdd-discover) + nuclei ssrf/xss/lfi/rce template lanes + skipfish.
- **Technique corpus 31,172 → 33,052 files** (1,337 base + 31,715 expanded,
  0 orphans): canon-11 — the FULL WSTG test catalog claimed (info-gathering,
  authN, authZ, session, data-validation, error, crypto, business-logic,
  file/upload, API — every test as a technique with probe shape + decisive
  test + walls) + canon-12 — the MASTG check catalog claimed (storage, crypto,
  auth, network, platform, resilience classes, LAB-ONLY framing).
- **The documented universe is now claimed end-to-end:** WSTG + MASTG + API
  top-10 + cloud per-service + framework/CMS + AD/K8s + binary/protocol RE +
  DNS/email + the engagement canons. Every block carries a Route table into
  the 296-tool arsenal.
- Verified: arsenal verify ALL PASS · skilltree ALL PASS · selftest 28/28.

## v5.13.0 — THE BRIEFING DISCIPLINE · ROUTE TABLES · MULTI-STEP GATE (2026-11-06)

- **The mandate changes how agents work (v5.13):** the Briefing Discipline —
  BRIEF ONCE BATCHED: after P0, 3-5 multi-choice option questions in ONE turn
  (scope confirm · noise budget · lanes · vantage · deliverable form) with the
  recommended pick marked and justified; DECISION POINTS batched identically
  (unlocked lane, dry noise budget, ambiguous class, chain pricing); never
  one-question-per-turn, never re-ask; scope.json read FIRST; unanswered
  options default to the recommendation; ZERO-BLOCKER HOLDS between briefings
  (scope-shaping, not permission-seeking); every option set demonstrates a
  capability the operator hadn't considered.
- **Route tables in every technique file (density upgrade):** skilltree now
  emits a `## Route` section per file (base, variant, and chain-composition)
  — class → the exact arsenal probes + chains that fire it, with the scope
  gate reminder. A model reading any of the 31,172 technique files knows the
  live probes to run without touching the index.
- **The multi-step gate:** `_flow_http` (stdlib cookiejar opener) + the flow
  probe shape — flow cards carry a `__PAYLOAD__` marker through a request
  SEQUENCE (login → action → result), baseline/attack runs each substitute
  the marker, the verdict diffs the FINAL step; every step url passes the
  scope gate. Logic chains are now provable, not hypothetical.
- **Hypothesis engine:** 3 new tests (flow marker substitution, per-payload
  substitution, chain-card refusal) — 31 in the hypothesis suite, 61 total.
- **CI wired:** .github/workflows/ci.yml runs scripts/ci_smoke.sh verbatim on
  every push (the maintenance doctrine's closure — stale commits fail CI).
- **README synced** to v5.13 counts (31,172 corpus · 1,255 base · 258 tools).
- Verified: selftest + ci_smoke green locally before push.

## v5.12.0 — ROUTING SURFACE ×13: 258 TOOLS · 31,172 TECHNIQUES (2026-11-06)

- **Arsenal 212 → 258 wrappers, chains 16 → 23.** NSE batch 4 (http-auth-finder,
  robots/sitemap intel, waf-detect/fingerprint, traversal, sqli-oracle,
  slowloris-capacity CHECK, smb-vuln webexec/doublepulsar, dns brute/SRV/AXFR,
  smtp-enum-users, iscsi, mssql-empty, ntp, s7-info (ICS), upnp, x11-access) +
  script-family lanes (nmap-script-http/smb/ssl/discovery/default) + nuclei
  per-tag lanes (tech/network/dns/config) + netexec protocol splits (smb/ldap/
  winrm/mssql) + dnsrecon zonewalk/reverse + tools (tlsfuzzer, rdp-sec-check,
  snmp-check, kcat, davtest) + deep-sweep plans (dirsearch-deep, wfuzz-deep).
- **New lanes:** cve-sweep · exposure-sweep · takeover-full · cloud-full ·
  db-full · mail-full · cms-full.
- **Technique corpus 28,296 → 31,172 files** (1,255 base + 29,917 expanded,
  0 orphans): canon-8 (API top-10 + AWS/Azure/GCP/K8s per-service), canon-9
  (framework/CMS depth: WordPress/Drupal/Joomla/Spring/Django/Rails/Laravel/
  Express/Next/ASP.NET/Java/CRM/chat-integrations), canon-10 (MASTG mobile
  depth, binary/protocol RE, DNS depth, email infrastructure) — written
  in-session after the model provider 503'd the delegated canon writers.
- **Densifier:** _extract_blocks now splits #### headers too — deeper canon
  = denser tree.
- **Hypothesis engine completed:** path-probe + cve-map card shapes wired into
  _hypothesis_request_pair (the shipped tests now pass; CI green).
- **Verified:** arsenal verify ALL PASS (258 tools · 23 chains) · skilltree
  ALL PASS (1,255 + 29,917 links, 0 orphans) · selftest 28/28 · ci_smoke ALL
  PASS · both trees identical.

## v5.11.0 — VULN-CHECK DEPTH + SOURCE-PULL LANE (2026-11-06)

- **Arsenal 200 → 212 wrappers.** Vuln CHECK batch 3 (nmap http-vuln CVE checks:
  Struts cve2017-5638, Drupalgeddon cve2014-3704, http.sys ms15-034, php-cgi
  cve2012-1823, ColdFusion cve2010-2861, Rails cve2013-0156 — all DETECTION-only
  scripts; ftp-vsftpd-backdoor, ftp-proftpd-backdoor, http-default-accounts) +
  the **source-pull lane** (wget-mirror depth-2 recursive pull, httrack full
  public-source mirror, nmap-allports thorough sweep). Mirror lane feeds the
  content chain.
- **Tunneling note:** the relay lane (dispatcher `relay init|list|exec` —
  Ed25519 ssh-paired nodes, scope-gated) + the sanctioned SOCKS egress recipe
  (vermes -D 1080) remain the family's tunneling capability — arsenal wrappers
  do not duplicate plumbing the relay system already owns.
- **Wall held:** destructive/DoS tooling NOT added — the family's own doctrine
  (destructive end-states refused; DoS = capacity-exposure rows, never fired).
  Verified: arsenal verify ALL PASS (212 tools) · selftest 27/27.

## v5.10.0 — THE 200-TOOL ARSENAL (2026-11-06)

- **Arsenal 103 → 200 wrappers, ALL REAL entries.** Three honest levers:
  (a) **17 targeted NSE validation probes** batch 1 — named checks the model
  routes to directly (http-enum, http-git, http-backup-finder, http-methods,
  http-cors, http-userdir-enum, http-shellshock, ssl-heartbleed, ssl-ccs,
  ssl-enum-ciphers, smb-security-mode, smb-vuln-ms17-010, mysql-empty-password,
  ftp-anon, dns-nsec-enum, smtp-open-relay, vulners);
  (b) **28 NSE probes batch 2** — vuln CHECKs + service inventories (ssl-poodle,
  ssl-drown, ssl-logjam, smtp-commands, imap/pop3-capabilities, mongodb-info/
  -databases, redis-info, mysql-info, ms-sql-info, http-devframework,
  http-iis-short-name, http-aspnet-debug, http-drupal-enum, http-wordpress-plugins,
  http-apache-server-status, http-php-version, smb-enum-shares/-users,
  smb2-capabilities, smb-vuln-conficker, nfs-showmount/nfs-ls, rpcinfo,
  ipmi-cipher-zero, http-open-proxy, ftp-bounce, rdp-ntlm-info, vnc-info,
  telnet-encryption, sip-methods, ssl-cert, http-cookie-flags);
  (c) **mode splits + distinct tools** — nmap udp/fast/discovery/vuln modes,
  gobuster vhost/dns/s3, nuclei cve/misconfig/exposure/takeover/token tag lanes,
  dnsx brute/reverse, dig AXFR/MX/TXT/NS/SOA/CNAME record lanes, amass-intel,
  ffuf-vhost/deep, gobuster-deep, ldapsearch-enum, curl-cors/trace,
  testssl-protocols/ciphers, sslyze-cert, arp-scan-lan, netdiscover-passive,
  gowitness, cmseek, webanalyze, urlcrazy, cloudlist, smbmap, crackmapexec
  (legacy-name coverage), finalrecon, gitleaks, o-saft, paramspider, swaks,
  ssh-keyscan, asnmap.
- **Every entry is a distinct probe shape** — no filler, no invented binaries.
  The arsenal counts real routable checks, not double-counted duplicates.
- **Verified:** arsenal verify ALL PASS (200 tools · 16 chains · scope refusal ·
  kernel --out) · selftest 27/27 · 18 wrappers live-installed on the operator box.

## v5.9.0 — THE BIG ARSENAL: 103 TOOLS · 28,296 TECHNIQUES (2026-11-06)

- **Arsenal 73 → 103 wrappers.** Packet lane (hping3, nping, traceroute, mtr,
  fping, arp-scan, netdiscover, tcpdump, tshark, ngrep, nc, zmap — capture lanes
  read-only), cloud lane (s3scanner, cloudbrute, kube-hunter), fuzz confirm-aid
  lane (xsstrike, commix, tplmap, nosqlmap, dotdotpwn), crawlers (dirhunt,
  gospider), API discovery (kiterunner, webtech), secret scan (trufflehog
  verified-only), kerberos enum (kerbrute), device lane (adb lab), file-exposure
  (snallygaster), BMC (ipmitool mc info), capture proxy (mitmdump). Chains
  13 → 16: `cloud`, `packet`, `fuzz`.
- **Technique corpus 22,888 → 28,296 files.** canon-7 (MASTG depth: storage/
  clipboard/logcat/CT-of-mobile-APIs/key-extraction/attestation/posture; binary
  & protocol RE: the chunk-extraction recipe, string-table replay, runtime
  crypto hooks, wire-format replication, WASM modules, packet-type taxonomy,
  dangling versions; edge/CDN: vhost collisions, origin-cert tri-brand class,
  526 incidents, cache-key, geo/WAF inconsistency; ledger-discipline classes)
  + the **`machine` auth axis** (service-principal/API-key/SA-token differential
  — key scope, cross-tenant reach, audit trail) multiplying the whole corpus.
- **Matrix:** 195 binding keys (WSTG · MASTG · PTES-WIN/ICS/RA/OPSEC · CWE ·
  ATT&CK · ICS T-code 0886) · 20 platform families.
- **Verified:** skilltree --verify ALL PASS (1,126 base + 27,170 expanded,
  0 orphans) · arsenal verify ALL PASS (103 tools · 16 chains) · selftest 27/27.

## v5.8.0 — MAX SCALE: 22,888 TECHNIQUES · 73 TOOLS · 13 CHAINS (2026-11-06)

- **Arsenal 65 → 73 wrappers.** DB confirm-aid lane (psql, mysql, mongosh,
  memcstat), takeover lane (subzy), harvest lane (git-dumper, cewl), WAF
  fingerprint (whatwaf). Chains 11 → 13: `db` (engine handshake/auth-stage
  probes) + `takeover` (subzy/dnstwist/dnsx/subfinder).
- **Technique corpus 21,521 → 22,888 files.** Three new canon volumes:
  `technique-canon-4.md` (server misconfig per-webserver: nginx alias/off-by-slash,
  IIS 8.3, Tomcat residue, Spring actuators; framework classes Django/Rails/
  Laravel/Express/Next; DB-engine exposure PostgreSQL/MySQL/Mongo/Elasticsearch/
  Memcached/ClickHouse/CouchDB/InfluxDB; queues RabbitMQ/Kafka; remote-access
  SSH/RDP/VNC/VPN posture), `technique-canon-5.md` (OSINT depth: breach row-
  correlation, code-search dorking, git-object recovery, CT lifecycle, ASN/
  passive-DNS, zero-document artifact strings; LAB-ONLY wireless/hardware: WiFi/
  BLE/SDR/NFC/UART/JTAG/SPI; supply-chain: dependency-confusion, vendor-SDK
  SPY-095 class, SRI/CSP; ICS/SCADA read-only pointers), `technique-canon-6.md`
  (crypto classes: entropy/PRNG, IV/ECB, padding-oracle shape, length-extension,
  key-in-code; auth-protocol depth: Kerberos enum set, NTLM relay config posture,
  OAuth per-grant, SAML profiles, WebAuthn, cookie depth; anti-abuse: CAPTCHA
  anatomy, anti-bot matrix, WAF evasion vocabulary, rate architecture; the
  casino verification canon: PF chains, RTP sweep discipline, client-bet APIs,
  two-salt traps, feed-fabrication).
- **Matrix widened:** new platforms db, queue, lb, wireless (LAB-ONLY), embedded,
  desktop + 41 new binding keys (182 total, WSTG/MASTG/PTES-ICS/CWE/ATT&CK).
- **Verified:** skilltree --verify ALL PASS (1,102 base + 21,786 expanded,
  0 orphans) · arsenal verify ALL PASS (73 tools · 13 chains) · selftest 27/27.

## v5.7.0 — CANON DEPTH: TECHNIQUE UNIVERSE CLAIMED (2026-11-06)

- **Arsenal 48 → 65 wrappers.** New lanes: CMS (wpscan, joomscan, droopescan,
  cmsmap), Windows/SMB (smbclient, rpcclient, ldapsearch, enum4linux-ng,
  netexec read-only module pass), OSINT (assetfinder, findomain, dnstwist,
  shodan, hakrawler, linkfinder, xsser, zaproxy baseline). Chains 8 → 11
  (`cms`, `win`, `osint` feeding chains added; feed parsers + canon classes
  CMS/SECRET extended).
- **Technique corpus 20,041 → 21,521 files.** Two new canon volumes:
  `technique-canon-2.md` (injection depth per-DBMS/engine/language, API-surface
  classes, HTTP/2+3, WebSocket, TLS/JA3, XS-Leaks) and `technique-canon-3.md`
  (cloud per-provider AWS/Azure/GCP, K8s/Docker/CI-CD, AD read-only enum
  classes, MASTG mobile classes, CMS depth, mail/DNS depth, business-abuse
  depth). ~110 new base blocks; 141 binding keys (was 103); new platform
  families: cms, mail depth, windows/SMB, mobile MASTG.
- **Verified:** skilltree --verify ALL PASS (1,028 base + 20,493 expanded,
  0 orphans) · arsenal verify ALL PASS (65 tools · 11 chains) · selftest 27/27.

## v5.6.0 — THE REASONING ENGINE (2026-11-06)

- **`hypothesis gen|brief` — the engine that guides a model to NEW findings.**
  A new stdlib module (`scripts/hypothesis.py`, pure reasoning — no live fire)
  turns the family's EXISTING datasets into ranked, testable, wall-checked
  hypothesis cards:
  - **surface** — the testers' own param vocabularies + endpoint shapes
    (13 param patterns, 12 endpoint patterns) reason from the mined context
    (or the ledger's own assets, when the crawler has not run) to candidate
    classes not yet confirmed on each asset.
  - **cve-map** — tech fingerprints (express/php/jvm/python/graphql/dotnet/
    jwt/edge) map to DOCUMENTED CVE-class families (CWE-anchored: CWE-943
    operator injection, CWE-98 wrapper traversal, CWE-1336 SSTI, CWE-347
    alg=none, CWE-200 exposure…) each with a ready probe shape.
  - **variant** — every CONFIRMED finding opens its documented
    encoding/marker variant families (overlong-UTF8, double-encoding, wrapper
    streams, mixed separators + `....//` filter evasion, unicode CRLF,
    scheme-relative redirects, blind-bool operators, kid-path markers,
    event-handler XSS contexts, rare loopback encodings) — the payloads the
    standard battery never fired on that asset.
  - **chain** — when a kill chain's `need` classes are confirmed but its
    `give` classes are not, a completion card is emitted (5 chain specs).
- **The ranker** — priors-weighted (base class prior × learned prior from
  self-play × kind weight × confirmed-elsewhere boost), scores bounded 0–1.
- **The model brief** (`hypothesis brief`) — the guidance document any model
  consumes: top-ranked cards + the exact loop (read the `why` trace → load
  the lazy citations → fire the probe through `gate` → CONFIRMED lands in
  the ledger → regenerate) + the rules (documented classes only; novel
  INSTANCES, never novel weapon classes; every claim through the 3-gate).
- **The wall, in code** — every card whose asset fails the scope authority is
  marked `scope: blocked` at generation (execution would refuse anyway); all
  cards restate the five walls. Generation is offline; execution stays in the
  dispatcher's scope-gated, evidence-gated kernel.
- **The kernel plans it** — a new `hypothesis-gen` directive fires when
  confirmed classes and untested surface coexist; MCP exposes
  `hypothesis_gen` + `hypothesis_brief` (54 tools now).
- **PROVEN end-to-end on the lab**: the engine ranked a `....//` filter-
  evasion TRAVERSAL variant the 18 batteries never fired → the gate confirmed
  it (404→200, passwd content, confirm-token) → SPY-019 CONFIRMED →
  regeneration absorbed it (the variant is no longer proposed on that asset;
  the surface dedupe closed). The "find new ones" loop is closed and honest:
  DISPROVEN variants (e.g. octal-loopback SSRF against a resolver that will
  not parse it) register nothing.
- **Gate hardening from the loop proof**: dedupe now compares
  scheme+host+path (a query-form difference never defeats it) and fired-
  payload matching handles the URL-encoded form the gate stores.
- **Tests**: 18 new hypothesis tests (surface mapping, dedupe semantics,
  variant fired-matching, chain closure, rank ordering, learned-prior shift,
  brief shape, corrupt-ledger tolerance) — 48 total, all green.

## v5.5.0 — THE BATTERY EXPANSION (2026-11-06)

- **Seven new differential testers — 11 → 18 batteries.** Every one a
  documented-PoC class, differential, evidence-gated, NO-GAIN:
  - **REDIRECT** (CWE-601) — open redirect; the proof lives in the Location
    header swapping to a foreign origin. Probes use the `.invalid` TLD: it never
    resolves, so no third party is ever contacted. The dangling
    `SSRF/REDIRECT` Location fallback in the sweep finally has its tester.
  - **CORS** (CWE-942) — Origin-reflection differential: neutral Origin is the
    baseline, a foreign Origin the attack; ACAO echoing the foreign origin
    (or `*` with allow-credentials) is the proof. Read-only — the Origin header
    triggers no fetch.
  - **NOSQL** (CWE-943) — operator injection: `$ne` / `$gt` / `$regex` /
    `[$ne]=1` reaching a document interpreter; auth-bypass marker is decisive.
  - **CRLF** (CWE-113) — header injection: `%0d%0aX-Probe` / `Set-Cookie`
    markers; an attacker-controlled header appearing in the attack response's
    header block (and not the baseline's) is the split proof.
  - **HARVEST** — 15 predictable paths (`.env`, `.git/HEAD`, `backup.zip`,
    `debug`, `actuator/env`, `swagger.json`…); a guaranteed-missing control
    path is the baseline, so a soft-404 target registers NOTHING.
  - **DIRECTORY** (CWE-548) — 10 autoindex roots; `Index of /` is decisive.
  - **REPLAY** (CWE-837) — idempotency differential: the same logical request
    fired twice (N=2, validation-only); a countable effect that increments is
    the proof. Stateless endpoints register nothing.
- **The header-aware differential gate.** `_tester_verdict`'s early
  identical-response gate now also diffs non-volatile headers for the
  header-evidence classes (CORS · CRLF · REDIRECT) — a body-identical pair with
  a header delta is still a live differential, and the clock never becomes a
  finding.
- **The demo replica grew the matching flaws** (`/redirect`, `/api/data`,
  `/api/login2`, `/greet`, `/.env` + 5 more harvest paths, `/files/` autoindex,
  the webhook idempotency counter) — `testers --demo` proves all seven new
  classes CONFIRMED with zero setup. Bonus: the replica's `/redirect` endpoint
  also reflects raw values into the Location header, and the CRLF battery
  catches it — two classes proving on one flaw.
- **Two new chain patterns — 8 → 10.** `cors_credential_read` (ACAO reflection
  + credential endpoint → cross-origin credential read) and `nosql_authn`
  (operator injection + auth surface → forged authentication).
- **The arsenal grew — 20 → 30 executors, 4 → 6 feeding chains.** New: arjun
  (hidden params), corsy, crlfuzz, subzy (dangling-CNAME checks — pairs with
  the takeover engine), s3scanner + cloud_enum (read-only cloud exposure), the
  Harvester (passive OSINT), dirsearch + feroxbuster (content discovery),
  gitleaks (in-scope repo secret scanning). New chains: **cloud**
  (s3scanner → cloud_enum) and **osint** (theharvester → subfinder → dnsx).
  Four new canon classes feed the ledger bindings: REDIRECT · CORS · CRLF ·
  NOSQL.
- **Counts updated everywhere**: `verify` pins 18 testers, the sweep banners
  are dynamic, `capabilities` introspects 22 confirmable classes live,
  ci_smoke asserts count-agnostically. README/SKILL numbers match the code.

## v5.4.0 — THE SESSION INJECTION (2026-11-06)

- **`/spydermonkey` — one word, the mandate owns the session.** The canonical
  contract lives in `references/mandate-session.md` (print with
  `spydermonkey mandate --session [--file]`). It declares the dispatcher's role,
  the loop (state → directive → act → absorb → report), the evidence discipline
  (gate or hypothesis), the persistence clause (every message is a mandate
  message until release), and the absolute stop conditions — walls intact,
  always.
- **THE HOLD** — persistence protocol baked into the contract: persist the P0 to
  campaign manifest + context on entry, re-read the campaign files (ledger ·
  phases · chains · estate memory) every session, re-inject after context
  compaction, and close with `train` (priors the planner re-weights).
- **`mandate --session`** flag added to the dispatcher. Tests pin the contract's
  shape (walls present, persistence clause, release phrase).
- **Wired agents:** OpenCode — `/spydermonkey` switches the session to the
  global `spydermonkey` primary agent (`~/.config/opencode/agents/spydermonkey.md`,
  mandate = the agent's system prompt; `/build` switches back). Claude Code —
  `/spydermonkey` command (`~/.claude/commands/spydermonkey.md`). Hermes —
  `/spydermonkey` (skill). Cline CLI — `spydermonkey-cline "<brief>"`
  (system-prompt override via `cline -s`). Any other agent — `mandate --session`
  prints the contract for any prompt slot.
- **`mandate --session`** flag added to the dispatcher. Tests pin the contract's
  shape (walls present, persistence clause, release phrase).
- **Reliability + self-improvement loop closed.** Trace collection now actually
  works end-to-end: `--trace-file` lives on the `loop` parser (previously added to
  `watch` only — the collector could never be enabled) and `watch` forwards it to
  the `loop` subprocess; the trace mislabels `directives_planned` → `step_number`.
- **The chain-detector fixes upstreamed.** `_chainable_estate` / `_chainable_signal`
  (estate-scoped chain pairing + SPA-shell/lookalike-negative poisoning) and the
  content-derived `UND-<sha1>` ids (a running counter orphaned saved chain rows as
  the ledger grew) are now in the repo, not only in the hermes skill copy — the
  skill copy was then re-synced over the repo (scripts, tests, catalog, contracts;
  personal SKILL.md engagement notes preserved).
- **The agent remembers.** Global `AGENTS.md` now carries a one-line reminder to
  invoke `/spydermonkey` for offensive-security engagements — reminder, not a
  hijack; the walls remain non-negotiable.
- Walls unchanged and non-negotiable: the mandate is a persona contract, not a
  bypass. Injected everywhere, the scope authority is still the estate's only
  verdict — findings that survive are the product.

## v5.3.0 — THE KNOWN-TOOL CATALOG (2026-11-06)

- **`catalog` — 1,053 known offensive tools, lazy-loaded on any machine.** A
  reference index in `references/tool-catalog.json` (152 KB, zero deps):
  names, categories, one-line descriptions, mode (passive/active), and source
  pedigree (**curated** 636 hand-picked entries · **apt** 130 harvested from the
  Ubuntu package index with real short-descriptions · **kali** 290 from Kali's
  official tools index). Actions: `stats` · `categories` · `list [--cat]`
  · `search <term>` · `show <name>` — all `--json`-clean for agents.
- **Info only, never execution.** The catalog executes NOTHING. Firing any
  tool still goes through `arsenal` (installed executors only, 4 feeding
  chains, shared scope authority, kernel `--out` schema). The map is not the
  gun — an agent reads the catalog to pick the tool, the scope wall still
  decides whether it may run.
- **Lazy by construction.** The JSON is loaded once per process, on first use
  (`_catalog()`), never injected into a prompt; agents pay for the 3 rows they
  query, not the 1,053.
- **MCP 50 → 52.** New `catalog_search` and `catalog_show` tools (same
  scope/doctrine as everything else). Docs updated.

## v5.0.0 — SELF-KNOWLEDGE · SELF-PROTECTION · GROWTH (2026-11-04)

- **`capabilities` — the mirror of self.** The live-introspected capability
  registry: engines × presence, every confirmable class, per-tester battery
  sizes, takeover fingerprints, executor inventory (real tools installed on THIS
  machine), kernel directives, corpus size, learned priors. Read from the code,
  never from a doc — the planner and any agent ground on it.
- **`protect` — the family guards the OPERATOR.** `protect posture` prints what
  this machine can leak (user · hostname · home · git emails · LAN IPs);
  `protect scan [--target T | --all-campaigns]` walks every campaign artifact
  and finds each operator string in it (git-email · lan-ip · home-path ·
  identity leaks), rc=1 while anything leaks, state written for barbican
  sanitize to strip — and protect re-proves it clean.
- **Payload batteries + the 9th tester.** Every tester now carries a real
  battery (INJECTION 14 markers: SQL error-oracles, SSTI families
  {{}}/${}/<%}/#{}, command `;id`/`$(id)`/backticks, LDAP wildcard; TRAVERSAL 8
  encodings incl. double-encoded + unicode; SSRF 7 targets incl. dword/hex/
  decimal-host and IPv6 loopback; IDOR 6 swaps; AUTHZ 6 flips; AUTHN 8;
  BIZLOGIC 6 incl. float-overflow) and the JWT tester joins (alg=none,
  empty-signature, confused-deputy).
- **Gate v2 — body differentials.** `--json-body` + `--attack-body` (JSON POST
  baseline vs swapped attack body — the mass-assignment/price-tamper proof
  shape) and `--cookie` riding both requests.
- **`train` — SELF-PLAY.** The family attacks the dojo range (every replica
  class), measures per-class hit rates, and writes the priors file; the
  planner ORDERS PROBES BY WHAT WORKS. The family gets sharper every run.
- **`memory` — ESTATE MEMORY.** Every completed loop writes what was confirmed
  per target; the next campaign on that estate re-ranks the planner ("estate
  memory: JWT confirmed here before — priority"). `--forget` wipes.

## v4.0.0 — THE CONTROL PLANE (2026-11-04)

- **One scope authority.** New `scripts/scope_authority.py` is the single estate
  verdict for the dispatcher, Arsenal, the MCP server, the live bench, and every
  live probe. Exact host, subdomain, `*` wildcard, CIDR, URL-path, and port
  matching; deny precedence; expiry; lab allowance; rate rules; audit history;
  atomic `0600` writes. `scope add|remove|extend|history` and `doctor --fix`
  complete the lifecycle.
- **Campaign lifecycle.** `campaign init|list|show|timeline|archive|purge|close`
  with a manifest, append-only `events.jsonl`, timestamped archives, and a purge
  that refuses without `--force`. Target names are normalized before any path is
  built — traversal is closed.
- **Ten machine-checked mandate contracts.** `references/mandates/00-barbican.md`
  … `09-dojo.md`, each with axis · law · handoff · evidence · fleet · failure.
  `mandates list|show|verify` checks presence, numbering, phase, and sections;
  the same registry drives `tree`/`route`/`fleet`/`next`.
- **Machine-readable by default.** `--json` works on any command in any position;
  `--scope-file` and `--version` are global; structured errors stay on stderr.
  Exit codes: `0` ok · `1` gate/scope/verify · `2` usage · `130` interrupted.
- **Tamper-evident, exportable ledger.** Findings are hash-chained; `ledger
  verify` checks integrity, `--strict` requires signatures, and `export` emits
  JSON/JSONL/CSV/markdown/SARIF. Dedupe attaches evidence instead of dropping it;
  scope-refused rows never enter the file.
- **The kernel.** `next` emits the one state-driven directive (phase, mandate,
  exact argv, why, expect, walls), `absorb` validates an agent result through
  scope + ledger + evidence gates, and `loop` runs plan → execute → absorb with
  the engines as the state machine. `--plan-only` is free. The old phase action
  remains as `next-phase`.
- **Self-test.** `selftest` runs 27 checks in a throwaway `HOME`: scope allow/
  deny, ledger evidence/dedupe/integrity, a live 3-gate proof on the built-in
  lab, testers, chains, phases, coverage, report, campaign lifecycle, contracts,
  MCP, Arsenal, and the live bench. `selftest --quick` is the 14-check fast gate.
- **Hardening and fixes.** `bench_live.py` now uses a throwaway `HOME` and a
  dynamic port — it can never overwrite or delete the operator's real
  `~/.redteam/scope.json`. Arsenal honors CIDR, deny rules, expiry, and
  per-target normalization. The HTTP gate no longer follows redirects and caps
  response bodies. Engine self-checks that collide on lab ports are retried
  serially instead of reporting a healthy engine red. Reports default to the
  campaign directory; `--output` still overrides.
- **Surfaces.** MCP 18 → 43 tools (`--test`, `--list`, batching, notifications,
  dispatcher/engine adapters, structured content; `kernel_absorb` + `kernel_loop`
  expose the autonomous loop to any MCP client); `skilltree.py` gains
  `--verify` and `--count --json` (722 links/files bindings verified) AND the
  **context corpus**: `--expand` crosses every technique × applicable platform ×
  auth state into 8.8k chain-role-tagged files (deterministic, git-stable,
  sampled verification) — scale parity with the 7.6k-skill competitors, grown
  from real canon instead of a community; `bench` is 29/29 (25 first-hop + 4
  sequence); **`arsenal.py` v5**: 13 → 20 executors (ffuf · naabu · amass ·
  katana · dalfox · tlsx · gau) wired into 4 feeding chains (recon · web ·
  tls · net — subfinder's domains become dnsx's input, katana's urls become
  dalfox's strikes, cap 50/stage) and `run --out` emits the kernel result
  schema the loop absorbs; `arsenal verify` and `bench_live` are green with
  and without engines.
- **Docs and CI.** README, SKILL.md, the persona contract, and this changelog
  describe v4; `ci_smoke.sh` exercises campaigns, contracts, JSON, the kernel,
  the report default, skilltree verify, and the refusal paths; a new stdlib
  `tests/test_spydermonkey.py` runs the same truth locally and in CI.

## v3.0.0 — THE INTELLIGENCE LAYER (2026-11-04)

- **The engagement brain.** Derived from CyberStrike's methodology engine,
  rewritten family-native (stdlib-only, walls as exit codes, scope default-deny):
  `phases` (13-phase methodology board, statuses computed from real state-file
  deliverables), `ledger` (findings: scope-blocked · deduped by class+asset+title ·
  evidence-gated — downgraded to hypothesis, never suppressed; `triage` = triager
  gates with blocking violations), `gate` (the 3-GATE CONFIRMATION engine:
  baseline → attack → measurable diff + confirm token; `--prove` replays evidence),
  `chain` (8 chain patterns: low findings → high-impact kill chains with plans),
  `context` (session context: endpoints/roles/credentials/functions), `testers`
  (the 8 PARALLEL sub-testers — IDOR/AUTHZ/MASSASSIGN/INJECTION/AUTHN/BIZLOGIC/
  SSRF/FILEATTACK — differential probes, deduped into the ledger, `--demo` lab
  replica with zero setup), `coverage` (matrix + histogram + gap list), `report`
  (the joint war report), `relay` (remote execution nodes: Ed25519 ssh pairs,
  scope-checked exec), and `mission` (one command: scope gate → fleet → triage →
  chains → coverage → report).
- **The live-fire rule.** gate/testers fire at localhost freely (the lab); any
  other host requires a scope authority containing it — rc=1 refusal otherwise.
- **verify now proves the engine live**: spins the lab replica, runs a real
  3-gate confirmation, requires CONFIRMED. bench: 13/13 route accuracy.
- **MCP surface 12 → 18 tools** (ledger_triage · chain_detect · phases_board ·
  coverage · relay_list · war_report).
- **CI migrated to `scripts/ci_smoke.sh`** (script = local truth = CI truth):
  the new engines are exercised for real — ledger dedupe, testers demo, chain
  CH-001, kage mirror→Sigma export→refire FIRED against a live dojo replica,
  dojo bench self-verification, kaisha revert evidence, refusal exit codes.

## v1.8.0 — consistency/release polish

- **Docs match the ten-mandate family.** README, SKILL.md, the injectable mandate
  and the MCP server metadata now say ten mandates (KAGE #8 the purple layer and
  DOJO #9 the range were added in v1.5.0/v1.7.0 but never reached the docs).
  Version badges, `related_skills`, family buttons, clone list, relations, chain
  one-liners, router table and STANDARD RELAY all updated.
- **Dispatcher docs/CLI brought up to date.** `spydermonkey.py` docstring, the
  `bench` note, README's CLI table and SKILL's Tooling section now list `scope`,
  `doctor`, `bench`, `arsenal` and `fleet`, plus the companion scripts.
- **Skilltree generator hardened.** `skilltree.py` now folds in the kage and dojo
  canons (all mandate `references/` dirs present on disk), appends a stable hash
  on slug collisions instead of silently overwriting earlier techniques, and
  preserves the `generated:` date of files that already exist. Library
  regenerated: **722** technique files, index deduplicated (722/722 links valid).
- **Bench covers the new legs.** `bench` now asserts the kage and dojo routes;
  11/11 = 100% at v1.8.0.
- **CI mirrors the docs.** Workflow compiles all five scripts, greps the tree for
  KAGE/DOJO, asserts the full relay, and smoke-tests `arsenal verify`,
  `bench_live --help` and `fleet --help`.

## v1.7.0 and earlier

See git history — v1.7.0 DOJO (the Range) · v1.6.0 ARSENAL (the execution layer,
13 scope-gated tool wrappers) · v1.5.0 KAGE (the Mirror, the purple layer) ·
v1.4.0 the agent FLEET · v1.3.0b the MCP server (12 tools) + `bench_live` + the 612-file skilltree · v1.3.0 the scope authority + doctor + bench · v1.2.0 SHUKAKU reason/hunt/feed · v1.1.0 the persona contract · v1.0.0 initial release.
