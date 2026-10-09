# Battery report: infsub-80-frame

- Target id: `infsub-80-frame`
- Claim: test the infinitive-subject reading ("to-[X] [80-s]") against the A8 verb-frame grant at all four "[X]er [80]" windows.
- Date: 2026-10-09
- Worker: battery worker (subagent 5661d8d9-9f13-4ca8-920d-ab429fac85ee)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; 1,847 pairs / 96 types re-derived in-session, asserts held). `canonical.py` never used. R5005, sealed gate instances, and the red-team adjudication queue untouched.

## Bar (verbatim, pre-registered before testing)

"all four windows parsed under one 80-frame statement, or the readings split with stated cause per window"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** All four "[X]er [80]" windows are enumerated byte-exact on the repaired stream (29='er' is banked ground truth, so the census is the complete "29 80" bigram set).
2. **C2:** The infinitive-subject reading R-SUBJ ("[X]er" is the subject of finite verb 80, "to-[X] [80-s]") is tested at each window under standing values.
3. **C3:** Either all four windows parse under one 80-frame statement, or the readings split with stated cause per window.

Verdict rule: **kill** iff R-SUBJ fails at kill grade (a window forces the reading false on standing values); **promote** iff R-SUBJ parses at all four under one consistent statement; **null** otherwise with 1-3 follow-ups.

## The two readings

- **R-A8 (A8 verb-frame grant, standing):** 80 is a verb-frame, value open. Per imp-80-set (battery, 2026-10-09): '80-77' = "[80]-le" x2 (@720/@1032) is the battery-grade imperative+enclitic diagnostic; @1156/@1322/@1596 are bare-verb candidates (imperative-consistent only with ungranted boundary assumptions).
- **R-SUBJ (tested):** "[X]er" is the subject of the finite verb 80 — "to-[X] [80-s]", e.g. "Mentir est honteux"-shaped. For R-SUBJ to hold at a window, 80 must be finite and "[X]er" its subject, with the rest of the window grammatical.

## Window-level evidence (all byte-exact, 0-based @)

### W1 @1031-1032 (row a6_03)

`1028=87(ce) 1029=01 1030=03 1031=29(er) 1032=80 1033=77(le?) 1034=11(la) 1035=70(pre) 1036=82(m) 1037=34(i) 1038=29(er) 1039=40(e) 1040=17(fois)`

"[03]er [80]-le, la première fois". **R-SUBJ: KILL at kill grade.** The '80-77' enclitic is the battery-grade imperative diagnostic (imp-80-set: exactly n=2, @720/@1032; 77='le' provisional). An imperative verb cannot take an infinitive subject (imperative subjects are the elided addressee). The only rescue — 80 as finite indicative — is killed by the postposed "le": French object pronouns are proclitic before finite verbs ("il le fait"); postposed "le" after a finite indicative is ungrammatical in 1841 French. No re-segmentation under standing values avoids this. Consistent with (does not duplicate) residual-1029-infinitive's PROMOTE of the exclamatory-infinitive + imperative reading at this locus.

### W2 @1155-1156 (row a6_09)

`1151=84(on) 1152=02 1153=00(pour) 1154=92 1155=29(er) 1156=80 1157=17(fois) 1158=77(le?) 1159=82(m)`

"on [02] pour [92]er [80] fois…". **R-SUBJ: KILL at kill grade.** 00='pour' is an A9 grant governing the infinitive ("pour [92]er"). A prepositional/governed infinitive cannot be a subject in French — hard grammatical fact, all periods. Rescue attempt (pour attaches leftward as purpose adjunct: "on [02] pour [92]er") fails twice over: (a) it removes "[92]er" from subject position, stranding 80 subjectless (pro-drop ungrammatical in 1841 French); (b) even granted, "[80] fois" is ungrammatical — bare "fois" (17='fois' promoted) cannot follow a finite verb without a determiner. No charitable parse survives.

### W3 @1321-1322 (row a7_04)

`1319=24 1320=03 1321=29(er) 1322=80 1323=08 1324=62 1325=98(vient)`

"[24] [03]er [80] [08]…". **R-SUBJ: KILL at kill grade.** 24 is finite verb at class level (R17-009 stands; the 24="faire" VALUE is only a conditional lead post-R18-008, but government does not depend on the value). A finite verb directly followed by an infinitive governs it as complement ("[24] [03]er" = V-fin + V-inf complement, whatever 24's value). A governed complement infinitive is structurally inside 24's VP and cannot be re-read as the subject of a following finite verb 80. The VP-subject rescue ("[24] [03]er" as subject of 80) is ungrammatical — finite VPs are not subjects in French. No clause boundary can be licensed between "[03]er" and "[80]" without breaking 24's government.

### W4 @1595-1596 (row a8_02)

`1591=47(ce) 1592=08 1593=81 1594=03 1595=29(er) 1596=80 1597=67 1598=77(le?) 1599=81 1600=82(m) 1601=98(vient)`

"ce [08] [81] [03]er [80] et le [81] m'vient…". **R-SUBJ: FENCE (not kill-grade, unlicensable at battery grade).** The bytes do not force it false (08, 81 open), but every R-SUBJ parse needs what a battery cannot license: (a) "[81] [03]er" as subject phrase needs 81=adverb ("bien manger"-shaped adverb+infinitive subject — 81's class open, unforced); (b) "et le [81]" as a coordinated NP/clause ("and the [81] …vient") needs 81=nominal — a direct §7 conflict with (a) (67 et/veut is the sole true polyvalence; a battery cannot split 81); (c) 80 as a finite verb taking a bare infinitive subject with no complement — unforced, value open. Cause stated: the reading is available only at the cost of a red-team 81 adjudication plus unforced 80 assumptions.

## Per-clause results

1. **C1: PASS** — the four "29 80" windows are the complete census (W1 @1031, W2 @1155, W3 @1321, W4 @1595), each byte-verified above.
2. **C2: FAIL at kill grade** — R-SUBJ is forced false at W1 (enclitic/imperative incompatibility), W2 ("pour"-government + bare "fois"), and W3 (V-fin + infinitive government); fenced at W4 (§7-barred 81 split required).
3. **C3: EXECUTED** — the readings split with stated cause per window: R-SUBJ is dead at three windows and unlicensable at the fourth; no uniform infinitive-subject statement covers the "[X]er [80]" set.

## Adverses

None listed. No standing or red-team verdict contradicted or downgraded: imp-80-set's imperative diagnostic and residual-1029-infinitive's PROMOTE are both confirmed consistent with these findings; §7 intact (no polyvalence declared — the W4 fence explicitly refuses the 81 split at battery level). Canonical-stream caveat stands (rows a6_03/a6_09/a7_04/a8_02 offsets unvalidated).

## Verdict: KILL

The infinitive-subject reading ("to-[X] [80-s]") is rejected as an account of the four "[X]er [80]" windows: three windows force it false at kill grade on standing values, and the fourth is fenced as unlicensable without red-team acts. The A8 verb-frame grant stands uncontradicted — at W1 the imperative+enclitic reading is battery-grade, and W2-W4's A8 verb-frame readings remain the live ones. Per §4, a kill does not regenerate follow-ups.

Supervisor observation (not a follow-up): W4's R-SUBJ fence is 81-gated; any future 81-class adjudication re-tests it. W2's "pour [92]er" government and W3's "[24] [03]er" government are now documented hard barriers for any future subject-infinitive proposal at those loci.
