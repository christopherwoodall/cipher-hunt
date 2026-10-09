# Battery report: dislocation-ce-sweep

- Target id: `dislocation-ce-sweep`
- Claim: "register-wide negative-confirmation of the no-bare-'ce'-dislocation rule."
- Date: 2026-10-09
- Worker: battery worker (subagent 0e2d823c-c2a9-4510-a073-d8a14e2b5931)
- Lock: code/crowd17/next-token/locks/dislocation-ce-sweep.lock (created at
  start, deleted on completion; no prior lock for this id existed).

Terms (ASD-STE100): "dislocation" = a topic moved to the front of the
clause, set off by a pause, and resumed by a pronoun ("Moi, je sais" =
"me, I know"). "Tonic" = the stressed form (moi, cela). "Clitic" = the
unstressed form (me, ce). "Negative-confirmation" = a census that fails
to find any counterexample, which supports the rule.

## Bar (verbatim, pre-registered before testing)

battery-queue.json `bars` for this target was null. The bar was fixed by
the chartering follow-up #3 of ce87-topic-licensing (2026-10-09), quoted
verbatim:

"widen the negative census to the full 19th-century register (beyond the
lane's 1841 corpus) as negative-confirmation of this kill. Bar: if a
genuine bare-'ce' dislocation attestation appears, this kill re-opens;
else the kill is confirmed at register level."

Numbered pass/fail clauses (restated before testing, not modified after):

1. Tier A (the lane's 1841-register French corpus,
   code/side-period/corpus/): zero genuine bare-"ce" dislocated topics;
   every "ce," hit classifies as interrogative cleft, "sur ce," formula,
   OCR artifact, or other non-topic use; zero "ce, [infinitive]"
   (reproduces ce87-topic-licensing's census).
2. Tier B (extended 19th-c French: Tocqueville 1835/1840, Hugo 1862,
   data/): zero genuine bare-"ce" dislocated topics.
3. Positive controls: tonic demonstratives "cela,"/ "ceci,"/ "ça,"
   attest the fronted-demonstrative topic slot in both tiers.
4. Verdict rule (chartered): a single genuine bare-"ce" dislocation
   attestation in either tier = the negative-confirmation battery is a
   KILL against the rule (the ce87-topic-licensing kill re-opens);
   zero genuine attestations = the kill is CONFIRMED at register level.

## Method

1. Read BATTERY-PROTOCOL.md first. Created/deleted the lock per protocol.
2. Census script /tmp/ce_census.py (patterns below). All hit contexts
   dumped to /tmp/ce_census_full.json and reviewed manually in full.
3. Exact search patterns: `\b[Cc]e\s*,` (all bare-"ce," hits);
   `\b[Cc]ela\s*,`, `\b[Cc]eci\s*,`, `\b[CÇç]a\s*,` (tonic controls);
   `\b[Cc]e\s*[:;]` (colon/semicolon dislocation variants).
   German allgemeine-zeitung issues (Fraktur OCR, German language) excluded
   from the French-construction census; their file list is named in
   code/side-period/corpus/ and was not searched.
4. Every "ce," hit (23 Tier A + 2 Tier B) and both colon/semicolon hits
   were read in context (±140 chars) and classified. No hit was skipped.
5. R5005, sealed gate instances, and the red-team adjudication queue were
   not touched. canonical.py never used (irrelevant here). No data invented;
   every number traces to the named files.

## Window-level evidence

### Corpora (exact files, byte sizes)

Tier A — 19 French files, 25,681,674 chars, code/side-period/corpus/:
guizot-memoires-t1-gutenberg.txt, guizot-memoires-t2-gutenberg.txt,
guizot-memoires-t3-gutenberg.txt, guizot-memoires-t5-t6.txt,
nesselrode-v7.txt, nesselrode-v8.txt, nesselrode-v9.txt,
nesselrode-v10.txt, pozzo-di-borgo-correspondance-v1.txt,
metternich-papiere-v4.txt, metternich-papiere-v6.txt,
talleyrand-memoires-v1.txt, levant-correspondence-1841-p3.txt,
revue-deux-mondes-1841-q1.txt, revue-deux-mondes-1841-q2.txt,
revue-deux-mondes-1841-q3.txt, revue-deux-mondes-1841-q4.txt,
adb-zeschau-heinrich-anton-von.txt.

Tier B — 3 files, 1,987,682 chars, data/:
gutenberg-30513-tocqueville-t1.txt (De la Démocratie en Amérique I, 1835),
gutenberg-30514-tocqueville-t2.txt (Démocratie II, 1840),
gutenberg-17489-miserables1.txt (Hugo, Les Misérables I, 1862; register
mismatch noted in its provenance file — kept as the widest 19th-c net).

Total register searched: 27,669,356 characters.

### Tier A: 23 bare "ce," hits — all classified, zero topics

- guizot-memoires-t5-t6.txt @942189: "de ce sacr.- / ce, se rapprocher
  des trois autres" — OCR line-wrap; the word is "sacrifice" split at the
  line break ("de ce sacrifice, se rapprocher…", absolute construction).
  Excluded with cause (same hit, same cause, as ce87-topic-licensing).
- guizot-memoires-t5-t6.txt @1743300, @1773375: "Fran- ce," x2 — OCR
  hyphen artifacts of "France" (in English-language quoted passages).
- nesselrode-v10.txt @251411; nesselrode-v8.txt @175844, @497774,
  @554127, @581648; nesselrode-v9.txt @356010, @435333, @472665,
  @477341: "Sur ce," x9 — the valediction formula ("on that note", never
  followed by an infinitive or topic-resumed clause).
- nesselrode-v9.txt @304319: "qui est ce, M. Hubert" — predicate nominal
  ("I do not know who this is, M. Hubert"), not dislocation.
- revue-deux-mondes-1841-q1.txt @1666724 ("Que sera-ce,"),
  @1709571 ("Qu'est-ce,"); q2.txt @1404903 ("qu'étaient-ce,"),
  @1963275 ("Que serait-ce,"); q3.txt @1197955 ("Est-ce,"),
  @1198103 ("Est-ce,"), @1730845 ("Qu'est-ce,"); q4.txt @728885
  ("Qu'est-ce,"), @760605 ("qu'est-ce,"), @2615404 ("Qu'est-ce,"):
  x10 interrogative clefts with subject-verb inversion — not topics.

23 = 9 formula + 10 clefts + 2 OCR hyphens + 1 OCR line-wrap + 1
predicate nominal. **Zero dislocated topics. Zero "ce, [infinitive]".**

### Tier B: 2 bare "ce," hits — both formula

- gutenberg-17489-miserables1.txt @32575, @279912: "Sur ce," x2 —
  valediction formula (Hugo 1862). Zero topics, zero "ce, [infinitive]".

### Punctuation variants: 2 hits — neither a dislocation

- metternich-papiere-v6.txt: "Sur ce; je me suis esquivé" — the formula
  with a semicolon.
- talleyrand-memoires-v1.txt: "à ce: égard" — OCR of "à cet égard".

### Positive controls: tonic forms own the slot

- Tier A: "cela," x291, "ceci," x39, "ça," x5 — exact reproduction of
  ce87-topic-licensing's control counts (291/39/5), which also
  cross-checks that the same French files were searched.
- Tier B: "cela," x29, "ceci," x6, "ça," x12 — tonic fronted-topic
  forms present in the extended register as well.

### Grammar (re-used, not re-fetched)

Littré (1872–77) art. "ce": "ce" is unstressed /sə/; Beauzée
(Encyclopédie): standalone demonstrative uses the forms with added "ci"
and "là" (ceci/cela) — the tonic slot-holders. A clitic cannot carry the
stress a dislocated topic requires. (Established by
ce87-topic-licensing; re-stated here as the rule under confirmation.)

## Per-clause pass/fail

1. Tier A zero genuine bare-"ce" dislocations: **PASS.** All 23 hits
   classified (formula/cleft/OCR/predicate-nominal); the one
   superficially close hit is an OCR line-wrap of "sacrifice", not a
   dislocation; the ce87-topic-licensing census reproduces exactly.
2. Tier B zero genuine bare-"ce" dislocations: **PASS.** Both hits are
   the "Sur ce," formula.
3. Tonic positive controls present: **PASS.** 291/39/5 in Tier A
   (exact), 29/6/12 in Tier B.
4. Verdict rule: **CONFIRM.** Zero genuine attestations across
   27,669,356 characters of 19th-century French.

## Adverses, answered

- None listed on this target (adverses: null).
- No standing verdict contradicted or downgraded: this battery confirms
  the ce87-topic-licensing kill at register level; 87='ce' (promoted),
  cela-87-11, and the skeleton-revision follow-ups (skeleton-1032-revise,
  ce87-1028-role) are untouched. This report makes no cipher-value
  promotion and proposes no skeleton change — "promote" here is the
  battery-level verdict on the target claim only, not a ratified
  solution promotion (those belong to the red team).

## Verdict: PROMOTE

The no-bare-'ce'-dislocation rule holds register-wide: 27.7M characters
of 19th-century French (the lane's 1841 corpus + Tocqueville 1835/1840 +
Hugo 1862) contain zero genuine bare-"ce" dislocated topics and zero
"ce, [infinitive]" attestations; the fronted-demonstrative topic slot is
owned by the tonic forms (cela x320, ceci x45, ça x17 across both tiers).
The ce87-topic-licensing kill stands, confirmed at register level; no
re-opening is warranted. No follow-ups are generated by this battery —
the chartered widening is complete and found nothing.

## Follow-ups

None. This was the follow-up; the widening is done and the negative
result was itself the chartered outcome.

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-dislocation-ce-sweep.md (this file).
- battery-queue.json: `dislocation-ce-sweep` queued -> verdict/promote
  via temp-file + rename (pre-write assert: status queued, verdict null;
  JSON re-validated post-write; own entry only; claim/evidence/adverses
  preserved).
- Lock created on start (agent id + UTC timestamp), deleted on completion.
- Census script and full hit dump: /tmp/ce_census.py,
  /tmp/ce_census_full.json (re-runnable against the named files).
- R5005, sealed gates, red-team queue untouched; no numbers invented.
