# Aggregation procedure (proven 2026-11-06) — chain composition

- source canon: `spydermonkey/ledger-dump.md`
- base technique: `spydermonkey-ledger-dump-aggregation-procedure-proven-2026-1.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
