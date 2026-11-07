# Aggregation procedure (proven 2026-11-06)

- source canon: `spydermonkey/ledger-dump.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

1. Parse every holyleadger `*.json` defensively (both shapes above); per target
   print: meta (drop `notes` from the chat line, keep it in the file), each
   confirmed class (status `confirmed`) with technique, each chain
   (crown_jewel / steps / impact).
2. Per campaign dir: parse ledger.jsonl rows; count severity / status / cls;
   top rows by cvss desc (id, severity/cvss, title, first ~400 chars of proof);
   chains from `chain-state.json` (or its keys); list `*report*.md` artifacts
   and `kage-rules/` dir count when present.
3. Drop the engine-artifact dirs from the portfolio view; label them
   "bench/training" if included at all.
4. DELIVERABLE: write the FULL dump (every row, proof, chain — ~126KB for the
   whole portfolio) to `~/holyleadger-portfolio-dump.md`; print a condensed
   per-target view in chat. The user reads the chat view; the file is the
   artifact. Aggregate with a Python script over the two stores — never hand-
   transcribe counts.
5. Single-brand follow-up ("how abt X"): produce the brand-filtered dump per
   the sister-brand rule, severity-sorted, with the brand's chains — starting
   from BOTH stores, not from a per-brand file that does not exist.
6. Console output can exceed the 50KB inline cap on a full dump — write the
   file first, then print only the condensed view; page the spill file if the
   full detail is needed mid-run.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
