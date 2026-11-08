# Positioning — why the name is SpyderMonkey (locked decision)

**Decision (2026-11-07): the name stays. No rebrand.** This file exists so the
question never gets re-opened.

## Why SpyderMonkey wins

- **The friendly/dangerous dichotomy is the brand.** It reads as a modern,
  approachable tech name (like the friendly critter it sounds like) while the
  intent is a war dispatcher. That contrast is the voice of the whole family:
  HolyShit!, 3AM Shinjitsu, the ten mandates. Approachable front door, war
  family behind it.
- **Text-unique.** The Y-spelling makes `spydermonkey` unambiguous in shell
  history, paths, configs, and greps — zero collision with Mozilla SpiderMonkey
  tooling in every context the tool actually operates in (trigger word, CLI,
  files).
- **Invocation is trigger-word, not search.** SEO / Google-findability against
  Mozilla's JS engine does not matter for a personal war-room dispatcher.

## Considered and rejected

- **torii** — "ugly" (owner verdict).
- **ronin / orochi / tengu / mikado** — shortlisted (family-consistent single
  words), owner chose to stay with SpyderMonkey instead.
- **Generic short names (smk as the NAME)** — an abbreviation is not a name;
  `smk` stays as an ALIAS only.

## The one condition that flips this

Productizing: if SpyderMonkey ever becomes a public product with marketing,
search presence, or conference demos, the Mozilla SpiderMonkey homophone makes
a rename worthwhile — do it THEN, cleanly, in one pass. Until then: keep.

## Ergonomics (already wired, verified)

- `smk` = zsh alias for `spydermonkey` (`~/.zshrc`) — the family already
  abbreviates campaigns to `smk-` (e.g. `smk-m-dossier.md`).
- `~/.local/bin/spydermonkey` = real CLI wrapper →
  `scripts/spydermonkey.py` (was a docs assumption; now true).
- Typing cost is a session-start one: `/spydermonkey` or `smk` activates the
  mandate-session contract; everything after runs in-mandate.