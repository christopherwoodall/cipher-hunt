# Battery report: frame-76-67 — 67-76 x2 vs 67's positional rule

- Target id: `frame-76-67`
- Worker: subagent 678385fd-d9cf-4975-9ed8-112b7ec7017b
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
  canonical.py NOT used. R5005 NOT touched. All @-offsets are global pair
  indices on the repaired stream. No stale lock was present; lock created
  2026-10-09T08:35:55Z, deleted on completion.

## Sibling context (read first)

- battery-frame-76-tension.md (null, 2026-10-09): 76's noun-vs-verb fork
  stands. Verb-side legs: 94-76 x2 and 67-76 x2 (@200, @1046: "67 76" =
  "et/veut [76]", verb-shaped iff 67="veut"). The 'la [76]' bigram does not
  exist on the repaired stream.
- battery-frame-76-ne-94.md (null, 2026-10-09): "82 94 76" x2 fences the
  verb read with the reversed clitic order; 76's class stays open.
- battery-noun-76 (processed, null): read @1046 as row-boundary misread
  ("la" closes row a6_03; 67 opens a6_04) with 67="et" by the positional
  rule; read @200 as `et(67) [76-noun]. Cela(87-11)` or `veut(67)
  [76-noun]`, both branches clean. This battery adjudicates the 'veut'
  branch it left open.

## Bar (verbatim, pre-registered)

> "resolve iff 76 parses as infinitive-shaped after 67='veut' under the positional rule, or the windows are re-parsed with stated cause"

### Numbered clauses

1. 76 parses as infinitive-shaped after 67="veut" under the positional rule
   (67="veut" iff follower infinitive-shaped).
2. OR the two "67 76" windows are re-parsed with stated cause (i.e. a
   67="et" reading, grammatical and grounded, at each window).

Operational definition of "infinitive-shaped" (lane usage, not invented):
the follower feeds the [stem]-29-89 template ("[X]er [89]", 29="er"
pencil, 89 granted verb-frame) — the exact pattern under which the lane's
standing 'veut' readings of 67 resolve (see @272: `67 33 29 89 84` =
"veut [33]er [89]"; @1390: `67 86 29 89 16` = "veut [86]er [89]", per
battery-erstem-33-id). The follower otherwise carries infinitive markers
(76-29, 76-89) or sits in the granted verb inventory (85 stem, 80/89
frames).

## Method

Rebuilt the repaired parse in-session (1,847 pairs, 96 distinct groups;
n(67)=38, n(76)=21 — matches sibling censuses). Censused all 38 of 67's
windows (predecessor/successor contacts), both "67 76" windows with +-4
context, all X-29-89 infinitive templates on stream, 76's full successor
profile, and byte-level row boundaries at both windows. No polyvalence
declared (67 et/veut remains the sole true polyvalence per §7).

## Window-level evidence (@-offsets on the repaired stream)

The two "67 76" windows (67@199/76@200; 67@1045/76@1046):

- @199 (a2_00): `01 21 60 08 67 76 87 11 92` — `…[08] 67 76 87 11 92`
- @1045 (a6_04): `77 82 63 11 67 76 85 41 88` — row boundary between
  11@1044 (last pair of a6_03) and 67@1045 (first pair of a6_04),
  verified in-session from the repaired offsets; the "la" (11) closes
  the prior row's clause and is not a constituent of this window.

Infinitive-shaped test for 76:
- X-29-89 templates on stream: 5, distinct stems {08, 33, 86, 93}.
  76 is NOT among them. 76-29 x0, 76-89 x0.
- 76's 21-window successor profile: 47 x4, 42 x3, 49 x3, 45 x2, 87 x2,
  01 x2, 82/18/59/85/48 x1 each. Zero infinitive markers (29, 89);
  zero granted-verb contacts (94-80/89/85 were already x0; 76-85 x1
  is 76 PRECEDING 85 at @1046, not 76 as verb).
- 76 is not in the granted verb inventory (80/89 frames, 85 stem).

Lane-calibration check (the positional rule's 'veut' readings are real
and rare): the only 67 windows on stream whose follower feeds the
X-29-89 template are @272 (`67 33 29 89`) and @1390 (`67 86 29 89`) —
exactly the two windows prior batteries read as "veut [X]er". All other
67 followers (77 x6, 78 x4, 11 x4, 64 x2, 46 x2, 08 x2, singletons)
fail the template and resolve 67="et". The rule is discriminating, not
vacuous.

Per-window re-parses (stated cause = §7 positional rule; 76 fails the
infinitive-shaped test, so 67="et"):
- @199: `…[08] et(67) [76-noun]. ‖ Cela(87-11)…` — 87="ce" (A4) +
  11="la" (pencil) = "ce-la" template ("that"); noun coordination
  "et [76]" after [08], then a fresh "Cela…" clause. Grammatical,
  zero contradiction. The 'veut' rival is fenced: it requires 76
  infinitive-shaped, and the template census is negative.
- @1045: `‖ Et(67) [76-noun] [85-verb-stem] [41]…` — clause-initial
  "Et" after the row boundary, subject noun [76], verb stem 85 (A3),
  continuation [41]. "Et [noun] [verb]…" = subject+verb, fully
  grammatical. The 'la'+verb rival was already killed by
  battery-noun-76 ("la veut [76]" has no subject). The 'veut' rival
  is fenced by the same negative template census.

## Per-clause pass/fail

- Clause 1 (76 infinitive-shaped after 67="veut"): FAIL — not at kill
  grade against the fork, but as a positive claim it is unsupported:
  76 feeds no X-29-89 template, takes 29/89 zero times in 21 windows,
  and is outside the granted verb inventory. The positional rule's
  condition for 67="veut" is not met at either window.
- Clause 2 (windows re-parsed with stated cause): PASS at both
  windows. Each re-parses as 67="et" + [76-noun] under the standing
  positional rule, with full stated cause (row boundary at @1045;
  "ce-la" template at @199; negative infinitive census for 76).

Adverses: none listed.

## Verdict: promote

Rationale: the bar is a disjunction and its second disjunct passes
cleanly at both windows with stated cause. The adjudication is
bankable: at the two "67 76" windows, 67 resolves "et" (not "veut"),
and 76 fails every infinitive-shaped test the lane operationalizes.
This contradicts no standing red-team verdict (76's class fork stays
open; no standing value or class is assigned to 76, and 67's 'et' legs
were already read this way by battery-noun-76). No second polyvalence
declared per §7. The 'veut' rival for these two windows is fenced with
stated cause — it is not ignored, it is rejected by the distributional
test. Residual: 76's noun-vs-verb class fork remains red-team business
(tension F3, ne-94 F3 still open); this battery only closes the
67-specific fork.
