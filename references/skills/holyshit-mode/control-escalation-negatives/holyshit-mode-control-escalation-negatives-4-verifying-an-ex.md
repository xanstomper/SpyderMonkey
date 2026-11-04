# 4. Verifying an exposed archive before declaring a DB leak

- source canon: `holyshit-mode/control-escalation-negatives.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- generated: 2026-11-04

## The technique

Download a candidate backup with a Range header first (`Range: bytes=0-200`), check the magic
(`PK` = zip), then pull full bytes and list `zipfile.namelist()` + `getinfo().file_size`. A `.zip`
whose members are all `.jpg`/media is a photo archive, not a credentials dump. Don't report "DB
backup exposed" from the filename alone.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
