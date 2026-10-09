# Battery verdict: stem-86 — 86 identification

Date: 2026-10-08. Worker: 041d19bc-a468-46fc-bff8-cd3ef1577fd9.

## Bar (verbatim from battery-queue.json)

"promote iff all 12 windows parse under one value + adverses answered"

Evidence-field CORRECTION (2026-10-08, stem-33-86 battery, part of the target
brief): 86 has n=32 on the repaired stream, not 12 (12 = the pre=00 subset).
The worker must test all 32 windows; the bar's "all 12 windows" scope
under-counts 20.

### Numbered clauses (operative)

1. All 32 windows of 86 on the repaired stream parse under ONE value.
2. Every listed adverse is answered (re-parsed cleanly, fenced with stated
   cause, or shown to be a misread — never ignored).

Listed adverses: three adverses for 86='le' (@552 'pour le est', @866, @888);
'par 86' @947 ungrammatical; value NOT named.

## Method

Parsed the repaired 1,847-pair stream exactly per
code/side-keyhunt/repair_parse.py (repaired_offsets.json +
data/upstream-ct_R5005.txt). Never used canonical.py. Enumerated all 32
indices i with seq[i]=='86' and printed seq[i-3:i+4] with stream @-offsets.
Tested each window for grammaticality in 1841 diplomatic French under the
candidate value 86='le' (the only value the adverses frame; value otherwise
not named), using banked values only: 11=la, 70=pre, 82=m, 34=i, 29=er,
40=e, 46=que (pencil); 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour,
47=ce, 84=on, 12=n, 48=e, 30=pas, 06=ent (granted); 59=est, 77=le
(provisional). INF-class for 86 granted (A9). No R5005 contact, no sealed
gates, no red-team queue contact.

Distributional facts confirmed on the repaired stream:
- n(86) = 32.
- 86-29 (infinitive-shaped) x4: @431, @1375, @1391, @1825.
- '00 86 56' x4: @962, @1002, @1506, @1792.
- '00 86 29' x2: @1375, @1825.
- 00 immediately left of 86 in 12 windows (the "pre=00 subset").
- 77 immediately left of 86 in 5 windows.

## Window-level evidence (all 32, @-offsets on repaired stream)

Notation: L3 L2 L1 [86] R1 R2 R3; known values substituted. Verdict per
window under 86='le'.

DETERMINER-SHAPED (parse under 'le'):
- #5 @661: 62 16 pour [le] 50 80 03 — "pour le [50]" OK (50 nominal slot).
- #14 @948: 62 98 par [le] 01 le* 86 — "par le [01]" OK if 01 nominal.
- #16 @962: 67 par pour [le] 56 41 19 — "pour le [56]" OK.
- #17 @1002: m 33 pour [le] 56 ce 91 — "pour le [56]" OK.
- #18 @1099: ent er 67(et) [le] 52 m 94 — "et le [52]" OK.
- #19 @1128: 37 43 pour [le] 52 37 86 — "pour le [52]" OK.
- #27 @1458: 61 21 67(et) [le] 66 79 17 — "et le [66]" OK if 66 nominal.
- #28 @1506: 42 33 pour [le] 56 41 12 — "pour le [56]" OK.
- #30 @1792: ce 03 pour [le] 56 42 94 — "pour le [56]" OK.

INFINITIVE-SHAPED (fail under 'le', parse under verb-stem per A9):
- #2 @431: 42 63 le* [le] er m 16 — "le le er" FAIL ('le' global).
- #25 @1375: 67 98 pour [le] er 89 84 — "pour le er" FAIL.
- #26 @1391: ent er 67 [le] er 89 16 — "veut/et le er" FAIL. (Under stem:
  67='veut' by the positional rule, "veut [stem]er" OK.)
- #31 @1825: pour 97 pour [le] er m 38 — "pour le er" FAIL.

HARD FAILS under 'le' (no dependence on provisional 77='le'):
- #0 @175: 60 09 ce [le] 21 69 14 — "ce le" ungrammatical. FAIL.
- #3 @553: 55 81 pour [le] est* i fois — "pour le est" ungrammatical. FAIL.
  (Elision fence "pour l'est" considered: grammatical in isolation, but the
  continuation "i fois" does not resolve — fenced as strained, not a parse.)
- #6 @671: 20 67 la [le] 24 80 03 — "la le" ungrammatical (11=la is pencil
  ground truth). FAIL.
- #8 @728: qui la pour [le] e 88 la — "pour le e" ungrammatical. FAIL.
- #24 @1345: 52 38 ce [le] 66 73 34 — "ce le" ungrammatical. FAIL.

FAILS under 'le' via provisional 77='le' adjacency ("le le"):
- #9 @799: 37 44 le* [le] 44 74 62 — "le le" FAIL.
- #11 @878: 49 16 le* [le] 78 17 08 — "le le" FAIL.
- #15 @951: 86 01 le* [le] par ce que — "le le" FAIL.
- #21 @1134: 86 24 le* [le] 20 62 98 — "le le" FAIL.

UNRESOLVED under current banked values (unknown neighbors):
- #1 @300: 78 e 97 [86] 91 18 89 — "97 [86] 91", 97/91 unknown. OPEN.
- #4 @557: est* i fois [86] 94 est* pas — 94 unknown (94='ne' lead would give
  "le ne est pas", ungrammatical). OPEN.
- #7 @716: 63 pour 66 [86] 01 02 21 — 66 unknown; previously killed orphan
  claim site. OPEN.
- #13 @899: 14 98 83 [86] 16 92 67 — 83 unknown. OPEN.
- #20 @1131: 86 52 37 [86] 24 le* 86 — "37 le [24-verb]" ungrammatical as
  noun-le-verb; previously killed orphan site. OPEN/FAIL-leaning.
- #22 @1147: 42 98 98 [86] 67 33 66 — 98='vient' unratified; "vient le 67"
  ungrammatical under current grants. OPEN.
- #23 @1335: 52 39 83 [86] 71 64 60 — 83 unknown. OPEN.
- #29 @1739: n e 52 [86] n i 94 — 52 unknown. OPEN.

MIXED (listed-adverse region, problem independent of 86):
- #10 @867: ce que pour [le] pre ce le* — "pour le pre[mier]" parses, but the
  window contains "87 77" = "ce le", ungrammatical regardless of 86. The @866
  adverse as framed against 86 does not hold; the window's defect lies
  downstream. Adverse ANSWERED as misread (offset + locus).
- #12 @889: 03 02 pour [le] ent le* 76 — "pour l'ent le" ungrammatical; no
  elision rescue ("l'entremise" would need "remise" after 06, but 77='le'
  follows). @888 adverse STANDS.

Adverse audit summary:
- @552 'pour le est' → repaired @553: CONFIRMED, stands (#3).
- @866 → repaired @867: ANSWERED as misread — "pour le pre" is grammatical;
  the ungrammatical "ce le" (87 77) is downstream of 86.
- @888 → repaired @889: CONFIRMED, stands (#12).
- 'par 86' @947 → repaired @948: ANSWERED as misread — "par le [01]" is
  grammatical pending 01; the ungrammaticality claim does not survive the
  repaired stream.

## Per-clause verdicts

Clause 1 (all 32 windows parse under one value): FAIL. 86='le' fails 14 of
32 windows outright (9 hard fails independent of provisional grants, 5 via
77='le' adjacency; #20 leans fail). The verb-stem reading (A9) covers the
four 86-29 windows but fails the nine determiner-shaped windows ('00 86 56'
x4, #5, #14, #18, #19, #27: "pour [stem] 56" is ungrammatical). No third
single value was found that covers both lives: noun fails #2 ("le [noun]er"),
preposition fails #0 ("ce [prep]"). The distribution splits cleanly into a
determiner-life and a stem-life.

Clause 2 (adverses answered): PARTIAL. Two of four adverses answered as
misreads on the repaired stream (@866, @947); two stand (@552→@553,
@888→@889). Not all adverses answered.

Kill-grade check: windows #0 ("ce le") and #6 ("la le") force 86='le' false
as a GLOBAL value at kill grade — both use only pencil/granted values
(87=ce, 11=la). This kills the 'le'-global hypothesis, not the target's
existential claim (value was never named), and no cleaner rival covers all
frames. Per protocol §4 this is not a target kill; it is a null with the
'le'-global hypothesis dead inside it.

## Verdict: NULL

No single value parses all 32 windows; 86='le' is dead as a global value
(#0, #6 at kill grade); the stem reading covers only the 86-29 subset. The
residue is structural: determiner-life vs stem-life in one digit-pair, which
is either polyvalence (needs red-team approval — 67 et/veut is currently the
sole true polyvalence), a homophone set, or mis-segmentation in the problem
windows. No standing verdict is contradicted; nothing is downgraded.

## Follow-up targets (null regenerates work)

1. `le-86-determiner-subset` (priority 2): test 86='le' on the
   determiner-shaped subset only (#5, #14, #16, #17, #18, #19, #27, #28,
   #30). Bar: promote iff all nine parse under 'le' with 50/01/52/56/66 in
   nominal slots + the "ce le"/"la le" windows (#0, #6, #24) explained by
   re-segmentation or fenced with cause. This decides whether a 'le'-life of
   86 survives once the stem-life is split off.
2. `homophone-86-split` (priority 2): distributional split test — 86='le'
   iff follower in {56, 50, 01, 52, 66, 70, 78, 48, 44, 24, 20, 67, 71, 12,
   21, 91, 94, 16, 96} (determiner-life) vs 86=stem iff follower 29
   (stem-life, n=4). Bar: promote the positional split rule iff no window
   violates it and 1690-uniformity holds within each life at the lane's
   standard; include a byte-level homophone-set candidacy check.
3. `reseg-86-problem-windows` (priority 3): re-segmentation audit of #0
   (@175 "ce 86 21"), #6 (@671 "la 86 24"), #8 (@728 "pour 86 48"), #7
   (@716). Bar: for each window, test whether 86 is word-internal (a
   syllable of a longer word with its neighbors) rather than a standalone
   word; kill the standalone-word assumption per window iff a cleaner
   multi-group word parse is demonstrated on bytes.

R5005, sealed gate instances, and the red-team adjudication queue were not
touched. Polyvalence for 86 is NOT declared here — it is flagged as the
structural question for the red team.
