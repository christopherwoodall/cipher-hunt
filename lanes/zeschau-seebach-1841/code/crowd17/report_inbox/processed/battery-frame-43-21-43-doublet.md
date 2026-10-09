# Battery report: frame-43-21-43-doublet — "43-21-43-le (@1303-1306) is a coordination/reduplication frame; both 43 slots take the SAME value"

- Target: `frame-43-21-43-doublet`
- Worker: battery worker frame-43-21-43-doublet (4c212c04-e4c4-401d-b6fd-2fcbf7aead80)
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt), parsed per code/side-keyhunt/repair_parse.py. 1,847 pairs / 96 types verified in-session. `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched. No data invented. @-offsets are 0-based repaired-stream pair indices (queue convention).

## 1. Bar (verbatim from battery-queue.json, pre-registered before testing)

"resolve iff (a) 21 is named (coordination vs preposition) with 08-43-21-43-77(le)-74 parsing; (b) both 43 slots take one value - if different values are needed, kill the coordination reading with cause; (c) the pre-37-08 left edge (@1300-1302, 70='pre') is parsed or fenced"

Numbered clauses (frozen, not modified after testing):
1. C1: 21 is named as either coordination or preposition, with "08 43 21 43 77(le) 74" parsing under standing values.
2. C2: both 43 slots take ONE shared value; if different values are needed, the coordination reading is killed with cause.
3. C3: the pre-37-08 left edge (@1300–1302, 70='pre') is parsed or fenced with stated cause.

## 2. Method

- Read BATTERY-PROTOCOL.md first; created `locks/frame-43-21-43-doublet.lock` on start (agent id + UTC timestamp 2026-10-09T05:56:56Z; no prior lock).
- Re-derived the repaired stream in-session; 1,847 pairs / 96 types byte-confirmed.
- Adopted, not re-litigated (protocol §5 — never downgrade an existing verdict):
  - 21 = NOUN class (battery-promote F122, cls tier, registry cells); 21="suite" value kill-grade dead (battery-suite-21-qui-que, @134).
  - 43 noun survivor set EMPTY (battery-cond-mesure-43full, 2026-10-09); @21 forces word-internal "43 29" = "[43]er" verb-stem shape (battery-43-29-segment PROMOTE, segmentation only); the @21 shape is escalated to queued `redteam-43-polyvalence` (adopted as venue, not decided).
  - Standing values used as premises only: 70='pre' (GT), 77='le' (prov), 37 predicative (A1 granted, value open), 30='pas' (prom), 46='que' (GT).

## 3. Window-level evidence (all byte-traced)

Target span (0-based), verified on the repaired stream:

| @ | group | row |
|---|-------|-----|
| 1298 | 16 | a7_03 |
| 1299 | 02 | a7_03 |
| 1300 | 70 ('pre') | a7_03 |
| 1301 | 37 | a7_03 |
| 1302 | 08 | a7_03 |
| 1303 | 43 | a7_03 |
| 1304 | 21 | a7_03 (last pair of row) |
| 1305 | 43 | a7_04 (first pair of row) |
| 1306 | 77 ('le') | a7_04 |
| 1307 | 74 | a7_04 |
| 1308 | 52 | a7_04 |
| 1309 | 30 ('pas') | a7_04 |
| 1310 | 92 | a7_04 |

- **Row boundary inside the doublet:** a7_03's stream span ends at @1304; a7_04 begins at @1305. The frame "43 21 | 43" straddles the row boundary.
- **Hapax:** "43 21 43" is the stream's ONLY 43-X-43 doublet (1x). "43 21" bigram: 1x. "21 43" bigram: 1x. Both occur only at this window.
- **21 census (n=30, verified):** windows @99/@109/@115/@118/@134/@171/@176/@196/@231/@359/@371/@505/@706/@719/@850/@937/@1064/@1162/@1172/@1207/@1304/@1422/@1456/@1463/@1466/@1529/@1538/@1631/@1787/@1841. Predecessors: 08x1, 11x2, 68x2, 14x1, 64x1, 48x2, 86x1, 01x2, 96x3, 06x2, 66x1, 02x1, 62x1, 33x3, 83x3, 61x2, 43x1, 46x1. Successors: 62x5, 67x8, 60x4, 65x4, 64x2, 69x1, 35x1, 80x1, 85x1, 43x1, 02x1, 68x1. Matches the adverse's "21->67 x8, 21->62 x5".
- **43 census (n=16, verified):** @21/@43/@244/@258/@343/@386/@439/@563/@1027/@1092/@1126/@1204/@1303/@1305/@1544/@1724. Successors include 77x2, 87x2, 98x2, 00x3, 29x1, 21x1.
- **08 census (n=18, verified):** value fully open; no standing value, no standing kill found in the lane's standing reports.
- **Bigrams at the left edge:** "70 37" 1x (this window only), "37 08" 2x, "08 43" 1x, "43 77" 2x, "77 74" 1x.

## 4. Phase-sensitivity of the frame (byte-level, decisive caveat)

Both adjacent rows have legal rival offsets with zero novel groups (inventories checked against the full 96-type set):

- a7_03 (60 digits, repaired offset=1): offset-0 re-parse gives tail [..., '03','70','84','32','16'] — "43 21" at @1303–1304 dissolves (re-pairs to "...84 32 16").
- a7_04 (55 digits, repaired offset=0): offset-1 re-parse gives head ['37','77','45','23','09','24','40','03'] — the second 43 vanishes entirely; 77 survives but the "43 77" bigram dissolves.

**The "43 21 43" frame dissolves under either adjacent row's rival offset.** It is a canonical-offset object, not a byte-anchored one — the same pattern as seg-a1_01 (row a1_01) and reseg-1481-98 (row a7_10). Any argument depending on the frame must carry the canonicality caveat (68 of 70 upstream row offsets unvalidated). Adoption of either offset is a red-team adjudication act.

## 5. Per-clause verdicts

### C1 (name 21 as coordination or preposition): FAIL
- 21 = NOUN class (battery-promote F122, cls tier) rests on five determiner/preposition NP frames ("la" x2, "par" x3) plus the zero-infinitive-context census (battery-de-frame-21-class, adopted). Naming 21 as a conjunction (coordination) or preposition would contradict the standing class promote — protocol §5 bars downgrading standing state.
- No conjunction or preposition VALUE for 21 has ever been named in the lane; the only named value candidate ("suite") is kill-grade dead (battery-suite-21-qui-que). 21's value is open precisely because no pivot-role value exists (adverse answered: the openness is stated, not a gap).
- A reduplicative "43 PREP 43" reading would need 21 = a preposition — unnameable under the noun class. A conjunctive "43 21 43" reading would need 21 = 'et'-like — 67 is the 'et' cell (sole §7 polyvalence); no 21-conjunction reading exists.

### C2 (both 43 slots take one value): FAIL at kill grade
- No single value is nameable for EITHER 43 slot at battery grade: the noun survivor set is EMPTY (battery-cond-mesure-43full), and the only live shape (@21, "[43]er" verb-stem) is escalated to the red-team `redteam-43-polyvalence` venue — naming it here would preempt the red team and declare §7 polyvalence at battery level.
- The bar's else-branch fires: the coordination reading cannot be stated because it requires a shared value and none exists. This is stronger than "different values needed": the shared-value premise is empty.
- Both slots' predecessors are disjoint in kind (08-open vs 21-open) and both successors' classes are open; no compositional rescue is byte-evidenced.

### C3 (parse or fence the "70 37 08" left edge): FENCED with stated cause
- "70 37 08": 70='pre' GT; 37 predicative (A1 granted, value open); 08 fully open. "70 37" occurs only here; "37 08" 2x. A predicative-37 parse needs a nominal head (absent — left context @1298–1299 is "16 02", both class/value open). Compositional "pre[37]" has no standing letter-composition precedent for 37 with 08 (the granted 37-01 unit is A12, not this). No byte-evidenced parse; fenced with stated cause.

## 6. Verdict: KILL (of the coordination/reduplication reading, at battery grade)

The coordination/reduplication claim is kill-grade dead at battery grade under standing values:

1. C1 fails: 21 cannot be the coordination/preposition pivot without contradicting the standing 21=noun-class promote; no pivot value exists.
2. C2 fails at kill grade: no shared 43 value is nameable (noun set empty; verb-stem shape is red-team venue).
3. The frame itself is phase-sensitive (§4): it dissolves under either adjacent row's rival offset, so it is not byte-anchored.

Scope: battery-grade only. Revival requires (i) red-team adjudication of `redteam-43-polyvalence` naming a 43 value, (ii) re-tiering of 21's noun-class promote to license a pivot role, and (iii) byte-anchored (offset-validated) rows a7_03/a7_04. None is a battery act.

Standing state: nothing contradicted or downgraded — 21=noun class kept, 43's crisis kept in `redteam-43-polyvalence`, 08 open, §7 intact. `canonical.py` never used; R5005, sealed gates, red-team queue untouched.

## 7. Adverses answered

- "21's value open (21->67 x8, 21->62 x5)": verified byte-exact (21 n=30; successors 67x8, 62x5, 60x4, 65x4, 64x2, 69/35/80/85x1, 43x1, 02x1, 68x1). The openness is exactly why C1 cannot resolve; stated, not ignored.
- "43-21-43 has no second instance": verified — the stream's only 43-X-43 doublet (1x); "43 21" x1 and "21 43" x1, both at this window. The hapax nature plus §4's phase-sensitivity is recorded as the reason no generalization is available.

## 8. Follow-ups proposed (kill — optional, verified absent from battery-queue.json)

1. `off-phase-a7-doublet` (P4) — run the seg-a1_01-style constraint sweep under a7_04's offset-1 re-parse (head ['37','77','45','23','09',...]); if constraint-clean, package for red-team offset adjudication alongside a1_01/a7_10.
2. `val-21-pivot-rerun` (P3) — re-run this bar's C1 iff `redteam-43-polyvalence` names a 43 value or 21's noun-class promote is re-tiered by the red team.
