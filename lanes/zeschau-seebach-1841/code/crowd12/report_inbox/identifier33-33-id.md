# 33-INFINITIVE IDENTIFIER — report (round 12, WO1)
**Executor:** 33-IDENTIFIER · **2026-10-07** · Prereg: `code/crowd12/identifier33/PREREG.md`
(2026-10-07 21:26:21 UTC, before any round-12 computation) · Script:
`code/crowd12/identifier33/identifier33.py` · Results:
`code/crowd12/identifier33/identifier33_results.json`
**Work order (STATE.md):** name 33's specific infinitive via the 8 "pour 33" frames.

## Pre-registered candidate set + bar (summary)
- **Candidates:** 461 infinitives, mechanical: `is_inf` (ends er/ir/re, len>3) ×
  n("pour X")≥3 on the clean 3.96M diplomatic pool (verified 3,960,009 tokens;
  = corpus minus AZ-newspaper/harvest-log/adb). 8 non-verb false positives
  hand-dropped with reasons (notre, votre, titre, premier, ministre, quatre,
  maître, homère). Ranked; frozen before tail queries.
- **R (rate):** X ∈ top-10 by n("pour X") on pool∖v8 (disjoint from v8 ⇒ R⊥T).
  Top-10: faire, être, avoir, aller, obtenir, donner, mettre, assurer, arriver,
  atteindre.
- **T (tail, v8 only, n("pour INF")=149):** unique argmax, n≥2, of the
  cluster's tail shape (F-A: "pour X W pour"; F-D: "pour X par [e-word]"
  cond. 96="par"; F-E: "pour X W qui" cond. 64="qui"; F-B/F-C: n/a, tails
  unglossed).
- **L (license, v8):** ΣT ≥ 1 else FENCED. **A (anchor hand-read):** confirmation only.
- **Bar:** ID = R∧T same X ∧ L ∧ A · LEAN = exactly one of R/T (L pass); T-n/a
  clusters need R + *striking* A · NULL = neither/divergent · FENCED = L fails.
  I recommend; red team adjudicates. F77 ("ment" void), F59 (no tiling counts) honored.

## Per-cluster findings
| cluster | frames | T (v8) | L | R | A | verdict |
|---|---|---|---|---|---|---|
| F-A | @186,@1245 "pour 33 16 pour" | 0 | **FAIL** | – | – | **FENCED** |
| F-B | @408 "pour 33 01 02" | n/a | n/a | top-10 (base rate) | not striking | **NULL** |
| F-C | @467,@1088 "pour 33 79 80" | n/a | n/a | top-10 (base rate) | not found/striking | **NULL** |
| F-D | @846 "pour 33 96(par) 40(e)" | 0 | **FAIL** | – | – | **FENCED** |
| F-E | @936,@1630 "pour 33 21 64(qui)" | 0 | fail* | – | – | **NULL** (+lead) |

\* F-E's v8 L-failure is **underpowered, not a true fence** (post-hoc): pool
(3.96M, 23,347 "pour") licenses "pour INF W qui" **29×**; v8-expected count
0.83 ⇒ P(v8-zero)≈0.44. Zero was the modal outcome.

- **F-A sharpened (post-hoc pool read):** "pour INF W pour" = 49× pool, but
  **always** infinitive-coordination (W = mais/non/et/ou/ni/soit) or
  beneficiary-NP ("wellington pour assurer") — the second "pour" is always
  infinitival. Cipher has 67 (et/veut fork, non-infinitival) after the second
  "pour" ⇒ "pour 33 16 pour 67" unlicensed. F81 confirmed + sharpened.
- **F-D:** "pour INF par [e-word]" = **0/3.96M** (95% UB ≈ 0.013%) ⇒ strong
  fence, conditional on 96="par"-prov. Second tension: the e-word's second
  chunk would be 62 ("on"-fenced-lead) — fits no natural e-word (écrit/exemple/
  erreur all mismatch); N28's ungranted "par écrit, on me" parse is chunk-short
  (5 chunks par-é-crit-on-me for 4 groups 96-40-62-21).
- **F-E lead (post-hoc, one check):** pool W-slot = **"ce" 14/29 (48%)**,
  demonstratives 62% ⇒ **21="ce"** (lead-grade; collides with 87="ce"-prov —
  allowed homophonically, flagged cost per lane note; RIVAL: N28's ungranted
  21="me" @850, which makes F-E "pour INF me qui" ungrammatical — fixed
  substitution forces a choice, reported below). Given W="ce": "pour **savoir**
  ce qui" ×2, unique modal (~73× enriched over P(savoir|"pour")). **BUT**
  F22 granularity objects: savoir = 2 syllables vs 33 = 1 group; under
  whole-word reading the only monosyllabic "pour X ce qui" is "faire" ×1.
  ⇒ 33 unnameable here; savoir NOT recommended even at LEAN.
- **F-B:** 26/149 v8 "pour INF" have "la" in −8 (not discriminating); the
  cipher's 34("i")-69-26 gap before "pour" matches no v8 adjacency. NULL.
- **F-C:** "00 33 79 80 06" ×2 (@467/@1088) ⇒ **same infinitive, unidentified**
  (replication datum, not an ID). @467: zero v8 "pour INF" with "par" shortly
  before. @1088: 3 "qui…pour INF" (remplacer/gâter/aller), non-convergent. NULL.

## Headline finding: the 33-value paradox (structural, unresolved)
F79 GRANTED both I1 ("pour 33" ×8 ⇒ 33 = infinitive) and I4 ("33 29" ×5 =
stem+"er" ⇒ 33 = stem chunk). Under fixed substitution + F22 granularity
(parl|er), 33 is ONE chunk and cannot be both:
- **Fork S (stem):** infinitive = "33"+suc. Then F-D's suc=96="par"-prov would
  be an infinitive ending — no French infinitive ends /paʁ/ ⇒ Fork S refutes
  96="par" (breaks the "parmi" @1196 leg; expensive).
- **Fork W (whole-word):** 33 = complete monosyllabic infinitive, suc = next
  word. Then I4's "33 29" = "INF er" is ungrammatical ⇒ Fork W refutes the I4
  stem+"er" reading (F79's C1 keeps I1×8 + I2×1 = 2 kinds, so the *class*
  verdict likely survives, but a leg dies).
- No per-frame infinitive can be responsibly named until the fork resolves.
  Further resolution paths: (a) suc-homophone hypothesis — 16/01/79/21 as
  "-er"-ending homophones (breaks 16="i"-lead, 96="par"-prov; for
  side-homophonic-rebuild); (b) 00≠"pour" at some frames (breaks strong lead).

## Recommendation
- **Overall: NULL** — 33's specific infinitive cannot be named. No ID, no LEAN
  for any value; F-A/F-D FENCED (frames, not values); F-B/F-C/F-E NULL.
- Named leads (not recommendations): 21="ce" (F-E W-slot, 1 post-hoc check;
  vs 21="me" N28-ungranted — needs adjudication); F-C pair = one unknown
  infinitive ×2.

## Evidence paths
- `code/crowd12/identifier33/PREREG.md` (bar + fork, pre-registered)
- `code/crowd12/identifier33/identifier33.py` (DROPS with reasons; R/T/L)
- `code/crowd12/identifier33/identifier33_results.json` (461 candidates,
  per-cluster tables, `posthoc_sensitivity` + `checkA_handread` labeled sections)
- v8 "pour INF" concordances: /tmp/v8_pourinf_ctx.txt (149 lines; ephemeral —
  regenerable via the script's tokenizer)

## What would break the tie
1. **Fork S vs W:** an independent stem/whole-word discriminator for 33 —
   e.g., a pencil-GT-anchored multi-group word containing 33, or I4-window
   re-analysis under whole-word reading.
2. **21="ce" vs 21="me":** 21's contact profile vs 47/87 ("ce") and vs
   object-pronoun positions; another "pour 33 21" frame; adjudication of
   N28's "on me" (chunk-count audit of "par écrit, on me" @845–853).
3. **F-E value:** a second independent check for "pour [X] ce qui" with
   monosyllabic X, or cipher-side confirmation of 21="ce".
4. **F-D:** if 96≠"par", the fence evaporates — re-run T_D unconditionally
   (fallback "pour INF W1 W2" was base-rate-dominated: faire 12).
5. **Methodology:** v8's 149 "pour INF" underpowers rare-shape fences —
   future batteries should pre-register pool-level license checks (this
   battery's L-bar fired at P≈0.44 under H0 for F-E: noise, not signal).
