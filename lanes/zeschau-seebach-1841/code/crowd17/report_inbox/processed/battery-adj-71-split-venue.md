# Battery report: adj-71-split-venue

**Target:** `adj-71-split-venue` — gather-only red-team input package: uniform adjective killed, @233 locus fenced at battery grade, 71 already split-shaped (nominal@1337 vs non-nominal@925); any adjective arm needs a §7 split declaration.

**Worker:** battery-worker-adj-71-split-venue (agent a979bf72-c7cf-493a-a68b-339cfc312a04). Date: 2026-10-09.

**Stream:** repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`). `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched. Offsets below are 1-based unless noted (0-based in parentheses where the queue convention needs it).

**Terms (ASD-STE100):** "gather-only" = this battery collects and packages evidence for the red-team docket; it performs no adjudication and declares no value, class, or split. "Split declaration" = the red-team act under §7 adding a second (or further) licensed value/class for one cell. "Lead" = a battery-level verdict awaiting red-team ratification. "Fence" = the claim is blocked for now, not killed.

## Bar (verbatim from battery-queue.json)

"Gather-only: deliver the package; no adjudication (red-team venue)"

**Numbered clauses (pre-registered before reading data):**
- C1: Deliver a ruling-ready package: uniform-adjective kill, @233 locus fence, 71's split shape, with byte evidence and source citations.
- C2: Perform no adjudication — no split declared, no class/value named, no standing verdict downgraded.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/adj-71-split-venue.lock` on start (agent id + 2026-10-09T18:44:55Z), deleted on completion.
2. Re-read the four battery source reports at `code/crowd17/report_inbox/processed/`: `battery-class-71-adjective.md` (KILL), `battery-adj-71-234-locus.md` (NULL fence), `battery-val-71-quant-nominal.md` (PROMOTE finding grade), plus supporting `battery-nom-71-1336-value.md` (NULL), `battery-quant-71-925-value.md` (NULL), `battery-un-71-det-census.md` (NULL).
3. Checked the red-team record: `code/crowd17/report_inbox/processed/next-token-redteam-r19.md` (R19-186) and `code/crowd17/report_inbox/processed/next-token-redteam-r20.md` (carry-forward table).
4. Checked the registry: `code/table-grid/table-registry.json` (`cells` — 71 absent; `_meta` carries the 71 §7 split-candidate note).

## Findings (ruling-ready package)

### P1. Uniform epithet-adjective 71 is KILLED at battery kill grade

Source: `battery-class-71-adjective.md`, 2026-10-09, verdict KILL. Census n(71)=7, all byte-verified:

| Window (1-based) | Context | Adjective test |
|---|---|---|
| @234 | `96 21 60 [71] 51 70 98` | compatible (sole one) |
| @326 | `60 15 63 [71] 10 01 19` | indeterminate (63 open) |
| @712 | `53 12 48 [71] 12 63 00` | incompatible (composes 'donne', a finite verb) |
| @925 | `49 74 74 40 08 65 [71] 17 61 96` | **71≠adjective forced (kill grade)** |
| @1337 | `94 70 52 39 83 86 [71] 64 60 08 65 64 52` | **71≠adjective forced (kill grade)** |
| @1565 | `17 11 26 30 06 60 [71] 50 29 24` | indeterminate, leaning fail (headless) |
| @1614 | `92 65 23 08 55 83 [71] 48 31 76` | indeterminate (83 open) |

Kill-grade details: at @925 ('t 65 [71] fois'), 71 as postposed epithet of 65 strands bare 'fois' (ungrammatical — 'fois' never stands bare); 71 as prenominal adjective of 'fois' ('derniere fois'-shaped) needs a determiner before the adjective, which 65 is not. At @1337 ('[86-INF] [71] qui'), a bare infinitive taking a postposed epithet without a determiner is ungrammatical ('le prendre'-shaped determiners are required), leaving 'qui' with no NP to attach to. Two independent windows; kill grade.

### P2. The @234 locus-level adjective reading is FENCED at battery grade

Source: `battery-adj-71-234-locus.md`, 2026-10-09, verdict NULL (fence). Window 0-based @233, row a2_01: `96 21 60 71 51 70 98` = "par [21-noun] [60-adj] [71] [51] pre…".

- C1 fail: zero positive byte evidence for an adjective-shaped 71. The inventory offers nominal (forced @1336), non-nominal/quantifier-like (forced @924), determiner 'une' (frequency leader). 'Sits after [60-adj]' is frame evidence, not value evidence; the slot also admits adverbs, quantifiers, or a word-internal onset with 51 (51's class open).
- C2 fail: period-corpus check (57 French files, German excluded) — **0 genuine** bare-stacked "PREP DET N ADJ ADJ"; the single regex candidate ("dans une conversation fort longue") is adverb+adjective, a false positive. Coordinated "ADJ et ADJ": 55 attestations — the grammatical norm. The target window is stricter (bare 21, no determiner).
- Not a kill: 71's class at this window stays open (adverb/quantifier/word-internal arms untested). Any future adjective arm for 71 is red-team §7 venue.

### P3. 71 is already §7 split-shaped (nominal@1337 vs non-nominal@925)

Source: `battery-val-71-quant-nominal.md`, 2026-10-09, verdict PROMOTE (finding grade); red-team R19-186 — **GRANT (finding grade: §7 split candidate)**, with the registry `_meta` recording "71 §7 split candidate" and "R20: 71 split declaration".

- @1337 forces nominal: "83 86 71 64" — 86=INF (registry class), 64='qui' (prom) needs a nominal antecedent; '[86-INF] [71-noun] qui' = direct object head of the qui-relative is the only viable class.
- @925 forces non-nominal: "71 fois" — bare "NOUN fois" is ungrammatical at any period; 71 is quantifier/determiner-like or '71 17' is a fused adverb ('toutefois'-shaped).
- "65 71" unit rescue refuted on three independent grounds: (1) row boundary (65 ends row a5_09, 71 starts a5_10 — word-internal bigrams do not straddle rows without cause); (2) grammar ('noun-unit fois' is the same ungrammatical shape); (3) class contradiction (65 is noun-class; the unit would need to be quantifier-like at @925).
- Sub-lexical support at @712: "48 71 12" = 'e 71 n' (48='e', 12='n' both promoted letters) — 71 must compose sub-lexically there.
- No split declared by either battery or red team: 67 et/veut remains the sole declared polyvalence (§7 honored).

### P4. Value routes are fenced at both anchor windows

- `battery-nom-71-1336-value.md` (2026-10-09, NULL): '86 71' is a stream hapax (1x); every neighbor's value is open (86/65 class-only; 83/60/08/52/38 fully open). Naming a nominal value would pre-judge the red-team split adjudication — red-team venue.
- `battery-quant-71-925-value.md` (2026-10-09, NULL): value route fenced by underdetermination among ≥4 survivors (une/deux/plusieurs/trois; chaque weakly disfavored; la excluded by the homophone kill). 'Une' is the frequency leader; no cell holds 'un'/'une' at any grade (`battery-un-71-det-census.md`, 2026-10-09, NULL), so no homophony exclusion fires.

### P5. Registry and red-team venue state

- 71 is **absent** from `table-registry.json` `cells` (checked 2026-10-09): no standing red-team value or class on 71.
- R20 carry-forward: "03 / 71 §7 splits — DEFER — no docket item owned them; R19-178 (stem-03) and R19-186 (71 split-candidate) stand on their own dockets." R19-186's own text says "R20: 71 split declaration" — the docket item was pointed at R20 and deferred.

### P6. What the red team must decide (input, not verdict)

1. **71 §7 split adjudication** — declare or reject the nominal@1337 vs non-nominal@925 split (R19-186 grant stands; declaration still outstanding).
2. **Adjective-arm venue** — if the split is declared, 71 would carry two classes; any adjective reading (e.g. @234 'par [21] [60] [71]') would be a **third** class and needs its own §7 declaration on top of the split. If the split is rejected, the adjective question collapses back into the single-class inquiry.

## Per-clause pass/fail

- **C1 — PASS.** Package delivered: P1 (uniform-adjective kill), P2 (@233 locus fence), P3 (split shape, R19-186 grant), P4 (value fences), P5 (registry/R20 venue), P6 (decision surface) — all with source citations.
- **C2 — PASS.** No adjudication performed: no split declared, no class/value named, no verdict downgraded, §7 intact, red-team venue untouched.

## Verdict: PROMOTE (gather-only packaging)

This is a packaging verdict only — it delivers the evidence package and makes **no cipher-value, cipher-class, or §7 split claim**. Adjudication belongs to the red team.

## Scope

- No standing or red-team verdict contradicted, downgraded, or re-litigated. R19-186 (GRANT, finding grade) and R20's deferral stand exactly as written.
- §7 intact: 67 et/veut remains the sole declared polyvalence.
- R5005, sealed gate instances, red-team adjudication queue untouched.
- Canonical-stream caveat stands (68/70 upstream row offsets unvalidated).

## Follow-ups

None required at battery grade — the deliverable is the package itself, and adjudication is red-team venue. The red-team docket owns: (a) the 71 §7 split declaration (deferred at R20), (b) any adjective-arm declaration (third class, conditional on (a)).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-adj-71-split-venue.md` (this file).
- Queue: `adj-71-split-venue` → `status: verdict`, `result: promote`, date 2026-10-09 (pre-write asserted queued/verdictless; temp-file + rename; JSON re-validated from disk; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/adj-71-split-venue.lock` created on start (agent a979bf72-c7cf-493a-a68b-339cfc312a04, 2026-10-09T18:44:55Z), deleted on completion.
