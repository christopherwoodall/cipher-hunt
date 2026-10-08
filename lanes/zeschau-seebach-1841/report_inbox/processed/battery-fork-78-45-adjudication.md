# Battery report: fork-78-45-adjudication

Target: `fork-78-45-adjudication`. Claim: 78-45 x4 contact adjudicates 45='ce' HOLD vs 45='dict' rival.
Date: 2026-10-08. Worker: eb6b1d3e-2994-4107-8600-1d91edd73cb5. No stale lock existed at start.

## Bar (verbatim, pre-registered)

"(a) run joint with ver-78: if 78='ver' promotes, the four windows (@314, @574, @983, @1165) must read 'verdict...' (45='dict' at minimum at these windows) or 45='ce' is killed at 4/22 windows; (b) state any positional rule that lets both claims survive, with per-window parses"

## Bar restated as numbered pass/fail clauses

1. Clause (a) — joint-with-ver-78 conditional: IF 78='ver' promotes, THEN the four 78-45 windows (45@314, @574, @983, @1165) must read 'verdict...' (45='dict' at minimum at these windows); ELSE 45='ce' is killed at 4/22 windows.
2. Clause (b) — state any positional rule that lets both claims (45='ce' HOLD, 45='dict' rival) survive, with per-window parses for all four windows.

## Method

Repaired 1,847-pair stream only: `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`. `canonical.py` never used. No R5005, sealed gate, or red-team contact. All counts below trace to the stream.

Located every 78-45 bigram: 78@313, 78@573, 78@982, 78@1164 (45@314, @574, @983, @1165). Count = 4, offsets match the bar. n(45) = 22. 45's top predecessor is 78 (4/22). 'ce verdict' x2 confirmed: 87@572 before 78@573, and 47@981 before 78@982 (47='ce' allophone tier, granted A4). The 5-gram 78-45-13-55-61 occurs x2 (78@573, 78@1164), byte-identical.

Standing values used: banked 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que; granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce (allophone), 94=ne, 12=n, 48=e (letters), 30=pas, 39=a/a; provisional 59=est, 77=le; A1 32 predicative; A11 45='ce' HOLD; 78='ver' is LEAD only (ver-78 battery null, R16-005, not settled — not granted).

## Window-level evidence (@-offsets are the 78 position; 45 = 78+1)

W1 — 78@313 (row a2_04): `... 20 17 46 84 24 37 | 78 45 | 64 59 32 94 06 11 92 ...`
W2 — 78@573 (row a3_02): `... 76 45 94 52 87 | 78 45 | 13 55 61 94 82 06 06 50 ...`
W3 — 78@982 (row a6_01): `... 92 07 76 47 | 78 45 | 01 24 89 48 01 76 49 ...`
W4 — 78@1164 (row a6_09): `... 80 17 77 82 44 83 21 67 | 78 45 | 13 55 61 94 87 83 21 ...`

Distributional facts: 45->13 occurs ONLY after 78 (x2, both = 13-55-61); 45->01 occurs only after 78 (x1, W3); 45-64 x3 = @314 (W1), @340, @1024 — the A11 mirror legs; 13-55-61 never follows standalone 45.

## Per-window parses

- W1 @313: under 45='ce': "...on [24] [37] ce qui est [32] ne [06] la..." — clean. 45-64 = 'ce qui' (A11 mirror leg), 59='est' provisional, 32 predicative granted (A1). Under what-if 78='ver'+45='dict': "...[37] verdict qui est [32]..." — also grammatical ('verdict' + relative clause). AMBIGUOUS — does not discriminate. This is the fork's crux: A11's own mirror leg is a fork window.
- W2 @573: under 45='ce': "ce [78] ce [13-55-61] ne m'[06][06]..." — 'ce X ce' strained (78 unvalued, so not kill-grade). Under what-if: "ce verdict [13-55-61] ne m'[06][06]..." — clean (94-82 = 'ne m'' elision frame; 94='ne', 82='m' banked). Favors dict under the what-if.
- W3 @982: under 45='ce': "ce [78] ce [01] en [89]..." — strained. Under what-if: "ce verdict [01]..." — clean. Favors dict under the what-if.
- W4 @1164: under 45='ce': "[67] [78] ce [13-55-61] ne ce [83]..." — needs 78 noun-shaped; 67='et' (follower not infinitive-shaped, per 67 positional rule). Under what-if: "et verdict [13-55-61] ne ce [83]..." — 'verdict' supplies the noun; 94-87 = 'ne ce' + unvalued 83 fenced. Partial; both readings need 78 noun-valued, dict supplies it.

## Per-clause pass/fail

1. Clause (a): VACUOUS — antecedent false. ver-78's verdict is null (2026-10-08); red-team R16-005 graded 78='ver' LEAD, not settled; @296 stands as red-team-fenced residual. 78='ver' did NOT promote. Therefore: 45='ce' is NOT killed at 4/22 windows; 45='dict' is NOT promoted; the fork stays open. The what-if parses above are recorded for the rerun.
2. Clause (b): PASS (rule stated). Positional rule R-pos: 45='dict' iff immediately preceded by 78 (word-internal syllable of the single word 'verdict'); otherwise 45='ce' (standalone word). Per-window under R-pos: W1 'verdict qui est [32]'; W2 'ce verdict [13-55-61] ne m'[06][06]...'; W3 'ce verdict [01]...'; W4 'et verdict [13-55-61] ne ce [83]...'. Caveats: (i) R-pos is a positional assignment for 45, and per protocol §7 (67 et/veut is the sole true polyvalence) only the red team may declare it — escalated, not adopted here; (ii) R-pos demotes A11's @314 mirror leg (cost recorded); (iii) alternative framing is analytic/syllabic duality (n-e-12-48 precedent): 78-45 as one word 'verdict' (two syllables) vs 45='ce' as a word — a word-boundary question, not a value question. Boundary evidence: 13-55-61 follows 45 only after 78. Adverse to the boundary: W1's 45-64 follower is shared with standalone 45-64 @340/@1024.

## Adverses answered

- "78='ver' queued not granted" — answered: ver-78 verdict = null, 78='ver' is LEAD per R16-005, not granted; clause (a) antecedent false, recorded, not ignored.
- "45='ce' is a HOLD" — answered: A11 HOLD stands; this battery neither kills nor promotes around it; R-pos not declared.
- "joint with ver-78" — answered: ver-78 result imported (null/LEAD, @296 red-team-fenced); this battery's conditional outcome is keyed to ver-78's future resolution.

## Verdict: null

Headline: the fork cannot adjudicate while ver-78 is unsettled. Clause (a)'s condition (78='ver' promotes) did not occur, so no kill fires; the surviving positional rule (R-pos) needs red-team declaration per §7. No contradiction with any standing red-team verdict (A11 HOLD untouched, R16-005 LEAD untouched) — nothing to escalate beyond the §7 declaration request.

## Follow-up targets (null regenerates work)

1. fork-78-45-rerun (priority 1). Claim: re-run this fork battery once ver-78 resolves. Bars: (a) if ver-78 promotes 78='ver', test the four windows for 'verdict...' reads; kill 45='ce' at exactly the windows that force it and record kill scope as k/22; (b) if ver-78 kills 78='ver', 45='dict' loses its syllabic host — kill dict-45's fork arm. Evidence: this report (what-if parses for all four windows). Adverses: R16-005 LEAD grading; A11 HOLD; W1 ambiguity.
2. dict-78-45-wordbound (priority 2). Claim: 78-45 is one word ('verdict') iff the boundary holds. Bars: (a) decide by contact profile: 45's post-78 followers {64, 13, 01} plus byte-identical 78-45-13-55-61 x2 vs standalone-45 followers {93x3, 23x3, 28x2, 64x2, 91, 54, 88, 46, 94}; (b) adjudicate W1's shared 45-64 follower adverse — if the boundary holds at W2–W4 but W1 parses two-word, record W1 as exception with stated cause. Evidence: 13-55-61 follows 45 only after 78; 01 follows 45 only at W3. Adverses: W1's 45-64-59-32 = A11 mirror leg shared with @340/@1024; demoting it costs A11 one leg.
3. w1-314-ambig (priority 2). Claim: W1 alone decides the fork's hardest window. Bars: parse the 84-24-37-78 left context of 78@313; if 37-78 is word-internal, dict wins W1; if 37 closes a clause (predicative 37 granted A1), ce wins. Evidence: full window 84-24-37-78-45-64-59-32. Adverses: 24 unvalued; 37's value unnamed (frame-37-reexam queued).
