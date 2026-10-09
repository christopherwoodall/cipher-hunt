# Battery report: noun-09-915-value

- Target id: `noun-09-915-value`
- Claim: Name 09's nominal value at 'par __' @915 under the split framing (noun-09-916's value-naming fence was pre-split; retry with the adverbial windows excluded from the candidate set).
- Date: 2026-10-09
- Worker: battery worker noun-09-915-value (subagent 52e905be-50b5-4c34-a424-d450b5b844f5)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.

## Bar (verbatim, pre-registered)

"Value named with >=2 legs under the split framing or fenced"

Numbered pass/fail clauses (restated before testing):

1. **C1:** Name 09's nominal value with ≥2 independent legs under the split framing (adverbial windows @1059/@1765 excluded from the candidate's distribution).
2. **C2:** Else fence the value-naming with stated cause.

## Method

Read BATTERY-PROTOCOL.md first; created `locks/noun-09-915-value.lock` on start
(agent 52e905be-50b5-4c34-a424-d450b5b844f5, 2026-10-09T19:18:52Z; deleted on
completion). Re-derived the repaired 1,847-pair / 96-type stream in-session
(asserts: n=1847, 96 types). Adopted (not re-litigated): the split-09-redteam-input
PROMOTE (nominal arm @915 + @289; adverbial arm @1059/@1765; single-class
hypothesis kill-grade dead) and the noun-09-916 NULL (pre-split value fence).

## The nominal-arm distribution under the split framing

n(09)=12. Adverbial windows EXCLUDED: @1059 (`23 77 84 09 98 83 82` =
"[23] l'on [09] vient m"), @1765 (`06 77 84 09 24 87 64` = "ent l'on [09]
verb ce qui"). Nominal-arm windows (10):

| locus | bytes | gloss | role |
|---|---|---|---|
| @915 | `59 37 96 09 02 24 49` | est [37] par [09] [02] verb [49] | FORCED nominal (par-agent) |
| @289 | `28 00 97 09 64 29 40` | [28] pour [97] [09] qui er e | nominal-frame (NP + qui-relative) |
| @0 | `09 00 97 51` | [09] pour [97] [51] | open |
| @173 | `48 21 60 09 87 86 21` | e noun [60] [09] ce INF noun | open |
| @518 | `87 77 80 09 70 91 77` | ce le [80] [09] pre [91] le | open |
| @591 | `97 41 41 09 00 92 79` | [97] [41] [41] [09] pour verb tout | open (doublet) |
| @680 | `77 45 23 09 07 00 92` | le ce/dict [23] [09] [07] pour verb | open |
| @1223 | `24 48 30 09 20 57 64` | verb e pas [09] [20] [57] qui | open |
| @1262 | `69 88 01 09 11 50 46` | noun gov [01] [09] la [50] que | open |
| @1820 | `37 01 02 09 19 00 97` | [37] [01] [02] [09] [19] pour [97] | open |

Standing values used: 96='par' (granted), 64='qui' (granted), 59='est'
(provisional), 00='pour' (A9 leg-1), 11='la' (pencil), 79='tout' (A5).

## C1: value-naming attempt — FAIL

**Leg 1 (@915):** "est [37-pred] par [09]" — passive agent, forced nominal
under granted 96='par'. But the VALUE is underdetermined: corpus census of
"par X" (2.0M chars 1841 French) shows dozens of short nominal complements
— articles (la/les/le), "un"/"une" (66/64x), "lui" (26x), "leur", "eux",
"hasard" (14x), "jour" (12x), bare nouns (écrit, an, mois, mer…). No single
value is forced; each candidate needs ≥1 ungranted assumption about the
open right edge ([02] class-open, modal-24's complement unlicensed).

**Leg 2 (@289):** "pour [97] [09] qui" — [97] [09] as NP antecedent of the
"qui"-relative. But [97] is class-open: if [97] is a determiner, 09 is head
noun; if [97] is a noun, 09 is modifier. No value for 09 is forced, and no
candidate from the @915 set converges here without assuming [97]'s class.

**Convergence test:** the strongest cross-window candidates ("lui",
"jour", "hasard") each die on the other window — "pour [97] lui qui"
needs [97] to vanish or compose (ungranted); "pour [97] jour qui" needs
[97]="chaque"-class (ungranted). Every candidate carries ≥2 ungranted
assumptions across the two legs. The lane's naming bar (cf. val-08-31-letter:
"anchored by pencil/standing values, zero new assumptions") is not met.

**Open windows:** none of the 8 open windows forces a value either — @1223
"pas [09]" sits inside the killed bare-nominal frame; @1262 "[09] la"
is ungrammatical as noun+article; @0/@591/@680/@1820 "[09] pour" needs
09's left/right class resolved first.

**C1: FAIL.** No French value parses ≥2 nominal-arm windows with standing
values and zero ungranted assumptions. The split framing removes the
adverbial windows from the distribution but adds no converging leg —
it makes the split coherent, not the value nameable.

## C2: fence — FIRES

09's nominal VALUE is fenced as unnameable at battery grade. This does NOT
disturb the split package: the nominal ARM (class-level) stands forced at
@915 under granted 96='par'; only the value-naming is fenced. No standing
or red-team verdict contradicted or downgraded; §7 intact (no polyvalence
declared). Canonical-stream caveat stands.

## Verdict: NULL (fence executed per bar's else-branch)

## Follow-ups (all verified ABSENT from battery-queue.json, for supervisor)

1. **`val-97-289-det`** (P3): name 97's class at @289. If 97 is a
   determiner, 09 is forced as head noun of the "qui"-relative NP —
   sharpens the second nominal leg from frame-level to class-level.
2. **`val-02-916-rightedge`** (P4): name 02's class at @916. The right edge
   of the "par [09]" window; a nominal vs verbal 02 decides what "par [09]"
   can compose with.
3. **`nom09-open-windows`** (P4): classify the 8 open 09-windows as
   nominal-compatible vs excluded under the split framing; finds additional
   nominal legs or shrinks the candidate distribution.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/noun-09-915-value.lock` created on
  start (2026-10-09T19:18:52Z, no stale lock), deleted on completion
  (verified gone).
- `battery-queue.json`: `noun-09-915-value` queued → verdict/null,
  2026-10-09 (pre-write assert passed — was queued/verdictless; own entry
  only; target-id-unique tmp `battery-queue.json.noun-09-915-value.tmp` +
  atomic rename; disk re-validated; no downgrade).
- `canonical.py` never used; R5005, sealed gates, red-team adjudication
  queue untouched.
