# Battery report: verb-92-subset

- id: verb-92-subset
- date: 2026-10-08
- worker: 373cd153-45bf-4405-9ac6-d787ac94ad98
- lock: locks/verb-92-subset.lock (created 2026-10-09T00:57:31Z, deleted on completion)
- verdict: **promote** (battery-level, subset-scoped)

## Bar (pre-registered, verbatim from battery-queue.json)

> "name 92=verb on the subset iff >=3 subset windows parse with zero forced contradiction within the subset (fenced residuals excluded); any new forced contradiction kills the subset claim"

Restated as numbered clauses:

1. Name 92=verb on the subset iff >=3 subset windows parse with zero forced contradiction within the subset (fenced residuals excluded).
2. Any new forced contradiction kills the subset claim.

The bar was fixed before testing. It was not changed after seeing data.

## Method

I parsed the repaired 1,847-pair stream only: `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` (tokenizer identical to `repair_parse.py`). I never used `canonical.py`. I never touched R5005.

92 has 22 windows on the repaired stream. The verbal-governor subset is the 8 windows governed by verbal governors (00='pour', 94='ne', 84='on', 46='que'): @49, @66, @330, @593, @978, @1154, @1379, @1453. @683 ('pour' + A6 frame) and @1022 ('on [92] qui') stay fenced as residuals per the pre-registered evidence. 'la [92]' x3 and 'prenne' @1550 stay fenced as the split question for the red team per the pre-registered adverses. Other governors (40, 98, 16, 83, 30, 13, 31, 81) are owned by other targets (seg-92-354-356, fence-92-1218, tail-1376-on92) and are out of scope here.

Standing values used: 00='pour' (A9 granted, leg-(1) downgraded), 84='on' (A15 granted), 46='que' (banked GT), 29='er' (banked GT), 79='tout' (A5 granted). 94='ne' is battery-promoted, pending ratification. 59='est' is provisional. Canonicality caveat stands (68 of 70 upstream row offsets unvalidated).

## Window-level evidence

- @49 (a1_01): `96-00-92-79-37` = 'par pour [92] tout [37]'. 00='pour' heads an infinitive slot. 92=verb (INF) parses. No forced contradiction.
- @66 (a1_01): `12-94-92-69-13` = 'n ne [92] [69] [13]'. 94='ne' heads a finite-verb slot (expletif 'ne'). 92=verb parses. No forced contradiction. NOTE: @1549's 94 is word-internal to 'prenne' (prenne-92-noun battery), so @66 is the only true ne-governor of 92. No cross-window tension.
- @330 (a2_05): `19-00-92-50-45` = '[19] pour [92] [50] ce'. 92=verb (INF) parses. No forced contradiction.
- @593 (a4_00): `09-00-92-79-85` = '[09] pour [92] tout [85]'. 92=verb (INF) parses. No forced contradiction. The '00-92-79' trigram is byte-parallel to @49.
- @978 (a6_01): `01-00-92-07-76` = '[01] pour [92] [07] [76]'. 92=verb (INF) parses. No forced contradiction.
- @1154 (a6_09): `02-00-92-29-80-17` = '[02] pour [92]er [80] fois'. 00='pour' + 92 + 29='er' (banked GT). This is 'pour' + verb-stem + infinitive ending: the smoking gun. 92=verb parses AND is forced by the 'er' ending. No forced contradiction.
- @1379 (a7_06): `89-84-92-69-13` = '[89] on [92] [69] [13]'. 84='on' (A15) heads a finite-verb slot. 92=verb (VFIN) parses. No forced contradiction. The tail '@1376' parse belongs to queued tail-1376-on92; I test only the governor slot.
- @1453 (a7_09): `33-46-92-62-61` = '[33] que [92] [62] [61]'. 46='que' heads a subjunctive slot. 92=verb (V-subj) parses. No forced contradiction.

## Per-clause pass/fail

1. Clause 1 (>=3 subset windows parse with zero forced contradiction within the subset): **PASS**. 8/8 subset windows parse under 92=verb (stem/inf/fin per governor). No window forces 92 to be non-verb.
2. Clause 2 (any new forced contradiction kills): **PASS** (no kill). No new forced contradiction was found in the subset. The known anomalies (@683, @1022 residuals; 'la' x3 and 'prenne' @1550 nominal governors) were fenced before testing and are excluded or fenced by the pre-registered bar and adverses.

Stem-vs-whole note: @1154 shows 92 as a stem ('pour [92]er'), while @49/@330/@593/@978 show bare 92 under 'pour'. The bar's claim is "stem/inf/fin per governor", so inflectional-form variation is anticipated, not a contradiction. A10's 'pour'+bare-stem lesson is specific to 33/86; nothing forces 92 to be only a bare stem (92 also stands alone as a whole infinitive). Word-boundary/segmentation questions belong to seg-92-354-356, not this battery.

## Adverses

- Nominal governors ('la' x3 @203/@321/@1607, 'prenne' @1550) fenced as the split question for the red team: **answered by fencing with stated cause**. Per §7, split/polyvalence is red-team business; this battery tests the verbal subset only and never decides 92's global class.
- Coordination with prenne-92-noun (noun arm): **do not duplicate**. NOTE for red team: prenne-92-noun returned **kill** on 2026-10-08, so the noun arm is dead. This target's subset promote does not decide the global class; the split question is still red-team business, now with one arm resolved.

## Verdict

**promote** — 92=verb on its verbal-governor subset (stem/inf/fin per governor). All bar clauses pass. Every listed adverse is answered (fenced with stated cause). The split/polyvalence consequence for 92's global class is escalated to the red team; this battery names the verb class on the subset only.
