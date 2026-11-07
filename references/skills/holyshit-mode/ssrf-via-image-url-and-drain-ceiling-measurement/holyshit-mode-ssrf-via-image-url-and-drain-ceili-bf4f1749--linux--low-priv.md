# Related — linux / low-priv

- source canon: `holyshit-mode/ssrf-via-image-url-and-drain-ceiling-measurement.md`
- base technique: `holyshit-mode-ssrf-via-image-url-and-drain-ceiling-measureme.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **linux** · auth **low-priv** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: read-only inventory first (kaisha rungs), then the documented class match
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- Recon discipline: enumerate BOTH the prod TLD and staging (`staging.<tld>`, `api.staging.<tld>`
  are often a parallel AWS-direct instance) — each serves its OWN keyless `/api/models` catalog that
  can leak hidden models (private/stealth slugs) and internal `*.modal.direct` / gateway base URLs
  the prod catalog omits.
- Contrast the open host (control/invocation surface) vs the keyed host (`/v1/models` → 401
  `Invalid API Key` on the sibling) to identify the ONE misconfigured host — a deployment error,
  not platform-wide intent.
- execute_code sandbox gotcha: import `json`/`re` explicitly at the top (used once via
  `__import__('re')` inline and the direct name was missing → NameError). Keep imports explicit.

## Probe adjustment (linux × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
