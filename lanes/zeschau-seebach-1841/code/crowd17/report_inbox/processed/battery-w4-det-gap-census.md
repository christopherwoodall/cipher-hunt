# Battery report: w4-det-gap-census — W4 determiner gap as lane-law

- Target id: `w4-det-gap-census` (priority 2, status queued)
- Claim: the W4 determiner gap is lane-law, not a one-window assertion
- Worker: ce827938-c6cc-4308-95bb-9ad302c73e24
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
  `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`;
  1,847 pairs / 96 types re-derived in-session before testing). `canonical.py`
  never used. R5005, sealed gates, red-team adjudication queue untouched.
- Lock: code/crowd17/next-token/locks/w4-det-gap-census.lock (no prior lock
  existed; deleted on completion).
- Source context: dict-45-w4-adjudicate null (2026-10-09) — W4 @1162-1165
  determiner-gap finding ("et verdict" = bare singular countable noun in
  argument position, no determiner; kill-grade in scope).

## Bar (verbatim, pre-registered before testing)

"(a) census all 67='et' loci on the repaired stream (67->X); state which X are
noun-valued under granted values; (b) the gap is law-grade iff zero
bare-countable-noun-after-'et' compositions occur among decidable loci;
(c) use only granted/banked values for the noun call"

Numbered pass/fail clauses (frozen before judging):

1. Every 67 locus on the repaired stream is censused with its follower X and
   its @-offset; the 67='et' vs 67='veut' partition follows the §7 positional
   rule (67="veut" iff follower infinitive-shaped).
2. Among the decidable et-loci (X carrying a banked or granted value), the
   count of bare-countable-noun-after-'et' compositions is zero.
3. The noun call uses ONLY §7 banked values (11=la, 70=pre, 82=m, 34=i, 29=er,
   40=e, 46=que) and granted values (87=ce, 64=qui, 96=par, 17=fois,
   79="tout" A5, 00="pour" A9, 84="on" A15, 47="ce" A4). Provisional (77='le'),
   LEAD (78='ver' R16-005), battery-promoted (e.g. 93 verb-shaped), and open
   X-values are excluded from the noun call.
4. The named noun-valued X (if any) is stated; "noun-valued" means the value
   assigned to X is a noun under banked/granted values.

Adverses: "67->78 x4 (noun-shaped 78); 21's open value (left edge)"

## Method

1. Re-derived the repaired stream in-session (1,847 pairs / 96 types,
   byte-exact per repair_parse.py).
2. Enumerated every 67 locus (38 total; last pair is 93, so all 38 have a
   follower). Applied the §7 sole-polyvalence positional rule to partition
   67='veut' (follower infinitive-shaped) from 67='et' (all other followers).
3. Infinitive-shaped followers under §7: 33 (A10 CONFIRM: 33 is a que-taking
   infinitive) and 86 (A9: 86 INF-class, class-level grant). All other
   followers are non-infinitive under standing values (93 is verb-shaped only
   per battery promotion 2026-10-09 — not §7-granted — so 67->93 stays an
   et-locus; the noun-call exclusion applies to X's class, not to 'et'-ness).
4. Classified every X against §7 banked/granted values only. The sole noun
   among them is 17=fois.

## Census: all 38 67-loci (0-based 67-offset, window ±7 shown for 67->78)

67='veut' loci (9) — follower infinitive-shaped per A10/A9:
- 67->33 x6 @272/1148/1423/1450/1476/1623 (33 = que-taking infinitive)
- 67->86 x3 @1098/1390/1457 (86 = INF-class)

67='et' loci (29):

| 67->X | n | @-offsets | X value (banked/granted) | decidable? | composition |
|---|---|---|---|---|---|
| 67->11 | 4 | 561/669/753/996 | 11=la (banked, determiner) | yes | "et la" x4 — determiner present |
| 67->46 | 2 | 471/1248 | 46=que (banked, complementizer) | yes | "et que" x2 |
| 67->64 | 2 | 143/394 | 64=qui (granted, rel. pronoun) | yes | "et qui" x2 |
| 67->96 | 1 | 959 | 96=par (granted, preposition) | yes | "et par" x1 |
| 67->77 | 6 | 506/638/743/1239/1400/1597 | 77='le' provisional — EXCLUDED by clause (c) | no | "et le"-shaped x6 (determiner present, would not be bare) |
| 67->78 | 4 | 351/491/1163/1842 | 78='ver' LEAD (R16-005 unsettled) — EXCLUDED by clause (c) | no | see §Adverses |
| 67->76 | 2 | 199/1045 | open — excluded | no | — |
| 67->08 | 2 | 630/1519 | open — excluded | no | — |
| 67->93 | 1 | 110 | verb-shaped, battery-promoted not §7-granted — excluded | no | — |
| 67->14 | 1 | 116 | open — excluded | no | — |
| 67->63 | 1 | 633 | open — excluded | no | — |
| 67->91 | 1 | 851 | open — excluded | no | — |
| 67->16 | 1 | 902 | open — excluded | no | — |
| 67->98 | 1 | 1372 | open — excluded | no | — |

Decidable et-loci: 9 (11 x4, 46 x2, 64 x2, 96 x1).
Undecidable et-loci: 20.

## Window-level evidence

Decidable loci (composition right of 'et'):
- @561 row a3_01: `59 34 17 86 94 59 30 [67] 11 43 24 80 97 13 76` → "et la [43]"
- @669 row a4_02: `50 80 03 62 06 00 20 [67] 11 86 24 80 03 64 37` → "et la [86]"
- @753 row a5_02: `85 28 00 64 02 97 40 [67] 11 70 82 34 29 40 20` → "et la pre…" (11-70 = "la pre…" crib-adjacent)
- @996 row a6_01: `76 49 24 26 30 03 60 [67] 11 96 82 33 00 86 56` → "et la par m…"
- @471 row a2_10: `42 96 00 33 79 80 06 [67] 46 84 24 37 78 74 45` → "et que on…"
- @1248 row a7_01: `81 87 11 00 33 16 00 [67] 46 26 30 06 65 46 01` → "et que [26]…"
- @143 row a1_04: `23 91 65 13 66 14 74 [67] 64 77 84 29 87 64 96` → "et qui [77] on…"
- @394 row a2_07: `91 36 62 91 84 73 34 [67] 64 79 82 48 06 11 45` → "et qui tout m…"
- @959 row a6_00: `96 87 46 24 85 04 20 [67] 96 00 86 56 41 19 24` → "et par pour [86]…"

67->78 windows (adverse 1), ±7:
- @351 row a2_05: `87 01 06 70 12 94 74 [67] 78 40 92 98 92 47 11` → "et [78] e [92]"
- @491 row a2_11: `01 19 64 76 42 41 20 [67] 78 42 94 02 79 88 47` → "et [78] [42] ne…"
- @1163 row a6_09 (W4): `80 17 77 82 44 83 21 [67] 78 45 13 55 61 94 87` → "…21 et [78-45] [13-55-61] ne ce…"
- @1842 row a8_11: `69 64 22 42 44 83 21 [67] 78 49 74 93` → "…21 et [78] [49] 74 [93]"

## Per-clause pass/fail

1. Full 67 census with et/veut partition: PASS — 38/38 loci censused, all with
   @-offsets; 9 veut-loci (67->33 x6, 67->86 x3) via the §7 positional rule;
   29 et-loci.
2. Zero bare-countable-noun-after-'et' among decidable loci: PASS — 9/9
   decidable compositions are non-noun: "et la" x4 (determiner), "et que" x2
   (complementizer), "et qui" x2 (relative pronoun), "et par" x1
   (preposition). Zero bare countable nouns.
3. Only banked/granted values used for the noun call: PASS — provisional
   77='le', LEAD 78='ver', battery-promoted 93 verb-shaped, and all open
   X-values (76/08/14/63/91/16/98) were excluded from the noun call; the
   veut-partition used only §7 class grants (A10, A9).
4. Noun-valued X stated: PASS — the sole noun among banked/granted values is
   17=fois; 67->17 occurs ZERO times on the repaired stream. No X is
   noun-valued under granted/banked values.

Adverses:
- "67->78 x4 (noun-shaped 78)": FENCED with stated cause — 78 is noun-shaped
  under granted evidence (determiner-predecessors 11=la banked, 47=ce and
  87=ce granted — see source report), but 78's own value is unsettled LEAD
  (R16-005), so clause (c) bars the noun call: these 4 loci are undecidable,
  not counted. Fenced, not ignored. Recorded stakes: these four windows are
  the exact shape the law forbids — if 78='ver' ever promotes, the law is
  falsified at 4/38 loci. The law is established over the decidable set only,
  as the bar writes it.
- "21's open value (left edge)": FENCED with stated cause — at W4 (@1162-1163:
  "21 67 78") 21's value is open, so a coordinate structure "...[21] et [78]…"
  cannot be excluded. It does not alter the census composition call (the
  67->78 composition stands regardless of the left edge), and French
  coordination does not let a left conjunct license a bare singular second
  conjunct ("et" does not project backward). The W4 global-parse residual is
  owned by the already-queued w4-left-edge-21-83 target (this battery's
  follow-up #2 from the source report) — no double-work.

No standing red-team verdict is contradicted: R16-005 grades 78='ver' LEAD
(correctly unsettled); this battery makes no value claim about 78.

## Verdict: PROMOTE

Headline: the W4 determiner gap is lane-law over the decidable set. Census of
all 38 67-loci on the repaired stream: 9 are 67='veut' (infinitive-shaped
followers 33/86 per §7); of the 29 et-loci, 9 are decidable under granted/
banked values and ALL NINE compose as non-noun ("et la" x4, "et que" x2,
"et qui" x2, "et par" x1) — zero bare-countable-noun-after-'et' compositions.
The sole granted noun, 17=fois, never follows 67. The four 67->78 loci are
undecidable under the bar's own clause (c) (78 unsettled LEAD) and are fenced
as the law's designated falsification set; 21's open left edge is fenced to
the already-queued w4-left-edge-21-83. Both adverses answered, none ignored.

Scope honesty: the law is established over the 9 decidable et-loci, not over
the 20 undecidable ones. The strongest undecidable group (67->77 x6, "et le"-
shaped under provisional 77='le') would, if 77='le' ratifies, ADD 6 more
confirming windows (determiner present, not bare). The risk group is only the
67->78 x4.

## Reproducibility

Stream re-derived in-session via repair_parse.py load_rows() + parse():
1,847 pairs / 96 types. Census script enumerated 67-loci directly (38 tokens,
38 with followers; last pair = 93). Grant table used: §7 banked + granted
verbatim from BATTERY-PROTOCOL.md; A10 (33 que-taking infinitive), A9 (86
INF-class) for the veut partition. No writes outside this report, the queue
edit (own entry only, temp-file + rename, re-read before write), and the
lockfile (deleted).
