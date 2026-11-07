# Infrastructure geo-pin: locate the physical server behind an origin IP — chain composition

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-infrastructure-geo-pin-locate-th.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

When the operator asks "where is it actually hosted", assemble the pin from five read-only sources — never probe neighbors (other IPs on the ISP's block are other customers' lines, out of estate):

1. **Regional registry whois** (KRNIC/JPNIC/RIPE style) — the netblock's `Service Name`/product field classifies the line: a hosting-product name = datacenter; a business-broadband product name (e.g. `broadNnet`) = an office/premises line. The registry's admin/tech contact email + phone is the subpoena/abuse channel for the subscriber identity — record it in the map.
2. **Multi-provider geo classification**: ip-api's `hosting` boolean is the DC-vs-premises tell (`hosting:False` on a business line = not a datacenter); district-level city fields are database-inferred — cite the provider, never present as surveyed fact. ipwho.is and similar often fall back to city-center coordinates; note the disagreement rather than averaging.
3. **PTR (reverse DNS) across resolvers** — no PTR anywhere is itself the signal: hosting lines get PTRs, business/consumer lines often don't. Absence + non-hosting classification = premises line.
4. **Traceroute from the sanctioned VM** — transit-hop hostnames name the path (`<pop>.<isp>.net`); the target ISP's edge hop (entry into their AS) + RTT sanity-checks the geography (great-circle distance / fiber ≈ RTT floor). Install if missing (`sudo -n dnf install -y traceroute` on OL9; `tracepath` is usually preinstalled). Internal ISP hops that don't answer ICMP is normal — the edge hop + RTT is the evidence, not the silent hops.
5. **Consumer-law legal entity**: Korean/Japanese/EU-facing consumer sites are legally required to display the operating entity (사업자등록번호-style registration number + address) in footers/terms — grep every saved page (`privacy/terms/fees/about`) for `registered office|incorporated|사업자|주식회사|registration number`. An offshore shell entity (e.g. Comoros/Anjouan IBC) riding premises-level infrastructure in another country is the physical/legal split that defines the estate's true exposure and the no-subpoena-surface reality.

State the honest ceiling in the map: district-level max for premises lines — the street address lives in the ISP's subscriber records behind local legal process.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
