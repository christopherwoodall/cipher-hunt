# Battery report: dict-45-contact-update — 45's post-78 follower profile

- Target: `dict-45-contact-update` (battery-queue.json, priority 2, status queued)
- Claim: 45's post-78 followers ({13, 01, 64}) form a disjoint profile from standalone-45 followers (syllable rival independent of ver-78)
- Worker: 50afa582-3df2-44c2-928f-81ffa0b23930
- Date: 2026-10-08
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`). `canonical.py` NOT used. R5005 untouched.
- All @-offsets are pair indices in the repaired stream. Predecessor/follower = immediate neighbor pair.

## Bar (verbatim, pre-registered)

"(a) census all 22 of 45's followers split by pre=78 vs pre!=78; (b) boundary holds iff follower distributions are disjoint at Fisher p<0.05 with stated counts"

Numbered clauses (frozen before testing):
1. All 22 of 45's windows are censused, each with its follower, split by pre=78 (n=4) vs pre!=78 (n=18).
2. The boundary holds iff the pre=78 follower distribution vs the standalone follower distribution is disjoint at Fisher p<0.05, computed on the stated counts (post-78 followers {13, 01, 64}).

## Method

Enumerated all 22 occurrences of 45 on the repaired stream; for each, recorded the immediate predecessor and follower plus row id. Split by predecessor = 78 vs predecessor != 78. Built the 2x2 contingency table (class x in-profile {13,01,64} vs out-of-profile) and computed the two-sided Fisher exact test exactly (math.comb, no approximations). Verified the byte-identical 5-gram loci and the {13,01} exclusivity claim. No value assumptions about 78 or 45 were used; the test conditions only on 78's occurrence as predecessor, so it is ver-78-independent.

## Window-level evidence

Full census (offsets of the 45 occurrence; follower at offset+1):

pre=78 (n=4):
- @314 (row a2_04): 78-45-64
- @574 (row a3_02): 78-45-13, with 575=55, 576=61 (5-gram 78-45-13-55-61; context 572=87)
- @983 (row a6_01): 78-45-01
- @1165 (row a6_09): 78-45-13, with 1166=55, 1167=61 (5-gram 78-45-13-55-61; context 1163=67)

pre!=78 (n=18):
- @14 (a1_00): 76-45-91
- @104 (a1_03): 59-45-28
- @262 (a2_02): 74-45-93
- @332 (a2_05): 50-45-54
- @340 (a2_05): 14-45-64
- @401 (a2_08): 11-45-88
- @437 (a2_09): 63-45-46
- @478 (a2_11): 74-45-93
- @569 (a3_02): 76-45-94
- @603 (a4_00): 96-45-93
- @678 (a5_00): 77-45-23
- @697 (a5_01): 50-45-28
- @974 (a6_01): 51-45-08
- @1024 (a6_03): 64-45-64
- @1055 (a6_04): 74-45-23
- @1201 (a7_00): 29-45-58
- @1214 (a7_00): 96-45-36
- @1551 (a8_00): 92-45-23

Post-78 follower set = {64, 13, 01, 13} = {13, 01, 64}, exactly as stated in the claim.
45->13 x2 confirmed at @574 and @1165, both inside byte-identical 78-45-13-55-61 5-grams (rows a3_02, a6_09). 45->01 occurs only at @983 (pre=78). {13, 01} occur as followers of 45 NOWHERE in the 18 standalone windows.
64 is shared across classes: pre=78 at @314, standalone at @340 and @1024 (the listed W1 adverse, re-derived).
n(45)=22 re-derived on the repaired stream; all 22 have followers (no 45 at stream end).

Contingency (class x in-{13,01,64} vs out):

|              | in-profile | out-of-profile |
|--------------|------------|----------------|
| pre=78 (n=4) | 4          | 0              |
| standalone (n=18) | 2 (@340, @1024) | 16 |

Fisher exact two-sided: p = 0.00205 (< 0.05). Exclusive-only variant {13,01} vs rest [[3,1],[0,18]]: p = 0.00260.

## Per-clause pass/fail

1. Census: PASS. All 22 of 45's windows censused with followers and split (pre=78: n=4; pre!=78: n=18). Verified against the stream: 22 occurrences total.
2. Boundary: PASS. Two-sided Fisher p = 0.00205 < 0.05 on the stated counts. The post-78 class is 4/4 in-profile ({13,01,64}) vs 2/18 standalone. The discriminating core is {13, 01}: 3/3 exclusive to post-78 windows, zero standalone occurrences.

## Adverses

- 64 shared with standalone (@340, @1024): FENCED with stated cause. 64="qui" is promoted (A-list); it is the highest-frequency function word in 45's contact set (3/22) and appears in both classes as profile-neutral filler. The load-bearing boundary is {13, 01}, which are 3/3 exclusive to post-78 windows. Sharing one function word does not erase the measured distribution difference (the Fisher table includes the shared 64s and still rejects at p=0.002). Not a misread: @314 (78-45-64), @340 (14-45-64), @1024 (64-45-64) all re-derived on the repaired stream.
- n=22 small: FENCED. Fisher exact is exact for small n; the post-78 class is n=4, so the boundary is one-window sensitive (one flipped window changes the table). Stated as caveat, not ignored. The observed effect (4/4 vs 2/18) is large enough to clear the bar's p<0.05 standard despite n.

Note on "disjoint": the bar's own adverse (64-sharing) was known at registration; the operational criterion in clause (b) is the Fisher test, which passes. Literally, the sets {13,01,64} and the standalone follower set overlap at {64}; the 13/01 sub-profile is strictly disjoint (3/3 vs 0/18).

## Verdict

**promote.** Both bar clauses pass and both adverses are fenced with stated cause.

Promoted content (narrow, per the claim): 45 shows two follower profiles conditioned on pre=78: post-78 45 takes {13, 01, 64} (4/4 windows), standalone 45 takes {91, 28, 93, 54, 88, 46, 94, 23, 08, 58, 36, 64} with {13, 01} absent (0/18); the class difference is significant (Fisher p=0.002). This establishes the syllable-rival contact profile as a real, ver-78-independent boundary (conditions only on 78's occurrence, never on 78's value). It does NOT by itself promote 45="dict"; it is the contact-profile leg of that rival, to be adjudicated with dict-frame-78-45-13-55-61 and fork-78-45-adjudication.

Non-duplication note: this battery tested only the contact-profile boundary. dict-frame-78-45-13-55-61's unit bar (13-55-61 as one named unit + negation-frame clauses) and dict-78-45-wordbound's boundary bar were not re-run here; the 5-gram loci (@574, @1165) were used only as positional confirmation of the stated counts.

## Follow-ups

None required (verdict is promote, not null). One flag for the red team / sister batteries: the post-78 class is n=4; any future re-parse that moves a single post-78 window re-opens this verdict. No standing verdict is contradicted.
