# Ad-Hoc Verify Harness Pitfall (hit 3× this session)

- source canon: `holyshit-mode/lessons-2026-10-06-c***REDACTED***-catalog.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-04

## The technique

When a verification-status system demands a fresh `/tmp/hermes-verify-*` script:

1. **Never assert stricter than the repo's own test tolerance.** Asserting EVERY `ios` field parses
   failed because the repo invariant tolerates free-text eras ("pre-iOS4 era", "iPod bootrom (IMG1
   partition handling)"). Scope ad-hoc assertions to exactly the changed behavior (e.g. the 7 new
   entries), not the whole dataset.
2. **Use a FIXED script name** (`/tmp/hermes-verify-<topic>.py`). A `$(date +%s)`-suffixed name
   defeats the subsequent `rm /tmp/hermes-verify-*.py` cleanup glob and leaves junk behind.
3. **Keep it short enough to eyeball** — a variable-name typo (`install` vs `inst`) failed a run.
4. Print `AD-HOC VERIFY: N/N passed` and report explicitly as **ad-hoc, never as suite green**.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
