# Battery report — ce86-le86-parity

Date: 2026-10-09. Worker: subagent 1ba680b2-ab7c-4086-bf00-52b1dca4aecb (battery worker).
Lock: `code/crowd17/next-token/locks/ce86-le86-parity.lock` (created
2026-10-09T18:16:00Z; no prior lock existed; deleted on completion).
Target id: ce86-le86-parity. Queue status at take: queued, priority 4,
verdict null. Stream: repaired 1,847-pair / 96-type parse
(`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed per `code/side-keyhunt/repair_parse.py`; n=1847 and 96 types
asserted in-session). `canonical.py` never used. R5005, sealed gate
instances, red-team adjudication queue untouched. No data invented; every
number re-derived below. @-offsets are 0-based stream indices.

## Bar (pre-registered verbatim from battery-queue.json, BEFORE testing)

"resolve iff the ce-pair and le-quadruple profiles are parity-compatible
(same noun-class behavior) or the divergence is characterized with stated
cause"

### Numbered clauses (operative, pre-registered)

1. Census L2/L1/R1/R2 contact classes for the 6 windows byte-exact on the
   repaired stream (@175/@1345 ce-pair; @799/@878/@951/@1134 le-quadruple),
   graded against standing values (pencil + red-team-granted = grant
   grade; 59/77 = provisional).
2. Test parity-compatibility: same noun-class behavior holds iff no
   grant-grade contact in either set forces 86 out of the masculine-noun
   class AND gender behavior is identical across the two determiners.
3. RESOLVE (not null) iff C2's parity arm passes → the ce-masc/le-masc
   merge is supported for `masc-noun-86-name`; otherwise characterize the
   divergence with stated cause and keep them separate.

Adverses (pre-registered): none listed.

## Method

1. Re-parsed the repaired stream; asserted 1,847 pairs / 96 types.
2. Extracted the 6 commissioned windows byte-exact; verified all match the
   windows claimed in battery-noun-86-dlife (no re-litigation, adoption
   confirmed):
   - @175 (a1_05): `60 09 87 [86] 21 69 14` — "…09 ce(87=ce GRANTED) [86]
     [21] [69]…" — matches prior "09 87 [86] 21 69". ✓
   - @1345 (a7_05): `52 38 47 [86] 66 73 34` — matches prior
     "38 47 [86] 66 73". ✓
   - @799 (a5_04): `37 44 77 [86] 44 74 62` — matches prior
     "44 77 [86] 44 74". ✓
   - @878 (a5_08): `49 16 77 [86] 78 17 08` — matches prior
     "16 77 [86] 78 17". ✓
   - @951 (a6_00): `86 01 77 [86] 96 87 46` — matches prior
     "01 77 [86] 96 87". ✓
   - @1134 (a6_08): `86 24 77 [86] 20 62 98` — matches prior
     "24 77 [86] 20 62". ✓
3. Graded every contact cell against protocol §7 standing values.

## Contact-profile census (grant grade in caps)

ce-pair:
- @175:  L2=09(open) L1=87=CE(G) [86] R1=21(open) R2=69(open)
- @1345: L2=38(open) L1=47=CE(G) [86] R1=66(open) R2=73(open)

le-quadruple:
- @799:  L2=44(open) L1=77=le(P) [86] R1=44(open) R2=74(open)
- @878:  L2=16(open) L1=77=le(P) [86] R1=78(open) R2=17=FOIS(G)
- @951:  L2=01(open) L1=77=le(P) [86] R1=96=PAR(G)  R2=87=CE(G)
- @1134: L2=24(open) L1=77=le(P) [86] R1=20(open) R2=62(open)

## Findings

**Gender behavior — identical, no divergence.** "ce" (87/47, granted)
and "le" (77, provisional) are both masculine-singular determiners.
Both sets present the frame [masc-sing-det] [86]; no set shows a
feminine or plural anchor.

**Class behavior — no grant-grade contact forces 86 out of noun class
in either set.** The only grant-grade contacts among the 24 cells:
- @951 R1=96=par: "le [86] par ce que" — noun + par-PP is a licensed
  nominal frame; admits many masculine nouns, discriminates none.
- @878 R2=17=fois: "le [86] [78] fois" — noun followed by a nominal
  modifier + "fois"; licensed.
- @951 R2=87=ce: nominal continuation; licensed.
All open contacts (L2 {09,38} vs {44,16,01,24}; R1 {21,66} vs
{44,78,20}; R2 {69,73} vs {74,62}) are unvalued at grant grade —
consistent with the noun-86-dlife finding that no discriminating
contact clue exists on either side.

**The one asymmetry is evidence grade, not behavior.** The ce-pair's
determiner is granted; the le-quad's is provisional (77="le"). This is
a property of the anchors, not a divergence in 86's contact behavior,
and it is carried as a standing caveat: if 77="le" ever dies, the four
le-windows lose their determiner anchor and the merge moots. It does
not separate the two sets while the provisional holds.

**Statistical note (honesty clause).** With n=2 vs n=4 and all
discriminating contacts unvalued, a formal indistinguishability test
(Fisher/permutation per the follow-up's suggestion) has no power; the
parity claim is at the "no forced divergence" level, not at a positive
statistical level. This is recorded, not hidden: the merge is supported
as "not ruled out by the bytes," not as "proven identical."

## Per-clause pass/fail

1. Census: PASS — all 6 windows byte-exact, all 24 contacts graded.
2. Parity-compatibility: PASS — identical gender behavior; no
   grant-grade contact in either set forces a non-nominal class.
3. RESOLVE: fires on the parity arm → ce-masc and le-masc may be kept
   as ONE masculine-value hypothesis for `masc-noun-86-name`. The
   divergence arm does not fire (no stated-cause divergence found).

## Adverses / §5.2 check

- None listed pre-registration. §5.2: the noun-86-dlife KILL (uniform
  noun VALUE over all D-windows, forced false by the @671 feminine
  split) is untouched — this merge covers only the masculine windows
  and names no value. The partition battery's noun CLASS promotes on
  det-left 3 and 77-adjacent 4 are consistent with the merge
  (class-level, not value-level). No standing or red-team verdict
  contradicted, downgraded, or re-litigated. §7 intact (no polyvalence
  declared; one value hypothesis, not two values).

## Verdict: PROMOTE (merge hypothesis)

The ce-pair (@175/@1345) and the le-quadruple
(@799/@878/@951/@1134) are parity-compatible: same masculine-singular
determiner frame, same noun-class behavior, no forced divergence. The
two sets may share ONE masculine value hypothesis, to be named (or not)
by `masc-noun-86-name`. This promotes the merge, not a value: 86's
value remains unnamed (noun-86-dlife kill stands), and the feminine
@671 window is outside this merge's scope. Caveats carried: (a) the
le-side anchor 77="le" is provisional; (b) parity is at the
no-forced-divergence level given n=2/4.

No follow-ups required (promote); one optional note for the supervisor:
`masc-noun-86-name` may now proceed on the merged 6-window hypothesis
set per the merge — the discriminator hunt it prescribes is unchanged.

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-ce86-le86-parity.md
- Queue: ce86-le86-parity → status verdict, result promote, 2026-10-09
  (pre-write assert passed — was queued/verdictless; temp-file +
  rename; disk re-validated; own entry only; no downgrade).
- Lock created on start, deleted on completion (verified gone). R5005,
  sealed gates, red-team adjudication queue untouched.
