# Battery report: w3-06-29-leftedge — verdict: PROMOTE (Parse A forced)

- Target id: `w3-06-29-leftedge`
- Claim: Pin down W3's '[06]er' left edge at @1817: standalone infinitive '[06]er' vs tail of a longer infinitive ('inventer'-shaped 42-06-29 under promoted 06='ent').
- Date: 2026-10-09
- Worker: battery worker (subagent 7501e343-0486-4c9a-b93a-127ee28c48ba)
- Stream: repaired 1,847-pair / 96-type parse re-derived in-session
  (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
  parsed per `code/side-keyhunt/repair_parse.py`; 1,847 pairs / 96 types
  confirmed). `canonical.py` never used. R5005, sealed gates, red-team
  adjudication queue untouched. All @-offsets 0-based.

## Bar (verbatim, pre-registered before testing)

1. "Does NOT threaten the parent promote verdict: 37-01 = 'satisfait'-shaped finite verb stands either way; this is W3-parse refinement only."
2. "Test both parses against the repaired 1,847-pair stream evidence (word-internal 'en' window at @21 is sole under 43; 42-06-29 'ent'-shaped reading per promoted 06='ent')."
3. "Return promote/narrowed if one parse is forced; null with follow-ups if underdetermined."

Numbered pass/fail clauses (restated before testing, not modified after):

- C1: the returned parse leaves 37-01 = 'satisfait'-shaped finite verb standing (parent promote unthreatened).
- C2: both parses tested against the repaired-stream evidence named in the bar.
- C3: one parse forced → promote/narrowed; underdetermined → null with follow-ups.

## The two parses

Locus (byte-confirmed, row a8_10): `@1813=50 @1814=42 @1815=06 @1816=29
@1817=37 @1818=01 @1819=02`.

- **Parse A** ("42 | 06 29"): 42 is a standalone word; "06 29" is the
  standalone infinitive "entrer" ("ent"+"er"); W3 = "...[50] [42].
  Entrer satisfait/contrefait [02]." = "...[50] [42]. To enter
  satisfies/forges [02]."
- **Parse B** ("42 06 29" = "[42]enter"): one word, tail-of-longer-infinitive
  ("inventer"-shaped: 42="inv", 06="ent", 29="er"); W3 = "...[50].
  [42]enter satisfait/contrefait [02]."

## Findings

### Parse A is forced by the standing registry

1. **42 is noun-class (red-team granted).** `code/table-grid/table-registry.json`
   carries `42: ["noun", "cls"]` (R19-055; confirmed compatible at R20-042
   and R20-081). A noun-class token is a word-tier item. Parse B needs 42
   as a word-initial sub-lexical syllable ("inv" of "inventer") — that is a
   tier split, and the poly-42 venue is DEFERRED to the red team (R20-1341);
   battery workers cannot declare splits (§7: 67 et/veut is the sole true
   polyvalence). At battery grade, with the registry as it stands, Parse B
   is unlicensable.
2. **"06 29" = "entrer" is the forced composition.** 06="ent" is promoted
   (registry `06: ["ent", "prom"]`, R17-007/R20-011); 29="er" is pencil
   ground truth. "ent"+"er" = "entrer" (to enter, go in) — a grammatical
   French infinitive, and the only French word the composition spells.
   06 word-initially is precedented (ent-06 F3: 06="ent" in "entreprenne").
3. **The infinitive-subject frame is grammatical.** "Entrer satisfait [02]"
   = "To enter satisfies [02]": bare infinitive subject + 3sg verb +
   direct object — the construction the parent battery already licensed
   ("Vouloir, c'est pouvoir"; "Partir, c'est mourir").
4. **42 as a standalone noun at @1814 matches its word-tier profile.**
   42's word demand ("42 94" ×3, "59 42" ×2, "76 42" ×3, object slots
   @205/@266/@1503) and R20-081's bare-capable-noun value inventory both
   license 42 as a complete noun word here; "...[50] [42]." ends the
   previous clause with no strain (50's class open, no contradiction).

### Parse B is excluded (and has zero precedent)

5. **Zero precedent for word-initial sub-lexical 42.** 42's syllable-tier
   attestations ("29 42" ×3 @78/@218/@1143) are all word-final/internal —
   42 completing "er-"-initial words — never word-initial. The bar's @21
   analogy cuts against Parse B: battery-en43-wordinternal-census showed
   the word-internal 'en' under 43 is sole/locus-specific; 42 does not even
   have a sole word-initial precedent to stand on.
6. **"42-06-29" is a stream hapax with no family.** It occurs exactly 1×
   (@1814). The other four "42 06" windows (@205/@266/@543/@1187) do NOT
   continue into 29 (followed by 77/73/00/84) — 06 there is the finite
   "-ent" ending, not an infinitive tail. No distributional family
   supports the 3-pair word.
7. **Promoted 06="ent" does not select Parse B.** It composes as "entrer"
   in Parse A just as well as "[42]enter" in Parse B; the discriminator is
   42's class, which selects Parse A.

### Standing-battery conflict (flagged, not adjudicated here)

8. `w5-enter-junction` (battery PROMOTE, 2026-10-09, processed) decided
   this same junction as ONE word "[42]enter" — but on the premise
   "42: class open", which misses R19-055 (42=["noun","cls"]). Its
   kill of "29 word-initial" (battery-elision82-48-x1) is untouched and
   stands — this battery's Parse A has 06 word-initial ("entrer"), not
   29, so that kill does not fire here. The two PROMOTEs conflict;
   **red-team adjudication needed**. Per §5, w5-enter-junction's queue
   entry is NOT downgraded or touched here.

## Per-clause pass/fail

- C1: PASS — "Entrer satisfait/contrefait [02]" keeps 37-01 as the
  'satisfait'-shaped 3sg finite verb; the parent (wordinternal-37-01)
  PROMOTE stands unthreatened. This is W3-parse refinement only.
- C2: PASS — both parses tested against the repaired stream (clauses
  1–7 above); the @21 'en' precedent and the promoted 06='ent' both
  addressed.
- C3: Parse A forced → PROMOTE.

## Verdict: PROMOTE

W3's "[06]er" is the standalone infinitive **"entrer"**; the word boundary
falls **after 42 (@1814)**, not after 50. W3 = "...[50] [42]. Entrer
satisfait/contrefait [02]." The "tail of a longer infinitive"
("[42]enter"/"inventer"-shaped) reading is excluded at battery grade by
42=["noun","cls"] (R19-055).

## Scope

W3 left-edge only (@1814–1816). Names no value for 42 or 50 and no
governor/subject for the infinitive. Untouched: wordinternal-37-01's
PROMOTE, 37's S5-owned value, the deferred poly-42 venue, ent-06,
w5-enter-junction's queue entry (conflict flagged for red-team
adjudication, entry not modified), §7, R5005, sealed gates, red-team
queue. Canonical-stream caveat stands (row a8_10 offset unvalidated).

**Re-open condition:** if the red team declares a tier split for 42
(poly-42 venue), Parse B re-opens; if 42=["noun","cls"] is ever
overturned, this verdict falls with it.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-w3-06-29-leftedge.md`
- Queue: `w3-06-29-leftedge` → `status: verdict`, `result: promote`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; target-id-unique tmp
  `battery-queue.json.w3-06-29-leftedge.tmp` + atomic rename; disk
  re-validated; own entry only; no downgrade; no tmp leftover).
- Lock `code/crowd17/next-token/locks/w3-06-29-leftedge.lock` created on
  start (no stale lock), deleted on completion (verified gone).
