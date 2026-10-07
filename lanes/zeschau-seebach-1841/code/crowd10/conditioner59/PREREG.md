# PREREG — 59 conditioned-polyvalence battery ("59COND")

Executor: 59-conditioner (round 10, work order 2).
**Pre-registered 2026-10-07 20:37 UTC (2026-10-07 15:37 CDT) — BEFORE any new
data query on the repaired 1,847-pair stream.**
Reading standing published results (NOTES F52/F64–F69, islet registry) for
battery design; no new stream query, census, or era count run before this file.

## Standing input (not re-litigated)
- 59="est" provisional (F52): 4 legs (S1 1.10× Nesselrode v8; S2 "qui est"
  3/47; S3 "n'est" 3/37; rivals re-killed 9–51× diplomatic). S5 quarantined,
  S4 residual honestly widened.
- F65/ISLET 8: 59="est"-as-word era-absent at @1447/@1803 (fenced n=2);
  viable parse = 84-59 bisyllabic-verb unit ("-este" verb), hypothesis-internal;
  era -este candidates déteste 17 / conteste 19 / atteste 36 / proteste 20 /
  manifeste 132 / reste 1251 (falsifier "candidates era-rare" did NOT fire).
- Registry form required if islet 10: rule (exact), n/n_eff, falsifier, leftovers.

## H0 (null)
59="est"-word unconditioned. The two fenced windows stay fenced adverses;
no islet.

## H1 (conditioned-polyvalence candidate), pre-registered exact forms
- **R_est:** 59="est"-word iff pre(59) ∈ {64, 94} — the two licensed word-frames
  are «qui est» (64-59) and «n'est» (94-59) from F52's S2/S3. n_eff counts
  distinct flanks (byte-identical ±3 7-mers merge to n_eff=1).
- **R_syl:** 59 = verb-final syllable "-este" iff pre(59) == 84 AND 59 sits in
  an «X le [V-bi]» verb frame — i.e. 84-59 is one bisyllabic verb unit with an
  era-real -este 3sg form whose stem is 84-compatible; specifically the two
  known frames «[37] qui le [84-59] [36]» (@1447) and «[ce] qui le [84-59]
  [35]» (@1803) must admit a real -este verb.

## Legs (≥2 independent checks required for any promotion/registry entry)
- **Leg A (R_est, era-rate):** P(59|pre=64) and P(59|pre=94) vs era
  P(est|qui), P(est|ne) on Nesselrode v8 (French-only). Pass bar: F33-style,
  in-band ≤2×, rivals dead.
- **Leg B (R_est, frame):** every 64-59 and 94-59 window parses
  grammatically as word-"est" (±2 successor inspection: predicative
  noun/adj/adv/participle expected).
- **Leg C (R_syl, verb ID):** from the Nesselrode v8 -este candidate set,
  report which -este verbs are era-real in the «qui le V» frame and rank by
  era rate. Unique ID OR viable-set-with-barrier, decided by data.
- **Leg D (R_syl, residual 84-59s):** census finds pre=84 59-windows; any
  beyond @1447/@1803 must admit the bisyllabic-verb parse (frame
  «le [84-59]» or verb-licensed) — else adverse.
- **Leg E (full census classification):** ALL n59 windows classified into
  {R_est, R_syl, adverse, unclassified-leftover}. Honest leftovers listed.

## Banked falsifier (F33-form, fires → rule dies)
- F1: a 59 window with pre ∉ {64,94} that REQUIRES word-"est" (era-grammatical
  «… est …» and no verb parse).
- F2: a pre=84 59-window admitting NO era-real -este verb in frame.
- F3: a pre ∈ {64,94} 59-window where word-"est" is era-absent/ungrammatical.
- F4: a pre=64/94-style "est"-frame realized on a DIFFERENT predecessor
  (rule over-narrow).

## Refutation bar (pre-registered — conditioned-polyvalence REFUTED)
≥2 of F1–F4 fire, OR R_syl's two known windows both admit a clean word-"est"
frame after all (F3-type), OR the 84-59 census yields a window that parses
as word-"est" under the frame from F65's own refinement. Then: no islet 10;
59 stays provisional-"est" with fenced adverses; return KILL rationale.

## Anti-gaming rules
- No manual-tiling bearing counts (F59) — per-window era nulls only.
- No re-litigation of standing kills (48="ne", H_verb, 86=que-family,
  unconditioned 84s, three mergers, refuge concretizations, retired WO-6 bar).
- Red team adjudicates any status change; nothing self-promoted.
- Census runs on the repaired 1,847-pair stream via
  `code/crowd6/redteam/verify_baseline.load_stream`; positions 0-based per
  REINDEX.md.
