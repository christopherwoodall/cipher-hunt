# Battery `adv-20-760-boundary` — verdict: NULL (fence executed)

## Bar (verbatim, pre-registered)

> clause boundary at @760 forced iff the 'est à' right-context frame holds with zero ungranted assumptions; else fence

Numbered clauses (restated before testing, not modified after):

- **C1.** The right-context frame `62 94 59 39 88 66` ("il ne est à [88] [66]")
  holds as a complete independent clause with **zero ungranted assumptions**
  → the clause boundary at @760 (after 20, before 62) is forced.
- **C2.** Else-arm: if C1 fails, fence @760's boundary (stated cause).

Adverses: none listed.

## Method

Read BATTERY-PROTOCOL.md first. Created `locks/adv-20-760-boundary.lock` on
start (agent id + UTC timestamp). Re-derived the repaired stream in-session
from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`:
**1,847 pairs / 96 types**, asserts held. `canonical.py` never used. R5005,
sealed gate instances, red-team adjudication queue untouched.

@-offsets below are **0-based** (matching the parent battery-adverb-20-wide's
locus labels: 20 sits at 0-based @760).

## Window evidence (byte-exact)

0-based @754–766, row a5_03 (gloss-anchored row):

```
754: 11   755: 70   756: 82   757: 34   758: 29   759: 40 | 760: 20 |
761: 62   762: 94   763: 59   764: 39   765: 88   766: 66
```

i.e. `11 70 82 34 29 40 |20| 62 94 59 39 88 66`.
The pencil gloss "la pre m i er e" sits over @754–759 ("la première");
20 at @760 is the locus; the right context is `62 94 59 39 88 66`.

Adopted standing premises for the right side:

| group | adopted value | grade |
|---|---|---|
| 62 | 'il' | battery-level lead (R17) |
| 94 | 'ne' | battery-level lead |
| 59 | 'est' | provisional (§7) |
| 39 | '/a/' ("à") | battery-level lead (R17-005) |
| 88 | infinitive-shaped | PROMOTE locus-level (battery-88-1727-shape), whose C2 analysis is exactly this frame: "est à [88]" @765 = the standard passive-infinitive construction ("est à faire"); 88 carries -er morphology (@1050 "88 29") |
| 66 | — | fully open (n=19, no adopted premise) |

## Per-clause results

**C1: FAIL.** The 'est à' frame does not close with zero ungranted
assumptions, on two independent grounds:

1. **66's role is the missing complement.** Under the adopted premises the
   right side reads "il n'est à [88-inf] [66]". The "être à + infinitif"
   passive-infinitive construction ("il est à craindre que…") requires its
   complement, and 66 supplies the only post-infinitival slot. 66's class is
   fully open across its 19 windows (followers {98, 84, 14, 24, 91, 73, 15,
   67…}, no adopted premise). Naming 66's role — "que", nominal complement,
   anything — is **one ungranted assumption minimum**, so the frame cannot
   hold at the bar's zero-assumption standard. The clause is incomplete
   without it: "il n'est à [inf]" begs its complement.
2. **Corpus strain on the negated frame.** In 32,547,082 chars of side-period
   corpus: affirmative impersonal "il est à + inf" is attested ("il est à
   souhaiter / remarquer / mettre / croire / craindre"); negated
   "n'est (pas) à + inf" has **zero** infinitive complements (only
   possessive/locative "n'est pas à vous / leurs / Hatto"). Bare "n'est à +
   [word]" is unattested outright. Absence is not ungrammaticality (literary
   "ne"-alone is normal 1841 French), so this is a strain, not a kill — but
   it means the frame leans on an unattested negated shape *in addition to*
   the ungranted 66 assumption.

**Second independent ground (boundary location, not just frame closure):**
even granting a complete right clause, the boundary is not forced to sit
*after* 20. The alternative — boundary before 20 ("la première | [20] il
n'est à [88] [66]", 20 clause-initial) — requires a clause-initial role for
20, and 20's clause-initial roles (conjunction/preposition, adverb) are
**fenced, not killed** (conj-prep-20-wide, adverb-20-wide). A fenced route
is a live route at fence grade, so the boundary location is undecidable:
forced-after-20 fails.

**C2: FIRES — fence executed.** @760's boundary is fenced with stated cause:
the 'est à' right-context frame needs 66's undetermined role (≥1 ungranted
assumption), carries a negated-shape corpus strain, and the boundary could
alternatively precede 20 via 20's fenced clause-initial roles.

## Scope

Fence, not kill. Nothing here rules out a boundary after 20 — "il n'est à
[88-inf] [66]" remains a live frame if 66 names as the infinitive's
complement. No standing or red-team verdict contradicted or downgraded:
battery-88-1727-shape's locus PROMOTE is adopted as a premise, not
re-litigated; §7 intact (no polyvalence declared). Canonical-stream caveat
stands (row a5_03 offset unvalidated beyond the gloss anchor).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `val-66-767-frame` (P3) — name 66's class at @767 ("88 66 98", 66→98
   'vient'-class follower). Bar: 66's role named with zero rivals → the
   'est à' frame closes → re-test whether the boundary hardens.
2. `est-a-neg-corpus` (P4) — wider corpus sweep (drama + prose, 1841 and
   modern) for negated impersonal "il n'est (pas) à + infinitif". Bar: ≥1
   genuine attestation removes the negation strain; confirmed zero keeps the
   frame fenced on this ground.
3. `boundary-760-20role` (P3) — test 20 as clause-initial at @761 directly
   (relative-adverb subclass "où/quand/comment" per reladv-20-1703's
   surviving arm, plus any other clause-initial role). Bar: every
   clause-initial role killed → the boundary must fall after 20 (boundary
   forced, given a complete right clause); any role live → the forced claim
   is dead.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-adv-20-760-boundary.md` (this file).
- Queue: `adv-20-760-boundary` queued → `verdict`/`null`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; temp-file + rename;
  JSON re-validated post-write; own entry only; no downgrade).
- Lock `adv-20-760-boundary.lock`: created on start, deleted on completion
  (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
