# Round-14 Red-Team Pre-Registration (PREREG14) — LOCKED

Red team: round-14 red-team adjudicator · 2026-10-07 (CDT) · kill authority
over all round-14 promotions, demotions, and kill recommendations.

**LOCK TIMESTAMP:** written and locked 2026-10-07 before any round-14 executor
output was read. At lock time NO round-14 executor package exists
(`code/crowd14/` absent; council/executor outputs for the round-14 work
orders have not landed). This document may not be amended after the first
round-14 executor output is read — bars, once locked, apply as written.

Scope: every round-14 executor recommendation under STATE.md "next: Round-14
work orders" (items 1–8). KE1/KE2 are red-team-owned kill experiments —
this docket rules EXECUTOR recommendations only; KE1 (INCONCLUSIVE) and KE2
(46=que re-derived GT) stand as adjudicated.

## §1 Authority and docket

1.1 Every promotion, demotion, and kill recommendation in round 14 is ruled
by the red team. No coordinator-applied bars — ever (F26-17 standing).
1.2 The single source of truth is `code/crowd14/redteam/RULINGS-ROUND14.md`.
No status change merges without its numbered ruling (R-###).
1.3 Ruling vocabulary: GRANT / GRANT-WITH-MODIFICATION / GRANT-WITH-CONDITION /
DENY / KILL / BANK (memo/data only, no status change) / NOTE (deficiency flag).
1.4 Sloppy work rule: executor packages with unverifiable numbers, missing
preregistration, or untraceable derivations are ruled DENY or DEMOTE with a
deficiency mark, and the deficiency is named in the ruling. Missing prereg
≠ no ruling — it rules AGAINST the claimant.

## §2 Preregistration audit (case law R11–R13)

2.1 An executor battery that computes results on the cipher must have a
PREREG whose mtime predates the first data-run mtime. Timestamp audit per
package: PASS / PASS-WITH-NOTE / FAIL. Loose header-time rounding is
tolerated only when mtimes govern and the margin is positive (R13: 13s
margin clean).
2.2 Post-hoc bars, post-hoc conditioning rules, and post-hoc window
selections are VOID (F33, H4g/F72 case law). Conditioning rules must be
stated before the windows are partitioned.
2.3 Corpus-discipline clauses are part of every prereg: v8 phrase-zeros VOID
(F77), v8 OCR splits VOID, clean 3.96M pool for phrase queries; v8 usable
for token-level rates only with an explicit sensitivity note.

## §3 The ≥2-independent-legs bar (promotion)

3.1 Promotions require ≥2 independent legs. The red team counts them — never
the executor's count.
3.2 Legs are INDEPENDENT only if they use different instruments on
disjoint data. Two legs from the same battery counting the same datum are
one leg. Ear legs sharing one by-ear model are one leg (N35/N39 case law).
3.3 Provisional statuses propagate: 87=ce is provisional; everything built
on it inherits provisional. 64="qui" re-promotion BLOCKED (stands).
3.4 Uniformity alone never promotes (1690 law, §7).

## §4 Kill bar

4.1 Kill-grade requires the pre-registered bar to have fired AS SPECIFIED —
no bar, no kill.
4.2 Kill-grade evidence classes: (a) grammatical zero on GT-anchored data;
(b) structural contradiction with a pencil crib; (c) n≥3 independent
adverses with no escape hatch; (d) a pre-registered numeric bar crossed with
the licensed instrument.
4.3 Demotions need ≥1 substantive failed leg or adverse; they are ruled too
(no silent demotions).

## §5 No-re-litigation list (round 14, extended)

The following are settled and may not be re-litigated. Referencing them as
established premises is fine; attempting to overturn them without a NEW
pre-registered kill-grade battery is barred:

5.1 48="ne" (KILLED kill-grade, F60). H_verb for 48 (KILLED, F64).
5.2 Unconditioned 48="de" (KILLED, F110). 86=que-family (REFUTED kill-grade,
F65). Unconditioned 84s (KILLED both, F53). Unconditioned-59 (REFUTED
kill-grade, F71). H4g (REFUTED, F72). Three mergers ({87,47}="ce"
unconditioned, {77,00}="le", {43,21}="me" — F56).
5.3 {33,86}, {48,94}, {52,59}, {76,78} as homophone SETS — splits stand
(F103, R-AB1/R-AB2/R-CD1/R-CD2). Class-mate analysis continues; merger
re-litigation is barred.
5.4 Digit hunt (retired, F106). Double-pour stack (PERMANENT FENCE, F111).
"gouvernement" at @1351 (OUT, HIGH — F70). "en ce" at the 3 adjudicated
windows (F107: "en cela" supersedes). Column-refuge concretizations (all
dead, F63). Retired WO-6 bar (F63). Settled round-11/12/13 fences (@1248
NEITHER, @199 NEITHER-conditional, @1351 R-c, @578 scoped, @863 pointer-only,
@633 et-CONDITIONAL, @1519/@1372/@902 nulls, 48's three fences).
5.5 Dissolved islets AS POLYVALENCE: ISLETs 1, 2, 3, 8, 10 dissolved into
word/frame rules (R-IA1–R-IA7, F100). They are word rules now. Any claim of
the form "ISLET X is true polyvalence" for X∈{1,2,3,8,10} must first defeat
the dissolution battery — else barred.
5.6 67 fork is the SOLE true polyvalence (F101). 66/89 are class-constraint
tier, not polyvalence (F102). Any new polyvalence claim needs an F33-form
conditioning rule (verified positional/lexical, falsifiers stated, zero
free cases) — asserted, not assumed.
5.7 1690 uniformity is lane law: NECESSARY but INSUFFICIENT. Any homophone
claim resting on uniformity alone dies. (F103.)

## §6 Instrument law

6.1 F30: rigid syllabification is DEAD. No era-syllable-conditional legs on
morphological fragments (29/82/34 excluded from all rate legs;
40-conditionals excluded). Era word-space legs survive.
6.2 N22 calibration exclusion: 29/82/34 excluded from rate legs (182×/60×/
3.3× over era — validates from a third angle in round 3).
6.3 Cipher-side geometry, word-space grammatical kills, ear/formula locks,
and era unigrams-as-context survive as instruments.
6.4 Traceability (F26-6 case law): every .md number must reproduce from
archived code; trust the JSON over the prose. Battery numbers: spot-check
minimum by the red team; FULL re-derivation for any KILL or registry change.
6.5 Anchor-preserving controls on all future drags (N34 lesson). Never
shuffle anchored windows for the null.
6.6 Echo rule (N32 caution): provisional anchors breed echoes. Any
"discovery" that is a pure echo of a provisional anchor (no new
information) is flagged, not promoted.
6.7 No-double-counting: n_eff governs; byte-identical windows count once
(64-77-84 ×3 precedent, N27).

## §7 Work-order-specific bars (STATE.md round-14 WOs)

WO1 — registry rewrite: the 5 dissolutions (R-IA1–R-IA7) are FINAL. Work
order is application, not re-adjudication. New edits to the word-rule tier
(W-ent1, W-le1, W-en1, W-este1, W-est1, W-est2, W-este2, F-qui-est, F-qui-le)
need rulings; dissolutions themselves are not re-opened (§5.5).

WO2 — 33's infinitive: Fork S/W discriminator. Bar: a pencil-GT-anchored
multi-group word containing 33, OR an I4-window re-analysis with ≥2
independent legs. "savoir" is fork-forbidden under BOTH forks (F109) —
re-proposing it without defeating the fork bar is barred.

WO3 — 81="prin": resolve the "la pour" post-context adverse — chance
artifact (FDR-consistent) or the lead is real. 81 flanks F-C@1088; anchor
pair only if 81 promotes. Bar: ≥2 independent legs; the post-context
adverse must be resolved, not ignored.

WO4 — 74-class / H_stem / 62-polyvalence batteries: standard bars.
74="te" lead stays LEAD until the battery rules. H_stem: leg, not value
(F110) — a value claim needs the verb-stem signature with the ne-marginal
tension resolved. 62-polyvalence: dissolves the "on-48" adverse only with
a positional (syllable-"on") demonstration, not an assertion.

WO5 — 52's non-est value: "la 52" ×3 needs its own battery ("la est"=0).
Bar: ≥2 independent legs; the est-arm (weak lead) must be addressed.

WO6 — 78 fork: ver-initial vs er-final by POSITION. Bar: a positional
(F33-form) conditioning rule or the fork stays unresolved. "le"-frames vs
the er|ne diagnostic tension is the adjudication point.

WO7 — 59's third value: @825 "en ce"+noun frame (word-"est" ruled out,
F71). Bar: ≥2 independent legs for the specific third value; the frame
is the venue, not the verdict.

WO8 — Smith side: main-fleet search scope stays ZERO until C1 passes on
the gapped family (standing). Judge instrument stand-up is the #1 blocker
(F113). Solver-side claims are ruled by the solver-side red team; this
docket rules main-fleet status changes only. Constraints memo: BANK only.

## §8 Docket mechanics

8.1 Rulings are numbered R-### in order of issue, each with: claim, evidence
re-derived by the red team, ruling, and what would overturn it.
8.2 Interim kills: recorded under "Interim kills" when issued (none at lock).
8.3 Baselines extended at close: R14BANK (cipher-side) in
`code/crowd7/redteam/verify_f26_17.py`, ROUND14-LEDGER (status deltas +
drift guards) in `code/crowd7/redteam/verify_round7.py`. Extend, don't
rebuild — earlier BANK/LEDGER blocks untouched.
8.4 This prereg may not be amended after the first round-14 executor output
is read.

---
*Locked 2026-10-07 before any round-14 executor output existed. Bars apply as written.*
