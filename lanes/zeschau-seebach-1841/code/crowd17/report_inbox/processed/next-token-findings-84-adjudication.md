# Finder report: 84-adjudication inputs (62/84 "on" collision)

Date: 2026-10-08. Beat: wave-2 `84-adjudication inputs`.
Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed like
`code/side-keyhunt/repair_parse.py`). Never canonical.py. Never R5005.

Purpose: INPUT beat for the queued `collision-62-84` battery (priority 1,
running concurrently). This report gathers window-level profiling evidence.
It does NOT claim the resolution. It complements the battery's re-derivation
with profiling detail the battery can cite.

Offsets: lane @-convention (report @ = 0-based stream index − 1; verified
against A15's 77-84 list and the Q1 @309/@472 windows).

Standing inputs respected: 84="on" is an A15 grant with conditions C1–C3;
62="on" is a standing STRONG LEAD, not a grant; 62's rival value is "il";
94="ne" is promotion-track (not yet promoted); 77="le" is provisional;
59="est" is provisional; 48="est"/"ne"/"de" are killed; 12="n"/48="e" letter
battery is queued.

## Headline findings

1. **@507 ("21-67-77-62-94-64-98") is the single kill-grade discriminator.**
   The trigram 77-62-94 reads "l'on ne" cleanly iff 62="on". Under 62="il"
   it reads "le il ne", which has no clean French parse ("l'il" is not a
   standard elision). This is the only 62 window that resists "il" at this
   grade. Conditional on 77="le" (provisional) and 94="ne" (promotion-track).
2. **Zero crossover re-derived on the repaired stream:** 62->94 x9 vs 84->59 x4,
   with 62->59 x0 and 84->94 x0. The two rivals never compete for the same
   follower slot.
3. **Slot split, not free competition:** 62's "on" lives in the pre-"ne"
   subject slot (62-94 x9; 62-61-59 x1 "n'est"-shaped at @445); 84's "on"
   lives in the post-clitic elision slot (77-84 x7 "l'on"; 46-84 x2 "qu'on").
   The 62-94-79-14-60 x2 formula and the 84-59-35-94-52 x2 formula tail
   de-duplicate to one frame each (see dedupe section).
4. **@1188 ("06-84-59") is a conditional kill trigger against unconditioned
   84="on":** under 84="on" it forces 06 to be clause-final, adverbial, or
   subject-shaped ("[06], on est" / "[adv] on est"). If the queued 06 battery
   promotes 06="en", @1188 breaks ("en on est" is bad).
5. **@390 ("36-62-91-84-73") holds BOTH rivals** ("62-91-84"): under
   {62="on", 84="on"} it stacks two "on" syllables two apart ("on 91 on");
   under {62="il", 84="on"} the distribution is cleaner ("il 91 on"). Mild
   evidence for split values; depends on 91.
6. **"il ne" x9 is fully clean:** no 62-94 window resists "il" on the bigram
   itself. The "il" rival dies or lives on left-context frames (@507), not on
   the 62-94 bigram.
7. **Stale counts corrected:** the queued `frame-20-62-94` target says
   "20 62 94 x3 (@760...)" — on the repaired stream 20 precedes 62 x4, of
   which x3 are the 20-62-94 trigram (@759, @838, @1702, report @ of the 20)
   and x1 is 20-62-98 (@1135). The queued `nest-subject-86-62-42` target cites
   "@762 '62 n'est 39'" — that window is @760 on the repaired stream
   ("20-62-94-59-39"); its offset predates the a5_03 repair.

## Census: 62 (35 occurrences)

Followers: 94 x9 | 48 x6 | 98 x5 | 16 x4 | 06 x2 | 61 x2 | 96, 91, 21, 18,
38, 46, 93 x1.
Predecessors: 21 x5 | 20 x4 | 74 x3 | 93, 03, 08, 78, 92 x2 | 30, 51, 36, 14,
10, 77, 40, 04, 06, 34, 02, 98, 41 x1.

| @ | pre | foll | window (±3) |
|---|---|---|---|
| 10 | 93 | 98 | 78-18-93-62-98-76-45 |
| 45 | 30 | 96 | 43-81-30-62-96-00-92 |
| 81 | 51 | 16 | 42-98-51-62-16-14-06 |
| 99 | 21 | 94 | 85-08-21-62-94-93-59 |
| 359 | 21 | 48 | 47-11-21-62-48-76-47 |
| 388 | 36 | 91 | 43-91-36-62-91-84-73 |
| 424 | 14 | 48 | 29-47-14-62-48-76-42 |
| 445 | 10 | 61 | 78-41-10-62-61-59-32 |
| 507 | 77 | 94 | 21-67-77-62-94-64-98 |
| 657 | 03 | 16 | 26-30-03-62-16-00-86 |
| 664 | 03 | 06 | 50-80-03-62-06-00-20 |
| 760 | 20 | 94 | 29-40-20-62-94-59-39 |
| 801 | 74 | 98 | 86-44-74-62-98-53-69 |
| 839 | 20 | 94 | 17-98-20-62-94-26-12 |
| 848 | 40 | 21 | 33-96-40-62-21-67-91 |
| 944 | 08 | 98 | 50-40-08-62-98-96-86 |
| 1064 | 21 | 18 | 82-96-21-62-18-70-39 |
| 1135 | 20 | 98 | 77-86-20-62-98-00-98 |
| 1140 | 78 | 16 | 00-98-78-62-16-29-42 |
| 1296 | 04 | 16 | 52-80-04-62-16-02-70 |
| 1314 | 74 | 48 | 00-36-74-62-48-98-15 |
| 1323 | 08 | 98 | 29-80-08-62-98-56-30 |
| 1328 | 06 | 94 | 56-30-06-62-94-70-52 |
| 1348 | 34 | 48 | 66-73-34-62-48-77-78 |
| 1361 | 92 | 94 | 35-13-92-62-94-79-14 |
| 1453 | 92 | 61 | 33-46-92-62-61-21-67 |
| 1463 | 21 | 48 | 17-01-21-62-48-21-02 |
| 1467 | 02 | 38 | 48-21-02-62-38-26-12 |
| 1481 | 98 | 46 | 82-16-98-62-46-77-84 |
| 1535 | 41 | 06 | 66-73-41-62-06-21-62 |
| 1538 | 21 | 93 | 62-06-21-62-93-88-77 |
| 1568 | 74 | 48 | 29-24-74-62-48-56-32 |
| 1685 | 93 | 94 | 65-13-93-62-94-79-14 |
| 1703 | 20 | 94 | 94-30-20-62-94-88-26 |
| 1771 | 78 | 94 | 26-37-78-62-94-24-87 |

## Census: 84 (25 occurrences)

Followers: 59 x4 | 24 x3 | 02, 92, 09 x2 | 29, 26, 53, 74, 91, 73, 51, 06,
79, 33, 78, 64 x1.
Predecessors: 77 x7 | 66, 89, 46, 53 x2 | 82, 91, 65, 48, 06, 17, 32, 74,
11, 94 x1.

| @ | pre | foll | window (±3) |
|---|---|---|---|
| 145 | 77 | 29 | 67-64-77-84-29-87-64 |
| 153 | 66 | 26 | 47-46-66-84-26-35-58 |
| 166 | 82 | 53 | 11-24-82-84-53-12-48 |
| 259 | 77 | 74 | 32-43-77-84-74-45-93 |
| 275 | 89 | 91 | 33-29-89-84-91-37-61 |
| 309 | 46 | 24 | 20-17-46-84-24-37-78 |
| 390 | 91 | 73 | 36-62-91-84-73-34-67 |
| 411 | 53 | 51 | 01-02-53-84-51-37-78 |
| 472 | 46 | 24 | 06-67-46-84-24-37-78 |
| 787 | 65 | 06 | 94-74-65-84-06-77-64 |
| 856 | 48 | 02 | 64-32-48-84-02-24-49 |
| 1020 | 53 | 92 | 66-91-53-84-92-64-45 |
| 1057 | 77 | 09 | 45-23-77-84-09-98-83 |
| 1150 | 66 | 02 | 67-33-66-84-02-00-92 |
| 1188 | 06 | 59 | 59-42-06-84-59-46-07 |
| 1289 | 17 | 59 | 00-11-17-84-59-35-94 |
| 1377 | 89 | 92 | 86-29-89-84-92-69-13 |
| 1417 | 32 | 79 | 34-52-32-84-79-15-33 |
| 1446 | 77 | 59 | 37-64-77-84-59-36-67 |
| 1484 | 77 | 
...[truncated 6948 chars]