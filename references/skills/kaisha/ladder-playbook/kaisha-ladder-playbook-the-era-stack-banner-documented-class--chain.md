# The era-stack (banner → documented classes) — chain composition

- source canon: `kaisha/ladder-playbook.md`
- base technique: `kaisha-ladder-playbook-the-era-stack-banner-documented-class.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

KAISHA never authors exploits. A banner maps to the era's documented technique
classes (3AM canon) — the ladder then plans those classes' validation tests:

| Banner pattern | Era | Documented classes | Canon |
|---|---|---|---|
| `nginx/1.(0-19).` | nginx legacy | header/parser-differential (9) · cache/edge-separation (7) | arsenal-01/02 |
| `apache/2.2|2.4` | apache legacy | validation-order (1) · parser-differential (9) | arsenal-01 |
| `openssh_(0-8).` | openssh old-major | entropy/forge (10) · identifier-trust (6) | arsenal-01 |
| `iis/7|8` | iis legacy | parser-differential (9) · type-coercion (3) | arsenal-06 |
| `tomcat/8|9 · jetty/9` | java app-server legacy | type-coercion (3) · state-machine-gaps (5) | arsenal-06 |
| windows / microsoft | windows estate | session/cookie-confusion (8) · operational-planes (20) | arsenal-06 · session-lessons |
| linux / ubuntu / debian | linux estate | state-machine-gaps (5) · database-exposure (15) | arsenal-06 |

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
