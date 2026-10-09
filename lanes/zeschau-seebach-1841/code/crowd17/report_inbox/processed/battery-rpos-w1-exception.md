# Battery verdict: rpos-w1-exception

**Target:** `rpos-w1-exception` (priority 2)
**Claim:** W1 falsifies unconditioned R-pos (45='dict' iff preceded by 78) — refined rule for red team
**Verdict: PROMOTE** (evidence package + refined rule candidacy for red team; no value named, no positional rule declared)

## Bar (verbatim from battery-queue.json)

> (a) W1 re-derived with 78 shown infinitive-final from this report; (b) state the refined rule candidate (45='dict' iff 78 is word-MEDIAL) with W1-W4 classified under it; (c) no red-team declaration made - evidence gathered for the S7 positional-rule decision only

Numbered clauses:
1. (a) W1 re-derived from the repaired stream in this report, with 78@313 shown word-FINAL (infinitive complete at 78, boundary before 45@314).
2. (b) Refined rule candidate stated: 45='dict' iff 78 is word-MEDIAL (78–45 word-internal, 78 not word-final); W1–W4 each classified under it.
3. (c) No red-team declaration made; this report gathers evidence for the §7 positional-rule decision only.

## Adverses (verbatim)

> R-pos never adopted (red-team act); W2-W4 untested under the refined rule (dict-78-45-wordbound verdict null)

## Method

- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`). `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Byte facts below re-derived in-session. Structural parses (modal-24 + infinitive complement; W2 one-word boundary; W4 double-residual) coordinated from promoted/nulled batteries, not re-run — cited with scope.

## 1. Locus census (re-derived)

78→45 adjacencies on the repaired stream are exhaustive at n=4 (78 index):

| Locus | 78@ | 45@ | Left context | Follower |
|---|---|---|---|---|
| W1 | 313 | 314 | 84 24 37 (@310–312) | 64 (@315) |
| W2 | 573 | 574 | 87 (@572) | 13 55 61 (@575–577) |
| W3 | 982 | 983 | 47 (@981) | 01 (@984) |
| W4 | 1164 | 1165 | 67 (@1163) | 13 55 61 (@1166–1168) |

Unconditioned R-pos ("45='dict' iff preceded by 78") predicts 45='dict' at all four. W1 already breaks it (45@314 = 'ce', A11 HOLD, adjudicated PROMOTE by battery-dict-313-w1-adjudicate 2026-10-08).

## 2. Clause 1 — W1 re-derived, 78 infinitive-final

W1 window @305–322 re-derived byte-exact: `02 88 20 17 46 84 24 37 78 45 64 59 32 94 06 11 92 60` (row a2_04).

- `84-24-37-78` occurs exactly x2 on the stream: @310–313 and @473–476. Byte-identical left context.
- 24→37 is exhaustive x2: n(24)=52, 37-successors = 2, both inside the two 4-gram windows. The frame is exclusive.
- Control @473–476: `84 24 37 78` followed by **74** (@477), a non-45 follower. In byte-identical left context, 78 strands before a non-45 follower — 78's pairing with 45 at W1 is not forced by the left context; the adjacency is coincidental.
- 78 census: n(78)=31; 37-predecessors x4 (two inside the 84-24-37-78 frames).
- Coordinated (w1-314-rebar, PROMOTE): 37–78 is the complete infinitive complement of modal-24 (24 = finite modal verb, class-level; 37 post-verbal per A1) — word-internal, **ending at 78**. The @475 control (78 before 74) confirms the infinitive is complete at 78 regardless of follower: 78 is word-FINAL.
- Therefore a word boundary falls between 78@313 and 45@314; 45@314 is word-initial → 'ce' (A11 HOLD; 45–64 mirror leg intact).

**Clause 1: PASS.** 78@313 is word-final; unconditioned R-pos is falsified at W1 (45 preceded by 78 yet = 'ce').

## 3. Clause 2 — refined rule candidate and W1–W4 classification

**Refined rule candidate (for red-team §7 decision, not declared here):**
> 45='dict' iff 78 is word-MEDIAL — i.e., the 78–45 adjacency is word-internal AND 78 is not word-final. Equivalently: post-78 45 is 'ce' iff a word boundary falls between 78 and 45.

Classification:

| Window | 78 word position (evidence) | Rule prediction | Observed | Status |
|---|---|---|---|---|
| W1 @313 | FINAL — infinitive complete at 78 (§2); boundary before 45 | 45='ce' | 45='ce' (A11 HOLD; dict-313-w1-adjudicate PROMOTE) | **consistent** |
| W2 @573 | MEDIAL — one-word boundary promoted (verdict-w2-574-gate: 78–45 one word; two-word "ce ver ce" impossible); 94–82 'ne m\'' elision frame | 45='dict' | 'dict'-syllable owns @574 | **consistent, conditional** on unsettled 78='ver' LEAD (R16-005) |
| W3 @982 | UNDETERMINED — w3-ceci nulled (01='-ci' not established); one-word "verdict-ci" vs two-word boundary undecided at battery level | — | neutral (W3 recorded neutral per its bar) | **unclassified** |
| W4 @1164 | UNDETERMINED — double-residual (dict-45-ce-rival-1165): ungrammatical under both two-token readings; 5-gram unit escape fenced to dict-frame-78-45-13-55-61 (null) | — | residual, pending red-team polyvalence decision | **unclassified** |

Falsification audit of the refined rule: no window contradicts it. W1 and W2 are consistent (W2 conditional on the 78='ver' lead). W3 and W4 are neutral — the rule makes no prediction where no two-token word segmentation is established, and neither window forces the claim false. The refined rule survives the full locus set; the unconditioned version does not survive W1.

**Clause 2: PASS.**

## 4. Clause 3 — no declaration

No positional rule is declared in this report. The refined rule is stated as a *candidate* for the red team's §7 positional-rule decision. No value for 45 or 78 is named, granted, or promoted here. A11 HOLD (45='ce') untouched. R-pos was never adopted — nothing is overturned.

**Clause 3: PASS.**

## Adverses — answered

1. "R-pos never adopted (red-team act)": answered — this report adopts nothing; the refined rule is evidence and candidacy only, explicitly fenced for red-team decision.
2. "W2–W4 untested under the refined rule (dict-78-45-wordbound verdict null)": answered — W2 classified via verdict-w2-574-gate's promoted one-word boundary (coordinated, not re-run); W3/W4 classified as neutral/unclassified with stated cause (boundary undetermined at battery level; dict-78-45-wordbound's null cited, not re-litigated). The classification does not depend on the nulled boundary battery.

## Verdict: PROMOTE

All three bar clauses pass; both adverses answered. **Promoted: the evidence package** — (i) W1 falsifies unconditioned R-pos at kill grade (45@314 preceded by 78 yet = 'ce', with 78 shown word-final from this report's re-derivation); (ii) the refined rule candidate (45='dict' iff 78 word-medial) with the W1–W4 classification table above, consistent across all four loci (two consistent, two neutral, zero contradictions). Scope: red-team candidacy only. No standing verdict contradicted or downgraded.

## Recommended next steps (not formal follow-ups; for supervisor/red-team awareness)

- The refined rule's W2 leg is conditional on the unsettled 78='ver' LEAD (R16-005) — ver-78 resolution flips W2 from conditional-consistent to decided.
- W3's classification awaits the 78–45 boundary decision at @982 (w3-ceci's null left it open).
- W4's classification awaits the red-team polyvalence decision (or the fenced 5-gram unit reading).

## Bookkeeping

- All counts re-derived in-session from the repaired stream (1,847 pairs). `canonical.py` never used.
- R5005, sealed gate instances, and the red-team adjudication queue untouched.
- Lock `locks/rpos-w1-exception.lock` created on start with agent id + UTC timestamp; deleted on completion.
