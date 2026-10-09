# Battery report: procreer-56-semantic

- Target id: `procreer-56-semantic` (priority 3, status queued at dispatch; no lockfile existed)
- Claim: "test procreer ('engendrer') against the three windows' semantic frames (@795, @1626, @1745)"
- Date: 2026-10-09
- Worker: battery worker (subagent e41ca560-b153-43fd-be4f-50a9addbf8ce)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). Verified in-worker: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Parent: follow-up #2 of the NULL `xeent-register-tiebreak` (2026-10-09), which closed the 9-verb -éer inventory (agréer, créer, dégréer, gréer, maugréer, procréer, recréer, réer, suppléer), killed réer at kill grade, and left an 8-way tie. Sibling `valency-maugreer-56` (queued) owns maugréer; no duplication.
- Lock: `code/crowd17/next-token/locks/procreer-56-semantic.lock` created on start (agent id + UTC timestamp), deleted on completion.

## Bar (verbatim, pre-registered)

"resolve iff an 'engender' reading parses at @1626/@1745 with stated semantic frames; else fence"

Numbered clauses (frozen before testing, not modified after):

1. C1 — an 'engender' reading (56 = procréer, Littré v.a. "Engendrer", usable absolutely; 3sg "procrée") parses at @1626 with the stated semantic frame ("33 46 56 69 26 00 33"): a grammatical French clause under standing values, contradicting no banked/granted/promoted value.
2. C2 — an 'engender' reading (56 = Xéent stem + "e-ent" = 3pl "procréent") parses at @1745 with the stated semantic frame ("94 82 46 56 40 06 65", glossed "ne m que [56]e ent [65]"): a grammatical French clause under standing values, contradicting no banked/granted/promoted value.

Resolve (promote) iff C1 and C2 both pass; else fence (null with 1–3 follow-ups, §4).

## Method

1. Read BATTERY-PROTOCOL.md and the target's queue entry fully before touching anything.
2. Byte re-derived the three windows from the repaired stream (0-based indices; brief's @795/@1626/@1745 confirmed byte-exact):
   - @795 (row a5_04): `...46 07 64 |56| 37 44 77` = "qui [56] [37]" (64='qui' banked).
   - @1626 (row a8_03): `...67 33 46 |56| 69 26 00 33...` = "[33] que [56] [69] [26] pour [33]" (46='que' banked, 00='pour' granted).
   - @1745 (rows a8_07/a8_08): `...34 94 82 46 |56| 40 06 65...` = "ne m que [56]e ent [65]" (82='m' banked, 40='e' banked, 06='ent' battery-standing, 65 noun class R18-001).
3. Standing premises adopted, not re-litigated: stem-56-whole PROMOTE (56 whole-word; @1745 the single budgeted orphan with the clean Xéent stem parse per rightedge-56-1745 C2); noun26-69-pour-dire PROMOTE (69 = noun, subject of 26 at the formula windows); 94='ne' STRONG LEAD (battery-standing; 94's value fenced red-team venue — my C2 result is independent of 94's value, stated below).
4. Littré facts for procréer (fetched by the parent battery 2026-10-09, adopted): v.a., "Engendrer", usable "Absolument". 3sg "procrée", 3pl "procréent" per the -éer paradigm (cf. "créent"/"agréent").

## Window-level evidence

### W795 — @795 "qui [56] [37]" (supporting context; not in the bar's iff)

"qui procrée [37]": relative subject "qui" + finite 3sg + 37 predicative/object complement (A1). Grammatical in frame; procréer's transitive arm ("engendrer [37]") fits. No discriminator — name-56-verb W1 showed all candidates fit this frame identically. Adopted as premise; selectional fit waits on 37's value (sel-37-pressure queued).

### W1626 — @1626 "33 46 56 69 26 00 33" (C1)

Wider context: `...11 84 78 66 67 33 46 56 69 26 00 33 21 64 37 01...` = "…on 78 66 et 33 que [56] 69 26 pour 33, qui 37…". Candidate parses for 56 = finite 3sg "procrée", each tested against standing verdicts:

- P-a (que = object relative, antecedent 33; subject 69 postverbal): "33 que procrée 69" = "33 which 69 engenders" — grammatical in isolation, BUT 69 is 26's subject at this formula window per noun26-69-pour-dire PROMOTE ("69 26 pour 33" = "[69] [26s] pour [33]", complete clause). One token cannot be subject of both 56 and 26. Contradicts a promoted battery. REJECTED.
- P-b (que = conjunction "that"; subject 33 leftward): "33 que procrée…" requires a matrix verb for 33 — none present; word order "33 que [V]" is ungrammatical as a conjunction clause. REJECTED.
- P-c (56 = infinitive "procréer"): "que procréer" is ungrammatical in standard French (no governing verb). REJECTED.
- P-d (56 = participle/passive): no auxiliary; unlicensed. REJECTED.
- P-e (que = interrogative "what", 33 vocative): "33, que procrée 69?" = "33, what does 69 beget?" — grammatical in isolation, but again strands 26 (69's verb per the landed battery) with 69 double-booked. REJECTED.
- P-f (33 = verb, "et [33] que" per val-33-verb's queued hypothesis): still leaves "que [56] [69] [26]" = two finite verbs (56, 26) with no coordinator. REJECTED.

No grammatical parse exhibits a finite 56 at @1626 without contradicting a standing promoted verdict. The clause structure is genuinely underdetermined at battery grade — this is parse-1626-clause's (queued) venue, not re-litigated here.

**C1: FAIL — does not resolve.** "Not excluded" is not "parses": no parse can be exhibited, so the bar's iff is not satisfied.

### W1745 — @1745 "94 82 46 56 40 06 65" (C2)

Core: "que [56]e-ent [65]" = "que procréent [65]". Xéent stem parse ("[56]" + 40='e' + 06='ent' = 3pl) adopted from rightedge-56-1745 C2 / stem-56-whole's budgeted orphan — zero contradiction, not re-litigated. Parse: conjunction "que" (46 banked) + 3pl "procréent" + postverbal subject 65 (noun class, R18-001) — postverbal subjects are licensed in subordinate clauses ("que vinrent les témoins"). Objectless frame: licensed by Littré's absolute use of procréer ("usable absolument") — "que procréent [65]" = "that [65] procreate/engender". Grammatical and semantically coherent as an event (selectional detail waits on 65's value; sel-65-1745-pressure queued).

Prefix residual "94 82" ("ne m"): under the 94='ne' strong lead the prefix is syntactically awkward ("ne me que" word order fits neither restrictive "ne…que" nor ne explétif), and no "pas" exists anywhere downstream (@1743–1846 contains zero 30 — verified) to complete a negation. The "94 82 46" trigram is a stream hapax. This residual does NOT falsify the core: the engender reading of "que procréent [65]" parses with zero contradiction, and C2's result is independent of 94's value (fenced red-team venue).

**C2: PASS.** An engender reading parses at @1745. Note: procréer's absolute use fits this objectless frame better than the strictly-transitive rivals (créer, recréer, gréer, dégréer) — a gradient advantage, not a discrimination (shared with maugréer/agréer/suppléer).

## Per-clause results

- C1 (@1626): FAIL — no grammatical engender parse exhibitable at battery grade; clause structure underdetermined (parse-1626-clause queued).
- C2 (@1745): PASS — "que procréent [65]" parses cleanly; absolute use licensed.

## Adverses

None listed for this target. §7 check: no standing verdict contradicted — C2 adopts rightedge-56-1745 C2 / stem-56-whole's orphan cause without re-litigation; C1 defers to parse-1626-clause (queued). No value named, no polyvalence declared, noun/verb class alternation untouched (red-team venue per stem-56-whole C2).

## Verdict: NULL (fence executed)

The bar's iff is not satisfied (C1 unresolved), so per the bar's own alternative the identity is fenced. Procréer is NOT excluded — it parses at @1745 (with a gradient fit advantage on the objectless frame via Littré's absolute use) and at @795 (no discriminator) — but "not excluded" does not resolve the 8-way tie, and @1626's clause structure blocks any semantic verdict there at battery grade.

## Follow-ups proposed (nulls regenerate work; 3)

1. `procreer-rerun-1626` (P3, gated on parse-1626-clause) — once parse-1626-clause lands the clause structure, re-test the engender reading at @1626: if 56 resolves as finite 3sg with a named subject, apply procréer's selectional restriction (animate patient, "engendrer") to the agent/patient slots; an animate patient promotes procréer, an artifact/institution patient kills it at semantic grade.
2. `procreer-absolute-corpus` (P3) — corpus attestation check (code/side-period/corpus/) for objectless "procréer/procrée/procréent" frames in 1841 French: is Littré's absolute use live in-register? An attested absolute "procréent" makes @1745's objectless frame a positive selector for procréer over the strictly-transitive rivals (créer/recréer/gréer/dégréer). (Parent's 3pl-form census found procréent 0/32M — form attestation, not frame attestation; this is new work.)
3. `procreer-patient-37` (P4, gated on sel-37-pressure) — once 37's value is named, apply the "engendrer" selectional at @795/@1658 ("qui [56] [37]"): an animate/offspring-like 37 promotes procréer; an artifact/institution/abstract-non-engenderable 37 kills it at semantic grade.

## Bookkeeping

- Queue: `procreer-56-semantic` → status `verdict`, result `null`, date 2026-10-09, report this file (temp-file + rename; pre-write assert passed — was `queued`, verdict placeholder null; JSON re-validated; own entry only).
- Lock `locks/procreer-56-semantic.lock`: created on start, deleted on completion (verified gone).
- `canonical.py` never used; R5005, sealed gates, red-team queue untouched. No numbers invented: every @-offset byte-derived from the repaired stream in-worker.
