# Battery verdict: noun-66-98-side

- Target: `noun-66-98-side` (battery-queue.json, priority 3, status queued)
- Claim: test the noun-66 arm in the X-66-98 subject windows (@88/@123/@766)
- Date: 2026-10-09

## Bar (verbatim, pre-registered)

"name 66's noun value or fence the noun arm at those windows"

- C1 (name): name 66's noun value with >=2 converging legs at zero new assumptions (lane naming bar, cf. masc-noun-86-name).
- C2 (fence): fence the value-naming arm at the three windows with stated cause.

No adverses listed on the queue entry.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
(asserts held: 1,847 pairs, 96 types). `canonical.py` never used. All loci
byte-confirmed. Standing values from the table registry; 98='vient' is LEAD
(unratified) and 77='le' provisional — used as frame, not as banked.

## Findings

### The three windows (byte-exact)

- @88: `14 06 88 77 66 98 19 41 98 81` → "…ent [gov] **le [66] vient** [19] [41] vient [81]"
- @123: `60 90 19 58 66 98 82 48 11 02` → "…[19] [58-nominal] **[66] vient** m e la [02]"
- @766: `94 59 39 88 66 98 80 10 22 94` → "ne est a/à [88-gov] **[66] vient** [80] [10] [22] ne"

### C1 fails: no value nameable

Adopted (not re-litigated): `subclass-66-98-noun` PROMOTE (2026-10-09) — 66
is a plain noun, subject of "vient" in all three windows; the
substantivized-infinitive rival is killed at grammaticality grade (0 genuine
infinitive subjects of "vient" in 57.4M chars). The class arm is closed; the
value is the question.

What the windows select:
- @88: masculine singular (provisional 77='le'), subject of "vient" — a noun
  capable of coming (animate or inchoative: homme/monsieur/enfant/moment/
  temps/jour/soir…).
- @123: singular (98 3sg), NP "58-nominal 66" as subject.
- @766: singular subject of "vient" before "[80-inf]".

Every valued contact is class-only or provisional (58=nominal cls, 88=gov
cls, 77='le' provisional, 80 open, 19 open). No window contains a byte that
selects one lexeme over its rivals: every masculine-singular "venir"-subject
noun parses all three windows identically. Per the masc-noun-86-name
precedent, a leg must *converge* — select a value over alternatives — and no
candidate can earn even one selective leg on current bytes. Lane naming bar
("zero new assumptions") not met.

### C2 fires: fence the value-naming arm

**Fence cause:** 66's noun class at the three windows stands (adopted
PROMOTE); the *value* is unnameable at battery grade. The noun arm as a class
is NOT fenced — fencing it would contradict the standing promote, which this
report does not do.

## Verdict: NULL (fence executed)

- C1 (name the value) FAIL; C2 (fence the naming arm) FIRES.
- Scope: value-naming only, at @88/@123/@766. Untouched: the subclass-66-98-noun
  class promote, 98='vient' LEAD, 77='le' provisional, all 66 subsets elsewhere
  (pour-governed non-finite arms, §7 red-team venue), num-65-agreement, §7.
  No standing/red-team verdict contradicted or downgraded. Canonical-stream
  caveat stands.

## Follow-ups proposed (§4; all verified ABSENT from battery-queue.json)

1. `noun-66-88-contact` (P4) — the @765–766 "88 66" contact: what does
   governor-class 88 do immediately before a noun subject? A licensed 88-role
   constrains 66's value.
2. `noun-66-123-58` (P4) — name 58's class at @122; a determiner-58 or
   adjective-58 reading constrains 66's noun value (gender/animacy legs).
3. `vient-subject-corpus-66` (P4) — corpus census of masculine-singular
   subjects of lexical "vient" in 1841 French; if one lexeme dominates
   selectionally, candidacy (or fence of the naming arm at corpus grade).

## Bookkeeping

- Queue: `noun-66-98-side` queued → `verdict`/`null` 2026-10-09 (pre-write
  assert passed — was queued/verdictless; target-id-unique tmp
  `battery-queue.json.noun-66-98-side.tmp` + atomic rename; disk re-validated;
  own entry only; no downgrade).
- Lock `locks/noun-66-98-side.lock`: created on start (agent
  6d8555c7-5f24-4f0e-bfaf-8b81d3c57485, 2026-10-09T19:29:00Z, no stale lock),
  deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
