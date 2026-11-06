# NoSQL operator injection ($ne, $regex)

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-INPV** · **CWE-74** · **ATT&CK T1190**
- generated: 2026-11-06

## The technique

JSON body operators accepted server-side ({"pass":{"$ne":""}}). Decisive test: {"$ne":null} on the login body of YOUR test account — a 200 without the password = the class.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
