# Battery report: importe-30-subject-sweep — finite-verb vehicle sweep over all 19 @30 windows

- Target: `importe-30-subject-sweep` (battery-queue.json, priority 2, status queued)
- Claim: "finite-verb vehicle sweep over all 19 @30 windows under granted values only"
- Worker: ag-cb35d600
- Date: 2026-10-08
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`). `canonical.py` NOT used. R5005 untouched.
- All @-offsets are pair indices in the repaired stream.
- Lock: `code/crowd17/next-token/locks/importe-30-subject-sweep.lock` created on start; no stale lock present.

## Bar (verbatim, pre-registered)

"promote-consideration iff >=1 window parses '[subj] importe' with a granted subject; else record 'importe' as @1702-word-formation-confined. @1561 gated on noun-26; @1309 gated on 74/52; @1327 gated on 62 - state gates, do not force."

Numbered clauses (frozen before testing):
1. >=1 of the 19 @30 windows parses "[subj] importe" with a subject whose value is granted -> promote-consideration for 30='importe'.
2. Else: record 'importe' as @1702-word-formation-confined (no finite-verb vehicle outside the word-formation anchor).
3. @1561 is gated on noun-26 (26's class open) — state the gate, do not force.
4. @1309 is gated on 74/52 (classes open) — state the gate, do not force.
5. @1327 is gated on 62 (class open) — state the gate, do not force.

## Method

Parsed the repaired stream fresh (1,847 pairs confirmed; n(30) = 19, re-derived). For each
window, inspected the 12-pair left context and tested whether any subject-headed
"[subj] importe" parse is available under GRANTED values only (§7 banked pencil +
promoted/granted + provisional, plus battery-promoted 94='ne', 12='n'/48='e',
06='ent', 24=finite-verb class).

Subject inventory under granted values (French grammar applied strictly):
- 79='tout' ("tout importe" = "everything matters", grammatical) — the only granted
  impersonal-capable subject candidate.
- 84='on' ("on importe" ungrammatical — "importer" in the "matter" sense takes no 'on').
- 47/87='ce' (bare "ce" cannot head an impersonal subject; needs the "cela" 87-11 form).
- 64='qui' (relative pronoun — needs an antecedent + matrix clause).
- 77='le'/11='la' (articles — need a noun value to head a subject).
- 59='est' (verb — cannot be a subject).
- 12='n'/48='e' letters — not words; cannot head a subject.
- Everything else in the local clauses is value-open and may not serve.

Adjacency is not strictly required (a subject may head a clause with intervening
granted material), but any intervening token must be granted for the parse to count.

## Window-level evidence

1. @30 (a1_00) `...00 34 24 | 30 03 64`: predecessor 24 (finite-verb class) adjacent —
   two finite verbs ("[verb] importe") = ungrammatical. FAIL.
2. @45 (a1_01) `...88 43 81 | 30 62 96`: predecessor 81 (value open; 81='prin' killed).
   No granted subject anywhere in the 12-pair clause. FAIL.
3. @483 (a2_11) `...00 13 52 | 30 01 19`: predecessor 52 (open). 84='on' 10 pairs back,
   but separated by 24 (finite verb) and "on importe" is ungrammatical anyway. FAIL.
4. @560 (a3_02) `...86 94 59 | 30 67 11`: "86 94 59 30" = "[86] n'est importe" — two
   finite verbs adjacent. FAIL.
5. @656 (a4_02) `...49 24 26 | 30 03 62`: predecessor 26 (class open, noun-26 null).
   "ce" (87) 12 back cannot bridge open material. FAIL.
6. @742 (a5_02) `...00 36 20 | 30 67 77`: predecessor 20 (value open; 20='fois' killed).
   "la" (11) 10 back takes 24 (finite verb) — no subject. FAIL.
7. @993 (a6_01) `...49 24 26 | 30 03 60`: predecessor 26 open; same shape as @656. FAIL.
8. @1114 (a6_07) `...41 65 38 | 30 69 11`: predecessor 38 (open). "ce" (47) 9 back,
   intervening material open. FAIL.
9. @1222 (a7_01) `...61 24 48 | 30 09 20`: predecessor 48='e' (letter, granted) — a
   letter is not a word and cannot head a subject. "le" (77) 6 back takes open 83. FAIL.
10. @1251 (a7_02) `...67 46 26 | 30 06 65`: predecessor 26 open. Granted "87 11"='cela'
    7-8 back, but "cela pour [33] [16] pour [67] que [26] importe" has open tokens
    (33,16,26) in the subject span — ungrantable. FAIL.
11. @1269 (a7_02) `...69 88 24 | 30 20 64`: predecessor 24 (finite verb). FAIL.
12. @1309 (a7_04) `...43 77 74 52 | 30 92 44`: GATE (clause 4) — "77 74 52 30"
    ("le [74] [52] importe") is gated on 74/52 classes (both open). Gate stated,
    not forced. No granted-subject parse. FAIL.
13. @1327 (a7_04) `...08 62 98 56 | 30 06 62`: GATE (clause 5) — "62 98 56 30" is
    gated on 62 ('on' killed unconditioned per collision-62-84; 'il' rival unpromoted).
    Gate stated, not forced. FAIL.
14. @1368 (a7_06) `...79 14 60 03 | 30 82 16`: predecessor 03 (open). Granted 79='tout'
    4 back: "94 79 14 60 03 30" = "ne tout [14] [60] [03] importe" — the only granted
    impersonal-subject candidate in any local clause, but 14/60/03 are value-open and
    cannot be granted as subject-span material. No granted-subject parse. (This window
    is also frame-62-94-79's standing unparsed residual — fenced, not re-decided.) FAIL.
15. @1561 (a8_01) `...17 11 26 | 30 06 60`: GATE (clause 3) — "17 11 26 30"
    ("fois la [26] [30]") is gated on noun-26 (class open per noun-26 null). Gate
    stated, not forced. FAIL.
16. @1702 (a8_06) `...85 33 94 | 30 20 62`: "94 30" = "n'importe" word-formation
    (sole stream 94-30 adjacency) — not subject-headed; this is the confinement
    anchor, not a vehicle window. FAIL (by design).
17. @1716 (a8_06) `...94 44 59 | 30 64 47`: "ne [44] est importe" — two finite verbs
    adjacent. FAIL.
18. @1729 (a8_07) `...39 88 24 | 30 15 01`: predecessor 24 (finite verb). "qui" (64)
    12 back cannot bridge a 24-finite-verb barrier. FAIL.
19. @1733 (a8_07) `...15 01 56 | 30 06 60`: predecessor 56 (open). (Also contains a
    second 30 four pairs upstream at @1729.) FAIL.

Result: 0/19 windows parse "[subj] importe" with a granted subject. Clause 1 FAILS;
clause 2 applies: 'importe' is recorded as @1702-word-formation-confined. Clauses 3-5:
gates stated, none forced.

## Per-clause results

1. >=1 window parses "[subj] importe" with a granted subject: FAIL — 0/19.
   The only grammatical subject candidate in any local clause (79='tout' @1368) cannot
   be granted its subject span (14/60/03 open); all other windows are verb-adjacent,
   open-predecessor, or gate-fenced.
2. Record 'importe' as @1702-word-formation-confined: APPLIES — the finite-verb
   vehicle does not materialize outside the word-formation anchor.
3. @1561 gate (noun-26): STATED, not forced — "fois la [26] importe" waits on noun-26.
4. @1309 gate (74/52): STATED, not forced — "le [74] [52] importe" waits on 74/52.
5. @1327 gate (62): STATED, not forced — "[62] [98] [56] importe" waits on 62.

## Adverses (answered, not ignored)

- **"26's class open (4/19 predecessors)":** CONFIRMED and respected. 26 directly
  precedes 30 at @656/@993/@1251/@1561 (4/19, re-derived); all four treated as gates
  or failures, none forced. The noun-26 null verdict is untouched.
- **"74/52 and 62 classes open":** CONFIRMED and respected. @1309 and @1327 gated
  per the bar; 62='il' not assumed (unpromoted), 62='on' not assumed (killed
  unconditioned per collision-62-84).
- **No standing verdict touched:** pas-30's promotion (30='pas') is not re-voted —
  this battery tests the rival's vehicle only, not 30's value. ne-30-1700's null,
  frame-62-94-79's unparsed residual (@1363/@1687), and the elision-test null all
  stand. §7 respected (67 the sole polyvalence; no polyvalence declared; all
  kills/splits/holds intact).

## Verdict

**null** — the finite-verb vehicle does not materialize: 0/19 @30 windows yield a
grammatical subject-headed "[subj] importe" parse under granted values only.
Per the bar's fallback, 'importe' is recorded as **@1702-word-formation-confined**
(the sole "n'importe" elision frame, stream-unique 94-30 adjacency). Not a kill:
no window forces the claim false and the bar defines no kill-grade clause; the
rival stands exactly where the elision-test null left it. Work regenerates below.

## Follow-ups (null regenerates work; supervisor to queue)

1. `importe-subject-gated-retest` (P2) — re-run this battery's bars on the three
   gated windows once their gates clear: @1561 (gate: noun-26 resolves), @1309
   (gate: 74/52 classes named), @1327 (gate: 62's class named). Bar:
   promote-consideration iff >=1 then parses "[subj] importe" with granted subjects;
   else re-confirm confinement.
2. `importe-tout-1368` (P3, gated on 14/60/03) — @1368 "94 79 14 60 03 30" is the
   only window with a granted impersonal-subject candidate (79='tout') in the local
   clause. Once 14/60/03 take values, test whether "tout [14] [60] [03] importe"
   parses with <=1 non-granted assumption; else fence it as a residual under
   frame-62-94-79.
3. `pas-30-importe-discrim` (P2) — adversarial value-level sweep: pas-30 stands
   promoted; sweep all 19 windows for any that FAILS under 30='pas' but parses under
   30='importe'. Bar: re-open 30's value iff >=1 discriminating window exists; else
   'importe' stays @1702-word-formation-confined and the rivalry is settled at
   battery level.
