## morphologist: 94="re" vs 94="ne" symmetric battery (WO3, round 4)

- Context: WO3 ordered a full ≥2-independent-check battery for 94="re" — the live
  rival to provisional-strong 94="ne" — symmetric with the "ne" case, F30-legal
  (word-space or syllabary-recovered legs only; the old rigid-syllable legs for
  "ne" — 1.025× rate, 1.054× trigram — are VOID under F30 and were rebuilt, not
  grandfathered). "re"'s only leg ("-rement" 1.28×) used the same dead instrument.
  Third value in play: 94="en" islets (F25 conditioned polyvalence). Evidence:
  `code/crowd4/morph94_re_battery.py` + `morph94_re_battery.json` (all numbers
  re-derived from `data/upstream-ct_R5005.txt`+`offsets.json` and Tocqueville t1+t2).
  Index note: my pair-offsets run 1 below the frenchman's (@1292 vs @1293 etc.);
  windows match byte-identical — same instances.

- Decision: **94="re" DEMOTED live-rival → disfavored.** **94="ne" holds
  provisional-strong, on REBUILT legs** (old A/B void, replaced 3-for-2).
  **Polyvalence: "ne"/"en" COEXIST as conditioned islets; "re" does not join**
  (no conditioning context, zero composing instances).

- Why: three symmetric F30-legal legs, both candidates face all three.
  (a) *Syllabary recovery* — `data/upstream-syll*.py` are annealers over a
  letter+syllable inventory; all three failed to find French (upstream-NOTES:
  "degenerates to ment/vous/ait"), which is itself the finding: frequency-driven
  rigid syllable statistics patent on this cipher. The RECOVERED cutting behavior
  comes from round-3 evidence, not the annealer outputs: single letters are legal
  units (82=m, 34=i standalone in pre|m|i|er|e), mute -e is WRITTEN (40=e),
  silent letters are DROPPED ("prend"→"pre" @1328), and cuts fall at arbitrary
  phonotactic boundaries ("personne" → per|so|nne AND pers|on|ne, same cipher).
  Consequence: any word containing "nement"/"rement" is a legal host for a
  ...94-82-06 ear-cut — so the F30-legal remake of the rate leg is a WORD-SPACE
  substring-host count, no syllabification. Era: 641 "nement"-hosts vs 282
  "rement"-hosts (disjoint sets, 0 overlap), **host odds 2.27:1 for "ne"**;
  'gouvernement' alone is 475/641 (74%) — the genre prior for a political
  despatch repeating one word twice (77-78-94-82-06 ×2 @1179/@1350).
  (b) *Compositional frames* (word grammar on anchors): "ne" composes in 8
  instances / 3 frame-types — 62-94-70-52 @1328 "on|ne|pre|pas" ("on ne prend
  pas", prend→pre attested), 35-94-52-80-04 ×2 byte-identical @1292/@1805
  ("ne pas [inf]", era "ne pas" attested 20× vs "re pas"/"en pas" 0×),
  94-82-06 ×3 ("…nement"); **"en" composes in 4/2** — 82-94-76 ×2 @650/@1574
  + 82-94-74 @1100 ("m'en", era "en ce" 20×; "m|ne"/"m|re" ungrammatical ×3),
  94-87 @1168 "61|en|ce|83"; **"re" composes in 0/0** — not one of its 36
  occurrences parses as French under "re" outside the contested trigram.
  (c) *Era word-bigram rate* on the 62-94 ×8 block: cipher P(94|62)=8/34=0.2353
  vs era P(ne|on)=191/1616=0.1182 → **1.99× (factor-2 band edge)**; vs era
  P(en|on)=0.0155 → 15× (kills "on en"); "on re" N/A as a word bigram.
  @1741 adjudication (94-82-46, "34|94|82|46|56|40|06"): unparsed under all
  three — "ne" weakly precedented (dropped silent letter, cf. "prend"→"pre":
  "i ne m[e] … que"), "re" has no parse at all ("i re m que"), "en" none
  ("i en m que"). It stays a true anomaly (25% of the 94→82 family) and does
  not discriminate in "re"'s favor.

- Enlightenment: the "ne"/"en" split is CONDITIONED, and the conditioning is
  visible in the neighbor table: 94="en" iff pre=82 ("m'en" ×3) or suc=87
  ("en ce" ×1) — 4/4 of the "en"-compatible frames; everywhere else the frames
  are "ne"-compatible (62-94 ×8, 94-52 ×3, 94-70, 94-82 ×4). The two values are
  anagrams (/nə/~/ɑ̃/ after m: "m'en"=/mɑ̃/ — the same nasal the 06-polyvalence
  trades in, F25), which is exactly the shape conditioned polyvalence should
  have: a phonetic bridge plus a disjoint context. "re" (/ʁə/) has neither a
  bridge nor a context — coexistence would be unconditioned homophony, a
  strictly weaker claim than the conditioned ne/en system, with zero instances
  to pay for it. Also: the old battery's "rival_re_ratio=1.067" and the 1.28×
  were artifacts of the rigid syllabifier — under ear-cut legality the same
  data says 2.27:1 the other way. The instrument was the rival.

- For the report: belongs in the 94 anchor section + F24 revision + the F25
  polyvalence section. Numbers that matter: **host odds 2.27:1 (641 vs 282,
  disjoint)**; **compositional frames ne 8/3, en 4/2, re 0/0**; **P(94|62)
  1.99× era P(ne|on), 15× P(en|on)**; 35-94-52-80-04 ×2 and 82-94-76 ×2
  byte-identical repeats; @1741 still unparsed (all three). Status changes:
  94="re" → disfavored; 94="ne" provisional-strong on rebuilt legs (old A/B
  marked VOID-per-F30); 94="en" islets → conditioned-polyvalent co-value
  (promotion-grade evidence: 4 composing instances, 2 byte-identical repeats,
  disjoint conditioning).

- Caveats: 52="pas" is lane-inconclusive — the "ne pas" leg leans on it, but
  the leg is comparative ("ne pas" era-attested 20× vs rivals 0×), so it
  survives as a discriminator regardless. My Tocqueville tokenization gives
  221,059 words vs attempt3's 214,861 — ratios are tokenizer-robust, counts
  differ. The factor-2 band is UNCALIBRATED per red team (F26) — the 1.99× is
  band-edge, structural/compositional legs carry the verdict. @578's trigram
  host is unidentified (could be a "rement" word — this is the thread a "re"
  revival would need). Wrinkle out of scope: 62-94-64 @509 "on|ne|qui" parses
  under none of the three (64="qui" tension or a fourth 94-value). No GitHub
  push. R5005 only.
