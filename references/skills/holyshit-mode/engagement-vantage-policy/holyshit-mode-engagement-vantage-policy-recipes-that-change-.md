# Recipes that change on the VM

- source canon: `holyshit-mode/engagement-vantage-policy.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Probes: `ssh vermes '<curl/python/etc>'` — per-command ~0.33s over the ssh mux.
- Long bursts/captures: nohup on the VM, poll the log. **ssh drop does NOT reliably kill remote foreground children** — a piped foreground run survived a terminal timeout and kept probing, so the next launch ran CONCURRENTLY and doubled request volume into one log. Before re-running a VM job, verify no stale remote process exists (`ps` by script name or a pidfile), and poll completion by the job's OWN DONE marker in its log — never `pgrep`/`pkill -f <script>`: the ssh wrapper's cmdline contains the pattern and
  self-matches (pgrep = false RUNNING; `pkill -f` = kills your own ssh session, exit 255) —
  use the process's bare name (`pkill -9 chromium`) or a bracketed regex.
- Inline Python over ssh heredocs: f-string expressions cannot contain backslash escapes (SyntaxError on the literal, hit 3x in one session). Bind the escaped regex/sub result to a variable before the f-string, or write the script to a file and scp it once it passes a few lines.
- `jq` on a jsonl verdict file needs `-s` (slurp) — without it every line errors `Cannot index string with "phase"` because jq parses each JSON value as its own document.
- The `holyleadger` mode-700 PermissionError rule now READS: run it on the VM as opc over ssh,
  or as the shell user at home — never from the execute_code sandbox.
- Dispatcher endpoints (HOLYSHIT_ENDPOINT) are home-local (FreeForge :8705) — LLM dispatch can
  stay on home or use VM-reachable providers; TARGET traffic is what must never touch home.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
