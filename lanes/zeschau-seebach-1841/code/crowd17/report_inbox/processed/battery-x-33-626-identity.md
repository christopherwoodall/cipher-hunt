# Battery report: x-33-626-identity (same-X vs two-X for the two byte-identical `33-29-87` windows)

- Worker: ba5d5d1b-e9ac-4e71-ace2-ddf00412b997
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed like code/side-keyhunt/repair_parse.py). Never used canonical.py. Never touched R5005.
- Lock: crowd17/next-token/locks/x-33-626-identity.lock created 2026-10-09T07:53:51Z, no pre-existing fresh lock.

## Bar (verbatim from battery-queue.json)

"same-X demonstrated iff both windows' stems share valency class with <=10% orphan, else two-X recorded."

## Bar restated as numbered pass/fail clauses (pre-registered before valency assignment)

- C1: The X stem at @626 (`33-29-87`, pre=37) and the X stem at @1424 (`33-29-87`, pre=67) take a direct complement of the same class (87 = 'ce', promoted A4 allophone tier) at both windows. PASS iff both stems are transitive with the identical pronoun-DO complement class.
- C2: Orphan scan over all five `33-29` stem windows on the repaired stream (@273, @626, @1232, @1424, @1477): count windows where X's valency class differs from the shared transitive/complement-taking class (e.g. intransitive use, que-taking). Orphan rate = orphans / 5. PASS iff <= 10% (i.e. 0 orphans of 5).
- C3: No stem window forces a valency class incompatible with a single causative -er X (the profile recorded by x-33-laisser-test: causative -er family, 'laisser' at LEAD strength). PASS iff 0 such windows.

## Method

1. Loaded the repaired stream: 1,847 pairs confirmed.
2. Located the two byte-identical `33-29-87` windows: @626 (row a4_01, extended `59-37-33-29-87-78-67-08`, pre=37) and @1424 (row a7_08, extended `21-67-33-29-87-63-91-61`, pre=67).
3. Left-context class comparison per the claim: @1424's pre=67 resolves to 'veut' under the §7 sole-polyvalence rule (follower 33-29 is infinitive-shaped, so 67 = 'veut', volitional, licenses a bare infinitive complement). @626's pre=37 is the A1-granted predicative frame (value open); the 37-33 adjacency at @625-626 is a hapax (37 n=28 on the stream; this is its only 33-follower).
4. Enumerated all five `33-29` stem windows with their complements (valency-relevant right context):
   - @273: `67-33-29-89-84` — X takes complement 89 (89's value open; verb-frame class per A8) → complement-taking, transitive-shaped.
   - @626: `37-33-29-87` — X takes 87 = 'ce' (promoted) → transitive, pronoun DO.
   - @1232: `47-33-29-85` — X takes complement 85 (verb-stem frame, A3 granted; value open) → complement-taking, causative-compatible.
   - @1424: `67-33-29-87` — X takes 87 = 'ce' → transitive, pronoun DO. Byte-identical window to @626.
   - @1477: `67-33-29-82-16` — X takes 82 = 'm' (banked clitic) + 16 → transitive, clitic DO.
5. Checked for a second valency class anywhere in the stem census: no stem window is complement-less (intransitive), none takes 46 = 'que', none forces a nominal-only reading.

## Window-level evidence

| window | left context class | stem complement | valency class |
|---|---|---|---|
| @273 | 67 = 'veut' (volitional) | 89 (open, verb-frame) | transitive, complement-taking |
| @626 | 37 predicative (A1 frame; 37-33 hapax) | 87 = 'ce' (promoted) | transitive, pronoun DO |
| @1232 | 47 (open) | 85 (verb-stem frame, A3) | transitive, complement-taking (causative-compatible) |
| @1424 | 67 = 'veut' (volitional) | 87 = 'ce' (promoted) | transitive, pronoun DO |
| @1477 | 67 = 'veut' (volitional) | 82 = 'm' + 16 (clitic) | transitive, clitic DO |

## Per-clause verdict

- C1: PASS. Both crux windows' stems take the identical complement class: 87 = 'ce' as direct object. Same valency class at the two byte-identical windows.
- C2: PASS. Orphan rate 0/5 = 0% <= 10%. All five stem windows show X taking a direct complement; none exhibits a different valency class.
- C3: PASS. Zero stem windows force an incompatible valency class. The @273 (89) and @1232 (85) complements are of open value but both are complement-taking positions consistent with the single causative -er X profile; neither forces intransitive, que-taking, or a second verb.

## Verdict: PROMOTE (same-X demonstrated)

The two byte-identical `33-29-87` windows share one X. The left-context classes differ (predicative 37 vs volitional 'veut' 67), but the stems' valency classes are identical (transitive, 'ce'-DO), and the full five-window stem census shows a single valency class with 0% orphan. Adverses: none recorded — nothing to answer.

Downstream consequence: the boundary route at @627 is unblocked on the X side — the 33 at @627 is the same stem X as the other four stem windows. The remaining blocker is 37-side, not X-side: the 37-33 hapax at @625-626 (how a predicative-frame 37 licenses a following bare infinitive) is still the open parse question, fenced by the clitic-14-623-steelman null. This battery does not resolve 37's licensing.

No contradiction with standing verdicts: consistent with x-33-laisser-test null (X = causative -er family, 'laisser' LEAD, gated), narrower than erstem-33-id null, consistent with the A10 33+29 HOLD (8 whole / 5 stem windows).

## Follow-up proposed (worker suggestion, not null-mandated)

- x-33-37-licensing: decide how 37 licenses the bare infinitive at the @625-626 hapax (37-33 adjacency, 37's only 33-follower in 28 occurrences). Bar: name the licensing mechanism (predicative-with-bare-infinitive, 37 non-predicative here, or boundary re-segmentation) with the window parsing under standing values + <=1 stated assumption. This is the remaining 37-side blocker on the boundary route at @627.
