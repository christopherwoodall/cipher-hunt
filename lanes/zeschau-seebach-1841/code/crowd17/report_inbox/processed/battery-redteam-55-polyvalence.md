# Red-team evidence package: the §7 venue question for 55

Target id: `redteam-55-polyvalence`.
Claim: GATHER-ONLY evidence package for the §7 venue question: whether 55 needs a second polyvalence ('prend'-stem @1205 vs 're'-prefix in the 55-81 windows), a positional segmentation rule, or one class covering all 12 windows. Battery may gather; only the red team decides.
Date: 2026-10-09. Worker: battery subagent 9ade6696-2a0c-407e-9984-72731b7b3c97.
Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`;
1,847 pairs / 96 types asserted in-session). `canonical.py` never used. R5005,
sealed gates, red-team adjudication queue untouched.
Offset convention: @n = 0-based pair index in the repaired stream.
Lock: `code/crowd17/next-token/locks/redteam-55-polyvalence.lock` created
2026-10-09T17:58:02Z (no pre-existing lock); deleted on completion.

## Bar (verbatim from battery-queue.json)

"Gather-only evidence: this report plus battery-re81-W2-noun-discrim and
battery-re81-W4-02-class when they return; battery may gather, only the"

## Numbered clauses (pre-registered before testing)

1. Re-derive 55's 12-window census byte-exact on the repaired stream
   (positions, followers, predecessors, successor-family contact checks).
2. Record the evidence for resolution option (A): second polyvalence —
   55="prend"-stem at @1205 (55-61) vs 55="re"-prefix at the 55-81 ×6
   windows, with the letter-level tension each implies.
3. Record the evidence for resolution option (B): positional segmentation
   rule — 55 word-internal iff followed by 61, separate word elsewhere.
4. Record the evidence for resolution option (C): one class covering all
   12 windows (uniform verb-class 55), with the windows that block it.
5. Record the status of the two companion discriminators
   (`re81-W2-noun-discrim`, `re81-W4-02-class`) and state explicitly what
   evidence is still missing from this package.
6. No adjudication: no polyvalence declared, no class named, no value
   promoted or killed in this package.

## Method

Read BATTERY-PROTOCOL.md first; created the lock on start. Re-derived the
repaired stream in-session with the row-based parse (per repair_parse.py);
every count below was re-derived from the stream, not trusted from prior
reports. Prior reports were read (not re-litigated, not downgraded); their
verdicts are recorded with dates. Standing values used only per protocol §7.
The R20 red-team report (`processed/next-token-redteam-r20.md`) was checked
for 55-related rulings: R20-034 re-derived n(55)=12 and '55 81' ×6 exact;
55=verb battery-grade (R19-077) stands; R20-045 grants 81 nominal at @524
(window-level). No §7 polyvalence ruling for 55 exists — the question is
still open red-team venue.

## Window-level evidence (clause 1: PASS — census re-derived byte-exact)

55 n=12. Positions (0-based): 25, 523, 550, 576, 906, 1085, 1094, 1167, 1205,
1285, 1611, 1671.
- Followers: 81 ×6, 61 ×3, 83 ×2, 68 ×1. (All four follower families sum to
  12; no other successor exists.)
- Predecessors (11 distinct): 13 ×2, 33, 06, 46, 18, 02, 07, 43, 98, 08, 78.
- Contact check: 61→81 ×0 and 81→61 ×0 stream-wide (zero contact either
  direction between the two successor families). 55's two families never
  touch.
- The 6-gram `78-45-13-55-61-94` occurs exactly ×2 (@576 row a3_02, @1167
  row a6_09) with identical left 4-gram `78-45-13-55`; only 94's follower
  differs (82 @576 vs 87 @1167).
- The three 55-61 windows: @576 (`87 78 45 13 | 55 61 | 94 82 06 06`),
  @1167 (`67 78 45 13 | 55 61 | 94 87 83 21`), @1205 (`16 64 29 45 58 47 43
  | 55 61 | 21 65 64 59 32 48`). Predecessors 13, 13, 43; successors 94,
  94, 21. Two carry 94, one does not.

## Option (A): second polyvalence — evidence (clause 2)

The letter-level tension: at @1205, 55 must contribute to the bare finite
stem "prend" (battery-seg-55-61-21-stem PROMOTE, 2026-10-09): the 7-gram
`58 47 43 55 61 21 65` parses as "[58] ce(47) [43] prend(55-61) [21].
[65] qui(64) est(59) [32]e(48) par(96) [36]" — "this [43] takes [21]. [65],
which is [32]ed by [36]." Indicative, not subjunctive (no trigger), so
"prend" not "prenne"; the missing 94 is the expected finite form, not a
hole. The "prend" reading wants 55="pre"/"pr" + 61="nd"/"end" at letter
level.

At W2 @523, the noun stems *repas*, *regard*, *retour* (all masculine)
survive cleanly under the standing nominal-"55 81" parse
(battery-re81-stem-elim NULL, 2026-10-09): "55 81" occupies the subject
slot, 81 nominal at @524 (nom-97-526-adverb PROMOTE; R20-045 window-level
grant). The "re"-prefix reading wants 55="re" + 81="pas"/"gard"/"tour" at
letter level.

The two letter values cannot both hold for the same cell in the same
position under §7's sole-polyvalence rule (67 et/veut is the only declared
polyvalence; protocol §7). This is the polyvalence-shaped observation:
55="prend"-stem (55-61 windows) vs 55="re"-prefix (55-81 windows).

Discriminating evidence already returned:
- At W1 @25, W3 @550, W5 @1094, W6 @1671, all "re"-stems are DEAD
  (re81-stem-elim, stated causes: fenced left edges, ungrammatical right
  edges, gender clash). Only W2 @523 keeps the "re" arm alive.
- At @576/@1167, the word-unit lead (55-61-94 = "prenne"-family) stays
  compatible-but-undemonstrated (battery-seg-55-61-94-word NULL, 2026-10-09);
  the "reprenne" letter segmentation (55="re"+61="pren"+94="ne") is tensed
  against the "prend" segmentation — the unit survives, its internal
  letters do not (flagged by seg-55-61-21-stem itself).
- Rival "re" legs killed: battery-re61-son-test KILL ("re-son-ne-ment"),
  battery-re83-gar-test KILL (83="gar"). 81="prin" kill (§7) intact.

## Option (B): positional segmentation rule — evidence (clause 3)

The distributional fact: 55 is word-internal at exactly the three 55-61
windows and separate-word-shaped at the other nine. A positional rule —
"55 word-internal iff followed by 61" — covers all 12 windows with zero
exceptions:
- Followed by 61 (×3): word-internal. @1205 decided "prend" (bare stem);
  @576/@1167 the 55-61-94 word unit ("prenne"-family, undemonstrated but
  live). The 61↔81 zero-contact count (both directions ×0 stream-wide)
  means the rule's two regimes never bleed into each other.
- Followed by 81 (×6): separate-word-shaped. W2 @523 nominal "repas/
  regard/retour" (re81-stem-elim); W1/W3/W5/W6 fenced with stated causes.
- Followed by 83 (×2, @906/@1611) and 68 (×1, @1285): separate-word-shaped
  ("les [83]" ×2, "les [68]" ×1 — class-55-det KILL recorded these as no
  clean determiner slots, but the word-internal rival is unexcluded there).
- battery-class-55-det (KILL, 2026-10-09) forces 55 word-internal at W3
  @1205 only; its 1-of-6 clean pre-noun slot (@550) failed the bar's ≥2
  requirement. The determiner arm is dead, which is compatible with both
  the polyvalence option and the positional-rule option.

Note: the positional rule and the polyvalence option are not mutually
exclusive at letter level — "55-61" as one word could still be spelled
with 55="re" ("reprenne") at the formula windows and 55="pre" at @1205,
which is the letter-level residual in option (A).

## Option (C): one class for all 12 windows — evidence (clause 4)

Uniform verb-class 55 (R19-077 battery-grade). R20-034's grant of
ver78-1670-5581 records that "55=verb battery-grade explains W1/W3/W4
conditionally but is blocked at W2 (06-rule) and W6 (no licensed post-
'la ver' verb frame)." The adjective arm is dead (zero legs; no §7 split
declarable at battery level). So a uniform verb class covers at most 10
of 12 windows and is actively blocked at 2 — option (C) has the weakest
coverage of the three, but it is the only option that names a class
without touching §7.

The letter-level residual applies to (C) as well: even if 55 is uniformly
verb-class, the letter contribution differs between "prend" (55-61) and
"re"+"stem" (55-81), so class-uniformity does not resolve the
polyvalence-shaped observation — it only defers it below the value tier.

## Companion discriminator status (clause 5: PASS — status recorded)

- `re81-W2-noun-discrim` (P3): still `status: queued`, no verdict. Its
  evidence — discriminating *repas* vs *regard* vs *retour* at W2 @523
  (needs 97's value) — is ABSENT from this package. If it lands, it
  strengthens or dissolves the "re"-prefix arm of option (A).
- `re81-W4-02-class` (P4): still `status: queued`, no verdict. Its
  evidence — determiner-02 vs subject-02 at W4 @1085 — is ABSENT from
  this package. If it lands, it gives the noun stems a second leg
  (determiner-02) or the verb stems a leg (subject-02).

This package is therefore explicitly partial: the two queued
discriminators are the missing evidence the target's bar cites. A
re-package after their return is proposed below.

## Per-clause pass/fail

1. PASS — census re-derived byte-exact (12/12 positions, follower and
   predecessor distributions, contact zeros, formula ×2).
2. PASS — option (A) evidence recorded with letter-level tension and all
   returned discriminators.
3. PASS — option (B) evidence recorded; zero-exception coverage stated
   with the non-exclusivity note.
4. PASS — option (C) evidence recorded with the blocking windows (W2, W6)
   and the letter-level residual.
5. PASS — both companion discriminators still queued; missing evidence
   stated explicitly.
6. PASS — no adjudication attempted anywhere in this package.

## Verdict: NULL (gather-only)

All six clauses pass. No polyvalence declared, no class named, no value
promoted or killed. This package is input to the red-team docket, which
decides. The three options for the red team:

- **(A) Second polyvalence:** declare 55 polyvalent ("prend"-stem vs
  "re"-prefix), the second after 67 et/veut. Needs the §7 declaration
  bar: kill-grade byte evidence for two 55 values.
- **(B) Positional segmentation rule:** declare "55 word-internal iff
  followed by 61" as a segmentation rule — no second value, the
  difference is positional. The 61↔81 zero-contact count is its strongest
  leg; the letter-level "reprenne" vs "prend" residual survives under it.
- **(C) One class:** hold 55 uniformly verb-class (R19-077) and treat the
  W2/W6 blocks as fenced residuals; leaves the letter-level tension
  unresolved below the value tier.

## Follow-ups (verified ABSENT from battery-queue.json)

1. `redteam-55-polyvalence-rerun` (P2, gather-only) — re-package this
   evidence question once `re81-W2-noun-discrim` and `re81-W4-02-class`
   return; their verdicts are the missing evidence this bar cites.
2. `seg-55-61-94-letters` (P3) — resolve the letter-level residual at the
   formula windows: test "reprenne" (55="re"+61="pren"+94="ne") vs "prend"
   (55="pre"+61="nd") segmentation with letter-tier evidence; whichever
   segmentation the red team adopts constrains options (A)/(B) directly.
3. `uniform-55-verb-w2w6` (P3) — test whether any uniform verb-class
   reading covers W2 @523 and W6 @1671 (the two windows blocking option
   (C)); kill-grade block at either window fences option (C).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-redteam-55-polyvalence.md`
- Queue: `redteam-55-polyvalence` → `status: verdict`, `result: null`,
  2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file
  + rename; disk re-validated; own entry only; no downgrade).
- Lock created on start (2026-10-09T17:58:02Z, no stale lock), deleted on
  completion. R5005, sealed gates, red-team adjudication queue untouched.
  No standing or red-team verdict contradicted, downgraded, or
  re-litigated. §7 intact.
