# Battery report: subj-56-1626

- Target id: `subj-56-1626`
- Claim: "locate finite-56's subject at @1626 (H1 vs H6 vs leftward); the subject search is now forced by form-56-1627 promote"
- Date: 2026-10-09
- Worker: battery worker (subagent 477c8fc9-997e-47a7-a73a-6ede7300e57d)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs, 96 types, re-derived in-session). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- Offset note: the brief uses 1-based @1627. This report uses 0-based @1626 (same locus). All offsets below are 0-based.

Terms (ASD-STE100): "subject" = the noun phrase that does the verb's action. "inversion" = the subject stands after the verb ("que lut Marie"). "relative pronoun" = "que/qui" linking a clause to a head noun. "complementizer" = "que" introducing a subordinate clause after a verb ("veut que"). "battery grade" = this pipeline's evidence standard. "granted" = red-team ratified. "lead" = battery-supported, not ratified.

## Bar (verbatim, pre-registered before testing)

"name the subject with zero ungranted assumptions; fence if undecidable"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** The subject is named as a specific cell/constituent, with every premise standing at battery grade or higher (zero ungranted assumptions: no invented value, class, or structure).
2. **C2:** Every rival subject placement (leftward of 56; 26 as subject; 69 as non-subject) is excluded at battery grade or better.
3. **C3 (fence arm):** If C1 or C2 fails, fence with stated cause instead of naming.

Adverses listed: none.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/subj-56-1626.lock` on start (agent id + UTC timestamp); deleted on completion. No stale lock was present.
2. Re-derived the repaired stream in-session. Byte-exact checks: "46 56" exactly 2x (@1625, @1744); "69 26" exactly 3x (@405, @933, @1627); "56 69" exactly 2x (@932, @1626); n(56)=23; n(69)=12.
3. Standing premises used, not re-litigated: 46=que (pencil GT); 64=qui (promoted); 69=[noun,cls] (R19-109 red-team GRANT; 'ce' value-lead R19-110, value open); 26=["noun","lead"]; 00="pour" (promoted); 33=["INF","cls"]; 56 finite 3sg at @1626 (form-56-1627 PROMOTE — the claim itself sanctions this premise); "69 26 00 33" = "ce [26-noun] pour [33-INF]" (kernel-6926-frame PROMOTE); 67 et/veut positional rule (sole §7 polyvalence); French is not pro-drop; "qui" (not "que") is the subject relative pronoun.
4. French grammar is used as the test apparatus (inversion licensing, relative-pronoun distribution, complementizer distribution), not as a lane assumption.

## Window-level evidence

The locus (0-based, row a8_03, byte-confirmed):

`[1623]67 [1624]33 [1625]46(que) [1626]56 [1627]69 [1628]26 [1629]00(pour) [1630]33`

The clause under test: "que [56-finite-3sg] [69] [26] pour [33]". The twin formula window W1 (@932, row a5_10: `98 83 56 69 26 00 33`) lacks "que" — its subject assignment is a separate question and is NOT decided here (scope note).

### The subject is the 69-headed nominal phrase

- 56 is finite 3sg (form-56-1627 PROMOTE). A finite verb needs an overt subject (French is not pro-drop).
- "que" after 33 (noun- or INF-class) cannot be a complementizer: complementizer "que" follows verbs/adjectives, never a bare noun or infinitive. It is therefore the relative pronoun (object form; the subject form is "qui"=64, promoted). Whether 67 reads "et" (relative head = 33) or "veut" (complementizer "que" after "vouloir"), the subject of 56 sits inside the clause, post-verbally. Both 67 arms agree; 67's value is not decided and need not be.
- Post-verbal nominal placement: in "que V NP", the NP is the subject by inversion ("que lut Marie"-shaped; licensed in subordinates). 69's nominal class is red-team granted (R19-109). The subject constituent is therefore the nominal phrase headed by 69.
- 26's role inside that phrase is fixed by the standing kernel battery (PROMOTE): "69 26" = "ce [26-noun]" determiner phrase. So the subject is the "69 26" NP ("ce [26-noun]"). This naming uses 69's granted class and the kernel's battery-grade resolution; 69's 'ce' VALUE stays lead-grade (R19-110) and is not named — the subject-hood finding does not depend on it.

### Rival exclusions (C2)

- **Leftward subject (33 or earlier): DEAD at kill grade.** "que" after 33 is relative-pronoun-only (complementizer ungrammatical after noun/infinitive). As relative pronoun it is object-form, so the subject must be inside the clause. 33 is the relative head (67="et" arm) or the matrix infinitive (67="veut" arm) — never 56's subject. The kill holds under both 67 readings and every open class of 33.
- **26 as subject, 69 as object: DEAD at kill grade.** Simple inversion puts the subject immediately post-verbally (69's slot). A post-verbal "69" cannot be a clitic object (French object clitics are preverbal); as a full-NP object before the subject ("*que V objet sujet") the order is ungrammatical. 69-as-adverb is closed by the R19-109 noun-class grant.
- **69 as object with null subject: DEAD at kill grade.** French is not pro-drop; "que" is not the subject relative form (that is "qui"=64).
- **69 detached/topic with 26 as subject: DEAD at battery grade.** Dislocation needs a prosodic break; no licensed structure supports it; the licensed parse ("que V NP" inversion) already fills the subject slot.
- **Exclamative "que" rival ("que crée ce-[26]!"): non-discriminating.** Even under the exclamative reading, the subject is still the 69-phrase. It changes the clause type, not the subject assignment.

### H1 / H6 / leftward mapping

- H1 (69 inverted subject, 26 adverb): subject locus CORRECT (69); its 26-adverb arm is dead per the standing kernel resolution (26 noun-lead; "ce [26]" determiner phrase).
- H6 (69 subject, 26 object NP): subject locus CORRECT (69); its 26-object arm is dead per the standing kernel resolution (26 is the head noun of the subject NP, not the object).
- Leftward: dead (above).

## Per-clause pass/fail

- **C1 — PASS.** The subject is named: the post-verbal nominal phrase headed by 69 (the "69 26" constituent; standing kernel gloss "ce [26-noun]"). Premises: form-56-1627 PROMOTE, R19-109 GRANT, kernel-6926-frame PROMOTE, 46=que GT, 64=qui promoted, 26 noun-lead, French grammar as apparatus. Zero invented values, classes, or structures. 69's 'ce' value is not named (stays lead-grade); the naming does not depend on it.
- **C2 — PASS.** All four rival placements excluded at battery grade or better (leftward and 26-as-subject and null-subject at kill grade; dislocation at battery grade).
- **C3 (fence arm): does not fire.** The subject is decidable.

No standing or red-team verdict is contradicted or downgraded: consistent with R19-109 (69 noun class), R19-110 ('ce' value-lead untouched), the 26 noun-lead, form-56-1627, kernel-6926-frame, and §7 (no polyvalence declared; no new class or value named). No adverse was listed; the 'ce'-lead dependency is fenced out of the naming by construction.

## Verdict: PROMOTE

The subject of finite-56 at @1626 is the 69-headed nominal phrase (the "69 26" constituent; standing kernel reading "ce [26-noun]"). H1 and H6 both locate the subject correctly at 69; they are superseded only on 26's role, which the standing kernel battery fixes as head noun of the subject NP. The leftward hypothesis is dead at kill grade.

## Scope and caveats (stated, not hidden)

- Names the subject constituent only. 69's VALUE stays open (lead-grade 'ce'); 26's value stays open; 33's class/value stay open; 67's et/veut reading stays open (non-discriminating).
- W1 @932 ("98 83 56 69 26 00 33", no "que") is out of scope: its subject assignment is a separate battery question.
- Canonical-stream caveat stands: row a8_03's upstream offset is unvalidated.
- Downstream: 56's valency under the fixed "ce [26]" subject belongs to the parse-1626-clause venue (kernel battery's note); not duplicated here.

Per §4, promotes require no follow-ups.

## Bookkeeping

- Queue: `subj-56-1626` → status `verdict`, result `promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated post-write; own entry only; no downgrade).
- Lock `locks/subj-56-1626.lock` created on start, deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
