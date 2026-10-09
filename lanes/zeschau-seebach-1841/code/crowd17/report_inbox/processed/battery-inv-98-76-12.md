# Battery verdict: inv-98-76-12

- Target id: `inv-98-76-12`
- Claim: Adjudicate @12's "93 62 98 76" window.
- Date: 2026-10-09
- Worker: battery worker (subagent 95f89034-de16-4bc1-930e-5f6a2769c8e0)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed per
  `code/side-keyhunt/repair_parse.py`; 1,847 pairs / 96 types re-derived
  in-work, asserts held). `canonical.py` never used. R5005, sealed gate
  instances, and the red-team adjudication queue untouched.

Terms (ASD-STE100): "word-medial unit" = two groups forming one French word,
where the second group is a syllable inside the word, not a word on its own.
"complement-class residual" = a window where 98's complement cannot be
licensed under the standing vient complement inventory, so the window stays
unparsed pending new values. "inversion" = subject-verb inversion
("vient-il"), which needs a licensed trigger (question, subordination, or
initial adverbial).

## Bar (verbatim from battery-queue.json, pre-registered)

"State 62's role at @11 (word-medial unit with 93 vs independent, with byte
evidence) and give "vient [76]" any grammatical parse (inversion with stated
determiner facts, or other); else fence 98-76 as the second
complement-class residual alongside 98-65."

Numbered pass/fail clauses (fixed BEFORE the stream census, not modified after):

- **C1:** 62's role at @11 is stated with byte evidence (word-medial unit
  with 93 vs independent).
- **C2:** "vient [76]" receives at least one grammatical 1841-French parse
  (inversion with stated determiner facts, or other route).
- **Else-arm:** if C1 or C2 cannot be met, fence 98-76 as the second
  complement-class residual alongside 98-65, with stated cause.

Resolve-arm: C1 met AND C2 met → resolve. Else-arm: fence.

## Method

1. Read BATTERY-PROTOCOL.md first. Created
   `code/crowd17/next-token/locks/inv-98-76-12.lock` on start (agent id +
   2026-10-09T10:32:30Z); no stale lock present.
2. Re-derived the repaired stream byte-exact per `repair_parse.py`.
3. Full distributional census of 62 (n=35), 93 (n=14), 76 (n=21), and all
   40 98-windows with successor profile.
4. Adopted (not re-litigated): 98 = vient (battery promote, 37/40 windows
   consistent, subject slot left, complement inventory {de, pour, elided
   clitic} right); battery-vient-65-complement NULL (98-65 fenced as
   complement-class residual). Standing values per §7.

## Window-level evidence (all byte-verified on the repaired stream)

### The locus — @12 (row a1_00)

`... [8]78 [9]18 [10]93 [11]62 [12]98 [13]76 [14]45 [15]91 [16]53 [17]17
[18]64 [19]98 [20]82 ...` = "...[78] [18] [93] [62] vient [76] ce(47)
[91] [53] fois(17) qui(64) vient(98) m(82)..." All of 78/18/93/62/76 are
value-open; 47='ce' (A4), 82='m' (pencil), 17='fois' (promoted),
64='qui' (granted).

### C1 — 62's role at @11: INDEPENDENT (byte evidence)

- **62's predecessor profile is free-combining, not bound:** 21 distinct
  predecessors stream-wide (top: 21-noun ×5, 20×4, 74×3, 93×2, 03×2, 08×2,
  78×2, 92×2, then 13 singletons). A bound "93-62" unit would show a
  dominant 93 predecessor; instead 93 is 4th at ×2.
- **62 occupies verb-slot frames independent of 93:** "62 98" ×5 (@11,
  @802, @945, @1136, @1324), "62 94" ×9, "62 48" ×6, "62 16" ×4. At @802
  ("74 62 98 53") and @945 ("08 62 98 96") 62 sits in the same pre-98
  verb slot with no 93 present.
- **"93 62" carries no unit signature:** it occurs exactly 2× (@10, @1685)
  with divergent continuations — @10→98, @1685 ("79 65 13 93 62 94 79 14
  60") →94. 93's own successor profile is fully heterogeneous (62×2,
  52×2, 59, 29, 00, 54, 76, 88, 61, 06, 50 — no dominant bigram).
- **The word-medial reading is untestable at battery grade:** naming a
  French word for "93-62" would need both values named; both are open.
  Per §3 (never invent data), the bound-unit arm is fenced, not assumed.

**C1: PASS — 62 is an independent element at @11** (byte evidence above).

### C2 — "vient [76]": no licensed grammatical parse

- **98-76 is a stream singleton** (@12, the only "98 76" contact in
  1,847 pairs). 98's successor profile is dominated by the standing
  inventory: 83×5 ('de' lead), 82×3 ('m' clitic), 00×3 ('pour' grant).
  76×1 sits outside the inventory, next to the other singletons
  (51, 19, 81, 41). This is the second complement-class residual after
  98-65 — the inventory's complement is now 11/12.
- **Inversion route (subject-verb inversion "vient [76]"):** fails on both
  legs.
  - Trigger leg: no licensed inversion trigger at @12. The clause shows
    no question morphology (no punctuation survives in the cipher), no
    subordinator "que" (46 absent), no initial adverbial. Left context
    "09 00 97 51 47 41 06 77 78 18 93 62" contains no trigger.
  - Determiner leg: inversion needs a bare pronoun or a licensed nominal
    subject directly after the verb. 76's class is split at battery
    grade — nominal legs ("le [76]" ×3 at @832/@891/@968; "ce [76]" ×2
    at @1272/@1274) vs verbal legs ("ne [76]" ×2 at @651/@1576;
    "qui [76]" ×1 at @486). Neither class is forced, so the
    subject-nominal premise is ungrantable. A bare unvalued group as
    postposed subject is unlicensed.
- **Infinitive-complement route ("vient [76-inf]"):** "vient" licenses
  motion-verb + "de"/"pour" + infinitive, not bare infinitive; 98's
  inventory contains no bare-infinitive arm. 76's infinitive class is
  unproven anyway.
- **Adverbial/idiom routes:** no adverbial 76 frame exists in its 21
  windows; no 1841 idiom "vient [76]" is attested.
- **One-word route ("98 76" as one word):** barred by §7 — 98=vient is
  promoted as an independent finite verb (40 windows); the sole
  polyvalence (67 et/veut) does not extend here.

**C2: FAIL — no grammatical parse of "vient [76]" is licensed under
standing values and byte evidence.**

### Else-arm — fence 98-76

- C1 met, C2 not met → the bar's else-arm fires.
- **98-76 is fenced as the second complement-class residual alongside
  98-65** (battery-vient-65-complement). Stated cause: 76 lies outside
  the standing vient complement inventory {de, pour, elided clitic}
  (inventory members ×3–5, 76 ×1); inversion is triggerless and
  class-blocked; every other route is unlicensed at battery grade.
- Canonical-stream caveat: row a1_00 offset unvalidated.

## Per-clause results

- **C1: PASS** — 62 independent at @11 (21 distinct predecessors,
  verb-slot frames without 93, no "93 62" unit signature).
- **C2: FAIL** — "vient [76]" unparseable (inversion triggerless and
  class-blocked; complement route outside inventory; all other routes
  unlicensed or §7-barred).
- **Else-arm: TAKEN — 98-76 fenced** as second complement-class residual.

## Verdict: NULL (fence executed)

Not kill-grade: no window forces a falsehood about 98-76 (the bar's
else-arm is the designed outcome for exactly this state). No standing
verdict contradicted or downgraded: 98=vient promote untouched;
battery-vient-65-complement's 98-65 fence extended, not disturbed;
§7 intact. No red-team verdict touched.

## Follow-ups proposed (for supervisor queuing)

1. `val-76-class-census` (P3) — name 76's class from its 21 windows
   ("le [76]"×3 / "ce [76]"×2 nominal legs vs "ne [76]"×2 / "qui [76]"
   verbal legs). A forced nominal-76 re-opens the inversion route at
   @12; a forced verb-76 closes it. Bar: class named with ≥2
   frame-legs at battery grade.
2. `vient-complement-inventory-ratify` (P2, red-team input) — consolidate
   the {de, pour, elided clitic} inventory across all 40 vient windows
   (successors 83×5, 82×3, 00×3). If any inventory member breaks, 98-76
   and 98-65 both re-open. Red-team venue.
3. `inv-12-clause-parse` (P4) — parse the full a1_00 @0–20 clause once
   78/18/93/62 resolve; the inversion trigger may be identifiable from
   the left context ("09 00 97 51 47 41 06 77 78 18 93 62").

## Bookkeeping

- Queue: `inv-98-76-12` queued → verdict/null via temp-file + rename,
  own entry only; pre-write assert confirmed no prior verdict; JSON
  re-validated post-write.
- Lock `inv-98-76-12.lock`: created on start, deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
