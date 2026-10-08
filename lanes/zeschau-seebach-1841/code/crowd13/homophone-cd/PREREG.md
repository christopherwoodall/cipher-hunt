# PREREG — Round 13 WO2: HOMOPHONE-SET BATTERIES {52,59} & {76,78}

Executor: homophone-set-battery (council round 13, work order 2).
**Pre-registered 2026-10-07 ~18:05 CDT — BEFORE any new data query for this
work order.** Standing published results read for battery design only:
- ISLET 10 from `code/french-blitz/frame59-map.md` (audit 2026-10-07):
  EST-ARM = 59=word-«est» iff pre∈{64,94,93}, 6/6 windows clean
  (@103 «ne l'est», @316/@1210/@1777 «(ce) qui est», @559/@763 «n'est»);
  ESTE-ARM = 59=verb-final «-este» iff pre=84 (@1190/@1448/@1804 firm,
  @1291 fenced); unclassified/fenced windows catalogued there.
- 78={ver,er} fork from `code/french-blitz/gouvernement-reread.md`:
  er|ne productive (52 tokens/22 types) vs ver|ne zero genuine
  (10.4×, p=3.2e-11); fork leans 78=«er», NOT resolved.
- Set proposals from `code/council/table-reconstruction.md` §b:
  {52,59} n=27/27, phase C/C, mutual sim 0.56, uniformity ✓ (identical);
  {76,78} n=21/31, phase C/C, mutual sim 0.54, uniformity ~ (ratio 1.48).
  F60's lesson (contact similarity NECESSARY, not sufficient) governs.
- Standing non-re-litigated: killed unconditioned-59, killed unconditioned
  84s, 52=«pas»-polyvalent per K5/N29 (caveat for «ne…pas» windows), no
  nulls, 1690 cycling doctrine.
- `code/council/drag/drag_hits.json` — FILE DOES NOT EXIST (checked
  2026-10-07 18:05). Nothing to consult; recorded as a gap.

No new stream census, window extraction, or era count run before this file.
Corpus: clean-diplo pool verbatim (`code/crowd12/estetie/estetie.py`
FRENCH_CLEAN list + lane `tok_elision` tokenizer; ~3.87M tokens).
Nesselrode v8 VOID for phrase queries (OCR word-split caution); v8
unigrams descriptive-only.

## H0 / design

- **H0-{52,59}:** 52 and 59 are free homophones of one syllable
  («est»/«-este» family), cycling per the 1690 order.
- **H0-{76,78}:** 76 and 78 are free homophones sharing the fork value
  («ver» or «er»).
- Falsifier pattern (table-reconstruction §c): predecessor-segregation is
  evidence AGAINST free homophony → SPLIT (positional allophones, cf {47,87});
  failure to parse in the known member's frames → KILL.

## Leg A — Frame battery (per set)

### {52,59}: does 52 parse in 59's «est» frames?
- Census all 27 52-windows (pre, suc, ±3 glossed with banked values).
- Partition by ISLET-10 arms:
  (i) pre∈{64,94,93} → word-«est» LICENSED: test era frames:
      64-52 vs «qui est» (1033/3.87M, banked-clean);
      94-52 vs «n'est» (3674/3.87M, banked-clean; check «ne» has its verb);
      93-52 vs «ne l'est» (51/3.87M, banked-clean; successor must license
      copula).
  (ii) pre=84 → «-este» arm would fire if 52=59-homophone; test whether
       any 52-window has pre=84 and what it forces.
  (iii) pre∉{64,94,93,84} → word-«est» NOT licensed by ISLET 10; record
       each window's parse status (fenced sub-tier analogs? unclassified?
       incompatible?). A window where 52 MUST be «est» but pre∉{64,94,93}
       would force rule-widening discussion (F1 analog); a window where
       52 CAN'T be «est» where 59 CAN → divergence data.
- **Bar (frame leg PASS):** ≥1 window with pre∈{64,94,93} where word-«est»
  parses grammatically with an era-attested frame at lane rates; and NO
  window where 52 is FORCED «est» outside {64,94,93} (else SPLIT-condition
  or rule break). EXPECTATION: unknown — will report honestly.
- 52=«pas»-polyvalent caveat (K5/N29): «ne [52]» windows may be
  «ne…pas», not «n'est» — each 94-52 window adjudicated individually.

### {76,78}: does 76 parse in ver/er frames? Which tine?
- Census all 21 76-windows + all 31 78-windows (pre, suc, ±3 glossed).
- Test T-er: 76-94 bigrams — the frenchman er|ne productivity test.
  If 76=«er», 76-94 = «…er ne…» (productive, multi-type); if 76=«ver»,
  «verne…» should be zero genuine. Count 76-94 occurrences and assess
  frame productivity from code.
- Test T-ver: 76 windows in noun-internal frames (ver-syllable position
  inside longer words) vs 78's verb-final «-er»/infinitive frames.
- Fork-tie reading: which tine lets 76 parse at its own windows AND keeps
  78's era-fork evidence consistent.
- **Bar (frame leg PASS):** 76 parses in 78's frames on one tine at era
  rates, with the productive/zero diagnostic agreeing with 78's own
  er|ne-vs-ver|ne signature. EXPECTATION: unknown — will report honestly.

## Leg B — Uniformity (χ² vs uniform, ratio<2 per §b)

- {52,59}: (27,27) — χ² trivially 0 by construction; REPORT anyway from
  code (sanity on the repaired stream).
- {76,78}: (21,31) — χ² = ((21−26)²+(31−26)²)/26 = 1.92, p≈0.17;
  ratio 1.48<2. Re-derive from code.

## Leg C — Cycling (runs test) + predecessor segregation (χ² homogeneity)

- Runs test (Wald-Wolfowitz) on set-membership sequence in stream order:
  interleaving (z≈0) = 1690 cycling consistent; clumping (z<−2) =
  positional use → SPLIT-signal.
- P(pre|h₁) vs P(pre|h₂) χ² homogeneity over top-k predecessor categories
  (lump tail into OTHER): divergence (p<0.05) → predecessor-segregation →
  evidence AGAINST free homophony → SPLIT; no divergence → homophony
  survives → PROMOTE-support.
- Same for successor distributions (secondary).

## Decision bars (per set; red team adjudicates any status change)

- **PROMOTE (homophones confirmed):** Leg A PASS + Leg C no-divergence +
  Leg B ✓ — ≥2 independent legs (A and C are independent).
- **SPLIT (positional allophones / conditional cells):** Leg A PASS but
  Leg C diverges (segregated predecessors) — the {47,87} pattern.
- **KILL:** Leg A FAILS (unidentified member does not parse in the known
  member's frames at era rates) → not the same value; OR a forced
  incompatible reading at a firm window.
- **INCONCLUSIVE:** legs split without meeting any bar; report numbers,
  no verdict.

## Outputs

`code/crowd13/homophone-cd/`:
- PREREG.md (this file)
- `homophone_cd.py` (all counts from code, F59 respected)
- `homophone_cd_results.json` (window tables, frame verdicts, χ²/z numbers)
- report note at `report_inbox/homophone-battery-cd.md` per REPORTING.md
