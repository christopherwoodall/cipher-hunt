# Battery report: le-77 — claim 77="le"

Worker: 7b91f7ab-d9a1-4fc8-9293-d210bd53b453. Date: 2026-10-07.
Lock note: predecessor worker bd568942-0be6-48c2-a764-5f26092af237 created
locks/le-77.lock at 2026-10-08T04:22:06Z and died at the agent daemon restart
(~2026-10-08 04:26 UTC) before writing any report. No partial report exists.
This is a clean restart per protocol §6 (stale lock, proceed with note).

## Bar (verbatim from battery-queue.json)

"promote iff adverse windows re-parse cleanly + >=3 independent article frames + 44-window scan zero hard contradictions"

## Bar restated as numbered pass/fail clauses (fixed before testing)

- Clause 1: The adverse windows (@611 "47 77 87" 'ce le ce' strain; @1031 "80 77 11"
  '[verb] le la première') re-parse cleanly as grammatical French under 77='le'.
- Clause 2: At least 3 independent article frames for 77 exist in the stream.
- Clause 3: A scan of all 44 windows of 77 finds zero hard contradictions
  (no window that cannot parse under 77='le' with granted/pencil values).

## Method

Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt), parsed per code/side-keyhunt/repair_parse.py.
code/side-keyhunt/canonical.py NOT used. R5005 not touched.
@-offsets are 0-based stream indices (calibrated: 87-11 "cela" hits at
74/163/201/461/830/1242/1403 match the queue's cited offsets).
All 44 windows of 77 were extracted with ±4 and ±12 context and judged
against pencil ground truth (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que)
and granted values (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on,
47=ce allophone tier, 59=est provisional).

## Census

- 44 windows of 77. Follower diversity: 20 distinct followers; top followers
  78 x7 and 84 x7 (7/44 each, matches queue evidence). Top predecessors:
  06 x6, 67 x6, 88 x3, 64 x3, 17 x3, 87 x2, 47 x1.
- 77-11 occurs exactly once (@1033). 11-77 occurs once (@831, inside the
  @832 "87 11 77" = "cela le" window — the le-la-adverse misread, confirmed).

## Article frames (Clause 2 evidence)

- F1 "l'on": 77-84 x7 @145 @259 @1057 @1446 @1484 @1763 @1802.
  Includes "que l'on" (@1484: "46 77 84") and "qui l'on" x2 (@1446, @1802).
  A15-vetted; elided article, 'il' rival killed.
- F2 "le [78]": 77-78 x7 @7 @213 @647 @1077 @1180 @1351 @1542
  ("le ver[dict]"-shaped; 78='ver' is a queued lead, frame is article-shaped
  regardless).
- F3 "et le": 67-77 x6 @507 @639 @744 @1240 @1401 @1598 ("et le [81]" x4,
  "et le [62]" @507, "et le [89]" @639 with subject carried from prior clause).
- F4 "[verb]-ent le": 06-77 x6 @7 @207 @521 @790 @891 @968
  (verb + article + noun, e.g. @891 "86 06 77 76").
- F5 "ce le [verb]": 87-77-80 @516, 87-77-89 @870 (A8 frames:
  "ce le [80/89]" = subject "ce" + object "le" + verb — grammatical).
- F6 "le [81]": 77-81 x4 @744 @1240 @1401 @1598.
- F7 "le [86]": 77-86 x5 @430 @798 @877 @950 @1133
  ("le [86-INF]" = substantivized infinitive, "le pouvoir"-shaped).
- Further article+noun shapes: @647 "88 77 78", @677 "37 77 45"
  ("qui [37-verb] le [45]"), @721 "21 80 77 03" ("[80-verb] le [03]"),
  @798 "44 77 86", @877 "16 77 86", @950 "01 77 86", @968 "06 77 76",
  @1306 "43 77 74", @1542 "88 77 78", @1678 "74 77 44".

## Adverse windows (Clause 1 evidence)

### @611: "47 77 87 83 70 88" (0-based 611="47")
Wide context: "54 64 39 64 02 58 [47] 77 87 83 70 88 10 29 88 37 76 82".
Candidate parses under 77='le':
- "ce le cède" (87-83 = "cède", verb "céder" 3sg): "ce" as subject of a
  non-"être" finite verb is ungrammatical in French ("ce" governs "être";
  only fixed "ce faisant / ce disant" except). STRAINED.
- "se le cède" (47='se' rival): "céder" is not pronominal. STRAINED.
- "ce/se le céder" (87-83 = infinitive): "le céder" = "to yield it" is fine,
  but "ce/se" + "le céder" has no grammatical frame. STRAINED.
- "ce/se le ce de pré..." (87='ce', 83='de'): "ce de" never grammatical. FAILS.
- "celui de" (47-77-87 = "celui"): needs 77='l', 87='ui' — contradicts granted
  values; too expensive. REJECTED.
- Single-token rivals for 77 ("ne", "les", "que", "qui", "en", "y") all fail:
  the strain is "ce...ce de", not the "le". The finder's "cheapest revision
  77!='le' there" is NOT the cheapest — the break localizes to 47/87/83.
Result: NO clean re-parse. Fenced as genuine residual strain, cause stated.

### @1033: "29 80 77 11 70 82 34 29 40 17" ("80 77 11" = "[80] le la")
Wide context: "87 01 03 29 80 [77] 11 70 82 34 29 40 17 77 82 63 11 67".
"77 11 70 82 34 29 40" = "le la pre m i er e" = "le la première".
Candidate parses:
- Clause boundary "…[80] le. La première fois, …": needs "80 77" to parse.
  Only grammatical option is imperative + pronoun ("[80-IMP]-le", e.g.
  "faites-le"). But A8 locks 80 as infinitive-shaped here ("29-80" post-'er'
  frame), and splitting "03-29"+"80" to free 80 for imperative leaves
  "87 01" = "ce [01]" unparsed (01 n=28, no clean "ce [01]" frame found).
  STRAINED, not clean.
- "[80-INF] le" (pronoun after infinitive): ungrammatical. FAILS.
- "le la" as article+article: ungrammatical. FAILS.
- 77 rivals ("l'" before vowel — 11='la' is consonant-initial; "les"): fail.
Result: NO clean re-parse. Fenced as genuine residual strain, cause stated.

### Le-la dissolution re-confirmed (supporting, not part of this bar)
- @832 (77 at 0-based 832): "01 24 87 11 [77] 76 59 35" =
  "[01] en cela, le [76] est [35]" — "in that, the [76] is [35]". CLEAN.
  (The old "@832 misread" was "87-11-77" read as "le la"; it is "cela le".)
- @1041 (77 at 0-based 1041): "…29 40 17 [77] 82 63 11…" =
  "la première fois. Le [82-63…]" — new-sentence subject article. SOFT
  (82-63 word shape unresolved, same fence as the old verdict).
- @1158 (77 at 0-based 1158): "…80 17 [77] 82 44…" = "[80] fois. Le m[44…]" —
  same subject-article parse. SOFT.

## Other non-clean windows (Clause 3 evidence)

- @790: "84 06 [77] 64 46" = "on [06] le qui que". "le qui" is ungrammatical
  under granted values (64='qui'). No clean parse ("ne le [verb]" needs
  ungranted 12-48='ne'; imperative split needs a sentence boundary after
  "on", impossible). HARD STRAIN, fenced.
- @521: "91 [77] 06" = "[91] le [06]" — clean only if 06 is nominal; 06's
  value is open (ent-06 battery queued). SOFT, fenced.
- @1077 / @1351: "48 [77] 78" = "[48] le [78]" — article shape intact ("le
  [78]"); preceding 48 unclear. SOFT, fenced. (Note: "77-78" = "le-ver" may
  alternatively be the word "lever"/"élever" spanning the boundary — syllabic
  parse; value 'le' unaffected.)
- @1216: "36 [77] 83" = "[36] le [83]" — clean only if 83 is nominal/verbal
  ("le dire"-shaped); 83='de' is a lead (98-83 x5 "vient de"), not granted.
  SOFT, fenced to the open 83 value.
- @453: "79 17 [77] 60" = "toutefois, le [60]" — CLEAN (new clause).
- @639: "60 67 [77] 89" = "[60]… et le [89]" — CLEAN ("et le [verb]", subject
  carried). @677, @721, @1180 verb+"le"+noun — CLEAN.
- @145/@259/@1057/@1446/@1484/@1763/@1802 "l'on" frames — CLEAN.

## Per-clause verdicts

- Clause 1 (adverse windows re-parse cleanly): FAIL. @611 and @1033 admit no
  clean parse under 77='le' with granted values; both fenced with stated
  cause (strain localizes to neighboring tokens 47/87/83 and to 80's
  infinitive/imperative fork, not to 77 itself).
- Clause 2 (>=3 independent article frames): PASS. Seven independent frame
  families (F1–F7 above), including 7x "l'on", 7x "le [78]", 6x "et le",
  6x "[verb]-ent le", 2x "ce le [verb]".
- Clause 3 (44-window scan, zero hard contradictions): FAIL at strict
  reading. @611, @1033, @790 do not parse; @521, @1041, @1077, @1158,
  @1216, @1351 are soft (fenced to open neighbor values).

## Verdict: NULL

Not promote: Clause 1 and Clause 3 fail — the two named adverses do not
re-parse cleanly. Not kill: no window forces 77≠'le' globally; the
distributional case is strong (44 windows, 20 distinct followers, top 7/44,
seven article-frame families, zero rival value demonstrated on the same
frames); both hard strains localize to neighboring tokens (47/87/83 at
@611; 80 at @1033), not to 77. The claim stays PROVISIONAL per §7; A8/A13/A15
keep their conditional status.

## Follow-up targets (null regenerates work)

### FU1 id "le611-reparse" — claim: "@611 re-parses under 77='le'"
- claim: "@611 '47 77 87 83 70' admits one grammatical French parse with 77='le'"
- bars: "resolve iff ONE parse is grammatical with <=1 non-granted value
  assumption; else confirm as genuine residual"
- evidence: "best candidates 'ce/se le cède' strained ('ce'+non-être verb;
  'céder' non-pronominal); strain localizes to 47/87/83, not 77; 87-83 =
  'cède/cédé/céder' verb readings untested"
- adverses: "may confirm residual; 47='se' rival (frame-qui-47) and 83='de'
  lead interact"

### FU2 id "le1033-imperative" — claim: "@1033 '80 77' = imperative + 'le'"
- claim: "@1033 parses as '[03-er]. [80-IMP]-le | La première fois,…' with
  77='le'"
- bars: "resolve iff 80-imperative parses consistently with A8's infinitive
  frames (inflectional, not lexical, polyvalence per §7) AND '87 01' left
  context parses; else confirm residual"
- evidence: "'29-80' infinitive frames (A8) vs '03-29'+80 split; 'la première
  fois' clause boundary is natural; imperative+'le' is the only grammatical
  '[verb] le' order"
- adverses: "§7 polyvalence rule (67 sole true polyvalence) may block;
  '87 01' = 'ce [01]' currently unparsed"

### FU3 id "le83-window" — claim: "83 takes a value making @1216 'le [83]' parse"
- claim: "83 has one value under which @1216 '36 77 83' = '[36] le [83]'
  parses ('le dire'-shaped)"
- bars: "resolve iff ONE 83 value parses both 'le [83]' (@1216) and 98-83 x5
  ('vient de'); else fence 83 as the blocker, not 77"
- evidence: "@1216 '[36] le [83]'; 83 n=15; 'de' lead from 98-83 x5
  (vient-parvenir formula); 83 followers 82 x3 / 21 x3 / 86 x2"
- adverses: "'de' lead vs article frame pull opposite ways; 83 value is open"

## Constraints respected

77="le" stays PROVISIONAL; no promotion recorded beyond this battery verdict.
R5005, sealed gates, and the red-team adjudication queue untouched. No
existing verdict downgraded (le-77 was queued). This null does not contradict
any standing red-team verdict (77='le' was never red-team granted).
