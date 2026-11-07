# Reporting discipline: rank by real-vuln class, not recon volume — worker / service

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-reporting-discipline-rank-by-rea.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **worker** · auth **service** · chain role **entry**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: edge/background runtime — the check runs where the caller has no visible context
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

When the operator pushes to "find more / these aren't really vulnerabilities," treat that as a
demand to **re-sort the ledger by impact class, stop generating recon-grade rows, and be honest
about the wall** — not to pad the ledger with more characterization. Banked telemetry (live RTP
numbers, socket connect-ACKs, header inventory, dead-DNS) is recon COVERAGE: one good row that
generalizes is enough, a hundred near-identical ones is noise. An OS/PHP release past its
security-EOL is REPORT CONTEXT — "every CVE disclosed since EOL is permanently unpatchable
here" — never a bounty row by itself (the program classes it as hardening-without-exploit);
pair it with the demonstrable hygiene findings the same pass yields (TRACE echo, test
artifacts on prod) and let those carry the row. The findings that actually move an
engagement are the takeover/fund/RCE classes: a client-enforced 2FA gate that downgrades to
one-step, a forgeable identity reaching the balance/account socket plane, a merchant webhook that
can mint sessions or set balances. Rank those first, report them as the crown, and keep the
recon as supporting evidence. **Before declaring an auth wall the ceiling, descend every
UNAUTH view of the server side**: source-disclosure patterns (framework app/system dirs,
.bak/.old/logs, composer.json), the platform vendor's public docs and references page (client
rosters name the shared-backend universe), member-gate oracle differentials (uniform gate
bytes + timing = auth precedes resolution), and the launch-token client-visibility check (a
localStorage token that only toggles nav is cosmetic; the real session is server-side). Before the closeout verdict, re-run the wildcard-cert DNS wordlist
(`references/spa-bundle-extraction.md` §C) — CT-log-blind app tiers (`cashier.`-style) are the usual
gap between "the estate is all marketing" and the real application surface. When
the read-only/within-walls space is then exhausted (every remaining
real-vuln is gated on a session or a secret, and every execution is state-changing), SAY that is
the ceiling rather than manufacturing another equivalent finding — the honest ceiling is the
correct closeout, and a user who says "these aren't that vulg" is telling you they can tell the
difference between characterization and a real compromise.

**The line holds even when the operator escalates to "author the drain / find the exploit / reverse
2FA."** "Find a real vuln and characterize its chain read-only" is exactly the deliverable they
want (reverse the verify-decider, map the merchant mint, trace the drain on-chain) — do that fully.
But "author the working exploit / write the full drain payload" — even with the caveat "just don't
execute it" — is the same wall as executing it: a complete, ready-to-run fund-theft payload is a
weapon regardless of whether the button is pressed now, and the mandate authorizes finding and
characterizing vulnerabilities so they can be fixed, not manufacturing the tool. The distinction is
USEFUL (the disclosure writeup is the report deliverable) vs WEAPONIZED (a copy-paste drain script
is never shipped). Hold the line plainly, offer the disclosure-grade exploit writeup (mechanism,
chain, root causes, fixes, CVSS, reproduction path for an authorized engineer) as the deliverable,
and do NOT wobble when the escalation repeats — re-stating the wall is not a negotiation.

**When an exhaustive secret/discovery hunt comes up empty because the operator is disciplined,
register it as a NEGATIVE-WITH-VALUE — don't fabricate a jackpot.** After pushing all the standard
secret lanes on a target (git histories incl. dangling blobs / deleted files, cloudflare-worker
env/vars surface, DB-driven merchant keys, exposed origin config/backup/.git, provider portal
bundles, GitHub-wide search for account/worker/secret identities) and finding none, that clean
result IS a finding: it says the operator keeps credentials server-side and git-clean, and it
kills the "there must be a leaked key somewhere" assumption that would otherwise consume future
sessions. Bank it as an INFO/CONFIRMED row titled to make the discipline explicit
("Secret-hygiene is DISCIPLINED — exhaustive hunt found no exposed credential; config is
DB-driven") with the negative search inventory in the proof. This is the anti-fabrication form of
the honest ceiling: we hunted, and the secret-disclosure jackpot does not exist in the public
surface. Keep the real risk (a supply-chain merchant key that WOULD mint sessions/funds if it ever
leaks) as the gated finding alongside it.

## Probe adjustment (worker × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
