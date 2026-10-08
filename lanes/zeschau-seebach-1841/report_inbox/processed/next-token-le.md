# Round-16 battery: le (77) — adverse dissolution, promotion adjudicated

Finder report: `code/crowd16/report_inbox/next-token-findings-le.md` (ingested 2026-10-07).
Status entering: 77="le" PROVISIONAL (load-bearing for A8/A13/A15). 84="on"
GRANTED-with-conditions (A15).

---

## PRE-REGISTRATION (locked before formal tests)

**Bar L0 ("le la" adverse):** DISSOLVED iff all three co-occurrences
re-derive with natural parses (cela-boundary @832; clause-boundary @1034;
article+pronoun @1042).

**Bar L1 (77="le" PROMOTE):** provisional → promoted iff (a) the adverse is
dissolved AND (b) ≥2 INDEPENDENT "le" legs on banked values AND (c) zero
unresolved contradictions. CAUTION: 77 is load-bearing — the bar is applied
strictly; conditional legs ("l'on" ×7, inherited from 84) do not count as
independent.

**Bar L2 (P1 84="fait" rival):** REJECTED iff it re-litigates the A15 grant
without new evidence AND its flagship windows don't parse. The 59-class
at @1190/@1448/@1804 is CHECKED against classification.json — if 59 is not
"est" there, the implications for A15's "on est" legs are recorded as a
correction, not buried.

---

## TESTS

`t = code/crowd16/next-token/test_le.py`.

| # | assertion | got |
|---|-----------|-----|
| 1 | n77 = 44 | |
| 2 | @832: P[828:838] = [1,24,87,11,77,76,59,35,56,17] (cela-boundary) | |
| 3 | @1034: P[1030:1042] (clause-boundary "le. La") | |
| 4 | @1042: P[1040:1048] = [17,77,82,63,11,67,76,85] (article+pronoun) | |
| 5 | @516: P[514:521] = [56,87,77,80,9,70,91] ("ce le [80]") | |
| 6 | @870: P[868:875] = [70,87,77,89,48,20,74] ("ce le [89]") | |
| 7 | 77-76 = [832,891,968] | |
| 8 | @1189: P[1186:1194] = [59,42,6,84,59,46,7,24]; 59@1190 class | |
| 9 | @1447: P[1445:1452]; 59@1448 class; @1803: P[1801:1808]; 59@1804 class | |
| 10 | 84-59-46 = [1189] (×1) | |
| 11 | 77-81 = [744,1240,1401,1598]; 81-87-11 = [1241,1402] | |
| 12 | 77-86 = [430,798,877,950,1133]; 86-29 = [431,1375,1391,1825] | |
| 13 | 06-77-76 = [890,967] (5-gram ×2) | |
| 14 | @1046: P[1044:1051] = [11,67,76,85,41,88,29] (76 tension) | |
| 15 | 77 follower top = {78:7, 84:7, 86:5, 81:4, 76:3} | |

---

## VERDICT

**L0 "le la" adverse — DISSOLVED (CONFIRM).** All three re-derived with
natural parses:
- @832 = [1,24,87,11,77,76,59,35,56,17]: 87-11="cela" (@830–831), then
  77="le" opens a new clause — "En cela, le [76] est [35]." No "la le".
- @1034: 80-77 = "[verb]-le" (object pronoun closing the clause), then
  "La première fois…" opens the next. Boundary parse clean.
- @1042 = [17,77,82,63,11,67,76,85]: "…fois. Le m[63] la [76]…" — "le
  [noun]" subject article + "la" object pronoun ("le ministre la [reçoit]"-
  shaped). Grammatical within one clause.
Zero "le/la" co-occurrences force ungrammatical French. The adverse that
kept 77 provisional no longer exists.

**L1 77="le" — PROMOTE.** Bar applied strictly (load-bearing):
(a) adverse dissolved ✓; (b) THREE independent "le" legs on banked values —
@516 "ce le [80]" (87="ce" banked), @870 "ce le [89]" (87 banked), @832
"En cela, le [76]" (87-11="cela" banked; article+noun slot — NOTE: 59@834
is LEFTOVER, not "est"; the leg is "le [76]", self-critique below) ✓;
(c) zero clean contradictions — @1031 "[inf] [80] le la" is fenced
(enclitic+break reading available), not a contradiction ✓.
Corroborating (not counted as independent): nominal follower diversity
(44 windows, top follower 7/44 — article-like spread) and the "l'on" ×7
(conditional on 84, C1-inherited). **77="le" PROMOTED** (provisional →
promoted). The load-bearing frames (A8, A13, A15-C1) get stronger.
Caveat (self-critique): @516/@870 lean on 80/89 verb-frames which are
conditional on 77="le" — the independent anchor is banked 87="ce" + the
"ce le" shape, not 80/89's verb status.

**L2 P1 (84="fait") — REJECTED.** Re-litigation of the A15 grant without new
evidence, and its flagships don't parse:
- @1189 = [59,42,6,84,59,46,7,24]: 06-84, not 77-84 — there is no "le" for
  "le fait est que".
- @1447/@1803 "qui le fait est [36/35]": ungrammatical (finder admits null
  on the parse).
- 59@1190/@1448/@1804 are ESTE, not "est" — "fait est" fails on the same
  ground as "on est" (see correction below).

**CORRECTION TO A15 (major — from the 59-class check):** The grant's
"84→59 ×4 (on est)" legs are VOID as "est" readings. Classification.json
(kill-grade ISLET-10):
- 59@1190 (from 84@1189): **ESTE** — "[06-84-59] que" 3-syllable -este verb
  + que-clause.
- 59@1291 (from 84@1290): **FENCED** ("[V-este] [35]" vs "la [17-84] est").
- 59@1448 (from 84@1447): **ESTE** — "qui le [84-59] [36]" ISLET-8 frame.
- 59@1804 (from 84@1803): **ESTE**.
The round-15 battery and red team never checked the 59-class on these legs
(scope gap, same species as the est-battery's ISLET-10 gap). **84="on"
STANDS but is WEAKENED:** it keeps all 59-independent legs ("qu'on en"×2
@309/@472, "mon"@166, "l'on"×7, 84→24 ×3) — the discriminating core is
intact — but loses the entire "on est" distributional family. **New tension
flagged for red team:** the ESTE verbs CONTAIN 84 ([06-84-59], [84-59] as
3-syllable verbs) — a verbal-syllable use of 84 conflicting with pronominal
"on". The 62/84 collision battery inherits this.

**P2 81 — masculine noun LEAD.** 77-81 ×4: @1086 "le [81] pour [33-INF]"
("le motif/moyen pour [inf]"), @1240/@1401 "le [81]. Cela" (exclusive
post-77, new-clause "cela"), @744/@1598 pre=67 "et/veut le [81]". 81's
"prin" reading dead per finder (kill record not re-verified here); 81 =
masculine abstract noun, LEAD (candidates motif/moyen/dessein — not named).

**P3 86-29 — substantivized-infinitive LEAD.** @430 "et/veut le [86]-er":
"veut"+"le"+bare-infinitive ungrammatical → 86-29 nominal ("le devoir/
pouvoir"-shaped). Converges with 86's INF-class + "par le [86]". LEAD.

**P4 76 gender — tension queued.** "le [76]" ×3 (@832/@891/@968) vs "la
[76]" @1046 ("…le m[63] la [76] [85]" — article+noun "la suite"? or pronoun
"la"+verb). 76 battery with red-team eyes; not a 77 problem (77="le" now
promoted; the tension is 76's).

**P5 06-77-76-01-98 ×2 — formula, queued** (@890/@968 byte-identical;
French not forced).

**P6 77-78-94-82 — not relitigated.** @1351 settled (round-10/11 triple-
collision); the 78-fork battery may re-examine the syllable parse, not the
verdict.

**Queued:** 81 noun battery; 86-29 substantivized check; 76 gender battery;
78-fork syllable parse @1180/@1351; 84 -este-verb tension (red team).
