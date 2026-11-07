# Client estate: the download portal's bundle is the client-infra map — wireless / root

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-client-estate-the-download-porta.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **wireless** · auth **root** · chain role **pivot**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: LAB-ONLY — your own radios and stations; third-party airwaves are the absolute wall
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

When a target ships native clients (and the bounty scope covers them), the public download landing
page (`/download/`, or a `download.<brand>-service.com` portal) is an Angular/Vue app whose
`main-*.js` is a one-request infrastructure map: installer endpoints per platform
(`/desktop/installer/windows|osx`, `/mobile/installer/android`, `/mobile/installer/enterprise/ios-plist`
— the ios-plist path names enterprise MDM distribution), the CDN/service domains behind them,
DEV-named asset hosts (`static.<brand>techdev.com`-style) that prod pages import from (supply-chain
class), and SSO domains (`ggpass.com`-style) that name the network's single-sign-on surface. Mine it
before any binary work.

- **The download host is DYNAMIC + REGIONAL** — `mobileDownloadService.getDownloadHost()` resolves the
  CDN per request, so `dlportal-1.<cdn>.com` can be TCP-dead from one vantage while
  `download.<svc>.com` 301s to a `dlportal.` host that 404s the same path. Never conclude "client
  unobtainable" from one host: try the alternates from the map and vary the UA.
- **The client lane's crown material is often the OPERATOR'S OWN BREACH HISTORY — zero probes
  needed.** Search the target's security-post blog + researcher writeups + community threads for:
  protocol-cleartext proofs (names the exact packets/hosts), client-mod/cheating incidents with
  confiscated amounts, and community reports that a fix was ineffective. That dossier is
  WhiteArmor-class breach forensics (admitted design weaknesses + proven exploitation paths) and it
  names the client-trust surfaces the bounty actually pays for. Register as operator-context with the
  sources in the proof.

## Probe adjustment (wireless × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
