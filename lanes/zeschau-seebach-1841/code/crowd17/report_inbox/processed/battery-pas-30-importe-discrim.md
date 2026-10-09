# Battery report: pas-30-importe-discrim — adversarial value-level sweep of 30

- Target: `pas-30-importe-discrim` (battery-queue.json, priority 2, status queued)
- Claim: adversarial value-level sweep: any of the 19 @30 windows that FAILS under 30='pas' but parses under 30='importe'
- Worker: dec9e278-3fc8-4be9-8aab-50a97ffe9cbd
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`). `canonical.py` NOT used. R5005 untouched.
- All @-offsets are 0-based pair indices in the repaired stream.
- Lock: `code/crowd17/next-token/locks/pas-30-importe-discrim.lock` created on start; no stale lock present.

## Bar (verbatim, pre-registered)

"re-open 30's value iff >=1 discriminating window exists; else 'importe' stays @1702-word-formation-confined and the rivalry is settled at battery level"

Numbered clauses (frozen before testing):
1. >=1 of the 19 @30 windows FAILS under 30='pas' (forces an ungrammatical/impossible reading) AND parses under 30='importe' -> re-open 30's value.
2. Else: 'importe' stays @1702-word-formation-confined and the rivalry is settled at battery level.

## Method

Re-derived the repaired stream fresh (1,847 pairs / 96 types confirmed; n(30) = 19, byte-matching the pas-30/importe-30 battery censuses). This is an ADVERSARIAL sweep: for each window I first tried to break 30='pas', then checked whether 30='importe' parses. A window only discriminates if it fails under 'pas'. Values used: banked pencil (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que), granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce), provisional (59=est, 77=le), battery-promoted 94='ne' (ratification caveat), 06='ent', 24=finite-verb class, 12='n'/48='e' letters. Nothing else assumed. 1841 French only.

## Window-level evidence

For each window: does 'pas' parse (P/N)? Does 'importe' parse (P/N)? A discriminator needs P(pas)=N, P(importe)=P.

1. @30 (a1_00) `81 00 34 24 | 30 03 64 32`: "34=i [24-verb] 30". 'pas': "i [verb] pas" parses. 'importe': two finite verbs adjacent ("[verb] importe") = ungrammatical. NOT discriminating (importe fails, not pas).
2. @45 (a1_01) `24 88 43 81 | 30 62 96 00`: "81 30" open predecessor. 'pas': "...pas par..." (96=par) parses. 'importe': no granted subject (81 open). NOT.
3. @483 (a2_11) `93 00 13 52 | 30 01 19 64`: "52 30" open. 'pas' parses. 'importe': no granted subject. NOT.
4. @560 (a3_02) `17 86 94 59 | 30 67 11`: "86 ne est 30 [et/veut] la" (94=ne, 59=est). 'pas': canonical "n'est pas" — parses cleanly. 'importe': "n'est importe" = two finite verbs, ungrammatical. NOT (strong pas window).
5. @656 (a4_02) `76 49 24 26 | 30 03 62 16`: ne-frame "ne 76 49 24 26 30". 'pas': "ne ... 26 pas" parses. 'importe': finite 24 in clause + "importe" = verb pile-up; 26's class open so "[26] importe" is ungranted. NOT.
6. @742 (a5_02) `06 00 36 20 | 30 67 77 81`: "20 30" with 20 value-open (20='fois' killed). 'pas': "pas [et/veut] le" (77=le provisional) parses. 'importe': "[20] importe" needs 20 nominal — ungranted. NOT.
7. @993 (a6_01) `24 89 48 01 76 49 24 26 | 30 03 60 67`: same ne-frame shape as @656. 'pas' parses. 'importe' ungranted as at @656. NOT.
8. @1114 (a6_07) `73 41 65 38 | 30 69 11 88 70`: "38 30" open. 'pas' parses. 'importe': no granted subject. NOT.
9. @1222 (a7_01) `92 61 24 48 | 30 09 20 57`: "24 48=e 30" (48='e' letter). 'pas': "24 e pas" parses (letter+pas, word boundary). 'importe': "24 e importe" — boundary, no forcing either way (elision-test checked). NOT.
10. @1251 (a7_02) `00 67 46 26 | 30 06 65 46 01`: "que 26 30 06 65 que" (46=que). 'pas': "que 26 pas 06 65 que" parses. 'importe': "26 importe" grammatical ONLY if 26 nominal — noun-26 is null (class open). Ungranted. NOT. ("30 06" one-word "importent" vs "pasent": boundary underdetermined per wordbound-30-06-importent; two-word parses under 'pas'.)
11. @1269 (a7_02) `46 69 88 24 | 30 20 64 47`: "24 30" finite verb + 30. 'pas' parses. 'importe': two finite verbs. NOT.
12. @1309 (a7_04) `43 77 74 52 | 30 92 44 00 36`: "le [74] [52] 30" gated on 74/52 (classes open). 'pas' parses. 'importe': subject needs 74/52 named — ungranted. NOT.
13. @1327 (a7_04) `08 62 98 56 | 30 06 62 94 70`: "56 30" open; gated on 62. 'pas': "pas 06 62 ne pre" parses. 'importe': "[62] [98] [56] importe" needs 62's class — ungranted. NOT.
14. @1368 (a7_06) `13 92 62 94 79 14 60 03 | 30 82 16`: ne-frame "ne tout 14 60 03 30" (79=tout). 'pas': "ne tout [14] [60] [03] pas" parses. 'importe': "ne ... importe" is not a French frame; the only granted subject candidate (79='tout') cannot bridge the open 14/60/03 span. NOT.
15. @1561 (a8_01) `40 17 11 26 | 30 06 60 71 50`: "e fois la [26] 30" (40=e, 17=fois, 11=la). Gated on noun-26. 'pas': "fois la [26] pas" parses. 'importe': "la [26] importe" grammatical ONLY if 26 nominal — ungranted. NOT.
16. @1702 (a8_06) `91 85 33 94 | 30 20 62 94 88`: the 'n'importe' anchor — sole stream 94-30 adjacency. 'importe': "n'importe" parses cleanly, elision-licensed. 'pas': "...33. Ne pas 20 62..." parses WITH a clause boundary at 33|94 — bracket-dependent but NOT forced false. NOT discriminating (bar requires FAIL under 'pas').
17. @1716 (a8_06) `12 06 29 40 65 94 44 59 | 30 64 47 68`: "n er e 65 ne [44] est 30 qui" (12=n, 29=er, 40=e, 94=ne, 59=est, 64=qui). 'pas': "ne [44] est pas qui" parses. 'importe': "est importe" = two finite verbs. NOT.
18. @1729 (a8_07) `98 39 88 24 | 30 15 01 56 30`: "24 30 ... 30". 'pas': "24 pas 15 01 56 pas" parses (two pas tokens, clause boundary). 'importe': "24 importe" = two finite verbs. NOT.
19. @1733 (a8_07) `30 15 01 56 | 30 06 60 12 48`: second 30. 'pas': "pas 15 01 56 pas" parses. 'importe': clause-initial "importe" without subject = ungrammatical. NOT.

Result: 0/19 windows fail under 30='pas'. The rival's best window (@1702) is bracket-dependent, not discriminating. No elision-forced consonantal window (77='le' never directly precedes 30; 94-30 adjacency unique to @1702). No granted-subject "importe" vehicle (confirms importe-30-subject-sweep). No word-formation discriminator ("30 06" boundary underdetermined per wordbound-30-06-importent).

## Per-clause results

1. >=1 discriminating window (fails under 'pas', parses under 'importe'): FAIL — 0/19.
2. Else-branch: APPLIES — 'importe' stays @1702-word-formation-confined; the rivalry is settled at battery level.

## Adverses (answered, not ignored)

- **"pas-30 stands promoted — adversarial re-test, not a re-vote":** CONFIRMED and respected. This battery does not re-vote the promotion; it tests only the bar's re-open condition (a discriminating window), which is not met. No downgrade, no standing verdict touched. The @1702 adverse fence from battery-pas-30 stands exactly as fenced.
- No red-team verdict touched. 94='ne' used with ratification-pending caveat. §7 respected (no polyvalence declared; 67 the sole polyvalence; all kills/splits/holds intact).
- Coordinated (not duplicated) with: importe-30-elision-test (phonology), importe-30-subject-sweep (finite-verb vehicle), wordbound-30-06-importent (boundary). All three nulls stand; this battery adds the adversarial value-level sweep they did not cover.

## Verdict

**null** — the adversarial sweep finds no discriminating window: 0/19 @30 windows fail under 30='pas'. Per the bar's else-branch, 'importe' stays @1702-word-formation-confined (stream-unique "n'importe" elision frame) and the pas/importe rivalry is SETTLED at battery level. Not a kill: @1702's 'n'importe' parse is clean and bracket-legitimate, so 'importe' remains a confined word-formation reading rather than a dead value.

## Follow-ups (null regenerates work; supervisor to queue)

1. `importe-gated-retest` (P2, gated on noun-26 / 62 / 74-52 resolving) — re-run this sweep's bars on @1251/@1561/@1327/@1309 once their gates clear: these are the only windows where a granted subject could ever make 'importe' parse. Bar: re-open 30's value iff >=1 then discriminates; else re-confirm confinement.
2. `importe-1702-singleton` (P3) — test whether the @1702 'n'importe' frame can ever grow beyond a singleton: sweep all 37 @94 windows for a second elision-licensed 94-30 adjacency under any value assignment consistent with standing verdicts; if none, record @1702 as a terminal singleton (strengthens confinement, bounds the rival permanently).
