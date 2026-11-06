# Cookie __Host- prefix and scoping regressions

- source canon: `spydermonkey/technique-canon.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-06

## The technique

Missing `__Host-`, missing Secure, or Domain=.parent leaves cookies portable across sibling hosts. Decisive test: set a cookie on sub.in-scope.host and read it from sibling.in-scope.host over HTTPS — cross-subdomain readability is the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
