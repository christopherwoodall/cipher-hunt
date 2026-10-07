## phonetician: CV-structure tests of the rotation

- Context: the rotation (chi²=366.3) has killed every coarse linguistic
  mapping (word-position N15; morphological/polyvalence/size/syntactic F43).
  This lane tested FINER phonetic structure among the 16 anchored +
  high-confidence groups using the crib-learned inventory's phonetic values
  (F44), not standard French: open vs closed syllables, inventory tier
  (Tier0/provisional/lead), sonority (consonant-heavy vs vowel-like).
  Pre-registered in `code/side-rotation/prereg_phonetician.md` BEFORE running;
  Fisher exact (Freeman-Halton) on fixed-margin tables, α=0.05.
- Decision: **CONSTRAINED NULL** — all three primary tests null
  (open/closed p=0.2500; tier p=0.3465; sonority p=0.7752, n=16 each).
  Robustness variant T-Pa2 (GT+provisional only, n=11) leans at p=0.0242
  but FAILS the Bonferroni gate (0.0167) and is tier-confounded + sensitive
  to the 78="ver" rival reading — flagged to Red Team, NOT a claim.
- Why: exact enumeration p-values; the T-Pa2 "effect" is entirely "no open
  GT/prov unit in phase C," and all three open C-phase units (77, 78, 52)
  are LEAD-tier — excluding them manufactured the pattern. Power note:
  minimum attainable p for T-Pa's margins is 0.0357, so the Bonferroni bar
  was unreachable by design; simulated power for deterministic alternatives
  is only 0.40–0.44.
- Enlightenment: this is the third granularity where phases refuse linguistic
  meaning (position → morphology → now fine phonetics), while the rotation
  stays loud, global, distributed, and period-3 beyond first-order Markov —
  exactly the table-geometry hypothesis's predicted package (linguistically
  arbitrary columns). The null tightens that fence; it doesn't touch E1.
- For the report: rotation-mystery section — "fine phonetics killed
  (open/closed p=0.25, tier p=0.35, sonority p=0.78; n=16); one gated lean
  (GT+prov open/closed p=0.024, fails Bonferroni, Red Team owns it)."
  Files: `code/side-rotation/phonetician/` (script, results JSON, verdict md).
- Caveats: 9/16 values are provisional/lead/bounded; null kills only STRONG
  deterministic phonetic-phase lockstep, not subtle structure; Fisher
  probability-definition is the conservative exact variant.
