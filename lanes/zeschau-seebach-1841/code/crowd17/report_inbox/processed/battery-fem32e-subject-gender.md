# Battery verdict: fem32e-subject-gender

## Bar (verbatim, pre-registered)

"a forced masculine subject conditions the claim; feminine/unmarked subjects keep it"

Restated as numbered clauses (frozen before testing):
1. State each subject's gender (61 @447, 65 @1208, 74 @1175) under standing values.
2. Test whether predicative agreement with 32e ('est 32e') is gender-licensed at each copula frame.
3. Resolve (keep the fem-32e claim) iff all three subjects' genders are consistent with the feminine reading of 32e; else fence.

Adverses: None.

## Method

Read BATTERY-PROTOCOL.md first. Created `locks/fem32e-subject-gender.lock` on start. Re-derived the full stream from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (parsed per `repair_parse.py`): 1,847 pairs, 96 types verified. `canonical.py` never touched. R5005, sealed gates, red-team adjudication queue untouched.

Standing values used: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que (GT pencil); 87=ce, 64=qui, 96=par, 17=fois, 79="tout" (A5), 00="pour" (A9), 84="on" (A15), 47="ce" (A4); 59=est, 77="le" (provisional); 32 predicative frame (A1, value open); 48="e" letter tier (R17); 62="il" (demonstrated); 98="vient" (battery-promoted); 65=noun (R18-ratified). 1841 diplomatic French throughout.

Full gender-evidence census of 61 (n=18) and 74 (n=34) windows re-derived byte-exact from the stream.

## Window-level evidence

**Subject 1: 61 @447** — frame `62 61 [59=est] 32 48` (row a2_09): "[61] est 32e".
- Gender evidence across all 18 of 61's windows: zero gendered determiners, zero agreeing adjectives or past participles, zero gender-marked frames anywhere (windows include "87 61" (ceci-fusion locus class, genderless), "77 83 92 61", "85 48 53 61", "65 46 01 61", "65 71 17 61").
- @446=62 (62="il" demonstrated) precedes 61 but does not agree with it — no gender inference on 61 itself.
- **Gender: UNMARKED** (value open globally).

**Subject 2: 65 @1208** — frame `65 [64=qui] [59=est] 32 48 [96=par]`: "65 qui est 32e par…" (row a7_00).
- 65=noun is R18-ratified. Gender: `det-65-gender-adjudicate` (NULL) left the tension open — the "tout 65" masculine leg (@1683) is currently the stronger leg, but it is battery-level, not forced: it rests on reseg-13-armA (battery PROMOTE) and 93's open class, and crucially on the `redteam-79-split-docket` ('tout'/'toute' allomorphy), which is a red-team act.
- The only feminine implication for 65 comes from adj-32's -e at this very window — circular with the claim under test. It cannot serve as independent evidence.
- **Gender: UNMARKED at battery grade** (masculine lean is a battery lead, not forced; the feminine implication is claim-circular).

**Subject 3: 74 @1175** — frame `74 [32] [48='e'] [59=est]`: "…74 32e est…" (row a6_10; 74 precedes the nominalized "32e").
- Gender evidence across all 34 of 74's windows: zero gendered determiners, zero agreeing adjectives; 74's class is fenced class-open (`noun-74-census` NULL — the '74 74' doubling family caps every whole-word class).
- Whether 74 determines "32e" or belongs to the prior clause, no gender mark attaches.
- **Gender: UNMARKED** (class-open).

## Per-clause pass/fail

1. **C1 PASS.** 61: unmarked. 65: unmarked (masculine lean battery-level, unfixed, claim-circular feminine implication). 74: unmarked (class-open).
2. **C2 PASS.** No subject forces masculine. The feminine-predicative reading of 32e ("est 32e", "32e est") is gender-licensed at all three frames: 61's frame ("[61] est 32e") and 74's frame ("32e est") have no gender demand beyond the claim; 65's frame ("65 qui est 32e par") licenses feminine agreement unless 65 is forced masculine — it is not (bar's own wording: a *forced* masculine subject conditions; nothing is forced).
3. **C3 PASS.** All three subjects are consistent with the feminine reading of 32e — the only reading under standing values (48='e' is an R17 letter-tier grant; predicative frames A1 are clean at all three; no battery named a rival masculine reading of "32e").

## Adverses

None listed.

## Verdict: PROMOTE (finding grade — gender-census finding)

No forced masculine subject exists at the three copula frames; feminine and unmarked subjects keep the fem-32e claim per the bar. The fem-32e claim is not gender-conditioned at battery grade.

**Stated tension (fenced, not hidden):** 65's battery-level masculine lean ("tout 65") is the one threat to feminine agreement at @1211, but it is itself contingent on the open `redteam-79-split-docket` and unfixed 93's class; it does not meet the bar's "forced" standard. Resolution of 65's gender and the 32-duality is red-team venue (`fem32e-1211-redteam-input` already packaged the @1211 evidence). If the red team forces 65 masculine, this verdict re-opens.

**Scope note:** this verdict keeps the fem-32e claim against gender objections only. It does not re-litigate fem-32e's own NULL (the @855 residual) — morphology "32e" intact, syntax unachievable there, per the parent battery.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/fem32e-subject-gender.lock` created on start, deleted on completion.
- `battery-queue.json`: `fem32e-subject-gender` queued → verdict/promote (temp-file + rename; pre-write assert confirmed no prior verdict; only this entry touched; JSON re-validated).
- R5005, sealed gates, red-team adjudication queue untouched. `canonical.py` never used. No standing or red-team verdict contradicted or downgraded. §7 intact.
- No follow-ups required (promote, not null).
