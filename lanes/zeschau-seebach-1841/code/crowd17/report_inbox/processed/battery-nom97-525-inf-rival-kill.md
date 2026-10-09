# Battery `nom97-525-inf-rival-kill` — verdict: KILL

## Bar (verbatim, pre-registered)

> "kill iff no grammatical INF parse exists; else fence the INF arm at @525"

Restated as numbered pass/fail clauses (before testing):
- **C1:** no grammatical INF parse exists for 97 at this window under
  standing values (no left governor, no right governor, no dislocated-topic
  shape, no copula-subject shape, no pour/exclamation/auxiliary shape) →
  KILL the INF arm at @525.
- **C2:** else (a grammatical INF parse survives) → fence the INF arm at
  @525 instead.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
(parsed like `code/side-keyhunt/repair_parse.py`); asserts held
(1847 pairs, 96 types). `canonical.py` never used.

Adopted premises (not re-litigated): `nom-97-526-adverb` PROMOTE
(adverbial-81 dead at @524; nominal-81 at this window); standing §7
values (47="ce" A4, 06="ent", 77="le" provisional, 59="est" provisional,
44/37 predicative A1, 70="pre" GT, 00="pour" A9, R24, R19-123).

Offset note: the queue evidence uses 0-based indices. 97 is at **0-based
@525** (parent battery's 1-based "@526"); 81 is at 0-based @524. All
offsets below are 0-based.

## Window-level evidence (byte-exact)

Locus, row a3_00, 0b@520–530:
`91 77 06 55 [81] 97 47 44 59 37 64`
= "[91] le(77,prov) ent(06) [55] [81-nom] [97] ce(47,prom) [44,A1]
est(59,prov) [37,A1] qui(64,grant)". Row join at 530|531.

97 census: n=10. Left: 00×4, 81×2, 40/80/02/16×1. Right:
51/46/09/86/47/13/41/40/69/00 ×1 each. The four "pour [97]" windows are
@2/@288/@588/@1823 — none is this window.

## Exhaustion of INF parse routes at @525

In 1841 French an infinitive needs a license: a governing verb or
preposition, a dislocated-topic frame, or a nominalized-subject frame.
Every route fails under standing values:

- **R1 (left-governed infinitive):** the left slot @524 is 81 = nominal
  (adopted premise); @523 = 55 (unvalued, determiner-position
  collocation); @522 = 06 = word-final "ent" syllable; @521 = 77 = "le"
  provisional; @520 = 91 unvalued; @519/518 = "pre" syllable. No verb,
  no preposition anywhere leftward. DEAD.
- **R2 (right-governed by 44):** geometry is "97 47 44" — 47 = "ce" (A4
  granted) intervenes, and 44 is predicative (A1), not an infinitive
  governor; it cannot govern leftward across "ce". DEAD.
- **R3 (dislocated infinitive-topic, "Partir, c'est…" shaped):**
  - R3a topic = 97 alone: strands nominal-81; "[55] [81-noun]" NP
    abutting a bare infinitive topic collapses into subject + predicate
    (the NOM parse) — ungrammatical as a dislocation. DEAD.
  - R3b topic = "81 97" as one unit: noun + bare infinitive is not a
    licensable unit in 1841 French (no "de/à" between). DEAD.
  - R3c topic with adverbial-81: adverbial-81 is dead at @524 (adopted
    premise — this was the revival condition the parent made the INF
    reading depend on). DEAD.
- **R4 (infinitive as subject of "est"):** 47 = "ce" (A4) holds the
  copula subject slot ("ce [44] est [37]" is complete); 97 cannot
  co-occupy the subject. DEAD.
- **R5 ("de [97], c'est…" with 81 = preposition "de"):** requires (i)
  naming 81's value — §3 bars battery value-naming on unvalued cells —
  and (ii) overturning the adopted window-level nominal-81 premise.
  Red-team venue only; not a standing battery parse. NOT A BATTERY PARSE.
- **R6 ("pour [97]" shaped):** no 00 adjacent to this 97. DEAD.
- **R7 (governed exclamatory infinitive):** the head clause is the
  copular "ce [44] est [37]", not an exclaimed noun phrase; the
  gov-excl-inf batteries licensed only exclaimed-NP heads. DEAD.
- **R8 (auxiliary chain / "ne … [97]"):** no auxiliary, no 94 in the
  window. DEAD.

## Per-clause pass/fail

- **C1 PASS:** no grammatical INF parse exists for 97 at @525 under
  standing values. The kill is positive, not epistemic: the subject
  slot is occupied by the nominal "55 81" NP, the copula subject is
  occupied by granted "ce", and no governor or dislocation frame is
  licensable. → **KILL.**
- **C2 does not fire.**

## Verdict: KILL

The INF rival at @525 (1b@526) is dead. The "@526 window" leg is now:
NOM-97 clean, INF-97 killed — the window-level INF/NOM tie is resolved
in favor of NOM.

## Scope and caveats (stated, not ignored)

- **Window-level only.** No registry change; 97's class stays open. The
  global INF/NOM tie for 97 survives unchanged via the four "pour [97]"
  windows (@2/@288/@588/@1823), which are untouched by this kill.
- R5's re-open is red-team venue: naming 81's value (or overturning the
  window-level nominal-81 premise) would revive an INF route, but that
  is a red-team adjudication, not a battery parse.
- §7 intact (67 sole polyvalence); no standing/red-team verdict
  contradicted or downgraded; canonical-stream caveat stands (row a3_00
  offsets unvalidated).
- Per §4, kills regenerate no follow-ups.

## Bookkeeping

- Queue: `nom97-525-inf-rival-kill` → `status: verdict`, `result: kill`,
  2026-10-09 (pre-write assert passed — was queued/verdictless;
  temp-file + rename; JSON re-validated from disk; own entry only; no
  downgrade).
- Lock created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
