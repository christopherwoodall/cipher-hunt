# Battery report: w1-314-ambig

**Target:** w1-314-ambig — W1 (78@313) alone decides the fork's hardest window
**Claim:** W1 (78@313) alone decides the fork's hardest window
**Date:** 2026-10-08
**Worker:** ac3b499f-10b3-4880-934d-82a7fbf57a0b. No stale lock existed at start; lock created 2026-10-09T00:19:41Z, deleted on completion.
**Stream:** repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py). Never canonical.py. No R5005, sealed gates, or red-team queue touched. All counts trace to the stream.

## Bar (verbatim, pre-registered BEFORE testing)

"parse the 84-24-37-78 left context of 78@313; if 37-78 is word-internal, dict wins W1; if 37 closes a clause (predicative 37 granted A1), ce wins"

## Bar restated as numbered pass/fail clauses (not modified)

1. Clause 1 (dict arm): IF the 84-24-37-78 left context shows 37-78 word-internal, THEN dict wins W1 (45@314 = 'dict', 78-45 = "verdict").
2. Clause 2 (ce arm): IF 37 closes a clause (predicative 37 per granted A1), THEN ce wins W1 (45@314 = 'ce', A11 mirror leg intact).

## Method

1. Reparsed the repaired stream byte-exactly per repair_parse.py (1,847 pairs, 96 unique).
2. Extracted W1's full window @300-345 (row a2_04) and the 84-24-37-78 left context.
3. Enumerated all 37-78 bigrams stream-wide (x4) and all 84-24-37 trigrams (x2) with ±8 context.
4. Imported 24's promoted class (ne-24-profile, PROMOTE 2026-10-08: 24 = finite modal verb) and tested both bar arms for grammaticality under standing values.
5. Built the @474-476 minimal-pair control (byte-identical left context 84-24-37, different 78 follower).

Standing values used: banked 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que; granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on (A15), 47=ce (A4), 94=ne, 12=n, 48=e, 30=pas, 39=a/a; promoted 06=ent; provisional 59=est, 77=le; A1 32 predicative; A11 45='ce' HOLD; 78='ver' LEAD only (R16-005, not granted).

## Window-level evidence (@-offsets are stream indices)

**W1 — 78@313 (row a2_04):**
`@307:20 @308:17 @309:46 @310:84 @311:24 @312:37 @313:78 @314:45 @315:64 @316:59 @317:32 @318:94 @319:06 @320:11 @321:92`
= "[20] fois(17) que(46) on(84) [24] [37] [78] [45] qui(64) est(59) [32] ne(94) [06] la(11) [92]"

**84-24-37-78 is x2 stream-wide:**
- @310-313 (W1): `46-84-24-37-78-45-64` (78 followed by 45)
- @473-476 (row a2_10): `46-84-24-37-78-74-45-93` (78 followed by 74, then 45-93)

**37-78 is x4 stream-wide** (@312, @414, @475, @1770). The two "on-24" instances (@312, @475) share byte-identical left context.

**24->37 is x2 = exactly the two 84-24-37 windows** (24's follower census: 87 x10, 85 x5, 82 x4, 30 x3, 89 x3, 37 x2, ...). 84-24 is x3 (@310, @473, @1485); @1485 is 84-24-87 (the ne-24-profile "clause-final 24 before ce-opener" frame), not 84-24-37.

**78's successor census** (31 windows): 45 x4, 40 x3, 48/49/41/62/94 x2 each, 18 singletons including 74 x1 (@476). 78 takes 20 distinct followers — it is not bound to 45.

## Analysis

**Step 1 — 24 is a modal verb at W1.** ne-24-profile PROMOTED (class-level, 2026-10-08): 24 = finite verb, infinitive-taking, modal-shaped; preposition arm killed at kill grade. At W1, "46-84-24" = "que-on-[24]" is one of the six cited subordinate finite-modal slots ("qu'on 24" x2 frame). A finite modal requires an infinitive complement (ellipsis would be marked and is unattested for 24: its complements are overt infinitives 85 x5 / 89 x3 / 80 x2).

**Step 2 — the infinitive complement must be 37-78.** After modal-24 at W1 come 37-78-45-64. Candidates:
- (a) 37 alone (1-pair infinitive): 37's profile contradicts infinitive-hood (37 takes infinitive complements itself: 37->86 x1 INF-class, 37->33 x1; A1 frames it predicative). Not viable.
- (b) 37-78 (2 pairs): "X-ver" with 78='ver' LEAD — French "-ver" infinitives exist (rêver, lever, trouver, prouver, ...). Viable.
- (c) 37-78-45 (3 pairs): would be an "X-ver-dict" infinitive under the fork's own 78='ver'+45='dict' assumption. No French infinitive ends in "-dict"/"verdict". Not viable.

Therefore 37-78 is the infinitive complement: **37-78 IS word-internal at W1** (Clause 1's condition is MET).

**Step 3 — the @475 control proves 78 is word-final.** With byte-identical left context (84-24-37), 78@476 is followed by 74, not 45. If 78-45 were a fixed word ("verdict") with 37 joining leftward, the identical left context should not strand 78 before 74. The parsimonious reading: "37-78" is the same complete infinitive word in both windows; 78 is infinitive-final (word-final) in both. 78's 20 distinct followers confirm it is not bound to 45.

**Step 4 — word-final 78 forces a boundary before 45.** 45@314 is therefore word-initial. A word-initial 45 cannot be 'dict' (45='dict' is a bound syllable of the "verdict" word per R-pos; syllables do not start words). 45@314 = 'ce' per standing A11 HOLD.

**Step 5 — the CE parse is fully grammatical; the dict parse is not.**

CE parse of W1: "[20] fois(17) que(46) on(84) [24-modal] [37-78-infinitive]. ce(45) qui(64) est(59) [32-predicative] ne(94) [06-ent] la(11) [92]…"
= "The [20]th time that one [modal]s [infinitive]; that which is [32] does-not [verb-ent] the [92]…" — clean, using only granted/promoted/banked values plus the promoted modal-24 class. A11's 45-64 mirror leg is intact.

Dict parse attempts, all fail:
- (i) "37-78-45" one word as modal complement: must be an infinitive; "X-verdict" is not a French infinitive. Ungrammatical.
- (ii) "[37] verdict(78-45)": modal-24 taking "[37]" (non-infinitive) as complement. Ungrammatical (modals require infinitives; 37 is not infinitive-shaped).
- (iii) "[37-78-infinitive] [45='dict']": 45='dict' requires 78-45 word-internal, but 78 is infinitive-final (Step 3). Contradiction.

**Step 6 — Clause 2 (predicative 37) does not fire.** 37 at W1 is infinitive-internal (a syllable of the infinitive word), not a standalone predicative adjective. Predicative-37 would additionally require 24 to be a copula, but 24 is modal-shaped (takes infinitives, killed preposition arm; no copula evidence). The A1 predicative grant is in any case under red-team escalation (frame-37-reexam null: 5/6 legs VOID per ISLET-10), so it cannot bear weight here regardless.

## Per-clause pass/fail

1. Clause 1 (dict arm): CONDITION MET — 37-78 is word-internal (infinitive complement of modal-24, confirmed by the @475 control). **BUT the pre-registered CONSEQUENCE ("dict wins") is REFUTED**: word-internal 37-78 is a COMPLETE infinitive word ending at 78, which forces a word boundary before 45, which forces 45='ce'. The bar's implicit assumption — that word-internal 37-78 means 37 joins the "verdict" word leftward — is false. The infinitive analysis EXCLUDES the verdict word at W1.
2. Clause 2 (ce arm): CONDITION NOT MET — 37 is not clause-final predicative at W1 (it is infinitive-internal; 24 is modal, not copula). Does not fire.

**The bar as written is self-contradictory on the evidence**: its Clause-1 condition is met, but the data forces the opposite of its Clause-1 consequence. Applying the bar literally would verdict "dict wins W1" — a grammatically impossible parse (Step 5). Rewriting the bar silently is prohibited (§2).

## Adverses answered

- "24 unvalued": ANSWERED. 24's VALUE ("peut"/"sait"/"doit") is open, but its CLASS (finite modal verb) is PROMOTED (ne-24-profile) and the class alone drives the analysis — the modal requires an infinitive complement regardless of which modal it is. The open value is fenced as immaterial to the boundary decision.
- "37's value unnamed (frame-37-reexam queued)": FENCED with cause. 37's global value remains unnamed and A1 predicative-37 is under red-team escalation (frame-37-reexam null, 5/6 legs VOID). This battery does not name 37 and does not rely on predicative-37: at W1, 37 is syllable-internal to the infinitive "37-78". NOTE for the red team: infinitive-internal 37 tensions a word-level predicative-37 value at this window, but the A1 adjudication is theirs, not this battery's.

## Verdict: null

**Headline: the bar's consequence mapping is inverted by the modal-24 evidence — W1 decides for CE, but the bar as written would have said dict.**

What the data establishes (conclusively at W1): 37-78 is word-internal as the infinitive complement of promoted modal-24; the infinitive is complete at 78 (@475 control: identical left context strands 78 before 74); the forced boundary before 45 makes 45@314 word-initial 'ce' (A11 HOLD, mirror leg 45-64 intact); every dict parse of W1 is ungrammatical. **CE wins W1; the "verdict" reading is excluded at W1.** Scope: W1 and the 84-24-37 left-context family only — W2/W3/W4 have different left contexts and are untouched (dict-78-45-wordbound queued owns the global boundary question).

Why null and not a CE promotion: the pre-registered bar maps the met condition (word-internal 37-78) to "dict wins". That mapping is refuted, so the bar is genuinely untestable as written (§4) — applying it would manufacture a false "dict" verdict, and silently rewriting it is prohibited. The fork itself is resolved at W1 (for CE), but this battery's verdict must be null with the inversion recorded as the finding.

No standing red-team verdict is contradicted: A11 HOLD is preserved (strengthened: 3/3 mirror legs intact); R16-005 (78='ver' LEAD) untouched; no polyvalence declared. NOTE: the fork battery's proposed positional rule R-pos (45='dict' iff preceded by 78) FAILS at W1 — 45@314 is preceded by 78 but parses as 'ce' because 78 is infinitive-final. R-pos was never adopted (needs red-team declaration per §7); W1 is recorded as a counterexample for the red team (see follow-up 3).

## Follow-up targets (null regenerates work)

1. **w1-314-rebar** (priority 1). Claim: W1 decides for CE under the corrected mapping. Bars: (a) 37-78 word-internal as infinitive complement of modal-24 re-derived on the repaired stream (84-24-37-78 x2, 24->37 x2 = exhaustive); (b) "37-78-45" single-word refuted (no French "X-verdict" infinitive; @475 control strands 78 before 74 in identical left context); (c) CE parse ("qu'on [modal] [infinitive]. ce qui est [32] ne [verb-ent] la [92]") grammatical with zero non-granted assumptions beyond provisional 59='est'; (d) all three dict parses shown ungrammatical with stated cause each. Evidence: this report. Adverses: 37's global value still open (tensions A1, red-team owned); R-pos counterexample recorded.
2. **inf-37-78-475** (priority 2). Claim: 37-78 is the same stable infinitive word at @475, confirming 78 word-final in the 84-24-37 family. Bars: (a) @474-482 parsed ("on [24] [37-78-inf] [74] ce(45) [93]") with 74's post-infinitive slot named or fenced; (b) 37-78 unit stability across all x4 (left contexts 84-24 x2, 84-51, 26-verb) stated — @414 (84-51-37-78-49) and @1770 (26-verb-37-78-62) must not contradict the infinitive reading; (c) 78's 20-follower scatter cited against bound-"verdict" reading. Evidence: this report's Steps 2-3. Adverses: 51's value open (@414); 74's value open.
3. **rpos-w1-exception** (priority 2). Claim: W1 falsifies unconditioned R-pos (45='dict' iff preceded by 78) — 45@314 is preceded by 78 yet is 'ce'. Bars: (a) W1 re-derived with 78 shown infinitive-final (boundary before 45) from this report; (b) state the refined rule candidate (45='dict' iff 78 is word-MEDIAL, i.e., 78-45 word-internal AND 78 not word-final) with W1-W4 classified under it; (c) no red-team declaration made — evidence gathered for the §7 positional-rule decision only. Evidence: this report's Step 4 + fork-78-45-adjudication's R-pos. Adverses: R-pos never adopted (red-team act); W2-W4 untested under the refined rule (dict-78-45-wordbound queued).
