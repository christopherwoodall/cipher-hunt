# Battery report: stem-44-1839 — "44's morphological status at @1838–1840: word-internal stem vs whole-word nominal head"

- Worker: battery worker stem-44-1839, session 4aba9700-307a-43cb-a7f1-c809e26fce62
- Date: 2026-10-08 (lock created 2026-10-09T01:19:42Z; no prior lock found, none stale)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py). canonical.py NOT used. R5005 untouched. Red-team adjudication queue untouched. All @-offsets are repaired-stream indices, re-derived in-work.

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"resolve iff 44 at @1839 is decided stem-vs-whole with the '42 44' contact explained; do not name a global value; do not re-litigate @1714"

Numbered clauses (frozen before testing):
1. 44 at @1839 is decided: word-internal stem vs whole-word nominal head — one reading established on window evidence, the other excluded.
2. The '42 44' contact is explained (composition vs two tokens, with evidence from both occurrences).
3. (Adverse) No global value is named for 44.
4. (Adverse) @1714 is not re-litigated.

## Method

Re-parsed the repaired stream in-work: 1,847 pairs, 96 distinct, n(44)=15 at [208, 249, 527, 540, 797, 800, 1070, 1160, 1311, 1583, 1603, 1618, 1679, 1714, 1839] (byte-identical to noun-44's and stem-44-nominal's re-parses). n(42)=20. '42 44' occurs exactly x2 (@1617, @1838 — i.e. 42@1617/44@1618 and 42@1838/44@1839). Ran predecessor/successor censuses for 42 (n=20) and 44 (n=15), and a letter-adjacency scan for 42 against standing letter values (82='m', 34='i', 29='er', 40='e', 12='n', 48='e'). Parses use only standing values per protocol §7. Coordinated with (not duplicating): de-frame-44-83-21 (null 2026-10-08; the @1839 5-gram window), stem-44-nominal (null 2026-10-08; stream-wide segmentation split fenced to red team), noun-44 (KILL 2026-10-08; value claim "44 is a noun" dead, @1714 clitic-slot forcing stands — NOT re-litigated here).

## Window-level evidence

**Target window @1838–1840 (row a8_11, stream-final region):** `64 22 42 | 44 83 21 67 78 | 49 74 93` — full @1830–1846: `24 82 16 59 36 69 64 22 42 44 83 21 67 78 49 74 93` (stream ends @1846). Standing reads: 64='qui' (granted), 83='de' (lead, conditioned), 67='et' by §7 positional rule (78 not infinitive-shaped), 78='ver'-word lead (de-frame clause b, passed).

**The stem reading (H_stem: 44 word-internal stem at @1839) — excluded, three composition candidates tested:**
- (a) Leftward "42[44]" with 44 as stem: requires a prefix/affix/letter role for 42. 42 has NO standing letter or affix value — its frame is A1 predicative (granted, value open). Letter-adjacency scan: 42 never touches 82 or 34 stream-wide; its only letter adjacencies are '29 42' x3, '42 48' x1, '48 42' x1 (29='er', 48='e' — none yields a 42-affix toward 44). A "42[44]" composition is not nameable without inventing a 42 value — inadmissible at battery level ("never invent data"). Contrast the forced 'm[44]' at @1160, which had banked 82='m' as the letter.
- (b) Elision "42'44": excluded — 44 is consonant-initial per stem-44-nominal's elision census ('la 44' @1070 unelided with 11='la' banked; 'le 44' x2 unelided; §7 one-form). French elision is mandatory before vowels; the unelided articles fix 44's onset.
- (c) Rightward "44[83]": blocked by the conditioned 83='de' lead — word-internal "44de" would overturn the lead, unavailable at battery level.
- H_stem is therefore not merely unsupported but inadmissible: every composition path needs an invented value or overturns a standing lead.

**The whole-word reading (H_whole: 44 whole-word nominal head at @1839) — established:**
- Slot grammar (de-frame-44-83-21 clause (a), passed at slot level and re-verified here): "[44] de [21] et [78-word]" — the 'de [21]' complement + 'et [78]' coordination is NP-internal; only a nominal 44 is grammatical in this position (a finite verb or adjective cannot head "…de [21] et [ver-word]"). 44 heads the 'de'-NP as a standalone word.
- Parallel '42 44' occurrence @1617–1619 (row a8_03): `31 76 42 44 11 84 78` — 44 followed by banked 11='la'; stem-44-nominal adjudicated 44 whole-word there (right-edge 'la on' fenced as 44-independent per noun-44). Same bigram, same segmentation at both occurrences: consistent two-token contact, no composition.
- 42's distributional profile (n=20, all windows): successors 06 x5, 98 x3, 94 x3, 16 x2, 44 x2, 48/63/96/41 x1; predecessors 29 x3, 76 x3, 33 x2, 59 x2, plus 12 singletons. 42 behaves as a standalone word-level token across the stream (A1 predicative frame) — e.g. '42 06' x5 ("[42] ent"), '42 94' x3 ("[42] ne") — not as a bound prefix. Nothing in 42's 20-window distribution suggests proclitic/compositional behavior toward a following token.

**'42 44' contact — explained:** two adjacent standalone tokens, occurring x2 (@1617, @1838). 42 = A1-predicative-frame token (value open, standalone distribution); 44 = whole-word nominal head of the following 'de'-NP. No composition is nameable under standing values; the contact is adjacency, not morphology.

## Per-clause verdicts

1. 44 at @1839 decided stem-vs-whole: PASS — whole-word nominal head. H_stem excluded (all three composition paths inadmissible: no 42 affix value exists, elision excluded by consonant-initial 44, rightward blocked by the de lead). H_whole positively established (NP-head slot grammar; parallel whole-word @1618).
2. '42 44' contact explained: PASS — two tokens in contact, not in composition; evidenced at both occurrences (@1617 with 44 whole-word before 'la'; @1838 with 44 heading the 'de'-NP) and by 42's standalone 20-window distribution.
3. (Adverse) No global value named: PASS — no value is named for 44 anywhere in this report.
4. (Adverse) @1714 not re-litigated: PASS — @1714 untouched; noun-44's kill and its clitic-slot forcing stand exactly as filed.

## Verdict: PROMOTE (instance-scoped)

44 at @1839 is a whole-word nominal head; the '42 44' contact is two-token adjacency. All bar clauses pass; both adverses answered by compliance.

**Scope fence (explicit, not a re-litigation):** this promote decides the @1839 instance only. It names no value for 44 and takes no position on @1714. The global question — whether whole-word nominal-head status at @1839 (and the other 12 whole-word windows) together with the clitic-slot forcing at @1714 requires a second value/polyvalence declaration for 44 under §7 — is already owned by the red-team docket (poly-44-docket and escalate-44-deframe, regenerated by stem-44-nominal and de-frame-44-83-21). That docket is flagged here, not decided, not re-litigated, and not contradicted: no standing verdict is downgraded by this report.

## Provenance

Every number re-derived from the repaired 1,847-pair stream in-work: n(44)=15, n(42)=20, '42 44' x2 (@1617, @1838), 42 successor/predecessor censuses, 42-letter adjacency scan (no 82/34 contact), window bytes @1830–1846 and @1615–1621. No invented data. canonical.py not used. R5005, sealed gates, and the red-team adjudication queue untouched. Lock deleted on completion.
