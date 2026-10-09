# Battery report: reseg-700-verbal

Worker: reseg-700-verbal subagent (session 2fe87aae-85c7-4332-9f3f-fbd898e6bb5b).
Date: 2026-10-09.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt), parsed per code/side-keyhunt/repair_parse.py
(re-implemented inline; n=1847 asserted, 96 types asserted). canonical.py
never used. R5005, sealed gates, and the red-team adjudication queue untouched.
@i = 0-based pair index.
Lock: code/crowd17/next-token/locks/reseg-700-verbal.lock created at start,
deleted on completion. No red-team verdict on this claim exists.

## Bar (verbatim, pre-registered from battery-queue.json BEFORE testing)

"cite verb-60-bare clause (c) and ne-ce-1169's seg-61-94-word; do not duplicate
their bars. Success reopens the finite-stem rescue; failure hardens the @700
exclusion"

Numbered clauses (fixed before data examination):

1. (C1) Cite verb-60-bare clause (c): 94@699's left neighbor 28 is a hapax
   predecessor ("28 94" x1 stream-wide); the @841 "94 26 12" twin anomaly
   corroborates 94's segmentation problems; no re-segmentation tested there
   produced a grammatical V2 — that is follow-up work, not assumed.
2. (C2) Cite seg-61-94-word: leftward 94 attachment is grant-compatible with
   94='ne' STRONG LEAD (R17-001, clause 4 PASS); the prenne-family precedent
   is stem-12-94 (medial 12 present); 61-94 NULLed, 55-61-94 the new lead.
3. (C3) Test 94-leftward re-segmentation [28-94][60][12][98] at @694-706:
   does a verbal 60 parse grammatically?
4. (C4) Test 12-rightward re-segmentation [28][94][60][12-98], and the
   combined [28-94][60][12-98]: does a verbal 60 parse grammatically?
5. (C5) Demonstration standard: the lane's value standard applies
   (banked/granted/promoted/provisional values only, cf. participle-60 C2).
   Success = a grammatical verbal-60 parse demonstrated; failure hardens
   the @700 exclusion.

Standing values used: banked 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que;
granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 47=ce (A4),
84=on (A15), 12=n, 48=e, 30=pas, 06=ent; battery-promoted 98='vient'
(vient-98-name), 94='ne' STRONG LEAD (R17-001); provisional 59=est, 77=le.

## Method

Fresh parse per protocol; the @694-706 window re-derived byte-exact
(row a5_01): @694=46 @695=02 @696=50 @697=45 @698=28 @699=94 @700=60
@701=12 @702=98 @703=20 @704=12 @705=66 @706=21.
Reads: "que[46] [02] [50] ce[45] [28] ne[94] [60] n[12] [98] [20]..."
Distributional facts re-derived (not trusted from citations):
- "28 94" bigram: x1 stream-wide (@698 only). Confirms verb-60-bare (c).
- "12 98" bigram: x1 stream-wide (@701 only). The @700 "n[98]" contact
  is unique on stream.
- 94 left neighbors: 18 distinct (62 x9, 12/42/82 x3, 61/65/22/78/35 x2,
  28/52/44/32 x1). 28 is a hapax left neighbor.
- 28 profile: n=6; predecessors 45 x2, 89/85/32/07 x1; followers 00 x3,
  94/52/89 x1. 28's value is unnamed and untriangulated.
- 98's value: battery-promoted 'vient' (finite semi-auxiliary,
  vient-98-name); consonant-initial.

## Window-level evidence

The re-segmentation space at @698-702 (28 94 60 12 98) with 60 kept a
standalone verbal unit has exactly four members (fusions swallowing 60 —
[94-60], [60-12], [28-94-60] — either fall to the impossibility proof
([60-12]: no French verb ends in bare -n, cited proof (a)) or abandon
the verbal-60 claim and are out of scope):

**R1 — standing [28][94][60][12][98]** (cited, not re-tested): "ne[94]
[60] n[12] [98]". verb-60-bare impossibility proof: (a) "[60]n"
impossible for every French verb; (b) all "n[98]" word-initial options
fail. FAIL (cited).

**R2 — 94 leftward [28-94][60][12][98]**: "...ce[45] [28]ne [60-verb]
n[12] [98]..."
- DECISIVE STRUCTURAL POINT: 60's right edge is byte-identical to
  standing. The impossibility proof is right-edge-based ("[60]n" /
  "n[98]"); leftward 94 attachment cannot touch the actual blocker.
  Proof (a) applies unchanged: "[60]n" impossible for every verb.
- Proof (b) applies unchanged except one sub-case: the "n'"+vowel-98
  elision option no longer yields double "ne" (94 is no longer the
  particle). But postverbal "n'" is ungrammatical in French of every
  period: "n'" is the elided negator "ne", which must be preverbal.
  "[28]ne [60-finite] n'[98]" = misplaced negator or two finite verbs.
  FAIL on independent grammatical grounds.
- Remaining "n[98]" content-word options need undemonstrated 98 values
  ("non" needs 98="on", contradicting battery-promoted 98="vient";
  "nous"/"notre" need preverbal position or a following noun;
  "nul"/"nom"/"nombre" fail grammatically; "nulle" needs 98="ulle").
  Under battery-promoted 98="vient", "n[98]" = "nvient" — not a word;
  "n'vient" impossible (consonant-initial, no elision).
- Additionally, [28-94] as a word needs 28's value (n=6, unnamed) —
  an unstated assumption under the demonstration standard.
- R2 FAILS twice over: (i) structurally irrelevant to the blocker,
  (ii) needs an undemonstrated 28 value. The 94-leftward rescue avenue
  is dead by deduction, not by lack of evidence.

**R3 — 12 rightward [28][94][60][12-98]**: "...ce[45] [28] ne[94]
[60-verb] [n98]..."
- 94 remains the particle "ne". The "n[98]" options are exactly the
  cited proof (b) — boundary-independent phonology — all fail.
  Under battery-promoted 98="vient": "ne [60] nvient" — no parse.
- Needs 98's value for any content-word option; the battery's best
  98 value ("vient") makes "n[98]" worse, not better.
- R3 FAIL (cited exhaustion + strengthened by 98="vient").

**R4 — combined [28-94][60][12-98]**: "...ce[45] [28]ne [60-verb]
[n98]..."
- Combines R2's and R3's failures; needs BOTH 28 and 98 values.
- Closest approach: "[28]ne [60-finite] non" with 98="on"
  ("il repond non" is grammatical 1841 French). Requires 28 nominal
  ("jeu"-class, undemonstrated) AND 98="on" (undemonstrated, and
  collides with granted 84="on" — would need a red-team homophony
  declaration). Two unstated assumptions plus a §7 cost: fails the
  demonstration standard. Recorded as the strongest killed rival.
- R4 FAIL.

**Scope note**: the prenne-family precedent (cited, C2) is stem-12-94
(medial 12 present). At @700 the shape is 60-12-98, not 60-12-94 —
the precedent does not reproduce here. (Observation, out of scope:
@1735 shows a second 60-12 contact, "60 12 48" = "[60]ne" with
promoted 12="n" + 48="e"; the "[60]ne" word shape is untested for
60's value — suggested follow-up below.)

## Per-clause pass/fail

- C1: PASS (cited verbatim; "28 94" x1 and "12 98" x1 re-derived,
  confirming).
- C2: PASS (cited; leftward attachment grant-compatible, precedent
  shape stem-12-94 noted).
- C3: FAIL at kill grade — 94-leftward is structurally incapable of
  addressing the right-edge blocker; the avenue is dead by deduction.
- C4: FAIL at kill grade — 12-rightward's option space exhaustively
  closed (cited (b) + 98="vient" strengthening); the combined form's
  strongest rival needs two unstated assumptions plus a §7 cost.
- C5: FAIL — no grammatical verbal-60 parse demonstrated under the
  lane's value standard on any re-segmentation.

## Verdict

**KILL** — the re-segmentation rescue of the finite-stem at @700 is
dead. participle-60's explicitly open caveat ("a future re-segmentation
could in principle reopen the rescue") is now closed: 94-leftward
attachment (28-94 span) cannot rescue 60 because the impossibility
proof is right-edge-based and the right edge is byte-identical under
R2; 12-rightward attachment (12-98 span) was already exhaustively
closed and is further closed by battery-promoted 98="vient". Per the
bar, the @700 exclusion is HARDENED: the finite-stem rescue cannot be
reopened via re-segmentation at @694-706.

Scope of the kill (no overreach):
- This kills the re-segmentation rescue hypothesis at @700 only.
- 60's verbal class is untouched: @1338 still forces verbal
  (participle-60 W5, standing). No standing verdict contradicted or
  downgraded: participle-60's NULL (polyvalence question) and
  verb-60-bare's NULL are narrowed, not overturned — this battery is
  the follow-up they explicitly left open. R17-001 (94='ne' STRONG
  LEAD) undisturbed; leftward attachment stays grant-compatible
  (cited C2). §7 untouched: no polyvalence declared.
- poly-60-redteam (queued P1) keeps the global 60 adjudication.

## Suggested follow-up (kill-grade verdict; for supervisor awareness)

1. `ne60-1735-word` (P3): test the "[60]ne" word shape at @1735
   ("06 60 12 48": pas[30] ent[06] [60] n[12] e[48]) — the second
   60-12 contact on stream, where 12's follower is promoted 48="e"
   (unlike @700's hapax 12-98). Bars: one French "[60]ne" word
   (prenne/donne/vienne/tienne family) parsing "…ent [60]ne…" with
   stated 60 value, or fence as a second 60+12 residual.

## Files

- Report: code/crowd17/report_inbox/battery-reseg-700-verbal.md (this file)
- Queue: battery-queue.json `reseg-700-verbal` → status `verdict`,
  result `kill` (own entry only, temp-file + rename; pre-write assert:
  no prior verdict existed)
- Lock: locks/reseg-700-verbal.lock created at start with agent id +
  UTC timestamp, deleted on completion
- R5005, sealed gate instances, and the red-team adjudication queue
  untouched throughout
