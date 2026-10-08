# Battery report: dict-45 — 45="dict"? (the "-dict" syllable rival)

- Target: `dict-45` — claim: 45="dict"?
- Worker: 6aa4aa59-76e6-4e24-baa3-1bd28e7359f6
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed like `code/side-keyhunt/repair_parse.py`). `canonical.py` not used. R5005 not touched.
- Lock: `code/crowd17/next-token/locks/dict-45.lock` created 2026-10-08T08:51:29Z, no pre-existing lock; deleted on completion.
- Offsets below are 0-indexed stream positions. (Queue evidence "@573/@982" = 78-positions 0-indexed; fork battery's @314/@574/@983/@1165 = 1-indexed 45-positions.)

## HEADLINE — ESCALATE TO RED TEAM

**Verdict: NULL.** The claim reduces to a positional reading (45="dict" iff preceded by 78, "verdict"; 45="ce" elsewhere), which requires a **second positional polyvalence** — a red-team-only declaration per §7 (67 et/veut is the sole true polyvalence). This battery cannot promote without contradicting the standing A11 HOLD (45="ce", zero contradictions across 22 windows), and cannot kill because no window forces "dict" false at the four 78-45 loci and 78="ver" is still unsettled (R16-005 LEAD, ver-78 battery null 2026-10-08). The fork battery (fork-78-45-adjudication, null 2026-10-08) already framed this exact positional rule as needing red-team declaration; this battery concurs and adds the closed host inventory below.

## Bar (verbatim from battery-queue.json)

> promote iff 'verdict' frames parse + 45 contact profile matches '-dict' syllable

Numbered clauses (pre-registered, unmodified):

1. **(a)** The 'verdict' frames parse — the four 78-45 windows read as "verdict ..." (PASS/FAIL per window).
2. **(b)** 45's contact profile matches the '-dict' syllable — i.e., 45 behaves like the bound French syllable "-dict-" (as in verdict/dicter/dictée), not like a free word.

Adverse (must be answered for promote): 45='ce' HOLD (A11) — 'dict' is the syllable rival.

## Method

1. Re-parsed the repaired stream (1,847 pairs, 96 types — matches repair_parse.py asserts).
2. Census of 45 (n=22) and 78 (n=31): full predecessor/follower distributions.
3. Located all four 78-45 bigrams: 78@313, 78@573, 78@982, 78@1164 (45 at +1 each).
4. Parsed each window under 78='ver' (R16-005 LEAD, **not granted**) + 45='dict', using only granted/banked values otherwise (87=ce, 64=qui, 94=ne, 82=m, 47=ce; provisional 59=est; 67='veut' positional rule).
5. Classified all 22 windows of 45 under the general 'dict' reading vs the positional reading; checked the A11 HOLD legs (45-64 x3) on the repaired stream.

## Window-level evidence (@-offsets, 0-indexed)

**45 census (n=22).** Predecessors: 78 x4, 74 x3, 76 x2, 50 x2, 96 x2, 59/14/11/63/77/51/64 x1.
Followers: 93 x3, 64 x3, 23 x3, 28 x2, 13 x2, 91/54/88/46/94/08/01 x1.

**The four 78-45 loci (clause-a test set):**

- **W1 — 78@313** (row a2_04): `84 24 37 78 45 64 59 32 94` → "on en [37] **verdict** qui est [32] ne..." — 64='qui' granted, 59='est' provisional. Parses conditionally clean; left edge `37 78` boundary is owned by queued w1-314-ambig.
- **W2 — 78@573** (row a3_02): `52 87 78 45 13 55 61 94 82 06 06` → "**ce verdict** [13-55-61] ne m' [06] [06]..." — 87='ce' granted, 94='ne' promoted, 82='m' banked. "ce verdict" is a clean NP; 13-55-61 open (owned by queued dict-frame-78-45-13-55-61). Parses conditionally clean. This is one of the two 'ce verdict' legs (87-78-45 @572-574).
- **W3 — 78@982** (row a6_01): `76 47 78 45 01 24 89 48 01` → "**ce verdict** [01] en [89] [48]..." — 47='ce' granted (allophone tier). Parses conditionally clean. Second 'ce verdict' leg (47-78-45 @981-983). Note: 47-78-45-01 admits the "ce verdict-ci" reading if 01='ci' (see follow-up F1).
- **W4 — 78@1164** (row a6_09): `21 67 78 45 13 55 61 94 87 83 21` → "veut **verdict** [13-55-61] ne ce de..." — bare "verdict" after 67='veut' has a **determiner gap** (no le/ce); strained under the two-token reading. Not forcing-false: the 5-syllable unit reading (78-45-13-55-61 one word) is open and owned by queued dict-frame-78-45-13-55-61 bar (c).

**'ce verdict' x2 confirmed** on the repaired stream: 87-78-45 @572-574, 47-78-45 @981-983.

**Clause-(b) profile test — all 22 windows of 45 (ctx −3..+3):**

| 45@ | context | under general 45='dict' |
|---|---|---|
| 14 | 76 45 91 | "[76] dict [91]" — ungrammatical |
| 104 | 59 45 28 | "est dict [28]" — ungrammatical |
| 262 | 74 45 93 | "[74] dict [93]" — ungrammatical |
| **314** | 78 45 64 | "**verdict** qui" — parses (conditional) |
| 332 | 50 45 54 | "[50] dict [54]" — ungrammatical |
| 340 | 14 45 64 | "[14] dict qui" — ungrammatical (A11 mirror leg) |
| 401 | 11 45 88 | "la dict [88]" — ungrammatical |
| 437 | 63 45 46 | "[63] dict que" — ungrammatical |
| 478 | 74 45 93 | "[74] dict [93]" — ungrammatical |
| 569 | 76 45 94 | "[76] dict ne" — ungrammatical |
| **574** | 87 78 45 13 | "ce **verdict** [13-55-61]" — parses (conditional) |
| 603 | 96 45 93 | "par dict [93]" — ungrammatical |
| 678 | 77 45 23 | "le dict [23]" — ungrammatical |
| 697 | 50 45 28 | "[50] dict [28]" — ungrammatical |
| 974 | 51 45 08 | "[51] dict [08]" — ungrammatical |
| **983** | 47 78 45 01 | "ce **verdict** [01]" — parses (conditional) |
| 1024 | 64 45 64 | "qui dict qui" — ungrammatical (A11 mirror leg) |
| 1055 | 74 45 23 | "[74] dict [23]" — ungrammatical |
| **1165** | 67 78 45 13 | "veut **verdict** [13-55-61]" — strained (determiner gap) |
| 1201 | 29 45 58 | "er dict [58]" — ungrammatical |
| 1214 | 96 45 36 | "par dict [36]" — ungrammatical |
| 1551 | 92 45 23 | "[92] dict [23]" — ungrammatical |

A bound syllable "-dict-" predicts: near-deterministic "ver" predecessor, vowel-initial or word-final followers, no free-word distribution. Observed: 18/22 windows have non-78 predecessors and free-word followers (93 x3, 23 x3, 28 x2 clusters — the ce45-frames finder confirmed zero 87-contact on these clusters; 45-64 x3 'ce qui' mirror per A11 re-derived above @314/@340/@1024).

## Per-clause verdicts

1. **Clause (a) — INCONCLUSIVE (conditional pass, not assertable).** W1/W2/W3 parse cleanly as "verdict ..." and W4 strains only on the determiner gap (open to the queued 5-gram unit reading) — **but every parse is conditional on 78='ver', which is LEAD-not-granted** (R16-005; ver-78 battery null 2026-10-08). The clause cannot pass under granted values at battery level.
2. **Clause (b) — FAILS as a general value (kill grade on the general reading); SURVIVES only as a positional value.** As a general syllable value, 18/22 windows are ungrammatical under 'dict' — distributional rejection. As a positional value (45='dict' iff pre=78), all four loci are consistent — but positional polyvalence is a red-team-only declaration per §7.

**Adverse status:** 45='ce' HOLD (A11) stands **untouched and unanswered** — its mirror legs re-derive on the repaired stream (45-64 x3 @314/@340/@1024; note @314 is itself a fork window, owned by w1-314-ambig). Promoting 'dict' generally would contradict a standing red-team adjudication; promoting it positionally needs the red-team polyvalence declaration.

## Verdict: NULL

- Not promote: adverse unanswered + clause (a) conditional on unsettled 78='ver' + positional reading needs red-team declaration (§7).
- Not kill: no window forces 45='dict' false at the four 78-45 loci; the general-value kill is already implicit in the standing A11 HOLD and was never the live claim ("'dict' is the syllable rival" — a rival for the 78-45 windows, framed positionally by fork-78-45-adjudication).
- No contradiction of a standing red-team verdict introduced by this battery (A11 HOLD and R16-005 LEAD both respected).

## Follow-ups (for the supervisor to queue; none duplicate existing queued targets)

- **F1 `dict-45-w3-ceci`** (priority 2): positive-leg battery for W3 — test 47-78-45-01 @981-984 as "ce verdict-ci" under 78='ver'(LEAD)+45='dict'+01='ci'. Bars: (a) 01='ci' coheres with ci-01-value's discriminators (coordinate, do not re-run them); (b) the '24 89' ("en [89]") continuation parses after the NP; (c) if 01≠'ci', record W3 neutral, not adverse.
- **F2 `dict-45-ce-rival-1165`** (priority 2): rival re-read of W4 @1164-1165 under 45='ce' HOLD ("21 67 78 45 13 55 61" two-token). Bar: produce the best 'ce' parse with ≤1 non-granted assumption, or record W4 as double-residual (ungrammatical under both two-token readings) — feeds the red-team polyvalence decision. (Does not duplicate dict-frame-78-45-13-55-61, which owns the 5-gram unit parse.)
- **F3 `dict-45-host-inventory`** (priority 3): bound-syllable host inventory — scan all 22 windows of 45 for any non-78 '-dict-' word host (dicter/dictée/diction/prédiction-shaped frames). Bar: name ≥1 non-78 host window parsing as a French dict-word, or certify 'verdict' as the sole host (closed inventory → strengthens the positional-polyvalence framing for the red team).

## Notes for the red team

- If ver-78 ever promotes 78='ver', clause (a) upgrades to a clean 3/4 pass (W4 still gated on the determiner/unit question) — see queued fork-78-45-rerun and ver78-45-dependency-gate, which already own that rerun.
- The decision this battery cannot make: declare 45 positionally polyvalent ('dict' after 78, 'ce' elsewhere), or re-read the four 78-45 windows under 45='ce' (W2 "ce [78] ce"? — awkward; W4 "veut [78] ce" — worse). Either path is red-team adjudication, not battery work.
