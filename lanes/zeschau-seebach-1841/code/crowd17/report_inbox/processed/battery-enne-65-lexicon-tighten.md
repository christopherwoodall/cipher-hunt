# Battery report — enne-65-lexicon-tighten

- Target id: `enne-65-lexicon-tighten` (priority 3)
- Worker: ce1a994f-46c4-472f-97ee-03ba766c9196
- Date: 2026-10-09
- Parent: follow-up #2 of hier-arm-94-nonneg NULL (2026-10-09)

## Bar (verbatim)

confirmed zero hardens the @65 word-final fence; any genuine form re-opens hier-arm-94-nonneg F1

## Bar restated as numbered pass/fail clauses

1. The side-period corpus contains ZERO genuine occurrences of "enne" as a standalone French word form.
2. The side-period corpus contains ZERO genuine occurrences of "erenne" as a standalone French word form.
3. The side-period corpus contains ZERO genuine occurrences of "ierenne" as a standalone French word form.
4. Every apparent hit adjudicates as a non-genuine token (hyphenation fragment or OCR garble) — so no genuine form re-opens hier-arm-94-nonneg F1.

## Method (corpus task — NOT the cipher stream)

- Corpus dir: `code/side-period/corpus/` (63 `.txt` files; provenance in `corpus/PROVENANCE.md`, harvested 2026-10-07).
- Byte count (exact, `find -printf %s` summed): **32,547,082 bytes** over the 63 files. (Claim text said "31.6M-char"; measured total is 32.55M bytes — the 0.9M delta likely reflects an earlier corpus state; it does not affect the census, which is byte-exhaustive on the corpus as it stands.)
- Tokenization: Unicode NFC, tokens = `[A-Za-zÀ-ÖØ-öø-ÿĀ-ž]+` sequences, case-folded to lower; exact whole-token match against "enne" / "erenne" / "ierenne". Total tokens scanned: 4,913,029.
- Every apparent hit re-inspected in ±90 chars of context for adjudication (genuine word form vs hyphenation fragment vs OCR garble).
- `code/side-keyhunt/canonical.py` was never executed (per standing constraint). R5005 untouched.

## Evidence

- "erenne": **0** occurrences, corpus-wide.
- "ierenne": **0** occurrences, corpus-wide.
- "enne": **14** raw occurrences — 0 in the German files (allgemeine-zeitung-augsburg-1841-*.txt, adb-zeschau-heinrich-anton-von.txt), all 14 in French files:
  - 13× "enne-" + line-break + "mis"/"mies" = the word "ennemis"/"ennemies" hyphen-split at the line end (newspaper/OCR layout). Files: guizot-memoires-t5-t6.txt (1), metternich-papiere-v4.txt ("europe^enne" = "européenne" split as "europe-enne", 1), nesselrode-v10.txt (1), nesselrode-v8.txt (1), revue-deux-mondes-1841-q1.txt (3), -q2.txt (4), -q3.txt (1), -q4.txt (1). All 13 are fragments of "ennemis"/"ennemies"/"européenne", not the word form "enne".
  - 1× revue-deux-mondes-1841-q4.txt: "campagnes de Tiu-enne" — OCR garble of a proper name fragment ("Tiu-enne", almost surely Turenne), not a lexical French form.
- Genuine standalone word forms "enne": **0**. Genuine "erenne": **0**. Genuine "ierenne": **0**.

## Per-clause pass/fail

1. PASS — 14 raw hits, all 14 adjudicated non-genuine (13 hyphenation fragments, 1 OCR garble). Genuine count = 0.
2. PASS — 0 occurrences.
3. PASS — 0 occurrences.
4. PASS — no genuine form found; hier-arm-94-nonneg F1 stays closed.

## Adverses

- "enne-word-64 was KILLED": consistent — the kill holds; this census finds no standalone "enne" form to support any word-64 assignment.
- "94='ne' battery-promoted (pending ratification)": no contradiction — this census concerns "enne"/"erenne"/"ierenne" only; nothing here touches the 94='ne' promotion, which remains a red-team matter.
- Result contradicts no standing red-team verdict; no escalation needed.

## Verdict

**promote** — the zero-word-form claim is confirmed on the full byte-counted corpus; the @65 word-final fence hardens.

## Follow-ups

None required (verdict promote, not null). Suggested future tightening (not queued): a French-only, line-join-aware census (de-hyphenate line-end splits before tokenizing) to eliminate the 13/14 hyphenation fragments at source.
