# Battery report: verb-92-value

**Target:** `verb-92-value` (P2)
**Date:** 2026-10-09
**Verdict:** NULL

## Bar (verbatim from queue)

"Test the other five "pour 92" windows (@49, @330, @593, @683, @978) for a shared verb stem, or coordinate with the split-92 red-team docket once the class question resolves."

## Bar restated as numbered clauses

1. A single shared verb stem parses all five "pour 92" windows (@49, @330, @593, @683, @978), and the stem is named.
2. (Alternative arm) If the class question is unresolved at battery level, coordinate with the split-92 red-team docket instead of naming.

## Method

Read BATTERY-PROTOCOL.md first. Lock `locks/verb-92-value.lock` created on start,
deleted on completion. Re-derived the repaired 1,847-pair / 96-type stream in-session
from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
(byte-exact tokenizer per `repair_parse.py`; asserts held: 1,847 pairs).
`canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
Class premises adopted, not re-litigated (per the adverse): verb-92-subset PROMOTE
(battery), R18-022 (red team: 92 = verb CLASS tier, subset-scoped, conditional;
global class HELD pending the §7 split question; 92 → ["verb","cls"] in registry).

## Window-level evidence (0-based @-offsets, repaired stream)

92 occurs 22x stream-wide. "00 92" (pour + 92) occurs exactly 6x: @49, @330, @593,
@683, @978, @1154.

- **@49** (a1_01): `96 00 | 92 79 37 11 79 85 58` — "par pour [92] tout [37] la tout [85]".
  79="tout" (A5), 11="la" GT. Infinitive-compatible: "pour V tout" (V takes "tout"
  as direct object). **Canonicality caveat:** a1_01 is phase-fragile — a clean
  offset-1 rival reparse exists for this row (battery finding, adoption is red-team
  business); the window is a canonical-offset object.
- **@330** (a2_05): `19 00 | 92 50 45 54 88 40 03` — "pour [92] [50] ce [54] [88]-e".
  45="ce" (A4). 50 open (n=11, no named value). No selectional info.
- **@593** (a4_00): `09 00 | 92 79 85 01 29 40 03` — "pour [92] tout [85] [01]-er".
  29="er" GT. Same "pour V tout" frame as @49.
- **@683** (a5_00): `07 00 | 92 64 29 40 65 94 29` — "pour [92] qui [29]-e ...".
  64="qui" granted follows 92 immediately. **No infinitive parse exists:**
  "pour [V-stem] qui ..." is ungrammatical in French — an infinitive after "pour"
  cannot be followed by "qui". This window belongs to the ratified nominal subset
  (R18-022 subset-scoped account; prof-92 battery PROMOTE listed @683 and @203 as
  the nominal subset, 2 legs).
- **@978** (a6_01): `01 00 | 92 07 76 47 78 45 01` — "pour [92] [07] [76] ce [78] ce...".
  47="ce" (A4). 07 open (n=8, no named value). No selectional info.
- **@1154** (a6_09, the sixth "pour 92" window, not in the bar): `00 92 29 80 17` —
  "pour [92]er [80] fois" — the smoking-gun infinitive leg (R18-022). Any -er verb.

92 follower census (n=22): 00 x6, 11 x3, 94 x2, 84 x2, 40/98/16/83/30/13 x1, 79 x2,
69 x2, 60 x2, 64 x2, 62 x2, 63/50/47/67/93 x1.

## Per-clause pass/fail

1. **FAIL (kill-grade for the uniform claim).** No single verb stem can cover all
   five windows: @683 ("pour [92] qui") is nominal under the ratified
   subset-scoped account — a verb stem there is ungrammatical, and naming one
   would contradict R18-022. For the remaining verb windows, no unique stem is
   nameable: "pour V tout" (@49, @593) admits the whole 1841-diplomatic-French
   class of verbs taking "tout" as direct object (prendre, voir, faire, savoir,
   comprendre, dire, rendre, ...), and @330/@978's followers (50, 07) are open
   values supplying zero selectional information. "Pour [92]er" (@1154) admits
   any -er verb.
2. **FIRES.** The class question is settled at red-team grade (92 = verb class,
   subset-scoped; split-92 docket live). Battery-level value naming defers to
   that docket's resolution of the verb/noun window assignment. Nothing is
   re-litigated here.

Adverses: the class bars of verb-92-subset are adopted as premises, not
duplicated. No standing or red-team verdict contradicted or downgraded; §7 intact.

## Verdict: NULL

The uniform shared verb stem is dead at @683 (ratified nominal subset); the
verb-subset windows supply no unique nameable stem. The value-naming task is
inconclusive at battery level and stays with the split-92 red-team docket.

## Recommended follow-ups (verified absent from queue)

1. `val-92-tout-verbs` (P3): enumerate the 1841-diplomatic-French -er verbs taking
   "tout" as direct object; test each candidate against @1154 "pour [92]er [80] fois"
   and the @330/@978 frames; kill zero-fit candidates on bytes.
2. `pour92-683-nounframe` (P3): parse @683 under the ratified nominal subset —
   "pour [92-noun] qui [29]-e ..."; name the noun-class frame so the split-92
   docket has both arms stated at battery grade.
3. `stem-92-50-07` (P4): re-test a shared stem once 50 and 07 name values
   (selectional info currently absent at @330/@978).

## Bookkeeping

- Lock `code/crowd17/next-token/locks/verb-92-value.lock` created on start, deleted
  on completion.
- `battery-queue.json`: `verb-92-value` queued -> verdict/null (temp-file + rename;
  pre-write assert confirmed no prior verdict; JSON re-validated; only this entry touched).
- R5005, sealed gates, red-team adjudication queue untouched.
