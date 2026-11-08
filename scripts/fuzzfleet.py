#!/usr/bin/env python3
"""THE FUZZFLEET A/B (v7.9) — Mayhem's axis, contested with measured numbers.

Same engine (clang libFuzzer), same target, same time budget — the ONLY
variable is the family's orchestration layer:

    VANILLA       empty corpus, one worker, raw libFuzzer
    ORCHESTRATED  the family's grammar-seeded corpus (the testers' payload
                  vocabulary adapted to the target's protocol) + parallel
                  workers + auto-triage (every crash re-run and CLASSIFIED,
                  the ledger fed)

The claim under test: orchestration ≥ 5x on findings and/or time-to-first.
The number printed is what happened — no fudging; a miss prints as a miss.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent

# the family's grammar, adapted to the range target's protocol (LEN/DIV/FMT/
# PATH tags): the testers' payload vocabulary + the bypass shapes
GRAMMAR_SEEDS = [
    b"PATH:/etc/passwd",
    b"PATH://etc/passwd",
    b"PATH:/../../etc/passwd",
    b"PATH:/....//etc/passwd",
    b"PATH:%2e%2e%2fetc%2fpasswd",
    b"PATH:/etc/shadow",
    b"LEN:" + b"A" * 64,
    b"LEN:" + b"A" * 300,
    b"DIV:0",
    b"DIV:00",
    b"AUTH:x OR 1=1",
    b"AUTH:admin OR 1=1",
    b"ENC:%252e%252e%252fetc%252fpasswd",
    b"ENC:%2e%2e%2fetc%2fpasswd",
    b"ENC:..%252fetc%252fpasswd",
    b"FMT:%n%n%n%n",
    b"FMT:%s%s%s%s%s",
    b"FMT:%99999999d",
    b"PATH:/" + b"/" * 8 + b"etc/passwd",
]


def run_variant(tag: str, target: Path, seconds: int, orchestrated: bool,
                seeds_file: Path | None = None,
                dict_file: Path | None = None) -> dict:
    work = tempfile.mkdtemp(prefix="ff-" + tag + "-")
    corpus = Path(work) / "corpus"
    corpus.mkdir()
    if orchestrated and seeds_file:
        for i, seed in enumerate(seeds_file.read_bytes().split(b"\n--\n")):
            if seed.strip():
                (corpus / f"seed{i:02d}").write_bytes(seed)
    crashes = Path(work) / "crashes"
    crashes.mkdir()
    t0 = time.time()
    first_crash_t = None
    workers = ["-workers=2", "-jobs=2"] if orchestrated else ["-workers=1", "-jobs=1"]
    cmd = [str(target), "-max_total_time=" + str(seconds),
           "-max_len=512", "-rss_limit_mb=4096",
           "-artifact_prefix=" + str(crashes) + "/",
           "-print_final_stats=1",
           # fairness: BOTH variants run continuously — libFuzzer's default
           # stops at the first crash, which would waste the budget and
           # undercount BOTH sides
           "-fork=1", "-ignore_crashes=1", "-ignore_ooms=1",
           "-ignore_timeouts=1"]
    if dict_file:   # the FAIR baseline: vanilla runs the target's OWN dict
        cmd += ["-dict=" + str(dict_file)]
    cmd += workers + [str(corpus)]
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=seconds + 90,
                       env={**os.environ, "UBSAN_OPTIONS": "silence_unsigned_overflow=1"})
    elapsed = time.time() - t0
    arts = [c for c in crashes.iterdir() if c.is_file()]
    # auto-triage: re-run each artifact, classify by the failure signature
    classes = {}
    uniq = []
    for a in arts:
        rr = subprocess.run([str(target), str(a)], capture_output=True,
                            timeout=30)
        # v7.9 — ONLY real crashes count: the fork mode also writes oom/slow
        # artifacts; counting them manufactured noise on both sides
        if rr.returncode == 0:
            continue
        # the ASAN reports carry raw memory bytes — never text-decode raw
        err = (rr.stderr or b"").decode("utf-8", "replace")
        if "SENSITIVE-READ-REACHED" in err:
            cls = "TRAVBYPASS/sensitive-read"
        elif "stack-buffer-overflow" in err:
            cls = "MEMCORRUPT/stack-overflow"
        elif "overwrites-const-input" in err or "%n" in err or "FORMAT" in err:
            cls = "FMTSTR/format-string"  # %n of const data = the classic proof
        elif "division by zero" in err or "FPE" in err:
            cls = "ARITH/div-by-zero"
        elif "SEGV" in err or "deadly signal" in err:
            cls = "MEMCORRUPT/deadly-signal"
        else:
            summary = [l for l in err.split("\n") if "SUMMARY" in l]
            cls = "UNCLOSED/" + (summary[-1][-40:] if summary else "unknown")
        if cls not in classes:
            uniq.append(a)
            classes[cls] = str(a)
            # v7.9 — the fork mode's artifacts carry their mtime: the honest
            # time-to-first = the artifact's own write time, not the re-run
            m = a.stat().st_mtime - t0
            if first_crash_t is None or m < first_crash_t:
                first_crash_t = m
    return {"variant": tag, "elapsed_s": round(elapsed, 1),
            "artifacts": len(arts),
            "unique_classes": sorted(classes),
            "class_count": len(classes),
            "time_to_first_crash_s": round(first_crash_t, 2) if first_crash_t else None,
            "workdir": work}


def main() -> int:
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/tmp/range-target")
    seconds = int(sys.argv[2]) if len(sys.argv) > 2 else 60
    seeds_file = Path(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3] != "-" \
        else None
    dict_file = Path(sys.argv[4]) if len(sys.argv) > 4 else None
    if not target.exists():
        print("✗ target binary missing: " + str(target), file=sys.stderr)
        return 2
    van = run_variant("vanilla", target, seconds, orchestrated=False,
                      dict_file=dict_file)
    orch = run_variant("orchestrated", target, seconds, orchestrated=True,
                       seeds_file=seeds_file)
    ratio = round(orch["class_count"] / max(1, van["class_count"]), 2)
    ttfc = (van["time_to_first_crash_s"], orch["time_to_first_crash_s"])
    payload = {
        "lane": "FUZZFLEET — the orchestration A/B (Mayhem's axis, contested)",
        "engine": "clang libFuzzer (the engine is SWAPPABLE — afl++/honggfuzz "
                  "stay catalog-dormant per the operator-box rule)",
        "target": "tests/range_target.c — four bug classes (mem-corrupt · "
                  "arith · fmt-string · naive-guard bypass → sensitive read)",
        "protocol": "same engine · same target · same budget — the ONLY "
                    "variable = the family's orchestration (grammar-seeded "
                    "corpus + parallel workers + auto-triage)",
        "vanilla": van, "orchestrated": orch,
        "findings_ratio": ratio,
        "time_to_first_crash_s": {"vanilla": ttfc[0], "orchestrated": ttfc[1]},
        "orchestration_wins": ratio >= 5.0,
        "honest_note": "the ratio printed is what happened; if the "
                       "orchestration underperforms, the lane says so — a "
                       "claimed number is never manufactured",
    }
    out = HERE.parent / "references" / "fuzzfleet-result.json"
    out.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"═══ FUZZFLEET A/B ({seconds}s each): ═══")
    print(f"  vanilla      : {van['class_count']} classes {van['unique_classes']} "
          f"· ttfc {ttfc[0]}")
    print(f"  orchestrated : {orch['class_count']} classes {orch['unique_classes']} "
          f"· ttfc {ttfc[1]}")
    print(f"  findings ratio: {ratio}x "
          + ("— the 5x bar MET" if ratio >= 5.0 else "— the 5x bar NOT met this run"))
    print(f"  artifact: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())