# Client estate: the download portal's bundle is the client-infra map

- source canon: `spydermonkey/engagement-ops.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-06

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
