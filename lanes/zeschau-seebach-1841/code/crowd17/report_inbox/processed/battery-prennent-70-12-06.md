# Battery report: prennent-70-12-06 — test the souvent parse's left edge

Worker: 565319b3-635d-4425-888b-286bd307924a | 2026-10-09T02:19:56Z–02:35Z
Target: `prennent-70-12-06` (priority 2). Lock
`locks/prennent-70-12-06.lock` created on start, deleted on completion. No
prior lock existed.

## Bar (verbatim, pre-registered)

"'11 88 70 12 06' parses as (plural NP) + 'prennent' with subject agreement,
or fence with stated cause"

Numbered clauses (fixed before verdict; bar text unmodified):
- C1: "11 88 70 12 06" @1116–1120 parses as (plural NP) + "prennent" with
  subject agreement. PASS iff "11 88" is a grammatical plural NP and agrees
  in number with the 3rd-plural verb under standing values.
- C2 (else-branch): the left edge is fenced with stated cause. PASS iff the
  fence names the blocking facts under standing values, answers the listed
  adverses, and invents no values.

## Method

Repaired 1,847-pair stream only:
`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`, parsed per
`code/side-keyhunt/repair_parse.py` (1,847 pairs verified; `canonical.py`
never used). R5005 untouched. @-offsets are 0-indexed pair positions (queue
convention). Standing values used: 11=la (banked), 70=pre (banked), 82=m,
29=er (pencil); 12=n, 48=e (promoted letters); 06=ent (promoted);
30=pas, 00=pour (promoted); 59=est, 77=le (provisional). 1841 diplomatic
French throughout.

Standing battery correction carried in (not re-litigated): the ent-06
battery refuted "prennent" as stated — 70-12-06 = "pre"+"n"+"ent" =
"prenent", one 'n' short of "prennent"; it reads "prennent" only under the
unproven clerk single-n spelling (queued as `spell-single-consonant`, P3).
The verb half of this target's claim is therefore CONDITIONAL, not
established. The 3rd-plural -ent marking itself is not in doubt.

## Window evidence (@1116–1120, row a6_07, row-relative 3–7)

Full local row a6_07 (@1113–1132):
`38 30 69 | 11 88 70 12 06 | 14 06 | 11 52 37 43 00 86 52 37 86 | 24 …`
Under standing values:
`[38] pas [69] | la [88] pre-n-ent | [14]-ent | la [52] [37] [43] pour [86] [52] [37] [86] | [24]…`

Distributional facts (all re-derived on the repaired stream):
- "11-88" bigram: UNIQUE on the stream (@1116). No corpus support for
  "la [88]" as any construction, plural or otherwise.
- "69-11" bigram: UNIQUE on the stream (@1115) — the word-internal-"la"
  adverse has exactly one locus to live or die at.
- n(88) = 23 (@42/@86/@210/@304/@306/@334/@402/@497/@513/@616/@619/@646/
  @730/@765/@904/@1049/@1117/@1260/@1267/@1514/@1541/@1706/@1727).
  Predecessors: 39 x2, 69 x2, 20 singles (24,06,50,89,02,88,54,45,79,65,70,
  29,61,48,16,41,11,81,93,94). Successors: 77 x3, 11 x2, 24 x2, 18 singles.
- 88's class profile (adverse 1 — "88's class open"): noun-LEANING but not
  decided. Noun frames: "79-88" @496 ("tout [88]", 79=tout promoted);
  "59-39-88" @764–765 ("est à [88]", 59=est provisional, 39=a/à promoted);
  "88-77" x3 (@86/@646/@1541 — "[88] le", 77=le provisional). Verb-shaped
  contact: "94-88" @1705 ("ne [88]"); "70-88" x1 @615 ("83-70-88-10-29" —
  possibly word-internal "pre[88]", e.g. "premier"-shaped). No pronoun
  ("ils/elles") signal anywhere. Class stays OPEN — adverse fenced, not
  answered.
- n(69) = 12; followers: 26 x3, 13 x2, 24 x2, 88 x2, 14, 11, 74, 64.
  "69-11" = "cela"-shaped word needs 69="ce"-class — ungranted and
  untestable on this profile. Adverse 2 ("'la' may be word-internal")
  fenced, not answered.

## Subject-agreement test (C1)

The verb "pre-n-ent" is plural-marked (3rd-plural -ent, promoted). Its
subject must be 3rd-plural. The candidate subject in the claim is "11 88":
- 11 = "la" is BANKED (pencil ground truth): feminine SINGULAR article.
- A singular article cannot head a plural NP in French. No standing value
  allows 11 to be plural; re-reading 11 is not available.
- Rescue candidates, all closed:
  - "la [88]" with plural 88: article-noun number mismatch — ungrammatical
    regardless of 88's class. DEAD.
  - "l'[88]" elision: 88 is not shown vowel-initial, and "l'" is still
    singular. DEAD.
  - Collective-noun 88 ("la [majorité]"): French collectives take SINGULAR
    agreement ("la majorité prend"), never "prennent". DEAD.
- Therefore the window FORCES the claim false: under standing values
  "11 88" cannot be a plural NP agreeing with the plural-marked verb.

The two live alternatives both sit OUTSIDE the claim's parse and are
fenced, not demonstrated:
- (a) "la" word-internal: "[69-11]" as one word ("cela"-shaped) + 88 alone
  as the plural subject. Needs 69="ce"-class (ungranted). Single locus
  @1115. FENCED.
- (b) 88 alone as plural subject ("[ils] prennent souvent la…"):
  grammatical French, but 88's class is open with a noun-leaning profile
  and zero pronoun signal. FENCED.

## Per-clause pass/fail

- C1 (plural NP + "prennent" with subject agreement): FAIL AT KILL GRADE.
  The window forces the claim false: 11="la" (banked, singular) cannot head
  a plural NP, and no plural-NP reading of "11 88" is grammatical under
  standing values. The verb half is additionally conditional on the queued
  clerk-single-n spelling (ent-06 correction).
- C2 (fence with stated cause): PASS. Fence stated above: (1) banked
  singular "la" vs plural-marked verb — forced mismatch; (2) verb surface
  is "prenent", "prennent" conditional on unproven spelling hypothesis;
  (3) adverses fenced with cause — 88's class open (profile gathered,
  noun-leaning, no pronoun signal), "la"-word-internal needs ungranted
  69="ce"-class at the unique @1115 locus.

## Verdict

**kill.** The stated parse — "'11 88 70 12 06' as (plural NP) +
'prennent' with subject agreement" — is forced false at @1116–1120 under
standing values. No standing verdict is contradicted or downgraded:
breaker-b4-1121's null verdict fenced exactly this left edge to this
target; the ent-06 "prenent" correction is cited, not re-litigated; no
red-team verdict touched; R5005 and sealed gates untouched. The souvent
parse's CLAUSE ("…prenent souvent la…") is not killed by this verdict —
only its subject-agreement reading as stated; the verb's subject remains
an open left-edge question.

Note for the sibling lanes (souvent-14-06-retest @84, le-14-kill-1121):
neither is duplicated or blocked by this work. If "souvent" is killed at
@84 or 14='le' promotes, the subject question at @1117 re-opens under the
new frame — the fenced alternatives (a) and (b) above are the re-entry
points.

## Follow-ups (left edge stays open; not duplicates of queued work)

1. `prennent-88-subject` (P2): name 88's class for the subject slot. Bar:
   "88 takes a plural subject value making '[88] prennent souvent la…'
   grammatical at @1117–1123 with ≤1 ungranted assumption, or the
   plural-pronoun arm is killed on 88's distributional profile (n=23;
   anchors: 'tout [88]' @496, 'est à [88]' @765, '88 le' x3 @86/@646/@1541,
   'ne [88]' @1705)."
2. `cela-69-11-word` (P2): test the word-internal-"la" adverse at its only
   locus. Bar: "'69 11' @1115–1116 parses as one word ('cela'-shaped,
   69='ce'-class) with the clause boundary before 88, or the
   word-internal-la hypothesis is killed at this window (69: n=12,
   followers 26 x3 / 13 x2 / 24 x2 / 88 x2 / 14 / 11 / 74 / 64)."
3. No third target: the clerk-single-n question is already queued as
   `spell-single-consonant` (P3) — deliberately not re-queued.
