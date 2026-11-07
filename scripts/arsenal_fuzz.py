"""
ARSENAL_FUZZ — SPYDERMONKEY v7.0.0: the fuzzing domain.

The lane the AIxCC-class systems own: coverage-guided mutation against real
targets. Discovery-based (activates where the binary exists — no installs on
the operator box), scope-gated through the shared authority, lab-bound by the
no-gain walls: fuzzing targets declared estates or the local range only.

Merged after arsenal_hw + arsenal_domain via merge_fuzz(); never overwrites
an existing tool.
"""
from __future__ import annotations

# name → (capability, classes, plan, argv-template)
# argv template tokens: {t} target · {x} wordlist/extra (omitted when None)
ARSENAL_FUZZ = {
    # ── coverage-guided mutation ──────────────────────────────────────────
    "afl-fuzz":    ("coverage-guided file fuzzer", ("fuzz", "binary"),
                    "mutation loop against a target binary (corpus via {x})",
                    ["-i", "{x}", "-o", "out", "{t}", "@@"]),
    "afl-showmap": ("coverage trace capture", ("fuzz", "binary"),
                    "edge-coverage map for one input on the target",
                    ["-q", "-o", "map", "{t}", "@@"]),
    "afl-cmin":    ("corpus minimizer", ("fuzz", "binary"),
                    "minimize the corpus to the minimal coverage set",
                    ["-i", "{x}", "-o", "min", "{t}", "@@"]),
    "afl-tmin":    ("test-case minimizer", ("fuzz", "binary"),
                    "shrink a crashing input to the essential bytes",
                    ["-i", "{x}", "-o", "min", "{t}"]),
    "honggfuzz":   ("feedback fuzzer (hw perf counters)", ("fuzz", "binary"),
                    "instrumented fuzzing with hardware feedback",
                    ["-i", "{x}", "-W", "out", "--", "{t}", "__AFL_SHM_ID"]),
    # ── dumb mutation ─────────────────────────────────────────────────────
    "radamsa":     ("generational mutator", ("fuzz", "fuzz_file"),
                    "mutate a seed corpus file into N test cases",
                    ["-n", "1000", "-o", "%n.fuzz", "{x}"]),
    "zzuf":        ("transparent file mutator", ("fuzz", "fuzz_file"),
                    "deterministic bit-flip fuzzing of an input through the target",
                    ["-r", "0.01", "-s", "seed", "{t}", "<", "{x}"]),
    # ── language-VM fuzzers ───────────────────────────────────────────────
    "jazzer":      ("JVM coverage fuzzer", ("fuzz", "fuzz_java"),
                    "libFuzzer-style fuzzing for Java/JVM targets (hook jar via {x})",
                    ["--cp={x}", "--target_class={t}"]),
    # ── protocol/stateful fuzzing ─────────────────────────────────────────
    "boofuzz":     ("network protocol fuzzer", ("fuzz", "fuzz_net"),
                    "stateful protocol fuzz blocks against a service",
                    ["--host", "{t}", "--iterations", "1000"]),
}

# tools that accept the extra {x} argument
FUZZ_EXTRA = {"afl-fuzz", "afl-showmap", "afl-cmin", "afl-tmin", "honggfuzz",
              "radamsa", "zzuf", "jazzer"}

# tools whose target is a URL (none — fuzzers take binaries/hosts)
FUZZ_HTTP: set[str] = set()

# curated chains: name → ordered tool list (only installed tools fire)
_CURATED_CHAINS = {
    "fuzz-file":     ["afl-fuzz", "honggfuzz", "radamsa", "zzuf"],
    "fuzz-binary":   ["afl-fuzz", "honggfuzz", "afl-showmap", "afl-tmin"],
    "fuzz-minimize": ["afl-cmin", "afl-tmin", "afl-showmap"],
    "fuzz-net":      ["boofuzz", "radamsa", "honggfuzz"],
    "fuzz-java":     ["jazzer"],
    "fuzz-full":     ["afl-cmin", "afl-fuzz", "afl-showmap", "afl-tmin",
                      "radamsa", "boofuzz"],
}


def _build_chains(arsenal: dict) -> dict[str, list[str]]:
    """Curated chains + cls-* per class + *-full composites, arsenal-filtered."""
    extra: dict[str, list[str]] = {}
    for name, tools in _CURATED_CHAINS.items():
        sel = [t for t in tools if t in arsenal]
        if sel:
            extra[name] = sel
    # cls- chains: every fuzz class gets its own chain
    classes: dict[str, list[str]] = {}
    for tool, (_cap, cls_t, _plan, _b) in arsenal.items():
        for c in cls_t:
            if c.startswith("fuzz"):
                classes.setdefault(c, [])
                if tool not in classes[c]:
                    classes[c].append(tool)
    for c, tools in classes.items():
        extra[f"cls-{c}"] = tools[:8]
    # *-full composites
    for c in list(classes):
        extra[f"{c}-full"] = [t for t in classes[c]][:8]
    extra.setdefault("fuzz-full", [t for t in
                                   ("afl-fuzz", "honggfuzz", "radamsa", "boofuzz")
                                   if t in arsenal])
    return extra


def merge_fuzz(arsenal: dict, chains: dict, chain_names: set,
               feed_parse: dict, takes_extra: set, http_tools: set,
               chain_target: int = 8) -> int:
    """Fold the fuzz domain into the live registries. NEVER overwrites an
    existing tool; appends up to chain_target new chains."""
    new = {k: v for k, v in ARSENAL_FUZZ.items() if k not in arsenal}
    arsenal.update(new)
    takes_extra.update(FUZZ_EXTRA & set(new))
    http_tools.update(FUZZ_HTTP & set(new))
    extra = _build_chains(arsenal)
    added = 0
    for name in sorted(extra):
        if added >= chain_target:
            break
        if name in chains:
            continue
        chains[name] = extra[name]
        chain_names.add(name)
        added += 1
    return added
