# Battery verdict: bare-subj-corpus

- Target: `bare-subj-corpus` (battery-queue.json, priority 3, status queued)
- Claim: "Corpus census: do bare singular -de-final nouns ever serve as finite-verb subjects in 1841 French? Closes the proper-noun/vocative rescue at grammaticality grade."
- Context: follow-up of noun-38de-1829-host NULL (2026-10-09), which fenced the '[38]de'-final noun fork at @1828 with two causes: (a) determiner absence (grammatical), (b) §7 block (structural). The fence was NOT a kill because "the proper-noun rescue is logically open (names need no determiner)". This battery tests that rescue at grammaticality grade.

## Bar (verbatim, pre-registered)

"attested iff >=1 genuine attestation at battery grade; else fence the proper-noun/vocative rescue"

- C1 (attested): ≥1 genuine attestation of a bare singular -de-final noun as finite-verb subject in 1841 French → PASS
- C2 (fence arm): moot (C1 fires)

## Findings

Repaired-stream caveat: this is a corpus census, not a stream parse; the corpus is code/side-period/corpus/ (97 .txt files, 61,065,841 bytes of 1841 French; revue-deux-mondes-1840-q1.txt is a known 170-byte 500-error stub, excluded). `canonical.py` never used. R5005 untouched.

Method (all steps re-runnable from the corpus dir):
1. Tokenized all 97 files; found 2,606 distinct -de-final tokens.
2. Built a 422-form finite-verb list (3sg/3pl indicative, common subjunctive/conditional forms, 1841 orthography).
3. Regex pass: `-de-final token` + `finite verb`, no determiner/article/adjective immediately before → 681 raw hits.
4. Hand-checked all candidate classes. False-positive classes excluded with cause:
   - l'/d'-elided forms ("l'Irlande", "d'Irlande", "l'étude") — carry an article, not bare.
   - Adjectives ("grande", "profonde", "timide", "sourde", "chaude", "froide", "ronde", "malade" as adjective).
   - Verbs ("demande", "décide", "tarde" as 1sg/3sg verb forms).
   - Idiom objects ("prendre garde", "en aide").
   - Determined NPs ("l'ancien monde", "ce bas monde", "le monde").
   - Locatives after prepositions ("en Hollande sont", "à Dresde avait").
   - Title-determined NPs ("le comte Nesselrode", "l'empereur Claude").
5. Strict pass (capitalized proper noun, no determiner/preposition/title in the two preceding tokens, finite verb after, no elision): **77 genuine hits, 63 distinct**, hand-verified top examples:
   - "Aristide avait pris" / "Aristide était le" / "Aristide fut dupe" (x17 strict)
   - "Mathilde est l'exemple" (x4)
   - "Adélaïde était donc" / "Adélaïde avait tiré" (x3)
   - "Clanricarde est revenu" / "Clanricarde avait remis" (x2)
   - "Clotilde attendent encore" (x2)
   - "M. Baude a essayé" (x6; "M." is a title, not a determiner)
6. Bare COMMON nouns: **zero genuine attestations.** Every common-noun candidate died as adjective, verb, idiom, or determined.

## Verdict: PROMOTE (attested)

C1 fires at battery grade: 77 strict genuine attestations of bare singular -de-final proper nouns as finite-verb subjects in 1841 French. The proper-noun/vocative rescue is LICENSED at grammaticality grade — it is not fenced.

## Scope

- Licenses ONLY the proper-noun fork. The bare common-noun fork stays fenced (zero attestations).
- Does NOT name any value, does NOT resolve @1828's "[38]de", does NOT touch the §7 block (cause (b) of noun-38de-1829-host stands — sub-lexical 38 vs verb-form class is structural, not grammatical).
- Qualifies noun-38de-1829-host's cause (a): determiner absence kills the common-noun fork; the proper-noun fork survives grammatically. For @1828 to use it, "[38]de" would need to be a proper noun — a value claim, not a battery license.
- No standing/red-team verdict contradicted, downgraded, or re-litigated; §7 intact. Canonical-stream caveat stands.

No follow-ups required (promote, not null).

## Bookkeeping

- Queue: `bare-subj-corpus` queued → `verdict`/`promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.bare-subj-corpus.tmp` + atomic rename; disk re-validated; own entry only; no downgrade).
- Lock `locks/bare-subj-corpus.lock`: created on start (agent 2f31aab3, 2026-10-09T19:52:00Z, no stale lock), deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
