# PREREG — @1351 RESOLVER (round 10, work order 1) — 2026-10-07 ~15:40 CDT

Executor: @1351 RESOLVER. Status: RECOMMENDATION ONLY — red team adjudicates
every status change. No promotion attempted. No kill bar pre-authorized for
the islets (lane n≥3 rule binds); this battery RECOMMENDS ownership of the
window and states the cost to losing readings.

## Standing bars accepted (not re-litigated)
- Canonical parse: repaired 1,847-pair (`code/side-keyhunt/repaired_offsets.json`).
- Rate bars: Nesselrode v8 strict (`code/side-period/corpus/nesselrode-v8.txt`),
  elision-split tokenizer (frenchman round-9 `corpus9.tokenize_elision`).
- No manual-tiling bearing counts (standing rule). No re-litigation of:
  48="ne" kill, H_verb-for-48 kill, 86=que-family refutation, unconditioned
  84s, the three mergers ({87,47}="ce", {77,00}="le", {43,21}="me") —
  NOTE: {77,00}="le" was the UNCONDITIONED merger (F56); F37's 77="le"
  provisional-CONDITIONED is a different, live claim and is NOT re-litigated
  by invoking it here. Refuge concretizations, retired WO-6 bar.
- F33 conditioned polyvalence stands; ISLET 3 (06="ent" iff pre=82) is LEAD,
  falsifier-watch found nothing (round 9), n=4/n_eff=3.

## The three readings (exact definitions)
Window @1351–1356 (0-based repaired pairs; to be re-derived byte-exact in D1).
- **R-a (06-islet parse):** @1353=94 "ne" (negation, prov-strong) +
  @1354=82 "m" (GT) + @1355=06 "ent" (ISLET 3 fires: pre=82) +
  @1356=52 "pas" (STRONG) → «ne ment pas». Silent on @1351/@1352.
  Era: grammatically perfect 1841 French; exact trigram unattested in v8
  (by-ear admissible, attestation gap noted — frenchman Gate 2).
- **R-b (gouvernement parse):** @1351=77 "gouv" + @1352=78 "er"/"ver" +
  @1353=94 "ne" (word-internal syllable) + @1354=82 "m" + @1355=06 "ent" →
  «gouvernement pas». Era: 0/40 v8 ("pas" after "gouvernement" needs an
  intervening verb+ne); ungrammatical adjacency.
- **R-c (77="le"):** @1351=77 "le" (F37 prov-conditioned) + R-a's
  94/82/06/52 → «le [78] ne ment pas» (78 unidentified; frame grammatical
  iff 78 is nominal — conditional, not refuted).

Mutual exclusions: 94=negation (R-a/R-c) vs 94=word-internal syllable (R-b)
— 94 cannot be both (frenchman Gate 6). 77="le" (R-c) vs 77="gouv" (R-b).
R-a vs R-c differ ONLY on 77@1351 (R-a leaves it unresolved under F37's
fenced "gou" exception; R-c fires 77="le" there).

## Decision rules (pre-registered)
- **D1 (byte-exact):** re-derive @1349–1360 from the repaired parse.
  Assert @1351–1355 = 77-78-94-82-06 and @1356=52. If the stream differs,
  the frame is VOID — report, do not adjudicate.
- **D2 (94's role — decided first, gates everything):** two independent
  discriminators, either sufficient to rule out R-b at @1351:
  (D2i) era grammaticality — grammatical "ne ment pas" beats ungrammatical
  "gouvernement pas" (0/40 v8, needs verb+ne) regardless of exact-trigram
  attestation gaps;
  (D2ii) 52="pas" (STRONG) is F33-conditioned on a negation frame — R-a/R-c
  supply 94="ne" @1353 (3 back); R-b supplies no negation particle in range
  (scan @1345–1365 for any other 94="ne" candidate; if none, R-b strands
  52="pas" unlicensed and must demote 52@1356 to "so"/"se"-LEAD with zero
  support — dependency-weight loss).
  R-b dies at @1351 iff D2i AND D2ii both go against it. (One against =
  fenced tension, not a ruling.)
- **D3 (77's value — only if R-b dies):** the F37 "gou" exception at @1351
  existed because the 5-mer might be "gouvernement". If D2 kills the one-word
  parse at @1351, the exception's trigger is gone there and 77@1351 falls
  back to the standing F37 conditioned default (77="le") UNLESS a banked
  @1351-specific adverse blocks it. Check: (a) any banked adverse naming
  77@1351 specifically; (b) the frenchman Gate-5 clitic veto (@1350:
  48=transitive-verb ∧ 77="le" cannot both hold) — 48 is UNIDENTIFIED (F64),
  so the veto constrains a non-existent conjunction, not 77="le" alone;
  record as conditional. If no blocker: R-c owns the window.
  If a blocker fires: R-a owns (77 unresolved, fenced exception stands).
- **D4 (dependency audit):** list every banked value each surviving reading
  needs with its status. A reading needing a killed/refuted value dies on
  arrival. Prefer the reading with strictly stronger banked dependencies;
  record any reading that needs an unbanked assumption as carrying it.
- **D5 (verdict form):** exactly one of {R-a owns (77 unresolved),
  R-b owns, R-c owns}. A split verdict (e.g. R-a+R-c compatible on 94–52
  with 77 resolved per D3) must be stated as R-c with the deduction chain
  shown, not as a hedge.
- **D6 (cost accounting — state explicitly whatever the verdict):**
  (i) 06-islet: ISLET 3 membership is POSITIONAL (pre=82). All three
  readings keep 06="ent"@1355 → the islet CANNOT lose the @1355 window on
  positional grounds under any verdict; record n=4/n_eff=3 unchanged and
  note only the by-ear gloss change ("ne ment pas" vs "gouvernement").
  (ii) 77="le": if R-b wins, the fenced "gou" exception at @1351 becomes
  live "gouv" (77="le" loses the chance to claim @1351); if R-c wins, the
  exception shrinks to @1180-only; if R-a wins, the exception stands as-is.
  (iii) gouvernement thread: if R-b dies at @1351, the thread loses its
  @1351 leg (2nd of 2 five-mer windows; n_eff was already 1 — byte-identical
  body — so the loss is the replication, not an n_eff drop); 77="gouv"
  → @1180-only (stays LEAD: n≥3 kill bar binds, no kill recommended);
  78="ver" islet keeps positional membership (@1352 next=94 regardless)
  but its by-ear "ver" gloss at @1352 was fenced on the unconfirmed host →
  gloss dies there, by-ear support drops to @1181-only. H1c/H1d fenced
  adverses: H1c moot (target reading dead); H1d NARROWS to {37="le",
  64="qui"} (the 37-64 bigram is outside this work order — flagged, not
  adjudicated).
- **D7:** verdict is a RECOMMENDATION with graded confidence. No status
  change self-applied. @1180 is OUT OF SCOPE — its fenced state is not
  touched whatever happens at @1351.

## What counts as success
A byte-exact re-derivation + a verdict that follows D1–D5 from pre-registered
rules + honest D6 cost accounting, including the steelman case for the losing
readings. An honest "D2 inconclusive → HOLD" is success if the bars say so.
