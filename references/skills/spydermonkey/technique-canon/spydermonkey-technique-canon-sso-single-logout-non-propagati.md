# SSO single-logout non-propagation

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-06

## The technique

Logout at the SP that leaves the IdP session (or a sibling SP) alive turns "logout" into a UI state. Decisive test: log out at SP-A, replay SP-B's deep link — an authenticated render is the finding. Crown: session lifetime after logout.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
