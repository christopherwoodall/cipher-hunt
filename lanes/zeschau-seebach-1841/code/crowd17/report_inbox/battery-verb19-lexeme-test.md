# Battery verdict: verb19-lexeme-test

## Bar (verbatim from queue)

"classify each of 9 windows' 19 slot; all-9-parse promotes 19 to 32's class; forced non-verbal window fences/kills"

Restated as numbered clauses:
- C1: each of 19's 9 windows gets its 19 slot classified (finite / infinitive / participle / stem / other).
- C2: all 9 windows parse under one verb lexeme (R17-008's 32 class: finite forms, past participle, participle-modifier, passive — value unnamed) → promote 19 to 32's class.
- C3: any window forcing a non-verbal slot fences or kills the claim.

Adverses: none listed.

## Method

Read BATTERY-PROTOCOL.md first. Created `locks/verb19-lexeme-test.lock` on start
with agent id + UTC timestamp. Re-derived the repaired 1,847-pair / 96-type
stream in-session from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json` (parsed per `repair_parse.py`;
1,847 pairs, 96 types verified). `canonical.py` never touched. R5005, sealed
gate instances, red-team adjudication queue untouched. All @-offsets below are
1-based stream indices (adj-19 / inflect-19e-48 convention), verified against
the stream. 1841 diplomatic French only.

Standing values used: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que (GT
pencil); 87=ce, 64=qui, 96=par, 17=fois, 79="tout" (A5), 00="pour" (A9,
class-level), 84="on" (A15), 47="ce" (A4); 59=est, 77="le" (provisional);
48="e" letter-tier PROMOTE (R17-003); 06="ent" PROMOTE (battery, pending
ratification); 94="ne" STRONG LEAD (R17-001); 30="pas" promote (ne-drop lane
precedent, w2-pas-nelicense); 98=finite-verb class (§5-standing, prof-98);
24=finite-verb class (R17-009; value disputed — 24-en-verb-conflict queued,
class only used here); 32=one verb lexeme, class-level PROMOTE (R17-008);
76=noun promoted (masculine); 78="ver" lead; 21/65/36=noun class; 88=verb
class (battery, six legs, 2026-10-09 — registry still shows R18-era "gov",
noted at W3); 92/93=verb class (battery); 56=finite-verb class (w5-pas-verb);
41=verb/determiner/letter three-role split candidate (class-41-contact);
45="ce" hold (A11). Kills hold: 20="fois", 81="prin", 48="est"/"ne"/"de",
{48,94} homophone-set, 09/92 "-ère" value, 84="fait". Splits hold: 20~17,
23~26. 67 et/veut sole polyvalence (§7).

Corpus facts re-derived: n(19)=9; predecessors {01x2, 98, 90, 88, 10, 41, 59,
09}; successors {00x2, 41, 58, 74, 64, 18, 24, 48}. "19 48" exactly once
(@1779), "48 19" zero — same left-attachment morphology as "32 48" x4
(inflect-19e-48 C1). "19 29" zero — matches 32's profile (32 never takes 29
either), so no missing-infinitive adverse.

## Window-level evidence

**W1 @91 (row a1_02):** `62 16 14 06 88 77 66 98 19 41 98 81 97 46 29 85 08`
- Slot: STEM. "98 19 41 98": 98 is finite-verb class, so "98 [19-fin]" is two
  finites (dead); "98 [19-noun] [41-fin]" is two finites (dead);
  "98 [19-noun] [41-det] 98" puts a determiner after a noun (dead).
- Surviving parse: "[98-fin] [19-41-word]" — 41 in its attested word-final
  letter role (donn-41-44 @61 "53 12 [41]"), 19 as the stem; then
  "[98-fin] [81-noun]" (81 = masculine abstract noun class, battery).
  One stated assumption: the 41-letter role extends beyond @61.
- The nominal-19 rival needs two unevidenced clause boundaries ("le 66 [98].
  [19-noun] [41-fin]. [98-fin] [81-noun]" with the last clause subjectless) —
  strictly weaker. Classification: stem, lexeme-compatible; not forced
  non-verbal.

**W2 @122 (row a1_03):** `89 68 21 67 14 21 60 90 19 58 66 98 82 48 11 02 26`
- Slot: FINITE VERB. "[90-subj] [19-fin] [58-obj] [66-subj] [98-fin] me(82-48)":
  90 is hapax (class open — subject slot does not force class), 58 the object,
  66 subject of the following 98. No clause boundary needed. Clean.
- Nominal rival ("[90] [19-noun]") not forced — 90's class is open.
  Classification: finite; lexeme ✓.

**W3 @212 (row a2_00):** `92 63 42 06 77 44 50 88 19 74 77 78 06 59 46 29 42`
- Slot: INFINITIVE. "[88-verb] [19-inf] [74] [le(77) ver(78)]" — infinitive
  complement of 88 (battery 88=verb carries "infinitive after à, direct -er,
  causative faire" legs; causatives take bare infinitives). 74 = complement
  of the infinitive (class open).
- Note: registry still labels 88 ["gov","cls"] (R18-era); the battery-grade
  88=verb finding (2026-10-09, six legs) is the premise used. If 88's
  verb-hood is held to the registry label, this window weakens to
  compatible — flagged, not fenced. Classification: infinitive; lexeme ✓.

**W4 @329 (row a2_05):** `11 92 60 15 63 71 10 01 19 00 92 50 45 54 88 40 03`
- Slot: FINITE VERB. "[01-subj] [19-fin] pour(00) [92-verb]" — purpose clause,
  byte-identical in shape to noun26-69-pour-dire's "[69-N-subj] [26-V-fin]
  pour [33]". 92=verb class after "pour" = infinitive frame. Clean, no
  boundary. Classification: finite; lexeme ✓. Strong leg.

**W5 @486 (row a2_11):** `74 45 93 00 13 52 30 01 19 64 76 42 41 20 67 78 42`
- Slot: INFINITIVE (primary) / FINITE (alternate). "52 30(pas) 01 19":
  ne-drop is lane precedent (w2-pas-nelicense), licensing "ne pas + inf".
  Primary: "pas [01-clitic] [19-inf]" — "ne pas le dire"-shaped; 01's class
  is open (noun-19-486-relative: "'01 19' x2 confers no class"), clitic slot
  available. Alternate: "[52] pas (ne-drop 'V pas') | [01-subj] [19-fin]"
  with boundary before "qui".
- Consistent with noun-19-486-relative's KILL (that kill targeted the
  relative-clause rival "01 19 qui 76" — not re-litigated; neither parse
  here uses it). The "qui 76[noun]" anomaly stays fenced to the "qui"-syntax
  puzzles. Classification: infinitive; lexeme ✓.

**W6 @585 (row a3_02):** `55 61 94 82 06 06 50 10 19 18 14 00 97 41 41 09 00`
- Slot: FINITE VERB (weakest window). "[10-subj] [19-fin] [18] [14] pour(00)
  [97]": 10's class open (n=7; successors 03x2/01/62/19/29/22 — subject slot
  does not force class); 18 = adjective stem at the -ment locus (battery);
  14 open; postverbal 18/14 unresolved but non-contradictory. No auxiliary
  or governor for a participle/infinitive reading; no forced nominal slot.
- Nominal rival ("[10] [19-noun] [18-adj]") live — not forced either way.
  Classification: finite, lexeme-compatible; flagged as the weakest window.

**W7 @966 (row a6_00):** `04 20 67 96 00 86 56 41 19 24 06 77 76 01 98 48 51`
- Slot: NOMINALIZED INFINITIVE. "[56-fin] [41-det] [19-inf]": 56=finite-verb
  class (w5-pas-verb), 41 in its determiner role (class-41-contact @238
  "vient [det] fois") → "56 le [19]" = "le dire"-shaped object, standard
  French. The verb lexeme supplies nominal slots via its infinitive —
  same kind as 32's @1176 ("32e est", verbal morphology in subject slot,
  R17-008). Bare-noun rival live. Not forced non-verbal.
- The "[24] [06]" @968 function stays fenced to the 24-conflict venue
  (ent-06-host-census) — this parse does not depend on it.
  Classification: infinitive (nominalized); lexeme ✓.

**W8 @1779 (row a8_09):** `37 78 62 94 24 87 64 59 19 48 74 65 23 98 83 82 96`
- Slot: FEMININE PAST PARTICIPLE. "ce(87) qui(64) est(59) 19[e](48)" —
  R17-003 certified the 48 here as 'e'-inflectional; "19e" ∥ "32e"
  morphological parallel established (inflect-19e-48 C1). Under R17-008's
  re-tiering ("the participle analysis dissolves the adjective/verb
  tension"), this is the lexeme's feminine past participle. Clean.
  Classification: past participle; lexeme ✓. Strong leg.

**W9 @1822 (row a8_10):** `50 42 06 29 37 01 02 09 19 00 97 00 86 29 82 38 83`
- Slot: FINITE VERB. "[09-subj] [19-fin] pour(00) [97]" — purpose clause,
  same shape as W4. 09's verb hypothesis is fenced (two noun-forcing
  windows) → 09 noun-ish, subject available. "pour [97]" with 97 open is
  precedented ("pour [33]" with 33 open, noun26-69-pour-dire). Clean.
  Classification: finite; lexeme ✓.

## Per-clause results

- **C1 — PASS.** All 9 slots classified: finite x4 (W2/W4/W6/W9),
  infinitive x3 (W3/W5/W7-nominalized), past participle x1 (W8), stem x1 (W1).
- **C2 — PASS.** All 9 windows parse under one verb lexeme: the attested
  R17-008 slot inventory (finite, past participle, participle-modifier,
  passive) covers every window — finite (W2/W4/W6/W9), infinitive complement
  (W3/W5), nominalized infinitive (W7, cf. 32 @1176), feminine past
  participle (W8), stem+letter word (W1). Epistemic grading: strong
  (W4/W8), clean (W2/W3/W5/W9), compatible-with-live-nominal-rival
  (W1/W6/W7) — stated per window above, not hidden.
- **C3 — PASS (vacuous).** No window forces a non-verbal slot for 19.

Adverses: none listed. Standing-state check: no red-team verdict contradicted
(adj-19's adjective lead is battery-level; inflect-19e-48 already re-tiered
its implication verb-lexeme-ward at battery grade). §7 intact — one lexeme,
no polyvalence declared. Kills, splits, holds all intact.

## Verdict: PROMOTE (class level)

**19 = one verb lexeme (class-level), value unnamed** — joining 32's class
per R17-008 (same grant shape: "Value unnamed — class-level grant"). This is
a battery promote; red-team ratification required before it enters the
banked map.

Notes for the supervisor / red team:
- Queued `participle-19e-frame` (P3) is substantially answered: W8 selects
  the past-participle reading under the lexeme (the adjective rival is
  dissolved per R17-008's logic). Recommend closing or re-scoping it.
- W6 is the weakest window (finite parse available; nominal rival live) —
  flagged for red-team weighting, not fenced.
- W1's stem parse carries one stated assumption (41-letter role extends
  beyond @61).
- W3's infinitive parse carries the battery-grade 88=verb premise (registry
  still shows the R18-era "gov" label).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-verb19-lexeme-test.md` (this file).
- `battery-queue.json`: `verb19-lexeme-test` → status `verdict`, result
  `promote`, date 2026-10-09 (temp-file + rename, own entry only; pre-write
  assert confirmed queued/verdictless; JSON re-validated post-write).
- Lock `locks/verb19-lexeme-test.lock`: deleted on completion.
- `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
