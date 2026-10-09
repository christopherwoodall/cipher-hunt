# Battery report: form-24-643

- Target id: `form-24-643`
- Claim: decide 24's form at @643 (finite vs 'en' residual); finite-24 kills the finite-88 reading here, 'en'-24 re-opens it.
- Date: 2026-10-09
- Worker: battery worker (subagent 2314dbfc-426c-4133-9549-58f8fb95d35b)
- Stream: repaired 1,847-pair / 96-type parse re-derived in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (asserts held: 1,847 pairs, 96 types, n(24)=52 re-derived). `canonical.py` never used. R5005, sealed gate instances, and the red-team adjudication queue untouched. No stale lock existed; `code/crowd17/next-token/locks/form-24-643.lock` created on start (2026-10-09T11:16:11Z), deleted on completion.

## Bar (verbatim, from battery-queue.json)

"name 24's form at @643 with zero ungranted assumptions; fence if undecidable"

Numbered pass/fail clauses (pre-registered before testing, not modified after):

1. **C1:** 24='en' at @643 is dead at kill grade — 'en' is ungrammatical in both its functions (adverbial pronoun and preposition) with no rescue under standing values.
2. **C2:** 24=finite at @643 is forced with zero ungranted assumptions — no licensed alternative reading under standing values.
3. **Verdict rule:** name the form iff C1 and C2 both pass (one arm dead, the other forced, nothing assumed beyond standing grants); kill iff the window forces 24 to be neither; else NULL (fence) with 1–3 follow-ups.

Adverses: none listed.

## Terms

- **24:** the cipher pair under test. Standing: 24=finite verb (class-level, ne-24-profile battery PROMOTE 2026-10-08; R17-009); 24='en' is a live residual arm (A3 GT); the 24="faire" value was REJECTED (R18-008). The global 24 question is docketed at the red team (24-en-verb-conflict, NULL-escalated 2026-10-09).
- **'en'-kill:** a window where 24='en' is ungrammatical as pronoun ('en' must sit directly before a verb) and as preposition ('en' needs a noun-phrase complement; bare "en ce" is ungrammatical).
- **Standing values used:** pencil 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que; granted 87=ce, 64=qui, 96=par, 17=fois, 79="tout" (A5), 00="pour" (A9), 84="on" (A15), 47="ce" (A4 allophone tier), 94="ne", 30="pas", 12="n", 48="e"; provisional 77="le", 59="est"; §7 sole true polyvalence (67 et/veut; positional rule: 67="veut" iff follower is infinitive-shaped). 1841 diplomatic French throughout.

## Method

1. Read BATTERY-PROTOCOL.md in full before touching anything.
2. Re-derived the repaired stream byte-exact per `code/side-keyhunt/repair_parse.py`. All @-offsets below are 0-based pair indices.
3. Re-derived the locus census in-session (not cited from memory): "24 87" x10/52 (matches ne-24-profile); "20 24" x1 stream-wide (the locus only); n(20)=15.
4. Tested both arms against the locus window with standing values only. Adopted, never re-litigated: 87='ce' (granted), 48='e' (letter, promoted), val-61-contact (KILL of any global 61 value, stands), frame-20-62-94 (NULL — 20's class paradox unresolved), 89-noun-89-inf (NULL — 89's class unresolved).

## Window-level evidence

### The locus — 0b@643 (row a4_02)

`[639]77 [640]89 [641]48 [642]20 [643]24 [644]87(ce) [645]61 [646]88 [647]78`

Wider clause (0b@636–656): `que(46) [60] et(67) le(77) [89] e(48) [20] [24] ce(87) [61] [88] le(77) [78] [52] m(82) ne(94) [76] [49] [24] [26] pas(30)`

- @643 is the ONLY "20 24" bigram in the stream (n=1).
- @643 is the ONLY "24 87 61" trigram in the stream (the ten "24 87" windows have followers 11 x3, 64 x3, 98 x1, 61 x1, 59 x1, 08 x1).
- 67 at @638 = 'et' by the standing positional rule (follower 77 is not infinitive-shaped); a conjunction cannot subject a verb.

### C1 — the 'en'-kill at @643 (re-derived, not cited)

"en" tested in both functions:

- **Pronoun:** 'en' must sit directly before a verb. @644=87='ce' (granted) is not a verb. Clitic skip over @645=61 to reach @646=88 is ungrammatical. "en"+"ce" is not a valid clitic cluster. Dead.
- **Preposition:** 'en' needs a noun-phrase complement. @644=87='ce' gives bare "en ce", which is ungrammatical ("en ce moment" needs the noun).
- **Rescue "en cela":** needs 87+11 ("cela"). @645=61, not 11. 61='la' is ungranted, and val-61-contact's KILL of any global 61 value stands. Dead. (Positive control: "24 87 11" at @73/@829 IS grammatical "en cela" — the lane's own contrast shows exactly which rescue works and why @643 lacks it.)
- **Rescue "en ce que":** needs 46 after 87. @645=61. Dead.
- **Rescue via later verb ("ne"-less):** no 94 adjacent to @643 (@651=94 is eight tokens away, across 87 61 88 77 78 52 82). Dead.
- **Rescue via imperative postverbal "en":** order wrong (24 precedes). Dead.

**C1: PASS.** 24='en' is dead at @643 at kill grade, using only the granted value 87='ce'. This agrees with 24-en-verb-conflict's C1, which independently lists @643 in its six 'en'-kill windows. No standing verdict contradicted.

### C2 — is finite-24 forced at @643?

A finite verb needs an overt subject (French has no pro-drop). Subject scan of the clause under standing values only:

- @642=20: class UNRESOLVED (frame-20-62-94 NULL; determiner/adjective leg vs feminine-noun leg — paradox stands). Not ruled out, not confirmed.
- @641=48: 'e' letter (promoted). A letter cannot subject a finite verb. Ruled out.
- @640=89: class UNRESOLVED (89-noun-89-inf NULL; noun arm conditional on provisional 77='le', never granted). Not confirmed.
- @639=77: 'le' (provisional). An article/object pronoun cannot subject a finite verb. Ruled out.
- @638=67: 'et' (standing positional rule). A conjunction cannot subject. Ruled out.
- @637=60: value unknown. Not confirmed.
- Wider ("que" at @636 opens a subordinate clause; "que"+finite needs a subject after "que"): no confirmed subject-shaped token between @636 and @643.

The only live candidate is 20, and naming it as subject needs 20's noun arm — an ungranted assumption (frame-20-62-94 is NULL). The verb reading is NOT killed (20's noun arm is live, so the no-subject kill fails), but it is NOT forced either.

**C2: FAIL.** Finite-24 at @643 is the sole surviving standing arm, but naming it needs an ungranted assumption (an unidentified, subject-shaped 20). The bar demands zero ungranted assumptions.

## Verdict: NULL (fence executed)

Neither form is forced at @643. The 'en' arm is dead at kill grade (C1 PASS); the finite arm survives but is unforced (C2 FAIL). Per the bar's own rule — "fence if undecidable" — the form cannot be named with zero ungranted assumptions.

**Consequence for the parent (fin-88-645):** that report's assumption (3) — "dissolving the [finite-24/finite-88] collision requires assuming 24 is the 'en'-residual here — a live but unproven arm" — is now refuted at @643: the 'en' arm is not live here; it is dead at kill grade. The collision therefore stands unrescued by the 'en' route. Whether finite-24 is the actual form at @643 (which would kill the finite-88 reading per the parent's logic) stays open pending the subject question. This report does not re-litigate fin-88-645 (verdict/null stands; no downgrade).

No standing or red-team verdict contradicted or downgraded. §7 intact (no battery-level polyvalence invoked). Canonical-stream caveat stands (row a4_02 offset unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json, 2026-10-09)

1. `subj-20-642` (P3) — resolve 20's class at @642 (noun-subject arm vs determiner/adjective arm of the frame-20-62-94 paradox). This is the direct blocker of C2: a subject-shaped 20 licenses finite-24 at @643; a non-subject 20 kills it. Bars: name 20's class at @642 with >=2 independent frame-legs; state the stated consequence for finite-24@643. Do not re-litigate frame-20-62-94 globally.
2. `fin24-1486-parallel` (P3) — force finite-24 at the parallel "24 87" window @1486 ("que l'on [24] ce": 46 77 84 24 87 08), where the subject "l'on" (=77+84) IS available under standing values. Same "24 ce" shape as @643, subject identified. Bars: promote-24=finite@1486 iff the subject parse holds with zero ungranted assumptions and 'en' stays dead there; a forced parallel gives finite-24@643 frame-consistency.
3. `form-24-654` (P3) — decide 24's form at @654, the second 24 in the same clause ("ne(94) [76] [49] [24] [26] pas(30)"). One finite verb per clause constrains @643: if @654 is forced finite, @643's 24 cannot also be finite, which tensions the C2 survivor. Bars: name 24's form at @654 with zero ungranted assumptions; state the stated consequence for @643; fence if undecidable.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-form-24-643.md` (this file).
- Queue: `form-24-643` queued → verdict/null, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/form-24-643.lock`: created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
