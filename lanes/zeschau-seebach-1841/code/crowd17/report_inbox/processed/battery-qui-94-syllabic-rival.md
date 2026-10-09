# Battery verdict: qui-94-syllabic-rival — NULL (fenced to red-team duality adjudication)

- Target: `qui-94-syllabic-rival` (priority 2)
- Date: 2026-10-08
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `repair_parse.py`; `canonical.py` never touched)
- Verdict: **NULL** — no coherent word-internal parse at battery grade; window fenced to the red-team 12/94-duality adjudication with gathered evidence. Nothing decided.

## Bar (verbatim)

"one coherent word-internal parse with all five pairs assigned; else fence to the red-team duality adjudication without deciding it"

## Bar as numbered clauses

1. **Produce one coherent word-internal parse assigning all five pairs (77, 62, 94, 64, 98) at battery grade** — i.e. using only pencil/granted/promoted/provisional values, no invented values, one French word. → **FAIL** (see §Parse attempt).
2. **Else fence the window to the red-team 12/94-duality adjudication with gathered evidence, deciding nothing.** → **TAKEN** (see §Fence).

## Method

1. Read `BATTERY-PROTOCOL.md` first; created `locks/qui-94-syllabic-rival.lock` on start.
2. Extracted window @507–511 from the repaired stream: **77-62-94-64-98**, row a3_00. Context @503–506 = 39-68-21-67; @512–517 = 65-88-56-87-77-80.
3. Re-derived the evidence-field distributional claims byte-exact (§Evidence).
4. Tested the particle reading ("ne" + "qui") against 1841 French grammar; tested syllabic candidates for a one-word parse.
5. Standing values used: 77="le" (provisional), 94="ne" (STRONG LEAD, R17-001), 64="qui" (granted). 62 and 98 open (62="il" killed in non-94 windows per frame-20-62-94 null; 98="vient" is battery-level, unratified).

## Evidence (re-derived, not cited)

- 94 windows: 37. Followers of 94 containing 64 ("qui"): **1/37** — @509 only.
- 64 windows: 47. Predecessors of 64 containing 94 ("ne"): **1/47** — @509 only.
- 94-64 bigram offsets on the repaired stream: **[@509] only** (unique).
- 'prenne' = 70-12-94 word-internal precedent confirmed: trigram at @347 (row a2_05) and @1547 (row a8_00). 12-94 bigrams additionally at @64 (row a1_01).
- 62 census: 35 windows; top followers 94 x9, 48 x6, 98 x5, 16 x4; top predecessors 21 x5, 20 x4.
- 98 census: 40 windows; top followers 83 x5, 82/80/98/00 x3.

## Parse attempt (clause 1)

Particle reading first: 94="ne" (particle) + 64="qui" (relative pronoun) = **"ne qui" — ungrammatical in 1841 French**. "Ne" is a preverbal negator clitic; "qui" is never a verb. No period construction places "ne" directly before "qui" (cf. the parallel kill: 94-87 "ne ce" ungrammatical, ne-ce-1169 null). **The analytic reading is dead at this window; 94 must be syllabic "ne"** — the same functional slot as word-internal 94 in 70-12-94 "prenne" (pre-n-ne).

One-word candidates with 77="le", 94="ne", 64="qui":
- Best near-miss: **"le mannequin"** = 77=le (determiner) + 62=man + 94=ne + 64=qui + 98=n. Requires **2 invented values** (62="man", 98="n" — zero independent legs each), is determiner+noun rather than one word, and "mannequin" is semantically thin for 1841 diplomatic French. Not battery grade.
- "emmannequiner" (em-man-ne-qui-ner) considered: needs 77="em", 62="ma", 98="ner" — 3 invented values, no legs. Rejected.
- No other French word matches ?-?-ne-qui-? with standing values.
- Note: 98="vient" (battery-level, unratified) is incompatible with ANY one-word parse of this window — recorded as a tension if 98="vient" is later ratified.

Clause 1 **FAILS**: no coherent word-internal parse with all five pairs assigned at battery grade.

## Fence (clause 2 — taken)

Window-level syllabic evidence gathered for the red-team 12/94-duality adjudication (R17-018), **deciding nothing**:

1. **94 is forced syllabic at @509.** The particle reading is ungrammatical, so this window is positive evidence that 94's value "ne" occupies a word-internal syllabic slot — parallel to 70-12-94 "prenne". The duality is therefore positional (analytic vs syllabic), not a value split, at least at this window.
2. **Uniqueness makes it load-bearing.** This is the stream's only 94-64 bigram: 94's sole "qui" of 37 windows, 64's sole "ne" of 47 windows. If the red team resolves the duality, this window is the sharpest single test of the syllabic leg.
3. **Near-miss fenced, not decided.** "le mannequin" (2 ungranted assumptions, determiner+noun split) is recorded for the red team, not promoted.

## Adverses

- "12/94 duality is red-team-owned (§7); this battery gathers only, never decides" — **answered**: the report fences the window to the red-team adjudication and decides nothing. No duality value declared; R17-001 (94="ne" STRONG LEAD) untouched; no standing verdict contradicted or downgraded.

## Caveats

- Canonicality: row a3_00's offset is unvalidated (68 of 70 upstream row offsets unvalidated; only a5_03/a8_05 anchored by pencil glosses).
- 77="le" is provisional; if re-valued, the "le mannequin" near-miss evaporates.
- 98="vient" is battery-level and unratified.

## Follow-ups (null regenerates work)

1. `mannequin-62-98-test` (P2): test 62="man" / 98="n" against 62's 35 windows (note 62-94 x9 "manne", 62-48 x6 with 48="e" banked, 62-98 x5) and 98's 40 windows. Kill or fence the near-miss.
2. `ne-particle-ungrammatical-sweep` (P2): census all 37 94-windows for particle-ungrammatical followers (94-87 "ne ce" known, 94-64 "ne qui" here) → syllabic-vs-particle map for the red-team duality adjudication.
3. `head-77-62-94-noun` (P3): identify the 77-62-94 head (word ending "-ne") under the forced syllabic-94 reading, with left context @503-506 (39-68-21-67; 67=et/veut positional).

## Bookkeeping

- Lock `locks/qui-94-syllabic-rival.lock` created on start with agent id + UTC timestamp; deleted on completion.
- `battery-queue.json`: target `qui-94-syllabic-rival` → status `verdict`, result `null` (temp-file + rename; own entry only; no prior verdict existed — no downgrade).
- R5005, sealed gate instances, and the red-team adjudication queue untouched.
