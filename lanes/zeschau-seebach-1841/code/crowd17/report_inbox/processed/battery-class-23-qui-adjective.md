# Battery report: class-23-qui-adjective

- Target id: `class-23-qui-adjective`
- Claim: "decide 23's class (n=8, sits between 'qui' and the adjective at @181-187)"
- Date: 2026-10-09
- Worker: battery worker (subagent bec06897-af37-43a7-890c-73f160769eb3)
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
  `data/upstream-ct_R5005.txt`, parsed like `code/side-keyhunt/repair_parse.py`;
  n=1847 asserted, 96 types asserted). All @-offsets are 0-based repaired-stream
  indices. `canonical.py` never used. R5005 not touched. Sealed gates and the
  red-team adjudication queue not touched.
- Lock: `code/crowd17/next-token/locks/class-23-qui-adjective.lock` (created at
  start, deleted on completion; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"state 23's class with byte evidence; <=10% orphan across 23's 8 windows"

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1) One class for 23 is stated with byte evidence.
2. (C2) At most 10% of 23's 8 windows are orphaned under the stated class
   (i.e., zero orphans: 1/8 = 12.5% exceeds the bar).

## Method

1. Re-derived the repaired parse in-session; asserted 1,847 pairs / 96 types.
   Censused 23: n=8 at 0-based indices [136, 182, 679, 1056, 1552, 1609, 1697,
   1782]. (The queue's "@181-187" gloss refers to the formula window whose
   23 sits at @182; pairs @181-187 = 64 23 37 06 00 33 16.)
2. Applied standing verdicts as constraints (never downgrade, never
   contradict-and-overwrite):
   - 64=qui (granted, §7); 45=ce (granted); 46=que, 11=la, 96=par, 00=pour,
     82=m (banked/granted); 47=ce (promoted, allophone tier); 84=on (promoted);
     65=noun class (R18 banked); 59=est (provisional); 77=le (provisional).
   - 23~26 SPLIT granted (A2): 23 and 26 are distinct values (successor
     p=0.0029). Respected throughout; 23≠26.
   - 37 = predicative adjective (A1 grant; verb-stem class DISTRIBUTIONALLY
     EXCLUDED at kill grade, qui37-rival-values; re-confirmed for @183 by
     battery-class-37-06-185 PROMOTE 2026-10-09).
   - Post-qui slot is verb-position by construction: battery-qui-2326-prefix
     PROMOTE ("A relative clause requires a finite verb after 'qui'") and
     battery-noun26-encequi-triple PROMOTE ("23 = 'the other verb (value
     open)'" in the "24 87 64 23/26 37" formula triple).
   - 98='vient' battery-promoted (vient-98-name; survives the 14-verb fence
     per vient-98-894-reaudit). Its 'revient' rival was KILLED ('pré-revient'
     is not a word, @236); the formula "98 83 82 96 21" holds x3
     byte-identical (@227/@1060/@1783), including our @1783 window.
   - §7: 67 et/veut is the sole true polyvalence — no second polyvalence
     declared at battery level.
3. Tested candidate classes (verb, adverb, pronoun, determiner, noun,
   adjective, preposition) window by window. "Orphan" = the window FORCES the
   class false (kill-grade structural contradiction), not mere strain.

## Window-level evidence (bytes, 0-based)

| # | @ | row | -4..+4 window | pre | fol |
|---|---|-----|---------------|-----|-----|
| W1 | 136 | a1_04 | 56 64/qui 21 65 [23] 91 65 13 66 | 65 (noun-cl) | 91 |
| W2 | 182 | a1_05 | 14 24 87/ce 64/qui [23] 37 06 00/pour 33 | 64=qui | 37 (pred-adj) |
| W3 | 679 | a5_00 | 64/qui 37 77/le? 45/ce [23] 09 07 00/pour 92 | 45=ce | 09 |
| W4 | 1056 | a6_04 | 29 74 74 45/ce [23] 77/le? 84/on 09 98 | 45=ce | 77=le? |
| W5 | 1552 | a8_00 | 12 94 92 45/ce [23] 99 13 93 61 | 45=ce | 99 |
| W6 | 1609 | a8_02 | 39 11/la 92 65 [23] 08 55 83 71 | 65 (noun-cl) | 08 |
| W7 | 1697 | a8_06 | 24 85 58 15 [23] 91 85/vstem 33 94 | 15 | 91 |
| W8 | 1782 | a8_09 | 19 48 74 65 [23] 98 83 82/m 96/par | 65 (noun-cl) | 98='vient' |

Predecessor census: 65 x3, 45 x3, 64 x1, 15 x1. Successor census: 91 x2,
37/09/77/99/08/98 x1.

### Class elimination

- **W2 (@182) forces finite-verb class.** The frame is "…ce(87) qui(64) [23]
  [37ent-adjective] pour(00) [33-inf]…". A relative clause after "qui"
  requires a finite verb in the [23] slot (qui-2326-prefix, PROMOTE). 37
  cannot be the verb (verb-stem class killed at kill grade; adjective
  PROMOTEd at this exact window by class-37-06-185). "qui 23" as one word
  is barred by granted 64='qui'. Therefore every surviving class hypothesis
  must be finite-verb-compatible at W2.
- **Noun / adjective / determiner / pronoun / preposition / adverb: all die
  at W2.** Each leaves "qui [X] [37ent-adjective]" with no finite verb —
  ungrammatical in 1841 French. (Parent L2 suggested testing adverb vs
  pronoun vs determiner; all three fail at W2 for this reason.)
- **Verb is the ONLY class that parses W2.** It is additionally FORCED
  there by two standing promotes ("the other verb" in the formula slot).

### Verb-class at the remaining seven windows

- W1 @136: "…qui(64) 21 65(noun-cl) [23] 91 65…" — "[65-subject] [23-verb]
  [91-object]" skeleton parses; "qui 21" relative-clause attachment is
  strained but forces nothing. COMPATIBLE (no forced contradiction).
- W3 @679: "…qui 37 [le] ce(45) [23] 09…" — "ce [23-verb] [09]" = "ce" +
  finite verb + object, clean. COMPATIBLE.
- W4 @1056: "…ce(45) [23] 77(le?) 84(on) 09 98…" — "ce [23-verb] le; on [09]
  vient…" parses with 09 as adverb. COMPATIBLE.
- W5 @1552: "…ce(45) [23] 99…" — "ce [23-verb] [99]". COMPATIBLE.
- W6 @1609: "…[92] 65(noun-cl) [23] 08…" — S-V-O skeleton. COMPATIBLE.
- W7 @1697: "…[15] [23] 91 85(vstem)…" — "[15-subject] [23-verb]
  [91-object]"; the trailing verb-stem 85 belongs to a following word.
  COMPATIBLE.
- **W8 @1782: FORCED ORPHAN for verb-class.** "…74 65(noun-cl) [23] [98]
  83 82/m 96/par…" with standing 98='vient' (finite, battery-promoted; the
  @1783 window is a clean leg of the x3 byte-identical "98 83 82 96 21"
  formula). Two adjacent finite verbs ("[noun] [23-verb] [vient]") are
  ungrammatical. Exhausted rescues, all rejected:
  - Clause boundary between 23 and 98: "vient" would need an overt subject;
    1841 French has no pro-drop. REJECTED.
  - Asyndetic coordination ("[65] [23] et [98]"): rhetorical, not diplomatic
    prose; no "et" present. REJECTED.
  - 23 as non-finite verb form ("[noun] [23-inf/part] vient"): no French
    construction licenses infinitive/participle + finite "vient" in this
    order. REJECTED.
  - "23 98" = one word "revient": contradicts the standing vient-98-name
    PROMOTE twice over — @1783 is its formula leg, and 98='revient' was
    explicitly KILLED ('pré-revient' is not a word, @236). A battery cannot
    overturn this; it is red-team venue. FENCED, not adopted.
  - 98 as noun/direct object: no positive byte evidence; would downgrade
    the standing promote. REJECTED at battery level.
  - 23 as adverb ("[noun] [23-adv] vient") or resumptive pronoun: parses
    W8 cleanly but DIES at W2 (no finite verb in "qui [adv] [37ent]").
    These are the two arms of the fenced split, not a uniform class.

Score: verb-class holds 7/8 windows (87.5%), with W2 forced and W1/W3–W7
compatible — but W8 is a forced orphan: **1/8 = 12.5% > 10%**.

## Per-clause pass/fail

- **C1 (state 23's class with byte evidence): FAIL as a uniform statement.**
  Verb-class is the unique surviving class (forced at W2, compatible at six
  more windows), but it does not hold at W8, so no single class can be
  honestly stated. The accurate statement is a fenced split: verb at 7/8
  windows; W8 requires a non-verb parse (adverb arm) or a re-segmentation
  ("23·98" one word / 98≠'vient' at @1783 — both red-team venue, since they
  touch the standing vient-98-name promote and the §7 sole-polyvalence law).
- **C2 (≤10% orphan): FAIL.** 1 forced orphan / 8 windows = 12.5%,
  exceeding the 10% bar. The bar was pre-registered and is not rewritten
  after seeing data.

No standing red-team verdict is contradicted: the 23~26 split (A2) is
respected (23≠26 kept distinct); the formula-slot verb reading of 23
(qui-2326-prefix, encequi-triple) is confirmed, not weakened; vient-98-name
is left intact.

## Verdict

**null** — 23's class is not uniformly decidable on current standing
evidence. Verb-class is established at 7/8 windows (forced at the @182
post-qui slot by two standing promotes; compatible at @136/@679/@1056/
@1552/@1609/@1697) but W8 @1782 ("65 23 98-vient") forces a non-verb parse
under the standing 98='vient' promote, orphaning 1/8 = 12.5% of windows
against the ≤10% bar. Every non-verb class dies at W2. The working account
is a FENCED SPLIT — verb at 7/8, W8 = adverb-arm or "23·98" re-segmentation
— packaged below and for the red-team docket (it implicates the vient-98
formula leg at @1783 and the §7 sole-polyvalence law).

## Follow-up targets (null mandate)

1. **`reseg-23-98-1782`** (priority 2): adjudicate @1782–1783. Discriminate
   with byte evidence: (a) 23=adverb — "[65-noun] [23-adv] vient de…"
   (clean, breaks no standing verdict; check 23's other windows for an
   adverb-compatible value); (b) "23 98" one word ("revient") — note this
   overturns vient-98-name's @1783 formula leg and its explicit 'revient'
   kill, so it needs red-team adjudication and new morphological evidence,
   not just a re-read; (c) 23=finite + clause boundary (expected KILL: null
   subject for "vient"). Bar: one grammatical parse named with byte
   evidence; any parse that downgrades a standing promote is escalated,
   not adopted.
2. **`verb-23-value`** (priority 3): value battery for 23 on the seven
   verb-windows. Discriminate: "concerne"/"regarde" (existing value lead
   from the formula window) vs "rendre"-shaped transitive (W2 reads "qui
   [23] [37ent-adj] pour [33-inf]") vs copula-shaped (formula slot-1
   parallels provisional 59='est'). Discriminating frames: "ce 23 X" x3
   (@679/@1056/@1552), "65 23 X" x2 (@136/@1609), 23→91 x2 (@136/@1697),
   23→09/08 (@679/@1609).
3. **`adv-23-uniform`** (priority 4): close the adverb arm properly. Uniform
   adverb class must dissolve W2's verb-forcing: test the "64 23" one-word
   rival ("qu'il"/"qu'on"-shaped) at @181–182 with morphological and
   distributional evidence. Expect KILL at W2 (granted 64='qui' blocks
   re-segmentation; escalation to red team if pursued) — a clean kill here
   confirms the fenced split in follow-up 1's arm (a).

## Traceability

- Census script logic: repaired parse per `code/side-keyhunt/repair_parse.py`;
  23-indices [136, 182, 679, 1056, 1552, 1609, 1697, 1782] re-derived
  in-session from `code/side-keyhunt/repaired_offsets.json` (1,847 pairs).
- Standing inputs: `code/crowd17/report_inbox/processed/battery-qui-2326-prefix.md`,
  `battery-noun26-encequi-triple.md` (via REPORT.md F95),
  `code/crowd17/report_inbox/battery-class-37-06-185.md`,
  `code/crowd17/report_inbox/processed/battery-vient-98-name.md`,
  `code/crowd17/report_inbox/battery-vient-98-894-reaudit.md`,
  `code/crowd17/report_inbox/processed/battery-thirds-60-68-pair.md`
  (23~26 split yardstick p=0.0029).
