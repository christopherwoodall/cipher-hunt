# Battery verdict: w508-noun-ne

**Target:** `w508-noun-ne` (P2)
**Date:** 2026-10-09
**Worker:** battery worker (subagent 5232bcbf-3f2f-4aad-a32b-6d456a9adbd9)
**Stream:** repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1,847 pairs / 96 types held). `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

## Bar (verbatim from battery-queue.json)

"62-94's contact profile at @508 vs the candidates' distributional signature; a clean parse promotes the resolution of R17-022's fenced residual"

## Numbered clauses (restated before testing; not modified after)

1. C1 — The @508 window parses cleanly as "et le [W]ne qui vient" under standing values for exactly one named candidate W.
2. C2 — The named candidate's distributional signature (gender, initial, -ne ending, corpus frame attestation, 62's stream profile) matches 62-94's contact profile at @508; every rival is killed or fenced with stated cause.
3. C3 — Naming the word resolves R17-022's fenced residual (the word-reading succeeds where every two-word parse failed).

Verdict mapping: promote iff C1–C3 all pass; kill iff a clause fails at kill grade; else null with 1–3 follow-ups.

## Method

1. Read BATTERY-PROTOCOL.md first; created `locks/w508-noun-ne.lock` on start (2026-10-09T08:03:07Z), no prior lockfile; deleted on completion.
2. Re-derived the repaired stream in-session; verified anchors (@1030–1033 = 03 29 80 77; @1115–1117 = 69 11 88) byte-exact.
3. Adopted (not duplicated): seg-62-94-wordfinal KILL (its @508 word-reading PASS: "et le [noun-ne] qui"; candidate set {moine, trone, prone, cone, hymne}); vient-98-name PROMOTE (98='vient', explicitly covering @511: "'ne qui vient [65]'. Clean"); verbless-ne-family PROMOTE (94 D3-un-attachable at @509 via the 64='qui' blocker — the two-word "il ne qui" parse is dead).
4. Ran the candidate census against the 27 MB period corpus (`code/side-period/corpus/`, 1841 French incl. Allgemeine Zeitung Jan 1841) for the "et le [W]" frame and W+venir collocations.
5. Tested under standing values only: 67='et' (positional rule — 77 not infinitive-shaped), 77='le' (provisional), 64='qui' (granted), 98='vient' (battery-promote), 65=noun class (R18). No invented data.

## Window-level evidence

**Window bytes (0-based @506–511, row a3_00, offset 0):** `67 77 62 94 64 98` = "et le [62][94] qui vient". Wider: @502–505 `56 39 68 21` ("[56] a/à [68] [21-noun]"), @512–513 `65 88` ("[65-noun] [88-verb]" — new clause; "vient" takes no nominal complement).

**62's stream profile (n=35, re-derived):** successors 94×9, 48×6, 98×5, 16×4, 61×2, 06×2, rest ×1. "77 62" (le+62) occurs exactly once stream-wide — this window. 62='il' demonstrated at the particle-'ne' 62-94 windows; 'donne'-verb weak at @1363. None contradicts a locus-level noun-stem reading here.

**Corpus frame census ("et le [W]", 1841 corpus):**

| candidate | corpus total | "et le [W]" | "du [W]" | W+venir |
|---|---|---|---|---|
| trône | 398 | **2** (political ctx) | 30 | "trônes qui viennent" ×1 |
| règne | 354 | 0 | 8 | 0 |
| moine | 160 | 0 | — | 0 |
| cône | 42 | 0 | — | — |
| hymne | 47 | — | — | — |
| prône | 6 | 0 | — | — |
| faune | 6 | 0 | — | — |
| automne | 48 | — | — | — |

**Per-candidate adjudication:**

- **trône** — masculine ✓, consonant-initial ("le trône" ✓), -ne ✓ ("trô"+"ne", 94='ne' syllable per the 'prenne' paradigm). "et le trône qui vient" parses cleanly under standing values. Unique positive frame attestation ("et le trône" ×2, political/diplomatic context); genre match (diplomatic letter). NAMED.
- **règne** — parses cleanly ("le règne qui vient" = "the coming reign", natural). FENCED: zero "et le règne" attestations despite 354 corpus hits; runner-up. (Not in the parent's candidate list; tested as extra arm since "règne/trône" is 62's narrowed value set — no contradiction: that narrowing is a global-value lead, this is a locus-level word read.)
- **moine** — parses cleanly ("le moine qui vient" most natural "qui vient" fit). FENCED: zero "et le moine" attestations; pragmatically odd in a diplomatic letter.
- **prône / cône / faune / chêne / frêne / crâne** — grammatical shape, but zero frame attestations and pragmatically bizarre in 1841 diplomatic French. FENCED with cause (no positive evidence; not killed — pragmatic absurdity is not byte-level force).
- **hymne / automne / aîné** — KILLED (conditional): vowel-initial → "le hymne"/"le automne" ungrammatical. Conditional on provisional 77='le'; re-opens iff 77≠'le'.
- **domaine** — EXCLUDED: "domaine" killed as 62's value by prior battery (adopted, not re-litigated).

## Per-clause pass/fail

1. **C1: PASS.** "et le trône qui vient" parses cleanly: 67='et' (positional), 77='le' (provisional), 62-94="trône" (word fusion per the granted "cela"-dissolution doctrine), 64='qui' (granted), 98='vient' (battery-promote, @511 explicitly covered). Clause boundary after "vient"; "65 88" opens the next clause.
2. **C2: PASS.** trône is the unique candidate with positive distributional signature match: masculine, consonant-initial, -ne-final, "et le trône" attested ×2 in political context in the 1841 corpus, "trônes qui viennent" ×1; genre-matched to a diplomatic letter. Rivals killed (hymne/automne, conditional) or fenced (règne runner-up; moine; prône/cône/faune/etc.).
3. **C3: PASS.** The two-word parses at @508 all failed (verbless-ne-family: 94 D3-un-attachable via qui-blocker; "le il ne qui" ungrammatical). The word-reading "et le trône qui vient" succeeds — R17-022's fenced residual is resolved structurally.

**Adverses:** none listed in the queue entry.

## Standing verdicts (checked, none downgraded)

- R17-001 (94='ne' STRONG LEAD): untouched — locus-level -ne syllable per the 'prenne' paradigm, same doctrine as granted "cela" dissolutions; no second 94 value declared (§7 intact).
- 62='il' (collision-62-84 / il-62): untouched — separate windows, locus-level reading here.
- seg-62-94-wordfinal KILL: consistent — its kill was x9-generalization; its @508 word-reading PASS is adopted as premise.
- 67 sole polyvalence (§7): intact.

## Caveats (stated, not hidden)

- **Canonicality:** a3_00 offset 0 is unvalidated upstream; the window dissolves under the row's rival phase (per protocol, verdict holds on the canonical stream; offset adoption is a red-team act).
- **Thin exact-word evidence:** the naming rests on 2 "et le trône" frame attestations + genre fit; "le trône qui vient" is semantically strained (thrones don't "come") — the structural resolution (C3) is stronger than the lexical identification.
- **hymne/automne kills** are conditional on provisional 77='le'.
- **Battery grade only:** needs red-team ratification before banked use. Runner-up règne stays live if the red team rejects trône.

## Verdict: PROMOTE (locus-level word name, battery grade)

The @508 word is **"trône"**: "et le trône qui vient". R17-022's fenced residual is resolved.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/w508-noun-ne.lock` created on start, deleted on completion (verified gone).
- `battery-queue.json`: `w508-noun-ne` status `queued` → `verdict`, `verdict: {"result": "promote", "report": "code/crowd17/report_inbox/battery-w508-noun-ne.md", "date": "2026-10-09"}` (temp-file + rename; pre-write assert confirmed queued/verdictless — no downgrade; JSON re-validated; only this entry touched).
- R5005, sealed gates, red-team adjudication queue untouched. No invented numbers.
