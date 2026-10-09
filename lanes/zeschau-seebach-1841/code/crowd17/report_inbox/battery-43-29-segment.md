# Battery verdict: 43-29-segment — the 43-29 boundary at @21

- Target: `43-29-segment`
- Claim: @21 'qui vient me [43]er' segments as word-internal '[43]er' infinitive, which would make 43 verb-stem-shaped and re-open the noun hypothesis
- Worker: battery-worker 43-29-segment (b94ccb0a-52eb-451c-b1b3-0ab359d45e0e)
- Date: 2026-10-09
- Verdict: **PROMOTE** (segmentation only — 43 is NOT re-named at battery level; the polyvalence question is escalated to the red team per the bar)

## 1. Bar (verbatim from battery-queue.json)

"decide the 43-29 boundary at @21 (word-internal vs word boundary) using 43's other 15 windows and 29's distribution; if word-internal, escalate the noun-43 hypothesis to the red team; do not re-name 43 at battery level"

Numbered clauses:
1. The 43-29 boundary at @21 is decided (word-internal vs word boundary), using 43's other 15 windows and 29's distribution.
2. If word-internal, the noun-43 hypothesis is escalated to the red team.
3. 43 is not re-named at battery level.

## 2. Method

- Stream: repaired 1,847-pair parse only (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, upstream tokenization `[s[i:i+2] for i in range(o, len(s)-1, 2)]`). Verified 1,847 pairs / 96 types. `canonical.py` never used. R5005 untouched. No invented numbers.
- Standing values used as given (protocol §7): 29='er' (banked GT), 64='qui', 98='vient' (battery-promoted, re-verified frames adopted), 82='m', 47='ce', 96='par', 11='la', 84='on'.
- Full censuses re-derived: 43 n=16 (@21/@43/@244/@258/@343/@386/@439/@563/@1027/@1092/@1126/@1204/@1303/@1305/@1544/@1724); 29 n=45 with full predecessor/successor distributions.
- The @21 window (0-based pair offsets): `17 64 98 82 43 29 47` @17–23 = '[17] qui vient me [43]er ce'. (Prior batteries anchor the same window at 98=@19; identical bytes.)

## 3. Window-level evidence

### 3a. 29's distribution (n=45)

Predecessors: 33 x5, 86 x4, 06 x4 (verb-stem/verbal cluster: 13/45 — the A10 `33+29` infinitive hold, `86-29`='voir' x4), 34 x3 (letter, 'première'), 64 x3, 03 x3, 11 x2, 46 x2, 48 x2, 43 x1, 93 x1, 84 x1.
Successors: 40 x9 (word-internal '-ere': '34 29 40'='ière' @62/@685, '82 34 29 40'='mière' @758/@1038), then word-starts 89 x5, 47 x4 ('ce'), 80 x4, 42 x3, 85 x3, 87 x3, 82 x3 — i.e. 29 is word-FINAL (infinitive '-er') before new words in the large majority.

The word-initial reading of 29 is real but narrow: @147 `77 84 29 87 64` = 'le on erre ce qui' ("l'on erre") — 29='erre' after standalone 84='on'. So a 43|29 word boundary is *distributionally* possible in principle.

### 3b. The @21 junction under both segmentations

Word-internal (`[43]er` one word): `64 98 82 43 29` = 'qui vient me [43]er' — the 'venir + me + INF' frame ('il vient me voir'), fully grammatical. Requires 43 verb-stem-shaped.

Word boundary (`[43] | erre`): 'qui vient me [43] erre ce [33]' — fails at kill grade:
- 'erre' (errer) is intransitive and needs a subject; 'me [43]' supplies none.
- 'erre ce' is impossible (errer takes no direct object).
- No other French 'er'-initial word fits: 47='ce' follows 29 immediately, ruling out 'erreur' and friends; no standalone 'er' word exists.
The boundary reading was the only live alternative (given the @147 'erre' precedent) and it is ungrammatical. **Boundary killed; word-internal stands.**

(The only other conceivable re-segmentation, boundary at 82|43 with '82 43 29'='m[43]er' one word, would make 43='esur'-shaped — dead on 43's noun legs, §3c.)

### 3c. 43's other 15 windows: noun-shaped, byte-exact

- 'par 43' x2: @342–343 (`64 96 43 87`), @1026–1027 (`64 96 43 87`) — 'par' + bare verb stem is ungrammatical; noun frame.
- 'la 52 37 43' x2: @1123–1126, @1721–1724 — feminine article + adjective + verb stem is ungrammatical; noun frame.
- '43 vient' x2 (subject position): @439 (`45 46 43 98 80`='que [43] vient [80]'), @1724 (`43 98 39`='[43] vient à [88]') — verb stem cannot be the subject of 'vient'.
- 'la [43]' @563 (`59 30 67 11 43 24`='est pas et la [43] [24]') — article + noun.
- 43's successor distribution: 00 x3, 77 x2, 87 x2, 98 x2, 81, 91, 24, 07, 55, 21 — all word-starts; **29 x1 (@21) is the sole verbal-ending adjacency in 16 windows**. In 15/16 windows 43 is word-final in noun slots.

A monovalent verb-stem 43 is therefore dead: the noun legs forbid it. The @21 word-internal reading makes 43 verb-stem-shaped **at that window only** — the exact signature of conditioned polyvalence, which is a red-team act under §7 (67 et/veut stays the sole true polyvalence until the red team rules).

## 4. Per-clause pass/fail

1. **PASS.** Boundary decided: word-internal. Decided on (a) 29's distribution — its word-initial 'erre' reading is real (@147) but ungrammatical at @21 ('erre' needs a subject; 'erre ce' impossible), while its dominant word-final '-er' infinitive role fits the grammatical 'vient me + INF' frame; and (b) 43's other 15 windows — noun-exclusive, so the verb-stem shape is isolated to @21 rather than systematic.
2. **PASS (executed).** The noun-43 hypothesis is escalated to the red team via follow-up `redteam-43-polyvalence` below (P1): either 43 is polyvalent (noun + verb-stem) or the red team re-analyzes @21. Battery does not declare.
3. **PASS.** 43 is not re-named: no value is assigned to 43 anywhere in this report.

## 5. Adverses answered

1. "43's noun legs ('la [52] [37] 43' x2, 'par 43' x2)" → ANSWERED and ADOPTED: re-derived byte-exactly (§3c) plus '43 vient' x2 and 'la [43]' @563. They are not contradicted by the segmentation — they are the *reason* this is an escalation rather than a battery re-naming. The noun legs stand intact.
2. "Protocol §7 67-sole-polyvalence" → HONORED: no second polyvalence is declared at battery level. The word-internal finding *creates* the polyvalence question; the red team owns the answer.

## 6. Verdict: PROMOTE (segmentation claim)

The claim's segmentation mechanism is confirmed: @21 '43 29' is word-internal '[43]er', an infinitive in the 'vient me + INF' frame. Scope is fenced explicitly: this promotes the *segmentation*, not a value for 43. 43 keeps its noun standing in 15/16 windows; the @21 verb-stem shape is escalated, not banked.

## 7. Follow-up targets (escalation — the bar's clause 2)

F1. id: `redteam-43-polyvalence` | priority: 1
claim: "Adjudicate 43: noun-43 (15 windows: 'par 43' x2, 'la 52 37 43' x2, '43 vient' x2, 'la 43' @563) against the @21 word-internal '[43]er' infinitive leg — declare polyvalence (noun + verb-stem), re-segment @21 with a grammatical alternative, or fence @21 with cause"
bars: "rule iff (a) the noun legs are confirmed or overturned on bytes, and (b) the @21 '[43]er' infinitive is either accepted as a second 43 value (polyvalence declaration, red-team act) or re-segmented grammatically; battery may not declare"
evidence: "this report: 43 n=16 census, 29 n=45 distribution, @21 '64 98 82 43 29 47'='qui vient me [43]er ce'; boundary rival ('erre') killed grammatically; 29's sole verb-stem predecessor among noun-shaped 43 windows"
adverses: "§7 67-sole-polyvalence; noun-43 legs stand until overturned; 'ce [33]' tail at @21 unparsed (out of scope)"
