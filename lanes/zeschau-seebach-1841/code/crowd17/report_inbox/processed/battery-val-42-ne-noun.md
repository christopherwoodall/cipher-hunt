# Battery verdict: val-42-ne-noun — KILL ([42ne]-noun has no compatible value)

**Target:** `val-42-ne-noun` (P3)
**Date:** 2026-10-09
**Worker:** battery worker (subagent 0700e692-dc2a-41be-b6aa-30a8c3b68b81)
**Claim:** Search 42's n=20 windows for a noun value compatible with a -ne-final French word (peine/haine/donne-family).
**Stream:** repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.

## Bar (verbatim from battery-queue.json)

"Search 42's n=20 windows for a noun value compatible with a -ne-final French word; kill [42ne]-noun if no compatible value exists"

## Numbered clauses (restated BEFORE testing; not modified after)

1. **C1 (name arm):** Name one specific French noun value for 42 compatible with a -ne-final French word, parsing in ≥2 independent windows with battery-grade evidence (clean grammatical parse under standing values, ≤1 ungranted assumption per window, no invented grammar or values — §3).
2. **C2 (kill arm):** If no compatible value exists — i.e., no French noun value for 42 can form a -ne-final word in the '42 94' windows while satisfying 42's standing constraints — KILL [42ne]-noun with stated cause.

## Method

1. Read BATTERY-PROTOCOL.md first; created `locks/val-42-ne-noun.lock` on start (2026-10-09T17:31:57Z), no prior lockfile present; entry confirmed queued/verdictless before testing.
2. Re-derived the repaired stream in-session (asserts held: 1,847 pairs, 96 types).
3. Full 20-window census of 42 re-derived (0-based @79/@205/@219/@266/@282/@428/@464/@488/@493/@543/@784/@1072/@1144/@1187/@1410/@1503/@1617/@1794/@1814/@1838 — byte-identical to prior censuses).
4. Byte-confirmed the three '42 94' windows (the only loci where the [42ne] one-word composition can apply): @493 (`78 [42] 94`, row a2_11), @784 (`24 [42] 94`, row a5_04), @1794 (`56 [42] 94`, row a8_09).
5. Built the -ne-final French noun inventory from the lane period corpus (`code/side-period/corpus/`, 59 French files, 34.5M chars; German allgemeine-zeitung/adb-zeschau/metternich excluded per standing method): 723 -ne-final types at freq≥3.
6. Adopted (never re-litigated): 42=["noun","cls"] (R19-055); 42 systematically determiner-less in argument positions → value restricted to bare-capable nouns (`val-42-det-gap` PROMOTE); T3 "29 42"×3 demands "er"+42 = one French word (adopted fence); 94='ne' STRONG LEAD (R17-001); noun is the only live class for [42ne] (`frame-42-94-leftward`: verb/adjective/adverb/pronoun arms dead or class-contradicting); 78='ver' LEAD (deferred, R16-005) — not a determiner; 24 = finite-modal (battery-promoted) — not a determiner; 56 class open — not a determiner under standing values; §7 (no battery polyvalence).

## The compatibility test

The [42ne]-noun hypothesis requires 42 to be the STEM of a -ne-final French noun ("[42]ne" one word, 94 as word-final 'ne' syllable). For any candidate value S to be COMPATIBLE, it must simultaneously satisfy:

- (i) **Word demand:** S is a standalone French word (42 is a word in its 17 non-'42 94' windows — subject/object/predicate slots per `subj-42-class` six frame-legs and `noun-42-value` demand (b)).
- (ii) **Syllable demand (T3):** "er"+S is a French word ("29 42"×3, adopted fence).
- (iii) **-ne demand:** S+"ne" is a French NOUN (the [42ne] word must be a noun — the only live class).
- (iv) **Bare-noun demand:** S is bare-capable (42 is determiner-less in all argument positions, `val-42-det-gap`; the three '42 94' windows have no determiner before 42 under standing values — 78 is 'ver'-syllable lead, 24 is finite-modal, 56 is class-open).

### Inventory result

Corpus-wide computation over 41,923 word types (freq≥3): exactly **ONE** stem S satisfies (i)+(ii)+(iii) jointly — S="re" ("erre"×24, "rene"×21). This S was already tested and killed in `noun-42-value` ("erre/re": @79 "l'erre" fits, all 16 standalone windows fail — bare "re"/"rêne" ungrammatical; score 1/20, FAIL).

All other -ne-final French nouns fail at least one demand:
- Stems that are standalone nouns (chai→"chaîne", lai→"laine", tribu→"tribune", cor→"corne", don→"donne", ton→"tonne", pan→"panne", van→"vanne", colon→"colonne", lion→"lionne", chien→"chienne", baron→"baronne", paysan→"paysanne", patron→"patronne", gardien→"gardienne", comédien→"comédienne"): EVERY one requires a determiner — none is bare-capable → all fail (iv). Additionally, none forms a French word with "er"+S ("erchai", "erlai", "ertribu", "ercor", "erdon", "erton", "erpan", "ervan", "ercolon", "erlion", "erchien", "erbaron" — all non-words) → all fail (ii).
- Stems that are not standalone words (pei→"peine", hai→"haine", vei→"veine", scè→"scène", chaî→"chaîne" [archaic stem], plai→"plaine", rei→"reine", gê→"gêne", person→"personne", couron→"couronne", zo→"zone", montag→"montagne", campag→"campagne", lig→"ligne", dig→"digne", vig→"vigne", consig→"consigne", sig→"signe", cyg→"cygne", peig→"peigne", règ→"règne"): all fail (i) — they cannot be 42's value in the 17 word-42 windows.
- Pronoun stems (mien→"mienne", sien→"sienne", tien→"tienne"): excluded — contradict R19-055's noun-class grant (flagged in `val-42-det-gap` C3).
- Proper-name edge case ("jean"→"Jeanne"): "Jean" is bare-capable, but "er"+"jean" is not a French word (fails T3/ii), "Jeanne" fails at @784 under standing values (finite-modal 24 + noun ungrammatical — same failure as `frame-42-94-leftward` W2), and naming a specific proper name on one window violates §3 (invention).

### Window-level confirmation (the three '42 94' loci)

Even setting the inventory aside, no -ne noun parses as a BARE word in the three windows:
- @493: `[78] [42ne] [02]` — 78 is 'ver'-syllable lead (R16-005), not a determiner; "[42ne]" would be a bare noun in object/subject slot → ungrammatical for every common-noun candidate.
- @784: `[24] [42ne] [74]` — 24 is finite-modal; "[modal] [bare-noun]" ungrammatical regardless of the noun chosen.
- @1794: `[56] [42ne] [59=est] [37]` — 56 is class-open (not a determiner under standing values); bare-noun subject of "n'est" ungrammatical for every common-noun candidate (corpus: bare "erreur" = 0/34.4M chars vs "l'erreur" 86× — `noun-42-value`; the same zero applies to all bare common nouns in subject position).

## Per-clause pass/fail

1. **C1 (name arm): FAIL — does not fire.** No compatible value exists; naming any value would invent data (§3). The sole triple-constraint survivor ("re"/"rêne") was already killed at 1/20.
2. **C2 (kill arm): FIRES.** Exhaustive inventory search (723 -ne types, 41,923-word vocabulary) finds no French noun value for 42 satisfying demands (i)–(iv) jointly. The [42ne]-noun hypothesis is rejected at the lane's distributional standard.

## Verdict: KILL

**[42ne]-as-noun-word is dead.** There is no noun value for 42 compatible with a -ne-final French word: the only stem satisfying the joint word/syllable/-ne constraints ("re") was already killed on bare-noun grounds, and every other -ne-final noun's stem either is not a standalone word, fails the "er"+S composition, or requires a determiner that 42's windows never supply.

## Scope of the kill

- KILLS: the "[42]ne" one-word composition with noun class — the hypothesis framed in `frame-42-94-leftward`. Since noun is the only live class for [42ne] (verb/adjective/adverb/pronoun arms dead or contradicting R19-055), this closes the one-word composition entirely.
- CONSEQUENCE: the three '42 94' windows (@493/@784/@1794) must parse as "[42-N] + ne(clausal) + X" (composition (b), already the standing alternative per `subj-42-class` C3) — 42 as standalone noun, 94 as the clausal negation particle.
- UNTOUCHED: 42=["noun","cls"] (R19-055 grant); A1 predicative frame; the T3 "29 42" fence and its "er[42]" rival; the 42-06 verb legs and their escalated polyvalence question; `val-42-det-gap`'s bare-capable restriction; all standing/red-team verdicts; §7 intact (no polyvalence declared).
- This kill is consistent with (not a downgrade of) `frame-42-94-leftward` NULL: that battery found [42ne]-noun "live but docket-gated"; this battery exhausts the value inventory and closes it.

## Adverses

None listed on the target. Standing-constraint check: no red-team verdict contradicted or downgraded; the kill narrows the hypothesis space within standing premises.

## Canonicality caveat

Rows a2_11, a5_04, a8_09 carry unvalidated upstream offsets; all @-offsets are repaired-stream 0-based indices per protocol.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/val-42-ne-noun.lock` created on start (2026-10-09T17:31:57Z, agent 0700e692-dc2a-41be-b6aa-30a8c3b68b81), no prior lockfile; deleted on completion (verified gone).
- `battery-queue.json`: `val-42-ne-noun` status `queued` → `verdict`, `verdict: {"result": "kill", "report": "code/crowd17/report_inbox/battery-val-42-ne-noun.md", "date": "2026-10-09"}` (temp-file + rename; pre-write assert confirmed queued/verdictless — no downgrade; JSON re-validated; only this entry touched).
- R5005, sealed gates, red-team adjudication queue untouched. No invented numbers: every @-offset traces to the repaired stream re-derived in-session; corpus counts from `code/side-period/corpus/` (59 French files).
