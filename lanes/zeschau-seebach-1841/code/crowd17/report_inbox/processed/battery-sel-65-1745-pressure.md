# Battery verdict: sel-65-1745-pressure

- Target: `sel-65-1745-pressure`
- Claim: "name 65's value at the @1745 postverbal-subject slot; a named 65 discriminates (animate subject vs rigging-like object)"
- Date: 2026-10-09
- Worker: e8e9d853-b614-412f-84c7-bddfc0cd1b7a
- Stream: repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py` with a5_03=0 repair). `canonical.py` never used. All counts re-derived in-work. @-offsets are 0-indexed pair positions.

## Bar (verbatim from battery-queue.json)

"name 65's value at @1745 iff one value holds with stated frame evidence; state the discrimination consequence"

Restated as numbered pass/fail clauses (pre-registered before testing):

- **C1:** One specific lexical value for 65 holds at the @1745-anchored slot (@1748) with stated frame evidence.
- **C2:** The discrimination consequence is stated (what a named 65 would imply for the 56 Xéent tie: animate subject vs rigging-like object).

Listed adverses: none.

## Method

Re-derived the repaired stream in-work (asserted 1,847 pairs, 96 types). Byte-verified the @1745 locus and its ±8 context. Censused all 25 windows of 65. Used standing values as premises: banked GT (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); granted (87=ce, 64=qui, 96=par, 17=fois, 79="tout" A5, 00="pour" A9, 84="on" A15, 47="ce" A4, 06="ent" 3pl ending promoted); provisional (59=est, 77="le"); battery-level 65=["noun","cls"] (prof-65 promote, R20-047 red-team grant). Consulted the prior `noun-65-value` battery (verdict NULL, 2026-10-09) as background, re-verified its key frames independently.

## Window-level evidence

### The @1745 locus (row a8_08)

Byte-verified: `@1742=94 @1743=82 @1744=46 @1745=56 @1746=40 @1747=06 @1748=65 @1749=34`

`[94] [82] que [56] [e] [ent] [65] [i]...`

- 46=que (GT), 56=open verb stem (the Xéent tie), 40=e (GT), 06=ent (promoted 3pl ending), 65=noun-class (granted).
- Parse: "que [56-stem]é-ent [65-N]" — i.e. "que [verb]-3pl [65]".
- 65 is the postverbal NP. There is no other overt subject candidate in the clause; French bars null subjects. Therefore 65 MUST be the subject (postverbal subject, literary inversion).
- 3pl agreement (06=ent) forces 65 to be plural (or a plural-agreeing collective).

### The 56 Xéent tie (background, from procreer-56-semantic-reweight)

8 candidates: {procréer, créer, recréer, gréer, dégréer, maugréer, agréer, suppléer}. All are "-éer" verbs. Subject selectional restrictions:
- procréer, créer, recréer, gréer, dégréer, maugréer: require animate subjects.
- agréer, suppléer: marginally allow inanimate subjects ("cela agrée", "cette somme supplée"), but 3pl postverbal-subject use with inanimate is strained.

### The "rigging-like object" alternative — grammatically closed

The claim's hoped-for discrimination was: 65=animate → subject (favors procréer/créer); 65=rigging-like → object (favors gréer/dégréer, "to rig the sails").

This alternative is ungrammatical:
1. As OBJECT: "que [56]éent [65-object]" leaves the 3pl verb with no overt subject. French does not allow null subjects. Ungrammatical.
2. As SUBJECT with inanimate value: "que gréent les voiles" ("that the sails rig") is semantically anomalous — sails do not rig; sailors rig sails. All 8 verb candidates require agentive subjects (agréer/suppléer only marginally excepted).

Therefore, for the clause to be grammatical, 65 MUST be an animate-compatible plural noun. The rigging-object route is dead. But this is a CLASS-level constraint, not a VALUE.

### No lexical value is forced

The constraint set at @1748 — plural (3pl subject), animate-compatible, masculine (1 conditional leg from "tout 65" @1683), bare NP (never articulated in 25 windows) — is satisfied by an open class of French nouns: hommes, peuples, rois, soldats, matelots, enfants, dieux...

No single value is selected by the frame. This independently confirms the prior `noun-65-value` battery's conclusion ("satisfied by an open class of masculine nouns (homme, peuple, roi, temps, bruit, …)").

### Number tension (recorded, not adjudicated)

- @1683 (a8_05): "00 46 79 65" = "pour que tout [65]" — 79="tout" is the granted masculine SINGULAR form → 65 singular here.
- @1208 (a7_00): "65 64 59" = "65 qui est" — 59=est is 3sg → 65 singular here.
- @1748 (a8_08): 65 must be plural (3pl subject of "ent").

65 is number-variable across windows. Number is inflectional, not lexical, so this does not block a value hypothesis, but it means number agreement cannot discriminate 65's value, and any value hypothesis must accommodate both singular and plural realizations.

## Per-clause pass/fail

- **C1:** FAIL — no specific lexical value for 65 holds at @1748 with frame evidence. The frame constrains 65 to (plural, animate-compatible, masculine?, bare NP), satisfied by an open class. No value is forced; none can be killed at kill grade either.
- **C2:** PASS — discrimination consequence stated (below).

## Discrimination consequence (stated per bar)

1. **The hoped-for discrimination collapses.** The "animate subject vs rigging-like object" fork assumed both parses were grammatical. The rigging-object parse is ungrammatical (no overt subject for a transitive reading; inanimate cannot be the 3pl subject of these verbs). Only the animate-subject parse survives.
2. **65's animacy does NOT break the 56 tie.** All 8 verb candidates (procréer, créer, recréer, gréer, dégréer, maugréer, agréer, suppléer) take animate subjects. An animate 65 is compatible with every candidate. The tie must be broken on other grounds (valency, attestation, object frames).
3. **Conditional elimination recorded:** IF 65 is firmly established as animate (currently only class-level, not value-level), THEN the gréer/dégréer-via-rigging-object route is dead at @1745. This does not eliminate gréer/dégréer with animate subjects ("que gréent les matelots" is grammatical).
4. **What would actually discriminate:** a NAMED 65 (e.g. "matelots" → nautical → gréer/dégréer; "enfants" → procréer; "dieux" → créer). No such naming is available.

## Verdict: NULL

65's value cannot be named at the @1745-anchored slot. The frame yields class-level constraints (plural animate-compatible noun) and kills the rigging-object alternative, but no lexical value is forced. No standing red-team verdict contradicted; §7 intact.

## Follow-ups (null per §4 — for supervisor queueing)

### F1 id `anim-65-select` — priority 3
- claim: "65's animacy established via selectional restrictions: test whether any 65 window forces inanimate or animate."
- bars: "name 65 animate iff ≥2 windows require an animate subject/object under standing values with zero kill-grade contradictions; name inanimate iff ≥2 windows force it; else fence animacy as undetermined."
- evidence: "This report: @1748 requires animate-compatible (3pl subject of -éer verbs); @1208 '65 qui est 32' (32's value constrains); @1683 'tout 65' (generic). noun-65-value §Gender-test."
- adverses: "65's value open; animacy is class-level, do not name a lexical value. 32's value open (adj-32 NULL)."

### F2 id `num-65-agreement` — priority 3
- claim: "Census number agreement across all 25 windows of 65 (singular vs plural verb/adjective/determiner agreement)."
- bars: "produce the full 25-window number-agreement table; fence 65 as number-variable iff both singular and plural agreement are attested at battery grade, else name the fixed number."
- evidence: "This report: singular at @1208 ('qui est') and @1683 ('tout'); plural required at @1748 (3pl 'ent')."
- adverses: "Number is inflectional; a variable result does not block value hypotheses. 59=est provisional; 79='tout' granted masc.sg."

### F3 id `subj-65-1748-corpus` — priority 4
- claim: "Corpus test: is a bare plural animate noun grammatical as postverbal 3pl subject in 1841 French ('que procréent hommes')?"
- bars: "rate of bare-NP postverbal 3pl subjects in the 1841 corpus; if ~0, the @1748 parse itself is challenged and 65's bare distribution becomes the problem, not its value."
- evidence: "@1744–1748 '46 56 40 06 65' (row a8_08); 65 bare in all 25 windows (noun-65-value)."
- adverses: "Literary inversion licenses bare subjects more freely than prose; register-match the corpus query. Does not name 65's value."

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-sel-65-1745-pressure.md` (this file).
- Queue: `sel-65-1745-pressure` → `status: verdict`, `result: null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; disk re-validated; own entry only; no downgrade).
- Lock created on start (2026-10-09T18:01:54Z, no stale lock), deleted on completion.
- R5005, sealed gate instances, and the red-team adjudication queue untouched. No standing/red-team verdict contradicted; §7 intact.

## Provenance

R5005 not touched. Every @-offset verified on the repaired 1,847-pair / 96-type stream in-work via `repair_parse.py` (a5_03=0 repair). `canonical.py` never used. No invented data.
