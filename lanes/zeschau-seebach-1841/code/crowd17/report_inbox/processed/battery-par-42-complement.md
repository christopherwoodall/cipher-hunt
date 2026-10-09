# Battery verdict: par-42-complement — can 42's noun value license a "par"-complement at @464?

Date: 2026-10-09. Worker: a2cd65e1-8e65-4160-a2b7-9d6132fce967.

Parent: `frame-464-fullparse` (verdict null, 2026-10-09), whose follow-up #1 proposed this target.

## Bar (verbatim from battery-queue.json)

`Bar: test whether 42's noun value can license a "par"-complement in 1841 diplomatic French, dissolving the seam leftward ("est [42] par …"). Bar: name one 42 value with a battery-grade-attested "par"-complement at this window, else fence the leftward route.`

## Bar restated as numbered clauses (pre-registered before testing)

- C1: name one concrete 42 noun value V such that "est V par" is battery-grade attested in 1841 diplomatic French AND the complement of "par" is what stands at this window — "pour [33]" (0-based @466–467). PASS iff such V is named.
- C2 (else-arm): fence the leftward route ("est [42] par …" dissolving the seam leftward) with stated cause.

## Method

- Re-derived the full 1,847-pair / 96-type stream from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (parse per `code/side-keyhunt/repair_parse.py`; asserts re-run: 1,847 pairs, 96 types). `canonical.py` never touched.
- Window byte-exact, row a2_10: 0-based @463=59, @464=42, @465=96, @466=00, @467=33 (1-based @464–467 "59 42 96 00" per the parent report).
- Corpus census over the lane's 1841 diplomatic corpus (`code/side-period/corpus/`, 77 files, 34,551,380 chars). Per R19-193 (corpus zeros require whitespace-normalized search): NFKD accent-strip + lowercase, hyphenated line-breaks joined, letter-boundary matches; a whitespace-insensitive pass added for "par pour".
- R5005, sealed gates, red-team adjudication queue untouched.

## Findings

- **The locus is unique.** n(42)=20 (0-based @79/@205/@219/@266/@282/@428/@464/@488/@493/@543/@784/@1072/@1144/@1187/@1410/@1503/@1617/@1794/@1814/@1838). Exactly one 42 is followed by 96: @464. The "est [42] par" configuration exists at no other window.
- **The complement of "par" at this window is "pour [33]".** 96=par granted, 00=pour (A9 class-level), 33 verb-stem (A10). For the leftward route to parse, "par pour [33-inf]" must be a licensed [par + complement] in 1841 diplomatic French.
- **Corpus zero, both passes.** "par pour" with letter boundaries: **0 in 34,551,380 chars**. Whitespace-insensitive "par pour" (catching line-break splits): **0**. "est X par pour": **0**. The word "pour" never follows "par" anywhere in the register.
- **Fairness — the head is licensable, the complement is not.** "est [N] par [X]" heads are attested 97× in the corpus (dominantly passive participles + par-agent: "faite", "désarmé", "prononcé"…; also noun heads). Means-complement "par écrit": 12× ("ordre par écrit", "déclaration par écrit" — the native noun+par shape). Agent-par: 1,932×. So a noun licensing a par-complement is in principle possible; what is unattested is a par-complement *beginning with "pour"*.
- **The passive route is closed by standing class, not re-litigated.** The native "est [X] par [agent]" shape is participle-driven; 42 is noun-class (promoted 2026-10-08) and §7 sole-polyvalence (67) bars a noun/participle split. Adopted from sibling `seg-par-pour-96-00` (NULL, fence executed), whose five rescues at all three "96 00" windows (ellipsis of par's complement; passive agent attaching left; "le pour" noun; clause boundary between 96 and 00; re-segmentation) were all rejected at battery grade; the sibling's fence is adopted, not re-litigated.
- **No 42 value can be named.** Any candidate V (moyen, ordre, voie, déclaration…) still faces "par pour", which the register never produces. Naming V would require inventing the complement (§3 bars inventing values/grammar).

## C1: FAIL — C2: EXECUTED

No 42 noun value licenses a "par"-complement at this window: the complement slot is occupied by "pour [33]", and "par pour" is a 34.55M-char corpus zero in 1841 diplomatic French. The leftward dissolution route ("est [42] par …" absorbing the seam) is **fenced** with stated cause: complement-side failure, not head-side.

## Fence scope

- Fences only the leftward dissolution of the @464 seam. The window itself stays in the parent's standing venue: **96/00-driven residual** (inherited fence, not a new independent problem).
- Untouched: 42's noun class; the parent's adopted leftward frame "tout cela est [42]" (`val-42-estframes`); the "96 00" collocation's standing venues (`par-pour-redteam` P2, `redteam-contre-00` P1); 96=par, 00=pour, 59=est, 33's verb-stem frame.
- No standing/red-team verdict contradicted or downgraded. §7 intact; no polyvalence declared. Canonical-stream caveat stands (row a2_10 offset unvalidated). Adverses: none listed.

## Verdict: NULL (fence executed per the bar's else-arm)

## Follow-up targets (null regenerates work; all verified ABSENT from battery-queue.json)

1. `noun-42-value` (P3) — name 42's actual value from its 20 windows (independent of the fenced par route); @464's right edge is unconstrained by this window. Bar: name one value fitting ≥3 of the 20 windows with battery-grade evidence, else fence the value route.
2. `96-complement-census` (P3) — census all 96 windows for complement type (agent-par, means-par, distributive, complement-less); test whether the three "96 00" windows are the only complement-less pars, feeding the red-team 96/00 venues. Bar: complete complement-typed census of all 96 windows with byte evidence.

(The parent's other two follow-ups, `toutesfois-452` and `locus-464-rerun-gated`, are already queued — not re-proposed.)

## Bookkeeping

- Report: this file.
- battery-queue.json: `par-42-complement` → status `verdict`, result `null`, date 2026-10-09 (temp-file + rename; pre-write assert confirmed queued/verdictless; JSON re-validated from disk after write; own entry only; no downgrade).
- Lock `locks/par-42-complement.lock`: created on start (agent id + UTC timestamp), deleted on completion.
