# Battery `syll-38-value-census` — verdict: NULL (fence arm satisfied; value tie unbreakable at battery grade)

- Target id: `syll-38-value-census` (priority 3)
- Claim: "name 38's syllable value from a census of its 7 windows"
- Date: 2026-10-09
- Worker: subagent 78ec5c34-4cb7-4578-9c0a-7efb8094055e
- Verdict: **NULL** — the bar's fence arm is satisfied: 38 is fenced as unnameable at battery grade. The value is narrowed to {"vouloir" (veut/voulu), "devoir" (doit/dû)} and the dedicated tie-breaker (`val-38-vouloir-devoir`) just NULL'd with the tie unbroken. No new leg emerged from this census.
- Lock: created `code/crowd17/next-token/locks/syll-38-value-census.lock` 2026-10-09T18:22:39Z, deleted on completion. No stale lock encountered.

## Bar (verbatim, pre-registered)

"name with >=2 independent legs, or fence as unnameable at battery grade"

## Bar restated as numbered pass/fail clauses

1. C1: 38's value is named from the 7-window census with >=2 independent legs (independent = distinct windows / distinct neighbor evidence, using only granted or battery-grade standing values).
2. C2: Failing C1, 38 is fenced as unnameable at battery grade with stated cause.

## Framing correction (recorded before testing)

The target's "syllable value" framing is superseded. `noun26-38-profile` (PROMOTE, filed 2026-10-09 07:11 UTC — ten hours BEFORE this target was proposed at ~17:31 UTC by `syll-83-de-1829`) established 38 = verb-form, uniform class (past participle @826, finite @1113 kill-grade, modal @1469, finite governor @1650; W4/W7 fenced; W1 indeterminate). 38 is not a syllable-tier cell; its forms are inflected verb forms ("veut/voulu" or "doit/dû" per `val-38-verb`). The census below therefore tests the VALUE-naming question under the promoted verb class, which is the live form of this target's claim. The target's evidence note ("38's value decides the '[38]de' noun-host candidate") likewise predates the promote — see the supervisor observation in Findings.

## Method

Re-derived the repaired stream per `code/side-keyhunt/repair_parse.py`
(`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`):
1,847 pairs confirmed, 96 types confirmed. n(38)=7 at 0-based
@384/@826/@1113/@1343/@1469/@1650/@1828 — byte-matching the brief's window
list. `canonical.py` never used. R5005, sealed gates, red-team adjudication
queue untouched. No invented data; every number traces to the stream.

Adopted as premises (stated, not re-litigated): standing values per
BATTERY-PROTOCOL.md §7; 30='pas' battery-promoted; 59='est' provisional;
65 noun-class (R18-001 ratified); "69 11"='cela' locus-level; 24 finite-verb
class-level; 86 INF-class. Prior battery results adopted as premises, each
independently spot-checked at the byte level below: `noun26-38-profile`
(PROMOTE, verb-form uniform), `val-38-verb` (NULL, {vouloir,devoir} tie),
`val-38-vouloir-devoir` (NULL, tie unbroken), `adj-38-w4-parse` (KILL, W4
fenced), `val-52-38-unit` (KILL, '52 38' unit rejected), `syll-83-de-1829`
(NULL, verb fork at @1829 fenced at kill grade, noun fork live).

## Window-level evidence (all 7 windows, byte-traced)

- **W1 @384** `82 48 00 11 50 82 16 52 38 37 43 91 36 62 91 84 73` — core `16 52 [38] 37 43`. 52 split-shaped (class open), 37 predicative-frame (value open), 16 open. No verb-form parse forced, no value forced. **Indeterminate** (agrees with parent). Cannot discriminate vouloir vs devoir: volition/obligation both need 52/37/43 values that are not granted.
- **W2 @826** `47 78 40 95 13 24 87 59 38 82 01 24 87 11 77 76 59` — core `87 59 [38] 82` = "ce(87) est(59) [38] m(82)". "c'est [pp]"-shaped: past participle ("c'est dit"/"c'est voulu"/"c'est dû") — both tie candidates license it. Conditional on provisional 59='est' (stated). **Verb-form leg (past participle).**
- **W3 @1113** `78 65 63 00 66 73 41 65 38 30 69 11 88 70 12 06 14` — core `65 [38] 30 69 11` = "[65-noun] [38] pas(30) cela(69-11)". "pas" is a verbal negator: forces finite-verb-38 at kill grade ("[65] [38-V] pas cela"); verbless readings dead. Both "ne veut pas cela" and "ne doit pas cela" license it. **Verb-form leg (finite 3sg, kill-grade).**
- **W4 @1343** `86 71 64 60 08 65 64 52 38 47 86 66 73 34 62 48 77` — core `64 52 [38] 47 86` = "qui(64) [52] [38] ce(47) [86-INF]". Verb-38 strands on "ce [86-INF]" (ungrammatical); participle-38 strands "qui" verbless. **Fenced with stated cause** (agrees with `adj-38-w4-parse` KILL).
- **W5 @1469** `17 01 21 62 48 21 02 62 38 26 12 41 53 60 06 67 33` — core `62 [38] 26` = "[62] [38-modal] [26]". Modal slot ("ne peut [inf]"-shaped): "veut [inf]" and "doit [inf]" both license it. **Verb-form leg (modal).**
- **W6 @1650** `33 98 60 03 64 31 10 03 38 82 16 01 56 37 11 24 48` — core `03 [38] 82 16` = "[03] [38-V-fin] me(82) [16-inf]" ("veut me voir"-shaped, conditional on 03-nominal and 16-infinitive, both battery grade). "veut me [inf]" and "doit me [inf]" both license it. **Verb-form leg (finite governor).**
- **W7 @1828** `09 19 00 97 00 86 29 82 38 83 24 82 16 59 36 69 64` — core `82 [38] 83 24` = "m(82) [38] [83] [24-finite]". Independently verified fenced for the verb class under EVERY live 83-branch (not only the 'de' fork): finite-38 gives "[38-Vfin] [83] [24-Vfin]" — two finite verbs separated only by 83, ungrammatical under every granted 83 value (83's live branches are the 'de'-syllable fork and open; none is a conjunction/complementizer); infinitive-38 gives "[INF-er] me [38-INF] [83] [24]" — stacked infinitives then finite 24, ungrammatical; participle-38 has no auxiliary. **Fenced with stated cause, 83-fork-independent** (strictly stronger than the parent's fence, which was stated for "both classes" without the branch analysis).

## Findings

1. **Census confirms the promoted class, adds no value leg.** Four verb-form legs (W2 pp, W3 finite kill-grade, W5 modal, W6 finite governor), two fences (W4, W7), one indeterminate (W1). Every leg is licensed EQUALLY by "vouloir" and "devoir" — the tie is symmetric across all four legs, not an artifact of one window.
2. **The tie is now doubly NULL'd.** `val-38-verb` (NULL): {vouloir, devoir} tie unbreakable on the bar frames. `val-38-vouloir-devoir` (NULL, verdict recorded 2026-10-09): dedicated discriminator search ("38 46"-family, 65-value, corpus arms) found no discriminator window. This census finds no fifth leg and no asymmetry the tie-breaker missed.
3. **C1 FAILS; C2 PASSES.** No value can be named with >=2 independent legs: the only two surviving candidates tie on every leg, and the tie-breaker battery exhausted the discriminator space at battery grade. 38 is fenced as unnameable at battery grade — cause: symmetric {vouloir, devoir} tie across all four verb legs, tie-breaker NULL'd, no further discriminating window in the 7-window census.
4. **Supervisor observation (not a finding against any battery):** queued `noun-38de-1829-host` ("[38]de" as a NOUN subject of finite 24) was proposed by `syll-83-de-1829` on the premise "38 is open" — but the verb-form PROMOTE predates it by ~10 hours. Under the uniform verb-form promote, a noun reading of 38 at @1828 would require a §7 split adjudication (verb-form in W2/W3/W5/W6, noun at W7). The queued target should not run its noun-naming bar on the stale premise; recommend the supervisor reconcile (fence the noun fork under uniform class, or escalate the split) before dispatch. This worker does not modify the queued entry.

## Per-clause results

- C1 (name with >=2 independent legs): FAIL — {vouloir, devoir} tie symmetric on all four legs; tie-breaker NULL'd.
- C2 (fence as unnameable at battery grade): PASS — cause stated in Finding 3.

## Verdict: NULL

Per lane precedent ("name X or fence" bars that fence resolve to NULL), the verdict is NULL, not KILL: 38's class is promoted (verb-form, uniform) and its value narrowed to a 2-way tie — the claim is fenced, not falsified. No standing battery or red-team verdict contradicted or downgraded; §7 intact (one lexeme with inflected forms is inflectional, not polyvalence).

## Adverses

None listed on the target. Coordinated (not duplicated):
- `noun26-38-profile` (PROMOTE): class premise adopted; W7 fence independently strengthened (83-fork-independent branch analysis).
- `val-38-verb` (NULL) and `val-38-vouloir-devoir` (NULL): tie adopted; this census confirms no missed asymmetry.
- `adj-38-w4-parse` (KILL), `val-52-38-unit` (KILL): W4 fence and '52 38' unit rejection adopted, not re-litigated.
- `syll-83-de-1829` (NULL): its follow-up 2 is this target; its "38 is open" premise noted stale (Finding 4). Its W7 verb-fork fence is consistent with this report's stronger W7 fence.

## Follow-up targets (null regenerates work; all verified ABSENT from battery-queue.json)

1. **vouloir-devoir-rearm-65** (P3, GATED on 65's value being named): the tie-breaker's own re-arm mechanism — re-run `val-38-vouloir-devoir`'s bar once 65's value lands; "cela" @1113 resolves to wanted vs owed (owe-sense forces "devoir", volition-sense forces "vouloir"). Do not run before 65 names.
2. **val-38-corpus-modal-owe** (P4): corpus arms for the tie in 1841 diplomatic French — is "devoir" in the owe sense with a "cela"-shaped object attested, and do "vouloir"/"devoir"-modal with "me + inf" show any selectional difference? Recorded as stated-weight lean only, never as a kill-grade discriminator.
3. **noun-38de-premise-reconcile** (P4): reconcile queued `noun-38de-1829-host` with the verb-form PROMOTE — either fence its noun fork under the uniform class or escalate a §7 split adjudication (verb-form W2/W3/W5/W6 vs noun W7); do not dispatch the noun-naming bar on the stale "38 is open" premise.

## Scope

Byte-level census of all 7 of 38's windows on the repaired 1,847-pair stream. Class question settled by prior promote (adopted); this battery settles only the value-naming question, fencing it at battery grade. The vouloir/devoir tie-break remains live via follow-ups 1–2; the noun-fork premise conflict is flagged for the supervisor (follow-up 3).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-syll-38-value-census.md` (this file)
- Queue: `syll-38-value-census` → `status: verdict`, `verdict: {result: null, report: code/crowd17/report_inbox/battery-syll-38-value-census.md, date: 2026-10-09}` (pre-write assert passed — was queued/verdictless; temp-file + rename; disk re-validated; own entry only; no downgrade)
- Lock created on start, deleted on completion. R5005, sealed gates, red-team adjudication queue untouched.
