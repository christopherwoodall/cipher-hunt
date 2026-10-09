# Battery report: adv-1135-leftward

- Target id: `adv-1135-leftward`
- Claim: "Test 20 as clause-FINAL adverb of the modal clause at @1135 ('...le [86-inf] [20-adv]' = '...le laisser ainsi'-shaped)."
- Date: 2026-10-09
- Worker: battery worker (subagent 57950282-a08a-4c7f-a22e-955aa88dc287)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). Asserts held: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gate instances, red-team queue untouched.
- Lock: `code/crowd17/next-token/locks/adv-1135-leftward.lock` created 2026-10-09T12:20Z; no stale lock existed; deleted on completion.

Terms (ASD-STE100): "clause-final adverb" = a manner adverb that closes a clause ("le laisser ainsi"). "battery grade" = licensed with zero ungranted assumptions. "modal clause" = a modal verb + clitic + governed infinitive ("veut le laisser").

## Bar (verbatim, from battery-queue.json)

"Kill iff no licensed clause-final-adverb frame survives at this window; this is the surviving rival the boundary-adverb must beat."

Numbered pass/fail clauses (pre-registered before testing, not modified after):

1. **C1 (survive):** a licensed clause-final-adverb frame survives at @1135 (modal clause complete on standing values; 20 licensed clause-finally; boundary after 20 licensed).
2. **C2 (kill arm):** no licensed clause-final-adverb frame survives at this window.
3. **Verdict rule:** C2 fires → kill. C1 passes (C2's condition false) → promote (the rival survives the kill test).

Adverses listed: none.

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock on start; deleted on completion.
2. Re-derived the repaired stream byte-exact. All @-offsets below are 0-based.
3. Adopted, never re-litigated: R17-009 (24 = finite/modal-shaped verb class); `infclass-86` PROMOTE (86 = INF-class); 77='le' (provisional, §7); 62='il' (battery promote); 98='vient' (vient-98-name promote); 00='pour' (promoted); `adverb-20-wide` NULL (fence of the *clause-edge* adverb arm; @1135 listed compatible-not-forced for the boundary adverb — a different position from the clause-final manner adverb tested here); `conj-prep-20-wide` NULL; `poly-20-docket` (20's global class = red-team venue, untouched); §7 (67 et/veut sole true polyvalence — this battery names no value, declares no polyvalence).

## Window-level evidence

### The locus — @1130–1142 (rows a6_07/a6_08)

`@1130=37 @1131=86 @1132=24 @1133=77 @1134=86 |@1135=20| @1136=62 @1137=98 @1138=00 @1139=98 @1140=78 @1141=62`

Focal geometry: `…[24] [77] [86-inf] |20| il(62) vient(98) pour(00)…`

### Distributional facts (byte-exact, re-derived in-session)

- n(20) = 15; 20 windows: [280, 307, 490, 642, 668, 703, 741, 760, 839, 873, 958, 1135, 1224, 1270, 1703].
- "86 20" bigram: 1× stream-wide (@1134–1135, hapax — zero repetition leverage, as the sibling recorded).
- "20 62" bigram: 4× stream-wide.
- "24 77 86" trigram: 1× stream-wide (@1132–1134, hapax); the composition is licensed by period grammar, not by distributional repetition.
- The window straddles the a6_07/a6_08 row join at @1132|@1133.

### C1 — PASS: the licensed frame survives, element by element

1. **Modal clause composition (licensed, zero new assumptions).** @1132=24 (R17-009 finite/modal-shaped) + @1133=77 ('le', provisional — a usable §7 tier) + @1134=86 (INF-class) composes as modal + clitic + governed infinitive ("veut le laisser"-shaped) on standing values alone. If 24 were read plain-finite (non-modal), "…[24-fin] le [86-inf]" would be ungrammatical — the modal reading is the only licensed one (adopted from the sibling battery's finding).
2. **The modal clause is syntactically complete at @1134.** "Veut le laisser" is a complete VP: 'laisser' as governed infinitive takes no required complement. Nothing in the frame forces continuation past @1134 — the infinitive does not leak rightward.
3. **Manner adverb clause-final is licensed 1841 French.** A manner adverb closes a complete clause in final position ("le laisser ainsi", "le faire bien", "le dire haut"). 20's value is open at battery grade; no standing verdict forces 20≠adverb at this window. (The `adverb-20-wide` NULL fenced the *clause-edge* adverb arm, a different syntactic object; it never tested or killed the clause-final manner-adverb position.)
4. **Unmarked boundary after 20 is licensed.** The new clause head "il(62) vient(98) pour(00)…" is clean on standing values (62='il' promote, 98='vient' promote, 00='pour' banked). An unmarked clause boundary before "il" is battery-grade standard — the sibling battery already recorded that the boundary-after-20 placement costs exactly the same single unmarked-boundary assumption as the boundary-before-20 rival.
5. **Nothing in the window breaks the frame.** No kill-grade successor/predecessor force, no polyvalence declaration, no red-team verdict contradicted.

### C2 — does not fire: every honest kill vector fails

- **Incompleteness kill?** Would need the modal clause to require a complement past @1134. It does not (see C1.2). Failed.
- **Adverb-position kill?** Would need French to bar clause-final manner adverbs. It licenses them. Failed.
- **Value-forcing kill?** Would need a standing verdict forcing 20 to a non-adverb class here. None exists; the registry has no 20 entry and the noun-20 rival is red-team venue, unadjudicated — but the bar's kill condition is about *this frame's license*, not about uniqueness against a live rival. Failed.
- **Boundary-cost kill?** Would need the boundary-after-20 placement to cost more than licensed. It costs one unmarked boundary — standard. Failed.
- **Wide-fence inheritance kill?** Would need `adverb-20-wide`'s fence to cover the clause-final manner position. Its bar tested the clause-edge adverb ("a word that modifies a whole clause… sits at a clause edge"); @1135 was listed compatible-not-forced even for that arm. The clause-final manner adverb was never in its scope. Failed.

## Verdict: PROMOTE

The kill condition does not fire. The clause-final-adverb frame ("…[24] [77] [86-inf] [20-adv]. il vient pour…" = "veut le laisser ainsi"-shaped) survives at battery grade with zero new assumptions. The rival the boundary-adverb must beat stays alive.

## Scope

- Window-level only (@1135). 20's global class stays red-team venue (`poly-20-docket`, queued, untouched).
- No value named for 20. No polyvalence declared. §7 intact.
- The boundary-adverb rival's fence (sibling NULL) is untouched; the noun-20 rival is untouched.
- No standing or red-team verdict contradicted or downgraded: R17-009, `infclass-86`, `adverb-20-wide`, `conj-prep-20-wide`, `poly-20-docket` all used as premises, none re-opened.
- Canonical-stream caveat stands (rows a6_07/a6_08 offsets unvalidated; the window straddles the row join, but pair-phase is unaffected).

## Follow-ups

None required (promote per §4). The natural continuations are already queued: `bound-1132-modal-edge` (P3 — whether naming 24's value fixes the modal clause's right edge, which would force the boundary before 20) and `noun20-1135-gated` (P4 — noun-20 rival once the red team adjudicates `poly-20-docket`). Both verified present in `battery-queue.json`.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-adv-1135-leftward.md` (this file).
- Queue: `adv-1135-leftward` queued → verdict/promote, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/adv-1135-leftward.lock`: created on start (no stale lock), deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
