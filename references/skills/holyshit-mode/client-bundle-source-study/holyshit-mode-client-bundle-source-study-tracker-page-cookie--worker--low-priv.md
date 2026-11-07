# Tracker-page cookie-toss gadget (no dangle needed) — worker / low-priv

- source canon: `holyshit-mode/client-bundle-source-study.md`
- base technique: `holyshit-mode-client-bundle-source-study-tracker-page-cookie.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **worker** · auth **low-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: edge/background runtime — the check runs where the caller has no visible context
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

The target's OWN tracker/attrib pages (`media.*`, `clever.*`, `out.*`) are a cookie-toss
primitive WITHOUT any dangling host: they write URL params as cookies on the MAIN
registrable domain (`Domain=<main>; Path=/; Max-Age=90d; SameSite=None; Secure`, often
≤25 params/visit). Test with a REAL browser (the CF burn pattern blocks scripted fetches
mid-round on these hosts — drive the harness browser instead).

1. Fetch the tracker page source and read its blocklist: reserved names are an EXACT-match
   Set (`session, sid, token, jwt, auth, csrf, xsrf`) — PREFIXED session cookies
   (`stel_token`-family), identity cookies, and `referralCode` fall through. Whatever name
   scheme the site prefixes, the blocklist misses it.
2. Map what the SPA READS from cookies: the React persistent-store pattern
   (`(0,X.N)("name", default)` builders) = cookie-backed stores; identity stores beat
   preference stores. `client-context` = the FingerprintJS Pro visitorId — the SPA SKIPS
   fingerprint generation when the cookie exists, so a tossed value IS the device
   identity (ban evasion + risk-model poison). `stag`-class cookies = affiliate tags read
   at signup (`getAffiliateTag`) = attribution hijack; a fixed-default stag on the tracker
   page = the operator's own ad-pipeline affiliate id.
3. Impact chain: attacker link → tracker page with params → cookies on the main origin →
   identity/attribution/fixation effects. Session-fixation verdict needs the real
   Set-Cookie attributes (HttpOnly guards JS overwrites of an EXISTING cookie; a tossed
   name still pre-plants before first login) — rate honestly, don't assume takeover.
4. Fleet multiplier: inventory media/clever/out hosts on EVERY mirror domain — the gadget
   ships per-brand (`clever.rainbet1.com` carried it when the main domain did).

## Probe adjustment (worker × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
