# Battery verdict: 62-regne-trone-final

**Verdict: NULL** — the règne/trône tie is not broken at battery grade. The narrower bar reproduces the parent's split: the head sub-frame favors trône, the tail sub-frame weakly favors règne, the exact frame is unattested for both, and no fresh 62-window discriminates. No standing verdict contradicted or downgraded (§5 honored throughout).

**Target:** `62-regne-trone-final` (P2)
**Date:** 2026-10-09
**Stream:** repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1,847 pairs / 96 types held in-session). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.

## Bar (verbatim, pre-registered before testing)

"Semantic fit at the @508 head under 'et le [62]ne qui [98]...' with 94='ne' letter-tier, or fresh frames from the 35-window census; 62-06/62-48 windows excluded (already consumed)."

Numbered clauses (restated before testing; not modified after):

- **C1**: Semantic fit at the @508 head under "et le [62]ne qui [98]..." with 94='ne' letter-tier names "règne" or "trône" at battery grade.
- **C2**: OR fresh frames from the 35-window census (62-06/62-48 windows excluded) name "règne" or "trône" at battery grade.

## Standing premises adopted (not re-litigated)

- `syll-94-508-verify` PROMOTE: 94 at @508 (0b@509) is the word-final 'ne' syllable of 62's word ("[62]ne"), conditional on provisional 77="le"; particle-94 kill-grade dead at this window.
- `w508-noun-ne` PROMOTE (battery grade, needs red-team ratification): locus-level word name **"trône"** at @508 ("et le trône qui vient"); règne fenced as runner-up (zero "et le règne" attestations).
- `regne-trone-tiebreak` NULL: differential frame found ("le [62]ne qui vient" selectionally favors règne) but below battery-grade naming confidence; naming règne would contradict the standing "trône" promote → red-team escalation.
- 98='vient' battery-promote (explicitly covering @511); 67='et' positional (77 not infinitive-shaped); 77='le' provisional; 94='ne' STRONG LEAD (R17-001, not a grant); 62='il' KILLED at kill grade (R19-106/R20-125).
- §7 intact: 67 et/veut remains the sole true polyvalence; no second value declared.

## C1: semantic fit at the @508 head

Window bytes (0-based @506–511, row a3_00): `67 77 62 94 64 98` = "et le [62][94] qui vient". Wider: @512–513 `65 88` ("[65-noun] [88]" — new clause; "vient" takes no nominal complement, per w508).

Corpus: `code/side-period/corpus/`, **34,551,456 chars** of 1841-register French, censused in-session, accent-insensitive (NFD strip). Provenance: lane period corpus (provenance notes in `code/side-period/corpus/PROVENANCE.md`).

**Exact head frame** ("et le [W] qui" / "le [W] qui vient"): all four cells **zero**:
- "et le trone qui" ×0; "et le regne qui" ×0; "le trone qui vient" ×0; "le regne qui vient" ×0.

**Sub-frame (a) — "et le [W]" (the determiner-phrase head slot):**
- "et le trone" ×3 — all genuine, all political/diplomatic register matching the letter's genre: "soutenir l'autel et le trone" (Delavigne tragedy), "et le trone comme la charte, la paix interieure" (press), "et le trone avec eux" (press).
- "et le regne" ×0 — despite a large "regne" sample in the corpus ("du regne" ×10).
- → favors **trône** on the head slot.

**Sub-frame (b) — "[W] qui vient" (selectional fit of the lexeme as subject of "venir"):**
- "regne": temporally-licensed (periods license "venir" in the onset sense, parallel to "l'année qui vient"); 1 corpus attestation "regne vient de commencer en france" ("the reign has just begun" — "venir de" onset construction; found with double-space "regne  vient", which is why a strict single-space search misses it).
- "trone": selectionally strained (thrones are ascended to — "monter sur le trône", "venir au trône" — they do not themselves arrive); 9 "trone"-near-"venir" hits hand-checked, **0 genuine** with "trône" as subject of lexical "venir" (all are "les rois viennent", "sa majesté vient", "n'interviendrait pas", etc.).
- → weakly favors **règne** on the tail.

**C1 adjudication: FAILS to name.** The two sub-frames of the head point in opposite directions — head-slot distribution favors trône (3 vs 0), tail selectional fit weakly favors règne (licensed+1 vs strained+0) — and the exact frame is 0/0. Neither arm reaches battery-grade naming confidence on semantic fit. This reproduces, rather than narrows, the parent's split; re-weighing the same evidence is not new evidence. Naming "règne" would additionally contradict the standing battery-grade `w508-noun-ne` "trône" promote — per §5 a battery worker never downgrades an existing verdict, so the contradiction is recorded here as escalation context, not acted on.

## C2: fresh frames from the 35-window census

35-window census of 62 re-derived byte-exact (matches parent census):
- 62-06 (consumed, excluded): @665, @1536.
- 62-48 (consumed, excluded): @360, @425, @1315, @1349, @1464, @1569.
- 62-94 (9): @100, @508 (locus), @761, @840, @1329, @1362, @1686, @1704, @1772.
- Other followers: 98×5 (@11, @802, @945, @1136, @1324), 16×4 (@82, @658, @1141, @1297), 61×2 (@446, @1454), 93×1 (@1539), 96×1 (@46), 91×1 (@389), 21×1 (@849), 18×1 (@1065), 46×1 (@1482), 38×1 (@1468).

Letter-composition test: a "règ"/"trôn" letter-cluster reading of 62 requires a letter-tier neighbor. Among fresh windows, only the eight non-508 62-94 windows qualify ("[62]ne"). Each tested for a "[62]ne"-word reading discriminating the arms:

- @100 (`08 21 [62] 94 93 59 45 28 00 46`): bracket geometry with closing 46 ("ne...que" shape, per verb-slot-62-1686-neque); no determiner before [62]ne; word-reading unfounded. No discrimination.
- @761 (`40 20 [62] 94 59 39 88 ...`): "[62]ne n'est" — "règne n'est" and "trône n'est" both grammatical; no determiner; both arms equally (un)licensed. No discrimination.
- @840 (`98 20 [62] 94 26 12 16 ...`): no determiner; 26 open. No discrimination.
- @1329 (`30 06 [62] 94 70 52 ...`): no clean word reading ("[62]ne pre..." ungrammatical under all standing values). No discrimination.
- @1362 (`13 92 [62] 94 79 14 ...`): "[62]ne tout" ungrammatical as word+particle. No discrimination.
- @1686 (`13 93 [62] 94 79 14 60 27 46`): bracket geometry fenced as genuine residual (verb-slot-62-1686-neque NULL). No discrimination.
- @1704 (`30 20 [62] 94 88 26 ...`): "[62]ne" as subject of 88 — both nouns admissible as subjects; no selection between them. No discrimination.
- @1772 (`37 78 [62] 94 24 87 64 59 ...`): the only other "le [62]ne" window (78="le" provisional): "le règne [24]..." / "le trône [24]..." both grammatical; 24's value open. No discrimination now — see follow-up 3.

All other fresh followers (16, 61, 38, 98, 93, 96, 91, 21, 18, 46) are not letter-tier under any standing verdict, so no word-internal composition frame exists for them. (98='vient' is a word; the "62 98" windows would need 62 as a separate word — 62='il' is kill-grade dead, and no other 62 word value is licensed.)

**C2 adjudication: FAILS to name.** No fresh frame discriminates "règne" vs "trône" at battery grade.

## Verdict: NULL

Neither clause names a winner at battery grade. The tie stands exactly where the parent left it: head-slot distribution favors trône (3 vs 0, genre-matched), tail selectional fit weakly favors règne (licensed + 1 onset attestation vs strained + 0), exact frame unattested for both. The standing battery-grade `w508-noun-ne` "trône" promote is untouched; the règne-leaning tail evidence remains a red-team input, not a battery act.

## Follow-ups proposed (all verified ABSENT from battery-queue.json; for supervisor queuing)

1. `et-regne-wider-register` (P3) — Wider 19th-century French search (beyond the lane corpus) for "et le règne". Bar: ≥1 genuine attestation re-opens the head-frame contest (the current 3-vs-0 rests on the lane corpus alone); confirmed zero across a larger base hardens trône's head-slot advantage. (Symmetric counterpart to queued `trone-vient-register`.)
2. `redteam-508-reread` (P2) — Red-team adjudication package for @508: standing battery-grade "trône" promote (`w508-noun-ne`) vs the balanced sub-frame evidence (head 3v0 trône; tail règne-leaning 1v0; exact frame 0v0). The battery cannot downgrade the standing promote — red-team venue. (Proposed by the parent battery; never queued.)
3. `det-62ne-1772-select` (P3) — @1772 `37 78 [62] 94 24 87 64 59`: the only other "le [62]ne" window in the stream. Bar: name 24's value/role at @1775 with zero new assumptions, then test whether the "le [62]ne [24] ce qui est" frame selects "règne" or "trône".

Related already-queued work (not re-proposed): `val-65-at-508` (65's value at the @508 locus — the keyhole), `trone-vient-register` (wider "trône"+"venir" search).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-62-regne-trone-final.md` (this file)
- Queue: `62-regne-trone-final` → `status: verdict`, `verdict: {"result": "null", "report": "code/crowd17/report_inbox/battery-62-regne-trone-final.md", "date": "2026-10-09"}` (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated post-write; own entry only; no downgrade)
- Lock: `locks/62-regne-trone-final.lock` created on start (agent 0dfa9f43-adf3-4444-8076-e58fa898c767, 2026-10-09T17:13:00Z), deleted on completion
- R5005, sealed gates, red-team adjudication queue untouched. No standing verdict contradicted or downgraded. §7 intact. Canonical-stream caveat stands (row a3_00's upstream offset unvalidated).
