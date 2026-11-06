# State-machine escape (order status skip)

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-06

## The technique

Order transitions (cart → paid → shipped) accepted out of order by direct API calls. Decisive test: call shipped-confirm on a test order still in cart — 200 = the class; the escape is characterized on your own order only.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
