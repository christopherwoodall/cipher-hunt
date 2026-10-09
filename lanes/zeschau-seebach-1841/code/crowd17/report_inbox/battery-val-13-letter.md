# Battery verdict: val-13-letter

- Target: `val-13-letter` (battery-queue.json, priority 3, status queued)
- Claim: Name 13's letter content with byte evidence; a named 13 re-opens the @481/@575/@1166 rightward attachment.
- Worker: 78fdd308-779d-462f-b7ad-938d2b3357b9 (battery worker). Date: 2026-10-09.
- Stream: repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs, 96 types). `canonical.py` NEVER used. R5005, sealed gates, red-team adjudication queue untouched.
- Lock: `code/crowd17/next-token/locks/val-13-letter.lock` created on start (no stale lock); deleted on completion.
- All @-offsets are 0-based pair indices in the repaired stream.

## Bar (verbatim, pre-registered from battery-queue.json)

"name 13's letter content iff it parses with byte evidence at >=2 windows with zero kill-grade contradictions"

**Restated as numbered pass/fail clauses (frozen before testing):**
- **C1 (name arm):** some letter L is named as 13's content, parsing with byte evidence at >=2 of 13's 12 windows.
- **C2 (contradiction arm):** zero kill-grade contradictions — no window, and no standing red-team verdict, forces the named letter false.

Queue adverses (answered, not re-litigated): 13='les' killed at kill grade (both arms: determiner by subj-13-value, object pronoun by pronoun-13-les) — neither revived here. 13='que' §7-blocked (46='que' banked) — not touched. 13's gloss open — confirmed open at start of this battery.

## Method

1. Read BATTERY-PROTOCOL.md in full before testing.
2. Re-derived the repaired stream in-session; byte-confirmed all 12 windows of 13 (n(13)=12): @68, @139, @456, @481, @567, @575, @822, @1166, @1360, @1381, @1554, @1684.
3. Tested candidate letters {a, d, e, l, n, r, s, t, y} at every window against standing values only (pencil GT, granted/promoted values, registry classes). Registry standing used: 69=[noun,cls], 76=[noun,prom], 24=[verb,cls] (+R17-009 finite), 93=[verb,cls], 92=[verb,cls], 65=[noun,cls], 35=[noun,cls]; 66/52/99/97/95/14/56/61/55/13 ABSENT.
4. Checked the result against standing red-team verdicts (R19-170/R20-106 armA GRANT, R20-134 split-13 FENCE, letter-13-verdicts KILL ratified R20-134).

## Window-level evidence (byte-confirmed, in-session)

| @ | row | frame (standing values) | 13='y' status |
|---|-----|------------------------|---------------|
| 68 | a1_01 | 69[noun] 13 24[verb-fin] | PARSES: "[NP] y [V-fin]" clean ("les hommes y vont"-shaped). **Collides with armA GRANT (see headline).** |
| 139 | a1_04 | 65[noun] 13 66[open] 14[open] | Conditional on 66 verb-shaped; 66 class contested (red-team venue). Fence, not kill. |
| 456 | a2_10 | 65[noun] 13 66[open] 14[open] | Same as @139. Fence, not kill. |
| 481 | a2_11 | pour 13 52[open] | Leftward close dead (armB KILL: preposition cannot host suffix). "pour y [52]" needs 52 verb (fenced, not standing). Fence, not kill. |
| 567 | a3_02 | 97[open] 13 76[noun-PROM] | 'y' before a promoted noun has no standing license; 97 open so imperative-"y" rescue not forced false. Fence, not kill. |
| 575 | a3_02 | 78 45[ce] 13 55-61[=prend] | Leftward dead (armB KILL); "y" between ce/verdict and granted "prend" unparseable under both 78-45 forks (fork undecided, red-team venue). Fence, not kill. |
| 822 | a5_05 | 95[open] 13 24[verb-fin] | Conditional on 95 nominal. Fence, not kill. |
| 1166 | a6_09 | 78 45[ce] 13 55-61[=prend] | Same as @575. Fence, not kill. |
| 1360 | a7_06 | qui 35[noun] 13 92[verb] | PARSES: "qui [NP] y [V]" clean. Arm-B window; no standing verdict covers it. |
| 1381 | a7_06 | on 92[verb] 69[noun] 13 24[verb-fin] 65[noun] | Local "69 y 24" parses; wider clause needs a boundary (92 finiteness not standing). Consistent, not counted. |
| 1554 | a8_01 | 99[open] 13 93[verb] | Conditional on 99 nominal. Fence, not kill. |
| 1684 | a8_05 | pour que tout 65[noun] 13 93[verb] | PARSES: "tout [NP] y [V]" clean ("tout le monde y va"-shaped). **Collides with armA GRANT (see headline).** |

Other letters swept: 13='a' KILLED globally (@68: "[NP] a [V-fin]" ungrammatical — 'a' is finite, 24 is finite; §7 one-value extends the kill). 13='n' dead (homophone-set {48,94} kill). 13='s' dead (word-final 's' killed, letter-13-verdicts, ratified R20-134; no standalone 's'). 13 in {d, e, l, r, t}: zero parses at battery grade (all compositions need open-neighbor contents). **'y' is the unique surviving letter candidate.**

## Clause results

- **C1: TECHNICALLY MET, SUBSTANTIVELY BLOCKED.** 13='y' parses cleanly at 3 windows (@68, @1360, @1684) with standing values only and zero new assumptions.
- **C2: FAILS — HEADLINE CONTRADICTION.** Two of the three parse windows (@68, @1684) are arm-A windows where reseg-13-armA holds a standing red-team GRANT (R19-170, confirmed R20-106): "13 closes the preceding nominal leftward... 13 is not a word here at all, it is a nominal-closing suffix, and the verb-class successor starts a new clause." The standalone-word 'y' parse ("[NP] y [V]" as ONE clause) is mutually exclusive with the granted segmentation at those windows. Per protocol §5.2, a battery result contradicting a standing red-team verdict is not promoted — it is recorded as NULL with the contradiction as the headline and escalated to the red team.

The armA-consistent alternative — 13='y' as the LETTER CONTENT of armA's nominal-closing suffix (armA explicitly left "the suffix's gloss" open) — has no distinguishing byte evidence: every leftward neighbor (69, 95, 92, 99, 65) is value-open, so no composed "[X]y" word can be stated without inventing data (same underdetermination as value-13-third-arm's third arm). 'y'-as-suffix-gloss is therefore live but unnameable at battery grade.

No standing or red-team verdict was downgraded or re-litigated. R20-134 (split-13-redteam FENCE) is untouched: this battery names no second value and declares no split; its declaration bar (two named values with kill-grade evidence, or armB landing) remains unmet. §7 intact (67 et/veut sole true polyvalence).

## Verdict: NULL

Headline per §5.2: **standalone-13='y' is the unique letter candidate (3 clean parses, all other letters dead or evidenceless), but it collides with the standing armA GRANT at @68/@1684; the armA-consistent 'y'-suffix gloss is underdetermined.** Escalated to the red team as input to the split-13 venue: the red team must decide whether armA's "13 is not a word here at all" holds against the 'y'-word parses, or whether a §7 conditioned split (word-'y' at arm-B windows, suffix at arm-A windows) is declared. Canonical-stream caveat stands.

## Scope

- Names nothing. 13's gloss remains open.
- Untouched: reseg-13-armA GRANT, reseg-13-armB KILL, R20-134 FENCE, letter-13-verdicts KILL, pronoun-13-les KILL, subj-13-value, 66/52/97/99/95 class-open status, §7, R5005, sealed gates, red-team queue.

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `y-suffix-13-gloss` (P4) — test 13='y' specifically as armA's suffix gloss: seek a window where the leftward neighbor's content is independently nameable, giving the composed "[X]y" word positive byte evidence. Currently all leftward neighbors are value-open.
2. `armA-y-adjudicate` (P3, red-team venue) — package the three standalone-'y' parses (@68/@1360/@1684, byte evidence above) against armA's granted suffix segmentation for red-team adjudication: uphold armA's "13 is not a word here at all," or declare the §7 conditioned split (word-'y' arm-B / suffix arm-A).
3. `val-97-567-class` (P4) — name 97's class at @567 (13's hardest window: 'y' before promoted noun 76); a verb-97 or noun-97 discriminates 13's role there and tests the imperative-"y" rescue.

## Bookkeeping

- `battery-queue.json`: `val-13-letter` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.val-13-letter.tmp` + atomic rename; disk re-validated; own entry only; no downgrade; no tmp leftover).
- Lock `locks/val-13-letter.lock`: created on start (no stale lock), deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
