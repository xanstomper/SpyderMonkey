#!/usr/bin/env python3
"""THE MASS LANE (v7.8) — the family's answer to the fuzzing sieves.

Mayhem/OSS-Fuzz beat the family on bug-finding THROUGHPUT — a sieve with no
walls. This lane gives the family its own mass engine: a stdlib mutation
fuzzer seeded from THE FAMILY'S OWN grammar (the testers' payload vocabularies
+ boundary values + the dojo replicas as the strike surface), measuring
inputs/sec and unique findings on 127.0.0.1 — lab-bound, walls intact,
validation-only (findings = differential hits, never corpora).

What beats the sieves at their own game: the seeds are knowledge — every
mutation descends from a documented PoC class, so a hit is immediately a
CLASSIFIED finding (the sieves need triage; the family's hits arrive named).
"""
from __future__ import annotations

import json
import random
import string
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import bench_apb as hb  # the port/free + sudo helpers

# the seeds: the family's own tester payloads (documented classes) + boundaries
SEEDS = [
    "../../etc/passwd", "....//etc/passwd", "..%2f..%2fetc%2fpasswd",
    "/etc/passwd", "{{7*7}}", "${7*7}", "1' OR '1'='1", "spy<svg/onload=x>",
    '"><svg/onload=x>', "../../", "%2e%2e%2f", "..\\..\\", "\x00", "\xff\xfe",
    "A" * 256, "9" * 64, "-1", "0x7f", "%s%s%s%n", "%25uff0e%25uff0e",
    "';system('id');//", "${system('id')}", "../../../../root/flag.txt",
]
BOUNDARIES = ["-1", "0", "1", "2147483647", "2147483648", "-2147483648",
              "9999999999999999999", "NaN", "null", "true", "{}", "[]"]


def mutate(seed: str, rng: random.Random) -> str:
    ops = rng.randint(1, 3)
    out = seed
    for _ in range(ops):
        op = rng.choice(("flip", "insert", "delete", "dup", "boundary", "rand"))
        if not out:
            out = rng.choice(SEEDS)
        if op == "flip" and out:
            i = rng.randrange(len(out))
            c = out[i]
            out = out[:i] + rng.choice(" ABC/\\.%'\";<>=&$`|}{#\x00\t") + out[i + 1:]
        elif op == "insert":
            i = rng.randrange(len(out) + 1)
            out = out[:i] + rng.choice(string.printable) + out[i:]
        elif op == "delete" and len(out) > 1:
            i = rng.randrange(len(out))
            out = out[:i] + out[i + 1:]
        elif op == "dup":
            i = rng.randrange(len(out))
            out = out[:i] + out[i] * 2 + out[i:]
        elif op == "boundary":
            i = rng.randrange(len(out) + 1)
            out = out[:i] + rng.choice(BOUNDARIES) + out[i:]
        else:
            i = rng.randrange(len(out) + 1)
            out = out[:i] + "".join(rng.choices(string.printable, k=4)) + out[i:]
    return out


def main() -> int:
    seconds = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 60
    # the strike target: a dojo replica (the vulnerability surface is REAL)
    dj = HERE.parent.parent / "dojo/scripts/dojo.py"
    if not dj.exists():
        dj = Path.home() / "dojo/scripts/dojo.py"
    port = hb._free_port()
    srv = subprocess.Popen([sys.executable, "-c",
                            f"import sys; sys.path.insert(0, '{dj.parent}');"
                            f"import dojo; srv = dojo._serve('TRAVERSAL', {port});"
                            "import time; time.sleep(999)"],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1.5)
    base = f"http://127.0.0.1:{port}"
    probe_path = "/file?path="
    rng = random.Random(20261108)
    findings = {}          # signature → count (unique findings)
    inputs = 0
    errors = 0
    t0 = time.time()
    baseline = hb._http(base + probe_path + "page1.php")
    baseline_sha = len(baseline)
    try:
        while time.time() - t0 < seconds:
            payload = mutate(rng.choice(SEEDS), rng)
            body = hb._http(hb._qenc(base + probe_path + payload), timeout=4)
            inputs += 1
            if body.startswith("__ERR__"):
                errors += 1
                findings.setdefault("transport-error", 0)
                findings["transport-error"] += 1
                continue
            # the classified hits: the family's signatures, not raw crashes
            for sig, cls in (("root:", "TRAVERSAL/passwd-read"),
                             ("flag", "TRAVERSAL/flag-reach"),
                             ("Directory", "DIRECTORY/index"),
                             ("SMRCE:", "RCE/exec")):
                if sig in body:
                    findings.setdefault(cls, 0)
                    findings[cls] += 1
            if len(body) != baseline_sha and "Page not found" not in body \
                    and "root:" not in body and "flag" not in body:
                cls = "DIFF/unexpected-body"
                findings.setdefault(cls, 0)
                findings[cls] += 1
    finally:
        srv.terminate()
    elapsed = time.time() - t0
    payload = {
        "lane": "MASS — stdlib mutation fuzzer, family-native seeds",
        "strike_surface": "dojo TRAVERSAL replica (127.0.0.1, lab-bound)",
        "inputs_fired": inputs,
        "transport_errors": errors,
        "elapsed_s": round(elapsed, 1),
        "throughput_ips": round(inputs / max(0.001, elapsed), 1),
        "unique_findings": {k: v for k, v in sorted(findings.items(),
                                                     key=lambda kv: -kv[1])},
        "classified_note": "every hit arrives NAMED (documented class) — the "
                           "sieves' triage step is already done",
        "honest_ceiling": "lab throughput only — Mayhem's real-world mass needs "
                          "real targets; the capability + number on the range "
                          "is the claim, not parity with their fleet",
    }
    out = HERE.parent / "references" / "masslane-result.json"
    out.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"═══ MASS LANE: {inputs} inputs in {elapsed:.0f}s "
          f"({payload['throughput_ips']:.0f}/s) · unique findings: "
          f"{len(findings)} ═══")
    for k, v in payload["unique_findings"].items():
        print(f"   {k}: {v}")
    print(f"  artifact: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())