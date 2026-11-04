# Related

- source canon: `holyshit-mode/ssrf-via-image-url-and-drain-ceiling-measurement.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-04

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
