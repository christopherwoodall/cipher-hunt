# PRE-REGISTRATION — HOMOPHONE-SET BATTERY (sets A/B), round 13 (council work order 2)

**Executor:** homophone-battery (sets A/B)
**Timestamp:** 2026-10-07 (written BEFORE the formal battery runs; only standing/recorded
numbers consulted: F33/F40/F56/F60/F79 case law, table-reconstruction.md §b–§d, the French
blitz syntax48-battery, crowd12 PREREGs. Exploratory frame reads done for orientation only —
no test statistic has been computed.)
**Work dir:** `code/crowd13/homophone-ab/` · **Report note:** `report_inbox/homophone-ab-<set>.md`
**Stream:** repaired 1,847-pair (`code/side-keyhunt/repaired_offsets.json`), via
`code/council/drag/common.py::load_stream`. **Corpus:** clean diplomatic pool
(`code/side-period/corpus/*.txt` minus allgemeine-zeitung-*, harvest-log, adb-zeschau;
F77: v8 "ment" tokens VOID).

## Standing context (not re-litigated)

- Board: 7 pencil GT (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que) + 5 provisional
  (87=ce, 64=qui, 96=par, 59=est, 77="le"-conditioned) + leads (00="pour" strong, 16="i",
  47="ce").
- F60 (kill-grade): 48="ne"-allophone REFUTED. 48 never enters the status line as "ne".
- F40 (F33-grade rule): 06/86 complementary distribution — 00→86 ×12 vs 00→06 ×0;
  06 in finite/imperative frames; 86 never there (0/14). Allomorph interpretation is
  WORKING HYPOTHESIS only.
- F79 (GRANT): 33 = infinitive-CLASS (pre==00 ×8, suc==29 ×5, pre==67 ×1 as stated).
- F22: groups are sub-word chunks; 29 = "-er" ending chunk. Fork S (33/86 = stem,
  suc = completion) vs Fork W (33/86 = whole monosyllabic infinitive, suc = next word)
  SURFACED unresolved in crowd12/identifier33 PREREG.
- F56 case law (via F60): interchangeability is NECESSARY, not sufficient, for homophony.
  Table-reconstruction §c.4: homophone candidates must show UNIFORM predecessor
  distributions (1690 cycling); segregated-by-predecessor kills free homophony.
  47/87 precedent: same value "ce", segregated predecessors (87←24×10) → positional
  allophones, SPLIT not PROMOTE.
- French blitz (syntax48-battery): 48="de" unconditioned KILLED kill-grade (11 windows);
  48="de" iff "de ce que" (suc=47→46) LEAD-weak n=1 @863; vowel-initial syllable tier
  (à/a/es/et/il/un) LEAD-weak conditional on "m-48" within-word premise; H_stem
  (verb stem) UNTESTED; null (UNIDENTIFIED) holds.
- Drag (`code/council/drag/`): NOT LANDED — no `drag_hits.json` exists as of this writing.
  Nothing to fold in. If it lands mid-battery, hits will be folded and the fold disclosed.

## Bar — SET A {33, 86} (contact sim 0.70↔0.70, phases B/B, n=25/32)

Neither member has a value; the battery is MUTUAL (86 in 33's frames and vice versa).
PROMOTE = "homophones of one stem syllable, 1690-cycled". Requires ALL of:

1. **Uniformity (re-derive):** χ² vs uniform on (25, 32); bar p > 0.05 (fail to reject).
   (Table claims χ²=0.86, p=0.35.)
2. **Cycling (runs test):** Wald–Wolfowitz on the despatch-order 33/86 membership
   sequence (n1=25, n2=32; E[runs]=29.07). Bar |z| < 2 (interleaved; clumping kills).
3. **No predecessor segregation (§c.4 test):** χ² on P(pre|33) vs P(pre|86)
   (pooled rare predecessors, Yates where needed). Bar p > 0.05. Significant divergence
   (p < 0.01) kills free homophony.
4. **≥2 frame-interchangeability legs** (positive, independent):
   - L1: 86 attested in 33's signature frames — "pour"-governed (pre==00) AND/OR
     29-completion (stem+"er") — at rates parallel to 33's (Fisher-parallel, not merely >0).
   - L2: 33 attested in 86's signature non-pour frames (77-governed "le"-frames ×5,
     56/24-successor frames) with 86-parallel role.
   - L3 (era): the shared frames are era-licensed on the clean pool at non-degenerate
     rates (e.g. "pour"+[stem]+"er" shape; "le"+[verb-stem] needs explicit era license —
     unlicensed = leg fails).
   Legs are per-frame-window, never manual-tiling counts (F59).

**SPLIT** (positional allophones / same class, different values — the 47/87 and 06/86
precedents): contact similarity retained AND (predecessor or successor distributions
significantly divergent, p < 0.01, OR frames disjoint/complementary with zero
interchangeability). Implication for 33's value: 33 stays infinitive-class pursuing its
own ID (identifier33 battery); 86 stays verb-stem-class; the two are NOT the same cell.

**KILL:** uniformity fails (p ≤ 0.05) OR runs show clumping (|z| ≥ 2, clumped direction)
OR zero frame interchangeability with similarity attributable to shared class alone.
Implication: the §b proposal was class-level resemblance; pursue 33 and 86 independently.

≥2 independent legs required for any PROMOTE (lane standing rule); adjudicator rules.

## Bar — SET B {48, 94} (contact sim 0.64↔0.64, phases B/B, n=38/37)

**PROMOTE is PRE-BARRED:** PROMOTE would mean 48="ne" (94's value), which F60 killed
kill-grade. No PROMOTE path exists without overturning F60 — out of scope. Live verdicts:
SPLIT vs KILL, plus an identity-constraint deliverable for 48 either way.

1. **Uniformity (re-derive):** χ² vs uniform on (38, 37); record p (table claims
   "near-perfect").
2. **Cycling (runs test):** Wald–Wolfowitz on despatch-order 48/94 membership
   (n1=38, n2=37; E[runs]=38.49). Record z.
3. **Predecessor divergence (§c.4):** χ² on P(pre|48) vs P(pre|94). Significant
   divergence (p < 0.01) → not cycling homophones (consistent with F60).
4. **Frame-substitution battery** (the work order's core test): for each 94="ne" window,
   substitute 48 and test candidate values against the clean pool:
   - V1: 48="de" (unconditioned — EXPECTED KILLED per blitz; confirm on 94's frames).
   - V2: 48="de" iff "de ce que" (suc=47→46) — the surviving LEAD-weak islet.
   - V3: vowel-initial syllable tier (à/a/es/et/il/un).
   - V4: verb stem (H_stem).
   And reverse: 94="ne" in 48's 38 windows (F60 already says no; spot-confirm, don't
   re-litigate).
   Deliverable: per-frame parse table; the value (if any) that parses 48 in 94's frames.

**SPLIT:** contact similarity reflects a REAL shared frame class (both pre-verbal
monosyllables in overlapping frames) but different values — i.e. 48 is ne-DISTRIBUTED
with its own value, and the battery names or constrains that value (≥1 frame-parsing leg
at era rates). Predecessor divergence expected and consistent.

**KILL:** the similarity is spurious — 48's and 94's frames are disjoint (no shared
(pre,suc) frame shapes), no candidate value parses 48 in 94's frames, and the contact
similarity is attributable to a few shared contexts. Implication for 48's identity:
back to the blitz shortlist (vowel-initial tier / de-ce-que islet / H_stem / null);
the {48,94} proposal is retired.

## What each verdict implies (pre-registered)

- {33,86} PROMOTE → 33's value = 86's value = ONE stem syllable; the 8 "pour 33" + 12
  "pour 86" frames are one infinitive's 20 tokens; identifier33's infinitive hunt gains
  12 more windows; suc==29 completions (5+4) are one paradigm.
- {33,86} SPLIT → 33 and 86 are different stems; 33's value hunt continues on its 8
  pour-frames alone; 86's verb-stem-class stands via F40; no shared ID.
- {33,86} KILL → the 0.70 similarity was class-level (both verb stems); independent pursuit.
- {48,94} SPLIT → 48 constrained to a ne-frame-class value V≠ne; the battery's per-frame
  table is the new lead list for 48's ID.
- {48,94} KILL → the 0.64 similarity was spurious; 48's ID hunt ignores 94.

## Falsifiers banked (would overturn my verdict — for the adjudicator)

- A 96-00-style compositional re-read dissolving any frame I use (cf. table-reconstruction §c).
- The drag landing with {33,86}/{48,94} hits contradicting my frame tables.
- A second "48-47-46" window (promotes the de-ce-que islet independently of my battery).
