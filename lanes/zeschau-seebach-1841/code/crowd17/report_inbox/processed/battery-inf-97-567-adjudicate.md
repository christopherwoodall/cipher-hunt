# Battery report: inf-97-567-adjudicate

- Target id: `inf-97-567-adjudicate`
- Claim: "test @567 "80 97" under modal-80 vs object-noun readings; sharpest INF/NOM discriminator (NOM clean, INF needs modal-80)"
- Date: 2026-10-09
- Worker: battery worker (subagent 46b57b01-7eb1-4dae-8641-fa333fb59473)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed like `repair_parse.py`); asserts held (1847 pairs, 96 types). `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

## Bar (verbatim, pre-registered before testing)

"resolve iff one reading parses with zero ungranted assumptions"

Numbered pass/fail clauses (restated before testing, not modified after):

1. The modal-80 reading (80 = modal governing 97-infinitive) parses with zero ungranted assumptions.
2. The object-noun reading (80 = verb, 97 = noun object) parses with zero ungranted assumptions.
3. Iff exactly one of C1/C2 holds, resolve for that reading. Iff neither or both, NULL.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/inf-97-567-adjudicate.lock` on start (agent id + 2026-10-09T12:37:00Z); no stale lock present.
2. Re-derived the locus on the repaired stream (1-based positions): @565=80, @566=97, row a3_02; full 1-based window @563–@571: `43 24 80 97 13 76 45 94 52`. "80 97" is a stream hapax (only @565–566 in 1-based; n(80)=17).
3. Tested both readings against CURRENT standing values, including Round-19 rulings (R19-045: 43=[noun,cls]; R19-120: 80 global class stays verb-frame A8, no second class declared; R19-191/R24: 24='en' iff follower=85, else finite/modal verb; R19-167/R19-168: 94 split closed).
4. Reused adopted battery verdicts without re-litigating: val-97-verb-test NULL (INF/NOM tie preserved, FIN-97 kill-grade dead), frame-97-profile PROMOTE (97 infinitive-class), noun-97-568 KILL (the @567/568 wall stands independent of 97's class).

## Window-level evidence

- **Left frame @563–@565:** `43 24 80`. 43 = noun-class (R19-045, granted). 24's follower is 80 (not 85), so 24 = finite/modal verb under R24 (class-level license, R17-009). The class-level 24→80 modal+governed-infinitive leg is licensed (this is one of the two 24→80 legs; R19-120 notes the legs now load on the modal arm, no longer the stale 24=finite premise).
- **Locus @565–@566:** `80 97`. 80 = verb-frame (A8); value open. 97 = infinitive-class (battery PROMOTE, frame-97-profile); noun arm live as preserved tie; finite/imperative arms killed.
- **Right frame @567–@568:** `13 76`. 13 = fenced residual (letter-13-verdicts / split-13-redteam queued); 76 = [noun,prom] masculine (R19 upgrade). The noun-97-568 battery closed the @567/568 wall independent of 97's class — the wall belongs to 13, not to this target.

## Per-clause pass/fail

**C1 — modal-80 reading: FAIL.** The INF reading needs 80 to govern 97 as its infinitive ("modal-80 + 97-inf", "veut pouvoir dire"-shaped). Modal-80 has no grant anywhere: the parent battery called it "unlicensed; 80's value open"; R19-120 kept 80's global class at verb-frame per A8 with no second class declared, and granted only locus-conditioned window findings (imperative @644-conditional, determiner @1156-scoped) — neither names a modal arm. No battery-grade modal-shaped 80→infinitive leg exists in any of the 17 80-windows. Modal-80 is an ungranted assumption, so C1 fails.

**C2 — object-noun reading: FAIL (strict bar).** The reading is "[80-verb] [97-noun]" object ("dire merci"-shaped; also licensed as "[24-modal] [80-inf] [97-noun-object]"). Its components: 80 = verb (A8, granted); 24 = finite/modal (R24, granted); 76 = noun (R19, granted). But 97 = noun is the preserved tie arm — live, evidence-backed (three clean favoring windows @526/@567/@1413), but NOT granted at any grade. The tie is explicitly unadjudicated (val-97-verb-test NULL). Noun-97 is therefore an ungranted assumption under the bar's letter, so C2 fails the zero-ungranted-assumptions test.

**C3: neither C1 nor C2 holds → NULL.** The discriminator does not discriminate at battery grade under the pre-registered bar. The parent's qualitative labels stand unchanged: NOM remains the favored reading at this window (uses only live premises), INF remains strained (needs an unlicensed value). Nothing is killed: modal-80 is unfalsified (merely unlicensed), and noun-97 is unfalsified (live tie).

## Scope

Kills nothing, promotes nothing, downgrades nothing. Adopted premises untouched: A8 (80 verb-frame), R19-120 (80 fence, no second class), R24 (24 finite/modal here), val-97-verb-test NULL (INF/NOM tie), noun-97-568 KILL (13-wall). No standing/red-team verdict contradicted or downgraded; §7 intact (67 sole polyvalence + R24's declared exception). Canonical-stream caveat stands (row a3_02 offsets unvalidated).

## Verdict: NULL

Neither reading parses with zero ungranted assumptions. The INF/NOM tie at @567 survives this discriminator.

## Follow-ups proposed (for supervisor queuing; both verified ABSENT from battery-queue.json)

1. `modal-80-license` (P3) — census all 17 80-windows for any modal-shaped government leg (80 governing an infinitive). Bar: kill the modal-80 arm entirely iff no battery-grade leg exists; else name the leg. This would KILL the INF reading at @567 instead of leaving it strained.
2. `inf97-526-vs-567` (P3) — joint test of the two NOM-favoring windows @526 ("[81] [97] ce(47) [44] est(59)") and @567 ("[80] [97] 13 [76]"): test whether a single noun-97 licenses both windows with zero ungranted assumptions besides noun-97 itself. Bar: promote noun-97 class iff both windows parse under one noun value; else fence. (Does not duplicate the already-queued `nom-97-526-adverb`, which tests 81's class, not 97's.)

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-inf-97-567-adjudicate.md` (this file).
- Queue write: `inf-97-567-adjudicate` → status `verdict`, result `null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated post-write; own entry only; no downgrade).
- Lock `locks/inf-97-567-adjudicate.lock` created on start, deleted on completion (verified gone).
