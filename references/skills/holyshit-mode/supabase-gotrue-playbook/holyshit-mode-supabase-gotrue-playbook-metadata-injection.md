# Metadata injection

- source canon: `holyshit-mode/supabase-gotrue-playbook.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

`user_metadata.role=admin`, `credits:999999` persists into the JWT (GoTrue does not strip user_metadata). But backends authorize on their own DB (profiles table / app_metadata), so admin claims almost never escalate. Record persistence as confirmed; expect authorization to fail.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
