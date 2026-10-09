# Battery report: reseg-3006-w35

Target: `reseg-3006-w35`. Claim: re-segment W3 @1327 ('98 56 30 06 62 94')
and W5 @1733 ('01 56 30 06 60') with the 'pas | [06...]' boundary shift.
Date: 2026-10-09. Worker: a7c69cda-fb6f-49c0-a673-a52f64b965a4.
Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`, parsed like `code/side-keyhunt/repair_parse.py`;
1,847 pairs re-verified). Never used `canonical.py`. R5005, sealed gates,
red-team queue untouched. Context: pasent-subject-26-56 kill (2026-10-09)
follow-up #2.

## Bar (verbatim, pre-registered BEFORE testing)

"per-window grammatical parse (test 'pas | [06...]' - 06='ent' as next word's
onset vs previous word's ending) or fence with stated cause; W3 must reconcile
'62 94', W5 must place 56 and 01"

Numbered clauses (fixed before testing, not modified after):

1. C1 — W3 @1327 yields a grammatical parse testing both 06 arms
   (Arm A: 06='ent' as next word's onset, "pas | ent…";
   Arm B: 06='ent' as previous word's ending, "…pasent | …"),
   OR W3 is fenced with stated cause.
2. C2 — W5 @1733 yields a grammatical parse testing both 06 arms,
   OR W5 is fenced with stated cause.
3. C3 — W3's "62 94" is reconciled (named values, stated reading).
4. C4 — W5's 56 and 01 are placed in their live arms
   (56 adverb/noun per brief; 01 per ci-01-value).

## Method

Re-parsed the repaired stream in-session. Byte-confirmed both target windows
and the "30 06" x4 / "62 94" x9 / "06 62" censuses below. Tested Arm A
(06 word-initial: "ent"+follower must open a French word) and Arm B
(06 word-final: "pas"+"ent" must close a French word) at each window under
standing values. Standing values used: 30='pas' (battery-promoted, pas-30,
conditional pending ratification); 06='ent' (battery-promoted, ent-06);
94='ne' (battery-promoted, ne-94); 12='n', 48='e' (letters, n-e-12-48);
70='pre', 29='er', 11='la' (pencil); 84='on' (A15), 87/47='ce', 64='qui',
96='par', 17='fois', 79='tout', 00='pour' (granted); 59='est', 77='le'
(provisional); 62='il' (demonstrated rival, NOT promoted; 62='on'
unconditioned KILLED per collision-62-84); 24=finite verb, modal-shaped
(ne-24-profile, class-level); 98 verb-shaped (frame-vient-parvenir);
80 verb-class (A8); 03 verb-stem (stem-03, promoted); 39='a/a'
(battery-promoted, a-39); 01: 'ci'/'faisant' general KILLED, bound "-ci"
fenced (ci-01-value); 56: subjecthood KILLED (pasent-subject-26-56);
23~26 SPLIT (A2); 67 sole polyvalence (§7).

## Window-level evidence (@-offsets, byte-confirmed)

Target windows:
- W3 @1327 (a7_04): `…03 29 80 08 | 62 98 56 [30] 06 62 94 70 52 39 83…`
  Byte check: @1324=62, @1325=98, @1326=56, @1327=30, @1328=06,
  @1329=62, @1330=94, @1331=70.
- W5 @1733 (a8_07): `…88 24 30 15 01 56 [30] 06 60 12 48 52 86 12…`
  Byte check: @1728=24, @1729=30, @1730=15, @1731=01, @1732=56,
  @1733=30, @1734=06, @1735=60, @1736=12, @1737=48.

Census (re-derived on repaired stream):
- "30 06" exactly x4 stream-wide: @1251, @1327, @1561, @1733 (matches
  spell-single-consonant).
- "62 94" x9: @100, @508, @761, @840, @1329, @1362, @1686, @1704, @1772.
  W3's @1329-1330 is instance 5 of 9.
- "06 62" HAPAX @1328 (W3 only). Zero other stream precedent for
  06 word-initial before 62.
- "06 60" x2: @1562 (W4, excluded window "11 26 30 06 60…") and @1734 (W5).
- "06 65" x2: @1252 (W2) and @1747 ("56 40 06 65" = "[56] e ent [65]").
- "01 56" x2: @1653 ("82 16 01 56 37 11…") and @1731 (W5).
- No 94 in the 20 pairs before W3's 'pas' (@1327): no 'ne' available
  for a backward "ne…pas" pairing. No 30 in the 60 pairs after W5's
  12-48 (@1736-1737): no forward 'pas' for a "ne…pas" pairing there.
- W5 left wide (@1700-1732): `33 94 30 20 62 94 88 26 12 06 29 40 65 94 44
  59 30 64 47 68 06 11 52 37 43 98 39 88 24 30 15 01 56` — contains the
  pas-30 flagship "65 ne 44 est pas" (@1712-1716), the ent-06 la-frame
  "68 06 11" (@1719-1721), and "[24] pas" (@1728-1729, ne-drop, 3rd
  instance per ne-24-profile).

### W3 @1327 parse attempt

`…[03]er [80-verb] [08] | il(62) [98-verb] [56] pas(30) | [06] |
il(62) ne(94) pre(70)[52] a(39) [83]…`

- Left edge: "03 29 80" = "[03]er [80]" (infinitive + verb-locked 80, A8).
- "62 98 56 30" = "il [98-verb] [56-adv/noun] pas": subject + verb +
  adverb/noun complement + 'pas' with 'ne' dropped. The author's ne-drop
  with postverbal 'pas' is attested ("[24] pas" x3, ne-24-profile).
  GRAMMATICAL under the brief's 56 arms.
- "62 94 70 52 39 83" = "il ne pre[52] a [83]": 'ne' + verb starting
  "pre" + "a" + 83. Lone-'ne' is the author's norm (34/37 baseline,
  ne-24-profile); 39='a' battery-promoted. GRAMMATICAL shape
  (pending 52/83 values). This reconciles "62 94" as 'il'+'ne'.
- 06 stranded between the two clauses:
  - Arm A ("pas | ent…"): the next word would be "ent"+"62"+… =
    "entil…" — not a French word (62='il'-rival). "06 62" is a hapax:
    zero stream precedent for 06 word-initial before 62. Re-reading 62
    to salvage "ent"+[62] would break the "62 94"='il'+'ne'
    reconciliation (C3). FAIL.
  - Arm B ("…pasent | …"): "pasent" is not a French word; the clerk
    single-consonant license for it is dead at kill grade
    (spell-single-consonant: "prenne" doubled-n contradiction). FAIL.

### W5 @1733 parse attempt

`…[88] [24-verb] pas(30) | [15] [01] [56] pas(30) | [06] |
[60]ne(12-48) [52] [86] n(12)…`

- "[88] [24] pas" @1727-1729: verb + postverbal 'pas', ne-drop
  (3rd instance). Clause boundary after @1729's 'pas' — consistent with
  pas-30's "clause-boundary adjacency" fence for the double-30
  @1729/@1733.
- New clause "[15] [01] [56] pas": under the brief's arms, 15 is open,
  01 is nominal (general 'ci'/'faisant' killed; bound "-ci" fenced),
  56 is adverb/noun. NO finite verb is present for 'pas' @1733 to
  negate. Contrast: every attested postverbal-'pas' window has a verb
  ("[24] pas" x3). 'pas' @1733 is verbless under the brief's arms.
- 06 stranded:
  - Arm A ("pas | ent…"): "ent"+"60"+… — 60's value open; no French
    word forms. "ent[60]ne" as "entonne" would need 60='on': zero
    independent support in 60's census (n=18; pre 21 x4/92 x2/14 x2,
    suc 03 x4/08 x2/71 x2/67 x2). "06 60" x2 is shared with excluded
    W4 — no word-formation precedent. FAIL.
  - Arm B ("…pasent | …"): "pasent" not a French word (same as W3). FAIL.
- Fenced alternative (OUTSIDE the brief's arms — noted, not adopted):
  56=verb is attested ("qui 56" @794, pasent census). Under 56=verb,
  "[01-subj] [56-verb] (ne) pas" parses with ne-drop, and parallels
  @1653 "01 56 37" as "[01] [56-verb] [37]". But 06 remains stranded
  under both arms even so. Owned by follow-up 2.

## Per-clause results

- **C1 — FENCE (W3).** Both 06 arms fail with stated cause: Arm A forces
  "entil…" (non-word; "06 62" hapax, zero precedent); Arm B forces
  "pasent" (non-word; clerk license dead). The flanking clauses parse
  ("il 98 [56] pas" with ne-drop; "il ne pre[52] a [83]" with lone
  'ne'), which isolates 06 — not the surroundings — as the problem.
  Failure is epistemic (depends on open 62), not a forced falsehood.
- **C2 — FENCE (W5).** Both 06 arms fail with stated cause: Arm A has no
  word ("ent"+[60], 60 open; "entonne" needs unsupported 60='on';
  "06 60" x2 no precedent); Arm B is "pasent" (non-word). Independently,
  'pas' @1733 is verbless under the brief's 56 arms ("[15] [01] [56]"
  has no finite verb). The verb-56 rescue ("[01] [56-verb] pas") is
  fenced as outside the brief's arms — and still strands 06.
- **C3 — PASS.** W3's "62 94" reconciles as 'il' (demonstrated rival) +
  'ne' (battery-promoted): "il ne pre[52] a [83]". @1329 is instance 5
  of the 9-window "62 94" series; zero crossover tension (62->59 x0
  per collision-62-84).
- **C4 — PARTIAL.** 56 placed in adverb/noun arms at both windows
  (W3: "il 98 [56-adv/noun] pas"; W5: "[01] [56-adv/noun]"); 01 placed
  as nominal (subject-shaped in the "01 56" x2 parallel; general values
  killed per ci-01-value). Placement does not yield a full parse
  (verbless 'pas' at W5; stranded 06 at both).

## Adverses (answered, not ignored)

- "56 adverb/noun arms per pasent-subject-26-56 census": HONORED. Both
  windows tested under adverb/noun 56 only. The attested verb leg
  ("qui 56" @794) is noted as a fenced alternative for W5, not adopted.
- "W3's '62 94' ('il'-rival + 'ne') independently blocks 'passent'":
  ACKNOWLEDGED — the 'passent' reading is not revived anywhere in this
  report. "62 94" is reconciled inside the new parse (C3), not around it.
- "W3's 98-as-subject fenced (98 verb-shaped)": HONORED. 98 stays verbal
  ("il [98-verb] …"); no subject reading is proposed.

## Verdict

**NULL** — both windows fence with stated cause; neither parses under
either 06 arm. The failures are epistemic (open 62/60/15/01 values), not
forced falsehoods: the "pas | [06…]" shift itself is not contradicted
(it follows from the independently promoted 30='pas' per the wordbound
battery). No standing verdict is contradicted or downgraded
(pasent-subject-26-56 KILL upheld; 06='ent', 30='pas', 94='ne', 62='il'
rival, §7 all untouched). No escalation needed.

## Follow-ups proposed (all verified absent from battery-queue.json)

1. `w3-06-attach-62` (P2) — W3's stranded 06, re-tested once 62's value
   is named. Bar: 06 placed in a grammatical word at W3 ("ent"+[62] iff
   62 names a compatible continuation; else 06 attaches left or fences
   as a genuine residual, which re-opens the two-word "pas | ent"
   shift) or 06 fenced as residual with stated cause. Narrower than the
   wordbound battery's unqueued `ent-right-attach-sweep` (W3-specific,
   62-gated).
2. `w5-pas-verb` (P2) — W5's verbless 'pas'. Bar: name a finite verb in
   "[15] [01] [56]" that 'pas' @1733 negates (test 15/01 verb-hood;
   test 56=verb via "qui 56" @794 and the "01 56" x2 subject+verb
   parallel @1653/@1731), or fence 'pas' @1733 as ungrammatical under
   30='pas' — which re-opens pas-30's "zero contradictions" claim.
3. `entonne-60-gate` (P3, gated on 60's value) — if 60 names as 'on',
   "06 60 12 48" @1734-1737 = "entonne" (ent+on+ne) gives Arm A a real
   word at W5; re-run the W5 parse under "…[56] pas | entonne | …".
   Bar: "entonne" parses as a verb (3sg or imperative) with its
   argument frame, or the gate closes.

## Bookkeeping

- Report: this file.
- battery-queue.json: `reseg-3006-w35` → status `verdict`, result
  `null`, date 2026-10-09 (temp-file + rename, own entry only;
  pre-write re-read; JSON re-validated post-write).
- Lock `locks/reseg-3006-w35.lock`: created on start, deleted on
  completion. No pre-existing lock was present.
