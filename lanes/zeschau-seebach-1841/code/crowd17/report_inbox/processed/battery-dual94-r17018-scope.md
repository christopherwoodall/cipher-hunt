# Battery report: dual94-r17018-scope

- Target id: `dual94-r17018-scope` (P1)
- Claim: "RED-TEAM INPUT — package the 6 verb-less windows needing non-particle 94 for R17-018 adjudication. Evidence only, no value named, no adjudication."
- Date: 2026-10-09
- Worker: battery worker (subagent 603c569a-e90a-41d6-a69d-586f6bd8798d)
- Stream: repaired 1,847-pair / 96-type parse re-derived in-session from
  `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
  (parsed per `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs,
  96 types). `canonical.py` never used. R5005, sealed gates, red-team
  adjudication queue untouched.

Terms (ASD-STE100): "particle-'ne'" = 94 as the free verbal negator ("ne").
"word-final-'ne'" = 94 as the bound syllable "-ne" at the end of a word
("...ne"). "verb-less window" = a 94-window where the particle reading is
dead or strained at battery grade (no verb attaches to "ne"). "R17-018" = the
red-team escalation: 12/94 "ne" duality, FENCED as compatible mechanism (the
analytic 12-48 vs syllabic 94 spellings of "ne"). This report does not
adjudicate R17-018. It packages evidence for the red team. No value is named.
No second 94 value is declared (protocol §7: 67 et/veut is the sole true
polyvalence).

## Bar (verbatim, pre-registered before testing)

"Package the 6 verb-less windows needing non-particle 94 for R17-018
adjudication; the 3 attachable windows (@1330, @1705, @1773) keep
particle-'ne' per ne-94 battery and ne-24-profile; battery declares no
second 94 value (S7)"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** the 6 verb-less 94-windows (94 at @101, @509, @762, @841, @1363,
   @1687 — all of the form 62-94) are packaged with byte-exact contexts,
   row ids, standing values, and the adopted battery-grade reason the
   particle-'ne' reading is dead or strained at each.
2. **C2:** the 3 attachable windows (94 at @1330, @1705, @1773) keep
   particle-'ne', with the adopted ne-94 / ne-24-profile evidence cited per
   window.
3. **C3:** no second 94 value is declared; the package is segmentation-only.
   Battery grade only; the red-team decision target `redteam-94-functional-split`
   is queued and untouched.

Adverse: the queue entry carries a supervisor note ("red-team venue item -
do not dispatch as a battery worker"). This worker was dispatched by its
parent; the note is honored in substance: evidence only, no value named, no
adjudication, red-team queue untouched.

## Method

1. Read BATTERY-PROTOCOL.md first. Created
   `code/crowd17/next-token/locks/dual94-r17018-scope.lock` on start
   (2026-10-09T12:04Z); no prior lockfile present.
2. Re-derived the repaired stream in-session: 1,847 pairs, 96 types (asserts
   held). All @-offsets below are 0-based repaired-stream indices.
3. Re-derived the 62-94 bigram census byte-exact: exactly x9 — 62 at @100,
   @508, @761, @840, @1329, @1362, @1686, @1704, @1772 (94 at +1 each). n(94)
   = 37.
4. Adopted (not re-litigated, cited with standing verdicts):
   - `seg-62-94-wordfinal` KILL (2026-10-09): the x9-as-word-final-'ne' claim
     is false at kill grade (@1772 forces a word break under standing
     promoted values: "[62] ne [24-fin] ce qui est" is the only parse; a word
     before a finite verb is ungrammatical). The kill narrows the live residue
     to the 6 D3-un-attachable windows.
   - `seg-62-94-wordless6` PROMOTE (2026-10-09): word-final-'ne' segmentation
     SUPPORTED at the 6 windows, W predominantly noun-class (4/6). The
     @1363/@1687 tension is resolved (both noun under the best parse).
   - `ne-94-right-context` PROMOTE (2026-10-09): 37-window right-context
     census; 11/37 windows provably cannot be the verbal negator (6 word-final
     '-ne' + 5 other non-particle frames).
   - `ne-94 battery` PROMOTE (standing): 94='ne' STRONG LEAD (R17-001);
     7 clean verbal-negator windows.
   - `ne-24-profile` PROMOTE (2026-10-08): 24 = finite verb (infinitive-taking,
     modal-shaped), class-level.
   - `x-61-94-boundary` PROMOTE (2026-10-09): "61 94" 2x (94 at @578, @1169)
     forces a two-word boundary `61 | 94`; boundary-side evidence for 94 as
     free word outside the 62-94 family.
   - R17-018 (next-token-redteam-r17, §C): 12/94 "ne" duality FENCED as
     compatible mechanism; neither 12="n" nor 94="ne" downgraded.

## The 6 verb-less windows (package for R17-018)

Each is a 62-94 window where the particle-'ne' reading is dead or strained at
battery grade and the adopted live reading needs non-particle 94
(word-final '-ne' syllable, or a red-team-declared second value). W = the
word formed as [62-value]+"ne" (62's value not named anywhere below).

### W1: 94 @101 (62 @100), row a1_02
Byte context: `85 8 [21] [62 94] [93-verb] [59]`.
- Left: 21 (noun, battery-promoted). Right: 93 (verb class, battery-promoted).
- Particle reading: "[21] 62 ne [93-verb]" — under the "il ne" left profile
  (il-62 battery PROMOTE) this gives "noun + il + ne + verb": 21 is a noun,
  not a subject pronoun, and the unattached "il" has no slot; the window has
  no grammatical parse under either class (wordless6 W1: NEITHER; gap, not a
  kill).
- Word reading: "[21] [W]ne [93-verb]": W directly before a promoted verb
  with no subject/relativizer — no clean parse; compatible only.
- Status for the red team: verb-less (no clean particle parse); the word
  reading is the only open route.

### W2: 94 @509 (62 @508), row a3_00 — ANCHOR
Byte context: `21 67(et) [77-le,prov] [62 94] [64-qui,granted] [98]`.
- Particle reading: "et le [62=il?] ne qui [98]" — 'ne qui' is a fenced
  anomaly (R17-022: "ne qui" singleton; the left edge "le il ne" failed at
  kill grade). Dead.
- Word reading: "et le [W]ne qui 98" — determiner + masculine -ne noun +
  relativizer. CLEAN (w508-noun-ne candidates: {moine, trone, prone, cone,
  hymne}). This resolved the R17-022 fenced residual. DEMONSTRATED.
- Status for the red team: verb-less; word-final-'ne' demonstrated at
  battery grade.

### W3: 94 @762 (62 @761), row a5_03 (gloss-anchored row)
Byte context: `[29-er,GT] [40-e,GT] [20] [62 94] [59-est,prov] [39]`.
- Particle reading: "[20] 62 ne est ..." — no verb attaches; 20's class is
  fenced (conj-prep-20-wide NULL), and "ne" has no licensed negated verb in
  the frame.
- Word reading: "[20] [W]ne est [39]" — W as subject of copula "est" = nominal
  slot (wordless6 W3: NOUN; class fixed by slot, cleanliness load-bearing on
  open 20/39).
- Status for the red team: verb-less; nominal word-final-'ne' at battery
  grade.

### W4: 94 @841 (62 @840), row a5_06
Byte context: `[17-fois,prom] [98] [20] [62 94] [26-noun] [12-n]`.
- Particle reading: "[20] 62 ne [26-noun]" — no verb in frame; dead.
- Word reading: "[20] [W-verb] [26]" — S-V-O with V+O core clean (26 = noun,
  battery-promoted); subject 20 open. Noun fails ("[W] [26]" noun+noun
  ungrammatical). Class: VERB (weak).
- Status for the red team: verb-less; the only outlier window where the
  word-final-'ne' word reads verb-class (weak).

### W5: 94 @1363 (62 @1362), row a7_06
Byte context: `[35] [13] [92-verb-class,prom] [62 94] [79-tout] [14]`.
- Particle reading: "[92] 62 ne tout [14][60]" — no verb in the negated frame
  (92 is verb-class itself; "92 ne" has no licensed parse); dead.
- Word reading: "[92-verb] [W-noun]" — V+O, direct-object slot. Class: NOUN
  (preferred; rests on 92's PROMOTED verb class). The parent's 'donne'-verb
  weak pass is superseded (it loaded on the below-standard 92-nominal
  subset).
- Status for the red team: verb-less; nominal word-final-'ne' at battery
  grade.

### W6: 94 @1687 (62 @1686), row a8_05
Byte context: `[65-noun,R18] [13] [93-verb-class,prom] [62 94] [79-tout]`.
- Particle reading: "[93] 62 ne tout ..." — no verb in the negated frame;
  dead. (Note: neque-79-twin-frame battery found no licensed shared 'ne'
  structure with the @1363 twin; still NULL.)
- Word reading: "[65] [93-verb] [W-noun] tout" — S-V-O-Adv. Class: NOUN
  (clean; 65 = noun R18, 93 = verb class promoted).
- Status for the red team: verb-less; nominal word-final-'ne' at battery
  grade.

Summary for the red team: 4/6 windows (W2, W3, W5, W6) support a nominal
word-final-'ne' segmentation at battery grade; W1 is verb-less with no clean
reading either way (gap); W4 is verb-less with a weak verb-shaped word
reading. The particle-'ne' reading is dead or strained at all six.

## The 3 attachable windows (keep particle-'ne')

### A1: 94 @1330 (62 @1329), row a7_04
Byte context: `[56] [30-pas] [06-ent,prom] [62 94] [70-pre,GT] [52]`.
- "il ne pre[70]" under the "il ne" left profile (il-62 battery). Particle
  'ne' marginally viable (ne-94-right-context: conditional; 'pre' admits no
  verb, but the left "il" profile keeps the negator frame open).
- Word reading dead: "[06] [W]ne pre[70]" — no clean parse
  (seg-62-94-wordfinal C3). The x-61-94-boundary promote (61 | 94 boundary
  at @578) is a parallel data point for free 94 after syllabic stems.
- Status: particle-'ne' stands. NOT part of the verb-less 6.

### A2: 94 @1705 (62 @1704), row a8_06
Byte context: `[94] [30-pas] [20] [62 94] [88-verb-class] [26-noun]`.
- "[62=il] ne [88-V] [26]" — "il ne [verb]": clean verbal-negator window
  (ne-94-right-context, clean list). The @1541 parallel ("Il [93-fin]
  [88-inf] le [78]") shows 88 non-finite there, but A2's 88 is the
  governing verb of "ne"; no contradiction at battery grade.
- Status: particle-'ne' stands (clean). NOT part of the verb-less 6.

### A3: 94 @1773 (62 @1772), row a8_09
Byte context: `[26] [37] [78] [62 94] [24-fin/modal] [87-ce,granted]`.
- "[62-subj] ne [24]. Ce qui est ..." — clean, promoted by ne-24-profile
  (lone-'ne' is the author's norm: 34/37 baseline; clause boundary before
  87). This is the kill-grade window that falsified the x9 word claim.
- Status: particle-'ne' stands (promoted). NOT part of the verb-less 6.

## The red-team question (packaged, not answered)

The lane's evidence now holds two battery-promoted facts side by side:

1. At 7 windows (plus 8 conditional), 94 is the free verbal negator
   particle ("ne"). Cleanest: A3 @1773, A2 @1705.
2. At 6 windows, 94 is the bound word-final '-ne' syllable of a
   noun-shaped word (4/6; W4 weak verb-shaped; W1 gap). Cleanest: W2 @509
   ("et le [W]ne qui" — the R17-022 residual resolved), W6 @1687
   (S-V-O-Adv with R18 65-noun + promoted 93-verb-class).

The battery cannot declare a second 94 value (§7). The options on the
R17-018 / redteam-94-functional-split docket, with the evidence each way:

- **(a) Declared positional/functional split** (preverbal negator vs
  word-final "-ne", a la 67 et/veut): would be the lane's second true
  polyvalence. Battery evidence is consistent (two disjoint, clean
  populations: 7+8 particle windows, 6 word-final windows, zero overlap).
  The tension it would resolve: W2's demonstrated word parse cannot be
  particle-'ne'; A3's promoted particle parse cannot be word-final-'ne'.
- **(b) R17-018's fenced 12/94 duality already covers it**: the analytic vs
  syllabic "ne" spellings are the homophonic cipher's ordinary mechanism.
  Open question for the red team: does the 12/94 duality cover *bound
  word-final* "-ne" as a syllable (W2/W3/W5/W6), or only the free-particle
  vs analytic spellings? The W4 weak-verb window and the W1 gap do not
  decide it.
- **(c) Word-final '-ne' belongs to the stems, not 94** (e.g. the "-ne"
  nouns are whole-word cells and 62-94 is a boundary artifact): killed for
  the x9 claim at @1772 but NOT tested at W2/W5/W6 (the "prenne" anchor
  x2 keeps a syllabic-94 precedent live: 70-12-94 = 'pre'+'n'+'ne',
  battery-verified).

Explicitly NOT decided by this battery: 94's value at any window; 62's
value anywhere; whether R17-018's fence extends to bound word-final '-ne'.

## Per-clause pass/fail

1. **C1 PASS** — all 6 verb-less windows packaged above with byte-exact
   contexts (re-derived in-session: 1,847 pairs, 96 types; 62-94 x9 census
   byte-exact), row ids, standing values, and adopted battery-grade reasons
   the particle reading is dead or strained (cited: seg-62-94-wordfinal,
   seg-62-94-wordless6, ne-94-right-context).
2. **C2 PASS** — the 3 attachable windows keep particle-'ne' with adopted
   evidence cited per window (A1: ne-94-right-context conditional;
   A2: ne-94-right-context clean; A3: ne-24-profile promoted).
3. **C3 PASS** — no second 94 value declared; segmentation only; §7 intact;
   `redteam-94-functional-split` queued and untouched; no red-team verdict
   contradicted or downgraded.

## Verdict: PROMOTE (evidence package delivered; no value named, no adjudication)

Ruling-ready input for the R17-018 red-team docket: the 6 verb-less windows
needing non-particle 94 (4/6 nominal word-final-'ne' at battery grade, W1
gap, W4 weak-verb outlier) and the 3 attachable windows keeping
particle-'ne' (@1330 conditional, @1705 clean, @1773 promoted). The
three-way scope of the red-team question ((a) declared split, (b) R17-018
duality coverage, (c) stem-owned "-ne") is stated with the battery evidence
for each. No cipher value named. No polyvalence declared.

No follow-ups proposed (promote; the docket target
`redteam-94-functional-split` owns the continuation).

## Bookkeeping

- Lock `code/crowd17/next-token/locks/dual94-r17018-scope.lock` created on
  start (2026-10-09T12:04Z), no prior lockfile; deleted on completion
  (verified gone).
- `battery-queue.json`: `dual94-r17018-scope` status `queued` -> `verdict`,
  `verdict: {"result": "promote", "report": "code/crowd17/report_inbox/battery-dual94-r17018-scope.md", "date": "2026-10-09"}`
  (temp-file + rename; pre-write assert confirmed queued/verdictless — no
  downgrade; JSON re-validated; only this entry touched).
- R5005, sealed gate instances, red-team adjudication queue untouched.
  Canonical-stream caveat stands (68/70 upstream row offsets unvalidated).
