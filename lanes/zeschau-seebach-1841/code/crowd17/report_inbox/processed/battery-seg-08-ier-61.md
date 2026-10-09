# Battery report: seg-08-ier-61

- Target id: `seg-08-ier-61`
- Claim: "@60-67 re-segments grammatically once 08 resolves"
- Date: 2026-10-09
- Worker: battery worker (subagent 7098e020-290e-4745-8542-0e5c8ca730d7)
- Stream: repaired 1,847-pair / 96-type parse, re-derived in-session from
  `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
  (parsed per `code/side-keyhunt/repair_parse.py`; asserts held).
  `canonical.py` never used. R5005, sealed gate instances, and the red-team
  adjudication queue untouched. Offsets below are 0-based repaired-stream @.

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"resolve iff ONE segmentation parses @60-67 grammatically with <=1 non-granted
value assumption (08's value); else fence the window as multi-residual. Two
arms: '08 34 29'='hier' (08='h' spelling-letter)+'40 12'='en'+94='ne'+92, or
'08 34 29 40' one word ('fiere'/'biere'/'pierre'-tail if 08 in {f,b,p}) with
'12 94'='n'+'ne'"

Adverses (verbatim): "'en ne' order obstacle at @64-65 under the 'hier' arm;
08's value unknown — gated on queued stem-08, do not force."

## Numbered pass/fail clauses (fixed before testing, bar not modified after data)

- **C1 (trigger):** 08's standing state permits the test — proceed iff 08 is at
  least established as a spelling letter at @60 (value itself is the budgeted
  assumption).
- **C2 (arm A):** "08 34 29"+"40 12"+94+92 parses @60-67 grammatically with
  <=1 non-granted value assumption → resolve.
- **C3 (arm B):** "08 34 29 40" as one word + "12 94"='n'+'ne' parses @60-67
  grammatically with <=1 non-granted value assumption → resolve.
- **C4 (else):** fence the window as multi-residual with stated cause.

## Method

1. Read BATTERY-PROTOCOL.md first. Created
   `code/crowd17/next-token/locks/seg-08-ier-61.lock` on start (agent id + UTC
   timestamp); no stale lock pre-existed. Deleted on completion.
2. Re-derived the repaired stream in-session; verified 1,847 pairs / 96 types.
3. Checked 08's standing state in `battery-queue.json` and
   `code/table-grid/table-registry.json` before testing.
4. Adopted (never re-litigated): banked GT 34='i', 29='er', 40='e'; 12='n'
   promoted (registry `["n","prom"]`); 94='ne' battery lead (registry
   `["ne","lead"]`, banked map); 92 verb class-level (registry
   `["verb","cls"]`); stem-08-letter-probe PROMOTE (08 word-internal, all three
   letter contacts licensed); enne-word-64 KILL (no French word contains the
   substring "ierenne" — any word covering @61-65 as one unit is dead).

## Trigger check (C1)

- `stem-08` verdict: null (08 disambiguation did not name a value).
- `stem-08-letter-probe` verdict: **promote** — 08 is word-internal; all three
  letter contacts (0b@60 →'i', 0b@922 'e'→08, 0b@944 'e'→08) segmentally
  licensed. 08's letter VALUE is still unnamed.
- Per the probe's downstream note, this target is "unblocked on its shared
  premise" (08 is a spelling letter at @60). The bar budgets 08's value as the
  single allowed non-granted assumption, so the test proceeds on that basis.
- **C1: PASS (proceed).** No standing/red-team verdict contradicted; the
  on-08-homophony KILL (08='on' dead) is honored — neither arm uses it.

## Window-level evidence

0b@60–67, row a1_01 (byte-exact, re-derived):

| @ | group | standing value |
|---|-------|----------------|
| 60 | 08 | open (word-internal, value unnamed) |
| 61 | 34 | 'i' (GT) |
| 62 | 29 | 'er' (GT) |
| 63 | 40 | 'e' (GT) |
| 64 | 12 | 'n' (promoted spelling letter) |
| 65 | 94 | 'ne' (battery lead) |
| 66 | 92 | verb (class-level) |
| 67 | 69 | open |

Left context: 0b@58=12 ('n'), 0b@59=41 (open). Right context: 0b@68=13 (open).

### C2 — arm A: "hier" + "en" + "ne" + 92

Segmentation: `08 34 29` | `40 12` | `94` | `92` (+ 69).

- 08='h' (the ONE budgeted non-granted assumption) + 34='i' + 29='er' =
  **"hier"** (yesterday) — licit French word, zero further assumptions.
- 40='e' (GT) + 12='n' (prom) = **"en"** — licit.
- 94='ne' (banked lead) as negation; 92 verb-class; 69 open.
- Assumption budget: exactly 1 non-granted (08='h'). **Budget met.**
- Grammaticality: the surface string is "hier en ne [92-verb]". The clitic
  sequence **"en ne" is ungrammatical in French of any period**: the fixed
  clitic order is ne – me/te/se/nous/vous – le/la/les – lui/leur – y – en –
  verb, so "en" can never precede "ne" ("n'en", never "en ne"). As a
  preposition, "en" cannot take "ne" as complement either. The bytes fix the
  order (40 12 94 = "e n ne"); no re-segmentation under the arm's premises
  avoids the "en"+"ne" adjacency ("hiere"/"hieren" are not words; "enne" is
  not a word).
- **C2: FAIL at kill grade.** The adverse's 'en ne' order obstacle is confirmed
  fatal, not merely an obstacle. (Variants with 08='f' → "fier en ne" die on
  the same order; 08='b' → "bier" is not a word.)

### C3 — arm B: one word "08 34 29 40" + "n" + "ne" + 92

Segmentation: `08 34 29 40` | `12` | `94` | `92` (+ 69).

- 08='f' → "fiere" = **"fière"** (fem. adj., proud); 08='b' → "biere" =
  **"bière"** (fem. noun); 08='p' → "piere" — not a French word (dead
  immediately). Live letters: {f, b}, each the ONE budgeted assumption.
- "12 94" = 'n' (prom spelling letter) + 'ne' (banked lead).
- Surface string: "[fière/bière] n ne [92-verb]". The bare **"n" has no
  licensed role**: 12='n' is promoted as a word-INTERNAL spelling letter, not
  as a standalone word; "n'"-elision needs a vowel-initial host to its right
  ("ne" starts with consonant 'n'); left-attachment ("fièren"/"bièren") and
  right-attachment ("nne") are non-words; composing "12 94" as the "-nne"
  ending re-invokes the parent enne-word-64 KILL ("fierenne"/"bierenne"
  contain the killed "ierenne" substring — family sweep found no French word
  with it).
- **C3: FAIL.** No grammatical parse; the failure is structural (the stranded
  "n"), not assumption-budget (budget met at 1).

### Exhaustion note

Remaining segmentations of @60-67 were swept and die independently:
"08 34 29 40 12"|94 ("hieren"/"fieren"/"bieren" — non-words);
"08 34 29 40 12 94"|92 ("hierenne"/"fierenne"/"bierenne" — parent-killed
family); 08 standalone (contradicts the word-internal promote and §7's sole
polyvalence); "08 34"|"29 40"|"12 94" ("hi"/"fi"+"ère"+"nne" — "hière"/"fière"+"nne"
re-invokes the killed family). None parses with ≤1 new assumption.

## Per-clause results

- **C1: PASS** — trigger half-met as designed (word-internal promoted; value
  is the budgeted assumption).
- **C2: FAIL (kill grade)** — arm A forces the ungrammatical "en ne" clitic
  sequence; no French construction licenses "en" before "ne".
- **C3: FAIL** — arm B strands a bare "n" (12='n' is a spelling letter, no
  standalone role); "-nne" composition is parent-killed.
- **C4: EXECUTED** — the window is fenced as multi-residual (below).

## Verdict: NULL

Not a kill of any value: no window forces a falsehood about 08's class or
value (08 stays word-internal, value open). The bar's else-branch is the
designed outcome. No standing or red-team verdict contradicted or downgraded:
stem-08-letter-probe's promote stands (this battery uses it as premise);
enne-word-64's kill stands (extended, not disturbed); ne-94's lead stands
(used as premise, not re-litigated); §7 intact. Canonical-stream caveat:
row a1_01 offset unvalidated (68 of 70 per §7).

## Fence (stated cause)

0b@60-67 ("08 34 29 40 12 94 92 69", row a1_01) is a **multi-residual**:
(a) the "hier"+"en"+"ne" arm dies on the ungrammatical "en ne" clitic order
(kill grade for the arm); (b) the "fière"/"bière"+"n"+"ne" arm dies on the
unlicensed bare "n"; (c) the one-word "ierenne"-family composition is
parent-killed (enne-word-64). 08's letter value remains the keyhole: naming
it (h/f/b/p/…) re-tests (a) and (b) under tighter spelling constraints.

## Follow-ups proposed (nulls regenerate work; all verified absent from battery-queue.json)

1. `hier-arm-94-nonneg` (P3) — re-test arm A dropping the 94=negation premise:
   ne-94-right-context established non-negator functions for 94 (6 word-final
   '-ne' syllable, 5 non-particle). Bar: parse "hier en [94-X] [92-verb]" iff
   a licensed non-negation function of 94 fits @65 with ≤1 new assumption;
   else fence. (The C2 kill assumed 94=negation; "hier en [verb]" alone is
   grammatical.)
2. `seg-41-08-leftedge` (P3) — test "41 08" (@59-60) as a word-initial unit.
   Bar: name 41's class/value at @59; resolve iff "41 08 …" parses with ≤1 new
   assumption, which moves 08 off word-initial position and re-opens @60-67
   segmentation; else fence @59 as residual.
3. `enne-residual-69-rerun` (P4) — gated re-run of this bar once 69's value
   resolves: 69 (@67) is the verb's right neighbor and a named 69 may reframe
   the clause (e.g., supply the governed complement that licenses "en").

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-seg-08-ier-61.md` (this file).
- Queue: `seg-08-ier-61` queued → verdict/null via temp-file + rename, own
  entry only; pre-write assert confirmed no prior verdict; JSON re-validated.
- Lock `code/crowd17/next-token/locks/seg-08-ier-61.lock`: created on start,
  deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
