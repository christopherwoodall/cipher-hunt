# Battery report: par43-ce-scope

- Target id: `par43-ce-scope`
- Claim: "Adjudicate the hostile '96 43 87' x2 windows (@343/@1027, 'par [43] ce [01]'), which resist every class under standing values and block ANY 43 class promote. Test: (a) 87='ce' scope at these windows (is 'ce' really the token here, or does the 6-gram '45-64-96-43-87-01' invite resegmentation?); (b) '43 87' as a unit; (c) 96='par' alternatives. Discriminating frames for the red-team docket."
- Date: 2026-10-09
- Worker: battery worker (subagent 82dfaaf4-92a9-46f6-8d82-56716cc44243)
- Stream: repaired 1,847-pair / 96-type parse re-derived in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (parsed per `code/side-keyhunt/repair_parse.py`); asserts held (1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

## Bar (verbatim, pre-registered before testing)

"discriminating frames: 87-scope, '43 87' unit, 96 alternatives"

## Bar restated as numbered pass/fail clauses

- **C1 (87-scope):** state 87's scope at the two windows — free 'ce' vs bound "ceci" vs leftward resegmentation — with byte evidence; produce the discriminating frame.
- **C2 ('43 87' unit):** test whether 43 and 87 compose one word; fence or kill the unit reading with stated cause.
- **C3 (96 alternatives):** enumerate alternative readings of 96 at these windows and kill or fence each; state what fixes 96's role.

Verdict rule: the bar names a docket input package, not a promote/kill claim. Verdict NULL with the discriminating frames as the deliverable, unless a clause resolves at kill grade.

## Standing state adopted (not re-litigated)

- 87='ce' granted/promoted; 96='par' granted (A15); 64='qui' granted; 45='ce' HOLD (A11).
- `ce-frame-45-64-96-43-87-01` (2026-10-08, NULL): the byte-identical 6-gram parses as "ce qui par [43] ce [01]" only under the conditional 43="suite" (sole noun-43 candidate grammatical after "par"); left edges fenced.
- `par43-adverbial-attestation` (2026-10-09, PROMOTE): bare "par mesure"/"par condition" adverbials unattested (Littré + TLF); par-43 noun kill terminal pending only the @21 polyvalence ruling (red-team docket).
- `ci-01-value` (KILL): 01='ci' as a general token value killed.
- `ci-bound-01` (NULL): bound '-ci' survives at @984 ("ceci [verb]"), compatible at @195; @345 and @1029 neighbor-driven residuals.
- `residual-1029-infinitive` (PROMOTE): @1026–1040 reads "Ceci, [03-stem]er! [80]-le, la première fois!" with 87='ce' granted and 01 as bound '-ci' (battery-level null premise).

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/par43-ce-scope.lock` on start; deleted on completion.
2. Re-derived the repaired stream; byte-verified both loci. The queue's "@343/@1027" are 1-based pair indices; 0-based hits are **342** and **1026** (96 43 87 at 0b 342–344 and 1026–1028).
3. Ran contact censuses: '96 43 87' x2, '43 87' x2, '87 01' x2, '45 64 96 43 87 01' x2 (byte-identical), '64 96' x3, 96's full follower/predecessor profile (n(96)=21), 87's follower profile (n(87)=32), 43's predecessor/follower profiles (n(43)=16).

## Window-level evidence (0-based @)

- **W1 (0b@342, row a2_05):** `…03 64 31 14 | 45 64 96 43 87 01 | 06 70 12 94 74 67 78…` = "…qui(64) [31] [14] | ce(45) qui(64) par(96) [43] ce(87) [01] | [06] pre(70) n(12) ne(94) [74] et/veut(67) [78]…"
- **W2 (0b@1026, row a6_03):** `…53 84 92 64 | 45 64 96 43 87 01 | 03 29 80 77 11 70 82 34 29 40 17` = "…[53] on(84) [92] qui(64) | ce(45) qui(64) par(96) [43] ce(87) [01] | [03]er(29) [80]-le(77) la(11) pre-m-i-er-e(70-82-34-29) fois(17)"
- The 6-gram is byte-identical; the windows diverge at the follower of 01: W1 → 06, W2 → 03. '01 06' and '01 03' are each stream hapax.
- Both windows open "[X] ce qui par [43] ce [01]" with X=14 (W1) / X=64 (W2) — i.e. a "ce qui" relative directly before "par [43]".

## C1: 87-scope — discriminating frame produced

Three scope readings tested:

- **R1 — 87='ce' free demonstrative pronoun, "ce [01]":** licensed by the grant. 87 takes "ce qui" followers x5 stream-wide (0b@148/180/1767/1775/1800), so 87 as a free demonstrative is distributionally anchored. At W2 this is the weaker reading: the promoted @1029 parse reads "87 01" as one word (R2).
- **R2 — "87 01" = "ceci" (bound '-ci'):** W2 licenses it — `residual-1029-infinitive` PROMOTE reads "Ceci, [03-stem]er! [80]-le, la première fois!" with 87-01 as the dislocated topic head. '87 01' occurs exactly 2x stream-wide (only these windows), so the composition is locus-bound, not distributional. At W1, R2 is fenced: the follower is 06, and `ci-bound-01` fenced @345's "87 01 06 70 12 94" as a 06-driven residual ("ce [01] entreprenne [74]…" does not parse in full context; the 06 "entreprenne" leg is independently killed).
- **R3 — leftward resegmentation (87 belongs with 43):** no French license (see C2). Fenced.

**Discriminating frame (docket input):** the byte-identical 6-gram does NOT determine 87's scope — the scope is follower-determined and window-divergent. W2's 87 scopes rightward as bound "ceci" (licensed by the @1029 exclamatory-infinitive promote); W1's 87 scopes as free "ce" followed by an unparseable tail (06-driven residual). Any red-team ruling on 43 at these windows must scope 87 per-window, not per-gram.

## C2: '43 87' unit — fenced (unlicensed, not kill-grade)

- '43 87' occurs exactly 2x stream-wide — only inside these two windows. Zero independent repetition leverage.
- 87='ce' is a granted free demonstrative; French has no productive "[stem]+ce" word family that could host a 43-87 composition.
- 43 is valueless at battery grade (noun kill terminal per par43-adverbial-attestation; only reopen path is the @21 polyvalence ruling), so composition is untestable on spelling grounds — but no composition is *needed*: R1/R2 (C1) cover both windows without it.
- The unit reading is therefore fenced as unlicensed, not killed at kill grade (no named value is forced false). It is not a live rival for the docket.

## C3: 96 alternatives — fixed as 'par'; hostility is 43-driven

- 96's profile (n=21): 12 distinct follower types {00x3, 87x3, 21x3, 43x2, 45x2, 82x2, 56/47/40/09/48/86 x1} — the signature of a free preposition taking nominal/demonstrative complements, not of a bound syllable. 43 is one follower among twelve; no 96-43 composition signature exists.
- '64 96' x3: the third instance (@149, `64 96 47 46` = "qui par ce que") shows 96='par' composing naturally with a demonstrative + "que" — "par ce que" is licensed French. This corroborates 96 as the free preposition 'par' at the locus windows too.
- Alternatives killed:
  - **96-43 = "parce" (one word):** "parce" never stands bare in French (always "parce que"); here the follower is 87='ce' (granted), not 46='que'. Kill-grade dead.
  - **96-43-87 = "parce que" (87='que'):** contradicts the standing 87='ce' grant — §5-barred at battery level. Dead.
  - **96 + 43=verb stem:** "par" + finite/bare verb stem is ungrammatical; no license. Dead.
- **Result:** 96's role is fixed as 'par' by the A15 grant plus the distributional corroboration. The windows' hostility is entirely 43-driven (43's noun line is kill-terminal; its verb/adjective lines were already closed by the noun-43 discriminator line). Nothing about 96 needs adjudication.

## Per-clause results

- **C1: PASS** — discriminating frame produced: 87's scope is follower-determined and window-divergent (W2 bound "ceci" via the @1029 promote; W1 free "ce" + 06-residual); leftward resegmentation fenced.
- **C2: PASS** — '43 87' unit fenced as unlicensed (not kill-grade; 43 valueless).
- **C3: PASS** — 96 fixed as 'par'; all alternatives dead; hostility localized to 43.

## Verdict: NULL (docket-input grade)

The bar's deliverable — discriminating frames for the red-team docket — is produced. No promote/kill claim was named by the bar, and none is warranted: C1's divergence, C2's fence, and C3's localization are inputs to the already-queued red-team 43 docket (`redteam-43-polyvalence`, `noun43-redteam-escalate`), not battery-grade verdicts. No standing/red-team verdict contradicted or downgraded; §7 intact; canonical-stream caveat stands (rows a2_05/a6_03 offsets unvalidated).

## Adverses

None listed. Adopted without re-litigation: ce-frame-45-64-96-43-87-01 (NULL), par43-adverbial-attestation (PROMOTE), ci-01-value (KILL), ci-bound-01 (NULL), residual-1029-infinitive (PROMOTE).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `par43-suite-adverbial` (P3) — Littré/TLF attestation test for bare "par suite" as a sentential adverbial ("consequently") in 1841 French. Gap found: `par43-adverbial-attestation` tested only "par mesure"/"par condition"; "suite" is the one noun-43 candidate the ce-frame battery found grammatical after "par", and its bare-adverbial shape was never attested or killed. Bars: (a) bare "par suite" adverbial attested in Littré/TLF with the needed shape; (b) if unattested, the "par suite" escape closes with stated cause.
2. `scope-87-follower-census` (P3) — test whether 87's scope (free 'ce' vs bound "ceci") correlates with follower class across all 32 87-windows. Bars: (a) full 87 follower census with scope assignment per window; (b) state whether the W1/W2 divergence generalizes or is locus-bound; (c) fence with stated cause if the correlation is untestable.
3. `w1-342-tail-parse` (P3) — full-context parse of W1's tail "87 01 06 70 12 94 74 67 78" (0b@344–352). Bars: (a) produce a grammatical parse with <=1 unstated assumption, or (b) fence W1's 87-scope as a 06-driven residual with stated cause; coordinate with (do not re-litigate) the killed 06 "entreprenne" leg and ci-bound-01's @345 fence.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-par43-ce-scope.md` (this file).
- Queue: `par43-ce-scope` queued → verdict/null via temp-file + rename, own entry only; pre-write assert confirmed no prior verdict; JSON re-validated post-write.
- Lock `code/crowd17/next-token/locks/par43-ce-scope.lock`: created on start, deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
