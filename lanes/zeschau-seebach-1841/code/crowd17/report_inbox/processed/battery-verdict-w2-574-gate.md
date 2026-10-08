# Battery report: verdict-w2-574-gate

Target: `verdict-w2-574-gate`. Claim: W2 @573 ('ce verdict [13-55-61] ne m'') is the flagship fork window; adjudicate it first when ver-78 resolves.
Date: 2026-10-08. Worker: 71de49fa-5eca-4026-8dbd-559e226b8312. No stale lock existed at start.

## Bar (verbatim, pre-registered)

"(a) decide by boundary evidence whether 78-45@573 is one word ('verdict') or two - state why the two-word parse is impossible under 78='ver'; (b) record whether 'ce [78] ce' survives at W2 under a non-ver 78 value, so the gate is useful even under a ver-78 kill"

## Bar restated as numbered pass/fail clauses

1. Clause (a) — decide by boundary evidence whether 78-45@573 is one word ('verdict') or two; state why the two-word parse is impossible under 78='ver'.
2. Clause (b) — record whether 'ce [78] ce' survives at W2 under a non-ver 78 value, so the gate is useful even under a ver-78 kill.

## Method

Repaired 1,847-pair stream only: `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`. `canonical.py` never used. No R5005, sealed gate, or red-team contact. All counts below trace to the stream.

Standing values used: banked 11=la, 82=m, 29=er, 40=e, 46=que; granted 87=ce, 64=qui, 96=par, 94=ne, 12=n, 48=e, 30=pas; A11 45='ce' HOLD; 78='ver' is LEAD only (ver-78 battery null, R16-005, not settled — not granted). The fork adjudication's what-if parses (report_inbox/processed/battery-fork-78-45-adjudication.md) supply the window inventory; every @-offset below is re-derived here.

## Window-level evidence (@-offsets are pair positions on the repaired stream)

W2 — 78@573 (row a3_02):
`... @568:76 @569:45 @570:94 @571:52 @572:87 | @573:78 @574:45 | @575:13 @576:55 @577:61 @578:94 @579:82 @580:06 @581:06 @582:50 ...`

Verified facts:
- 78-45 bigrams occur exactly 4x: 78@313, @573, @982, @1164 (45@314, @574, @983, @1165). n(45) = 22.
- Left of W2: 87@572 = 'ce' (granted). So the window opens "ce [78] [45] ...".
- Right of W2: 13-55-61 @575-577, then 94-82 @578-579 = 'ne m'' (94='ne' promoted, 82='m' banked; 94-82 bigram x4 stream-wide).
- 13-55-61 trigram occurs exactly 2x: @575 and @1166. Both have pre-context 78-45 (byte-identical 5-gram 78-45-13-55-61 @573/@1164). Zero occurrences elsewhere.
- 45's followers split by left context: post-78 = {13 x2, 01 x1, 64 x1}; standalone-45 (pre != 78) = {93 x3, 23 x3, 28 x2, 64 x2, 91, 54, 88, 46, 94, 08, 58, 36}. Followers 13 and 01 occur after 45 ONLY in post-78 context. The single shared follower is 64 (W1's A11 mirror leg vs @340/@1024).

## Per-clause pass/fail

1. Clause (a): PASS — 78-45@573 is one word; the two-word parse is impossible under 78='ver'.
   - One-word reading: 78='ver' + 45='dict' = 'verdict'. With 87='ce' before it: "ce verdict" (this verdict). Canonical French NP. The right edge parses: "[13-55-61] ne m'[06][06]" — the 'ne m'' elision frame is clean under the dict reading. The 13-55-61 exclusivity (2/2 after 78-45, 0 elsewhere) and the disjoint post-78 follower set ({13, 01} exclusive) are the boundary evidence: 45 after 78 behaves word-internally, not word-initially.
   - Two-word reading under 78='ver': 78 as a free morpheme + 45 as a separate word. 45's only live standalone value is 'ce' (A11 HOLD; 'dict' is syllabic and cannot stand alone). The parse would be "ce(87) ver(78) ce(45) [13-55-61] ne m'...". As a French free word, "ver" exists only as the noun "ver" (worm, masculine). "ce ver" is grammatical alone; "ce ver ce" — demonstrative doubling — is impossible French. There is no verb "ver", no adjective "ver", no preposition "ver". The 78='ver' hypothesis is itself syllabic ('ver'+'dict'), so promoting 78 to a free word already breaks the hypothesis; even granting it, the only available word reading fails grammar. Therefore the two-word parse is impossible under 78='ver'. One word is forced.
2. Clause (b): PASS — 'ce [78] ce' does NOT survive at W2 under any non-ver 78 value. The gate is useful even under a ver-78 kill.
   - The two-word reading at W2 is "87(=ce) | 78=X | 45(=ce) | 13-55-61 | 94(=ne) 82(=m') ..." for X in any class:
     - X noun: "ce [noun] ce" — demonstrative doubling, ungrammatical, no exceptions.
     - X finite verb: 87='ce' cannot govern a finite verb; "ce" as subject pairs only with etre ("c'est / ce sont"), and 45='ce' cannot follow as a direct object (French "ce" is never a COD pronoun).
     - X infinitive: the archaic "ce faire"-type admits no trailing second "ce".
     - X adjective/adverb/preposition: "ce [X] ce" ungrammatical.
     - 45='ce' as relative-pronoun head ("ce que / ce qui"): falsified — 13-55-61 follows, not "que"/"qui" (46='que' banked elsewhere).
   - So the two-word parse fails for every X, independent of 78's value. The W2 boundary decision (one word) holds whether ver-78 promotes, kills, or stays null. Under a ver-78 kill, dict-45's fork arm dies with its syllabic host (fork-rerun bar (b) already charters that), but the one-word boundary at W2 stands with 78-45's value open — the gate's adjudication survives the kill it was built for.

## Adverses answered

- "A11 HOLD" — answered, fenced with stated cause. W2 (@574) is excluded from 45='ce' scope: kill-scope 1/22 windows. A11's HOLD stands on the remaining 21 windows (@340/@1024 mirror legs and the rest). This gate neither overturns the A11 verdict (a HOLD, not a grant) nor touches its other legs; the scoping matches the fork-rerun battery's chartered k/22 accounting. Note: W2 was never an A11 mirror leg (ce-45-mirror2 found no second mirror frame-type), so no mirror leg is lost.
- "W1 ambiguity" — fenced. @313's 45-64 is A11's own mirror leg, shared with standalone 45-64 @340/@1024; W1 stays ambiguous and stays owned by dict-78-45-wordbound and w1-314-ambig. This gate does not touch W1.
- "R-pos needs red-team declaration" — answered. This gate declares NO positional rule for 45 and no polyvalence. It adjudicates only W2's boundary. The R-pos declaration request from the fork battery stands escalated to the red team per protocol §7 (67 et/veut is the sole true polyvalence).

## Verdict: promote

Both bar clauses pass on re-derived stream evidence. All three adverses are answered or fenced with stated cause. No standing red-team verdict is contradicted: A11 HOLD preserved at 21/22, ver-78's R16-005 LEAD untouched, @296's red-team fence untouched.

Gate deliverable (the adjudication the supervisor can use immediately, before and after ver-78 resolves):
- W2 @573: 78-45 is ONE word. The two-word parse is impossible under 78='ver' (clause a) and impossible under every non-ver 78 value (clause b). The decision is ver-78-independent.
- Under 78='ver' (LEAD, unsettled): the one word reads 'verdict', giving "ce verdict [13-55-61] ne m'...". This gate does NOT promote 78='ver'; the value reading stays conditional on the unsettled LEAD.
- Kill-scope for 45='ce': exactly 1/22 windows (@574). The remaining 21 keep A11's HOLD.
- Fork-routing consequence: fork-78-45-rerun's clause (a) can consume W2 as settled (45='ce' killed at @574 if ver-78 promotes); clause (b) (ver-78 kill) keeps W2's boundary while dropping the 'verdict' value.
