# CLOSER verdict — 87="ce" → **PROMOTED to CONFIRMED**

Worker: closer (crowd round 3, WO4). Code: `code/crowd3/closer.py` (deterministic;
reuses `crib_attack.load_pairs`). Numbers: `code/crowd3/closer_results.json`.
Corpora: Tocqueville t1+t2 (1835/1840, 214,861 words, attempt-3 tokenizer) as era
primary; Les Mis t1 (119,514 words) as the dialogue-register instrument for the
documented mixed-register checks. Les Mis is diagnostic only, not primary.

## Verdict

**87="ce" is PROMOTED from provisional to CONFIRMED.** It clears the bar with
three new legs beyond the old scorecard (two fully independent, one
conditional-coherence), survives an exhaustive vocabulary inversion in which it
is the only frequent word fitting its profile, and every named rival dies by
statistical margins — not band judgments. The one surviving weakness (the
cela-rate's dialogue-register tilt) is characterized, bounded, and consistent
with an independent register finding from round 2; it favors no rival.

## Cipher profile of 87 (recomputed from the pair stream)

n(87)=32, rank 16/96 (1-based), share 1.733%. Followers:
{11:7, 64:5, 46:3, 01:2, 77:2, 78:2, 83:2, then nine at 1}.
P(11|87)=7/32=0.2188, 95% CI [0.110,0.388]; P(64|87)=5/32=0.1562, CI
[0.069,0.318]; P(46|87)=3/32=0.0938, CI [0.032,0.242]. 14 distinct predecessors
(24×10, 29×3, 96×3, …). **87 is the #1 predecessor of 11=la** (7 vs 00:4, 06:4,
47:3, 67:3, 37:2). All three 87→46 bigrams have predecessor 96
(@pair indices in JSON): P(46|87,pre=96)=3/3 vs pre=24 0/10 — reframing
reproduced exactly.

## The steelman, rebuilt from scratch

1. **Triple signature.** 87's top-3 followers {11, 64, 46} = 15/32 occurrences
   (47%). Under "ce" they read {cela, ce qui, ce que} — all grammatical, and
   exactly the signature collocations of "ce". Era word-space rates:
   P(que|ce)=0.1076 ∈ cipher CI ✓; P(qui|ce)=0.1878 ∈ cipher CI ✓.
   Syllabary-aware model (denominator = ce-tokens + cela-tokens, the minimal
   assumption consistent with the observed follower set — no te/x spike from
   cette/ceux): era P(qui)=0.1803 (1.15×), P(que)=0.1033 (1.10×) ✓; cela leg
   0.0398 vs 0.2188 — the register gap (see caveat R1).
2. **de/à refutation stands.** 87→46=que ×3 makes "de que"/"à que"
   ungrammatical — recomputed, unchanged.
3. **96-frame.** 96-87-46 ×3 with 96="par" reads "parce que" (par+ce+que
   syllabified). Era: P(que∨qu | "parce")=132/132=**1.0000**; syllabic
   prediction P(87|96)=n(parce)/(n(par)+n(parce))=132/1168=0.1130 vs cipher
   3/21=0.1429 (**1.26×**). No rival is grammatical in a "par _ que" frame
   (era trigram counts all 0). Conditional on 96=par (leg N3, caveat noted).

## New leg N1 — the triple kills every rival statistically (independent)

Era rates for the six WO rivals vs the cipher's 95% CIs:

| rival | P(que\|R) era | in cipher CI [0.032,0.242]? | P(qui\|R) era | in cipher CI [0.069,0.318]? | triple grammar |
|---|---|---|---|---|---|
| se (n=1524) | 0.0000 | ✗ | 0.0000 | ✗ | se+la rare, se+que ✗, se+qui ✗ |
| ne (n=1793) | 0.0000 | ✗ | 0.0000 | ✗ | ne+la marginal, ne+que ✗, ne+qui ✗ |
| le (n=4570) | 0.0000 | ✗ | 0.0000 | ✗ | le+la ✗, le+que ✗, le+qui ✗ |
| je (n=669) | 0.0075 | ✗ (12.5×) | 0.0000 | ✗ | je+la ✓, je+que ✗, je+qui ✗ |
| on (n=1594) | 0.0038 | ✗ (25×) | 0.0000 | ✗ | on+la ✓, on+que ✗, on+qui ✗ |
| en (n=2714) | 0.0007 | ✗ (134×) | 0.0000 | ✗ | en+la rare, en+que ✗, en+qui ✗ |
| **ce (n=1134)** | **0.1076** | **✓** | **0.1878** | **✓** | **cela ✓, ce que ✓, ce qui ✓** |

The rival zeros are **register-independent**: "le qui", "se qui", "je que",
"on que" are ungrammatical in every register — these are count-zeros with
n≥669, not band judgments. Even dropping the provisional 64="qui" prong, the
{cela, ce que} pair alone kills all six rivals on counts. This is new: the old
scorecard never ran a rival battery beyond pour/sans/de/à and never tested the
triple jointly.

## New leg N2 — exhaustive 87-inversion (independent)

Swept the full era vocabulary (n≥20, ~4,000 words) for
{P(que|W)≈0.0938, P(qui|W)≈0.1562} within factor-2. **"ce" is the only word
with n>100 passing both legs** (overall #2 behind "puissances", n=23 — low-n
noise; then objets n=62, différences n=21, celles n=68, …). Under Les Mis,
"ce" is outright #1. The only other passer of note is **"celles" —
the ce-family**. No rival, no alternative function word, survives the sweep.
The la-leg was excluded from the sweep with a documented register caveat (see
R1); including it changes nothing about rival ranking.

## New leg N3 — 96-frame coherence (conditional on 96="par")

See steelman §3. Caveat: 96="par" was promoted using 87="ce" as one of its
legs, so this is mutual-support coherence, not fully independent evidence.
It still constrains the joint hypothesis tightly: the frame admits "ce" and
nothing else.

## Correction C1 — F19's "parce" rate was miscomputed (lane record fix)

F19/hypothesis-sweeper wrote era P(ce|par)=132/1036=0.1274 (1.12× vs cipher
3/21). **Wrong:** 132 is n("parce"), not the (par,ce) bigram count. True
word-space P(ce|par)=13/1036=**0.0125** — as stated it would be an 11.4× fail.
The syllabary-aware repair — P(87|96) predicted as
n(parce)/(n(par)+n(parce))=0.1130 vs cipher 0.1429 (**1.26×**) — restores the
leg and is strictly better than F19's number. The frame leg
P(que|parce)=1.0000 (que+qu pooled; raw que-only 0.3258) was and is correct.
96="par" keeps its CONFIRMED status; one of its four legs is now the repaired
version. (This correction also weakens nothing about 87: the frame reading
"parce que" requires 87="ce" regardless.)

## Residual caveat R1 — the cela register tilt (bounded, favors no rival)

Cipher P(11|87)=0.2188, CI [0.110,0.388]. Era syllabic prediction 0.018–0.040
(outside CI — a genuine era-fail, not hand-waving); Les Mis prediction
0.131–0.217 (inside CI). So R5005's ce-collocations tilt dialogue-register —
**independently corroborated** by the round-2 closer's "est ce" finding
(cipher 0.1923 sides with Les Mis 0.1177 over era 0.0099, an 11.9× gap).
This is a property of the text's register, and it discriminates against no
rival (all rivals fail the cela leg harder: "le la" impossible, "se la"
n=0, "je la" n=2, …). It does not threaten the promotion; it is recorded as
the precisely bounded residual.

## Inversion redo (c) — 24's intersection stays empty under mixed rates

Mixed-register model (documented): a word fits if it passes both legs under
**either** corpus (union). Legs: B*=P(ce|W)≈0.1923, C*=P(W|que,qu)≈0.1034.
Result: **intersection empty under era, empty under Les Mis, empty under the
union.** Near-misses: era top-B "tout" 0.1172 (fails C ~10×), top-C "il"
0.1045 (fails B); Les Mis top-B "est" 0.1177 (fails C 6.6×), "voici/voilà"
(fail C). With 87="ce" now confirmed rather than provisional, the updated
implication: 24's profile matches no French function word in either register —
24 is likely not a plain function word (or is split across groups). The empty
intersection no longer points at 87.

## What would falsify / fully close this

- Falsify: (a) a register-calibrated reference (1830s–40s ministerial
  despatches, not essays) showing cela-rates at Tocqueville levels; (b) any
  rival surviving the triple with non-zero qui/que follower rates; (c) 64≠qui
  removes the qui prong — but {cela, ce que} alone still kills all six rivals.
- Fully close: an independent second ce-collocation anchor (e.g. identifying
  the groups for "ci"/"te" to test ceci/cette spellings) or a
  register-matched corpus.

## Downstream consequences

- 64="qui": its check (b) (P(64|87)=0.1562 ≈ era P(qui|ce)=0.1878) no longer
  conditions on a provisional — the condition is now confirmed. Recommend
  re-promoting 64="qui" to CONFIRMED on the next pass.
- 96="par": keeps CONFIRMED (one leg repaired per C1, strictly stronger now).
- Drags using 87="ce" no longer inherit provisional uncertainty from this
  anchor. The 82↔87 Jaccard flag (87 patterns with 82=m) remains unexplained
  and is now the top open anomaly in 87's neighborhood.

## Files

- `code/crowd3/closer.py` — deterministic; reuses `crib_attack.load_pairs`
- `code/crowd3/closer_results.json` — all counts, rates, battery, inversions,
  Wilson CIs, verdict block
- `code/crowd3/report_inbox/closer-87ce-resolution.md` — report note
