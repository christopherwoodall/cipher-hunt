# Battery report: val-13-567

- Target id: `val-13-567`
- Claim: "Name 13's class at @567 ('[97] 13 [76]' window); the direct blocker for this joint test."
- Date: 2026-10-09
- Worker: battery worker (subagent 1d47b28a-5248-43c5-887e-cd66a9091710)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed like `code/side-keyhunt/repair_parse.py`); asserts held (1847 pairs, 96 types). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.

## Bar (verbatim, pre-registered from battery-queue.json)

"post-nominal-adjective / word-final-letter / word-internal, with byte evidence at battery grade; fence if none licensed."

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1 — post-nominal adjective:** 13's class at @567 is named as post-nominal adjective with byte evidence at battery grade — "[97] [13-ADJ] [76]" parses under standing values.
2. **C2 — word-final letter:** 13's class at @567 is named as word-final letter with byte evidence at battery grade. EXCLUDED by standing kill (`letter-13-verdicts`); the task directive bars re-litigation. Not tested.
3. **C3 — word-internal:** 13's class at @567 is named as word-internal (letter/syllable/suffix inside a longer word) with byte evidence at battery grade.
4. **Verdict rule:** promote the class naming iff exactly one of C1/C3 passes at battery grade; fence the @567 class-naming claim iff none is licensed.

## Method

Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/val-13-567.lock` on start (agent id + 2026-10-09T18:23:14Z); no stale lock present. Re-derived the repaired stream in-session before testing. Offset convention: @n = 0-based pair index (1-based in parens).

Standing values used (protocol §7 + battery record; premises only, never re-litigated): banked GT 11=la, 82=m, 34=i, 29=er, 40=e, 46=que; granted 87=ce, 47="ce" (A4), 00="pour" (A9), 84="on" (A15); 80 verb-frame (A8); 76=["noun","prom"] masculine (R19; `val-76-class-census`; never downgraded); 45="ce/dict" lead (A11 HOLD); 97 INF/NOM tie unadjudicated (`val-97-verb-test` NULL; `redteam-97-tie-adjudication` delivered the adjudication package, decision pending); 13 unvalued; §7 (67 et/veut sole true polyvalence). Adopted battery verdicts: `letter-13-verdicts` KILL (word-final-13 at the two "78-45-13" windows); `subj-13-value` KILL (plural determiner, class-level); `pronoun-13-les` KILL ('les' object pronoun, died at @567); `value-13-third-arm` KILL (uniform non-'les' word-level values, adjective included; the @567/568 wall decisive); `noun-97-568` KILL (the "97 13 76" wall is class-independent); `reseg-13-armA` PROMOTE (13 = nominal-closing suffix at the five arm-A windows); `reseg-13-armB` KILL (uniform-suffix falsified; @567 = conditional admit IFF 97 nominal).

## Window-level evidence (byte-exact, re-derived)

Locus @567 (1-based @568), row a3_02:

`@561:67 @562:11 @563:43 @564:24 @565:80 @566:97 @567:13 @568:76 @569:45 @570:94 @571:52`

The joint-test window: `80 97 13 76 45` (0b@565–569). Census results:
- Trigram "97 13 76": **1x stream-wide (hapax)** — no recurrence; no byte support for a multi-group word unit here (contrast the byte-exact x2 "13-55-61" unit at W1/W2, @575/@1166, which does not occur at @567).
- Bigrams: "97 13" x1; "13 76" x1.
- Dislocation-precedent check for the adjective rescue: "N(noun-class) 45 94" windows stream-wide = exactly one, **@568 itself** ("76 45 94", preceded by 13). "X 47 94" (47=ce granted) windows = **zero**. No battery-grade "N, ce ne…" dislocation precedent exists anywhere.

## Per-clause pass/fail

**C1 — post-nominal adjective: FAIL (per-window, kill grade).**

- Under NOM-97 (live tie arm): "[80-V] [97-N] [13-ADJ] [76-N]" — 80→97 and 97→13 are fine in principle, but 13→76 is bare ADJ→NOUN contact, ungrammatical in 1841 French without a clause boundary. All rescues exhausted at battery grade: (i) dislocation "[76], ce(45) ne(94)…" — zero byte precedent (only "N 45 94" window is @568 itself; zero "X 47 94" windows); (ii) asyndetic boundary — no punctuation data; the lane's battery-grade boundaries all ride standing-value verbs (reseg batteries), none abuts here; (iii) 76 non-nominal — barred by 76's group-level noun promote (never downgraded).
- Under INF-97 (adopted promote): the adjective has no nominal host ("[97-INF] [13-ADJ]" cannot modify an infinitive; substantivization needs a determiner — absent).
- The uniform-adjective value is already kill-grade dead globally (`value-13-third-arm`: adjective + finite verb at the five verb windows; §7 one-value extends). A local @567 adjective exception would need §7 red-team venue (second polyvalence) — not declarable at battery grade.
- The adjective arm is excluded at @567 under every live premise.

**C2 — word-final letter: EXCLUDED.** Standing kill (`letter-13-verdicts`: 13 = plural "s" of "verdicts" falsified by the forced "ce verdicts" mismatch); task directive bars re-litigation. Not tested.

**C3 — word-internal: FAIL (not licensed at battery grade).** Shapes enumerated:

- (a) "97-13" one word: fenced to red-team venue (`value-13-third-arm`: sub-lexical 13 "underdetermined at battery grade"; `noun-97-568`: "explicitly fenced as red-team territory"). Not licensed at battery grade.
- (b) "13-76" / "97-13-76" one word: contradicts 76's group-level noun promote (`value-13-third-arm`: "not available at battery grade"). Excluded.
- (c) 13 = nominal-closing suffix on "[97]-13" (the armA/armB sub-lexical shape): the SOLE surviving shape at @567 — admissible IFF 97 is nominal (`reseg-13-armB`: conditional admit; same "compatible-not-proven" standard as the arm-A legs; pattern support: "[X-noun]-13" at @139/@456/@1360 with registry nouns 65/35). But conditional on the unadjudicated INF/NOM tie, which is red-team venue (`redteam-97-tie-adjudication` delivered, decision pending) — admissible, not battery-grade licensed.
- (d) letter/syllable value for 13 at @567: no lane inventory evidence names one; the hapax trigram gives no recurrence for any multi-group unit.

**C4 verdict rule:** none of C1/C3 is licensed → the claim "name 13's class at @567" is **FENCED**. C2 stays dead by standing kill.

## Verdict: NULL (fence executed)

No arm names 13's class at @567 with byte evidence at battery grade. Post-nominal-adjective is excluded at this window under every live premise (both tie arms fail; rescues byte-unsupported). Word-final stays dead by standing kill (not re-litigated). Word-internal has only the tie-conditional suffix shape, which rides the unadjudicated INF/NOM tie (red-team venue) and is not battery-grade licensing. The joint test stays blocked on the tie; 13's class at @567 is fenced, not named.

## Scope

- Promotes nothing; kills nothing globally; downgrades nothing.
- Narrows (per-window): post-nominal-adjective-13 is excluded at @567 at kill grade (the uniform-adjective global kill already stands; this is its @567 instance). Word-final-13: standing kill adopted, not re-litigated. Word-internal-13: fenced pending the 97-tie adjudication; the "97-13" composition route stays red-team venue.
- No standing or red-team verdict contradicted or downgraded; §7 intact. Canonical-stream caveat stands (row a3_02 offsets unvalidated).

## Follow-ups proposed (for supervisor queuing; all ids verified ABSENT from battery-queue.json)

1. `joint-97-13-567` (P3, gated on the red-team's 97-tie adjudication). Claim: the 97-tie adjudication unblocks 13's class at @567. Bars: (a) if 97=NOM is ratified, test the "[97]-13" suffix segmentation on the armA/armB byte pattern — promote 13=suffix-class iff zero ungranted assumptions AND the 13→76 boundary is stated with standing values; (b) if 97=INF is ratified, kill the suffix shape at @567 (no nominal host) and confirm the adjective arm dead at kill grade → @567 permanently fenced. Evidence: this report + `reseg-13-armB` + `redteam-97-tie-adjudication`.
2. `disloc-76-45-94-frame` (P4). Claim: the @567 adjective rescue's missing license is tested lane-wide. Bars: census dislocation-shaped windows ("N 45/47 94") stream-wide — name ≥1 byte-evidenced "N, ce ne…" dislocation precedent, or fence the dislocation rescue permanently (this report: zero "X 47 94" windows; the only "N(noun-class) 45 94" is @568 itself).
3. `wordint-13-567-lettertier` (P4). Claim: the lane's letter/syllable tier can host a word-internal 13 at @567. Bars: name a letter/syllable value for 13 with battery-grade inventory evidence (cf. `syllable-08-letter-value`), or fence the letter-tier route at @567 permanently. Evidence: this report (hapax trigram; no multi-group recurrence).

Notes for the supervisor: `suffix-13-narrow` (armB's P4 recommendation, the 4 admitting windows @139/@456/@567/@1360) is already queued — not re-proposed. `reseg-13-rightward` already verdict/null. `les567-imperative` already verdict/kill (imperative-97 dead; its "97 nominal" premise is superseded by the live tie — red-team venue).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-13-567.md` (this file).
- Queue write: `val-13-567` → status `verdict`, result `null`, 2026-10-09 (pre-write assert: was queued/verdictless; temp-file + rename; JSON re-validated post-write; own entry only; no downgrade).
- Lock `locks/val-13-567.lock` created on start (2026-10-09T18:23:14Z), deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
