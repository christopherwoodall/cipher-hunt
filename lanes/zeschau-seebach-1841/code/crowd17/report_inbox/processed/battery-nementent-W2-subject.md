# Battery report: nementent-W2-subject

Target: `nementent-W2-subject`. Claim (queue): W2's "ne mentent" (@1183) likewise
lacks a 3pl subject ("le ver[78]" singular; right context "est [42]").
Date: 2026-10-09. Worker: d7b830d0-a0ef-474f-90db-a5700eedb0f0 (battery worker).
Lock `locks/nementent-W2-subject.lock` created 2026-10-09T12:45:56Z (no stale
lock); deleted on completion.
Parent: `w1-573-subject` NULL (follow-up #3, this target), processed report
`code/crowd17/report_inbox/processed/battery-w1-573-subject.md` — adopted as
premise, not re-litigated.

Offset convention: @n below = 0-based pair index in the repaired 1,847-pair
stream unless marked 1-based (lane reports use 1-based: +1).

## Bar (verbatim, pre-registered)

"decide whether both windows share one subject account or the frame needs
re-segmentation; feed the red-team 94-duality adjudication"

## Bar restated (numbered pass/fail clauses; frozen before testing)

- C1: DECIDE — state whether both "ne mentent" windows share ONE subject
  account (name it) OR the frame needs re-segmentation (state the alternative
  segmentation and what it resolves), with stated cause at battery grade.
- C2: PACKAGE — deliver the evidence package feeding the red-team 94-duality
  adjudication: evidence only, no adjudication, no §7 violation (no class,
  split, value, or polyvalence declared by this battery).

## Method

Read BATTERY-PROTOCOL.md first. Re-derived the repaired 1,847-pair stream
independently from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json` (parsed per
`code/side-keyhunt/repair_parse.py`; verified 1,847 pairs / 96 types).
`canonical.py` never used. R5005, sealed gates, red-team adjudication queue
untouched. Every number traces to the stream.

Standing values used (protocol §7 + R19, adopted as premises):
- Pencil GT: 11=la, 82=m, 29=er, 40=e, 46=que.
- Granted/promoted: 87=ce, 47="ce" (A4), 59="est" (provisional), 77="le"
  (provisional), 84="on", 00="pour", 30="pas", 79="tout", 83=["de","lead"]
  (conditioned), 06="ent" (R17-007 conditional promote), 76=["noun","prom"],
  65/69=["noun","cls"] (R19), 58=["nominal","cls"] (R19), 43=["noun","cls"]
  (R19-045), 24=R24 (finite/modal here — follower is 82/07, not 85), 33 INF.
- Leads: 78="ver" (R16-005, value open — red-team venue), 94="ne" STRONG LEAD
  (R17-001/R16-006).
- Binding red-team law: **R19-167** (94 split REJECTED/CLOSED: 94's value is
  the single syllabic spelling "ne"; word-final "-ne" is a SEGMENTATION
  distinction, not a second value; 67 et/veut remains the SOLE true
  polyvalence) and **R19-168** (dual94 scope: no split declared; per-window
  segmentation findings only). The duality map's PARTICLE-STRAINED
  classification of both "ne mentent" windows (from
  battery-ne-particle-ungrammatical-sweep, adopted by the parent) is adopted
  as premise, not re-litigated.

## Window-level evidence (re-derived in-session)

"94 82 06 06" census: exactly **x2** stream-wide — 0-based @578 (row a3_02,
parent's W1) and 0-based @1182 (row a6_10, this target's W2). Byte-exact.

W1 — 0b@566–590 (row a3_02):
`97 13 76 45 94 52 | 87 78 45 13 55 61 | 94 82 06 06 | 50 10 19 18 14 00 97 41`
= "…[13] [76=noun] [45] ne(94) [52] | ce(87) verdict(78-45, LEAD) [13-55-61]
| ne(94) mentent(82-06-06) | [50] [10] [19] [18] [14] pour(00) [97] [41]…"

W2 — 0b@1170–1204 (row a6_10):
`87 83 21 85 36 74 | 32 48 59 37 77 78 | 94 82 06 06 | 59 42 06 84 59 46 07 24`
= "…ce(87) [83='de',lead] [21=noun] [85] [36] [74] | [32] [48='e'] est(59,prov)
[37,frame] le(77,prov) ver[78](LEAD) | ne(94) mentent(82-06-06) | est(59,prov)
[42] [06] on(84) est(59) que(46) [07] [24=R24 modal/finite]…"

### W2 subject census (no licensed 3pl subject)

Left clause: "ce [de] [21] [85] [36] [74]" — determiner ce (singular) + de +
noun; no plural. Then "[32] [48] est [37] le ver[78]" — closed copular clause
(predicative 37 frame): subject "le ver[78]" = singular ("le" strictly
singular in every period; 77='le' provisional). 32 unvalued, 48='e' letter.
**No 3pl NP.** Right clause: "est [42] [06] on est que [07] [24]" — "est [42]"
is predicative (42 unvalued, A1 frame); 84='on' is a subject pronoun but
appears only after two more "est" clauses and governs none of them as a 3pl
subject of "mentent". **No 3pl subject of "ne mentent" anywhere in either
clause.** The parent's claim ("le ver[78]" singular; right context "est
[42]") re-verified byte-exact.

### Cross-window comparison

| Feature | W1 (0b@578) | W2 (0b@1182) |
|---|---|---|
| Frame | "94 82 06 06" | "94 82 06 06" (byte-identical) |
| Preverbal left | "ce verdict [13-55-61]" — X unnameable (name-13-55-61 NULL) | "le ver[78]" — singular, closed copular clause |
| Right | "…[50] [10] [19]…" — 50 unvalued; inversion fenced by parent | "est [42] [06] on…" — predicative; no 3pl |
| Overt 3pl subject | none licensed | none licensed |

### Re-segmentation test

Candidate re-segmentations of "94 82 06 06" that would remove the 3pl-subject
requirement:
1. "ne m'ent-ent" (pronoun + doubled "ent"): "m'ent" is not a French word;
   freestanding "ent" is not a word; no battery-grade license anywhere.
2. Any reading that voids the finite-verb "mentent" reading contradicts the
   standing grants 06="ent" (R17-007 conditional promote, red-team),
   82='m' (pencil), 94="ne" (STRONG LEAD, single value per R19-167) —
   red-team venue, not a battery act.
3. The duality map already classified both windows PARTICLE-STRAINED; adopted
   as premise. Strain ≠ license for re-segmentation.

No licensed re-segmentation resolves the subject gap at battery grade.

## Per-clause pass/fail

- **C1 PASS — ONE SUBJECT ACCOUNT.** Both windows share the same structural
  configuration: [singular nominal clause] + "ne mentent" (finite 3pl, under
  the standing R17-007 conditional grant) + [no 3pl NP anywhere in the clause].
  The gap is systematic — a property of the x2 "94 82 06 06" frame, not a
  per-window accident. W1's preverbal slot X=[13-55-61] is unnameable;
  W2's is the named-singular "le ver[78]"; neither yields a licensed 3pl
  subject. Re-segmentation fails (no licensed alternative under standing
  grants; voiding the finite reading is red-team venue).
- **C2 PASS — package delivered.** Evidence for the red-team 94-duality
  adjudication: (a) both "ne mentent" windows are particle-STRAINED and
  subjectless under the standing "ne mentent" segmentation; (b) the R17-007
  conditional "ne mentent" grant therefore rests on two clauses with no overt
  3pl subject. **Disposition note:** R19-167 has CLOSED the 94 split (94 =
  single "ne"; 67 sole polyvalence) and R19-168 ruled the scope package —
  this evidence enters the closed record as consistent support; **no new
  red-team act is requested** by this package.

## Adverse

"§7 sole-polyvalence — battery gathers only" — HONORED. No class, split,
value, or polyvalence declared; no re-litigation of R19-167/168; the 94
duality question is treated as closed at red-team level.

## Verdict

**PROMOTE** (red-team input package delivered; evidence only, no
adjudication). C1 decides the one-account question; C2 delivers the package
with the R19-closure disposition. No standing/red-team verdict contradicted
or downgraded (R17-001, R17-007, R19-167, R19-168, A1, A4, A8, A11 all
adopted); §7 intact; canonical-stream caveat stands (rows a3_02/a6_10
offsets unvalidated). Per §4, promotes propose no follow-ups; the natural
re-open conditions are red-team venue only (78's value naming per R16-005 /
R20 open call; 42's class; a red-team re-opening of the 94 split).

## Bookkeeping

- Report: this file.
- `battery-queue.json`: `nementent-W2-subject` queued → verdict/promote via
  temp-file + rename (pre-write assert confirmed queued/verdictless; JSON
  re-validated post-write). Own entry only; no downgrade.
- Lock created on start (agent id + UTC), deleted on completion.
- `canonical.py` never used. R5005, sealed gates, red-team adjudication queue
  untouched.
