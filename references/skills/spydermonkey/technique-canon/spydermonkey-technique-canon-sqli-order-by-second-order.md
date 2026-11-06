# SQLi ORDER BY / second-order

- source canon: `spydermonkey/technique-canon.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-06

## The technique

ORDER BY injection (no UNION needed) and second-order (payload stored, executed in another query) are the two shapes scanners miss. Decisive test: ORDER BY (CASE WHEN 1=1 THEN col ELSE col2 END) — row-order delta = injectable; second-order requires your own stored payload re-read in the admin/profile render.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
