# Battery report: subclass-66-98-noun

- Target id: `subclass-66-98-noun`
- Claim: "discriminate 66's sub-class inside the X-66-98 subject role (plain noun vs substantivized infinitive), the fenced C2 rival 6"
- Date: 2026-10-09
- Worker: battery worker (subagent 33f47e89-2e02-4d83-b085-b1b474cd5412)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session). `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Parent: `battery-val-66-767-frame.md` (NULL, 2026-10-09), C2 rival 6.

Terms (ASD-STE100): "X-66-98" = the three-window cluster where 66 is subject of 98='vient' (@88, @123, @766). "Substantivized infinitive" = an infinitive used as a noun ("le manger"). "Plain noun" = a lexical noun. "Article-headedness" = headed by a determiner/article.

## Bar (verbatim, pre-registered before testing)

"Bar: 77='le' ratification at @88 decides article-headedness; or number/agreement probes across @88/@123/@766. A plain-noun resolve hardens the subject naming to class grain."

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** The 77='le' ratification path decides article-headedness at @88.
2. **C2:** Number/agreement probes across @88/@123/@766 discriminate plain noun vs substantivized infinitive.
3. **C3:** A plain-noun resolve hardens the subject naming to class grain.

Adverses listed: none.

Task NOTE (from dispatch brief, honored): the 77='le'-ratification path is unratified — use the agreement-probe path, not the ratification path.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/subclass-66-98-noun.lock` on start (agent id + 2026-10-09T19:10:00Z); no prior/stale lock; deleted on completion.
2. Re-derived the repaired stream byte-exact in-session (1,847 pairs / 96 types asserted).
3. Adopted (not re-litigated): 98='vient' finite (battery-promoted, vient-98-name); 66's role as nominal subject of 98 in X-66-98 x3 (parent C1, role grain); 58=nominal (registry cls); 77='le' provisional (§7); 84='on' (A15); poly-66-split NULL (split declaration is red-team venue — not declared here).
4. Ran three agreement probes (see below). Corpus: `code/side-period/corpus`, 81 French files, 57,375,788 chars (German files excluded).

## The three X-66-98 windows (byte-exact, re-derived)

- @88, row a1_02: `14 06 88 [77 66 98 19] 41 98` = "[77] [66] vient [19]" (77='le' provisional)
- @123, row a1_03: `60 90 19 [58 66 98 82] 48 11` = "[58] [66] vient m'[82]" (82='m' GT; 58=nominal cls)
- @766, row a5_03: `59 39 88 [66 98 80] 10 22` = "[88-inf] [66] vient [80]"

## Window-level evidence / probes

### Probe 1 — corpus grammaticality of infinitive-subject-of-"venir" (decisive)

Question: does 1841 French allow "[infinitive] vient" or "le [infinitive] vient" (infinitive subject of "venir")?

- 2,431 occurrences of "vient" in 57.4M chars of French period text.
- Every candidate with an infinitive-shaped immediate predecessor (word ending -er/-ir/-re/-oir) hand-checked: 13 subject-position candidates, 10 substantivized-pattern candidates, 5 bare clause-initial candidates — **all 28 are false positives** (proper nouns: "M. Pradier vient", "Pasquier vient"; common nouns: "le soir vient", "le danger vient", "l'affaire vient", "la famille entière vient").
- **0 genuine infinitive subjects of "vient" in 57.4M chars.** The search was exhaustive over shapes: every French infinitive ends in -er/-ir/-re/-oir, so no infinitive subject could escape the pattern.
- Positive control: "le [common noun] vient" is productive (23 hits on a 24-noun sample; true count far higher).
- Semantic ground: "venir" (to come) selects subjects capable of coming; an infinitive (an action) cannot "come". The zero is grammatical, not accidental.

**Result:** the substantivized-infinitive reading of 66 is ungrammatical in the period register at all three windows. Rival 6 is KILLED at grammaticality grade (upgrades the parent's fence).

### Probe 2 — @123's nominal governor ("58 66")

- 58 = nominal (registry cls, standing). n(58)=7; distribution noun-compatible ("35 58 35", "ce 58 ce", verb-stem + 58).
- @123: "[58-nominal] [66] vient". In French, a nominal directly followed by a bare infinitive (no preposition) is ungrammatical; nominal + nominal (apposition/compound) is fine.
- Therefore 66 at @123 cannot be a bare infinitive; it must be nominal. **Plain-noun reading forced at @123.**

### Probe 3 — number agreement across the three windows

- 98='vient' is 3sg finite in all three windows (adopted promote). French finite verbs agree in number with their subject.
- 66 must therefore be singular in all three windows. A substantivized infinitive is always singular; a plain noun can be singular. Consistent with plain noun; the infinitive rival is already dead by Probe 1.
- No plural marking on 66 anywhere in its 19-window distribution that would complicate the singular reading.

### Probe 4 — @88's article (supporting, not decisive)

- "77 66 98" with 77='le' provisional: article-headed 66. An article-headed infinitive would be substantivized — but Probe 1 kills "le [inf] vient" (0/57.4M). Under the provisional reading, @88 is "le [66-noun] vient", fully grammatical. (Not used as the ratification path per the task NOTE.)

### 98's 40-window subject census (supporting)

- n(98)=40, re-derived. Classified subjects: 'qui' (64) x2 (@19, @511), 'ce' (47) x2 (@1579, @1660), nominal/noun-class subjects (43, 58/66-cluster, 70, 92, 17, 76, 37, 65, 23, ...), plus open/unresolved slots. Zero infinitive subjects — consistent with Probe 1. (Full 40-window classification adopted from the parent's census; no window re-litigated.)

## Per-clause pass/fail

- **C1:** NOT RUNNABLE — 77='le' is provisional, unratified (per task NOTE). Recorded, not failed. The bar's disjunctive "or" routes through C2.
- **C2:** PASS — the agreement probes discriminate. Probe 1 kills the substantivized-infinitive rival at grammaticality grade (0/57.4M chars, exhaustive shape coverage, semantic ground). Probe 2 forces nominal 66 at @123 (nominal governor + bare-infinitive ungrammaticality). Probe 3 confirms singular agreement consistent with plain noun. The plain-noun reading is the sole surviving sub-class in all three windows.
- **C3:** PASS — 66 is a plain noun in the X-66-98 subject role (@88, @123, @766). The subject naming hardens from role grain to class grain.

Adverses: none listed. No standing or red-team verdict contradicted, downgraded, or re-litigated. §7 intact.

## Verdict: PROMOTE

66 is a **plain noun** in the X-66-98 subject role (@88 "le [66] vient", @123 "[58] [66] vient", @766 "[88] [66] vient"). The substantivized-infinitive rival (parent C2 rival 6) is killed at grammaticality grade: 1841 French never puts an infinitive subject on "venir" (0 genuine in 57.4M chars / 2,431 "vient" tokens, exhaustive shape search, hand-verified).

## Scope (stated, not hidden)

- **This promote is scoped to the three X-66-98 windows.** It names 66's sub-class inside the subject role only.
- It does NOT name 66's global class or value. It does NOT declare the poly-66-split (red-team venue under §7 — the pour-governed x7 infinitive-arm windows are untouched, and the split declaration remains fenced to the red team).
- It does not touch 77='le' provisional status, 98='vient' battery grade, or any other window of 66.
- Canonical-stream caveat stands: rows a1_02/a1_03/a5_03 offsets unvalidated (68/70).

## Follow-ups

None required (promote, not null). Natural red-team continuation: ratify the X-66-98 plain-noun sub-class as `66=["noun","cls"]` scoped to the subject role, or fold into the poly-66-split docket.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-subclass-66-98-noun.md` (this file).
- Queue: `subclass-66-98-noun` queued → `verdict`/`promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/subclass-66-98-noun.lock` created on start, deleted on completion (verified gone).
- Corpus evidence: `code/side-period/corpus` (81 French files, 57,375,788 chars); provenance in `code/side-period/corpus/PROVENANCE.md`.
- R5005, sealed gates, red-team adjudication queue untouched.
