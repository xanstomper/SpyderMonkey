# Stack fingerprint trick — worker / guest

- source canon: `holyshit-mode/cf-wp-origin-bypass-recipe.md`
- base technique: `holyshit-mode-cf-wp-origin-bypass-recipe-stack-fingerprint-t.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **worker** · auth **guest** · chain role **entry**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: edge/background runtime — the check runs where the caller has no visible context
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

Repeated `Server:` flips (LiteSpeed ↔ openresty/1.31.1.1) across connections = **multi-instance
load-balanced backend**, not a misread. Note both versions; CVE-match against the larger
surface (WordPress 6.7.3 / WooCommerce 9.5.1 / Elementor 3.26.4+Pro / HT Mega 2.7.8 / The Plus
6.2.2 / Qi Addons 1.8.9 / Funnel Builder 3.8.0 / Blocksy 2.0.84 / wp-statistics).

## Probe adjustment (worker × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
