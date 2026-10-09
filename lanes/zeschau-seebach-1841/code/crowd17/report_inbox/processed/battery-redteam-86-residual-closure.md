# Battery report: redteam-86-residual-closure — gather-only red-team closure package for the 86 split docket

- Target id: `redteam-86-residual-closure`
- Claim: "Package this report's 10-window fence inventory as red-team closure input for the 86 split docket (redteam-86-split-docket already queued). Battery gathers; red team decides"
- Date: 2026-10-09
- Worker: battery worker (subagent 82807f1e-3aa0-4f2e-bba8-4db6632f95bf)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session; offsets re-verified below). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.

Terms (ASD-STE100): "gather-only" = this report packages evidence; it makes no ruling, declares no split, names no value, and overturns nothing. "Fence" = a window is fenced when no value hypothesis can be positively licensed there, with the stated cause. "D-window" = 86 windows from the det-86-dlife-partition census (86's 26 of 32 windows in that census's scope; 32 total confirmed in-session).

## Bar (verbatim, pre-registered before testing)

"Gather-only: deliver the package; no adjudication"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** the 10-window fence inventory is packaged with byte-verified offsets, window-level causes, and provenance — PASS.
2. **C2:** no adjudication — no value named, no split declared, no standing or red-team verdict contradicted, downgraded, or re-litigated — PASS.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/redteam-86-residual-closure.lock` on start (agent id + 2026-10-09T18:50:00Z); no prior/stale lock; deleted on completion.
2. Read the source report in full (`code/crowd17/report_inbox/processed/battery-residual-86-finer.md`, verdict NULL 2026-10-09).
3. Re-derived the repaired stream byte-exact in-session: n(86)=32 confirmed; all 10 reported offsets re-verified as 86-windows; ±4 contexts match the source report exactly (see §"Independent byte verification").
4. Read the related lane record for the package (no re-litigation): `det-86-dlife-partition` (PROMOTE), `split-86-amended-rule` (PROMOTE), `homophone-86-split` (NULL), `ce86-le86-parity` (PROMOTE), `val-86-1391` (NULL), `fem-noun-86-frames` (PROMOTE), and the R20-123 ruling on `redteam-86-split-docket`.
5. Copied evidence values verbatim; all numbers trace to lane files or the stream.

## Independent byte verification (this session)

Re-derived contexts (0-based offsets, ±4), all matching the source report:

| Offset | Context (±4) |
|---|---|
| @728 | 65 64 11 00 86 48 88 11 24 |
| @867 | 48 47 46 00 86 70 87 77 89 |
| @899 | 82 14 98 83 86 16 92 67 16 |
| @1335 | 70 52 39 83 86 71 64 60 08 |
| @300 | 11 78 40 97 86 91 18 89 88 |
| @716 | 12 63 00 66 86 01 02 21 80 |
| @1131 | 00 86 52 37 86 24 77 86 20 |
| @1147 | 29 42 98 98 86 67 33 66 84 |
| @557 | 86 59 34 17 86 94 59 30 67 |
| @1739 | 60 12 48 52 86 12 34 94 82 |

## The 10-window fence inventory (source: residual-86-finer, verbatim claims)

Subset A — 00-left defective-left family (×2). @728: "65 64 11 00 [86] 48 88 11 24" = "…qui la pour [86] 48 88 la 24"; 11=la (pencil), 00=pour (granted). "la pour" ungrammatical under pencil+granted values under EVERY 86 value — orthogonal granted-defect, discriminating nothing about 86. @867: "48 47 46 00 [86] 70 87 77 89" = "…ce que pour [86] pre ce le"; 46=que (pencil GT), 00=pour (granted). "que pour" ungrammatical under granted values under every 86 value. Common cause: left-frame defect independent of 86's value.

Subset B — 83-left pair (×2). @899: "82 14 98 83 [86] 16 92 67" = "m [14] vient [83] [86] 16 92 et/veut". @1335: "70 52 39 83 [86] 71 64 60" = "pre 52 39 [83] [86] 71 qui 60". Frame "83 [86]" ×2, frame-consistent. Per syll-83-de-1829 (NULL): the verb fork is fenced at kill grade; the NOUN fork stays live ("[38]de" as noun subject). With 83 a live noun-shape, "de [86]" forces no 86 value: 86='le' → no contradiction; 86=noun → no contradiction; neither parses with positive force. Cause: 83's value open.

Subset C — confirmed orphans, adopted kill-grade resolution failures (×4). @300: orphan86-300 KILL — resolution via 97's or 78's class refuted at kill grade; orphan CONFIRMED. @716: orphan86-716 KILL — no 66 class makes "pour [66] [86] [01]" parse with zero contradiction. @1131: orphan86-1131-1147 KILL — failures localize to 86's own slot; "00 86 52 37 [86] 24 77 86" with today's 52 split-shape leaving "52 37 [86]" unresolved. @1147: orphan86-1131-1147 KILL — no stated neighbor assumption yields a zero-contradiction whole-parse. Cause: adopted kill-grade resolution failures; failures localized to 86's slot, not to fenceable neighbors.

Subset D — open-neighbor fences (×2). @557: "86 59 34 17 [86] 94 59 30" = "[86] est(?) i fois [86] ne(?) est(?) pas(?)"; 59=est provisional, 34=i pencil, 17=fois promoted, 94=ne STRONG LEAD (not granted), 30 open. 86='le' → "fois le" needs a clause boundary; absolute construction ("une fois le [N]…") stays grammatical but the noun never materializes (94=ne-lead follows). 86=noun → bare noun after "fois" strained (proper-noun rescue unevidenced). Fenced tension, not kill-grade on standing values. @1739: "60 12 48 52 [86] 12 34 94" = "60 n(?) 48 52 [86] n(?) i ne"; 12=n pencil GT, 34=i, 94=ne-lead; 48/52/60 open. 52's 'plus'/'jamais' tie fenced unbreakable at battery grade (plus-jamais-tiebreak NULL). No standing value constrains 86 here: 'le', noun, and word-internal readings all contradiction-free and all force-free. Cause: fully open neighbors, no discriminating value.

## Related docket record (packaged, not re-litigated)

1. **R20-123: redteam-86-split-docket — FENCE (confirm R19-134).** Declaration conditions for any 86 split/polyvalence/homophone-set declaration: kill-grade byte evidence for two 86 values, OR a positional rule covering the partition. "No declaration-grade evidence (positional split vs polyvalence vs homophone set) has landed." Registry: none. 86=["INF","cls"].
2. **det-86-dlife-partition (PROMOTE):** 86's 26 D-windows partition into frame-consistent subsets (le-life / det-left / 77-adjacent / Subset 4 = this residual 10). The 86='le' and 86=noun hypotheses were tested across all 10 by its §4a/4b → NULL.
3. **split-86-amended-rule (PROMOTE, battery level):** amended positional rule exceptionless over all 32 windows with byte-level fence causes for non-conforming windows. Caveat: declaring the split is a red-team act under §7; battery escalates only.
4. **homophone-86-split (NULL):** the exceptionless "iff" positional rule is violated by 2/32 windows (both standing re-segmentation adverses). The distributional segregation stands as a live structural signal (30/32 conform, perfect follower mutual exclusivity); killing it would misreport the signal.
5. **ce86-le86-parity (PROMOTE, 2026-10-09):** ce-pair (@175/@1345) and le-quadruple (@799/@878/@951/@1134) are parity-compatible as ONE masculine-value hypothesis for `masc-noun-86-name` (86's value stays unnamed; noun-86-dlife KILL stands; conditional on provisional 77="le" surviving).
6. **val-86-1391 (NULL, 2026-10-09):** no stem value reaches ≥2 legs; battery-grade tier result — "[86]er" is a spelled -er infinitive (stem 86 + 'er'), so the 89 slot at @1391 can only be licensed infinitive-shaped, never by a lexical noun. The stem/det split declaration is red-team venue.
7. **fem-noun-86-frames (PROMOTE, 2026-10-09):** two distinct frames (determinative, subject licensing) parse with 86 as a feminine noun at @671. Class-level only — no feminine noun value named. Conditional on the red-team 24 docket.
8. **clitic-86-77-windows KILL** (pre-R19, consistent with the R20-123 package): 86=object-clitic dead at @951 on granted 96='par'.
9. **det-86-dlife-value / noun-86-dlife / noun-86-dlife-name (KILL):** 86's value unnamed; noun-dlife value killed.
10. **Queued (not yet run):** `masc-noun-86-name` (P3), `residual-86-83pair` (P4, gated on 83's value), `residual-86-557-fois` (P4, gated on 59/94/30 landing), `val-86-728-entr` (P3).

## What the red team is asked to decide (no battery adjudication)

- Whether the residual-10 fence inventory, together with the packaged segregation signals (homophone-86-split NULL, split-86-amended-rule battery PROMOTE), meets R20-123's declaration conditions: kill-grade byte evidence for two 86 values, or a positional rule covering the partition.
- The clitic-vs-noun adjudication the parent suggested for @1131/@1147 awaits 24's class / 67's positional ratification — red-team venue, recorded here, not acted on.
- The @300 orphan confirmation stands against re-opening by today's 52/76/08 verdicts (window-orthogonal; recorded per window).

## Per-clause pass/fail

1. C1 (package delivered): PASS. 10/10 windows packaged with byte-verified offsets, fence causes, and provenance to the source report and related battery verdicts.
2. C2 (no adjudication): PASS. No value named; no split declared; no standing or red-team verdict contradicted, downgraded, or re-litigated; §7 intact (no second polyvalence named).

## Verdict: NULL (gather-only; per precedent, gather-only/fence bars resolve to NULL)

## Follow-ups (null regenerates work; all verified ABSENT from battery-queue.json)

1. `redteam-86-inventory-refresh` (P4, gather-only): re-package the full 86-window accounting (n=32) for the next red-team round once the queued 86 items land (`masc-noun-86-name`, `residual-86-83pair`, `residual-86-557-fois`, `val-86-728-entr`); merge with this package rather than duplicating it.
2. `val-86-dwindows-ledger` (P4): ledger the remaining D-windows' per-subset values under the current package so a future declaration can cite byte-level sub-subset membership.

## Bookkeeping

- Queue entry `redteam-86-residual-closure` was queued/verdictless with no lock at take (pre-write assert passed); updated to `status: verdict`, `verdict: {"result": "null", "report": "code/crowd17/report_inbox/battery-redteam-86-residual-closure.md", "date": "2026-10-09"}` via temp-file + rename; own entry only; no downgrade; disk re-validated (1,508 targets).
- Lock `code/crowd17/next-token/locks/redteam-86-residual-closure.lock` created on start, deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched. No standing/red-team verdict contradicted or downgraded.
