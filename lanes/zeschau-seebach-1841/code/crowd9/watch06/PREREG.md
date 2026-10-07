# PRE-REGISTRATION — 06-FALSIFIER-WATCH round 9 (2026-10-07)
## Hunt against: 06="ent" iff pre=82 (F61, crowd8/frenchman; conditioned LEAD)

### The banked falsifier (exact form, F33-form)
F61's grant rests on the F33 conditioning contract (PREREG-ROUND8 §3):
predicted window list **W06 = [579, 737, 1183, 1354]** (n=4, n_eff=3 — the
@1183/@1354 pair is the byte-identical ×2 repeat of the 77-78-94-82-06 5-mer
@1180/@1351). The iff has two legs:
- **Leg →** : pre=82 ⇒ 06 reads "ent"
- **Leg ←** : 06 reads "ent" ⇒ pre=82

The banked falsifier FIRES on:
- **FIRE-IN (domain contradiction):** a 06-window with pre=82 that
  contradicts the "ent" reading (adverse inside the conditioned domain), OR
- **FIRE-OUT (iff break):** a 06-window with pre≠82 that reads cleanly as
  "ent" (adverse to the ← leg), OR
- **FIRE-PART (partition defect):** the census finds pre=82 06-windows NOT
  on W06 — the F33 predicted window list was incomplete ⇒ the
  pre-registration itself is defective (F33: partitions must be
  pre-registered BEFORE classification; an incomplete list voids the form).

### Bars (pre-registered before the census)
- **Kill/demotion recommendation:** single adverse = fenced (lane n≥3 rule).
  ≥2 independent adverses (n_eff≥2, disjoint positions) against the same leg
  ⇒ recommend DEMOTION of the islet to disfavored. ≥3 ⇒ recommend KILL.
  A FIRE-OUT with a full "-ment"-shaped trigram frame (pre≠82 with an
  era-plausible stem+ment shape) breaks the biconditional by itself ⇒ the
  "iff" is downgraded to at most a one-way regularity (recommendation:
  KILL of the conditioning, keep any residual 06="ent" as unconditioned
  null-hypothesis work).
- **"Reads cleanly as ent" (FIRE-OUT) decision rule (F34/F44 by-ear):**
  a pre≠82 06-window counts iff an era reader accepts
  [gloss(pre)]+"ent"+[gloss(suc)] as a French word tail — gloss from the GT
  table {11=la,70=pre,82=m,34=i,29=er,40=e,46=que} and pencil-provisional
  {87=ce,64=qui,59=est,94=ne,77=le}; where gloss is unknown the window is
  NOT counted (conservative; unknown ≠ support). Each counted window is
  recorded with its by-ear sentence so red team can audit the judgment.
- **"Contradicts ent" (FIRE-IN) decision rule:** a pre=82 06-window fails
  iff its contact forces a non-"ent" parse: predecessor-of-82 frame making
  "m" unreadable (e.g. a GT sequence forming an impossible junction), or a
  successor GT group forcing re-syllabification of "ent" into a larger unit
  (e.g. 06→29 "er" is NOT a contradiction — "-enter" is speakable; but a
  GT consonant-initial successor fused with "ent" into a live GT lexeme
  would be). Judgment recorded per window; no manual-tiling bearing counts
  are scored (standing rule).
- **F34/F44 by-ear at the 4 claimed windows:** each of W06 must admit the
  gloss "…[stem]ment" with no contact violation. Failure at any window =
  adverse (fenced at n<3 per F33; 2+ failures ⇒ demotion recommendation).
  The lone-82 window @737 (no 94 prefix) is audited for what precedes
  82@736 — a non-stem contact there is an adverse to the "m'en" leg.
- **Coincidence probe (Nesselrode v8 rates, exact binomial):**
  verify n06=44; compute n82, E[82→06]=n82·n06/1847 under independence,
  exact P(obs≥4). If p>0.05: pre=82 does NO statistically significant
  selection work ⇒ adverse to the conditioner (the islet is 4 windows out
  of 44 with chance-level association; the "iff" is a post-hoc description
  of 4 points, n_eff=3). If p<0.01: the selection is real and the hunt
  moves to content. Either way the number is reported honestly.
  Also: successor-profile comparison of the 4 islet windows vs the other
  40 06-windows (exact, no manual tiling): if indistinguishable, the
  conditioner adds no shape beyond selection.

### Blindness note (honest)
Partial-blindness acknowledged: W06 was visible in crowd8/frenchman/
results.json before this hunt (windows [579,737,1183,1354]); the census
code enumerates independently from the repaired stream and will flag ANY
82→06 window, predicted or not. The decision RULES above were written
before the census ran. GT/pencil tables and era corpora were not consulted
for window candidacy beyond the rule text.

### What counts as success
A fired falsifier with a pre-registered bar = success. A survived hunt
with documented coverage = success. Recommendation PACKAGE only — the
round-9 red team adjudicates kills.

### Addendum (post-census, 2026-10-07): index-convention correction
The frenchman package's `islet_06_ent.windows = [579, 737, 1183, 1354]`
are **82-positions** (`PAIRS[i]==82 and PAIRS[i+1]==6`, s4_verdicts.py:82).
In 06-position convention the predicted list is **W06 = [580, 738, 1184,
1355]**. The independent census found exactly these 4 82→06 windows and
no others ⇒ **no partition defect** (FIRE-PART does not fire). The firing
rules above are unchanged; all window citations below use 06-positions.
