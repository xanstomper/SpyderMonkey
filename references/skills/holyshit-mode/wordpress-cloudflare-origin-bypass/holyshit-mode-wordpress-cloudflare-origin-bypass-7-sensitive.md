# 7. Sensitive-file soft-404 discriminator (don't false-positive)

- source canon: `holyshit-mode/wordpress-cloudflare-origin-bypass.md`
- bindings: **WSTG-INPV-05** · **CWE-89** · **ATT&CK T1190**
- generated: 2026-11-04

## The technique

On this origin, every missing path under `.env.bak`, `/.htpasswd`, `/backup.zip`, `/dump.sql`,
`/.git/config`, `/wp-config.php` returned **`200 text/html`** with the same generic
"DOCTYPE html / charset=utf8 / viewport" page. That identical template is a **custom soft-404**,
NOT file content. Discriminate by body: real secrets would differ / be smaller; an identical
shell = file does not exist. A plain `st==200` is a false-positive trap.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
