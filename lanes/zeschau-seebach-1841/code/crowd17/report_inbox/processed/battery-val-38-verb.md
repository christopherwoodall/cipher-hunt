# Battery report: val-38-verb

- Target id: `val-38-verb` (P3)
- Claim: "Name 38's verb value: the value must license finite-3sg @1113 ("[65] [V] pas cela") AND past-participle @826 ("c'est [pp]") — a syncretic verb (cf. "dit": "il dit" / "c'est dit") or a stated form alternation. If no French verb covers both frames, re-open the fenced split."
- Date: 2026-10-09
- Worker: battery worker (subagent 7b9ea086-20ea-41ea-99a9-d1407e30cfaf)
- Stream: repaired 1,847-pair / 96-type parse, re-derived in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (asserts held: 1847 pairs, 96 types). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.

## Bar (verbatim, pre-registered before testing)

"The value must license finite-3sg @1113 ("[65] [V] pas cela") AND past-participle @826 ("c'est [pp]"); if no French verb covers both frames, re-open the fenced split."

Numbered pass/fail clauses (restated before testing, not modified after):

- **C1:** A named French verb value licenses finite-3sg at @1113: "[65-N] [V-3sg] pas cela" (65 noun-class, 30='pas' verbal negator, "cela"=69-11 direct object).
- **C2:** The same named value licenses past participle at @826: "ce(87) est(59) [pp]" (conditional on provisional 59='est').
- **C3:** If NO French verb covers both frames, re-open the fenced split (predicative vs verb-form, resolved uniform by noun26-38-profile). If at least one covers both, the split stays closed.
- **C4:** Naming is unique at battery grade (the claim says "Name 38's verb value", singular). Adverses: none listed.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/val-38-verb.lock` on start (deleted on completion).
2. Adopted (never re-litigated) standing premises from noun26-38-profile (PROMOTE, 2026-10-09): 38 = verb-form (uniform class); @826 = past participle ("c'est [pp]"-shaped, conditional on provisional 59='est'); @1113 = finite 3sg ("[65] [V] pas cela", kill-grade forced); @1469 = modal slot ("[62] [38-modal] [26-inf]"); @1650 = finite governor ("[03] [38] me [16-inf]", "veut me voir"-shaped, conditional); W1 indeterminate; W4/W7 fenced with stated cause. Standing values: 30='pas' (battery-promoted), 87='ce', 65 noun-class (R18-001 ratified), 69-11='cela' (locus-level).
3. Enumerated the French syncretic-verb inventory (3sg present = past participle) and the stated-alternation candidates; tested each against C1 and C2, then used @1469 (modal) and @1650 (governor) as tiebreakers. All @-offsets 0-based repaired-stream.

## Window-level evidence (byte-exact)

- **@826 (a5_06):** `24 87 59 38 82 01 24` = "[24] ce est [38-pp] m [01] [24]". C2 frame: "c'est [pp]".
- **@1113 (a6_07):** `73 41 65 38 30 69 11 88` = "[73] qui [65-N] [38-V-3sg] pas cela [88-V]". C1 frame: "[65] [V] pas cela".
- **@1469 (a7_09):** `21 02 62 38 26 12 41` = "[62] [38-modal] [26-inf]" ('ne peut [inf]'-shaped). Tiebreaker: 38 must govern a bare infinitive.
- **@1650 (a8_04):** `31 10 03 38 82 16 01` = "[03] [38-V-fin] me [16-inf]" ("veut me voir"-shaped). Tiebreaker: 38 must take "me + infinitive".
- @384, @1343, @1828: no contradiction with any surviving candidate (W1 indeterminate; W4/W7 fenced for both classes per parent).

## Candidate analysis

**Syncretic verbs (3sg = pp) — the bar's preferred shape:**

| Candidate | @1113 "[V] pas cela" | @826 "c'est [pp]" | @1469 modal+inf | @1650 "V me inf" |
|---|---|---|---|---|
| dit (dire) | "ne dit pas cela" ✓✓ | "c'est dit" ✓✓ | "dit [inf]" ✗ (dire takes que-clauses) | ✗ |
| fait (faire) | "ne fait pas cela" ✓✓ | "c'est fait" ✓✓ | "fait [inf]" ✓ (causative) | "fait me [inf]" ✗ (clitic must precede: "me fait [inf]") |
| écrit (écrire) | "n'écrit pas cela" ✓ | "c'est écrit" ✓ | ✗ | ✗ |
| interdit (interdire) | "n'interdit pas cela" ✓ | "c'est interdit" ✓✓ | ✗ (needs "de") | ✗ |
| prescrit/décrit/inscrit/… | ✓ | ✓ | ✗ | ✗ |

**Result: no syncretic verb covers the modal/governor windows.** The value, if nameable, must be a stated form alternation.

**Stated-alternation candidates:**

| Candidate (3sg / pp) | @1113 | @826 | @1469 | @1650 | Sense uniformity |
|---|---|---|---|---|---|
| vouloir (veut/voulu) | "ne veut pas cela" ✓✓ | "c'est voulu" ✓✓ | "veut [inf]" ✓✓ | "veut me [inf]" ✓✓ (parent's own gloss) | volition in all 4 windows ✓ |
| devoir (doit/dû) | "ne doit pas cela" ✓ ("owe" sense) | "c'est dû" ✓✓ | "doit [inf]" ✓✓ | "doit me [inf]" ✓ ("must see me") | owe @1113/@826 vs must @1469/@1650 — sense-switch required |
| savoir (sait/su) | "ne sait pas cela" ✓✓ | "c'est su" ✓✓ | "sait [inf]" ✓ (weaker) | "sait me [inf]" ✗ (bizarre) | — (killed at @1650) |
| pouvoir (peut/pu) | "ne peut pas cela" ✗ ("pouvoir cela" marginal) | — | — | — | — (killed at C1) |

**Result: a 2-way tie between "vouloir" (veut/voulu) and "devoir" (doit/dû).** Both license both bar frames and both tiebreaker windows. "Vouloir" has a parsimony edge (uniform volition sense across all four windows; the parent's @1650 gloss was literally "'veut me voir'-shaped"), but "devoir"'s owe/must polysemy is standard French, not a kill-grade defect. The tie cannot be broken at battery grade on the available windows.

## Per-clause pass/fail

- **C1 — PASS (existential).** "Vouloir" and "devoir" both license finite-3sg at @1113.
- **C2 — PASS (existential).** "Vouloir" ("c'est voulu") and "devoir" ("c'est dû") both license the pp at @826.
- **C3 — does not fire.** French verbs DO cover both frames, so the fenced split is NOT re-opened. The parent's uniform verb-form promote stands; the predicative-vs-verb-form split stays closed.
- **C4 — FAIL.** The value cannot be uniquely named: "vouloir" vs "devoir" is a genuine 2-way tie at battery grade. Naming "vouloir" alone would overstate (the sense-uniformity lean is parsimony, not kill-grade, against "devoir").

## Verdict: NULL (underdetermined value — 2-way tie, not a split re-open)

38's verb value is narrowed to **{"vouloir" (veut/voulu), "devoir" (doit/dû)}** — a stated form alternation in either case, since no syncretic verb covers the modal/governor windows. "Vouloir" is the parsimony lead (uniform volition sense; parent's "'veut me voir'" gloss at @1650). This NULL does not disturb any standing verdict: noun26-38-profile's uniform verb-form PROMOTE stands, no red-team verdict on 38 exists (verified: the only queue id matching '38' is `resid-1097-1389-escalate`, which concerns @1097/@1389 residuals, not group 38), §7 intact (one lexeme with inflected forms is inflectional, not polyvalence, per the parent's framing).

## Caveats (stated, not hidden)

1. If "vouloir" is eventually named, groups 38 and 67 share the surface "veut" — a homophony claim the red team must adjudicate per §7 (1690-uniformity necessary but insufficient; 67="veut" is positional-rule battery grade).
2. @826 conditional on provisional 59='est'; @1113 conditional on battery-promoted 30='pas'; @1469 conditional on 62='il' (demonstrated, not promoted) and 26 infinitive-shaped; @1650 conditional on 03-nominal and 16-infinitive (both battery grade, pending ratification).
3. Canonicality caveat stands (68 of 70 upstream row offsets unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `val-38-vouloir-devoir` (P3) — discriminate "vouloir" vs "devoir" at battery grade. Bar: name iff a 38 window (or 65's value once named, fixing @1113's "cela" as wanted vs owed) forces volition-only or obligation/owe-only; "vouloir" takes "que"+subjunctive, "devoir"-modal takes bare infinitive — a "38 46"-family window would discriminate.
2. `w1-38-384-reread` (P4) — re-read W1 @384 ("82 16 52 38 37 43 91 36") once 52's and 37's classes resolve; a governor/complement frame there discriminates volition vs obligation.
3. `homophone-38-67-veut` (P4) — gated: IF "vouloir" is named, test the 38/67 "veut" surface-sharing implication per §7's homophony standard (frequency + distributional, not 1690-uniformity alone).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-38-verb.md`
- Queue: `val-38-verb` → `verdict`/`null`, 2026-10-09 (pre-write assert: was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/val-38-verb.lock` created on start, deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
