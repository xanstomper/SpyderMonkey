# Supabase JS client — bundle ships truncated anon key placeholder — grpc / guest

- source canon: `holyshit-mode/oauth-redirect-uri-impact-gate.md`
- base technique: `holyshit-mode-oauth-redirect-uri-impact-gate-supabase-js-cli.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **grpc** · auth **guest** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: reflection/list methods first; protobuf definitions are the schema oracle
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

When the SPA uses `@supabase/supabase-js` with the pattern `createClient(url, anonKey)`, some builds ship the anon key as a **truncated placeholder** in the bundle:

```js
var Kr=`https://auth.TARGET`, qr=`eyJhbG...YuCQ`
//                                        ^^^ literal "..." — not the real key
```

The real key is injected at runtime from environment / a separate config fetch. Don't waste time trying to extract a full key from the bundle when you see `...` in the middle — verify by checking the byte length (real Supabase anon keys are ~169-220 chars; a truncated placeholder is visibly shorter). If the bundle has a placeholder, the key comes from elsewhere (build-time env, edge function, or a `/api/config` endpoint).

## Probe adjustment (grpc × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
