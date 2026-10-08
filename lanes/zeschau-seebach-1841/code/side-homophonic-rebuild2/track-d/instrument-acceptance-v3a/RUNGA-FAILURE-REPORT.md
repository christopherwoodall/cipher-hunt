# Rung A failure report (PREREG-D-v3 ladder, per protocol)

Rung A (prompt-v3A.txt, sha256 `84393ae4c5f702f218841636871715e84f790be524d3e380bf4fb283f1fcd85e`)
trial campaign complete 2026-10-07. 3 fresh blind judges × 18 calls (6 blind labels × 3 passes, fresh random order per pass),
54 records, all mechanically audited PASS (first-line-int == extracted_score, word_list == line 2, sha pin on every record).

## Re-registration note
Prompt delta from v2 (targeted at the R13 collapse mechanism): holistic "coherent prose?" scoring replaced with
countable evidence — mandatory Step 1 scan-and-list of identifiable French words/phrases (including spaceless and by-ear
forms), Step 2 score from the count/quality of recovered French. Band anchors rewritten: 0–15 none / 20–35 fragments /
40–55 isolated words / 60–75 words+phrases (degraded but French) / 80–90 long stretches / 95–100 clean. Output envelope:
line 1 int 0–100, line 2 comma-separated word list (or NONE), line 3 one-sentence justification. No steering toward any
candidate; no candidate plaintext was read by any judge; key opened only after all 54 calls logged.

## Verdict: FAIL (against pre-registered criteria)

Binding bar (ladder §3): mT−mS ≥ 30 on 6/6 AND median(truth) ≥ 50.

| seed | truth median (3 passes) | salad median (3 passes) | margin |
|------|----------------------|----------------------|--------|
| 184101 | 65 [65,65,70] | 45 [40,45,45] | 20 |
| 184102 | 62 [61,62,63] | 45 [44,45,46] | 17 |
| 184103 | 68 [67,68,69] | 44 [43,44,45] | 24 |
| 184104 | 65 [60,65,65] | 45 [44,45,46] | 20 |
| 184105 | 65 [65,65,70] | 51 [50,51,52] | 14 |
| 184106 | 68 [66,68,70] | 45 [45,45,46] | 23 |

- mT−mS ≥ 30 on 6/6: **FAIL — 0/6 seeds meet the bar** (observed margins 14–24).
- median(truth) ≥ 50: PASS (65).
- Void-probe diagnostic: median(paraphrase)=98 vs median(salad)=45 — scale not broken (non-binding, symmetry with pilot).
- ±3 pilot-median reproduction: truth YES (65 vs pilot 62); salad NO (45 vs pilot 20.5); paraphrase YES (98 vs pilot 91 — slightly high but direction-consistent).
- Cross-pass stability (task-added bar ≤2): 5 of 18 candidates exceed — 5b0cc51e range 4 [66,68,70]; 51569b66, 30429b0e, a223a3ab, ab83f1d5 each range 5 (e.g. [40,45,45], [65,65,70]).
- Note: truth and salad distributions do not overlap (truth min 60 > salad max 52). Discrimination exists; it is too weak for the bar.

## Diagnosis (in the judges' own words)

1. **The segmentation mechanism is repaired.** Cold judges read THROUGH degradation: truth landed 60–70 with
   word-lists like "chapitre, Myriel, ... la partie de la vie, première, charité" and justifications such as
   "Many French words and short phrases such as chapitre, livre, visite, and la partie de la vie are recoverable
   despite heavy by-ear misspelling." Truth no longer collapses into the salad band. The R13 failure signature is gone.

2. **The salad floor is too high — anchored by the 40–55 band.** The band "many identifiable French words, but only
   as isolated words" fits noise exactly: judges report "A handful of real French words such as quelque, première,
   être, and mettre surface in isolation, but the passage is overwhelmingly repetitive noise with no phrases" and
   score 40–46. Noise passages deliberately contain repeated real French tokens; one judge flagged the mechanism:
   "for 30429b0e, the noise tokens are literally 'me', 'leurs', 'se', which are also real French words."

3. **The truth ceiling is compressed by the 60–75 band.** Truth passages scored 60–70 because judges find words and
   short phrases but "fluent stretches never form" / "nothing longer than a short phrase reconstructs." The pilot's
   62 sat in this same band; the band tops out before the ≥75 needed to clear margins.

4. Net: the v3A band anchors compress BOTH classes toward the middle (truth ~65, salad ~45 → margin ~20).
   No judge failed to attempt segmentation; no anchoring drift to ~25. The bar demands a margin the anchors cannot produce.

## Ladder consequence (per §4)

Strike count: R13 recorded strike one; rung A FAIL does not add a strike (§4: strikes only after all three rungs fail).
**Proceed to rung B** (prompt-v3B.txt: frozen v2 prompt + three synthetic calibration exemplars). Fresh judges, new labels,
same binding criteria. Rung B attacks the anchor-drift mechanism directly, which is the residual failure mode here
(compressed anchors, not segmentation failure).

## Integrity
- Prompt sha256 asserted at judge startup; all 54 records carry the pin.
- Blind labels fresh per rung; zero old-label hits in packages/logs.
- Key (new→old label map) opened only after all 54 calls logged.
- R5005 and sealed gate instances (184201–184204, 184206, 184207) never contacted (tripwire grep before and after: clean).
- Schedule provenance: pkg-1/agent1 from the prior interrupted session (verified intact); pkg-2/pkg-3 judges followed
  the coordinator's message schedules (fresh random per pass); the /tmp scratch schedule files disagreed with the
  message schedules (transcription delta, documented in SCHEDULE-NOTE.md) — the used orders are recorded and pinned.
