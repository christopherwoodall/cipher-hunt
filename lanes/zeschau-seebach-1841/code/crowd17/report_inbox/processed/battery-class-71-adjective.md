# Battery verdict: class-71-adjective

**Verdict: KILL** — the uniform epithet-adjective claim for 71 is dead at kill grade. Two independent windows (@925 and @1337) force 71≠adjective under standing values. The §7 split candidacy (nominal@1337 vs non-nominal@925, battery-val-71-quant-nominal PROMOTE) is sharpened, not contradicted: adjective is now excluded as the uniform class and excluded at both anchor windows.

## Bar (verbatim from battery-queue.json)

"test @925 '[65-noun] [71-adj] fois' ('derniere fois'-shaped) and @1337 '[86] [71-adj] qui' (qui attaching to NP)"

**Bar restated as numbered clauses:**
- C1: @925 parses as '[65-noun] [71-adj] fois' ('derniere fois'-shaped).
- C2: @1337 parses as '[86] [71-adj] qui' with 'qui' attaching to an NP.
- C3 (claim-level): 71 is epithet-adjective-compatible at all 7 windows (uniform class claim).

**Adverses:** "class-level 71=adjective (epithet) never tested" — tested now, all 7 windows.

## Method

Read BATTERY-PROTOCOL.md first. Created `locks/class-71-adjective.lock` (agent id + UTC timestamp) on start. Re-derived the repaired stream from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`: **1,847 pairs / 96 types verified**. `canonical.py` never touched. R5005, sealed gate instances, red-team adjudication queue untouched. Offsets below are 1-based on the repaired stream (0-based in parentheses where the queue convention needs it).

Standing values used as premises (table-registry.json / protocol §7): 11='la', 70='pre', 82='m', 34='i', 29='er', 40='e', 46='que' (banked GT); 87='ce', 64='qui', 96='par', 17='fois', 79='tout' (A5), 00='pour' (A9), 84='on' (A15), 47='ce' (A4); 65='noun' (cls, R18-001), 21='noun' (cls), 86='INF' (cls); 12='n' (prom), 48='e' (prom); 59='est', 77='le' (provisional); 67 et/veut sole polyvalence (§7). 1841 diplomatic French throughout.

## Census (byte-exact, re-derived; n(71)=7)

| # | 1-based @ | Row | Context (±3) |
|---|---|---|---|
| W1 | @234 | a2_01 | 96 21 60 [71] 51 70 98 |
| W2 | @326 | a2_05 | 60 15 63 [71] 10 01 19 |
| W3 | @712 | a5_01 | 53 12 48 [71] 12 63 00 |
| W4 | @925 | a5_10 | 40 08 65 [71] 17 61 96 |
| W5 | @1337 | a7_05 | 39 83 86 [71] 64 60 08 |
| W6 | @1565 | a8_01 | 30 06 60 [71] 50 29 24 |
| W7 | @1614 | a8_03 | 08 55 83 [71] 48 31 76 |

Predecessors: 60 x2, 63, 48, 65, 86, 83. Successors: 51, 10, 12, 17, 64, 50, 48 (each x1). Matches battery-val-71-quant-nominal's census exactly.

## C1: @925 '[65-noun] [71-adj] fois' — FAIL at kill grade

Window byte-confirmed: 1-based @925 = 0-based @924, row a5_10. Full ±6: `49 74 74 40 08 65 | 71 17 61 96 48 82 98`. **71 is the first token of row a5_10 (in-row 0); 65 is the last token of row a5_09** (verified: token at stream index 923 = ('65','a5_09'), index 924 = ('71','a5_10')). A transcription-row boundary sits between 65 and 71.

Exhaustive adjective parses, all fail:
- **(i) 71 as postposed epithet of 65** ('[65-noun] [71-adj]'): leaves bare 'fois' stranded. 'Fois' never stands bare in French at any period — it takes determiners/quantifiers/numerals ('une fois', 'chaque fois', 'deux fois', 'la première fois') or fuses ('toutefois'). Ungrammatical. The NP would also straddle the a5_09/a5_10 row break; battery-val-71-quant-nominal refuted the '65 71' unit on three strikes (row boundary, grammar, class contradiction) — adopted as premise, not re-litigated.
- **(ii) 71 as prenominal adjective of 'fois'** ('[71-adj] fois', the 'derniere fois' shape): the shape requires a determiner before the adjective ('la première fois'). 65 is noun-class (R18-001), not a determiner. Bare '[adj] fois' ('*dernière fois' as adverbial) is ungrammatical in 1841 French. Fails.
- **(iii) 71 sub-lexical / fused adverb** ('71 17' as 'toutefois'-shaped): live rival per battery-val-71-quant-nominal, but it is not an adjective reading — excluded by the claim's terms.

**71≠adjective is forced at @925.** Kill grade.

## C2: @1337 '[86] [71-adj] qui' — FAIL at kill grade

Window byte-confirmed: 1-based @1337 = 0-based @1336, row a7_05 mid-row. Full ±6: `94 70 52 39 83 86 | 71 64 60 08 65 64 52`. So '86 71 64' = '[86] [71] qui', with 64='qui' (banked GT) requiring a nominal antecedent.

- 86 = INF class (registry `["INF","cls"]`); the R18-002 amended rule is recorded as PROPOSAL, declaration HELD — no standing nominal-86 at this window.
- '[86-INF] [71-adj]': a bare infinitive taking a postposed epithet adjective without a determiner ('prendre grand') is ungrammatical. Nominalized infinitives require determiners in French ('le prendre', 'un parler lent').
- With no nominal head, 'qui' has no NP to attach to under the adjective reading. Elided-noun rescues are unevidenced.
- The viable reading is the standing one: '[86-INF] [71-noun] qui' = 'prendre [X] qui' (direct object head of 'qui'-relative), battery-val-71-quant-nominal PROMOTE — adopted as premise.

**71≠adjective is forced at @1337.** Kill grade.

## C3: uniform class claim — KILL

Two independent windows force 71≠adjective. The uniform epithet-adjective claim is dead.

## Remaining windows (completeness; not needed for the kill)

- **W1 @234** ('par [21-noun] [60-adj] [71]'): adjective-compatible — stacked epithets ('par [noun] [adj] [adj]') are grammatical; 60=adjective holds locus-level at the four '21 60' windows (battery-adj-60-2160). Sole adjective-compatible window.
- **W2 @326** ('[63] [71] [10]'): indeterminate — 63's class open; adjective possible iff 63 nominal.
- **W3 @712** ('53 12 48 [71] 12'): adjective-incompatible under standing composition — '53 12 48' composes as 'don'+'n'+'e' = 'donne' (12='n' and 48='e' both promoted letters; donn-41-44's '53 12 [X]' composition adopted as premise), a complete finite verb-word; an epithet adjective cannot follow a finite verb, and the val-71-quant-nominal sub-lexical analysis ('e 71 n') independently excludes word-level adjective here.
- **W6 @1565** ('pas [06] [60] [71] [50]'): the claim's reframe '[60] [71-adj]' needs 60 nominal (open); if 60 is adjective, '[60-adj] [71-adj]' is headless — fails. Indeterminate leaning fail.
- **W7 @1614** ('[83] [71] [48]e'): indeterminate — 83's class open (conditioned '83=de' never promoted).

## Standing-state check

No contradiction with battery-val-71-quant-nominal (PROMOTE): that battery established nominal@1337 vs non-nominal@925 as a §7 split candidacy; this battery closes the adjective-uniform route at both anchor windows, sharpening the candidacy (nominal vs quantifier-like/sub-lexical). No red-team verdict on 71 exists. Nothing downgraded. §7 intact — no polyvalence declared; the KILL is on the uniform-class claim, which is a battery-grade decision.

## Adverse answered

'class-level 71=adjective (epithet) never tested' — tested at all 7 windows above; killed at @925 and @1337, incompatible at @712, headless at @1565, indeterminate at @326/@1614, compatible only at @234.

## Follow-ups proposed

1. `quant-71-925-value` (P3) — name 71's quantifier/determiner value at @925 under the forced non-nominal reading (chaque? plusieurs? deux?); the window forces the class, the value is open.
2. `nom-71-1336-value` (P3) — name 71's nominal value at @1336 ('[86-INF] [71-noun] qui', direct-object head of 'qui'-relative).
3. `adj-71-234-locus` (P4) — test adjective-71 as a locus-level-only reading at @234 ('par [21-noun] [60-adj] [71-adj]', stacked epithets), the sole adjective-compatible window.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-class-71-adjective.md` (this file).
- `battery-queue.json`: `class-71-adjective` → status `verdict`, result `kill`, date 2026-10-09 (temp-file + rename; pre-write assert confirmed `queued`/verdictless; JSON re-validated post-write).
- Lock `locks/class-71-adjective.lock` deleted on completion.
- Stream re-derived in-session: 1,847 pairs / 96 types. `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
