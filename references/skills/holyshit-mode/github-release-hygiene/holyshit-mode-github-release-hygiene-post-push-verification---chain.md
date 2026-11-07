# Post-Push Verification Checklist — chain composition

- source canon: `holyshit-mode/github-release-hygiene.md`
- base technique: `holyshit-mode-github-release-hygiene-post-push-verification-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

1. `git ls-files | sort` — confirm no `.pyc`, `.env`, or unexpected files
2. `curl https://raw.githubusercontent.com/<org>/<repo>/main/README.md | head -5` —
   confirm README renders on the default branch
3. `gh api repos/<org>/<repo>/actions/runs?per_page=1` — confirm latest run conclusion=success
4. Leak scan: `grep -rniE "sk-[a-z0-9]{20,}|gho_[a-z0-9]{20,}|bearer [a-z0-9]{20,}" .`
   (excluding `.env.example` and env-var names)

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
