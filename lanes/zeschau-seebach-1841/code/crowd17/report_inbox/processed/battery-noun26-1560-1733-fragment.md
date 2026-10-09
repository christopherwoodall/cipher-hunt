# Battery report: noun26-1560-1733-fragment
Date: 2026-10-08. Worker: 7cfd0356-e30e-482c-ba94-23d1bbd53e84.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt), parsed like code/side-keyhunt/repair_parse.py.
canonical.py NOT used. R5005 untouched. All @-offsets are repaired-stream
pair indices. Target id: `noun26-1560-1733-fragment` (priority 2).

## Bar (verbatim from battery-queue.json)
"parse the @1733 '30 06 60 12 48' fragment (no noun crux; use the 12='n'/48='e'
letter-level foothold); state the construction that licenses it and apply it to
@1561's right side; else fence with stated cause."

## Bar as numbered pass/fail clauses (frozen from the bar text; not modified after testing)
- Clause 1: parse the @1733 "30 06 60 12 48" fragment with no noun crux,
  using the 12='n'/48='e' letter-level foothold.
- Clause 2: state the construction that licenses the fragment.
- Clause 3: apply that construction to @1561's right side.
- Clause 4 (else-branch): if clauses 1-3 cannot be met at battery grade,
  fence with stated cause.

## Method
Re-derived @1733 and @1561 windows on the repaired stream; censused "12 48"
(5x), "60 12" (2x), "94 52" (3x), 52's 27 windows, and 60's 18 windows.
Standing values only: banked pencil (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e,
46=que), granted/promoted set per protocol §7 (30=pas battery-promoted,
87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce, 94=ne
battery-promoted pending red-team ratification, 12=n / 48=e letters).
pas-30 battery's "pas ..., pas ..." clause-boundary adjacency taken as
standing, not re-litigated. ne-alone-02-74 owns the internal licensing of
"pas [06] [60]" — not re-litigated per the adverse.

## Window-level evidence (all re-derived on the repaired stream)
1. **@1733 window** (row a8_07): `...88 24 30 15 01 56 | 30 06 60 12 48 | 52 86
   12 34 94 82 46` — i.e. @1729=30(pas), @1733=30(pas), @1734=06, @1735=60,
   @1736=12(n), @1737=48(e), @1738=52. **No noun crux**: the fragment's left
   neighbor is "56", inside the first pas-limb "pas 15 01 56" (pas-30 battery);
   no determiner+noun precedes. The "30 06 60" trigram is left-independent
   here — "30 06 60" occurs exactly 2x stream-wide (@1561→71, @1733→12).
2. **"12 48" = "ne" particle, established**: 5x stream-wide —
   @169 ("53 ne 21"), @709 ("53 ne 71"), @809 ("41 ne 24", 24=finite-verb
   class: clean preverbal "ne"), @1075 ("98 ne 77 78": "ne le[77] [78-verb]",
   the proclitic cluster "ne le + verb", grammatical), @1736 ("60 ne 52").
3. **"[60]ne"-as-one-word rival KILLED distributionally**: "60 12" occurs 2x;
   the other instance @700 ("94 60 12 98 20") is followed by 98, not 48.
   12 does not bind to 60 as a fixed "-ne" ending. Segmentation is
   "60 | 12 48", not "60 12 48".
4. **52 is verb-shaped**: n(52)=27; "94 52" x3 (@570 "ce ne [52] ce",
   @1293/@1806 "on est [35] ne [52] [80]") — 94='ne' precedes, so 52 sits in
   the verb slot; "52 30" x2 — "pas" follows 52 twice ("[52] pas" order).
5. **The "ne [52]" frame in dual spelling** (R17-018 duality, byte-level):
   "94 52" x3 (@570/@1293/@1806, group-94 spelling) vs "12 48 52" @1736
   (letter spelling n+e). Same syntactic frame, two spellings — analytic
   versus syllabic segmentation of the same "ne".
6. **No downstream "pas"**: zero 30-tokens in the 111 pairs after @1738, so
   "ne [52]" is not the first half of a split "ne ... pas". The reversed
   pairing ("pas" @1733 precedes "ne" @1736) rules out "ne [52] pas".
   "ne...que" considered and rejected: "12 34" ("ni") intervenes between 52
   and 46="que", breaking the restrictive frame.
7. **@1561 window** (row a8_00): `...40 17 11 26 | 30 06 60 71 50 29 24 74...`
   = "...e fois, la [26] | pas [06] [60] [71] [50]er [24-verb]..."
   (29=er banked). Same "30 06 60" left-independent fragment as @1733,
   followed by its own new clause "71 50...".

## Per-clause pass/fail
- Clause 1 (parse @1733 fragment, no noun crux, letter foothold used): PASS.
  "30(pas) 06 60" | "12(n) 48(e) 52" = "pas [06] [60]" (second limb of the
  standing asyndetic "pas ..., pas ..." adjacency) + "ne [52-verb]" (new
  clause headed by analytically-spelled "ne"; 52 verb-shaped per evidence 4).
  No noun precedes (evidence 1); the word-ending rival is dead (evidence 3).
- Clause 2 (state the licensing construction): PASS. (a) Asyndetic
  "pas ..., pas ..." — the "30 06 60" limb is the second pas-headed
  elliptical fragment (pas-30 battery, standing). (b) Clause-initial "ne"
  spelled 12+48 opens the next clause: "ne [52-verb]", the R17-018 duality
  demonstrated in one frame (evidence 5).
- Clause 3 (apply to @1561's right side): PASS. @1561's right side is the
  same left-independent "pas [06] [60]" fragment followed by a new clause
  ("71 50..."). The @1733 parallel proves "30 06 60" needs no noun to its
  left — so at @1561 "pas" heads RIGHT: "la [26]" | "pas [06] [60] [71]...",
  confirming the forced 26|30 boundary from noun26-1560-pas.
- Clause 4 (else-branch): N/A — clauses 1-3 met.

## Fenced residuals (stated cause, none ignored)
- R1: "ne [52]" has no postverbal "pas" → reads as literary sans-pas
  negation; licensed iff 52 belongs to the admitting verb set; 52's value is
  open. (Follow-up 1.)
- R2: internal licensing of "pas [06] [60]" ("pas de"-ellipsis vs other) —
  owned by queued ne-alone-02-74; 06's value contested (06-value battery
  nulled). Not re-litigated per the adverse.
- R3: values of 06/60/52 remain open; this promote is constructional
  (segmentation + frame), not a value promote.

## Adverses answered (none ignored)
- "narrower than the bare-pas umbrella (ne-alone-02-74) — do not re-litigate
  ne-alone": ANSWERED. The internal licensing of "pas [06] [60]" is untouched;
  the pas-30 battery's "pas ..., pas ..." adjacency is taken as standing.
  This battery owns only the segmentation, the "ne [52]" frame, and the
  @1561 application.

## Verdict: PROMOTE (battery-level, constructional)
The @1733 "30 06 60 12 48" fragment parses as "pas [06] [60]" + "ne [52-verb]"
with no noun crux; the construction (asyndetic pas-limb + analytic-"ne"-headed
clause) applies to @1561's right side, confirming "pas" heads right of the
26|30 boundary. Names no values for 06/60/52. New byte-level finding: the
"ne [52]" frame in dual spelling ("94 52" x3 vs "12 48 52" @1736) —
direct evidence for the R17-018 12/94 "ne" duality as analytic vs syllabic
segmentation. No standing verdict contradicted or downgraded; R5005, sealed
gates, and the red-team queue untouched.

## Follow-up targets (for the supervisor to queue)
1. verb-52-frames (P2) — bar: name 52's value/class on its 27 windows;
   decides whether "ne [52]" @1736 (and "94 52" @570/@1293/@1806) is literary
   sans-pas negation or needs reanalysis. Distributional verb-hood ("94 52"
   x3, "52 30" x2) is the leg to confirm or kill.
2. dual-ne-52-packet (P3) — bar: assemble the R17-018 red-team evidence
   packet: "ne [52]" in both spellings ("94 52" @570/@1293/@1806 vs
   "12 48 52" @1736) plus "12 48"="ne" particle windows @809 ("ne 24-verb")
   and @1075 ("ne le 78-verb"); state whether the duality is positional,
   free, or clerk-driven.
