# Battery verdict: val-77-722-det

- Target: `val-77-722-det` (battery-queue.json, priority 3, status queued)
- Claim: determiner-vs-clitic test for 77 at @721 (follower-class census across n(77)=44)
- Worker: 54e399f6-2a45-4fb7-9afb-c03e27656184. Date: 2026-10-09.
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`; asserts held in-session: 1,847 pairs, 96 types). `canonical.py` NOT used. R5005, sealed gates, red-team adjudication queue untouched.
- All @-offsets are 0-based pair indices in the repaired stream.
- Lock: `code/crowd17/next-token/locks/val-77-722-det.lock` created on start (no lock present, no stale lock); deleted on completion.
- Lineage: this target is follow-up #1 of the NULL verdict on `seg-77-03-722` (all three arms fenced at @721–@722; see report). This battery does not re-litigate that fence; it tests the follower census it requested.

## Bar (verbatim, pre-registered)

"name determiner-77 iff follower classes license a determiner reading with zero new assumptions; clitic-77 iff object-pronoun geometry forced; else fence at the locus"

**Restated as numbered pass/fail clauses (frozen before testing):**
1. **C1 (determiner-77):** name determiner-77 iff follower classes license a determiner reading with zero new assumptions.
2. **C2 (clitic-77):** name clitic-77 iff object-pronoun geometry is forced.
3. **C3 (else):** if neither C1 nor C2 passes, fence at the locus (@721–@722).

Standing values used (protocol §7): pencil ground truth (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); promoted/granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce); provisional (59=est, 77="le"); kills hold (incl. 81="prin"); 06='ent' (verb ending, promoted). A15 'l'on' (77-84 x7) is a granted frame.

## Method

1. Read BATTERY-PROTOCOL.md in full before testing.
2. Re-derived the repaired stream in-session (asserts held); census computed over all 44 77-instances on the repaired stream. No invented data; every number traces to the stream.

## Window-level evidence

Locus @721 (row a5_02; @720 on a5_01):
`@719=21 @720=80 | @721=77 | @722=03 @723=91 @724=65 @725=64`
Full @717–@725: `01 02 21 80 77 03 91 65 64`. Predecessor @720=80 is verb-locked (A8). '77 03' is a stream hapax (1/1,847 pair co-occurrences).

Follower-class census, n(77)=44, with @-offsets (77 at offset, follower at offset+1):

- 84 x7: @145, @259, @1057, @1446, @1484, @1763, @1802 (=on, subject pronoun; 77-84 = 'l'on' per granted A15)
- 78 x7: @7, @213, @647, @1077, @1180, @1351, @1542 ('ver' LEAD, unsettled per R16-005)
- 86 x5: @430, @798, @877, @950, @1133 (INF-class, A9 class-level grant)
- 81 x4: @744, @1240, @1401, @1598 ('prin' killed; class unknown)
- 76 x3: @832, @891, @968 (class unknown)
- 44 x2: @207, @1678
- 89 x2: @639, @870 (verb-frame, A8; @870 sits inside the granted 'ce le [verb]' frame)
- 82 x2: @1041, @1158 (=m, pencil letter)
- 80 x1: @516 (verb-locked, A8)
- 06 x1: @521 ('ent' verb ending, promoted)
- 11 x1: @1033 (=la, pencil)
- 45 x1: @677 (=ce, promoted A4)
- 64 x1: @790 (=qui, granted)
- 87 x1: @612 (=ce, granted)
- 03 x1: @721 (the hapax locus)
- 60 x1: @453; 62 x1: @507; 66 x1: @87; 74 x1: @1306; 83 x1: @1216 (all class-open)

Class roll-up: verb-class followers 9/44 (86x5, 80x1, 89x2, 06x1); pronoun/particle followers 13/44 (84x7, 44x2, 11x1, 45x1, 64x1, 87x1); nominal-class followers 0/44 (none of the settled nominal classes {17, 20, 26, 32, 37, 42, 65, 68, 09, 92} follows 77 anywhere); class-open 22/44.

## Clause results

- **C1 (determiner-77): FAIL.** Zero of 44 followers sit in any settled nominal class — the census does not license a determiner reading. The heaviest followers actively resist it: 84 x7 is the granted 'l'on' formula (subject pronoun, not noun), 86 x5 is INF-class (verbal), 82 x2 is the pencil letter m, and the pronoun followers (11=la, 44x2, 87=ce, 64=qui, 45=ce) are not noun-shaped. Licensing determiner-77 would require new assumptions — e.g. that 76/78/81 (14/44 combined) are nominal (78='ver' is an unsettled LEAD, 81's class is unknown, 76's class is unknown), or that 03 is nominal at @722 (R20 deferred the 03/71 split; `val-03-noun` and `val-03-value-census` are queued and undecided). None of those assumptions is available at zero cost. Not forced false either: no window kills 77='le' wholesale (the provisional stands).
- **C2 (clitic-77): FAIL.** Object-pronoun geometry is not forced. Only 9/44 followers are verb-class (86x5, 80x1, 89x2, 06x1); 35/44 are not. The granted 77-84='l'on' x7 (A15) is a settled alternative geometry for 77 in which 77 is NOT an object clitic (subject pronoun 'on' follows; elision, not object-pronoun position) — a single standing alternative defeats "forced". The pronoun followers (44x2, 11, 87, 64) also resist a uniform object-pronoun reading. The two '77 89' windows (@639, @870, the latter inside the granted A8 'ce le [verb]' frame) are clitic-compatible legs but compatibility is not force.
- **C3: FIRES.** Fence at the locus @721–@722: determiner-77 is unlicensed by the census, clitic-77 is unforced by it. The fence is locus-scoped: it says nothing about 77's class stream-wide, about 78/76/81/03 classes, or about the queued 03 batteries. It is consistent with (and reinforces) `seg-77-03-722`'s all-three-arms fence at this locus.

## Adverses

- 77='le' provisional: stands, untouched. Both candidate readings were compatible with the provisional phoneme value; the fence needs no change to it.
- '77 03' hapax: confirmed 1/1,847 pair co-occurrence at @721–@722. Fenced per C3 with the stated cause (03's class is open at battery grade; R20 deferred the 03/71 split). The venue for un-fencing is the queued `val-03-noun` / `val-03-value-census` verdicts, not this battery.

## Verdict: NULL (fence executed)

No standing or red-team verdict contradicted, downgraded, or re-litigated; §7 intact. The parent report's "follower distribution does not discriminate" is sharpened: the census actively unlicenses determiner-77 (0/44 nominal) while failing to force clitic-77 (9/44 verbal, granted 'l'on' alternative standing).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `objpron-77-89` (P3) — discriminating clitic-77 frame. The two '77 89' windows (@639, @870; @870 inside the granted A8 'ce le [verb]' frame) are the strongest clitic-compatible legs. Bar: name clitic-77 iff both windows parse as [clitic le]+[verb] with 89's verb reading held and no determiner/word-internal rival survives at either window; else fence the clitic arm at @639/@870.
2. `det-77-86-substantivized` (P3) — determiner-77's last stand. '77 86' x5 (@430, @798, @877, @950, @1133); 86 is INF-class, and `stem-86` evidence shows substantivized-infinitive 86 ('le pouvoir'-shaped), which a determiner could govern. Bar: revive determiner-77 iff 86's stems substantivize with zero new assumptions in >=3 of the 5 windows; if the bar fails, determiner-77 is closed at battery grade and the fence becomes a kill.
3. `locus-721-rerun` (P4, gated on `val-03-noun` + `val-03-value-census` verdicts) — re-run the @721–@722 fence once 03's class is settled; consumes this report's locus fence. If 03 is nominal, arms A/B of `seg-77-03-722` reopen with this census as the 77-side input.

## Bookkeeping

- `battery-queue.json`: `val-77-722-det` queued → verdict/null (temp-file + rename, own entry only; pre-write assert confirmed no prior verdict; JSON re-validated from disk; no downgrade; no other entries touched).
- Lock `locks/val-77-722-det.lock`: created on start, deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched. No invented data.
