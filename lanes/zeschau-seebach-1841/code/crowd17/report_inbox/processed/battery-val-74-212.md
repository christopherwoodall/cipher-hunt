# Battery report: val-74-212

- Target id: `val-74-212`
- Claim: "Name 74's class at @212."
- Date: 2026-10-09
- Worker: battery worker (subagent 1871aa0a-5a7c-4ca9-9c39-08f07e6761ed)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed per
  `code/side-keyhunt/repair_parse.py`; asserted in-session: 1,847 pairs, 96
  types). `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Lock: `code/crowd17/next-token/locks/val-74-212.lock` created 2026-10-09T19:07:27Z
  (no prior/stale lock); deleted on completion.
- Parent: follow-up #3 of NULL `ver78-rerun-214-1543` (2026-10-09), which fenced
  @214 because promoted 06='ent' (bound verb ending) has no licensed host
  ("verent"/"entest" non-French). This target tests whether a verb-shaped 74
  revives @214's NP-integration arm independent of the 'ent' continuation.

Terms (ASD-STE100): "verb-shaped" = 74 takes the grammatical role of a finite
verb in the window. "Subject-NP" = the noun phrase "le ver" (77="le"
provisional + 78="ver" LEAD) functioning as the SUBJECT of the finite verb.
"Postverbal subject" = a subject that follows its verb ("vient le jour"),
licensed in French only for specific verb classes/contexts. "Fence" = set the
question aside with a stated reason, not kill it.

## Bar (verbatim, pre-registered before testing)

"Verb-shaped 74 licenses '[74-fin] le ver...' as a subject-NP left clause, else fence the left edge."

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** 74 is verb-shaped (finite) at @212.
2. **C2:** The reading "[74-fin] le ver..." parses with "le ver" as the subject
   NP of finite 74 — a licensed subject-NP left clause in 1841 French.
3. **C3 (else-arm):** if C1 or C2 fails, fence the @212 left edge with stated cause.

Adverses listed: none.

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock on start; deleted on completion.
2. Re-derived the repaired stream byte-exact in-session. All @-offsets below are
   0-based repaired-stream pair indices.
3. Ran a window-complete census of all 34 of 74's windows (predecessors,
   successors, ±3 context) and tested each class arm (verb finite, noun,
   adjective, adverb, letter-tier) at @212 by local elimination.
4. Tested the bar's subject-NP reading against 1841 French grammar, with a
   period-corpus check of the postverbal-subject shape
   (`code/side-period/corpus`).
5. Adopted, never re-litigated: 77="le" provisional, 78="ver" LEAD, 06="ent"
   promoted (bound verb ending), 94="ne" STRONG LEAD, 84="on" (A15 granted),
   87="ce" granted, 46="que" banked; chain-follower-class KILL (2026-10-09)
   fencing single-word "49 74 74"; §7 (67 "et/veut" sole polyvalence).

## Window-level evidence

### The @212 locus (row a2_00)

`@210=88 | @211=19 | @212=74 | @213=77 | @214=78 | @215=06 | @216=59 | @217=46 | @218=29`

Span: "…[88] [19] [74] le(77) ver(78) ent(06) [59] que(46) er(29)…"

### 74's stream-wide census (n=34, byte-exact)

Offsets: 142, 212, 261, 350, 417, 418, 477, 635, 693, 786, 801, 816, 817,
861, 862, 874, 919, 920, 1053, 1054, 1071, 1103, 1175, 1307, 1314, 1414,
1500, 1568, 1635, 1637, 1638, 1677, 1780, 1845.

**Verb-forcing frames (4 independent legs):**
- "ne [74]" ×3 — @350 ("94 [74] 67 78"), @786 ("94 [74] 65 84"),
  @1103 ("94 [74] 47 78"). 94="ne" is STRONG LEAD; "ne" is a preverbal
  negator clitic that must immediately precede a finite verb (only object /
  reflexive clitics may intervene; the bigrams are adjacent, so none do).
  74-as-clitic fails (@786's follower 65 is noun-class — "ne [clitic]
  [noun]" is ungrammatical). → 74 forced finite-verb-shaped in 3 windows.
- "on [74]" ×1 — @261 ("84 [74] 45 93"). 84="on" (A15 granted) is a subject
  pronoun; it must be followed by a finite verb. → 74 forced finite-verb-shaped.

**Noun-forcing frames (2 legs):**
- "ce [74]" ×1 — @1637 ("01 [74] 87 [74]"): 87="ce" GRANTED determiner
  directly before 74 → 74 noun-shaped (battery grade).
- "le [74]" ×1 — @1307 ("77 [74] 52"): 77="le" provisional determiner
  directly before 74 → 74 noun-shaped (provisional grade).

74 is split-shaped stream-wide (verb in ne/on frames, noun after
determiners) — cf. 88/52/97/09. Declaring the split is red-team venue
under §7; this battery names only the @212 class.

**Chain note:** 74 follows itself 6× (@417–418, @816–817, @861–862,
@919–920, @1053–1054, @1635–1638) and follows 49 five times. The
single-word "49 74 74" reading is fenced (chain-follower-class KILL,
2026-10-09, heterogeneous government); it does not touch @212, whose
predecessor is 19.

### C1 test — 74's class at @212 by local elimination

Frame: "19 [74] le(77) ver(78)". 19's class is open (n=19 is 9; no
determiner/verb frame forces it), 77="le" provisional, 78="ver" LEAD.

- **Noun arm:** "[74-N] le ver" — bare noun followed by a full determined NP.
  Ungrammatical (no apposition license for two bare/determined nouns; no
  coordination). FAIL.
- **Adjective arm:** "[74-adj] le ver" — adjective with no head noun before a
  full NP. Ungrammatical. FAIL.
- **Adverb arm:** "[74-adv] le ver" — sentence adverb before a bare NP (not a
  clause). Ungrammatical. FAIL.
- **Letter-tier arm:** no "[74]le"/"[19][74]" word evidence; "74 77" is 2×
  (@212, @1677) with no compositional license. No positive evidence. FAIL.
- **Verb arm:** "[74-fin] le ver" — finite verb + direct-object NP ("le ver").
  Fully grammatical (e.g. "voit le ver", "trouve le ver"). PASS — the sole
  surviving arm.

**C1 — PASS.** 74 is verb-shaped (finite) at @212: forced by local
elimination, with 4 independent stream-wide verb legs ("ne [74]" ×3,
"on [74]" ×1) showing the finite reading is independently licensed.

### C2 test — "[74-fin] le ver..." as subject-NP left clause

The bar requires "le ver" as the SUBJECT NP of finite 74, i.e. a
postverbal subject in "[74] le ver" order.

1841-French grammar: postverbal subjects in declarative clauses are
licensed only for unaccusative/presentational verbs or in specific
licensing contexts (fronted adverbials, etc.). A general transitive verb
in "[V] le [N]" order reads unambiguously as verb + DIRECT OBJECT.

Period-corpus check (`code/side-period/corpus`, French files): the shape
"[unaccusative-V] le [N]" is genuine — 279 hits ("vient le pasteur",
"naît le monde", "entre le directeur", "reste le ...", "arrive le ...",
"tombe le ...", "paraît le ..."). Every hit is an unaccusative/
presentational verb. Zero hits with a plain transitive verb taking a
postverbal subject.

Applied to @212:
- 74's VALUE is open (this battery names class only) → 74's membership in
  the unaccusative subclass cannot be verified. The subject-NP reading is
  conditional on an unvalued verb. Not battery grade.
- The left context (@210=88 "gov"-class, @211=19 open) supplies no
  verifiable licensing context (no adverbial, no interrogative frame).
- The unconditionally grammatical parse ("[74-fin] le ver" = finite verb +
  direct object) does NOT satisfy the bar as written — "le ver" is the
  object, not a subject-NP — and it leaves 06='ent' stranded, so it does
  not move the parent's @214 deadlock either way.

**C2 — FAIL.** The bar's subject-NP licensing is not demonstrated at
battery grade: the reading is a real French shape but lexically restricted,
and the restriction cannot be checked with 74's value open.

### C3 — else-arm

**C3 — FIRES.** Fence the @212 left edge.

Stated cause: 74 is verb-shaped (finite) at @212 at battery grade (C1 —
sole grammatical arm locally; 4 independent verb legs stream-wide), but
the specific "[74-fin] le ver" subject-NP parse the bar requires needs a
postverbal-subject license (unaccusative verb value or licensing context)
that is unestablished (74's value open; 88/19 open). The grammatical
verb+object parse is out-of-bar and does not integrate 06='ent', so
@214's deadlock is unmoved: 'ent' still has no host ("verent"/"entest"
non-French, 74 not adjacent to 06). The left edge stays fenced pending
74's value (unaccusative test) or red-team §7 split adjudication for 74
(verb in ne/on frames vs noun after determiners).

## Per-clause pass/fail

1. **C1 — PASS.** 74 verb-shaped (finite) at @212.
2. **C2 — FAIL.** Subject-NP licensing of "le ver" not demonstrated at
   battery grade (conditional on open verb value / open left context).
3. **C3 — FIRES.** Fence executed with stated cause above.

## Verdict: NULL (fence executed)

No red-team contradiction: 94="ne" STRONG LEAD adopted (not re-litigated);
84="on" A15 adopted; 87="ce" grant adopted; 77="le" provisional untouched;
78="ver" LEAD untouched; 06="ent" promote adopted (the @214 fence stands);
chain-follower-class KILL adopted. No existing verdict downgraded. §7
intact — no split declared (74's split shape recorded, not adjudicated).
Canonical-stream caveat stands (row a2_00 offset unvalidated).

## Scope

- Names 74's CLASS at @212 only (verb/finite, battery grade). 74's VALUE
  stays open; 74's class elsewhere stays open (split-shaped: verb in
  "ne [74]"×3 + "on [74]"×1; noun in "ce [74]" + "le [74]").
- Does not resolve @214's 'ent' deadlock (recorded as unmoved).
- Does not touch `val-74-letter` (queued), `tail-74-78-frame` (queued),
  `det-74-141-rerun` (queued), `homophone-74-76` (queued).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `val-74-unaccusative` (P3) — name 74's value with ≥2 independent legs;
   if 74 names an unaccusative/presentational verb (venir/arriver/rester/
   entrer/sortir/naître/tomber/paraître...), the "[74-fin] le ver"
   subject-NP reading at @212 revives and this fence lifts. Bar: value
   named with ≥2 legs AND attested in the unaccusative inventory; else
   fence the subject-NP arm permanently.
2. `split-74-redteam-input` (P2, gather-only) — package 74's split shape
   (verb forced: "ne [74]" @350/@786/@1103, "on [74]" @261; noun forced:
   "ce [74]" @1637 with granted 87, "le [74]" @1307 with provisional 77)
   as red-team input for §7 split adjudication. No battery-level split
   declaration.
3. `leftedge-212-88-19` (P4) — class the @210–211 left context (88
   "gov"-class, 19 open); a licensed adverbial/presentational context
   would license the postverbal subject independent of 74's value. Bar:
   name the licensing frame with a period-corpus leg, or fence.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-74-212.md` (this file).
- Queue: `val-74-212` queued → `verdict`/`null`, 2026-10-09 (pre-write
  assert passed — was queued/verdictless; temp-file + rename; JSON
  re-validated; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/val-74-212.lock` created on start,
  deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
