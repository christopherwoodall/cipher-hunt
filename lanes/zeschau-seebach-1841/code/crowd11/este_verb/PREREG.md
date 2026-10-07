# PREREG — Round 11 WO1: ESTE-VERB IDENTIFIER ("este-verb-id")

Executor: este-verb-identifier (round 11, work order 1).
**Pre-registered 2026-10-07 ~16:05 CDT — BEFORE any new data query for this
work order.** Standing published results read for battery design (NOTES,
islet_registry.md ISLET 1/8/10, crowd10 RULINGS-ROUND10 R7/R8,
ISLET10-PROPOSAL.md, era_battery.json, era_battery_diplo.json); no new
stream census, window extraction, or era count run before this file.

## Standing input (not re-litigated)
- ISLET 10 (LEAD, R7 GRANT-WITH-MODIFICATION): 59=verb-final «-este» iff
  pre(59)=84 — firm @1190/@1448/@1804, fenced @1291. (pre=06/61/44/86 tiers
  are fenced sub-tiers, NOT rule members — untouched.)
- Leg C set-valued candidate inventory (diplomatic corpus 3.96M):
  {manifeste 131, atteste 35, proteste 20, conteste 19, déteste 23
  (=17+6 unaccented)}; reste EXCLUDED (intransitive — «qui le reste»
  impossible). Banked, not re-derived as a claim.
- Frenchman F-B (R8, banked): «qui le [V]» frame licensed (515/4.2M);
  specific -este value era-NEUTRAL (0/4.2M all) — verb ID cannot promote
  the este-arm without stem IDs. Register caveat banked: inventory is
  diplomatic-corpus-based, not v8-strict.
- ISLET 1: 84="en" iff pre∈{82}∪{66,89}; noun identity NULL (rescoped).
- Killed/rescoped, not re-litigated: unconditioned 59="est",
  unconditioned 84s, 86=que-family, three mergers, 48="ne".

## H0 (null)
The -este verb stays set-valued {manifeste, atteste, proteste, conteste,
déteste}; no candidate promoted, demoted, or killed. Unique ID unattainable
on current evidence.

## Required 84 readings under test (84-59 = bisyllabic verb, 59="-este" banked)
At @1448/@1804 (84 = FIRST syllable of 84-59):
- manifeste → 84="manif" | atteste → 84="att" | proteste → 84="prot"
  | conteste → 84="cont" | déteste → 84="dét"
At @1190 (06-84-59 trisyllabic; 84 = MIDDLE syllable, 06 = first): required
84 value per candidate depends on the by-ear 3-cell cut; enumerated per
candidate in the run (e.g. manifeste: 06="man"/84="if"; proteste:
06="pro"/84="t"; etc.). By-ear cut variance is EXPECTED (frenchman
enlightenment: inconsistent cutting) — cuts are hypotheses, not claims.
At @1291 (fenced): verb-parse «la [17] [84-59] [35]» needs 17/35; 84 =
first syllable under the verb parse only.

## Checks (per candidate; every count from code, F59 respected)
- **(a) 84-profile:** (a1) verify pre(84) at the @1448/@1804 84-positions
  (=77, banked) → ISLET-1 en-condition does NOT fire (77∉{82,66,89}) →
  required for all five: no "en" conflict expected. (a2) verify none of
  {manif,att,prot,cont,dét} is a standalone French noun/word (else it would
  touch the rescoped 84=noun islet). (a3) cross-window: 84@1189 (middle of
  06-84-59) vs 84@1447/@1803 (first syllable) — test monovalence
  compatibility per candidate under plausible by-ear cuts. PRE-REGISTERED:
  a mismatch is recorded as "84 polyvalent here OR different verb at
  @1190", NEVER a candidate kill (polyvalence is live lane-wide: 06/86,
  47/87, 52).
- **(b) v8 era rates (standing reference nesselrode-v8.txt, N=92,594):**
  n(V), «qui le V», «le V», «V que» per candidate. PRE-REGISTERED: v8 zeros
  are DESCRIPTIVE ONLY — no kill/promotion on v8 sparsity (N too small);
  the diplo 0/4.2M «qui le V» is already ruled era-neutral (F-B), not a
  kill. Diplo unigrams cited as banked context, not re-derived claims.
- **(c) frame coherence (French grammaticality, banked neighbor values):**
  - @1448: «[37] qui le V [36] [67]» — «qui le V» grammatical iff V
    transitive (all five are; reste's exclusion is the precedent).
    Successor check: 67=et/veut fork (ISLET 4); 36/37 unknown — record
    what each candidate's selectional frame would need from 36.
  - @1804: «ce qui le V [35] ne [52]» — 94="ne" prov-strong. The «ne»
    needs a verb downstream; check each candidate's parse doesn't strand
    it (52="pas"-polyvalent per K5/N29 — «ne…pas» needs care).
  - @1190: «[06-84-59] que» — que-clause licensed per leg C (attested
    {manifeste,atteste,proteste}; grammatical {déteste,conteste}).
  - @1291 fenced: NO verdict; record per-candidate what 17/35 would need
    to be under the verb parse (17="fois"-WEAK noted as banked lead).
  Frenchman register check: the five verbs' transitivity + «qui le V»
  grammaticality are register-neutral standard French (not argot/dialogue);
  the candidate inventory is diplomatic-corpus-based = despatch-register
  matched (banked caveat, not a new claim).

## Decision bars (pre-registered)
- **PROMOTE (unique verb ID):** ≥2 INDEPENDENT legs (rate + frame +
  84-profile, pairwise independent) AND an independent stem-ID leg (84's
  stem value fixed outside the este windows, or 36/35/06 identified with
  selectional force). EXPECTATION: not met — will report honestly.
- **DEMOTE (→ disfavored):** kill-grade grammatical contradiction at a
  FIRM window, or an 84-profile conflict (a1/a2 fail).
- **KILL:** banked-profile contradiction. EXPECTATION: none.
- **Tie-breaking statement (pre-registered):** if H0 holds, state exactly
  what breaks the tie: (1) independent ID of 84's stem at @1447/@1803
  (second 84-window, same stem); (2) ID of 36 (@1448) or 35 (@1804) with
  selectional restrictions licensing exactly one verb; (3) ID of 06
  (@1190) fixing the 3-cell cut so middle-84 admits exactly one
  candidate; (4) a second «qui le [84-59]» occurrence with discriminating
  context. @1291 un-fences iff 17/35 resolve.

## Anti-gaming
- No manual-tiling bearing counts (F59) — all counts from scripts.
- No re-litigation of settled kills (listed above).
- Red team adjudicates any status change; nothing self-promoted.
- Positions 0-based on the repaired 1,847-pair stream
  (`code/crowd6/redteam/verify_baseline.load_stream`).
