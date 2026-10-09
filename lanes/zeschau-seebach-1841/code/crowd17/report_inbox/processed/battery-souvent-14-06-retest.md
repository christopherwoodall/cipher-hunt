# Battery report: souvent-14-06-retest — second "14 06" window @84 under 14="sou"

Worker: 0a626439-617b-4de1-b771-a893447d6996 | 2026-10-09T02:20Z–02:35Z
Target: `souvent-14-06-retest` (priority 2). Lock
`locks/souvent-14-06-retest.lock` created on start, deleted on completion.
No prior/stale lock existed. Sibling targets `prennent-70-12-06` (locked,
running in parallel) and `le-14-kill-1121` (queued) not blocked on and not
duplicated: this report tests only the @84 window and the spelling of the
"souvent" gloss both siblings inherit.

## Bar (verbatim, pre-registered)

"@80-90 parses as '[16] souvent [88]' with 16/88 class-consistent, or
'souvent' is killed at @84 (which would make @1121's parse a coincidence,
not a pattern)"

Numbered clauses (fixed before testing):
- C1: @80–90 parses as "[16] souvent [88]" with 16/88 class-consistent.
  PASS iff the window admits a grammatical French parse under the claimed
  value 14="sou" and standing values, with 16's and 88's classes
  consistent with the parse (distributional or granted evidence cited).
- C2: "souvent" is killed at @84 at kill grade. PASS iff window-level
  evidence at @84 forces the "souvent" gloss false.

## Method

Repaired 1,847-pair stream only: `code/side-keyhunt/repaired_offsets.json`
+ `data/upstream-ct_R5005.txt`, parsed exactly like
`code/side-keyhunt/repair_parse.py` (byte-exact
`[s[i:i+2] for i in range(o, len(s)-1, 2)]`; 1,847 pairs verified).
`canonical.py` never used. R5005 untouched. @-offsets are 0-indexed pair
positions (queue convention). Standing values used: banked 11=la, 82=m,
29=er, 40=e; promoted 06=ent (round-17 red-team), 00=pour; provisional
77=le; battery-level lead 62=il; class grant 88=governor/verb
(registry `["gov","cls"]`, battery-governor-88-value). Every count below
re-derived from the stream, none copied.

## Window evidence (@84, row a1_02, row-relative 14 of 32 — mid-row)

Surface pairs @80–90: `98 51 62 16 | 14 06 | 88 77 66 98 19`
(all row a1_02; no row boundary within the window).

Distributional facts (re-derived):
- "14 06" bigrams stream-wide: exactly 2 — @84 and @1121 (breaker-b4-1121
  confirmed; re-derived identical). n(14)=15 at 72, 84, 117, 141, 178,
  339, 424, 458, 586, 623, 813, 896, 1121, 1365, 1689 — matches the
  breaker census exactly.
- 16 (n=28): predecessors 82("m", banked) x11, 62 x4, 12 x3, 33/42 x2;
  successors 00("pour", promoted) x4, 24/01/91/76 x2, 14 x1 (@83 only).
  "m 16" x11 = clitic-pronoun + verb frame; "62 16" x4 with 62="il"
  (battery lead) = subject + verb; "16 pour" x4 = verb + pour-infinitive
  frame. 16 verb-class: SUPPORTED distributionally. Registry: 16 open
  (no entry) — no granted value contradicts.
- 88 (n=23): class VERB/governor STANDING (registry ["gov","cls"];
  battery-governor-88-value promote, wave-7). The very window under test
  is L4 of that report: @86 "14-06 [88] 77-66" = "[88] le [66]"
  transitive frame. Preposition rival already rejected there (Fisher
  p=0.0113 / p=0.0004); not re-litigated, cited.
- Class-level skeleton of @82–88 under the claim: "[62:il-lead]
  [16:verb] souvent [88:verb] le[77:prov] [66]" — grammatical French
  skeleton ("il [verb] souvent [verb] le [noun]"-shaped), zero ungranted
  assumptions beyond the claimed 14 value. Class-consistency: PASS on
  its own terms.

## The spelling finding (kill-grade)

Under the claim's own value 14="sou" and standing 06="ent"
(round-17 red-team promoted):

14 + 06 = "sou" + "ent" = **"souent"** — not "souvent". There is no
French word "souent"; the "v" is unaccounted for. The lane's
concatenation convention is exact (crib "la premiere" =
la+pre+m+i+er+e; "prennent" = pre+n+ent, both letter-exact). No lane
precedent tolerates a dropped medial consonant, and 06="ent" is
red-team standing, so the gap cannot be repaired on the 06 side.
The exact spelling "souvent" requires 14="souv" ("souv"+"ent"), a
different value from the claim's 14="sou".

Breaker-b4-1121 wrote "[14]-[06] (= sou-ent, 'souvent')" — that equation
is misspelled, and this target's bar inherits it. The defect is
demonstrated AT this window (@84 yields "[16] souent [88]", a
non-word where the bar requires "souvent"), and it applies identically
at @1121: both "14 06" windows fail to spell "souvent" under 14="sou".

## Per-clause pass/fail

- C1 (@80–90 parses as "[16] souvent [88]", 16/88 class-consistent):
  FAIL AT KILL GRADE. Class-consistency passes on its own (16
  verb-class supported distributionally; 88 verb/governor class
  standing; skeleton grammatical), but the required parse as
  "souvent" is impossible under the claimed value: the window spells
  "[16] souent [88]", and "souent" is not French. A bar clause fails
  at kill grade when the window forces the claim false — it does.
- C2 ("souvent" killed at @84): PASS. The "souvent" gloss is killed at
  this window by the spelling gap: 14="sou" + 06="ent" (standing)
  cannot yield "souvent". Note the killer is global to the value
  claim, not window-local: it bears equally on @1121, so it does not
  make @1121 "a coincidence" — it invalidates the shared gloss at
  both windows.

Adverses: none stated in the queue entry. Standing constraints
respected: 06="ent" upheld (not weakened); 88's gov-class used, not
contradicted; no red-team verdict touched; breaker-b4-1121's NULL
verdict not downgraded (nulls are inconclusive by definition; this
report refines its reasoning, it does not alter its recorded
verdict). R5005, sealed gates, red-team queue untouched. No
promotion beyond a battery verdict is claimed or implied.

## Verdict: KILL

C1 fails at kill grade (window forces the claim false: "souent" is not
"souvent" under the claimed value and standing 06="ent"); C2 passes.
The "souvent" gloss for "14 06" under 14="sou" is dead at @84 — and,
by the same spelling evidence, at @1121. The class-consistency half
of the bar survives (16 verb-class, 88 verb/governor-class both
supported/standing), so the "[14]ent"-adverb frame is not ruled out as
a shape — only the "sou" spelling of it.

## Recommended downstream (for supervisor disposition, not mandated)

1. `souv-14-06-repair` (P2/P3): re-test both "14 06" windows under the
   spelling-repaired value 14="souv": bar — "@80–90 and @1116–1127
   parse as '[16] souvent [88]' / 'prennent souvent la' with exact
   spelling and 16/88 class-consistent; kill iff 'souv' is
   distributionally untenable as a group value elsewhere."
2. Note for `prennent-70-12-06` (running): its "prennent souvent"
   combined read inherits the same v-gap — "prennent" spelling is
   exact and unaffected, but the joint gloss needs "souv", not "sou".
3. Note for `le-14-kill-1121` (queued): unaffected — 14="le" is a
   word-level rival, independent of the "sou"/"souv" spelling question.
