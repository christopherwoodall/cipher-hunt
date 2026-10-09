# Battery verdict: seg-55-61-94-letters

- Target: `seg-55-61-94-letters` (battery-queue.json, priority 3, status queued)
- Claim: "Resolve the letter-level residual at the formula windows: test 'reprenne' (55='re'+61='pren'+94='ne') vs 'prend' (55='pre'+61='nd') segmentation with letter-tier evidence; whichever segmentation the red team adopts constrains options (A)/(B) directly"
- Adverses: none listed.

## Bar (verbatim, pre-registered)

"One segmentation wins on letter-tier evidence or fence with the tie recorded for the red team"

Numbered clauses:
- C1: One segmentation wins on letter-tier evidence.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/seg-55-61-94-letters.lock` on start (agent id + UTC timestamp); no pre-existing lock for this id.
2. Re-derived the repaired stream in-session (1,847 pairs / 96 types); asserts held.
3. Byte-confirmed all `55 61 94` windows and the `55 61` non-94 window.
4. Adopted (never re-litigated or downgraded) the standing verdicts: `seg-61-pren-polyvalence` KILL (2026-10-09), `seg-55-61-21-stem` PROMOTE (2026-10-09), `nece-1169-revisit` NULL (2026-10-09), 94='ne' STRONG LEAD (R17-001).
5. `canonical.py` never used.

## Window-level evidence

The `55 61 94` trigram is exactly **2× stream-wide**, both after the 4-gram `78 45 13 55`:

- **@576** (0-based): `87(ce) 78(ver) 45(ce/dict) 13(?) |55 61 94| 82(m) 06(ent) 06(ent) 50(?) …`
- **@1167** (0-based): `67(et/veut) 78(ver) 45(ce/dict) 13(?) |55 61 94| 87(ce) 83(de) 21(noun) …`

A third `55 61` window without 94 exists at **@1205**: `43(noun) |55 61| 21(noun) 65(noun)…` — the locus of the standing `seg-55-61-21-stem` PROMOTE.

## Findings

### Segmentation A ('reprenne' = 55 're' + 61 'pren' + 94 'ne') — DEAD at kill grade

Segmentation A requires 61 to carry the letter value 'pren'. That value is **kill-grade dead globally**:

- `seg-61-pren-polyvalence` (KILL, 2026-10-09): two independent windows force 61="pren" false with banked neighbors — @1556 ("prene fois" with banked 40='e'/17='fois'; "prene" is not a French word) and @367 ("prenpre" unreadable, 61 followed by 70='pre').
- A frame-restricted rescue (61='pren' only after 55, i.e. only at the formula windows) would be a polyvalence — forbidden by §7 and the bar's clause 3; the battery cannot license it. `nece-1169-revisit` (today) independently fenced the leftward "...ne" rescue: "Its demonstrated word 'prenne' via 61='pren' is kill-grade dead."
- Additionally, A consumes 94 word-internally, which conflicts with 94='ne' STRONG LEAD (R17-001, the negator particle): neither formula window contains any other 'ne', so A leaves the negation slot empty with no licensed alternative.

This is letter-tier evidence: it directly concerns 61's letter content, and it is fatal to A.

### Segmentation B ('prend' = 55 + 61, 94 = 'ne' particle) — WINS

- `seg-55-61-21-stem` (PROMOTE, discriminator success, 2026-10-09): 55-61 = bare finite stem "prend" + noun object at @1205. Adopted without re-litigation by `class-55-det` (KILL), `det-55-1206`, `re81-stem-elim`, `redteam-55-class-input`, and `redteam-55-polyvalence` — five independent batteries treat the "prend(55-61)" unit as standing.
- B keeps 94='ne' as the negator particle (STRONG LEAD intact); no standing value is contradicted.
- 61's stream profile (n=18; followers 94×2 / 96×2 / 59×2 / 21×2, predecessors 55×3 / 62×2) is consistent with a verb-stem-final syllable; nothing in it contradicts the "prend" unit.

### Open residual (scoped, not verdict-affecting)

The seg-55-61-21-stem report flagged the *internal* letter split of "prend" as open: 55='pre'+61='nd' (the claim's framing) vs 55='pr'+61='end'. No letter-tier evidence at battery grade selects between these — both spell "prend" identically at every 55-61 window. This residual is recorded for the red team; it does not affect the A-vs-B segmentation verdict, because both sub-variants keep 94 as a particle.

The full clause-level parse of the two formula windows ("prend ne …" word order) remains anomalous — adopted, not re-litigated: `battery-dict-frame-78-45-13-55-61` (NULL: "W1's 'ne mentent' subjectless, W2's 'ne ce' a hapax anomaly"). The segmentation verdict does not claim a clause parse.

## Per-clause verdict

- **C1 — PASS.** Segmentation B wins on letter-tier evidence: A is kill-grade dead (61='pren' impossible), B is the standing battery promote, and 94='ne' STRONG LEAD is compatible only with B.

## Verdict: PROMOTE (segmentation B)

The red-team options resolve as: **(B) 94 is the negator particle; 55-61 is the word "prend".** Option (A) (94 word-internal, 'reprenne' family) is closed at battery grade.

## Scope

Segmentation only, at the two formula windows (@576, @1167) plus the @1205 unit window. Untouched: 55's and 61's global values/classes, 94='ne' STRONG LEAD, the clause-level anomaly of the formula windows, §7 (no polyvalence declared), and all standing/red-team verdicts. No standing verdict contradicted or downgraded. Canonical-stream caveat stands (rows a4_01/a6_02 offsets unvalidated).

No follow-ups required (promote, not null). The internal letter-split residual (55='pre'+61='nd' vs 55='pr'+61='end') is red-team material if the red team needs it.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-seg-55-61-94-letters.md`
- Queue: `seg-55-61-94-letters` queued → `status: verdict`, `result: promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.seg-55-61-94-letters.tmp` + atomic rename; disk re-validated; own entry only; no downgrade)
- Lock `locks/seg-55-61-94-letters.lock`: created on start, deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
