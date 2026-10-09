# Battery report: dict-313-w1-adjudicate

- Target id: `dict-313-w1-adjudicate`
- Claim: "@313's parse is decided between 'ce qui' (A11 two-word exception, standing) and 'verdict qui' (one-word, conditional on 78='ver' LEAD + 45='dict' lead)"
- Date: 2026-10-08
- Worker: battery worker (session 8c503f7d-fa0e-41af-8644-94b6b51edf27)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py; re-derived in-session: 1,847 pairs / 96 types). canonical.py never used. R5005, sealed gates, and the red-team adjudication queue untouched.
- Lock: code/crowd17/next-token/locks/dict-313-w1-adjudicate.lock (created at start, no prior lock existed; deleted on completion).
- Scope: @313-314's parse only. No positional declaration (owned by rpos-w1-exception, queued — not duplicated).

## Bar (verbatim, pre-registered BEFORE testing)

"(a) parse @305-322 under both readings with the left edge '84-24-37' (84='on' granted A15) and the right edge '64-59-32' (59='est' provisional, A1 predicative) — the reading needing fewer ungranted assumptions wins; (b) if tied, fence @314 as A11's 'ce' with no verdict change (never-downgrade) and record ver-78's resolution as the gate that flips it; (c) coordinate with rpos-w1-exception (queued — owns the refined R-pos framing; do not duplicate)."

## Bar restated as numbered pass/fail clauses (not modified after seeing data)

1. Clause (a): parse @305-322 under the 'ce qui' and the 'verdict qui' readings; the reading needing fewer ungranted assumptions (beyond the named grants: 84='on' A15, 59='est' provisional, 32 predicative A1) wins.
2. Clause (b): if the counts tie, fence @314 as A11's 'ce' with no verdict change and record ver-78's resolution as the gate that flips it.
3. Clause (c): rpos-w1-exception owns the refined R-pos framing — confirm it is queued and make no positional declaration here.

## Method

1. Re-derived the repaired stream byte-exactly per repair_parse.py (1,847 pairs, 96 unique).
2. Extracted the W1 window @305-322, the 84-24-37 left-context family, 24->37 exhaustiveness, 37-78 loci, 78-45 loci, and the 45-64 mirror legs — all from the stream, not cited from memory.
3. Counted ungranted value assumptions for each reading using standing values only (§7: banked/promoted/granted; A11 HOLD; 59='est' provisional; 78='ver' LEAD and 45='dict' lead explicitly unsettled).
4. Did not re-run dict-78-45-wordbound's contact profile (cited per the brief's adverse) and did not re-litigate 64='qui'.

## Window-level evidence (@-offsets are 0-based pair indices in the repaired stream)

- **W1 window @305-322:** `02 88 20 17 46 84 24 37 78 45 64 59 32 94 06 11 92 60`
- **Left edge:** @310-312 = `84 24 37`; @310-313 = `84 24 37 78`. **Right edge:** @315-317 = `64 59 32`.
- **84-24-37-78 family:** exactly 2 — @310 and @473. `@310: 84 24 37 78 45 64 59 32 94`; `@473: 84 24 37 78 74 45 93 00 13` — byte-identical left context with 78 stranded before 74 (not 45).
- **24->37 exhaustive:** @311 and @474 only; both lie inside the two 84-24-37 windows.
- **37-78 loci:** @312, @414, @475, @1770.
- **78-45 loci:** @313, @573, @982, @1164.
- **45-64 mirror legs:** @314, @340, @1024 — three legs, all intact in the stream.

## Reading 1: 'ce qui' (A11 two-word exception, standing)

`@305-318: [02] [88] [20] fois(17) que(46) on(84) [24-modal] [37-78]. ce(45) qui(64) est(59) [32]. ne(94)…`

Ungranted assumptions beyond the named grants: **1 — 59='est' provisional** (explicitly budgeted by the bar). All other tokens touching the decision are standing values: 84='on' (A15 grant), 45='ce' (A11 HOLD), 64='qui' (promoted), 32 predicative (A1 frame grant), 17='fois' and 46='que' (banked). The parse is grammatical: "[…] on [modal]s […]. ce qui est [32] ne […]" = "[…] one [modal]-s […]. that which is [32] does not […]".

## Reading 2: 'verdict qui' (one-word, conditional)

`@310-317: on(84) [24-modal] [37] verdict(78-45) qui(64) est(59) [32]…`

Ungranted assumptions: **2 — 78='ver' (LEAD, unsettled per R16-005) and 45='dict' (lead, unsettled)**. This is the mutual conditionality diagnosed by dict-45-circle-break: neither leg is independent. In addition, the reading requires 78-45 word-internal at W1, contradicted on this stream by the @473-476 control re-derived above (byte-identical left context 84-24-37 strands 78@476 before 74) — consistent with battery-w1-314-rebar's promoted finding (battery-level) that 78 is word-final at W1 and every dict parse of W1 is ungrammatical.

## Per-clause pass/fail

1. **Clause (a) — PASS.** Reading 1 needs 1 ungranted assumption (provisional 59='est', budgeted); reading 2 needs 2 ungranted assumptions (78='ver' LEAD + 45='dict' lead) plus a word-internality contradicted at this window. **'ce qui' wins.**
2. **Clause (b) — NOT FIRED.** No tie: the count is 1 (permitted) versus 2. The fence path is moot; the adjudication resolves directly.
3. **Clause (c) — PASS.** rpos-w1-exception is confirmed queued (priority 2, status queued) and owns the refined R-pos framing. This battery makes no positional declaration — the adjudication is local to @313-314's parse.

## Adverses answered

- **"64='qui' promoted"** — ANSWERED. 64@315='qui' is promoted and shared by both readings (the deciding contact, not a discriminator); it was not relitigated.
- **"Contact profile silent on W1 (dict-78-45-wordbound — cite, do not re-run)"** — CITED, not re-run. That battery fenced W1 as the two-word exception with a profile-neutral 64 follower; the boundary cannot decide W1. This adjudication is consistent with that fence and does not reopen it.

## Verdict: promote

**The adjudication decides for 'ce qui': 45@314 parses as 'ce', the standing A11 two-word exception.** The 45-64 mirror-leg family (@314/@340/@1024) stays intact; A11 HOLD is strengthened, not changed; no standing verdict is contradicted or downgraded (the never-downgrade rule is honored — promoting 'dict' here would have required overwriting A11's exception). The result corroborates battery-w1-314-rebar's promoted W1 finding (battery level, pending red-team ratification) rather than duplicating its structural work. Scope: @313-314's parse only. No positional declaration made; the ver-78 lead (R16-005) and the fork-78-45 red-team gate are untouched, as is the queued rpos-w1-exception. No sealed gate, R5005, or red-team adjudication queue touched.

## Reproducibility

Stream re-derivation: `code/side-keyhunt/repair_parse.py` (`load_rows` + `parse` with `repaired_offsets.json`), run in-session 2026-10-08: 1,847 pairs / 96 types; W1 window `@305-322 = 02 88 20 17 46 84 24 37 78 45 64 59 32 94 06 11 92 60`; 84-24-37-78 x2 (@310, @473); control @473-476 = `84 24 37 78 74`; 24->37 x2 (@311, @474); 37-78 x4; 78-45 x4; 45-64 x3 (@314/@340/@1024). No writes outside this report, the queue edit (own entry only, temp-file + rename), and the lockfile (deleted).
