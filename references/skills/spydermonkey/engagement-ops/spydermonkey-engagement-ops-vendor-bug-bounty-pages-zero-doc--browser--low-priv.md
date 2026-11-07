# Vendor bug-bounty pages = zero-document authorization — browser / low-priv

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-vendor-bug-bounty-pages-zero-doc.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **browser** · auth **low-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the CLIENT is the boundary — same-origin, extension, and postMessage trust are the probe shape
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

A self-published `/bugbounty` page is an authorization document that needs no paperwork —
parse it into the engagement before any probe: §3 in-scope list → `scope add` entries (domains
AND the feature list: auth/session/KYC/wallet/bonus/APIs/game-launch/business-logic), §4
out-of-scope → the exclusion gates (enumeration-without-impact, headers-only hardening,
scanner-spam-without-proof, DoS/volumetric), §5 report channel + subject format, §7
safe-harbor walls. Bank the parsed program in the holyleadger `program` field — its severity
tier table defines what the vendor pays for and pre-ranks the report. Program walls stack on
top of the family's own: validation-only + no other-user data + no disruption stay absolute,
and program-excluded classes (bare DMARC/headers, cosmetics) register as informative at most.

**Feeding the bounty page into 3AM (shinjitsu) needs the FULL manifest schema, and `--target` must be
a scope entry.** `validate --authorization <file>` refuses partial manifests — it requires
`authorization_id, authorized, operator, engagement, approved_by, roe_reference, expires_at, targets,
allowed_methods`; point `approved_by`/`roe_reference` at the program's own page and contact address.
The `--target` value must match an entry in the manifest's `targets[]` — pass the DOMAIN
(`ggpoker.com`), never the campaign nickname (`ggpoker`), or the gate refuses with "not in the
authorization scope". Without DNS control add `dns_control:false` — validation still passes but the
method downgrades to passive/active-read-only, and the sweep runs as `plan --target <domain>
--state <campaign>/3am-state.json` + honest `set-status` verdicts (EXHAUSTED/BLOCKED per domain)
instead of a live sweep. That is the wall holding, not a failure. (shinjitsu has NO sweep command —
validate → challenge → verify-dns → plan → set-status → report IS the interface.)

## Probe adjustment (browser × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
