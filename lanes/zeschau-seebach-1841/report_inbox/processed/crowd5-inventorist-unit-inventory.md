## inventorist: unit inventory

- Context: Round-5 work order — learn the cipher's syllable inventory bottom-up
  from the cribs instead of importing French syllabification. The word-pattern
  fleet proved the lexicon's unit alphabet cannot express the cipher's units
  (the 4-GT-anchor "première" tail returns zero candidates at every tier), so
  the inventory had to be rebuilt from ground truth: the 7 pencil cribs, the
  ear-cutting exemplars, the polyvalence islets (F33), and cutting rules R1–R4.
- Decision: Deliver the cipher's own unit inventory as 24 units in 4 tiers —
  7 crib-PROVEN (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que), 10
  lane-inferred (87=ce, 64=qui, 96=par, 94=ne, 06=verb-stem-class, 67=veut,
  62=on, 78=me, 77=le, 47=ce — status-marked), 3 conditioned-polyvalence
  islets (06, 52, 94), and 4 cutting rules (R1–R4) — plus 10 things the
  inventory rules out. Files: `code/crowd5/unit_inventory.{py,md,json}`;
  the .py re-derives every cipher-side number from the canonical repaired
  parse and asserts every evidence claim before emitting the JSON.
- Why: The crib "la première" = pre|m|i|er|e (5 groups) vs the lexicon's
  pre|mi|è|re (4) is the whole argument in one word: bare consonant `m` as a
  unit is phonotactically impossible in French but GT-proven (lexicon: "m" as
  a syllable in exactly 1 of 11,870 era words). From there the rules follow:
  1-letter cells mandatory (R1), by-ear inconsistent cuts ("personne" ×2
  spellings, R2), mute -e written (R3, kills N17-style phonetic models),
  mixed table of letters/syllables/endings/whole words (R4). The 29/82/34
  rate overages (182×/61×/3.3× vs era, N22) void era-syllable-conditioned
  legs (F30); polyvalence is conditioned-or-nothing (F33: 3/25 groups, zero
  free cases).
- Enlightenment: The inventory's backbone is grammatical, not phonological —
  the proven units are la, que, pre, m, i, er, e; the provisional backbone is
  ce, qui, par, ne, on, me, le. And the by-ear model made a genuine
  prediction that verified: "qu'on"=/kɔ̃/ as one spoken syllable → 46→62 =
  0× (re-verified this round on the repaired parse). When the instrument
  predicts a zero and the zero is there, the model is doing real work.
- For the report: new section "Unit inventory (INVENTORIST, round 5)" —
  the numbers that matter: 7 GT units + 10 valued + 3 conditioned islets =
  24 units; 12.0% conditioned polyvalence; 35.2% token coverage; 'm' as
  syllable 1/11,870 (lexicon) vs GT here; 29=er 2.44% vs era 0.038%.
- Caveats: every lane-inferred unit inherits the red team's status marks —
  87=ce stays provisional (cela-leg register-dependent, N27), 64="qui"
  re-promotion BLOCKED, 96="par" inherits 87's status, 94="en" co-value
  promotion DENIED (independence fail, N31). Era-comparison rates are
  lane-banked (N15/N22/N20), not recomputed here. Unidentified head
  00/24/98/48/74 are the inventory's empty slots. The frenchman's prose
  @-citations were loose (e.g. "on ne prend pas" @1329 on the canonical
  parse, not @1331) — positions in the inventory are re-derived from the
  repaired parse.
