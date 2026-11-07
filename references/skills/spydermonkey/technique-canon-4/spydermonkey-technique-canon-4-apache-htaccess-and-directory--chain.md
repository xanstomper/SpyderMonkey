# Apache .htaccess and directory-move classes — chain composition

- source canon: `spydermonkey/technique-canon-4.md`
- base technique: `spydermonkey-technique-canon-4-apache-htaccess-and-directory.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

.htaccess exposure itself (fetch it), Options +Indexes (already DIRECTORY canon), and mod_userdir legacy. Decisive test: direct fetch of .htaccess — the file content IS the harvest.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
