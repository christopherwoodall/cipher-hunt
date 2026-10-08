# PRE-REGISTRATION — CARRY-FORWARD (CLASSES), round 13 (council WO7, class half)
**Executor:** CARRY-CLASSES · **Date:** 2026-10-07 (written BEFORE any round-13
decision computation; only standing/recorded numbers consulted:
`code/crowd12/identifier33/identifier33_results.json`,
`code/crowd12/class3192/{b31,b92}_results.json`,
`code/crowd12/veutleg/veutleg_results.json`,
`code/crowd12/report_inbox/redteam-rulings12.md`,
french-blitz reports, NOTES.md/STATE.md)
**Work dir:** `code/crowd13/carry-classes/`
**Report note:** `report_inbox/carry-classes-r13.md`

**Task (council WO7, class half):** (1) 33's specific infinitive — pre-register a
candidate set from era "pour [inf]" rates (Nesselrode v8 / clean pool), test each
of the 8 "pour 33" frames, report leading candidate with legs or an honest
"unidentified with constraints". Round-12's value paradox stands — NOT forced.
(2) 31-class battery — 31 contested leaning verbal; needs 08 disambiguation or a
second GT-anchored nominal contact. (3) 92-class battery — conditioned-polyvalence
candidate; run the F33 battery on 92 as subject.

**Standing record (not re-derived):**
- Round-12 R1 GRANTED: 33's specific infinitive NULL; F-A/F-D FENCED; F-B/F-C/F-E
  NULL; **33-value paradox recorded unresolved** (Fork S: 33=stem ⇒ breaks
  96="par"; Fork W: 33=whole-word monosyllabic inf ⇒ breaks I4 stem+"er";
  F79's C1 survives on I1+I2, class grant stands). Lead banked: 21="ce"
  (post-hoc, granted; rival 21="me" ungranted). F-C pair = same unknown
  infinitive ×2 (replication datum).
- Round-12 R3 GRANTED: **31=VERBAL (finite) provisional-conditioned**
  (3 disambiguated verbal windows @338/@1647 qui-relative + @1489 D-ce;
  C1 conditionals 64="qui"/87="ce"/08="l'"-lead; E31-1 era leg VOID, disclosed).
  92 H-pre REFUTED (cross-signature @683, mechanical falsifier). 92 H-presuc
  FENCED (n_eff=1 < ISLET-3 precedent; NOUN-islet additionally fenced by the T1
  "-quière" tension; F1–F4 replication legs named for round 13). VERB-arm
  (92=finite verb iff pre∈{94,46}, n=3) recorded as datum.
- Drag: `code/council/drag/drag_hits.json` NOT landed (drag/ holds build/run
  scripts only) — nothing to integrate; recorded.
- No re-litigation of settled kills. Recommendations only; adjudicator rules.

## Instrument (identical lanes to round-12, verified by gates)
- Repaired 1,847-pair stream via `code/crowd8/frenchman/util` (PAIRS/N/UNI/GT).
  Byte-verify gate: N=1847; @1519 window=[11,91,67,8,31]; @902 window=[16,92,67,16,88].
  n33 "pour 33" frames = 8 (@186/@408/@467/@846/@936/@1088/@1245/@1630);
  n31=8; n92=22; n08=18. HALT on drift.
- Era pool for the F33 battery = identifier33's clean pool: all
  `code/side-period/corpus/*.txt` minus AZ-newspaper, harvest-log,
  adb-zeschau (gate: 3,960,009 tokens, lane `tok()` verbatim; v8 NW=92,677).
  Rate bars on pool∖v8 (disjoint from v8). **v8-VOID rule (F77): no phrase
  query rests on v8 OCR text.** For NEW phrase queries I use pool∖v8 (3.87M,
  disjoint from v8 AND from round-12's v8 tail arm) — strictly stronger than F77.
- For the 31 battery: class3192's 14-file French pool (gate: 3,212,595 tokens)
  via `code/crowd12/class3192/era.py`.
- Candidate set C: mechanical, `is_inf(w) = endswith(er,ir,re) and len>3` ×
  n("pour X")≥3 on the 3.96M pool; round-12's 8 hand-drops carried verbatim
  with reasons (notre, votre, titre, premier, ministre, quatre, maître,
  homère). Gate: |C| = 461 raw→453 after drops, R top-10 identical to
  round-12's (faire, être, avoir, aller, obtenir, donner, mettre, assurer,
  arriver, atteindre) — drift check.

## Battery R13-33 — 33's specific infinitive (council carry)
### Scope condition (disclosed upfront)
This is a WHOLE-WORD battery: it tests the Fork-W interpretation (33 =
complete monosyllabic infinitive, suc = next word). Under Fork S (33 = stem),
"pour [inf]" whole-word rates do not apply. The unresolved fork (R1) caps any
outcome below ID regardless of counts — I do not force it.

### Checks (pre-registered; all on pool∖v8 except the named v8 arm)
- **R (rate):** X ∈ round-12's top-10 by n("pour X") on pool∖v8. Gate: top-10
  list identical ⇒ no drift. (Base-rate, never an ID leg alone.)
- **T2 (NEW independent arm; the banked-21="ce" datum):** F-E (@936/@1630) with
  21="ce" GRANTED-banked ⇒ frame "pour X ce qui" (suc(21)=64="qui"-prov). On
  **pool∖v8** (disjoint from round-12's v8 T-arm): T2(X) = n("pour X ce qui").
  FIRES iff UNIQUE argmax with n ≥ 2. R⊥T2 by disjoint corpora (the lane's
  ≥2-check rule). Hand-read: the single winner's era windows (3 examples,
  constituency-checked) + fork-compatibility note (syllable count, by-hand).
- **T-D (pool fence re-check):** F-D (@846, suc=96="par"-prov): n_pool∖v8
  ("pour X par" + e-initial next). Expect 0 (round-12: 0/3.96M). If 0 ⇒
  F-D fence RE-CONFIRMED on the disjoint corpus. (Conditional on 96="par".)
- **J-C (joint replication constraint):** the F-C pair (@467/@1088, "00 33 79 80
  06") is ONE unknown infinitive ×2 (R1). Testable joint constraint with
  unglossed tails: the candidate's era "pour X" rate must be non-degenerate
  AND its supplementary-anchor profile must be consistent at both frames —
  @467: 96="par"-prov two pairs before 00; @1088: 29="er"-GT after 06.
  Pre-registered honest scope: with 79/80/06 unglossed, the joint constraint
  reduces to R-membership + anchor compatibility; report as constraint datum,
  never an ID. If nothing converges ⇒ "one unknown infinitive ×2" stands.
- **L/A (per round-12):** L = ΣT ≥ 1 per cluster else FENCED; A = hand-read
  anchor confirmation only. F-B (@408) and F-C (@467/@1088) tails unglossed ⇒
  T n/a (recorded, not scored); F-A (@186/@1245) FENCED per R1 (F81), re-verified
  by gate, not re-argued.
- **Complement-frame datum (new, weak):** for the T2 winner X (if any), pool∖v8
  complement distribution of "pour X ce qui" (what follows) vs the cipher's
  @936/@1630 tails — reported as constraint, not a leg.

### Verdict bars R13-33 (I recommend; adjudicator rules)
- **ID:** unreachable this round (fork unresolved ⇒ cap). Not scored.
- **LEAN:** T2 unique argmax (n≥2) ∧ A found ∧ fork-compatible by hand-read ∧
  R-membership. ≥2 independent checks (R⊥T2).
- **NULL (constrained):** otherwise. Constraints stated explicitly:
  transitivity (F-C pair = one unknown ×2; F-E pair = one unknown ×2),
  complement frames per cluster, fork scope (Fork-W only), conditional
  gloss dependencies (96="par", 64="qui", 21="ce" — all provisional/banked).

## Battery R13-31 — 31's class (verification carry)
Round-12's 31=VERBAL provisional-conditioned was GRANTED by the red team — this
is VERIFICATION, not re-litigation: an independent byte-exact re-derivation of
the B31 census (fresh script, same pre-registered D-rules) to confirm no drift,
plus the conservative-outcome audit the WO demands.

- **Re-derive:** D-ce/D-que/D-ne/D-qui over all 18 08-positions; classify all 8
  31-windows (qui-relative / D-rule / 08-undisambiguated / 11-ambiguous /
  pre-unidentified). CONFIRM iff ≥2 disambiguated verbal contacts from distinct
  windows ∧ 0 disambiguated nominal contacts, byte-identical to round-12's
  (@338, @1647 qui-relative; @1489 D-ce).
- **Conservative audit (disclosed, pre-listed):**
  1. Conditionals: 64="qui"-prov (C1), 87="ce"-prov (C1), 08="l'"-lead.
  2. "-quière" FENCE (R3): "64 29 40" @290/@684 tensions 64="qui"-word;
     64 stays provisional-FAVORED; flag open for the 64 lane.
  3. E31-1 era leg VOID (honestly disclosed round-12): 11/12 ("ce","l'") hits
     are "est-ce"+article OCR idiom — the D-ce grammar argument stands alone.
  4. One-sidedness: D-rules can only resolve toward VERBAL (no article-forcing
     rule exists); route (b) (second GT-anchored nominal contact) STILL
     unmeetable (11→31 n=1 @1516 only; 46→31 n=0).
- **Consistency datum (not a leg — shares the hypothesis):** the 31→29 window
  under F22 granularity: if 31 = finite-verb stem, "31 29" = stem+"er" ending
  (e.g. "ce l'empêche" = 87,08,31,29 at @1488–@1491). Report consistent/
  inconsistent, never counted toward the bar.
- **Verdict rule:** CONFIRM 31=VERBAL (finite) provisional-conditioned iff the
  re-derivation matches round-12 byte-exact; else surface the drift. No status
  change applied by me.

## Battery R13-92 — the F33 battery on 92 as subject
Scope: the F33 whole-word identification battery (candidate set C, R/T/L/A)
applied to 92's POUR-arm windows only: @49 (suc 79), @330 (suc 50),
@593 (suc 79), @683 (suc 64), @978 (suc 7), @1154 (suc 29).
LA-arm (11 92) and VERB-arm (94/46 92) out of scope — recorded, not forced.
Same Fork-W scope condition as R13-33; the fork paradox applies to 92 equally
(I1: pre==00 ×6; I4: 92→29 ×1 at @1154 — the 33 paradox at small n).

- **R:** X ∈ top-10 n("pour X") pool∖v8 (base-rate per window; never an ID).
- **T (tail, v8 arm, only where glossed):**
  - @683 (suc=64="qui"-prov): T_683(X) = n_v8("pour X W qui"). B92's
    NOUN-strong datum predicts ~0 for infinitives (E92-1: the 4
    infinitive-lean middles were interrogative-qui, not relative).
    Cross-instrument check: T_683≈0 ⇒ corroborates B92's NOUN-islet.
    (Conditional on 64="qui"; additionally fenced by the "-quière" tension.)
  - @1154 (suc=29="er"-GT): sub-word tail — tail-shape query not definable at
    word granularity; report FRAME LICENSE only (E92-3: 3,325 "pour"+er-word).
  - @49/@330/@593/@978: tails unglossed ⇒ T n/a (recorded, not scored).
- **J-POUR (joint constraint):** whole-word reading demands ONE X across all
  six POUR-arm windows. T_683≈0 (predicted) ⇒ the single-infinitive hypothesis
  FAILS the joint constraint at @683 ⇒ the F33 battery itself corroborates
  conditioned-polyvalence (cross-instrument with B92's FENCED H-presuc), or
  forces Fork-S for 92. Report as constraint datum, not a kill.
- **L/A:** as round-12 (L = ΣT ≥ 1; A = hand-read confirmation only).

### Verdict bars R13-92
- **ID:** unreachable (T n/a at 4/6 windows; @683 predicts T≈0). Not scored.
- **LEAN:** not reachable at window level either — capped by T-n/a; recorded.
- **NULL (constrained):** expected. Constraints stated: (a) J-POUR failure ⇒
  POUR-arm is not one whole-word infinitive; (b) @683 infinitive-zero ⇒
  NOUN-islet corroborated (B92 cross-instrument); (c) @1154 frame licensed,
  value unidentifiable at whole-word granularity; (d) fork scope (Fork-W).

## What counts as done
`r13_33.py`/`r13_31.py`/`r13_92.py` + `r13_33_results.json`/`r13_31_results.json`/
`r13_92_results.json` (per-window tables, exact counts, all 0-based repaired
positions; no ciphertext invented), this PREREG.md, and the report note at
`report_inbox/carry-classes-r13.md` with per-item verdicts (33 status, 31
verdict, 92 verdict), the paradox/constraints stated where honest, evidence
paths, and what would break ties.
