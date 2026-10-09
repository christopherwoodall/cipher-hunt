# Battery report: modal24-windows-no24

- Target id: `modal24-windows-no24` (priority 3)
- Claim: re-derive the five infinitive-slot legs (80 @564/@672, 89 @221/@985, @1497 weak) under ONLY standing values (R17-009 class-level + A8 verb-frames), dropping the load-bearing battery-grade 24=modal assumption
- Evidence (queue): battery-inf-80-89-ratify.md NULL 2026-10-09, follow-up 2
- Adverses (queue): none
- Date: 2026-10-09
- Worker: battery worker (subagent 600aa63a-9523-4bc7-9e0d-a942b8cfbbd5)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). Verified in-session: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

Terms (ASD-STE100): "leg" = one window supporting the frame. "modal-shaped" = a finite verb that takes bare verb-stem complements (like "pouvoir", "vouloir"). "infinitive-slot" = the position after a modal verb, which only an infinitive can fill. "standing values" = the lane's §7 set (banked pencil GT, red-team grants, battery promotes, provisional). "load-bearing" = the derivation fails without it.

## Bar (verbatim, pre-registered before testing)

"test whether the legs survive on standing values alone"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** Leg 1 (80 @564) parses as infinitive-slot under standing values alone — R17-009 class-level 24 (no battery-grade 24=modal).
2. **C2:** Leg 2 (80 @672) parses as infinitive-slot under standing values alone.
3. **C3:** Leg 3 (89 @221) parses as infinitive-slot under standing values alone.
4. **C4:** Leg 4 (89 @985) parses as infinitive-slot under standing values alone.
5. **C5:** Leg 5 (89 @1497, weak) parses at the same weak/conditional grade under standing values alone.

Verdict rule: promote iff C1–C5 pass. Kill iff a window forces the claim false. Null iff inconclusive (with 1–3 follow-ups).

## Method

Read BATTERY-PROTOCOL.md first. Created `locks/modal24-windows-no24.lock` on start (agent id + 2026-10-09T11:34:50Z); no stale lock present. Pre-write assert: queue entry was `queued` with no prior verdict — held.

The five legs were taken from `battery-frames-80-89-indep.md` (2026-10-08), Section A. That battery derived them with the battery-grade ne-24-profile "24=modal" (2026-10-08 promote, unratified). This battery drops exactly that premise and re-derives each leg using only §7 standing values, chiefly R17-009 (24 = finite verb, modal-shaped, class-level, red-team GRANT PROMOTE) + A8 (80/89 verb-frames). Every @-offset below is a 0-based pair index; the parent's "@N" convention = 24's index, target cell at N+1 (verified byte-exact against the parent's named n-grams).

Standing 24 state, verified in-session from the adjudication records:
- **R17-009** (`next-token-redteam-r17.md` L105–111): "24 = finite verb, modal-shaped — GRANT PROMOTE (class level). Six subordinate finite slots..., infinitive-taking complements (24->85 x5, 24->89 x3, 24->80 x2), postverbal 'pas' x3. The preposition-arm is KILLED... Value ('peut'/'sait'/'doit') unnamed — class-level grant."
- **R18-008** (`next-token-redteam-r18.md` L104–110): 24="faire" REJECTED as promote; survivor set {faire, laisser} stays open; 24="faire" is lead-grade only.
- No coordinated red-team round after Round 18.

The distributional grounding of 24's modal-shapedness (24->85 x5, 85=verb-stem per A3) was re-derived byte-exact in-session: @732 (a5_02), @955 (a6_00), @1438 (a7_08), @1693 (a8_06), @1754 (a8_08). It is independent of 80/89 and of the dropped battery-grade label.

## Window-level evidence

### C1 — 80 @564: PASS

Locus byte-confirmed: `67 11 43 24 80 97` at 561–566, row a3_02 (24@564, 80@565).

Standing parse: 67='et' (positional rule — follower 11='la', not infinitive-shaped; sole polyvalence, standing). 11='la' (banked GT). 24 = finite/modal-shaped verb, infinitive-taking (R17-009, red-team class level). 80 = verb-frame (A8). Composition: "et la [43] [24] [80] [97]" — a modal-shaped finite verb governs a bare infinitive, never a finite verb ("*il peut il vient" is ungrammatical in every period); 80 in verb-class in that slot is therefore infinitive-slot. The subject "la [43]" and object [97] are the leg's own inherited premises (43's class open, slotted — not re-litigated; the bar tests only the 24-premise change).

License check: R17-009's "modal-shaped" + its recorded "infinitive-taking complements" supply exactly the license ne-24-profile's battery-grade "24=modal" supplied. The dropped label did no unique work here.

### C2 — 80 @672: PASS

Locus byte-confirmed: `67 11 86 24 80 03 64` at 669–675, row a5_00 (24@672, 80@673).

Standing parse: "et la [86] [24] [80] [03] qui [37] [77]" — 64='qui' granted; the trailing 77 sits inside the relative clause and does not touch the leg (parent's fence, adopted). 86 = INF-class (A9). Modal 24 + infinitive 80, same composition as C1. The dropped label did no unique work. PASS.

### C3 — 89 @221: PASS

Locus byte-confirmed: `16 24 89 61` at 220–223, wider `29 42 16 24 89 61 96 87 46` at 219–227, row a2_01 (24@221, 89@222).

Standing parse: "[42] [16] [24-modal] [89-infinitive] [61] par ce que" — 96='par' granted, 87='ce' granted, 46='que' banked GT. Subject "42 16" slotted but open (parent's fence, adopted — not re-litigated). Modal 24 + infinitive 89. The dropped label did no unique work. PASS.

### C4 — 89 @985: PASS

Locus byte-confirmed: `01 24 89 48 01` at 984–988, row a6_01 (24@985, 89@986).

Standing parse: "[01] [24-modal] [89-infinitive] [48] [01]". The 48-junction: 48='e' is a standing letter value (§7); "[89]e" left-attachment would unmake the infinitive under the modal governor, so 48 attaches right ("e[01]", 01 open). Both premises are standing: the modal license from R17-009, the letter value from §7. The dropped label did no unique work. PASS.

### C5 — 89 @1497 (weak): PASS at unchanged weak grade

Locus byte-confirmed: `59 24 89 41` at 1496–1499, wider `66 15 59 24 89 41 74 84 33` at 1494–1502, row a7_11 (24@1497, 89@1498).

The "[24] [89]" core is modal+infinitive under R17-009 (same composition as C3/C4). The left junction "59 24" ("est [24]") stays broken under provisional 59='est' — provisional status is standing and unchanged. The leg survives at exactly the weak/conditional grade the parent assigned it; nothing about the 24-premise change touches the 59 junction. PASS (weak, as before).

## Key finding

The battery-grade ne-24-profile "24=modal" was **load-bearing in name only**. R17-009 already grants, at red-team class level, "24 = finite verb, modal-shaped" **with** "infinitive-taking complements (24->85 x5, 24->89 x3, 24->80 x2)" — the infinitive-taking property is inside R17-009 itself, grounded on the A3 (85=verb-stem) distributional leg that is independent of 80/89. Every one of the five derivations consumes only that license. Dropping the unratified battery-grade label changes zero inferences.

Inherited residual (unchanged, priced into the legs by the parent): vouloir/savoir-shaped modals can also take nouns, so the legs are frame-grade, not deductive. This residual persists identically under standing values.

## Scope (what this promote does and does not do)

- PROMOTES: the five infinitive-slot legs survive on standing values alone.
- Does NOT promote 80/89 to infinitive-slot verb-class. The hard contradictions from frames-80-89-indep still block frame independence: @1155 (80=determiner, "pour [92]er [80] fois") and @1376 (89=noun/adverb, "pour [86-inf] [89], on..."). Those belong to the already-queued `noun-89-1377-adjudicate` and `det-adj-80-adjudicate` venues — untouched here.
- No standing or red-team verdict contradicted or downgraded. R17-009, R18-008, A8, A3, A9, §7 all intact. No polyvalence declared.
- Note for red team / supervisor (no queue action taken): `inf-80-89-ratify`'s trigger concern is softened — the legs never needed the unratified battery-grade premise. Whether `inf-80-89-ratify-rerun-gated` (P2) can fire on R17-009 alone, and whether `ratify-24-modal-input` (P2) should absorb this finding, are red-team/queue decisions. This battery takes no action beyond its own entry.
- Canonical-stream caveat stands (68/70 row offsets unvalidated).

## Verdict: PROMOTE

All five bar clauses pass on byte evidence. No adverses were listed.

## Bookkeeping

- Queue: `modal24-windows-no24` → status `verdict`, result `promote`, 2026-10-09 (pre-write assert passed — was `queued`/verdictless; temp-file + rename; JSON re-validated post-write; own entry only; no downgrade).
- Lock `locks/modal24-windows-no24.lock` created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
