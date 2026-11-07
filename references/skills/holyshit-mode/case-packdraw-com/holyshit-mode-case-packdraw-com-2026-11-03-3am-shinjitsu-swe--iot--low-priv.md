# 2026-11-03 3AM-shinjitsu sweep (P3 prepared-exploit + P5 closeout) — iot / low-priv

- source canon: `holyshit-mode/case-packdraw-com.md`
- base technique: `holyshit-mode-case-packdraw-com-2026-11-03-3am-shinjitsu-swe.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **iot** · auth **low-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: radio/serial surface — BLE/NFC/UART classes, lab hardware only
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- **CVE-2025-29927 (Next middleware bypass): BLOCKED** — identical statuses with/without
  `x-middleware-subrequest` on /en-us/account + 7 route guesses; Vercel platform fix.
- **_next/image optimizer SSRF: BLOCKED** — 400 on any non-allow-listed host (allow-list =
  imagekit etc.; Vercel metadata-IP block upstream).
- **postMessage surface: none** in loaded client chunks.
- **Breach-context brief (cartel class):** no hack/leak of PackDraw; but no gambling
  license; federal litigation (MN 25-cv-4128, Sept-2026 order) alleges PackDraw built
  with misappropriated Partnership code (The House/WowDAO/Packs.com/Packs Protocol
  brands) delivered into Roobet orbit; PDCC Services Ltd entity; minor-recruitment
  suits MN+NY; $500K-impersonation laundering suit defendant; ~$259M deposits by
  Apr-2025; Trustpilot 3.9/5 with unauthorized-charge + odds-tightening complaints.
- **§8 coverage verdict:** all 10 classes probed or N/A for the unauth plane; every
  finding ledgered; remaining account-plane tests = operator ask (seed-rotation 2-open
  test, cross-user pusher with session, create-pack EV, battle hash verify).

## Probe adjustment (iot × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
