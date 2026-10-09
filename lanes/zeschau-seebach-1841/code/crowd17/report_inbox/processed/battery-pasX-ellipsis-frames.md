# Battery verdict: pasX-ellipsis-frames

## Bar (verbatim, pre-registered)

> fence iff no elliptical frame parses

Numbered clauses (pre-registered before testing):
1. (Enumeration clause) Every "30 X" window with no verb host in the immediate (30, X) bigram is enumerated from the repaired 1,847-pair stream, re-derived — not copied from the census.
2. (Sample clause) Each sample window — @1114 "pas [69-noun] la", @1368 "pas m [16]", @1716 "pas qui ce" — is tested for a grammatical elliptical bare-"pas" parse: ne-drop + ellipsis with "pas" negating a non-verbal constituent, under standing values only.
3. (Fence clause) The ellipsis hypothesis is fenced iff no window in the test set parses under the elliptical reading; it survives iff at least one window parses.

Origin: null follow-up #3 of battery-pasX-adverb-census (2026-10-09). Adverses: none listed.

## Method

Read BATTERY-PROTOCOL.md first. Lock `locks/pasX-ellipsis-frames.lock` created on start (agent id 40d417e1-ec7a-4665-bad3-3288c9480cd0 + UTC 2026-10-09T14:47:36Z); no fresh lock present; deleted on completion.

Re-derived the stream inline per `code/side-keyhunt/repair_parse.py` from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`: 1,847 pairs, 96 groups, asserts held. `canonical.py` never touched. R5005, sealed gates, red-team adjudication queue untouched. No standing red-team verdict on ellipsis/bare-pas found (r19's ellipsis ruling concerns subject ellipsis, a different frame).

Standing values honored, not re-litigated: 30="pas" (prom), 11="la" (gt), 82="m" (gt, letter), 64="qui" (prom), 47="ce" (prom), 79="tout" (prom), 59="est" (provisional), 77="le" (provisional), 92=verb (class), 19=one verb lexeme, 65=noun (class), 69=noun (battery-grade), 06="ent" (prom; syllabic here per the 06-function rule since left neighbor 30 is not a verb stem), 62="il" (lead). Kills hold (48="est"/"ne"/"de", 20="fois", 09/92 "-ère").

Elliptical bare-"pas" frames tested (French, ne dropped, no verb host): "pas de N" / "pas d'N" (partitive — requires X="de"); "pas Adv" (pas encore / seulement — already fenced for every X by the adverb census); fixed/interjective ("pas question", "pas la peine", "pas moi/toi/lui", "non pas", "pas du tout", "pas mal"); answer-fragment "[ce n'est] pas X"; contrastive "pas X, mais Y" (wide ±4 windows scanned for contrastive continuations).

## Enumeration (re-derived): 19 "30" occurrences, positions match census byte-for-byte

| @ | row | L | 30 X Y | elliptical test |
|---|---|---|---|---|
| 30 | a1_00 | 24 | 30 03 64 | "pas [03-noun] qui" — no frame |
| 45 | a1_01 | 81 | 30 62 96 | "pas il par" — no frame (adv-62 fence stands) |
| 483 | a2_11 | 52 | 30 01 19 | "pas [01] [19-verb]" — 01 OPEN; elliptical "pas [01]" alone unnameable; non-elliptical "pas [adv] [verb]" needs 01=adverb (fenced; owned by queued adv-01-19-frame) |
| 560 | a3_02 | 59 | 30 67 11 | "pas et la" — 67≠"veut" (follower 11="la" not infinitive, §7); neither arm adverb-shaped |
| 656 | a4_02 | 26 | 30 03 62 | "pas [noun] il" — no frame |
| 742 | a5_02 | 20 | 30 67 77 | "pas et le" — no frame |
| 993 | a6_01 | 26 | 30 03 60 | "pas [noun] [60]" — no frame |
| 1114 | a6_07 | 38 | 30 69 11 | "pas [69-noun] la" — SAMPLE, see below |
| 1222 | a7_01 | 48 | 30 09 20 | "pas [09] [20]" — both OPEN, no frame nameable (wide: 92 61 24 48 \| 30 09 20 \| 57 64) |
| 1251 | a7_02 | 26 | 30 06 65 | "pas"+"ent" syllabic + [65-noun] — no bare-pas constituent (the "passent" re-segmentation is owned by queued pasent-subject-26-56 / reseg-1564-pasent / spell-pasent-test) |
| 1269 | a7_02 | 24 | 30 20 64 | "pas [20] qui" — no frame (wide: 46 69 88 24 \| 30 20 64 \| 47 76) |
| 1309 | a7_04 | 52 | 30 92 44 | "pas [92-verb]" — CANONICAL NEGATION, has verb host in the bigram; control, excluded from the elliptical set |
| 1327 | a7_04 | 56 | 30 06 62 | "pas"+"ent" syllabic + "il" — no frame |
| 1368 | a7_06 | 03 | 30 82 16 | "pas m [16]" — SAMPLE, see below |
| 1561 | a8_01 | 26 | 30 06 60 | "pas"+"ent" syllabic + [60] — no frame |
| 1702 | a8_06 | 94 | 30 20 62 | "pas [20] il" — no frame (wide: 91 85 33 94 \| 30 20 62 \| 94 88) |
| 1716 | a8_06 | 59 | 30 64 47 | "pas qui ce" — SAMPLE, see below |
| 1729 | a8_07 | 24 | 30 15 01 | "pas [15] [01]" — both OPEN, no frame nameable (wide: 98 39 88 24 \| 30 15 01 \| 56 30) |
| 1733 | a8_07 | 56 | 30 06 60 | "pas"+"ent" syllabic + [60] — no frame |

Precision note on the evidence text: it says "19 '30 X' windows with no verb host". The re-derivation finds 19 "30" occurrences, but @1309 "pas [92-verb]" DOES have a verb host in the immediate bigram — it is the canonical-negation control. The elliptical test set is 18 windows. The off-by-one does not change the outcome.

Sample window verdicts (window-level evidence, @-offsets):
- @1114 (a6_07, wide "73 41 65 38 | 30 69 11 | 88 70"): "pas [69-noun] la". 69=noun (battery-grade), 11="la" (gt). No elliptical frame: "pas la peine" would need X=la (here Y=la); "pas [N] la" is unattested in every register; fragment-answer "pas"+bare-NP is ungrammatical for full NPs (only pronouns: "pas moi/lui"). FAIL.
- @1368 (a7_06, wide "79 14 60 03 | 30 82 16 | 91 67"): "pas m [16]". 82="m" is a gt letter, not "moi"; 16 is OPEN. "pas m…" matches no bare-pas frame; a "pas m'[vowel]" elision rescue would require naming 16's value — inventing data. FAIL.
- @1716 (a8_06, wide "65 94 44 59 | 30 64 47 | 68 06"): "pas qui ce". 64="qui" (prom, relative/interrogative pronoun) can never be a pas-complement — "pas qui" is ungrammatical in all registers; "qui ce" order excludes any cleft rescue ("ce … qui" would need reversed order). Left neighbor 59="est" is provisional only and even "[n']est pas qui ce" leaves the complement ungrammatical. FAIL.

Extended sweep: all 18 verb-less windows checked against every frame class above. Zero parses. No "pas de N" (no X is "de"; 48="de" killed). No "pas Adv" (fenced). No fixed idiom. No fragment. No contrastive continuation in any ±4 window.

## Clause verdicts

1. (Enumeration clause) PASS — 19 "30" occurrences re-derived from the repaired stream; 18 lack a verb host in the immediate bigram (@1309 is the canonical-negation control).
2. (Sample clause) PASS (test executed) — all three sample windows fail every elliptical bare-"pas" frame under standing values, with stated grammatical causes.
3. (Fence clause) PASS (fence condition met) — 0 of 18 windows parse; the extended sweep finds no elliptical frame anywhere in the set. Fence executes.

Kill check: kill requires a kill-grade contradiction. The claim is existential ("test whether … parses"); zero parses fences the hypothesis but forces no value ≠ at kill grade. No kill. No standing red-team verdict contradicted.

## Verdict: NULL (fence executed)

The ne-drop + ellipsis hypothesis is fenced across the "30 X" inventory: no verb-less "pas" window parses as bare "pas" negating a non-verbal constituent. The fence is window-local and grammatical (not value-lack) at 15 of 18 windows; value-lack at @1222 (09/20 OPEN), @1729 (15/01 OPEN), and partly @483 (01 OPEN).

## Follow-ups (null regenerates work; all verified absent from battery-queue.json)

1. `pasX-leftverb-59` (P3): at @560 and @1716 the LEFT neighbor is 59 ("est", provisional) — test "59 30" as "[n']est pas" (ordinary ne-drop negation with a leftward verb host), which would dissolve the "verb-less" premise for those two windows with no ellipsis at all. Bar: promote iff "59 30" parses as "[ne] est pas" with 59="est" attested independently of these windows; fence iff 59≠"est" or the post-pas complement stays ungrammatical.
2. `pasX-64qui-reorder` (P4): @1716/@1269 show "qui ce" / "[20] qui ce"-adjacent order — test whether 64="qui" holds at these windows or a local re-segmentation parses (the "pas qui" impossibility may signal segmentation, not grammar). Bar: name the re-segmentation from independent windows only; fence iff none parses.
3. `pasX-15-01-values` (P4): @1729 "pas [15] [01]" is fenced on value-lack, not grammar — propose values for 15 and 01 from independent windows, then re-test the elliptical frame. Bar: name both values independently (no invention); kill iff a named pair forces a non-elliptical parse.

## Bookkeeping

- Lock `locks/pasX-ellipsis-frames.lock` created on start, deleted on completion.
- `battery-queue.json`: target `pasX-ellipsis-frames` queued → verdict/null (own entry only, temp-file + rename; pre-write assert confirmed status "queued" with null verdict; JSON re-validated post-write).
- R5005, sealed gates, red-team adjudication queue untouched. `canonical.py` never used. No data invented; every offset re-derived from the repaired 1,847-pair stream.
