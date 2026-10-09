# Battery report: ceci-195-nounslot

- Target id: `ceci-195-nounslot`
- Claim: "re-test the @194-200 clause with 21 fixed nominal"
- Date: 2026-10-09
- Worker: battery worker (subagent f1fea315-a413-4df7-9b2d-8dd444a3e78f)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed per
  `code/side-keyhunt/repair_parse.py`); 1,847 pairs / 96 types re-derived
  in-work. `canonical.py` never used. R5005, sealed gates, red-team
  adjudication queue untouched.

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"resolve iff a full-clause parse of 47-01-21-60-08-67-76 exists with 21 nominal
and <=1 unstated assumption; else fence @195 as a [21]/[60]-driven residual
with stated cause (not a 47-01 residual)"

Numbered pass/fail clauses (fixed before data examination):

1. (C1) A full-clause parse of 47-01-21-60-08-67-76 exists (0-based offsets,
   queue convention: @195 = 01's position) with 21 nominal and ≤1 unstated
   assumption → resolve (PROMOTE).
2. (C2) Else — fence @195 as a [21]- or [60]-driven residual with stated
   cause; the fence is explicitly NOT a 47-01 residual (i.e. not a
   "ceci"-subject failure).

The bar is scoped to the 7-group slice @194–200 (0-based) = "47 01 21 60 08
67 76" (row a2_00). It overlaps but does not duplicate the completed
`slot-60-at-197` battery (whose bar was a three-arm class test over a
wider window): that battery's PROMOTE (2026-10-09) is adopted here as a
premise, not re-litigated. This battery adds the 76-nominal leg to close
the clause fully.

## Method

1. Read `BATTERY-PROTOCOL.md` first. Created
   `code/crowd17/next-token/locks/ceci-195-nounslot.lock` on start; deleted
   on completion.
2. Re-derived the repaired stream byte-exact in-session (1,847 pairs / 96
   types; asserts held).
3. Extracted the slice (0-based @194–200, byte-exact, row a2_00, mid-row):
   `47 01 21 60 08 67 76`.
4. Adopted standing premises (§7) plus battery-verdict premises listed
   below; counted every class/value not covered by a verdict as an unstated
   assumption.

## Standing premises (adopted, not re-litigated)

- 47='ce' granted (A4 allophone tier).
- 21 noun-class PROMOTED (de-frame-21-class, battery grade 2026-10-08).
- 76 noun-class PROMOTED (noun-76, battery grade 2026-10-08).
- 60 verbal class forced: verb-60's V1 ('qui 60 08' @1338), V2 ('ne 60 12'
  @700), V4 ('53 60 06' @1474) adopt as the verb+complement frame;
  `slot-60-at-197` PROMOTE (battery grade 2026-10-09) added the @197
  window as a 7th bare-verb window with 21 nominal; noun-60 KILLED;
  uniform-adjective 60 KILLED (adj-60).
- 67 positional rule (§7): 67='veut' iff follower infinitive-shaped; the
  follower here (@200=76) is nominal → 67='et'.
- 01's class is open; no det/adj-01 verdict and no det/adj-01 kill exist.
- 08's class/value open (stem-08 NULL, 2026-10-09); 08 is not verb-shaped.

## Window-level evidence (0-based, byte-exact)

Slice: `194=47 195=01 196=21 197=60 198=08 199=67 200=76` (row a2_00).

- "21 60" bigram: exactly 4× stream-wide (@118, @171, @196, @231); @196 is
  this window.
- "60 08" bigram: exactly **2×** stream-wide — @197 and @1338. The
  geometry at @197 is byte-identical to verb-60's V1 frame ('qui 60 08'),
  i.e. the verb+08 frame verb-60 itself flagged at the @197 twin.
- Context ±8: `24 87 98 56 | 47 01 21 60 08 67 76 | 87 11 92 63 42 06 77 44`.

### The parse (C1 candidate)

"ce(47) [01-det/adj] [21-N-subject] [60-V] [08-complement] et(67) [76-N]"

- Subject NP "ce [01] [21]": 47='ce' granted; 21 nominal (promoted class);
  01 must be determiner/adjective class to complete the NP — **the single
  unstated assumption** (1 of ≤1 allowed). No standing verdict kills it
  (01's class is genuinely open; no det/adj-01 kill exists anywhere).
- 60-V: finite verb slot with subject present; geometry byte-identical to
  verb-60's V1 'qui 60 08' frame ('[21-N] 60 08' here). Battery-promoted
  verb class (slot-60-at-197's 7th window) — not an assumption.
- 08: licensed complement slot by the verb+08 frame; 08's class left OPEN
  (fenced, not assumed).
- "et [76]": 67='et' via the standing positional rule (76 nominal, not
  infinitive-shaped); 76 nominal promoted. The conjoined NP completes the
  clause.
- Zero kill-grade contradictions: "ce [01] [21] [60-V]" needs no
  archaism (the subject is an NP headed by 21, not bare "ce" before a
  lexical verb — the TLFi archaism leg does not bite); no word-order
  violation; no invented clause boundary (mid-row slice).

Assumption count: **1** (01 = determiner/adjective). Within the bar's gate.

### Since-then check (nothing post-dating slot-60-at-197 breaks the parse)

- `01-verbclass-probe` NULL (2026-10-09): 01 shows verb-ness at @1256
  (re-opening avenue A), but the det/adj-01 assumption is neither forced
  nor killed by it; the §7 tension (01 cannot be both nominal and verbal)
  is red-team venue. No downgrade.
- `infsub-80-frame`, `ne-08-verb-slot`, `imp-80-bare-1156-1596`
  (all 2026-10-09): no contact with this slice.
- `participle-60-newvalue` KILL (2026-10-09): closes the PP avenue for 60;
  consistent with the verb-slot parse adopted here.
- `framecensus-60-redteam-pack` PROMOTE (2026-10-09): lists @197 among the
  verbal-arm windows — corroborates, not contradicts.

## Per-clause pass/fail

- **C1: PASS.** A full-clause parse of 47-01-21-60-08-67-76 exists with 21
  nominal and exactly 1 unstated assumption (01 = determiner/adjective).
- **C2: MOOT.** The resolve arm fired; no residual to fence. (For the
  record: the fence would have been a [21]-driven residual if 01 could not
  complete the subject NP, or a [60]-driven residual if the verb slot
  collapsed — neither obtains.)

## Verdict: PROMOTE

The @194–200 clause resolves as "ce [01] [21-N] [60-V] [08] et [76-N]"
with 1 unstated assumption. This CONFIRMS (adopts, does not duplicate)
`slot-60-at-197`'s battery PROMOTE and adds the 76-nominal leg for a
closed clause. Battery grade; needs red-team ratification like every
promote.

## Adverses answered

- "60's slot gated on verb-60 / poly-60-redteam": honored — verb-60's
  frame and slot-60-at-197's promote adopted as premises;
  poly-60-redteam stays queued and untouched; no polyvalence declared
  (§7 intact).
- "08 open (stem-08)": 08 fenced as an open complement slot; no value
  assumed. stem-08's NULL (2026-10-09) confirmed in-work.
- "67 positional needs 76's shape": 76 nominal-class promoted (noun-76,
  2026-10-08); follower not infinitive-shaped → 67='et' via the standing
  positional rule.

## Caveats

1. Row a2_00's upstream offset is one of the 68 unvalidated offsets
   (canonicality caveat): under a rival row phase this window could
   re-segment, dissolving the result. Canonical-stream verdict per
   protocol.
2. The single assumption (01 = determiner/adjective) is a hapax slot
   (@195 is 01's only det-01-noun-shaped window among n(01)=28) with no
   distributional support; it is unstated but uncontradicted.
3. 60's VALUE stays unnamed (slot verdict, not value verdict).

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-ceci-195-nounslot.md (this
  file).
- Queue: `ceci-195-nounslot` queued → verdict/promote via temp-file +
  rename, own entry only; pre-write assert confirmed no prior verdict;
  JSON re-validated post-write.
- Lock `locks/ceci-195-nounslot.lock`: created on start, deleted on
  completion.
- `canonical.py` never used; R5005, sealed gates, red-team adjudication
  queue untouched; no standing or red-team verdict contradicted or
  downgraded; §7 intact.
