# 2026-11-03 3AM-shinjitsu sweep (P3 prepared-exploit + P5 closeout) — chain composition

- source canon: `holyshit-mode/case-packdraw-com.md`
- base technique: `holyshit-mode-case-packdraw-com-2026-11-03-3am-shinjitsu-swe.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
