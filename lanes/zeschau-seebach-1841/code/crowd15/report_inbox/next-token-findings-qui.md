# Next-token findings: "qui" (64) followers — all 47 windows

Method: every 64 occurrence extracted from the repaired 1,847-pair stream
(`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed per `code/side-keyhunt/repair_parse.py`); 3 following groups recorded.
Windows clustered by follower pattern FIRST; predictions second. Banked values
used: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que (GT); 87=ce, 64=qui,
96=par (promoted); 59=est, 77="le" (provisional); 31=VERBAL, 33=INF (class);
17="fois" (newly promoted). 87+11="cela" compositional at 7 windows.

## Cluster inventory (follower patterns, n=47)

| followers | windows | notes |
|---|---|---|
| 59-32-94 / 59-32-48 / 59-19-48 | @315, @1209, @1776 | "qui est" ×3; "est 32" ×2; "est _ 48" ×2 |
| 77-84-29 / 77-84-59 / 77-84-59 | @144, @1445, @1801 | "qui le 84" ×3; 29/59 alternate in slot 3 |
| 96-47-46 / 96-43-87 / 96-43-87 | @149, @341, @1025 | "qui par" ×3; 96-43-87 identical ×2 |
| 79-82-48 (identical) | @395, @1226 | trigram ×2 |
| 29-40-65 (identical) | @290, @684 | "qui er e 65" ×2 |
| 23-37-06 / 26-37-78 | @181, @1768 | "en ce qui" ×2 of 3; 23/26 same slot, 37 shared |
| 37-01-07 / 37-01-74 | @938, @1632 | "qui 37 01" ×2 |
| 31-14-45 / 31-10-03 | @337, @1646 | "qui [VERBAL]" ×2 |
| 02-58-47 / 02-97-40 | @608, @749 | "qui 02" ×2 |
| 52-38-47 / 52-82-16 | @1341, @1434 | "qui 52" ×2 |
| 06-52-89 / 06-91-11 | @1079, @1666 | "qui 06" ×2 |
| 47-76-87 / 47-68-06 | @1271, @1717 | "qui 47" ×2 |
| 98-82-43 / 98-65-88 | @18, @510 | "qui 98" ×2 |
| 32-01-08 / 32-48-84 | @32, @854 | "qui 32" ×2 |
| 46-07-64 | @791 | "qui que 07 qui" — oddity, see P11 |
| (singletons) | 15 windows | listed in cluster table above as needed |

Predecessors of "qui" (top): 87="ce" ×5 ("ce qui"), 03 ×4, 45 ×3, 37 ×3, 65 ×3.

## Ranked predictions

**P1 (HIGH). "ce qui" + predicate confirmed; "en ce qui" verb slot = 23/26-37.**
"ce qui" ×5 (87-predecessor: @149, @181, @1768, @1776, @1801); followers are
verb-shaped (23-37, 26-37), "est" (59), "le 84" — all predicate position, no
anomaly. "en ce qui" ×3: @179→23-37-06, @1766→26-37-78, @1774→59-19-48.
23/26 same slot + shared 37 = homophone candidates (or near-synonyms).
Predict: "concerne"/"regarde"-family verb ("en ce qui concerne" is the
diplomatic default).
TESTABLE: (a) 23/26 homophone battery — joint frames + Fisher on successors
(the {33,86} split precedent: 0/30 shared killed there); (b) 37's contact
profile as verb-second-syllable ("-cerne"/"-garde"); (c) NOTE 06="ent" verbal
ending in slot 3 @179: 23-37-06 could be "con-cern-ent" ("en ce qui
concernent", grammatical with plural). Do not force singular.

**P2 (HIGH). 32 = predicative (adjective or past participle), 2–4 legs.**
"qui est 32" ×2 (@315, @1209) + "qui 32" ×2 (@32: 32-01-08, @854: 32-48-84).
Followed by the ne-distributed pair 94/48 in THREE windows (@315: 32-94-06,
@854: 32-48-84, @1209: 32-48-96) — the {48,94} split precedent says these are
class-mates, and here they share the post-predicate slot.
Predict: predicative after "est" — diplomatic "nécessaire / important /
certain / évident" family (adjective vs participle left open deliberately).
TESTABLE: adjective/participle frame battery on 32's 4 windows; the 94/48
slot reads "ne…" or vowel-initial verb — note @1209's "…48-par" tension
against 48="à" (96="par" follows; flag, don't resolve here).

**P3 (HIGH). 19 = predicative, 2 legs.**
"est 19" ×2: @1774 ("en ce qui est 19-48") and @1776 ("ce qui est 19-48-74").
Both followed by 48 — "est 19 48" ×2, and with P2 that's THREE "est [pred] 48"
windows (@1209, @1776, @1774) vs one "est [pred] 94" (@315).
TESTABLE: same battery as P2; test 19/32 same-slot relation (both follow
"est"; compare their follower distributions — shared 48 is already 1 leg).

**P4 (HIGH as formula; NULL on the French reading). F-qui-par:
45-64-96-43-87-01 ×2 (6 groups).**
@341: 31-14-[45-qui-par-43-ce-01]; @1025: 92-64-[45-qui-par-43-ce-01] (with an
extra "qui" at 1023: "qui 45 qui par 43 ce"). Identical 6-gram ×2 + shared
45-predecessor + shared 01-successor = formula-grade, same species as
"par ce que" ×3. The French is NOT visible — do not force.
TESTABLE: (a) 45="ce"? — "45 qui" ×3 total; run contact-similarity vs 87
(the {47,87} positional-allophone precedent); (b) 96 verb-stem? — round 13
left 96 verb-stem inconclusive; test "par-"-family (parler/paraître) with
43="le" ("parle ce" noted as STRAINED — "parle ce 01" is poor French, keep the
strain on the record); (c) 87-01 as "ceci": only 2× corpus-wide — WEAK,
do not build on it.

**P5 (MEDIUM, open puzzle). "qui le 84" ×3.**
@144: 67-[qui-le-84-er]-ce (67 = et/veut fork); @1445: [est-37]-qui-le-84-est-36;
@1801: [79-ce]-qui-le-84-est-35. 29="er"/59="est" alternate in slot 3;
@1445/@1801 share "est" + consecutive followers (36/35 — weak).
No French reading forced: "qui le [84]-er" (infinitive?) vs "qui le [84] est
[noun/adj]" don't reconcile without 84's value. 77="le" is provisional and
the "le la" tension is already on record — do NOT re-derive 77 here.
TESTABLE: 84's contact profile first; then re-read the frame.

**P6 (MEDIUM). Trigram 79-82-48 ×2 identical (@395, @1226).**
82=m (GT letter) between 79 and vowel-initial 48 (H_stem: French lacks mC-
onsets, so 48 is vowel-initial if within-word — from the 48 syntax battery).
Contexts: @395: 67-qui-79-m-48-06; @1226: 57-qui-79-m-48-er.
Leads (not verdicts): "m'est avis" frame ("qui [79] m'est avis [que]…"),
"me"+verb ("qui [79] me [48-verb]…"), or 79-82-48 as one m-containing word.
TESTABLE: 79's contact profile (79="tout" lead interacts here — "qui tout
m…" is poor French, adverse noted); 48's vowel-initial set (à/a/es/et/il/un).

**P7 (MEDIUM). [09/92]+"ère" ×2 (@290, @684).**
"qui [09/92] er e 65" — identical except slot 1; 09/92 same-slot pair (same
shape as 23/26). Predecessors differ (09←09, 92←92 at -1; 00 at -2 both —
weak). Predict: "-ière/-ère" noun, 3-group word: "manière" ("de manière
[65]…"), "lumière", "dernière" family. (Cf. pencil crib: "première" =
pre-m-i-er-e, 5 groups; this is the 3-group -ère shape.)
TESTABLE: 09/92 homophone battery; 65's value (follows ×2 in same slot).

**P8 (MEDIUM). "qui 37 01" ×2 (@938: 37-01-07, @1632: 37-01-74).**
Bigram constraint on 37-01. Possible link to P1's 37 (verb-second-syllable):
"qui [?]37-01" — note, don't merge (different slot: here 37 is FIRST after
"qui").

**P9 (CORROBORATIVE). "qui 31 [VERBAL]" ×2 (@337: 31-14-45, @1646: 31-10-03).**
Two more legs for 31=finite-verbal (provisional-conditioned): "qui" directly
followed by finite verb, seconds differ (14 vs 10) as a class should. No new
value; strengthens the classification.

**P10 (WEAK, listed). Doublet slots "qui 02/52/06/47/98" ×2 each.**
@608/@749 (02), @1341/@1434 (52), @1079/@1666 (06), @1271/@1717 (47),
@18/@510 (98). No reading proposed; slot-pairs for future batteries.

**P11 (FLAG). @791: "…le-qui-que-07-qui-56…"**
"qui que" bigram + second "qui" two groups later. "Qui que ce soit" does NOT
fit (07≠ce-pattern, second 64≠soit). "Quoique" hypothesis: WEAK (phonetics
strained: qui≠quoi). Recorded as oddity, not pursued.

## Nulls and anti-predictions (honest)

- Top French guesses "qui a / ont / doit / peut / se": NO specific auxiliary
  pinned. The structural confirmation is 31=VERBAL ×2 (P9), not named verbs.
- "qui est" ×3 (@315, @1209, @1776) are all 59="est" — strengthens 59's
  provisional (conditioned frame), no new information about 59's third value.
- "cela" (87+11): no "qui"-window conflict — @1801 has 87 standalone before
  "qui" ("79-ce-qui"), consistent.
- P4's French reading: explicit NULL. The formula is real; the reading is not.

## Handoff to batteries (round 15)

Priority order: P2/P3 adjective battery (32, 19 — most legs, clearest frames) →
P1 23/26 homophone battery → P7 09/92 battery → P6 trigram → P4 formula hunter
(45="ce" contact test first — cheapest) → P5 after 84 is profiled.
