## phonetician: pass-1 fuzzy-equivalence rules for the Slider
- Context: the Slider needs explicit matching rules for the crib-bootstrap side-path
  loop. The main fleet's Frenchman proved the encipherer spells by ear and cuts
  inconsistently — I turned that into numbered, graded rules at
  `code/sidepath/phonetic_rules.md` (+ machine-readable `.json`), with every rule
  and every forbidden move citing a lane file.
- Decision: 11 rules (6 SOLID, 4 PROVISIONAL, 1 SPECULATIVE) + an 11-item
  FORBIDDEN list. Graded by evidence strength per the red team's bar:
  SOLID = pencil-crib ground truth or kill-grade adjudication; PROVISIONAL =
  attested-but-conditional or scorer inference; SPECULATIVE = derived from a
  principle, never directly attested.
- Why: the solid rules all rest on ground truth, not statistics. "première" =
  la|pre|m|i|er|e proves written mute-e (R1), letter-level cutting (R9), and the
  crib-anchored fragments; "personne" = per|so|nne @160 vs pers|on|ne @508 proves
  inconsistent cutting (R2) in the same cipher; "prend"→"pre" @1331 proves by-ear
  spelling (R3); "qui erre" = …29(er)+40(e) ×2 proves the er|e split (R4);
  "on ne prend pas", "ne pas [inf]" ×2, the two "en" islets, and 52="so" in
  "personne" prove polyvalence as a mechanism (R5, still unquantified — the
  lane's explicit open problem, F31). F22 (stripped final -er) and the "l'a"
  elision rescue stay PROVISIONAL because one is a scorer inference and the
  other is a single conditional rescue; elision remains uncalibrated per the
  red team. R11 (silent consonants generalize beyond -d-) is SPECULATIVE and
  marked generator-only, never a discriminator.
- Enlightenment: the strongest rule is R1's kill-side twin — the red team's
  §4 kill of 06=/mɑ̃/ died on EXACTLY this ground truth: the model needed
  mute-e unwritten ("demande pas" = ?+06+77) while the crib writes 40 for it
  ("première" = …er+**e**), and observed 06→40→77 is 0×. The crib doesn't just
  license the Slider's fuzziness — it has already killed a CONFIRMED claim
  through the same doorway. The forbidden list (mute-e-unwritten models,
  rigid syllabification, era rates on 29/82/34/40, V29-as-stem, single-reading
  absolutism, formula-minus-mandatory-word) is the red team's body count, and
  the Slider must not reintroduce any of it.
- For the report: methodology section — "phonetic fuzzy-equivalence rules for
  the side-path Slider" with the 6/4/1 strength counts and the forbidden list
  as the red-team guardrail carried forward.
- Caveats: I read only the frenchman, red-team (both rounds), stem-hunter,
  and round3b results plus STATE.md — ~140 windows max through the frenchman's
  eyes, not the full 1,846 pairs; polyvalence's extent is genuinely unknown
  (R5's scope says so explicitly); 06's stem identity and the conditioning
  variable for R10 are still open; nothing here changes any lane status — the
  frenchman's ear findings remain non-promotional per red-team authority.
  No GitHub push (per task).
