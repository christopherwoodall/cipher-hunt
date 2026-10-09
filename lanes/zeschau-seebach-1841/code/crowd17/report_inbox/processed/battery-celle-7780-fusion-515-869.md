# Battery report: celle-7780-fusion-515-869

- Target id: `celle-7780-fusion-515-869`
- Claim: window-scoped test of the '87 77' = 'celle' fusion at @515/@869 against the relative-requirement (expected dead; confirm at these loci)
- Date: 2026-10-09
- Worker: battery worker (agent dfce58d2-860c-4c35-bef9-8fce091fe12b)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched.

Terms (ASD-STE100): "fusion" = two digit-groups read as one French word ("87 77" as "celle", not "ce"+"le"). "Relative-requirement" = the battery-grade rule from ce-le-verb-frame: a demonstrative "celle" must be followed by a relative clause ("celle qui...", "celle que...", "celle de..."). "Relative" = a word that opens a relative clause. Under standing values only 64="qui" and 46="que" are relatives. "Verb-frame" = a group with a verb-class grant (A8 covers 80/89) but an open value. "Standing value" = a value granted or promoted by the lane (protocol §7). "Battery grade" = proven at the lane's battery standard. "Kill grade" = a window forces the claim false.

## Bar (verbatim from the brief)

"'87 77' = 'celle' parses at @515/@869 under the relative-requirement; kill if forced false; fence if undecidable"

Numbered pass/fail clauses (restated before testing, not modified after):

1. C1: At @515 (row a3_00), the group right after the "87 77" bigram (@517) is a relative (64 or 46) under standing values.
2. C2: At @869 (row a5_07), the group right after the "87 77" bigram (@871) is a relative (64 or 46) under standing values.
3. C3: Verdict rule. PROMOTE iff C1 and C2 both pass. KILL iff any clause fails at kill grade (a window forces the claim false). FENCE iff a clause is undecidable (the follower cannot be classed under standing values).

## Method

1. Read BATTERY-PROTOCOL.md in full first. Created `code/crowd17/next-token/locks/celle-7780-fusion-515-869.lock` on start (agent id + 2026-10-09T11:16Z). No stale lock existed. Lock deleted on completion (verified gone).
2. Re-derived the repaired stream in-session. Census: "87 77" occurs exactly **2x** stream-wide, both as direct bigrams. Byte-confirmed:
   - Window A @515 (row a3_00): `…511=98 512=65 513=88 514=56 | 515=87 516=77 | 517=80 | 518=09 519=70`
   - Window B @869 (row a5_07): `…865=46 866=00 867=86 868=70 | 869=87 870=77 | 871=89 | 872=48 873=20`
   These match the prior inf-7780-reseg windows group-for-group (the a5_03 repair shifts only row a5_03 onward by one pair index; row a3_00 is untouched and row a5_07's group content is identical).
3. Standing values held fixed per §7: 87="ce" (granted), 77="le" (provisional), 64="qui", 46="que" (the only relatives), 80/89 = A8 verb-frame (value open, not relatives). Adverses: none listed.

## C1: @515 follower test — FAIL

The follower @517 is 80. Under standing values 80 is an A8 verb-frame, value open. It is not 64 ("qui") and not 46 ("que"). The relative-requirement is not met at @515. The failure is forced, not undecidable: 80's verb-frame class is a standing grant, incompatible with a relative reading.

## C2: @869 follower test — FAIL

The follower @871 is 89. Under standing values 89 is an A8 verb-frame, value open. It is not 64 ("qui") and not 46 ("que"). The relative-requirement is not met at @869. The failure is forced, not undecidable: 89's verb-frame class is a standing grant, incompatible with a relative reading.

## Escape routes checked and closed

- "celle de" (prepositional "de" instead of "qui/que"): the only "de" candidate, 83, sits at NULL (de-83-sweep, unratified) and is not present at either window anyway (followers are 80/89). A preposition "de" also contradicts the A8 verb-frame grant.
- 80/89 as relative: no standing value licenses this; the A8 grant is verb-frame class. Contradicted.
- Distributional cross-check (repaired stream): 87 is followed by 64 x5 ("ce qui") and 46 x3 ("ce que") elsewhere — the "ce"+relative pattern is real in the stream, and the "87 77" loci fail exactly where that pattern would require success.

No standing/red-team verdict contradicted or downgraded; §7 intact; canonicality caveat stands (rows a3_00/a5_07 upstream offsets unvalidated — the test is defined against the lane's authorized repaired stream, and the caveat does not change the verdict).

## C3: verdict rule — KILL

Both windows force the claim false under a battery-grade requirement. The bar says "kill if forced false". The fusion "'87 77' = 'celle'" is dead at both loci on the repaired stream, matching the prior finding (ce-le-verb-frame account 5, adopted there and confirmed here at kill grade).

## Verdict: KILL

## Follow-ups proposed

None required for a kill. The '87 77' = 'celle' fusion is closed at both loci. (The '87 77' = 'ce'+'le' re-segmentation line continues via `inf-7780-rerun-gated` and `window-515-fullparse`, queued by the prior null.)

## Bookkeeping

- Queue: `celle-7780-fusion-515-869` → `verdict`/`kill`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock created on start, deleted on completion (verified gone).
