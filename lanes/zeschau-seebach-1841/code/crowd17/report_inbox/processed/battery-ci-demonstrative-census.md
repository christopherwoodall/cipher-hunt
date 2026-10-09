# Battery report: ci-demonstrative-census

- Target id: `ci-demonstrative-census`
- Claim: "bound '-ci' occurs outside ce-adjacent positions ('ce ... N-ci' demonstrative frames)"
- Date: 2026-10-09
- Worker: battery worker (session f187ca54-3dc9-4653-b9e3-2c24efafb2cb)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
  All @-offsets are 0-based repaired-stream indices of the 01 token. n(01) = 28.
  Never used canonical.py. R5005, sealed gates, red-team queue untouched.
- Lock: code/crowd17/next-token/locks/ci-demonstrative-census.lock (created at
  start, deleted at end; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"name the demonstrative-suffix environment iff >=2 additional windows parse as
'ce N-ci' with stated NP boundaries; else fence @984 as the unique
'-ci'-after-noun window with stated cause"

Numbered pass/fail clauses (restated before testing, not modified after):

1. (Naming arm) >=2 additional windows (beyond @984) parse as 'ce N-ci'
   demonstrative frames ("ce"-determiner + noun + bound '-ci' suffix) with
   stated NP boundaries. If met, name the demonstrative-suffix environment.
2. (Fence arm) If clause 1 fails, fence @984 as the unique '-ci'-after-noun
   window, with stated cause.
3. Adverses answered: (a) the three 01='en' windows (disc-01-24-ci-X) --
   coordinated, not re-litigated; (b) ci-bound-01's ce-context restriction --
   coordinated, not re-run.

"Additional" = beyond @984 (the reference '-ci'-after-noun window).

## Method

1. Re-derived the repaired stream in-session (1,847 pairs, 96 types; n(01)=28
   confirmed). Parsed per repair_parse.py; canonical.py never touched.
2. Exhaustive census: for each of the 28 01 windows, recorded (i) whether a
   ce-group (87/47/45) occurs within -6, (ii) whether the immediate
   predecessor is noun-shaped under standing values, (iii) wider ±8/±15
   context for candidates.
3. Tested every candidate for a grammatical 'ce N-ci' parse under standing
   values (banked GT, promoted/granted, provisional; 1841 diplomatic French).
4. Cross-checked against the coordinated reports (ci-bound-01 NULL,
   disc-01-24-ci-X PROMOTE-unratified) without re-running their bars.

## Window-level evidence

### Census: ce-groups near 01 (within -6), all 28 windows

Only 8 windows have a ce-group within -6 of 01:

| 01 @ (0b) | ce at | status |
|---|---|---|
| @195 | 47 at -1, 87 at -4 | direct ce-context ("ceci", ci-bound-01) |
| @345 | 87 at -1, 45 at -5 | direct ce-context ("ceci", ci-bound-01) |
| @484 | 45 at -6 | "45 93 pour [13] [52] pas(30) [01]" -- 01 after "pas"; '-ci' never attaches to "pas". No NP. FAIL. |
| @828 | 87 at -4 | 01='en' decided (disc-01-24-ci-X). Unavailable as '-ci'. FAIL. |
| @976 | 45 at -2 | "45 08 [01] pour(00)" -- 08's value open; unparseable under standing values. Fenced residual, not a parse. FAIL. |
| @984 | 45 at -1, 47 at -3 | reference window (see fence arm) |
| @988 | 45 at -5 | separated by "01 24 89 48"; no NP containing 01. FAIL. |
| @1029 | 87 at -1, 45 at -5 | direct ce-context ("ceci", ci-bound-01) |

The other 20 windows have no ce-group within -6.

### Census: 01 after noun-shaped predecessors

01 windows whose immediate predecessor is noun-shaped under standing values:

- @893 / @970: "le(77) [76] [01]" -- 76 = noun (battery-promoted, masculine).
  Determiner is "le", not "ce". "le N-ci" is ungrammatical French. FAIL as
  'ce N-ci' (01's value stays open per ci-bound-01's sweep).
- @1462: "[66] tout(79) fois(17) [01]" -- 17 = "fois" (granted noun). No
  ce-group anywhere in ±15 (checked: 84 59 36 67 33 46 92 62 61 21 67 86
  66 79 17 | 21 62 48 21 02 62 38 26 ...). Determiner slot occupied by
  79="tout" (A5, contested). "fois-ci" without a "ce"-determiner is not
  'ce N-ci'. FAIL.
- @295 / @1653: pre=16 -- 16's noun candidacy is dead (frame-82-16 NULL,
  2026-10-09: 16="même"/"mais"/noun/infinitive all killed; live lead is
  finite verb "a"/"est" via elision). Not a noun. FAIL.
- All other predecessors (32, 41, 66, 10, 33, 30, 85, 86, 82, 37, 08,
  48, 46, 88, 15) are verb/particle/open/A12-unit -- none is a
  decided noun inside a ce-headed NP.

### @976 detail (the only other ce-adjacent 01 with an open nominal slot)

"77 76 01 98 48 51 45 08 |01| 00 92 07 76 47 78 45 01" (row a6_01).
Under A11 (45='ce', HOLD): "ce [08] [01] pour(00)". 08's value is open;
no parse is licensed at battery grade, and "ce N-ci pour" needs the
noun first. Under the 45='dict' lead: "dict [08] [01]" -- 08 open again.
Fenced as an 08-driven residual, not a 'ce N-ci' parse.

## Per-clause pass/fail

1. Naming arm (>=2 additional 'ce N-ci' windows): FAIL. Zero additional
   windows parse as 'ce N-ci'. The census is exhaustive: no window beyond
   @984 combines a "ce"-determiner, a noun, and 01 in demonstrative-suffix
   position under standing values.
2. Fence arm: FIRES. @984 is fenced as the unique '-ci'-after-noun window:
   - Uniqueness byte-confirmed: the '78-45-01' trigram ("verdict-ci" shape)
     occurs exactly once stream-wide (0b@982, row a6_01).
   - The '-ci'-after-noun reading at @984 is "ce(47) verdict(78-45) -ci(01)"
     = "ce verdict-ci". It is conditional on TWO unratified NULL leads:
     ver-78 (R16-005 LEAD) and dict-45 (R16-004 lead, refined R18-026).
     ('verdict' as sole host of 45="dict" was certified today by
     dict-45-host-inventory PROMOTE -- still battery-level, unratified.)
   - It competes with the A11 reading "ce(47) [78] ceci(45-01) fait(24)"
     (ci-bound-01 W1: clean parse conditional on the A11 HOLD) and the
     01='en' reading "ce(45) en(01) fait(24)" (disc-01-24-ci-X PROMOTE,
     battery-level, unratified).
   - Three-way contest, each conditional on a different unratified
     lead/HOLD: fenced, not promoted, not killed. If ver-78 ever promotes,
     fork-78-45 clause (a) already flags this leg for re-examination.
3. Adverses: (a) ANSWERED -- the three 01-24 windows (@40, @828, @984) carry
   01='en' local per disc-01-24-ci-X (battery PROMOTE, unratified); @828's
   and @40's 01 are therefore unavailable as '-ci'; @984 admits both 'en'
   and '-ci' readings, which is consistent with fencing rather than
   promoting. Nothing re-litigated. (b) ANSWERED -- ci-bound-01 (NULL)
   restricted bound '-ci' to the four ce-contexts with 01 valueless
   elsewhere; this independent 28-window census agrees (no 'ce N-ci' frame
   outside @984; the A12-unit windows @940/@1634/@1818 and the "-cier"
   syllable lead @596 are sub-token and name no value). No contradiction.

## Verdict: NULL (fence executed per the bar's else-arm)

The demonstrative-suffix environment is NOT named: the general claim
"bound '-ci' occurs outside ce-adjacent positions" finds zero support in
the exhaustive 28-window census. @984 is fenced as the unique
'-ci'-after-noun window ("ce verdict-ci" reading, conditional on the
unratified ver-78 and dict-45 leads, contested by the A11 "ceci" and the
01='en' readings).

No standing red-team verdict is contradicted or downgraded: A11 (45='ce'
HOLD), A12 (37-01 unit), ver-78 NULL, dict-45 NULL, fork-78-45 NULL,
ci-bound-01 NULL, and disc-01-24-ci-X's battery promote are all
consistent with the findings. No polyvalence declared (§7 intact).

## Follow-up targets (nulls regenerate work)

1. **ci-984-reading-adjudicate** (priority 2): adjudicate @984's three-way
   reading contest -- (i) A11 "ce(47) [78] ceci(45-01) fait(24)", (ii)
   ver-78+dict-45 "ce(47) verdict(78-45) -ci(01) fait(24)", (iii) 01='en'
   "ce(45) en(01) fait(24)". Each is conditional on a different unratified
   lead/HOLD; battery cannot resolve it. Red-team act.
2. **ci-976-08-gate** (priority 3): test "ce(45) [08]-ci pour(00)" at @976
   once 08's value resolves. The only other ce-adjacent 01 with an open
   nominal slot; currently unparseable (08 open), fenced as an 08-driven
   residual.
