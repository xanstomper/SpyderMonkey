# Supabase JS client — bundle ships truncated anon key placeholder — chain composition

- source canon: `holyshit-mode/oauth-redirect-uri-impact-gate.md`
- base technique: `holyshit-mode-oauth-redirect-uri-impact-gate-supabase-js-cli.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

When the SPA uses `@supabase/supabase-js` with the pattern `createClient(url, anonKey)`, some builds ship the anon key as a **truncated placeholder** in the bundle:

```js
var Kr=`https://auth.TARGET`, qr=`eyJhbG...YuCQ`
//                                        ^^^ literal "..." — not the real key
```

The real key is injected at runtime from environment / a separate config fetch. Don't waste time trying to extract a full key from the bundle when you see `...` in the middle — verify by checking the byte length (real Supabase anon keys are ~169-220 chars; a truncated placeholder is visibly shorter). If the bundle has a placeholder, the key comes from elsewhere (build-time env, edge function, or a `/api/config` endpoint).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
