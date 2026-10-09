# Battery report: verb-gap-ne-508 (@505-525 downstream verb hunt)

Worker: afb49eb9-7a1c-4ff9-958a-bff954eca6b8. Date: 2026-10-08.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
canonical.py never used. R5005 never touched.
Anchor convention: @-indices are 0-based pair indices in the repaired stream.
Lock: code/crowd17/next-token/locks/verb-gap-ne-508.lock (created
2026-10-09T01:51:10Z, deleted on completion).

## Bar (verbatim, pre-registered)

"state the full parse with the verb named and every pair @505-520 assigned;
else confirm the verb gap as a second window residual"

Numbered clauses (stated BEFORE testing, unchanged after data):

1. State the full parse with the verb named and every pair @505-520 assigned:
   a downstream finite verb in @510-525 completes the 'ne' clause at @508-509,
   keeping 64='qui', with every pair @505-520 assigned a value or class.
2. ELSE confirm the verb gap as a second window residual (null-grade outcome):
   no such verb exists under standing grants, with the grammatical cause stated.

Adverses: none listed.

## Method

Fresh parse of the repaired stream; no prior counts trusted. Re-derived the
@505-525 window byte-exact, re-checked the left-context readings from
battery-lon-94-64-rightedge.md (which cites battery-lon-ne-77-62-94.md:
"et le il ne" dead; "et l'on ne" verb-less), and censused 98 (n=40) for the
'vient' battery-promote's fit at @511. Tested every finite-verb-shaped
candidate in @510-525 against the French preverbal-'ne' adjacency requirement.

## Window-level evidence (@-offsets, repaired stream, row a3_00)

@505='21' (NOUN class), @506='67' ('et': positional rule, follower 77 not
infinitive-shaped), @507='77' ('le' provisional), @508='62' ('il'? /
conditioned-'on'? open), @509='94' ('ne', battery-promoted, unratified),
@510='64' ('qui', granted), @511='98' (open; 'vient' battery-promote pending
red-team), @512='65' (NOUN class, battery-promoted), @513='88'
(governor/verb-class), @514='56' (open), @515='87' ('ce', granted),
@516='77' ('le' provisional), @517='80' (verb-frame, A8), @518='09' (open),
@519='70' ('pre', ground truth), @520='91' (open), @521='77', @522='06',
@523='55', @524='81', @525='97'.

Finite-verb-shaped candidates in @510-525:
- @511='98': 'vient' is battery-promoted (pending red-team ratification); a
  finite verb. 98 n=40; '98-65' occurs x1 stream-wide (this window).
- @513='88': governor/verb-class (class-level, no value).
- @517='80': verb-frame per A8 (class-level, no value).

## Per-clause pass/fail

1. Full parse with the verb named, every pair @505-520 assigned — FAIL.
   The grammatical blocker is absolute, not quantitative: French 'ne' is a
   bound preverbal clitic and must stand immediately before its verb (bare
   'ne' with cesser/oser/pouvoir/savoir, expletive 'ne', 'ne...que',
   'n'importe' — every licensed form has 'ne' directly preverbal; no
   construction separates 'ne' from its verb by an intervening relative
   clause or any other material). @510='qui' is granted and sits directly
   between 'ne' @509 and every downstream verb-shaped candidate (@511
   'vient', @513 88-class, @517 80-frame). Therefore no candidate in @510-525
   can complete the 'ne' clause while keeping 64='qui' — not @511 (blocked
   by @510 itself), not @513/@517 (same intervention, plus class-level only).
   The left-context readings are already exhausted ('et le il ne' dead;
   'et l'on ne' verb-less, per the cited batteries). No assignment of
   @505-520 satisfies the bar's first arm. FAIL.
2. Confirm the verb gap as a second window residual — TAKEN.
   The gap is now doubly fenced: battery-lon-94-64-rightedge.md fenced the
   'ne qui' contact itself (no boundary can intervene @509|@510; no
   window-local cause for 64='qui' to fail), and this battery fences the
   downstream span (no verb in @510-525 can attach to 'ne' @509 under the
   preverbal-adjacency law with 64='qui' granted). The residual localizes to
   the 'ne' reading of 94 at this window, not to any downstream value.

## Verdict

**NULL — verb gap confirmed as a second window residual.** No standing
verdict contradicted or downgraded: 64='qui' grant untouched, 94='ne'
promotion-track not re-litigated, 98='vient' battery-promote not decided here
(@511's relative-clause fit is recorded below as a follow-up, not a claim).
R5005, sealed gates, and the red-team adjudication queue untouched. The
red-team-owned 12/94 duality and conditioned-62='on' questions are not
decided.

## Null follow-ups (per §4 — work regenerates, never ends)

1. `ne-508-reseg` (P2): if 94 at @509 is syllable-final "ne" (word-internal,
   cf. 70-12-94 'prenne' precedent), no 'ne' clause exists and the verb gap
   dissolves. Bar: one coherent word-internal parse of @507-511 with every
   pair's syllable role stated; else fence to the red-team 12/94 duality
   adjudication.
2. `vient-98-511-relative` (P2): test @510-517 as "qui vient [65] [88]..."
   under 98='vient' (battery-promote). 98-65 is a stream singleton (this
   window), so the fit is local. Bar: state whether the relative clause
   parses with ≤1 ungranted assumption; if yes, the right side is clean and
   the residual belongs purely to 'ne'.
3. `verbless-ne-family` (P3): coordinate with ne-follower-verbless-sweep
   (queued) — if a verb-less 'ne' family exists across 94's 37 windows,
   re-frame @508 inside it instead of as an isolated residual.
