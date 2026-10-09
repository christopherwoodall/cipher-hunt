# Battery report: reseg-690-leftedge

- Target id: `reseg-690-leftedge`
- Claim: Test leftward fusions @687-689 ('[65]94' one word; '94 29' = 'ner'-shaped) as the only segmentation routes dit-60-syncretic's audit did not exhaust; kill iff every fusion strands 'er' or contradicts banked 29='er'.
- Date: 2026-10-09
- Worker: battery worker (subagent 29e643be-6af3-457f-be5b-a2d0680001d9)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; 1,847 pairs / 96 types re-derived in-session, asserts held). `canonical.py` never used. R5005, sealed gate instances, and the red-team adjudication queue untouched.
- Lock: `code/crowd17/next-token/locks/reseg-690-leftedge.lock` created on start (agent id + UTC timestamp); no prior/stale lock; deleted on completion.

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"test leftward fusions @687-689 ('[65]94' one word; '94 29' = 'ner'-shaped) as the only segmentation routes dit-60-syncretic's audit did not exhaust; kill iff every fusion strands 'er' or contradicts banked 29='er'"

Numbered pass/fail clauses (fixed before data examination):

- **C1:** Route 1 ('[65]94' as one word, @687-688) is tested; it fails at kill grade iff it strands 'er' or contradicts banked 29='er'.
- **C2:** Route 2 ('94 29' fused as 'ner'-shaped, @688-689) is tested; it fails at kill grade iff it strands 'er' or contradicts banked 29='er'.
- **C3:** KILL iff C1 and C2 both fail at kill grade (no fusion rescues the window). Otherwise the surviving route is recorded and the segmentation space stays open.

Adverses (from brief, answered not ignored): expected negative outcome — '[65]94' fusion dissolves 'ne' but strands 'er [60]'; '94 29' fused ('ner[V]') is not a French word; this closes only the segmentation space at @690.

## Method

1. Read BATTERY-PROTOCOL.md first; created/deleted the lock per §6.
2. Re-derived the repaired stream byte-exact in-session (1,847 pairs / 96 types asserted).
3. Ran bigram censuses for "65 94" and "94 29", plus contact profiles for 65, 94, 29.
4. Tested each fusion route against standing values (§7): banked 29='er' (pencil GT), 65 noun-class (prof-65 / R18), 94='ne' battery-promoted pending ratification (ne-94-right-context), 03 verb-stem promoted, 60 value open (participle avenue dead, verb-class live).
5. Adopted (did not re-litigate): dit-60-syncretic's W2 kill of 60="dit"; ne-94-right-context's promote; the lane's "word-internal iff X is bound" compositional standard (from the 89 word-internal fork kill).

## Window-level evidence (all byte-verified on the repaired stream)

Locus, row a5_00 (@-offsets 0-based):

| @ | group | row |
|---|-------|-----|
| 684 | 64 (qui, granted) | a5_00 |
| 685 | 29 (er, banked) | a5_00 |
| 686 | 40 (e, banked) | a5_00 |
| 687 | 65 (noun-class, value open) | a5_00 |
| 688 | 94 (ne, battery-promoted) | a5_00 |
| 689 | 29 (er, banked) | a5_00 |
| 690 | 60 (value open) | a5_00 |
| 691 | 03 (verb stem, promoted) | a5_00 |
| 692 | 39 (open) | a5_00 |

Distributional facts (re-derived):

- "65 94" bigram: exactly **2x** stream-wide (@687, @1712). The locus is not unique.
- "94 29" bigram: exactly **1x** stream-wide (@688, the locus — hapax).
- "29 60" bigram: exactly **1x** stream-wide (@689-690, the locus — hapax). The right edge is unique.
- 65: n=25; noun-class; 12 distinct predecessors, 13 distinct followers — free-word signature; value open.
- 94: n=37; 9 distinct predecessors (62x9 top), 13 distinct followers — free-word signature; 'ne' battery-promoted (7 clean verbal-negator windows), pending ratification.
- 29: n=45; 'er' banked pencil GT; followers 40x9 ("ere" frame), 89x5, 47x4, 80x4, ... 60x1 (locus only).
- Second "65 94" window (@1712-1713, row a8_06): `29 40 | 65 94 | 44 59 30 64 47` = "er e [65] [94] [44] est[59] pas[30] qui[64] ce[47]". No composition license for "[65]94" here either (65 value open, 44 open).

## Route 1: '[65]94' as one word (@687-688)

- The fusion requires 94 bound word-finally to 65. 94 is a free word (n=37, free-combining profile; 7 clean 'ne' windows). Under the lane's "word-internal iff X is bound" standard there is no license for bound 94, and 65's open value supplies no composition evidence for a "[65]ne" French word. The fusion is unlicensed at both "65 94" windows.
- After fusion the window reads "[65-word] | er | [60] | [03]". Banked 29='er' as infinitive ending has no stem (the fused word is noun-class; a noun cannot host a verbal infinitive ending), and standalone "er" is not a French word. **'er' is stranded.**
- The only alternative (29 fusing rightward into "er"+60) abandons 29's banked independent-'er' status.
- **C1: kill clause fires** — the fusion strands 'er' (and the rightward rescue contradicts banked 29='er').

## Route 2: '94 29' fused as 'ner'-shaped (@688-689)

- "ner" is not a standalone French word (no such word exists; longer "ner-" words like "nerf"/"nerveux"/"nervure" do not license the bare stem).
- As a word-initial fragment ("ner..."), it would need composition with 60; 60's value is open and no positive license exists for 94 as a bound word-initial element. The "ner"-shaped fusion requires 94='n', inconsistent with the battery-promoted 94='ne' lead (noted, not downgraded per §5).
- Since "ner" cannot be a word, the fusion is impossible; 29 must remain the independent banked 'er', which stands stranded in this window (no stem; cf. dit-60-syncretic's "NO rescue exists under any 94 value").
- **C2: kill clause fires** — the fusion cannot rescue 'er'; banked 29='er' stands as the immovable obstacle and the absorbing fusion is forced false.

## Per-clause results

- **C1: PASS** (route 1 dead at kill grade — strands 'er').
- **C2: PASS** (route 2 dead — "ner" is not a French word; no composition license; no rescue).
- **C3: FIRES** — both fusions fail; no re-segmentation rescues the window.

## Verdict: KILL

Both leftward fusion routes are dead value-independently (not only under 60="dit"). The segmentation space at @690 is closed: dit-60-syncretic's W2 re-segmentation audit is confirmed complete. Scope is strictly the @687-690 segmentation space; this does not touch other 60 windows, the poly-60 question (poly-60-redteam), or any standing value. No standing or red-team verdict contradicted or downgraded; §7 intact.

## Adverses answered

The brief's expected negative outcome is confirmed: '[65]94' fusion dissolves 'ne' but strands 'er [60]'; '94 29' as 'ner' is not a French word. The closure is fenced to the @690 segmentation space only.

## Supervisor observations (not findings; kills regenerate no follow-ups per §4)

1. The "29 60" bigram is a stream hapax (@689-690); the locus's right edge has zero repetition leverage anywhere.
2. The second "65 94" (@1712) independently confirms route 1 has no composition license at either window.
3. The @690 window remains a fenced residual for any future 60-value candidacy: any 60 value must survive the "94 29 60" = "ne er [60]" left edge with banked 29='er' immovable.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-reseg-690-leftedge.md` (this file).
- Queue: `battery-queue.json` `reseg-690-leftedge` queued → verdict/kill (own entry only, temp-file + rename; pre-write assert confirmed no prior verdict; JSON re-validated).
- Lock: `locks/reseg-690-leftedge.lock` created on start, deleted on completion.
- R5005, sealed gate instances, and the red-team adjudication queue untouched throughout.
