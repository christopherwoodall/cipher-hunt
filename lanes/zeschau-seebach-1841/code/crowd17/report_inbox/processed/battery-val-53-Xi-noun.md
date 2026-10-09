# Battery verdict: val-53-Xi-noun — wider search for "[X]i"-shaped nouns/adjectives with "Xn" also French

- Target id: `val-53-Xi-noun` (priority 3)
- Claim: "wider search for '[X]i'-shaped French nouns/adjectives X with 'Xn' also French (beyond 'boni'/'merci'/'ami' family)"
- Date: 2026-10-09
- Worker: battery worker (subagent session 399421b9-8e10-4183-814d-635f943ef34e)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, repair_parse.py tokenization; 1,847 pairs / 96 types re-asserted in-session). All @-offsets are 0-based repaired-stream pair indices. `canonical.py` never used. R5005 untouched. Sealed gates untouched. Red-team queue untouched. No invented numbers.
- Lock: code/crowd17/next-token/locks/val-53-Xi-noun.lock (created 2026-10-09T08:26:35Z, no pre-existing lock, nothing stale; deleted on completion).

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"name X with both 'Xi' and 'Xn' French and the @402 object slot parsing; else close the '[X]i'-noun space"

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1) EXISTENCE: a French noun/adjective X exists, beyond the sibling-exhausted family, such that "Xi" is French (34='i' banked letter) and "Xn" is French (12='n' promoted letter tier) — i.e. the joint [X]i/[X]n constraint is satisfiable at all.
2. (C2) OBJECT SLOT: the named X parses at @402 with zero new assumptions — the surface word at @402-404 is "[53]i" word-internal (ce88-53-wordbound PROMOTE), occupying 88's direct-object slot ("Ce [88] [Xi]...") grammatically.
3. (C3) "53 12" COHERENCE: the named X coheres with the "53 12" x4 windows (@57 "35 53 12 41", @168 "84=on 53 12 48='e'", @708 "35 53 12 48", @1581 "24 53 12 44") — "Xn..." must be French-compatible in all four with zero new assumptions (no revaluing 12, 48, or 84).

Pre-registered kill condition (evidence field): "kill iff none parses at @402 with zero new assumptions."

## Method

1. Re-derived the repaired stream in-session; asserted 1,847 pairs / 96 types. Never used canonical.py. R5005 not touched.
2. Adopted as premises (cited, not re-litigated): ce88-pronoun-frame PROMOTE (53 as 88's complement at @402-403; 45='ce' demonstrative pronoun; locus @400-406 = "11=la 45=ce [88] [53] 34=i [69] [26]"), ce88-53-wordbound PROMOTE ("53 34" one word "[53]i", no boundary — so the @402 surface word IS "Xi"), battery-ce88-53-value NULL (the 'don'-vs-'doni' irreconcilability; its "[X]i" rival sweep is extended here), 12='n' letter tier, 34='i' banked, 48='e' inflectional, 84='on' granted (A15), 17='fois' granted.
3. Enumerated French nouns/adjectives of shape "[X]i" (final -i, per the wordbound promote) against the joint "Xn"-French constraint, in 1841 diplomatic French. Tested every survivor against C2 (@402 object slot) and C3 (the "53 12" x4 windows) on bytes.

## Window-level evidence

**The locus.** @400-406, row a2_08: `11=la 45=ce [88] [53] 34=i [69] [26]` — "Ce [88] [53]i..." The object-slot word at @402-404 is the single word "[53]i"; any candidate X must supply a noun that stands bare as a direct object here.

**The "53 12" family (re-verified).** @57: `35 53 12 41`; @168: `84=on 53 12 48='e'`; @708: `35 53 12 48`; @1581: `24 53 12 44`. With 12='n' and 48='e', these read "X"+"n"+("e"|41|44). 53 census re-verified: 11 windows at @16/@57/@168/@403/@411/@708/@804/@1020/@1280/@1473/@1581.

**Enumeration.** French nouns/adjectives ending in final -i, each tested for "Xn" French:

- FAIL C1 outright ("Xn" not a French word or word-start): merci (mercn), ami (amn→"amne" only), ici/parmi/aussi (not nouns/adjs; icn/parmn/aussn), pari (parn, proper-only), taxi (taxn), ski (skn), défi (défn), souci (soucn), ennui (ennun), appui (appun), oubli (oubln), cri (crn), pli (pln), péri (pérn), alibi (alibn), rabbi (rabbn), fini (finn, proper-derived only; "finne" not common French), uni (unn), puni (punn), muni (munn), béni (bénn), bruni (brunn), jauni (jaunn), verni (vernn), terni (ternn), garni (garnn), fourni (fournn), banni (bannn), joli (joln), poli (poln), demi (demn), blanchi (blanchn), grandi (grandn), toi/moi (pronouns, not noun/adj), lui ("lu" verb form; lun), si/mi/fi ("le si"/"le mi"/"faire fi" nouns but sn/mn/fn), mini (not 1841 French; minn), kiki/pipi (familiar; kikn/pipin). The -is/-it/-u/-e final families (souris, tapis, avis, détruit, voulu, sosie...) do not match the "[X]i" shape (34='i' must be word-final per the wordbound promote).
- WEAK C1 pass, killed on C2/C3 — the only three X with "Xi" a noun/adjective AND "Xn" a French word or clean word-start:
  1. X="bon": "boni" (le boni, noun) / "bonn" (word-start: bonne, bonnet, bonheur). C2 FAIL: bare singular countable "boni" cannot stand as a direct object without a determiner (*"Ce [88] boni" — French bars bare singular count nouns in object position). C3 FAIL: @168 "84=on 53 12 48" = "on bonne" — "on" (granted pronoun) requires a finite verb; "bonne" is an adjective → ungrammatical with zero new assumptions (12 stays 'n', 48 stays 'e'). @16 "91 53 17=fois" = "[91] bon fois" — masculine "bon" against feminine "fois" (agreement fail), bare pre-nominal adjective without determiner (syntax fail).
  2. X="so": "soi" ("le soi" philosophical noun; disjoint pronoun) / "son" (word: le son / possessive). C2 FAIL: "soi" cannot be a direct object — it is prepositional or reflexive-only (*"Ce [88] soi"; "le soi" needs its article and is philosophical jargon, a new assumption in 1841 diplomatic French). C3 FAIL: @168 "on sone" — "sone" is not French; @708 "[35] sone" likewise.
  3. X="co": "coi" (adj: "se tenir coi") / "con" (word). C2 FAIL: "coi" is an adjective with no nominalized use (*"Ce [88] coi"; *"le coi" does not exist). C3 FAIL: @168 "on cone" — "cone" is not French ("cône" needs its circumflex; "conne" needs double n).

No fourth candidate exists: every other French "[X]i" noun/adjective fails the "Xn"-French half of the joint constraint, and the three that pass it weakly all fail the object slot and the "53 12" windows on bytes, with zero new assumptions.

## Per-clause pass/fail

1. **C1 FAIL (exhaustion).** Beyond the sibling-exhausted family, only "bon"/"so"/"co" satisfy even the weak joint constraint; no clean satisfier exists.
2. **C2 FAIL (kill grade).** None of the three survivors parses in the @402 object slot: "boni" needs a determiner, "soi" cannot be a direct object, "coi" is not nominalizable. The pre-registered kill condition ("kill iff none parses at @402 with zero new assumptions") is met.
3. **C3 FAIL (kill grade).** All three survivors are forced false by the "53 12" windows: "on bonne" / "on sone" / "on cone" are ungrammatical or non-French at @168 (and @708 identically), with standing values 12='n', 48='e', 84='on' untouched.

No standing or red-team verdict contradicted or downgraded. No battery verdict downgraded (ce88-pronoun-frame, ce88-53-wordbound, battery-ce88-53-value, and the §7 standings are used as premises, not re-litigated).

## Verdict: KILL

The "[X]i"-noun space is closed. Exhaustive enumeration of French nouns/adjectives of shape "[X]i" shows the joint "[X]i"-French + "[X]n"-French constraint admits only three weak candidates ("bon", "so", "co"), and each is forced false by the @402 object slot and the "53 12" x4 windows with zero new assumptions. The bar's else-branch ("close the '[X]i'-noun space") and the pre-registered kill condition are both satisfied. This kill touches only the [X]i hypothesis family — it does not name 53's value and does not disturb the "don"-vs-"doni" irreconcilability already packaged for the red team by battery-ce88-53-value.

## Follow-ups

None required (kill verdict; §4 follow-ups are mandatory for nulls only). The surviving open question — 53's value under the jointly-unsatisfiable "53n" x4 / "53 34"-word-internal constraints — is already queued as `poly-53-redteam-package` (priority 2) for the red-team §7 docket.

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-val-53-Xi-noun.md (this file).
- Queue: `battery-queue.json` -> `val-53-Xi-noun` status `verdict`, result `kill`, date 2026-10-09 (pre-write assert: prior status `queued`, verdict null; own entry only; temp-file + rename; JSON re-validated).
- Lock created at start, deleted on completion.
- canonical.py never used; R5005, sealed gates, red-team adjudication queue untouched.
