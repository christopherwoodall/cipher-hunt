# Round-16 battery: la (11) — frames, fork votes, anomalies

Finder report: `code/crowd16/report_inbox/next-token-findings-la.md` (ingested 2026-10-07).
Status entering: 11="la" BANKED (pencil GT). This battery adjudicates 11's
frames and the finder's fork votes — not the value.

---

## PRE-REGISTRATION (locked before formal tests)

**De-dup check (load-bearing):** n11=45; 87-11 ×7; 47-11 ×3; standalone 35.
All frame claims use the standalone 35.

**Bar L1 (P1 06="ent/ment" LEAD):** LEAD-grade iff the 3 "[X]-06 la [NOUN]"
windows re-derive exact AND 06's profile is ending-compatible (06→77 ×6,
06→11 ×4). The verb-vs-adverb fork stays open → LEAD, not promotion.

**Bar L2 (P2 "la 52-37-43" → 37-adjective):** the trigram re-derives
byte-identical ×2; no finite-verb parse available in the slot. Two tokens of
ONE phrase type → LEAD for 37-postnominal-adjective (short of a frame grant;
does NOT restore the demoted est-frame — different frame).

**Bar L3 (P3 78 fork votes):** windows re-derived; votes recorded as
fork-conditional data for the forks battery (@296 → 78="er"; @1669 →
78="ver"). The positional-allophony hypothesis is queued, not ruled here.

**Bar L4 (P4 "l'en-X" ×3):** conditioned on the 24="en" LEAD; 3 windows
re-derived exact. LEAD (elision reading); the 48 tension flagged.

**Bar L5 (P5 26-noun ×2):** 2 windows re-derived; the 26=verb tension
recorded. LEAD for 26-noun (2 legs).

**Bar L7 (P7/@108 vs pour-beat @106 — CONTRADICTION):** the physical window
is ONE (67@110; P[106:114] = [0,46,11,21,67,93,29,89]). The pour reading
rests on BANKED 00="pour" (→ 67="et"); the la reading (67="veut") requires
unbanking 00 at @106. Bar: the banked value wins ties — the "veut" vote at
@110 is REJECTED as a fork datum unless new evidence against 00 at @106;
recorded as a conditional (IF 67="veut" independently established at @110,
THEN 00≠"pour" at @106).

**Bar L8 (anomalies):** A1/A2/A3 verified and queued/fenced, not forced.

---

## TESTS

`t = code/crowd16/next-token/test_la.py`. (key assertions; full script on disk)

| # | assertion | got |
|---|-----------|-----|
| 1 | n11=45; 87-11 ×7; 47-11 ×3; standalone 35 | |
| 2 | P1 windows: @320 [94,6,11,92]; @1123 [14,6,11,52,37,43]; @1721 [68,6,11,52,37,43] | |
| 3 | 11-52-37-43 ×2 @1123/@1721 byte-identical | |
| 4 | 11-78 ×2: @296 [16,1,11,78,40,97,86]; @1669 [6,91,11,78,55,81,92] | |
| 5 | 11-24 standalone ×3 @731/@782/@1656 (@164 is cela-classified) | |
| 6 | 11-26 ×2 @239/@1559 | |
| 7 | @106 full P[106:114] = [0,46,11,21,67,93,29,89] (single 67@110) | |
| 8 | 11-11 @1523: P[1521:1529] = [31,24,11,11,48,96,87,46] | |
| 9 | @1288: P[1286:1294] = [68,0,11,17,84,59,35,94] | |
| 10 | @997: P[995:1002] = [60,67,11,96,82,33,0] | |
| 11 | 06→77 ×6; 06→11 ×4 | |
| 12 | @1044: P[1042:1049] = [82,63,11,67,76,85,41] | |
| 13 | @498: P[496:503] = [79,88,47,11,29,40,56] (flagback window) | |

---

## VERDICT

**De-dup CONFIRMED (load-bearing):** n11=45; 87-11 ×7; 47-11 ×3; standalone
35 — all re-derived exact. The finder's frame counts are clean.

**L1 06="ent/ment" — LEAD GRANTED.** The 3 "[X]-06 la [NOUN]" windows
re-derived exact (@320 [94,6,11,92]; @1123 [14,6,11,52,37,43];
@1721 [68,6,11,52,37,43]); 06→77 ×6 and 06→11 ×4 confirmed. Both readings
(3pl verb ending / "-ment" adverb) stay grammatical → the verb-vs-adverb
fork is queued for the stem battery. LEAD, not promotion — and note the
cross-frame support the finder cites (23-37-06 "concern-ent" @179) is
real but itself 06-conditioned.

**L2 "la 52-37-43" ×2 — LEAD for 37-postnominal-adjective.** Byte-identical
×2 @1123/@1721 re-derived. No finite-verb parse is available in the "la
[52] [37]" slot → 37 is adjectival-or-nominal here, non-finite at minimum.
Graded as LEAD (2 tokens, 1 phrase type — short of a frame grant), and it
does NOT restore the demoted est-frame (different frame; the est battery's
demotion stands). It is, however, the first multi-leg adjective-frame
evidence for 37 from outside the est family — the 37 war now has: est-frame
0 valid legs (demoted), post-nominal frame 2 tokens/1 type (lead),
verb-frames ("en ce qui 37", "que 84-24-37") live. Feed to the 37 battery.

**L3 78 fork votes — recorded as fork-conditional data.** @296
[16,1,11,78,40,97,86] ("la 78-40", "l'ère"-shaped → votes 78="er") and @1669
[6,91,11,78,55,81,92] ("la 78-55-81", "la vérité"-shaped → votes 78="ver")
both re-derived exact; 11-78 ×2 confirmed. The positional-allophony
hypothesis (78="er" before 40-type, "ver" before 55-type) is QUEUED for the
forks battery with these as the seed minimal pair — not ruled here.

**L4 "l'en-X" ×3 — LEAD (conditioned).** @731/@782/@1656 re-derived exact;
@164 confirmed cela-classified (excluded correctly). Conditioned on the
24="en" LEAD: "l'en-85 / l'en-42 / l'en-48" (envoi/entrée/enquête-class).
Three different second syllables → three words or one word with allophone
seconds — the battery the finder queues. The 48 tension ("est [pred] 48"
frames vs 48="trée") is flagged, not resolved.

**L5 26-noun ×2 — LEAD.** @239/@1559 re-derived exact ("[X] fois, la [26]…",
absolute construction). Two legs for 26 = feminine noun — this DIRECTLY
tensions 26=verb ("en ce qui 26-37") and the dead 23/26 homophone pair. The
26 noun-vs-verb battery is now priority (it also bears on P4's "qui se"
question via 76/68... no — via 26's own slot).

**L6 43/86 same-slot — observation recorded.** @562/@670 re-derived; one
window each → needs the noun batteries, no verdict.

**L7 @108 vs @106 — CONTRADICTION ADJUDICATED.** The physical window is ONE:
P[106:114] = [0,46,11,21,67,93,29,89] (67@110). The pour-beat reading rests
on BANKED 00="pour" ("pour que la [21] et…" iff 67="et"); the la-finder's
"veut" vote parses "que la [21] veut [93]" by DROPPING the banked 00@106
(their own "pour?" betrays it). Per bar L7: **the "veut" vote at @110 is
REJECTED as a fork datum** — unbanking 00="pour" (50/55 clean windows) on
one window's strength, without new evidence against 00 at @106, is not
allowed. Recorded as a conditional: IF 67="veut" were independently
established at @110, THEN 00≠"pour" at @106. The @106 window stays a
67="et" vote conditional on banked 00. Both conditionals handed to the
forks battery.

**L8 anomalies:**
- **A1 "la la" @1523:** verified ([31,24,11,11,48,96,87,46]). Queued:
  48's word-second-syllable profile ("en la [la-48…]" vs "là").
- **A2 @1288 "pour la fois":** verified ([68,0,11,17,84,59,35,94]).
  Cross-referenced to the pour battery's fenced @1287 mild tension ("pour
  la fois" unidiomatic; "pour la fois où…" marginal save). Fenced, not
  killing.
- **A3 @997 "la par":** verified ([60,67,11,96,82,33,0]). "la par" parses
  under no reading of banked 96="par" → either 96≠"par" here (mild
  adverse, fenced) or word-internal "l'ap-par…" (82="m" strains it).
  96-profile battery queued.

**@499 flagback — strain fenced.** P[496:503] = [79,88,47,11,29,40,56]:
"cela 29-40" ("cela ere…") doesn't parse cleanly. The 47-11="cela" at @498
is strained; the other two (@269/@357) are clean. Fenced as a 1-window
strain on the allophone's "cela" frame — not a break (cf. ce47 verdict).

**Queued:** 06 stem battery (verb vs adverb ending); 37 post-nominal battery
(@1123/@1721 vs verb frames); 78 positional-allophony battery (seed pair
@296/@1669); 85/42/48 second-syllable batteries; 26 noun-vs-verb battery;
43/86 noun batteries; 96-profile @997; 48 word-second-syllable @1523.
