# Coupon stacking and chain arithmetic

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-BUSL-05** · **CWE-285** · **ATT&CK T1068**
- generated: 2026-11-06

## The technique

Multiple discount codes applied per cart (or a code re-applied per item) is arithmetic the server should refuse. Decisive test: apply code A then B — final total below the item floor = the class; capture the order-preview JSON before/after as baseline/attack/diff.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
