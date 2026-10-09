# Battery report: fem32e-1211-redteam-input

**Target:** `fem32e-1211-redteam-input` (P2)
**Date:** 2026-10-09
**Worker:** battery worker fem32e-1211-redteam-input, agent 88e20a7f-ca63-4267-95ee-ff4b4d69cd62
**Verdict:** PROMOTE (ruling-ready input package grade)

## Bar (verbatim from battery-queue.json)

"produce the ruling-ready statement with @-offsets (449/855/1176/1211) and the three clean copula parses; no battery-level duality declaration; flag the 65-gender dependency (feminine 65 follows only via predicative agreement on 32's adjective arm)."

Numbered clauses (restated before testing, not modified after):
1. The ruling-ready statement is produced with @-offsets 449/855/1176/1211 and the three clean copula parses.
2. No battery-level duality declaration is made.
3. The 65-gender dependency is flagged.

## Method

Read BATTERY-PROTOCOL.md first. Created `locks/fem32e-1211-redteam-input.lock`
on start. Re-derived the repaired 1,847-pair / 96-type stream in-session from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
(asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed
gates, red-team adjudication queue untouched. Adopted as premises (not
re-litigated): battery-fem-32e.md (NULL), battery-det-65-gender-adjudicate.md
(NULL), adj-32 (NULL), 48='e' letter-tier grant (R17). All @-offsets are
0-based pair indices; independently re-verified below.

## Independent byte re-verification

- `32 48` bigrams stream-wide: exactly 4 — @449, @855, @1176, @1211. Zero `48 32`.
  Closed set confirmed byte-exact on the re-derived stream.
- @449 (row a2_09): `10 62 61 59 32 48 79 17 77 60 65` — "61 59 [32 48]" =
  "[subject] est 32e", then "79 17" = "tout fois".
- @1211 (row a7_00): `21 65 64 59 32 48 96 45 36 77 83` — "65 64 59 32 48 96" =
  "65 qui est 32e par".
- @1176 (row a6_10): `21 85 36 74 32 48 59 37 77 78 94` — "74 32 48 59" =
  "74 32e est".
- @855 (row a5_07): `67 91 51 64 32 48 84 02 24 49 74` — "51 64 32 48 84 02" =
  "[51] qui 32e on [02]".

## Ruling-ready statement (for the red-team 32-duality docket)

**Question:** does the '32 48' contact resolve as feminine inflection
("32e" = adjective/past-participle stem + granted 'e') under the
32-duality adjudication?

**Evidence for the feminine -e reading (battery grade):**
- **E1 — closed set.** Exactly 4 '32 48' bigrams stream-wide (@449, @855,
  @1176, @1211), zero '48 32'. The contact is a stable closed family, not
  accidental adjacency.
- **E2 — morphology intact everywhere.** 48='e' is a letter-tier R17 grant;
  no window forces a non-'e' reading of 48, and "32e" has no competing
  morphological segmentation under standing values.
- **E3 — three clean copula parses:**
  - @449: "est 32e" after a subject slot (predicative adjective frame,
    clean under provisional 59='est'). Tail "tout fois" is fenced to the A5
    'tout' docket (fem-32e adverse (b)); it does not disturb the copula core.
  - @1211: "qui est 32e par" — the canonical passive shape "est [feminine
    PP] par [agent]" (64=qui granted, 96=par granted). The strongest leg:
    the "par" continuation is grammatical only under a passive-participle
    reading of the head.
  - @1176: "32e est" — nominalized feminine subject + copula ("[the] 32e is
    [37]"), residual noted: determination of the subject is open (74 @1175
    may supply it or belong to the previous clause).
- **E4 — the @855 residual is fenced, not fatal.** "qui 32e on" admits no
  grammatical parse under standing values and no byte-evidenced clause
  boundary (row a5_07 is continuous). The morphology is intact there; the
  failure is syntactic-integration, recorded as epistemic (fem-32e C1).

**Evidence limiting the reading (battery grade):**
- **L1 — 32's adjective arm is unresolved.** adj-32 verdict: NULL. The
  copula parses license the *frames*, not the stem value; a non-adjective 32
  (e.g. nominalized participle with invariant -e) remains open at battery
  grade.
- **L2 — the 65-gender dependency (flagged).** At @1211, the relativized
  subject is 65: "65 qui est 32e par". If 32e is a feminine agreeing form,
  predicative agreement requires a feminine (or gender-unmarked) 65.
  battery-det-65-gender-adjudicate NULL: 65's gender is unadjudicated; the
  masculine "tout 65" leg (@1683, subject parse confirmed by reseg-13-armA
  PROMOTE) is currently the stronger of the two legs. **Consequence: a
  feminine-32e reading at @1211 either (a) implies feminine 65 — the red
  team must resolve the gender tension — or (b) requires 32e to be a
  gender-invariant form.** This dependency is live for the docket, not
  decidable at battery level.
- **L3 — @855 is unresolved.** Any ruling that declares "32e" a clean
  feminine form must either resolve the @855 residual or scope the claim
  to the three copula windows.

**Adverses answered:**
- 48='e' letter-tier grant (R17): adopted as premise, re-verified
  byte-exact in the closed-set census above.
- 32's adjective arm unresolved (adj-32 NULL): recorded as L1; no
  battery-level duality declaration is made (clause 2).
- Coordinate with the red-team 32-duality docket: this input is evidence,
  not a ruling; nothing in it duplicates the docket's bar.

## Per-clause pass/fail

1. **PASS.** The ruling-ready statement is produced above with @-offsets
   449/855/1176/1211 and the three clean copula parses (@449, @1211, @1176),
   each independently re-verified on the repaired stream.
2. **PASS.** No battery-level duality declaration: L1–L3 state the open
   arms explicitly; the fence from fem-32e NULL stands undisturbed.
3. **PASS.** The 65-gender dependency is flagged (L2): feminine-32e at @1211
   implies feminine 65 via predicative agreement, in tension with the
   currently stronger masculine "tout 65" leg; resolution is red-team venue.

## Verdict: PROMOTE (ruling-ready input package grade)

The @1211 feminine -e evidence is packaged as a complete ruling-ready input
for the red-team 32-duality docket: byte-verified closed set, three clean
copula parses, fenced @855 residual, stated limitations, and the live
65-gender dependency. No standing or red-team verdict contradicted or
downgraded; §7 intact (no polyvalence declared — determiner↔pronoun-style
inflectional duality is the docket's to adjudicate, not a battery claim).

## Follow-ups

None required (promote of a package, not a null). Natural downstream venues
already exist: `adj-32-inflect-gate` (P2), `qui32e-855-reseg` (P3),
`fem32e-subject-gender` (P3) — all queued.

## Bookkeeping

- `battery-queue.json`: `fem32e-1211-redteam-input` queued → verdict/promote
  (temp-file + rename; pre-write assert confirmed no prior verdict; JSON
  re-validated; only this entry touched).
- Lock `code/crowd17/next-token/locks/fem32e-1211-redteam-input.lock` created
  2026-10-09T08:28:59Z, deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
