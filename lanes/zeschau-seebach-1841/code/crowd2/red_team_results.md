# Red Team — crowd round 2 (2026-10-07)

Executor: RED TEAM (kill authority over new CONFIRMED claims). Every cipher
count re-derived from `load_pairs()`; every era rate re-derived from the
Tocqueville corpus with attempt-3's tokenizer. Numbers: `red_team_results.json`;
code: `red_team.py`.

## Verdicts

| Claim | Verdict |
|---|---|
| H1 24="est" (the Closer) | **DEMOTE** — refuted as a 4-check confirmation case (R1–R5 below). Remains a weak open hypothesis. |
| F9 64="qui" | **DEMOTE** — CONFIRMED 4/4 → PROVISIONAL (R1–R4 below). "qui" stays the best single reading; it is not identified. |
| H5 77-78-94-82-06 = "J'ai l'honneur de" | **KILL** (K1, K2 below). |
| Factor-2 era-rate methodology | **UNCALIBRATED** — never validated; verdicts flip with corpus choice (B1–B5 below). |
| F13 "24-87-46 0/10 joint contradiction" | **DISSOLVED** — era-matched binomial P(0/10)=0.247, not significant. |

Nothing promoted (standing rule).

## H1: 24="est" — re-derivation of the 4 checks, era-matched

The surgeon's checks 2–4 were scored on Les Mis (1862 novel) rates. The lane
standard since attempt 3 is the era corpus (Tocqueville 1835/1840, 214,861
words). Re-scored:

| # | Check (surgeon) | Era-matched result |
|---|---|---|
| 1 | rank "1", freq 52, top band | 24 is **rank 2** (freq 52; rank 1 is 00 at 54). Era rank("est")=15, rank("en")=11, rank("de")=1. Top-band, but the "rank-1" label is factually wrong. |
| 2 | P(87\|24)=10/52=0.192, 11× over base | Reproduces (0.1923 vs base 0.0173). The enrichment is real. |
| 3 | Les Mis P(ce\|est)=0.118 within 2× of 0.192 | **FAILS 19.4×**: era P(ce\|est)=23/2331=**0.0099** ("est-ce" interrogative). Band allows 2×. The PASS was a corpus artifact — Les Mis dialogue "est-ce que" vs despatch prose is a **12× register gap**. |
| 4 | 46→24 ×3 = "qu'est" elision, PASS | **Never rate-checked; fails 31×**: era P(est\|qu')=7/2150=**0.0033** vs cipher P(24\|46)=3/29=**0.1034**. |

Numbered refutations:

- **R1 (check 3, era-matched):** observed/cipher 0.1923 vs era 0.0099 = 19.4× over; factor-2 band violated by an order of magnitude. The confirmation case's central rate leg does not survive the lane's own era standard.
- **R2 (check 4, rate it):** "qu'est" was asserted as grammar, never measured. Era P(est|qu')=0.0033 vs cipher 0.1034 = 31× over. As a rate check it fails; as pure grammar it is non-discriminating (46-24 is equally "qu'en" under the en-rival).
- **R3 (internal inconsistency on elisions):** check 4 assumes the encoder splits elided forms (46-24 = "qu'est", i.e. 46 covers elided "qu'"). Under that assumption "c'est" = 87-24 should occur at era P(est|c')=361/395=**0.914** → expected ~29 of 32, observed **0** (binomial ≈ 1e-34). The hypothesis cannot use split-elisions for check 4 while needing unsplit-elisions to excuse 87→24=0. Either branch damages H1: split → 87→24=0 kills it; unsplit → check 4 is void (and the lane has never established which branch holds — uncalibrated assumption).
- **R4 (the "est cela" anomaly is a refutation, not a lean):** cipher 24-87-11 ×3 ("est cela" under H1); era n("est","cela")=**0** in 214,861 words. Under the lane's factor-2 methodology this is an infinite-ratio deviation. "Anomaly unresolved; est kept as the lean" is special pleading — the methodology gives no procedure for keeping a lean against its own failed check.
- **R5 (check 1 misstates rank):** 24 is rank 2, not rank 1 (00 leads at 54). Minor, but the "rank-1 band" phrasing is wrong and 00 (rank 1, 54×) is itself unidentified — the top of the frequency table is unread.

Rival sweep (all fail too — the problem is structural):
- 24="en": era P(ce|en)=0.0074 → 26× over. ("qu'en": P(en|qu')=0.0507 vs 0.1034 = 2.03× — just outside the band; "en cela": era n=3, P=0.0011 vs cipher 0.058 = 53× over.)
- 24="de": era P(ce|de)=0.0167 → 11.5× over.
- 24="tout" (the only era word with n≥50 and P(ce|X) in-band, 0.1172): refuted — era rank 76 / share 16× below cipher 24's; era P(tout|que)=0.0056 vs cipher P(24|46)=0.103 (18×).
- Net: **no era French word explains P(87|24)=0.192 under 87="ce"**. The 11× enrichment is a real lead, but under the provisional 87="ce" it has no word-level reading. H1 is demoted to weak open hypothesis, not promotable.

## F9: 64="qui" — adversarial treatment

Re-derivation: rank(64)=5 (ties 06 at 46; "rank 4" depends on tie-break),
P(64|87)=5/32=0.1562, 46→64=0, P(87|64)=5/46=0.1087, spread 28/28 distinct,
top share 0.065.

- **R1 (dependency):** check (b) — the identifying leg — conditions on 87="ce", which is provisional (F6: best-tested reading, cela-leg register-dependent). A CONFIRMED verdict cannot be grounded on a provisional premise. 64="qui" is at best provisional-given-provisional.
- **R2 (non-identification):** the factor-2 band [0.078, 0.313] around 0.1562 admits **three** era readings: "qui" 0.1878 (ratio 0.83), **"qu'" (elided que) 0.1041 (ratio 1.50)**, **"n'" (elided ne) 0.0794 (ratio 1.97 — at the band edge)**. The methodology does not select "qui". ("qu'" would be a homophone of ground-truth 46=que — the lane assumes injectivity without establishing it.)
- **R3 (check (d) is weak, check (a) is qualitative):** the spread statistic matches any free function word — ground-truth 11=la shows the same profile (29 distinct / 0.091). It is a weak pass, not an identifying check. On shares (stricter than the rank-band hand-wave): cipher 64 = 2.49% vs era "qui" = 1.10% → 2.27×, outside a strict factor-2 share reading.
- **R4 (rival framing corrected):** P(87|64)=0.1087 vs era P(ce-precedes-qui)=213/2360=0.0903 → ratio 1.20, in-band. This is a weak PASS for "qui", but attempt-3's "disfavours ci" overclaimed: it refutes only the narrow "64 exists solely to spell ceci" sub-reading; "ci"-as-syllable is uncomputable without syllabification. The negative control (46→64=0) is consistent with all three survivors ("que qui"/"que qu'"/"que n'" all ≈ 0 in era prose), so it does not discriminate either.

Verdict: **DEMOTE to PROVISIONAL**. "qui" remains the best single reading (closest rate, #1 era follower of "ce", clean negative control), but CONFIRMED 4/4 is unsound.

## H5: "J'ai l'honneur de" — KILL

- **K1 (frequency premise void):** the hypothesis was built on the ×5 count ("repeated once per subject paragraph"). Pair-aligned count is **×2** (@1179, @1350; F3, formula-hunter re-verified). The premise is corrected out from under it.
- **K2 (ground-truth contradiction):** position 4 of 77-78-94-82-06 is **82 = "m" (pencil-crib ground truth)**; "j'ai·l'·hon·**neur**·de" requires "neur" there. Direct contradiction with ground truth. Direction-independent (reversed reading is nonsense).
- Supporting: formula-hunter N2 — no salutation-length repeat in the opening 100 groups. (H3 06="ne" would conflict with position-5 "de", but H3 is hypothesis-only; K1+K2 suffice.)

## Methodology audit: the factor-2 band (task item c)

- **B1 (never calibrated):** the sole testable ground-truth bigram (46=que → 11=la): cipher 1/29=0.0345 vs era P(la|que)=0.1174 — point estimate fails the band (ratio 0.29), but Wilson 95% CI [0.006, 0.175] covers the band edge 0.059. **Inconclusive at n=29** — i.e., the band is unvalidated, not validated. No false-positive rate has ever been measured.
- **B2 (no CONFIRMED claim sits at the band edge):** edge-distances (min ratio to either edge): 87=ce 1.74, 64=qui 1.66. But the **n' rival for 64 sits at 1.02** — survival vs death is decided by 0.03 of ratio. The band's arbitrariness is load-bearing.
- **B3 (verdicts flip with corpus choice):** the cela-leg needs half-width 0.79 on Les Mis vs **5.28** on era prose. Register gaps exceed the band itself: "est-ce" 12×, "cela" 6.7× between the two corpora the lane has used.
- **B4 (admits non-identification):** 64's band admits three readings (R2 above). The band can confirm "X follows ce at a plausible rate" but not "X = qui".
- **B5 (elision blindness):** the tokenizer erases c'/qu'/l'/d' distinctions ("c'est"→c+est, "qu'est"→qu+est). Checks involving elided forms (c'est, qu'est, qu'en) are unrateable or misrated as currently computed — a systematic gap for a syllabary whose elision handling was never established (see R3).

## F13 reassessed: the "joint contradiction" dissolves era-matched

24-87-46 = 0/10. Era: n("est","ce","que")=3, n("est","ce")=23 → P=0.1304 →
binomial P(0/10)=**0.247**. Not significant. The predecessor's p=9.1e-04 used
Les Mis rates; era-matched, there is no contradiction — with or without 87=ce
being provisional. (Under 24="en" the 0× is exactly predicted: era
n("en","ce","que")=0.)

## Surviving residue (leads, not claims)

- P(87|24)=0.192 vs base 0.017 (11×) is real and unexplained at word level under 87="ce". Either 87≠"ce" or 24 is not a plain French word in that slot.
- Group 00 (rank 1, 54×) is unidentified — the top of the table is unread, which should temper all rank-band arguments.
- 64's follower/predecessor lists are recorded in JSON for the next worker; "qui"/"qu'"/"n'" need anchor-dense windows to separate.

## Caveats (not verified)

- Elision handling of the cipher is uncalibrated (R3's two branches); no independent test exists yet.
- Injectivity (one group = one value, no homophones) is assumed, not established — the "qu'"/46=que overlap is the concrete risk.
- Era corpus is Tocqueville (political essay), not diplomatic despatches — a residual register gap the linguist flagged; Meisel 1826 diplomatic corpus exists but was not rate-extracted.
- Ground-truth calibration is n=1 pair (la/que); syllable anchors (pre, m, i, er, e) are not word-level testable.
- 87=ce itself remains provisional (F6); everything conditioned on it inherits that status.
