# Battery report: gov-excl-inf-drama

- Target id: `gov-excl-inf-drama`
- Claim: "governed-shape exclamatory infinitive census in the drama corpus"
- Date: 2026-10-09
- Worker: battery worker (subagent a50607e1-2424-4c51-99c5-98b245ba8dd8)
- Stream: not applicable — corpus-census target; the 1,847-pair repaired
  parse was not used. R5005, sealed gate instances, and the red-team
  adjudication queue were not touched.

Terms (ASD-STE100): "governed exclamatory infinitive" = an infinitive
governed by a preposition (pour / a / de) used as an exclamation in its
own right ("pour rire !" = the infinitive phrase IS the exclaimed
element). "Genuine attestation" = the "!" terminates the governed
infinitive phrase itself; the infinitive is not embedded in a finite
matrix clause whose "!" belongs to the matrix, and not embedded in an
exclaimed noun phrase. "Register" = the ingested drama corpus
(14 distinct plays, one edition per play).

## Duplicate status (stated up front)

The queue entry's `evidence` field carries a supervisor note dated
2026-10-09: this target is "covered by the PROMOTE of
gov-excl-inf-register-drama (battery report 2026-10-09: 1 genuine
'Pour conspirer !' in drama, Scribe Bertrand et Raton). This target's
bar (>=1 genuine re-opens at register level) is satisfied by that
verdict - do NOT dispatch; close as duplicate at run end."

The topup hook dispatched this target despite that note. No second
839-window census was run per the do-not-dispatch instruction.
Instead: (1) the sibling battery's report was read in full and
(2) its key attestation was independently verified byte-exact in the
corpus file. The close below rests on verified bytes, not on trust.

## Parentage

`gov-excl-inf-register-drama` (P2, 2026-10-09, PROMOTE) ran the P1/P2
governed-infinitive census (any topic) against the drama corpus —
839 candidates (524 tight dist<=40, 315 wide), all 839 classified,
1 genuine attestation. Its report is
`code/crowd17/report_inbox/processed/battery-gov-excl-inf-register-drama.md`.
Its queue entry stands at `status: verdict`, `result: promote`.
That verdict is not overwritten or downgraded here.

## Bar (verbatim, pre-registered)

">=1 genuine attestation re-opens at register level; confirmed zero
hardens the fence"

Numbered pass/fail clauses (restated before testing, not modified after):

1. >=1 genuine governed exclamatory infinitive in the drama corpus:
   if yes, the register-level re-open fires (satisfied by the sibling
   battery's verdict + the independent byte check below).
2. Confirmed zero in drama: if yes, the prose null generalizes and
   the fence hardens. ANTECEDENT FALSE — a genuine attestation exists.

## Independent byte verification of the attestation

Target of the check: the sibling report's sole genuine attestation —
Rantzau's standalone turn in Scribe, Bertrand et Raton.

Method: python3 byte read of
`code/side-period/corpus/scribe-bertrand-et-raton.txt`
(182,448 chars, matches the sibling census's per-file size), located
the single case-insensitive occurrence of "pour conspirer", and read
+-context bytes.

Observed (verbatim from the file):

```
LA REINE.
 
Vous me refusez, vous, qui en secret aviez toujours pris ma défense, vous en qui j’espérais !…

RANTZAU.
 
Pour conspirer !… Votre majesté avait grand tort. 

LA REINE.
 
Et pour quelles raisons ? 
```

Classification check: Rantzau's turn is a standalone exclamation —
the "!" (followed by the suspension "…") terminates the
pour-infinitive phrase itself. No finite matrix clause in his turn;
not embedded in an exclaimed noun phrase. Zero topic (elliptical;
the anaphor is the Queen's "Vous me refusez"). It is the
"pour rire !" shape with a non-demonstrative (zero) topic — the
same reading the sibling battery reported. Check PASSES.

## Per-clause pass/fail

1. >=1 genuine governed exclamatory infinitive in the drama corpus:
   **PASS.** 1 genuine: "Pour conspirer !" (Scribe, Bertrand et
   Raton, Rantzau; verified in bytes above). The register-level
   re-open fires: the construction exists in dramatic dialogue, so
   the prose zero is print-register-specific, and the pairing
   (governed exclamatory infinitive + zero/implied topic) is
   re-opened at register level. This concurs with — does not
   re-litigate — the sibling PROMOTE.
2. Confirmed zero hardens the fence: **ANTECEDENT FALSE.** The zero
   does not hold in drama; the fence does not harden on this axis.

## Verdict: PROMOTE (duplicate close)

The pre-registered bar is satisfied by one genuine attestation,
verified byte-exact in the drama corpus. This is a duplicate close
of a target already answered by `gov-excl-inf-register-drama`'s
PROMOTE; no new corpus work was performed, per the supervisor's
do-not-dispatch note recorded in the queue entry. Nothing here
contradicts any standing or red-team verdict; the sibling verdict
stands untouched.

### Caveats (inherited from the sibling battery, stated not hidden)

- The promotion rests on n=1 genuine of 839 candidates.
- The attestation is a dialogue-anaphoric fragment ("[vous me
  refusez] pour conspirer !"), not a fully conventionalized
  standalone like "pour rire !".
- Drama has ~4.5x the "!" density of the prose corpus; dialogue
  ellipsis is the mechanism of the register boundary, not a
  contradiction of the prose null (27,657,940 chars, 0 genuine).

## Adverses, answered

- None pre-registered on this target ("Adverses: none listed" in the
  dispatch brief).
- The duplicate-close instruction in the queue `evidence` field was
  followed: no second worker census, no queue mutation beyond this
  target's own entry.

## Bookkeeping

- Sibling report:
  code/crowd17/report_inbox/processed/battery-gov-excl-inf-register-drama.md
- Sibling census script + JSON:
  code/crowd17/next-token/gov_excl_inf_register_drama_census.py,
  gov-excl-inf-register-drama_census.json (839 candidates with
  prep/infinitive/dist fields; re-runnable).
- Report: code/crowd17/report_inbox/battery-gov-excl-inf-drama.md
  (this file).
- battery-queue.json: `gov-excl-inf-drama` queued -> verdict/promote
  via temp-file + rename (pre-write assert confirmed
  queued/verdictless; JSON re-validated post-write; own entry only;
  no downgrade; claim/bars/evidence/adverses preserved).
- Lock `locks/gov-excl-inf-drama.lock` created on start (agent id +
  UTC timestamp), deleted on completion. No stale lock existed.
- R5005, sealed gates, red-team queue untouched. Every number traces
  to the named corpus file or the sibling census JSON; no invented
  data.
