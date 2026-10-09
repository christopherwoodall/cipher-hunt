# Battery verdict: seg-62-94-wordfinal

**Target:** `seg-62-94-wordfinal` (P2)
**Date:** 2026-10-09
**Worker:** battery worker (subagent 17738c7b-eefa-4a02-b1f6-26e0a30a0459)
**Claim:** "Test the surviving 62-94 x9 as word-final 'ne' syllable (paradigm: 70-12-94 'prenne', 61-94 candidate); the re-frame's segmentation hypothesis is the natural next test."
**Stream:** repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847 pairs / 96 types held). `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

## Bar (verbatim from battery-queue.json)

"paradigm test"

## Numbered clauses (restated before testing; not modified after)

1. C1 — Anchor: both 70-12-94 instances (@348, @1548) parse as the single French word "prenne" = 70 ('pre', banked) + 12 ('n', letter, promoted) + 94 (word-final 'ne' syllable). PASS iff 2/2 parse.
2. C2 — Control: both 61-94 instances (@578, @1169) parse as one word ending in the 'ne' syllable (stem 61 + 94), with no context forcing a word break between 61 and 94. PASS iff 2/2 parse.
3. C3 — Generalization: each of the nine 62-94 windows (94 at @101, @509, @762, @841, @1330, @1363, @1687, @1705, @1773) parses as one word [62]+'ne' with grammatical surroundings; no window requires a word break between 62 and 94. PASS iff >=7/9 parse.
4. C4 — No kill-grade contradiction: no window forces a non-word reading under standing granted/promoted values (no window where 62 and 94 must be separate words). PASS iff 0 such windows.

Verdict mapping (pre-registered): promote iff C1 and C2 and C3 and C4 all PASS; kill iff a clause fails at kill grade (a window forces the claim false); else null with 1-3 follow-ups.

## Method

1. Read BATTERY-PROTOCOL.md first; created `locks/seg-62-94-wordfinal.lock` on start (2026-10-09T07:53:44Z), no prior lockfile present.
2. Re-derived the repaired stream independently; asserted 1,847 pairs, 96 types.
3. Verified the 94 census byte-exact (37 windows), the 62-94 bigram (exactly x9), the 70-12-94 bigram (exactly x2), the 61-94 bigram (exactly x2).
4. Adopted (not duplicated): prenne-70-12-94 battery clause 1 (composition "pre"+"n"+"ne" PASS at both windows); verbless-ne-family battery census and D3 spot-checks; ne-24-profile battery promote (24 = finite verb); verb-93 battery promote (93 = verb class); il-62 battery promote (62='il', noted not adjudicated here); class-62-fullcensus null ('il' killed globally — pre-existing tension with il-62, not adjudicated here).
5. Tested each window's word-reading against standing values only. No invented numbers.

## Window-level evidence

### Census (re-derived on the bytes)

- 94 census: 37 windows, byte-exact vs parent list (@65 101 161 250 318 349 494 509 558 570 578 651 688 699 762 771 774 785 841 1102 1169 1182 1293 1330 1353 1363 1549 1576 1664 1687 1701 1705 1713 1742 1773 1795 1806).
- 62-94: exactly x9 (62 at @100 @508 @761 @840 @1329 @1362 @1686 @1704 @1772; 94 at +1 each).
- 70-12-94: exactly x2 (@347 row a2_05; @1547 row a8_00).
- 61-94: exactly x2 (@577 row a3_02; @1168 row a6_09).

### C1: 'prenne' anchor

- @347 (a2_05): `01 06 [70 12 94] 74` — "pre"+"n"+"ne" spells 'prenne' cleanly (70='pre' banked, 12='n' promoted letter, 94='ne' promoted). Adopted PASS from prenne battery clause 1; bytes re-verified.
- @1547 (a8_00): `00 46 [70 12 94] 92` — "pour que prenne 92"; composition clean (subject slot fenced in prenne battery, not re-litigated). PASS.
- C1: PASS (2/2).

### C2: 61-94 control

- @577 (a3_02): `13 55 [61 94] 82 06 06` — word-reading "[55] [W]ne m'ent-ent": no clean French word parse under standing values (82='m' banked, 06='ent' promoted; doubled 06 unparsed — owned by queued frame-94-82-06-06). Compatible only.
- @1168 (a6_09): `13 55 [61 94] 87 83` — word-reading "[55] [W]ne ce [83]": no clean parse (83's value open and fenced as blocker by le83-window). Compatible only.
- C2: FAIL (weak) — 0/2 clean parses. The "candidate" does not confirm. The paradigm keeps its single anchor ('prenne'); this fail does not kill the paradigm by itself.

### C3: the nine 62-94 windows under the word-reading

- @101 (a1_02): `08 21 [62 94] 93 59` — "[21] [W]ne [93-verb] est ce": W directly before promoted verb 93 with no subject/relativizer — no clean parse. Compatible only. (Note: pre-existing tension — il-62 reads "[21] il ne [93] est" clean; verb-93 fences "ne [93] est" ungrammatical. Not adjudicated here.)
- @509 (a3_00): `67 77 [62 94] 64 98` — 67's follower 77='le' (provisional) is not infinitive-shaped, so 67='et' per the positional rule: "et le [W]ne qui 98". W = masculine -ne noun ("moine"/"trone"/"prone"/"cone"/"hymne"-shaped) + 'qui' (64 granted) relative — CLEAN. PASS. (This resolves the R17-022 fenced residual: "le il ne qui" failed; "le [noun-ne] qui" parses.)
- @762 (a5_03): `40 20 [62 94] 59 39` — "[20] [W]ne est a": no clean parse (W as subject or verb both ungrammatical with 'est a' under standing values). Compatible only.
- @841 (a5_06): `98 20 [62 94] 26 12` — "[20] [W]ne [26]": 26's class open (noun-26 null); no clean parse. Compatible only.
- @1330 (a7_04): `30 06 [62 94] 70 52` — "[06] [W]ne pre[70]": no clean parse; particle reading marginally viable (86-inf at +5, "ne"+infinitive marginal in 1841 French). Compatible only.
- @1363 (a7_06): `13 92 [62 94] 79 14` — "[92] [W]ne tout [14][60]": weak parse as "[92-nominal] donne tout" (W='donne' verb, 92 feminine-noun subject per 'la 92' x3). Grammatical but load-bearing on open 92/62 values. WEAK PASS.
- @1687 (a8_05): `13 93 [62 94] 79 14` — "[93-verb] [W]ne tout": W after a finite verb must be object/complement; no clean -ne nominal parse. Compatible only. (Tension with @1363: same right edge, different left class — one word cannot be verb-shaped at @1363 and noun-shaped at @1687.)
- @1705 (a8_06): `30 20 [62 94] 88 26` — "[20] [W]ne [88]": no clean parse; particle reading marginally viable (33 at +6). Compatible only.
- @1773 (a8_09): see C4 — word-reading ungrammatical at kill grade.
- C3: FAIL — 2/9 parse (1 clean + 1 weak), need >=7/9.

### C4: kill-grade contradiction

- @1772-1775 (a8_09): `37 78 [62 94] 24 87 64` — word-reading gives "…[78] [W]ne [24-finite-verb] ce qui est": a word directly followed by a finite verb with no subject/relativizer is ungrammatical in French. 24's class (finite verb) is PROMOTED by ne-24-profile; 87='ce' and 64='qui' are granted. No grammatical parse exists under any standing value. The particle reading "[62] ne [24]. Ce qui est…" is clean and PROMOTED (ne-24-profile). The word-reading is impossible at this window; the claim "62-94 x9 as one word" is forced false here.
- C4: FAIL at kill grade.

## Per-clause pass/fail

1. C1: PASS — 'prenne' x2 composition clean (adopted, bytes re-verified).
2. C2: FAIL (weak) — 61-94 x2: no clean word parse; compatible only.
3. C3: FAIL — 2/9 windows parse as one word (need >=7/9).
4. C4: FAIL at kill grade — @1772 forces the x9 word-claim false under standing promoted values.

## Adverses

None listed in the queue entry. One standing-tension noted (not an adverse of this target): il-62's PROMOTE ("il ne" x9, 62='il') vs class-62-fullcensus's NULL ('il' killed globally) — pre-existing contradiction in the queue, not adjudicated here. This battery touches 62's segmentation only, not its value.

## Standing verdicts (checked, none downgraded)

- R17-001 (94='ne' STRONG LEAD): untouched. Kill is segmentation-only; the 3 attachable windows keep particle-'ne'.
- ne-94 battery promote: not downgraded. Its 62-94 x9 support is narrowed (particle reading stands at @1773/@1330/@1705; strained at the 6 verb-less windows), but the verdict itself is untouched.
- il-62 battery promote: not downgraded. 62's value untouched; at @1772 the particle reading "[62] ne [24]" is compatible with 62='il'.
- ne-24-profile battery promote: used as premise, not contradicted.
- verbless-ne-family battery promote: not downgraded. Its re-frame disjunction was "(62-94 word-final 'ne' syllable) OR (distinct 94 value per R17-018)". This kill closes the x9-word disjunct only; the family finding and the @508 re-frame stand — and the @508 word parse ("et le [noun-ne] qui") is new positive evidence for the word disjunct at that window.
- R17-018 (12/94 duality): untouched; the 6 verb-less windows still need a non-particle 94 (word-final 'ne' at a subset, or a red-team-declared second value).
- R17-022 (@508 fenced residual): adopted; this battery proposes its resolution (see follow-up 2).
- 67 sole polyvalence (§7): intact. No new polyvalence declared.

## Verdict: KILL

The x9-as-word-final-'ne' claim is false: @1772 forces a word break between 62 and 94 at kill grade (C4), and only 2/9 windows parse as one word (C3). The cleaner rival on the forced frame is the particle reading ("[62] ne [24]", ne-24-profile promoted).

Positive residue (not buried by the kill): the word-reading is DEMONSTRATED at @508 ("et le [noun-ne] qui" — resolves the R17-022 residual where every two-word parse failed) and remains the live hypothesis for the 6 D3-un-attachable windows (@101, @509, @762, @841, @1363, @1687), where the particle reading is dead or strained. Work regenerates below.

## Follow-ups (kill regenerates work)

1. **seg-62-94-wordless6** (P2): scope the word-final-'ne' segmentation to the 6 D3-un-attachable windows only (@101, @509, @762, @841, @1363, @1687). Anchor: @508 "et le [W] qui" (clean, this battery). Bars: name W's class per window (noun vs verb) with >=4/6 parsing under one class; resolve the @1363/@1687 left-class tension ('donne'-verb at @1363 vs noun-needed at @1687).
2. **w508-noun-ne** (P2): name the @508 word: masculine -ne noun before 'qui' (64 granted). Candidates: {moine, trone, prone, cone, hymne}. Bars: 62-94's contact profile at @508 vs the candidates' distributional signature; a clean parse promotes the resolution of R17-022's fenced residual.
3. **dual94-r17018-scope** (P1, red-team venue): the 6 verb-less windows need non-particle 94 (word-final 'ne' syllable at a subset, or a distinct 94 value); the 3 attachable windows (@1330, @1705, @1773) keep particle-'ne' per ne-94 battery and ne-24-profile. Battery cannot declare the second 94 value (§7); escalate for R17-018 adjudication. (Supervisor routes; this worker does not touch the red-team queue.)

## Bookkeeping

- Lock `code/crowd17/next-token/locks/seg-62-94-wordfinal.lock` created on start (agent id + UTC 2026-10-09T07:53:44Z), no prior lockfile; deleted on completion (verified gone).
- `battery-queue.json`: `seg-62-94-wordfinal` status `queued` -> `verdict`, `verdict: {"result": "kill", "report": "code/crowd17/report_inbox/battery-seg-62-94-wordfinal.md", "date": "2026-10-09"}` (temp-file + rename; pre-write assert confirmed queued/verdictless — no downgrade; JSON re-validated; only this entry touched).
- R5005, sealed gates, red-team adjudication queue untouched. No invented numbers: every @-offset traces to the repaired stream re-derived in-session.
