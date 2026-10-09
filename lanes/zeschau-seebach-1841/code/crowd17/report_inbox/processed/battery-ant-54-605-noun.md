# Battery report: ant-54-605-noun — name 54's class at @605

- Worker session: a4c83dff-e5de-434a-beed-eee2987e4ee3
- Date: 2026-10-09 (UTC 13:29 start)
- Lock: created `code/crowd17/next-token/locks/ant-54-605-noun.lock` on start, deleted on completion (verified).
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
  `data/upstream-ct_R5005.txt`, parsed like `code/side-keyhunt/repair_parse.py`;
  1,847 pairs / 96 types re-derived in-session). `canonical.py` never used.
  R5005 never touched. Sealed gates untouched. Red-team adjudication queue
  untouched. Sibling battery `ant-91-36-noun` (still queued) and follow-up
  `wordbound-39-607` (still queued) untouched.

## Bar (verbatim from battery-queue.json)

"promote iff noun-54 parses both qui frames with zero new assumptions."

Numbered clauses (pre-registered before testing, unmodified after seeing data):

1. C1 — noun-54 licenses the antecedent frame of the first qui (@606) with zero
   new assumptions (beyond the noun-54 naming itself).
2. C2 — noun-54 parses / re-opens the "à qui" frame at @607–608 with zero new
   assumptions (beyond the noun-54 naming itself).

## Method

Byte-exact loci on the repaired stream: @605=54, @606=64, @607=39, @608=64
(row a4_00). All three 54 occurrences in the stream (@333, @605, @908) were
windowed. Relative-clause span @607–@680 was scanned for any cell carrying a
verb-class standing at battery grade. Adopted standings (not re-litigated):
64='qui' promoted; 39="à" allophone tier with a-39 adverse A1 adopted
("neither 'qui a qui' nor 'qui à qui' is French", fenced at this exact
window @606–608); 88='gov' (NOT banked as a finite verb); §7 intact.

## Window-level evidence

### W1 — the three 54 windows (distributional position)

- @333 (row a2_05): `... 50 45(ce) 54 88(gov) 40(e) 03(verb-stem) 64(qui) 31 14 45 64(qui) 96(par) 43(noun) 87(ce)`. 54 sits in `ce 54` (a canonical ce+noun NP
  shape) immediately before a gov/verb lead-in to a qui relative. Noun-like
  position.
- @605 (row a4_00): `... 93(verb) 54 64(qui) 39(à) 64(qui) 02 58(nominal) 47(ce) 77(le*) 87(ce) 83(de) 70(pre) 88(gov) 10`. 54 immediately left of the
  first qui — the canonical antecedent slot.
- @908 (row a5_09): `... 83(de) 54 49 64(qui) 83(de) 59(est*) 37 ...`. 54 two
  cells left of a qui (with unvalued 49 as the immediate antecedent slot) —
  compatible with a nominal head, inconclusive on its own.

Distributional read: 54 never occurs in a verb slot in any of its 3 windows;
all 3 place it in antecedent-ish nominal position before a qui. The noun-class
hypothesis for 54 itself is NOT refuted by the stream. (Recorded, not
promoted — 3 occurrences is a thin base, and the bar is about the frames.)

### W2 — frame 1: "54(noun) qui(@606) ..." and its relative clause

- Antecedent slot: licensed. `54 64` is immediate adjacency; "noun qui" is the
  licensed subject-relative frame. Needs nothing beyond the noun-54 naming.
- Full frame: the relative clause opens at @607. Near span @607–@619 (rest of
  row a4_00): `39 64 02 58(nominal) 47(ce) 77(le*) 87(ce) 83(de) 70(pre) 88(gov)
  10` — NO cell with any verb-class standing at battery grade (88 is 'gov',
  not banked finite; 58 is nominal; the rest are unvalued or non-verbal).
  First verb-class cell after @606 is @620=37 (predicative frame, granted A1),
  14 pairs out on row a4_01. A parse reaching it needs (a) a 14+-pair relative
  clause crossing a row boundary, and (b) the intervening `à qui` opener at
  @607–608 to itself parse as a sub-clause — it does not (W3). Both are new
  assumptions. → full frame does not parse at battery grade.

### W3 — frame 2: the "à qui" test at @607–608

- Geometry, byte-exact: `@605=54 @606=64(qui) @607=39(à) @608=64(qui)`.
- The antecedent of a prepositional relative "à qui" is the nominal
  immediately left of "à" (@607) — that is @606=64=qui. A relative pronoun is
  ungrammatical as the antecedent of a following prepositional relative.
  Naming 54 does not change this: 54 sits two cells left, across a relative
  pronoun — not the licensed antecedent position for "à qui".
- Adopted fence a-39 A1 covers exactly this window: "neither 'qui a qui' nor
  'qui à qui' is French". Not re-litigated (per brief scope).
- The only rescue is a dislocation reading ("54, à qui ...", antecedent of
  @608 = 54 across "qui à"): that is a new assumption (comma/dislocation with
  no boundary evidence at battery grade) AND it conflicts with adopted A1.
- No predicate exists in the plausible @608-clause span @609–@619 either
  (02?, 58-nominal, 47=ce, 77=le*, 87=ce, 83=de, 70=pre, 88=gov, 10?).
- → The @608 test is NOT re-opened by naming 54: every blocker of the W2
  fence in battery-qui-38-608-aqui (antecedent=@606=qui; A1; no predicate) is
  independent of 54's class.

### Adverse (verbatim): "naming 54 unvalued invents a value."

Answered, not ignored: the adverse stands as stated — 54 is unvalued in every
standing and the naming IS an invented value. The bar demanded the invention
pay for itself by parsing both qui frames with zero new assumptions; it does
not (C2 fails structurally). The invention is therefore not licensed at battery
grade. 54 stays unvalued.

## Per-clause results

- C1: PARTIAL — antecedent slot licensed by noun-54 with no further
  assumption; but the full qui frame does not parse (no battery-grade
  predicate in the near clause @607–@619; a parse reaching @620=37 needs new
  assumptions and depends on the fenced @607–608 sub-clause).
- C2: FAIL — window @606–608 forces the claim's re-open mechanism false:
  the "à qui" antecedent slot is @606=qui regardless of 54's class, A1 fences
  "qui à qui", and no predicate follows. Naming 54 changes none of this.

## Verdict: KILL

Not promote: the bar is conjunctive on both frames and C2 fails. Not null:
the failure is structural, not data-thin — no narrower test on 54's class
can change the @606=qui antecedent geometry or lift the adopted A1 fence, so
there is no honest follow-up that re-opens THIS battery. (The @608 question
itself stays live in its own venue: `wordbound-39-607`, still queued at P4,
tests 39's word-boundary at @607 — the mechanism that could genuinely
re-open @608. Untouched by this verdict.)

No standing or red-team verdict contradicted or downgraded (§7 intact; 54
was unvalued and stays unvalued; 67 remains the sole polyvalence;
canonical-stream caveat stands: rows a4_00/a4_01 offsets unvalidated).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-ant-54-605-noun.md`
- Queue: `ant-54-605-noun` → `status: verdict`, `result: kill`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; temp-file + rename;
  JSON re-validated; own entry only; no downgrade)
- Lock created on start, deleted on completion (verified gone).
