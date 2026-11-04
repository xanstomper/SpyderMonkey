# Ad-Hoc Verify Harness Pitfall (hit 3× this session) — chain composition

- source canon: `holyshit-mode/lessons-2026-10-06-c***REDACTED***-catalog.md`
- base technique: `holyshit-mode-lessons-2026-10-06-c***REDACTED***-catalog-ad-hoc-ve.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

When a verification-status system demands a fresh `/tmp/hermes-verify-*` script:

1. **Never assert stricter than the repo's own test tolerance.** Asserting EVERY `ios` field parses
   failed because the repo invariant tolerates free-text eras ("pre-iOS4 era", "iPod bootrom (IMG1
   partition handling)"). Scope ad-hoc assertions to exactly the changed behavior (e.g. the 7 new
   entries), not the whole dataset.
2. **Use a FIXED script name** (`/tmp/hermes-verify-<topic>.py`). A `$(date +%s)`-suffixed name
   defeats the subsequent `rm /tmp/hermes-verify-*.py` cleanup glob and leaves junk behind.
3. **Keep it short enough to eyeball** — a variable-name typo (`install` vs `inst`) failed a run.
4. Print `AD-HOC VERIFY: N/N passed` and report explicitly as **ad-hoc, never as suite green**.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
