# PRE-REGISTRATION (round-8 morphologist, 2026-10-07)

## (a) Second 64-96-47 window hunt
Criteria (fixed before data):
1. Cipher-side match: in the repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json),
   find ALL positions i with pairs[i]=='96', pairs[i-1]=='64', pairs[i+1]=='47', i != 150.
2. F33-falsifiable bar (same as the first window, F55): the window promotes the
   conditioned reading only if the 96=verb-stem reading survives adjudication at
   THIS window: (a) the slot filler class must be verb-compatible (era verb-filler
   unanimity from N47 applies to the frame class "qui __ ce"), (b) the rival
   96="par" reading must have zero era support at this slot ("qui par ce"=0),
   (c) fragment-substitution must be excluded by the window's neighbors
   (the Q2-style test: neighbors must not carry fragment markers).
   A window where the verb reading is forced into ungrammaticality KILLS the
   candidacy; a window where the reading is unfalsifiable (no prediction
   differential between verb and par at that window) is scored neutral/absent,
   NOT promoted.
3. Independence: the second window must not share context with @149-151 beyond
   the trigram itself.

## (a') Downstream-verb hunt for the parenthetical
Continue from round 7's two honest nulls: (i) exhaustive census of "ce qui __ ce
que" frames found none beyond @148-152; (ii) downstream window @155-175 held no
identified verb cell. For round 8: hunt cipher-side for verb-shaped cells
downstream of any 64-96-47 window (follower-profile verb markers: 29=er,
46=que, GT/prov anchors), and mine the diplomatic corpus for "qui [V] ce que"
verb-continuation profiles that would predict what SHOULD follow the parenthetical.

## (b) 67 classification of the 9 open windows
Only the standing rules (battery67_final.json): R_et1..6, R_veut1..3, plus the
R_et5 fence (does not fire when pre in {21,11}). New rules need their own
pre-registration — none pre-registered here, so none will be invented.
@630/@633 (doubled 67s, "78 67 08 52 67 63 ... 74 46 60"): classify each 67
by its own (pre, suc) conditioning; split is legitimate only if the two windows
fire different rules or different fences apply.
Open: 199 (08/76), 630 (78/08), 633 (52/63), 902 (92/16), 1248 (00/46),
1372 (91/98), 1450 (36/33), 1519 (91/08), 1623 (66/33).
For each: report (pre, suc), rule fired or open-residual, evidence.
