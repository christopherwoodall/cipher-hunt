# Battery report: pas-30 — claim 30="pas"

- Target: `pas-30` (battery-queue.json, priority 1, status queued)
- Claim: 30 = "pas"
- Worker: b36303dc-97fb-4dc2-9db1-c38201067701
- Date: 2026-10-08
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`). `canonical.py` NOT used. R5005 untouched.
- All @-offsets are pair indices in the repaired stream.

## Bar (verbatim, pre-registered)

"promote iff both ne-frames parse as 'ne...pas' + >=1 more independent ne-frame + zero contradictions"

Numbered clauses (frozen before testing):
1. The ne-frame at @558 (94@558, 59@559, 30@560) parses as 'ne...pas'.
2. The ne-frame at @1713 (94@1713, 44@1714, 59@1715, 30@1716) parses as 'ne...pas'.
3. At least one more independent ne-frame (94 ... 30) parses as 'ne...pas'.
4. Zero contradictions: no tested window forces 30 != "pas".

## Method

Enumerated every 94 (37 occurrences) and every 30 (19 occurrences, matching the
queue's "19 windows to test"). For each 94, inspected the +1..+8 downstream
window; for each 30, the -4..+4 window and the nearest upstream 94. Parses use
only standing values: banked pencil (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e,
46=que), promoted/granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour,
84=on, 47=ce), provisional (59=est, 77=le), battery-promoted 94=ne (pending
red-team ratification), 67 et/veut polyvalence. No other values assumed.

## Window-level evidence

Standing-value key: 94=ne, 59=est (provisional), 11=la, 40=e, 34=i, 46=que,
64=qui, 96=par, 17=fois, 79=tout, 00=pour, 67=et/veut.

**Clause-1 frame, @558 (row a3_02):** 557=86, 558=94=ne, 559=59=est, 560=30,
561=67=et/veut, 562=11=la. Reads "86 n'est pas [et/veut] la ..." — canonical
"n'est pas" order, followed by clause boundary + new clause ("[il] n'est pas;
veut la ..." or "...pas, et la ..."). Parses as 'ne...pas' cleanly.

**Clause-2 frame, @1713 (row a8_06):** 1712=65, 1713=94=ne, 1714=44,
1715=59=est, 1716=30, 1717=64=qui, 1718=47=ce. Reads "65 ne [44] est pas qui
ce ..." — ne...pas with intervening material 44 (unknown, positional
clitic/adverb slot) and the verb 59=est, as in "n'en est pas" / "ne l'est
pas". Parses as 'ne...pas'.

**Clause-3 frames (independent ne-frames, different rows/contexts):**
- 94@651 (row a4_02): 651=94=ne, 652=76, 653=49, 654=24, 655=26, 656=30,
  657=03. "ne 76 49 24 26 pas" — ne...pas with 4 intervening pairs. Parses.
- 94@1363 (row a7_06): 1363=94=ne, 1364=79=tout, 1365=14, 1366=60, 1367=03,
  1368=30, 1369=82=m. "ne tout 14 60 03 pas m..." — ne...pas with 4
  intervening pairs. Parses.
Both are independent of the canonical pair and of each other (rows a4_02 vs
a7_06, disjoint contexts).

**All 19 @30 windows (contradiction scan):**
- @30[30] (a1_00): 34=i 24 30 03 64=qui — "i 24 pas 03 qui". No forced
  non-pas parse.
- @30[45] (a1_01): 81 30 62 96=par — "...pas par..." ("not by ..."). Parses.
- @30[483] (a2_11): 13 52 30 01 19 64=qui. Parses.
- @30[560] (a3_02): clause-1 frame above. Parses.
- @30[656] (a4_02): 24 26 30 03 62 — "...pas 03...". Parses.
- @30[742] (a5_02): 20 30 67=et/veut 77=le — "...pas veut le..." (clause
  boundary). Parses.
- @30[993] (a6_01): 24 26 30 03 60. Parses.
- @30[1114] (a6_07): 38 30 69 11=la — nearest upstream 94 at d=12 (@1102).
  Parses ("pas de"-class licensed absence).
- @30[1222] (a7_01): 24 48 30 09 20 — 48 is killed as est/ne/de per §7, so
  no conflicting 'ne' reading; "...48 pas..." parses.
- @30[1251] (a7_02): 46=que 26 30 06 65 46=que — "que 26 pas 06 65 que".
  Parses.
- @30[1269] (a7_02): 88 24 30 20 64=qui 47=ce. Parses.
- @30[1309] (a7_04): 74 52 30 92 44 00=pour. Parses.
- @30[1327] (a7_04): 56 30 06 62 94=ne 70=pre — "pas 06 62 ne pre...";
  pas-parse and following ne-frame coexist (clause boundary). Parses.
- @30[1368] (a7_06): clause-3 frame above. Parses.
- @30[1561] (a8_01): 11=la 26 30 06 60 — "la 26 pas 06 60"; nearest 94 at
  d=12 (@1549). Parses.
- @30[1702] (a8_06): FENCED — see adverse below.
- @30[1716] (a8_06): clause-2 frame above. Parses.
- @30[1729] (a8_07): 88 24 30 15 01 56 30 — "24 pas 15 01 56 pas";
  clause-boundary adjacency of two pas tokens (cf. "pas ..., pas ...").
  Parses.
- @30[1733] (a8_07): 30 15 01 56 30 06 60 — "pas 15 01 56 pas"; same
  clause-boundary reading as @1729. Parses.

94-frames without a downstream 30 (30 of 37) are not contradictions: French
'ne' pairs with jamais/que/rien/personne as well as pas (e.g. 94@1705 ->
"...29=er 40=e 65" with no 30; 94@1182 -> "94 82=m 06 06 59=est ...", a
ne...est frame). No frame forces a non-pas value on 30.

## Adverse (fenced, not ignored)

**@1700/1702 frame vs queued target ne-30-1700 ('n'importe' rival).** Window
1698..1706: 91 85 33 94=ne 30 20 62 94=ne 88. The rival reads 94@1701+30@1702
as "n'importe" (30='importe'), parsing "85 33=dire n'importe 20 62" without a
clause boundary; under 30='pas' the same window parses as "...33. Ne pas 20
62..." requiring a clause boundary at 33|94 (33='dire' is itself only a queued
hypothesis). Both readings are bracket-dependent; neither is forced. This
battery does NOT use @1701/1702 for any bar clause (clause 3 is satisfied by
@651 and @1363 instead). Fenced with stated cause: the rival value
30='importe' is under test by ne-30-1700 — this report does not decide that
target. If ne-30-1700 demonstrates 30='importe' on this frame, this promotion
must be re-opened.

## Per-clause results

1. @558 frame parses as 'ne...pas': PASS ("n'est pas", canonical order).
2. @1713 frame parses as 'ne...pas': PASS ("ne 44 est pas", intervening 44
   in clitic/adverb slot).
3. >=1 more independent ne-frame: PASS — two, @651->656 and @1363->1368.
4. Zero contradictions: PASS — all 19 @30 windows scanned; none forces
   30 != "pas"; the one bracket-dependent rival frame (@1702) is fenced to
   ne-30-1700 per protocol §4.

## Caveats (epistemic status, marked up front)

- 94='ne' is battery-promoted, PENDING red-team ratification (§7); all
  ne-frame readings inherit that caveat. If 94 != 'ne', this promotion falls.
- 59='est' is provisional; clause 1's "n'est" gloss depends on it.
- Canonicality caveat stands (§7): 68 of 70 upstream row offsets unvalidated;
  offsets here are post-repair indices.

## Verdict

**promote** — all four bar clauses pass; the single discovered adverse
(@1700/1702 'n'importe' rival) is fenced with stated cause to the queued
ne-30-1700 battery per protocol §4, and was deliberately excluded from the
clause-3 evidence. Promotion is conditional on red-team ratification (of this
battery and of 94='ne'); the red team re-opens this verdict if ne-30-1700
demonstrates 30='importe' on the @1702 frame.

(No null, so no follow-up targets required. Do NOT edit battery-queue.json:
supervisor ingests this report.)
