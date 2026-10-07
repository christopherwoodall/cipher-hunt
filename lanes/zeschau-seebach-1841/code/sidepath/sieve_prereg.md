# SIEVE pre-registration — side-path rapid crib screen (pass 1)

**Frozen:** 2026-10-07, before `slide_pass1.json` arrives. Nothing below changes once candidates are seen.
**Corpus:** R5005, 1,846 pairs / 96 groups. Era reference: `data/gutenberg-30513-tocqueville-t1.txt` +
`data/gutenberg-30514-tocqueville-t2.txt` (214,861 words), syllable rates from
`code/crowd3/battery.py` era table (maximal-onset orthographic syllabifier).
**Calibration exclusions (frozen from `code/crowd3/bigram_closer_results.md`):**
29, 82, 34 are contaminated (29=er 182× over era, 82=m 60×, 34=i).
**NEVER run a rate leg on 29/82/34.** On these groups, check (a) records `NEUTRAL-NO-LEG`
and check (b) alone decides (with GT-clash kill authority).

Status flags: GT = ground-truth anchor (crib: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que).
PROV = provisional lane values (87=ce, 64=qui, 96=par, 94=ne-strong, 06=verb-stem-class,
67=veut, 62=on-candidate). LEAD = screen-internal leads. Polyvalence is the cipher's
mechanism (F31) — same reading claimed by two groups is a WEAK, never a kill.

## Check (a): frequency plausibility (rate leg)

`f_c = count(group) / 1846`. Era rate: syllable-rate table for fragment readings,
word-rate table for whole-word readings (same Tocqueville corpus).
`r = f_c / f_era`.

| ratio r | verdict |
|---|---|
| 29/82/34 group | NEUTRAL-NO-LEG (skip; check (b) decides) |
| 0.5 ≤ r ≤ 2.0 | PASS |
| 0.25 ≤ r < 0.5 **or** 2.0 < r ≤ 5.0 | LEAD-WEAK |
| r > 5.0 **or** r < 0.25 | KILL |

Precedent anchor (lane): 6.69×/13.58×/28.9×/40.8× were kills; 3.29× out-of-band
survived as a caveat; 1.02–1.65 were passes. Red team F26 notes the factor-2 band
is uncalibrated — so the WEAK band is deliberately wide and anything inside it
survives to red team.

## Check (b): contextual/grammatical coherence (one window leg)

For each candidate, evaluate its actual cipher windows against applied GT/PROV neighbors:

1. **GT clash → KILL.** Candidate reading equals a GT anchor's value for the same
   group, or the group is GT-identified as a different reading (e.g. 78="e" vs
   40=e GT).
2. **Era-unattested GT-adjacent pair → KILL.** The candidate's reading next to a GT
   anchor with era bigram n=0 **and** ≥2 cipher occurrences
   (precedent: 78→40=e ×3, era ("e","e")=0 → killed).
3. **PASS.** ≥1 adjacent GT-anchor pair era-attested n≥5 and the reading parses
   grammatically in-window (e.g. "ce que" with 96-licensed que frame).
4. **LEAD-WEAK.** Everything else: windows only touch PROV/LEAD values or the
   candidate group itself (LEAD-next-to-LEAD is weaker than GT-adjacent and can
   only yield LEAD-WEAK, never a pass or a kill); attested pairs with era n<5;
   unattested context (no known neighbors).

**Kill requires BOTH:** a hard GT-anchor contradiction (rules 1–2). PROV/LEAD
collisions, rival readings, and "ungrammatical-with-provisional-neighbor" cases
are LEAD-WEAK with the tension noted — red team adjudicates, the sieve does not.

## Pass-1 output schema (`code/sidepath/sieve_pass1.json`)

```json
{"group": 78, "reading": "me", "check_a": {"verdict": "PASS", "r": 1.108},
 "check_b": {"verdict": "PASS", "note": "11=la→78 GT x2, era (la,me) n>=5"},
 "disposition": "SURVIVE"}
```
Dispositions: SURVIVE (both pass, or a-pass+weak), LEAD-WEAK (any weak, no kill),
KILL (one-line kill reason: which rule, which numbers). Killed entries still listed.

## Speed creed (binding)

Two checks, no deliberation. Ambiguity → LEAD-WEAK, through to red team.
I filter; red team kills.
