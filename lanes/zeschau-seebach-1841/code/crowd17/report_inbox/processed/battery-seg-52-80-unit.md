# Battery verdict: seg-52-80-unit — KILL

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"unit reading holds iff 52-80 parses as one infinitive with zero contradiction under standing values (cf. queued seg-52-86-unit for the @1738 window); else kill the unit reading with the failing clause stated"

**Numbered pass/fail clauses (restated before testing, not modified after):**

- **C1:** "52 80" at @1294/@1807 composes as one infinitive word (52 = prefix syllable) and the resulting window parse has zero contradiction under standing values.
- **C2 (adverse):** the A8 verb-frame grant survives; @1738 ("12 48 52 86", seg-52-86-unit's venue) untouched.

## Method

- Read BATTERY-PROTOCOL.md first. Lock `locks/seg-52-80-unit.lock` created on start (no prior/stale lock present), deleted on completion.
- Re-derived the repaired 1,847-pair / 96-type stream in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `repair_parse.py` (pair up from row offset, drop trailing odd digit). Verified: 1,847 pairs, 96 types.
- `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- Standing context adopted (not re-litigated): ne52inf-adverb NULL (2026-10-09) — the 'ne [52] [INF]' frame is real at all three windows (W1 @1294, W2 @1738, W3 @1807); 52 is negation-adverb-shaped with a {plus, jamais} tie; global uniformity needs a red-team §7 act. ne-94-right-context PROMOTE — @1293/@1806 (94's 0-based positions) are "unfenced — right neighbor value open", not clean verbal-negator; R17-001 (94='ne' STRONG LEAD) stands. A8 verb-frame grant (80/89, value open).

## Window-level evidence (byte-exact)

**Loci confirmed:** "94 52 80" occurs exactly **2× stream-wide** — 1-based @1294 (0-based @1293, row a7_03) and @1807 (0-based @1806, row a8_10). ±4 windows byte-identical except two slots:

- @1294: `68 00 11 | 17 84 59 35 | 94 52 80 | 04 62 16`
- @1807: `79 87 64 | 77 84 59 35 | 94 52 80 | 04 61 15`

i.e. `17/77 84 59 35 | 94 52 80 | 04 62/61`. Standing values: 84="on" (A15), 59="est" (provisional), 17="fois" (promoted), 77="le" (provisional), 94="ne" (STRONG LEAD), 52 open, 80 verb-frame (A8), 35 noun-class, 04/62/61 open. Surface under the lead reading: "fois/le on est [35] ne [52] [80] [04]…".

**52's distributional profile (n=27):** 12 distinct followers ({82×5, 37×4, 89×2, 38×2, 30×2, 80×2, then singletons}) and 12 distinct predecessors — a free word, anti-correlated with a bound prefix. "52 80" = exactly 2× (the two loci). The unit claim lives or dies on these two windows alone: zero repetition leverage, zero compositional evidence (no letter values for 52/80 spelling any French infinitive).

## Per-clause pass/fail

- **C1: FAIL at kill grade.** Under standing values, the unit reading dissolves the negation-adverb 52 that the standing battery analysis (ne52inf-adverb NULL) established as the live role inside the real 'ne [52] [INF]' frame, and leaves the only available parse: `35 | ne(94) | [52-80-INF] | 04` = **bare "ne" + infinitive**. Bare "ne [infinitive]" is ungrammatical in 1841 French (negation of an infinitive requires the forclusif: ne pas / ne plus / ne jamais / ne point / ne rien / ne guère). That is a contradiction under standing values. The only rescue — re-reading 94 at these windows as an infinitive-licensing particle — contradicts the standing battery analysis of these exact windows (94='ne' STRONG LEAD, frame real), i.e. it is not available "under standing values"; and no named French infinitive for "52-80" exists to license the composition in the first place.
- **C2: PASS.** Only @1294/@1807 tested; @1738 ("12 48 52 86") untouched — no duplication of seg-52-86-unit. The A8 verb-frame grant is untouched: 80's verb-frame role at its other windows stands, and the parent's 'ne [52-adv] [80-INF]' frame survives the unit reading's death.

## Verdict: KILL

The "52-80 as one infinitive (52 = prefix syllable)" reading is forced false at both loci: it dissolves the standing licensed frame and yields an ungrammatical construction. Failing clause: **grammaticality under standing values** — the unit reading produces bare "ne [infinitive]", which 1841 French does not license, and no rescue exists within standing values.

## Scope

Kills only the "52-80"-as-one-infinitive unit claim. 52's negation-adverb arm ({plus, jamais} tie) stays live in the ne-frames; 52's adjective arm stays live ("la [52]" ×3, "52 37" ×4); the §7 split tension for 52 stands as red-team venue (split-52-redteam, priority 2). ne52inf-adverb's NULL untouched; ne-94-right-context's PROMOTE untouched; A8 intact.

## Supervisor observations (not findings, no follow-ups per §4 — kills regenerate none)

1. A **non-infinitive** unit reading of "52-80" (e.g. an adverb word) was not tested — the claim and bar were infinitive-scoped. If ever revived, it must beat the standing 'ne [52-adv] [80-INF]' frame on the same bytes.
2. W4 of the parent battery ("12 48 52 86" @1738) remains seg-52-86-unit's venue; this verdict does not touch it.
