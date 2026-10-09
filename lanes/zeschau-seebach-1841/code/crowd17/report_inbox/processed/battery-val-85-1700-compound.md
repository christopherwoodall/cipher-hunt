# Battery verdict: val-85-1700-compound

- Target: `val-85-1700-compound` (battery-queue.json, priority 3, status queued)
- Claim: "narrow alternative: name 85 value from the @1699-1702 "85 33 94 30" compound locus itself (byte-verified "91 85 33 94 30" at row a8_06; cf. stem-85 W-at-1699); if 85 compounds with "33 94 30" as dire/croire, the value is licensed directly at the locus"
- Worker: d849d966-ae63-48c7-8e42-e0056396ae14. Date: 2026-10-09.
- Note: clean re-dispatch after a daemon-restart killed the first worker; no prior report or queue changes existed.
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs, 96 types). `canonical.py` NOT used. R5005, sealed gates, red-team queue untouched.
- All @-offsets are pair indices in the repaired stream.
- Lock: `code/crowd17/next-token/locks/val-85-1700-compound.lock` created on start (no stale lock present); deleted on completion.

## Bar (verbatim, pre-registered)

"name iff the compound geometry forces one value"

**Restated as numbered pass/fail clauses (frozen before testing):**
1. **C1 (force):** the @1699–1702 geometry admits exactly one 85 value — every rival value is kill-grade excluded at the locus.
2. **C2 (name):** that value is stated with byte evidence and zero new assumptions.
3. **C3 (adverses):** none listed.

Standing values used (per protocol §7): pencil GT (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); promoted/granted (87=ce, 64=qui, 96=par, 17=fois, 79="tout", 00="pour", 84="on", 47="ce"); provisional (59=est, 77="le"); frames granted (A3 85 verb-stem class, value open; 94="ne" STRONG LEAD per R17-001/R20-007; 30="pas" conditional per pasX-leftverb-59). Red-team: R20-029(b) "n'importe" fused lexical item; R20-125 62='il' REJECTED (62's cell absent); R16-005 78='ver' LEAD; 33 dire/croire tie open; 20 locus-level relative adverb (reladv-20-1703 PROMOTE, battery grade).

## Method

1. Read BATTERY-PROTOCOL.md in full before testing.
2. Re-derived the locus byte-exact in-session; read the governing prior batteries: `contredire-85-33-vehicle` (PROMOTE, evidence-gathering), `croire-33-compound85`, `stem-85-then-1700` (NULL, gate closed), `ne-30-1700` (NULL), `reladv-20-1703` (PROMOTE), `pasX-leftverb-59` (PROMOTE), `val-85-narrow` (NULL).
3. Enumerated the compound candidates the geometry admits and tested each against the force standard.

## Locus (byte-exact, row a8_06)

| @ | pair | row |
|---|---|---|
| 1698 | 91 | a8_06 |
| 1699 | 85 | a8_06 |
| 1700 | 33 | a8_06 |
| 1701 | 94 | a8_06 |
| 1702 | 30 | a8_06 |
| 1703 | 20 | a8_06 |
| 1704 | 62 | a8_06 |
| 1705 | 94 | a8_06 |
| 1706 | 88 | a8_06 |

i.e. `…[91] [85] [33] [94] [30] [20] [62] [94] [88]…`.

**Tail reading (adopted, not re-litigated):** @1701–1702 = fused "n'importe" (reladv-20-1703 PROMOTE, battery grade; R20-029(b) confirms fused lexical status; unique stream-wide '94 30' adjacency). 30='pas' is kill-grade excluded at THIS window by word order (ne-30-1700 NULL: "30='pas' is ungrammatical at this window"). The geometry under test is therefore `[91] [85] [33] n'importe [20-reladv] [62] ne [88-fin]`.

## Candidate enumeration

| candidate 85 value | compound reading | force test |
|---|---|---|
| 'contre' (+ 33='dire') = "contredire" | "…[91] contredire, n'importe où [62] ne [88]…" | Admitted (contredire-85-33-vehicle: French-plausible, scheme-plausible). NOT forced: needs 85="contre" (open) AND 33="dire" (open tie) = 2 new assumptions; the rival 'laisser' and bare-infinitive parses are not kill-grade excluded below. |
| 'laisser' (LEAD) | "…[91] laisser [33] n'importe où…" | NOT forced: 33 as laisser's object/complement has no standing license (33 class open); the parse stalls, but "stalls" ≠ "kill-grade excluded". |
| 85 = bare stem, 33 adverbial/other | various | NOT forced: 33's class is open; nothing excludes a non-compound segmentation at kill grade. |
| 'croire'-family compound | "contrecroire" | Dead at word-formation level ("contrecroire" is not French) — but this only removes a rival of 'contredire', it does not force 'contredire' over 'laisser'. |

Additional facts: "85 33" is a stream hapax (@1699; 33→85 x0) — no recurrence to discriminate; 33→29 x5 and 33→46 x2 keep the dire/croire tie open and unrelated to this locus; the 6 A3 frame legs are value-open (val-85-narrow NULL); 91's class at @1698 is open (R19-164's 91=past-participle grant is locus-scoped to @538/@1371).

## Per-clause results

1. **C1 (force): FAIL.** The geometry admits "contredire" (French-plausible, per the vehicle battery) but does not force it: naming the compound requires two new assumptions (85="contre", 33="dire"), and neither 'laisser' nor the bare-stem reading is kill-grade excluded at the locus. The force standard is not met.
2. **C2 (name): not reached** — naming without forcing would be invention (§3).
3. **C3: PASS** — no adverses listed.

## Verdict: NULL (fence executed)

The compound geometry admits "contredire" but forces no value. The naming bar's condition is not met; the locus stays open with "contredire" as the admitted (not forced) compound. This is consistent with `contredire-85-33-vehicle` (evidence-gathering PROMOTE, no value named) and `stem-85-then-1700` (gate closed: 85's value still unnamed at battery grade).

No standing/red-team verdict contradicted or downgraded; §7 intact. Canonical-stream caveat stands (row a8_06 offset unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `compound-85-33-scheme` (P4) — gather cipher-scheme precedent: do clear prefix-compounds elsewhere in the cipher ("re-", "contre-", "pour-") segment the same way? Evidence-gathering for the compound vehicle; red-team venue for any declaration.
2. `ne30-1701-tail-reconcile` (P3) — reconcile the fused "n'importe" reading at @1701–1702 with the conditional 30="pas" (pasX-leftverb-59): does the fused item hold wherever 30="pas" parses elsewhere? The tail reading gates every compound parse at the locus.
3. `laisser-85-1699` (P3) — test 'laisser' specifically at @1699 ("[91] laisser [33] n'importe où…"): can 33 compose as laisser's object/complement under standing values? Kill iff no composition parses with zero new assumptions.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-85-1700-compound.md` (this file).
- Queue: `val-85-1700-compound` queued → verdict/null (temp-file + rename, own entry only; pre-write assert confirmed queued/verdictless; JSON re-validated post-write; no downgrade).
- Lock `locks/val-85-1700-compound.lock`: created on start, deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched.
