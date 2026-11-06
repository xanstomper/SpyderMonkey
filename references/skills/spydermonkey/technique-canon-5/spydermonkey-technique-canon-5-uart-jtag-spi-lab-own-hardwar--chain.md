# UART/JTAG/SPI (lab, own hardware) — chain composition

- source canon: `spydermonkey/technique-canon-5.md`
- base technique: `spydermonkey-technique-canon-5-uart-jtag-spi-lab-own-hardwar.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Console discovery (baud-rate sweep on your own board), JTAG chain enumeration, SPI flash dump — firmware-extraction classes with the no-gain read-only framing (MASTG-RES canon). Decisive test: the extracted image hash + strings inventory of YOUR device.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
