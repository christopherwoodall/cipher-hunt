# Battery verdict: agr-89-642-adj — **PROMOTE** (adjective arm confirmed agreement-admissible)

## Target
- id: `agr-89-642-adj` (priority 3)
- claim: agreement check — does "le [89]e" admit an adjectival 20 (gender/number compatibility once 89's value resolves)?
- Parent: `subj-20-642` PROMOTE (2026-10-09) — follow-up 1 of 1. Adjectival 20 at @642 was the unique grammatical survivor; this target gates it on agreement.
- adverses: none listed.

## Bar (verbatim from battery-queue.json)
"Bar: agreement check: does "le [89]e" admit an adjectival 20 (gender/number compatibility once 89's value resolves)? Bar: confirm or fence the adjective arm on agreement grounds."

Numbered pass/fail clauses (restated before testing — bar not modified after data):
1. **C1:** no forced gender/number mismatch exists under standing values → adjective arm CONFIRMED as agreement-admissible.
2. **C2:** if a forced mismatch exists → fence the adjective arm with stated cause.

Verdict rule: confirm (promote) iff C1 passes; else null with fence.

## Method
Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/agr-89-642-adj.lock`
on start (agent 6744e2b4-9306-4eee-947e-61538a178ccc, 2026-10-09T13:05:01Z); no prior/stale
lock. Re-derived the repaired 1,847-pair / 96-type stream in-session from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
(tokenization per `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs,
96 types). `canonical.py` never used. R5005, sealed gate instances, and the
red-team adjudication queue untouched.

Adopted standing premises (used, not re-litigated):
- 77="le" — provisional (protocol §7); masculine singular determiner.
- `subj-20-642` PROMOTE: "77 89 48" = closed NP "le [89]e", noun forced (arm A);
  20 at @642 = post-nominal adjective, the unique grammatical survivor.
- 48="e" — promoted inflectional ending (the word-final "e" of "[89]e").
- 89's global class (noun vs infinitive) is red-team venue (`class-89-adjudicate`
  packaged; `noun-89-1377-adjudicate` null; 89's value open).
- 20's global class/value unvalued (`noun-20-value`, `det-20-value` null;
  `poly-20-docket` red-team venue).
- 67 et/veut sole polyvalence; positional rule stands.

## Locus (byte-exact, re-derived)
0-based @639–642, row a4_01: `77 89 48 20` = "le [89]e [20]", followed by
@643=24 (finite/modal, R17-009) and @644=87 "ce".
89 census: n=14 (@113/@222/@275/@285/@303/@640/@781/@871/@986/@1082/@1377/
@1393/@1498/@1752). The @640 window is the "le [89]e [20]" locus.

## Agreement check

1841 French: a post-nominal adjective agrees with its noun in gender and
number. Under the standing premises:

1. **Gender of the noun.** 77="le" is masculine singular (provisional, standing).
   The adjective arm therefore requires 89's noun to be masculine. Nothing in
   standing values forces 89 feminine:
   - 89's value is open (infinitive-shaped under 24 at @222; "-re" family; value
     candidates faire/dire/mettre unvalued).
   - 48="e" is a promoted *inflectional* ending, not a banked feminine marker.
     At battery grade the "-e" ending does not force feminine (French has
     masculine nouns in -e); no standing verdict genders 89. A repo-wide grep
     for gender claims on 89 returned none.
   - No contradiction forced. (If 89's value ever resolves feminine, the
     contradiction would fall on the standing 77="le" premise, not on the
     adjective arm alone — recorded as a caveat, not a fence.)
2. **Number.** Singular throughout: "le" singular; no plural marking on 89 or
   20 (no 13-"s" or other plural licensor adjacent). No forced mismatch.
3. **Agreement of 20.** 20's value is unvalued globally, so its masculine-
   singular form cannot be positively spelled out — but nothing forces a
   feminine/plural shape on it either. Agreement is compatible with every
   standing value.

**C1 PASS — no forced gender/number mismatch.** The adjective arm is confirmed
as agreement-admissible. C2 moot.

## Positive deliverable (derived constraint)
Under the standing premises, the adjective arm *constrains* 89's resolution:
once 89's value resolves at this window, it must be a **masculine singular
noun**, and 20 at @642 must agree masculine singular in form. This is a
battery-grade check on any future 89 value candidate at the "le [89]e"
windows: a feminine noun value would collide with 77="le" and re-open the
arm-A NP premise.

## Scope and caveats
- Window-level only (@639–642). No registry change; 89 and 20 stay unvalued.
- 77="le" is provisional — if 77 ever resolves otherwise, the agreement premise
  moves with it.
- 89's global noun-vs-infinitive class stays red-team venue; if the red team
  rules 89 globally non-noun, the "le [89]e" NP premise (and with it this
  window's adjective arm) re-opens — their act, not battery's.
- §7 intact: no polyvalence declared; 67 remains the sole true polyvalence.
- No standing or red-team verdict contradicted or downgraded. Canonical-stream
  caveat stands (row a4_01 upstream row offset unvalidated).
- No follow-ups required per §4 (promote). The derived masculine-singular
  constraint rides with any future 89-value battery at the "le [89]e" windows.

## Bookkeeping
- Queue: `agr-89-642-adj` → `status: verdict`, `result: promote`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; temp-file + rename;
  JSON re-validated from disk; own entry only; no downgrade).
- Lock `locks/agr-89-642-adj.lock` created on start, deleted on completion
  (verified gone).
