# Battery report: leftedge-52-86-1736 (NULL — 52 unnameable at battery grade)

**Target:** leftedge-52-86-1736 — "@1736-1739 'ne [52] [86]' parses as the main clause hosting the fenced window"
**Worker:** 60807c57-efca-40c7-830b-711201bfc706 | **Date:** 2026-10-09
**Stream:** repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py). Never canonical.py. No R5005 touched. No data invented. Every @-offset re-derived from the stream.
**Coordination:** rightedge-56-1745 runs in parallel — this battery does not touch @1742+ right-edge analysis or @1745+; boundary work stops at @1741.

## Bar (verbatim from battery-queue.json)

"(a) 52 named with 'ne [52] [86]' parsing (12-48 analytic 'ne' + INF-class 86); (b) the clause boundary before @1742 stated or fenced; (c) zero contradiction with A9's 86 grant"

## Bar as numbered clauses (pre-registered before testing)

1. 52 is named (given a French value) such that 'ne [52] [86]' parses, with 12-48 as analytic 'ne' and 86 as INF-class.
2. The clause boundary before @1742 is stated (located with evidence) or fenced (declared unresolvable with cause).
3. Zero contradiction with A9's 86 INF-class grant.

## Method

1. Reparsed the repaired stream byte-exactly per repair_parse.py (1,847 pairs, 96 unique; asserts hold).
2. Confirmed the window on stream: @1736-1739 = 12 48 52 86 (row a8_07); left context @1730-1735 = 15 01 56 30 06 60; right @1739-1744 = 86 12 34 94 82 46 (the ni-1740-1742 fenced window, adopted as standing context, not re-litigated).
3. Ran full-stream censuses: 52 (n=27, all windows with ±4 context), 86 predecessors/successors (n=32), 12-48 bigrams (x5), bigram counts for 86-12 / 12-34 / 48-52 / 52-86.
4. Tested 52-value candidates {pas, plus, jamais, point, guère, rien, se, finite-modal, adjective} against all 27 windows of 52 and the three 'ne [52] [INF]' frames.
5. Checked corpus plausibility of "ne [X] [INF]" frames against the lane's French texts (gutenberg-17489-miserables1, gutenberg-30513/30514-tocqueville-t1/t2).
6. Standing values used: 12='n' + 48='e' letters (R17 battery), 94='ne' (battery-promoted, arguendo where noted), 30='pas' (promoted), 86 INF-class (A9, class-level), 82='m' / 34='i' / 46='que' (banked GT).

## Window-level evidence (@-offsets)

**The target window (re-derived):**
- @1736-1739 = `12 48 52 86` = 'ne' (12-48, 1 of x5) + 52 + 86 (INF-class, A9).

**The 'ne [52] [INF]' frame is real and consistent (x3):**
- @1294: `84 59 35 94 52 80 04` = "on est [35] ne [52] [80-verb]"
- @1736: `60 12 48 52 86 12` = "[60] ne [52] [86-INF]…" (12-48 analytic 'ne')
- @1807: `84 59 35 94 52 80 04` = byte-identical to @1294 (`94 52 80 04` x2)
- 80 is verb-frame/infinitive (A8); 86 is INF-class (A9). In all three, 52 sits between 'ne' (94 or 12-48) and an infinitive.

**52's full census (n=27):** predecessors spread (94 x3, 11 x3, 48 x2, 06 x2, 86 x2, 64 x2, 93 x2, rest x1); successors: 82 x5 ('52 82 94' x3 @649/@1100/@1574, '52 82 16' x2 @1385/@1435), 37 x4 (@1124/@1129/@1356/@1722), 89/38/30/80 x2, 86/94/33/87/67/35/39/42/32/68 x1.

**Boundary bigrams:** 86-12 x1 (hapax), 12-34 x1 (hapax), 48-52 x2, 52-86 x1, 12-48 x5.

**Corpus check ("ne [X] [infinitive]" in Misérables/Tocqueville t1/t2):**
- "ne [finite-modal] [INF]" dominant: 'ne peut' x73, 'ne saurait' x74, 'ne pourra' x39, 'ne doivent' etc. (literary 'ne' without 'pas').
- "ne pas [INF]" x32; "ne point [INF]" x10 — always as "de ne point [INF]".
- Bare "de ne [lexical-INF]" attested x7: "de ne parler/signal er/contracter/travailler/faire/voir/mettre".
- "ne se [INF]": NOT attested (the x10 crude hits were finite-verb frames, e.g. "ne se rencontre").

**Prior battery context adopted:** stem-86 battery left @1739 OPEN with "52 unknown"; ni-1740-1742 KILLED @1739-1744 (zero parses, both readings fenced); adj-52-37-value NULL ({même/seule} tie, 52-37 adjective lead unpromoted).

## Per-clause pass/fail

**Clause 1 (52 named) — FAIL at null grade.**
The 'ne [52] [INF]' frame is locally coherent — IF 52 is adverbial, "ne [52] [INF]" parses (corpus: "ne pas/point [INF]", "de ne [INF]"). But no single French value names 52 across its 27 windows:
- 52='pas': BLOCKED. 30='pas' is promoted, and '52 30' x2 (@482 '00 13 52 30 01', @1308 '77 74 52 30 92') would read "pas pas" — ungrammatical.
- 52∈{plus, jamais, point, guère, rien}: each fails globally. @571 '45 94 52 87 78' ("ne [adv] ce [78]" — ungrammatical); @482/@1308 '[X] [52] 30' ("[adv] pas" — ungrammatical); @649/@1100/@1574 '[X] [52] 82 94' ("[adv] m ne" — ungrammatical); @1007 '91 11 52 35' ("la [adv]" — ungrammatical).
- 52=finite modal ('peut'-class; the corpus-dominant "ne peut [INF]"): fails — @1007 "la peut", @482 "pour [13] peut pas", @571 "ce ne peut ce", @649 "le ver peut m ne", @1308 "le [74] peut pas" are all ungrammatical.
- 52='se': "ne se [INF]" unattested in the corpus; fails globally the same way as the adverbs.
- Polyvalence rescue (adverb in 'ne [52] [INF]' x3 vs adjective {même/seule} lead in 'la [52]' x3 / 52-37 x4) would violate §7 (67 et/veut is the sole true polyvalence) — a red-team declaration, not available at battery grade.
- NOT kill-grade: no window forces the 'ne [52] [86]' STRUCTURE false. The parse is conditionally coherent; the failure is 52's unnameability (inconclusive). The stem-86 battery independently left @1739 OPEN on exactly this ground ("52 unknown").

**Clause 2 (boundary before @1742) — PASS (stated).**
The main clause's right edge is after @1739 (86); the boundary sits between @1739 and @1740 (before @1742 ✓).
- 86-12 is a hapax bigram (1/1847); 12-34 is a hapax (1/1847).
- ni-1740-1742 proved @1739-1744 admits zero parses with banked values — @1740+ cannot continue the clause, so the clause ends at @1739.
- @1740-1741 (12-34) is fenced debris: hapax, no "ni…ni" correlative partner stream-wide, no word parse (per ni battery, adopted). The clause does not extend into it.

**Clause 3 (zero contradiction with A9) — PASS.**
- A9 grants 86 INF-CLASS at class level only (subject to the stem/whole caveat); pre=00 x12 and suc=29 x4 are supporting legs, not per-window requirements.
- This window uses 86 as a whole infinitive ('ne [52] [86-INF]') — consistent with the class grant; pre=52 / suc=12 (hapax) contradict nothing in A9.
- Adverse "86 stem/whole caveat" ANSWERED as fenced with stated cause: nothing at @1736-1739 forces the stem reading (suc=29 is only 4/32 of 86's successor profile; 86's suc=12 hapax is neutral). The whole-infinitive reading stands unfalsified; the caveat is noted, not ignored.

## Adverses

- **"52's value open"**: CONFIRMED still open — this is the clause-1 failure. Not ignored: full candidate matrix above; work regenerates via F1–F3.
- **"86 stem/whole caveat"**: fenced with stated cause (clause 3) — class-level grant compatible with the whole-infinitive use here; no forcing evidence either way at this window.

## Red-team consistency check

- A9 (86 INF-class): upheld, no contradiction (clause 3).
- R17-002 (12='n' letter grant): used as granted, not re-litigated.
- ni-1740-1742 KILL: adopted as standing context; this battery's boundary statement (clause 2) is consistent with its fence, not a re-decision.
- §7 sole-polyvalence rule: honored — no polyvalence declared; the tension is escalated (F1/F3), not resolved.
- No existing verdict downgraded (this target had none).

## Verdict

**NULL.** Clause 1 fails at null grade (52 unnameable at battery grade; the 'ne [52] [INF]' frame is real but no value covers 52's 27 windows without red-team-declared polyvalence). Clauses 2–3 pass. Not kill: no window forces the 'ne [52] [86]' parse structure false.

## Follow-up targets for the supervisor queue (null regeneration)

**F1. id: "ne52inf-adverb" | priority: 2**
claim: "52 takes one adverb value across the three 'ne [52] [INF]' windows (@1294, @1736, @1807)"
bars: "name 52 iff a single adverb value parses all three windows with <=1 ungranted assumption AND the global polyvalence tension with the 52-37 adjective lead is stated for red team (battery may not declare polyvalence per S7)"
evidence: "leftedge-52-86-1736 null (2026-10-09): 'ne [52] [INF]' x3 is a consistent frame (@1294/@1807 byte-identical '94 52 80 04'); 52 unnameable at battery grade; {plus, jamais, point, rien, se, finite-modal} all fail globally (@571 'ne [52] ce', @482/@1308 '[X] [52] pas', @649 'ver [52] m ne', @1007 'la [52]')"
adverses: "52's value open; S7 sole-polyvalence rule (67) blocks adverb+adjective without red-team declaration; 52-37 Type-A/B/C split already with red team"

**F2. id: "seg-52-86-unit" | priority: 3**
claim: "'52-86' @1738-1739 is one infinitive (52 = prefix syllable, 86 = stem), making @1736-1739 '[60] ne [INF]' on the corpus-attested 'de ne [INF]' pattern"
bars: "unit reading holds iff 60 takes 'de'/de-class value AND 52-86 as one infinitive parses with zero contradiction AND A9's class-level grant survives (86 stays INF-class); else kill the unit reading with the failing clause stated"
evidence: "corpus 'de ne [lexical-INF]' x7 ('de ne parler/signaler/contracter/travailler/faire/voir/mettre'); 86-12 hapax compatible with word-internal boundary under stem reading; stem-86 battery left @1739 OPEN; 60 n=18 (@1735 '56 30 06 60 12 48')"
adverses: "86 stem/whole caveat (A10 HOLD); 60's value open (no 'de' signal in its 18-window profile yet); 52-86 bigram x1"

**F3. id: "leftedge-60-value" | priority: 3**
claim: "60's value at @1735 decides whether '[60] ne [52] [86]' opens with 'de' (supports F2) or with a subject noun"
bars: "name 60 iff its 18-window profile yields one value parsing @1735 ('56 30 06 60 12 48') with <=1 ungranted assumption; record the consequence for the leftedge parse either way"
evidence: "60 n=18; predecessors 21 x4 / 92 x2 / 14 x2 / 06 x2; successors 03 x4 / 12 x2 (@700 '94 60 12 98', @1735); @172 '12 48 21 60' is a second 'ne'-adjacent 60 window"
adverses: "60's class fully open; gates F2's '[60]=de' arm"

---
Lock: locks/leftedge-52-86-1736.lock created 2026-10-09T05:16:14Z, deleted on completion of this report. No R5005 touched. No sealed gates touched. No promotions made. No red-team verdicts modified. rightedge-56-1745's bar not duplicated (@1742+ untouched).
