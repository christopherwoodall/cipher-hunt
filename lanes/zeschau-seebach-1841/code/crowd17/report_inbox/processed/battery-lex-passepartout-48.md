# Battery `lex-passepartout-48` — "passe-partout" near-miss at @44–48

## Bar (verbatim from queue)

"resolve whether @44–48 can read \"passe-partout\"-shaped given 00='pour' granted vs the needed 'tout'; the 00 conflict is red-team venue if it blocks"

## Bar as numbered pass/fail clauses

1. **C1 (parse):** @44–48 reads "passe-partout"-shaped with all pairs assigned consistently under standing values; the 00='pour' conflict is then escalated to the red team as the venue (battery may not overturn the A9 grant).
2. **C2 (kill):** else, kill the compound with 00='pour' byte evidence plus 81's profile. Discriminator: any other "passe-X" compound in the corpus.

## Method

Read BATTERY-PROTOCOL.md first; created `locks/lex-passepartout-48.lock` on start.
Re-derived the window independently on the repaired 1,847-pair stream
(`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
parsed byte-exact per `repair_parse.py`: `[s[i:i+2] for i in range(o, len(s)-1, 2)]`).
`canonical.py` never used. R5005, sealed gates, red-team queue untouched.
Parent context: `code/crowd17/report_inbox/battery-seg-30-62-96.md` (null follow-up #1).

## Window-level evidence (re-derived)

- Total: 1,847 pairs, 96 types (verified).
- **@44–48 = `81 30 62 96 00`** (confirmed; @40–52 = `01 24 88 43 81 30 62 96 00 92 79 37`).
- Standing values: 30='pas' (promoted), 96='par' (promoted), 00='pour' (granted A9, leg-1 class-level).
- **30-62 bigram occurs exactly once stream-wide (@45)** — this window is the sole
  "passe-X" locus; the discriminator search returns no second compound candidate.
- 62 census: n=35 (followers 94 x9, 48 x6, 98 x5, 16 x4, ...). 62="il" is kill-grade
  dead (standing); 62's value is otherwise open.
- 81: "prin" kill stands; value otherwise open.

## Per-clause results

**C1 — FAIL.** Under standing values the compound is byte-excluded at exactly one
pair. @45–47 = `30 62 96` fits "passe-partout" (= pas/se/par/tout) byte-perfectly
iff 62='se'; but @48 = `00` = 'pour' (granted A9) where the compound requires
'79' = 'tout' (promoted A5). "passe-parpour" is not a French word. The parent
battery's lexicon check (cited, not re-derived) found "passe-partout" the sole
French host of "pas"+X+"par" contiguity ("passeport" needs "por" at @47;
"passe-passe" needs "passe" at @47–48 — both contradicted by standing bytes);
my independent byte checks confirm the window and the sole-locus (30-62 x1)
premises of that check. The 00 conflict blocks; per the bar it is red-team venue
— recorded as a note below, not executed.

**C2 — PASS (kill-grade).** Byte evidence: pairs @44–48 are fixed bytes on the
repaired stream; @48 = `00` = 'pour' (granted) vs the compound's required 'tout'
is a direct contradiction between two standing values — a window forcing the
claim false. 81's profile: @44 = 81 cannot rescue the compound (its value is
open and no licit left-neighbor of "passe-partout" is named); the compound is
already dead at @48, so 81 is moot — stated honestly, 81 adds nothing. The
discriminator is exhausted: no other "passe-X" compound exists in the corpus
(30-62 bigram x1 stream-wide).

## Adverses

- **00='pour' granted (needs 'tout' for passe-partout): ANSWERED.** The conflict
  is the kill instrument itself: 00='pour' is not re-litigated; its granted
  status is exactly what excludes the compound at @48.
- **Red-team venue if the 00 conflict blocks: HONORED.** It blocks; the venue
  note is recorded (below) and no battery action touches the A9 grant.

## Red-team venue note (not a finding, not tested)

Overturning 00='pour' at @48 would be required for the "passe-partout" reading;
that re-valuation belongs to the red team. The near-miss is genuine
(3 of 4 compound pairs byte-perfect under 62='se'), so if the red team ever
re-opens 00, this window re-activates as a 62='se' leg. Until then it is dead.

## Verdict: KILL

The "passe-partout" reading of @44–48 is killed at battery grade: the compound
requires @48='tout' and the byte is 00='pour' (granted). The near-miss is
adjudicated — real shape, single-pair byte exclusion, no second "passe-X"
locus in the corpus. No standing verdict contradicted or downgraded.
