# Battery verdict: seg-1772-wordbound

- Target: `seg-1772-wordbound` (battery-queue.json, priority 3, status queued)
- Claim: Test the word boundary at @1771-1772 under standing values: '37 78' | '62 94...' vs the bar's assumed 'le [62]ne' contact; standing parse favors '[62] ne [24-modal]' with no '[62]ne' word present at this window.
- Adverses: 78='ver' LEAD stands; do not assume 78='le'.

## Bar (verbatim, numbered)

"**name the boundary with stated values at battery grade; kill the 'le [62]ne' reading at this window iff the boundary is incompatible**"

- **C1.** Name the boundary with stated values at battery grade.
- **C2.** Kill the 'le [62]ne' reading at this window iff the boundary is incompatible.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/seg-1772-wordbound.lock` on start (agent cf9fa7fe-9c09-494f-896a-bed3f8bcc5ee, 2026-10-09T20:34:00Z); deleted on completion.
2. Re-derived the repaired stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` via `repair_parse.py`: 1,847 pairs, 96 types. `canonical.py` never used.
3. Byte-confirmed the locus (0-based): @1770=37 (a8_08), @1771=78 (a8_09), @1772=62, @1773=94, @1774=24, @1775=87, @1776=64, @1777=59, @1778=19, @1779=48. Row boundary a8_08/a8_09 sits between @1770 and @1771.
4. Distributional checks on the stream: '78 62' bigram exactly 2x (@1140, @1771); '37 78' bigram 4x (@312, @414, @475, @1770); '62 94' bigram 9x. n(78)=31, n(62)=35, n(94)=37.
5. Read the parent report `code/crowd17/report_inbox/processed/battery-det-62ne-1772-select.md` (NULL): its bar was untestable as written because its load-bearing premise (78="le" at @1771) contradicts the standing R16-005 LEAD. This battery is the narrower successor that tests only what standing values license.

## Standing values used (all stated, no new assumptions)

- 78='ver' LEAD (R16-005, red-team venue; battery does not re-litigate it).
- 94='ne' STRONG LEAD, standalone negator particle (R17-001).
- 62: 'il' KILLED at kill grade (R19-106, confirmed R20-125); value otherwise open.
- 87='ce' (granted), 64='qui' (granted), 59='est' (provisional), 48='e' letter tier (R17-002/003, R20-008).
- 37 = A1 predicative-frame cell (value open); 24 = verb-class (R17-009, value contested at red team).

## Findings

### C1 — boundary named: PASS

Named boundary at battery grade: **@1771 | @1772 | @1773** — i.e., `78 | 62 | 94`:

1. **62 | 94 is forced by the STRONG LEAD.** 94='ne' (R17-001) is a standalone negator particle. It cannot be consumed word-internally inside a "[62]ne" word without a §7 declaration the battery cannot make. The 9 stream-wide '62 94' windows parse as "[62-word] ne [24...]" — 94 stands alone. Boundary named with a standing grant, zero new assumptions.
2. **78 | 62 under the 'ver' LEAD.** @1771=78 sits under the standing R16-005 LEAD ('ver'), not 'le' — the adverse explicitly bars assuming 78='le', and this battery does not assume it. No byte evidence licenses a 78-62 word under standing values: the other '78 62' window (@1140, "...98 00 98 | 78 62 16 29 42...") shows the same standalone-78 contact, and 62's value is open ('il' killed), so no "verX" composition is statable. The '37 78' bigram (4x) sits in the A1 predicative cell's left edge and carries no word-unit license either.
3. The full locus under standing values: `...[37] [78-ver] | [62] | ne | [24-verb] ce qui est...` — a clean left-to-right segmentation with every stated value banked.

### C2 — 'le [62]ne' reading at @1771-1773: KILLED

The rival reading requires two premises; both are forced false by standing grants at battery grade:

1. **The 'le' arm dies on the adverse.** 'le [62]ne' needs 78='le' at @1771. The standing R16-005 LEAD (78='ver') is the red-team's ruling; the adverse bars assuming 78='le'. No battery path opens it. Forced false at this window.
2. **The '[62]ne' word arm dies on the STRONG LEAD.** Fusing 62-94 into a "[62]ne" word consumes 94 word-internally, contradicting 94='ne' STRONG LEAD's standalone-particle status (R17-001). No §7 declaration exists to license the consumption. Forced false at this window.

Both arms fail independently, so the reading is incompatible with the named boundary → killed at this window. This does not touch the LEAD, the STRONG LEAD, or any red-team verdict — it complies with them.

### Adverse answered

78='ver' LEAD stands untouched; 78='le' was never assumed. The parent's NULL (bar untestable under the LEAD) is not contradicted — this battery tested the narrower, standing-compliant question.

## Verdict: PROMOTE

C1 passes (boundary named with stated values at battery grade); C2 passes (rival killed — incompatible with the named boundary); the adverse is answered. The standing parse is `37 78 | 62 | ne | 24...` with no '[62]ne' word present at this window.

## Scope

- Locus-level only: @1770–1773. Names no value, declares no split, grants no class.
- 62's value, 37's value, 24's value, 78's 'ver' LEAD grading, §7 all untouched.
- No standing or red-team verdict contradicted, downgraded, or re-litigated. Canonical-stream caveat stands (row a8_08/a8_09 boundary offsets unvalidated).
- No follow-ups (promote, not null).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-seg-1772-wordbound.md`
- Queue: `seg-1772-wordbound` queued → `verdict`/`promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.seg-1772-wordbound.tmp` + rename; disk re-validated; own entry only; no downgrade)
- Lock `locks/seg-1772-wordbound.lock`: created on start, deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
