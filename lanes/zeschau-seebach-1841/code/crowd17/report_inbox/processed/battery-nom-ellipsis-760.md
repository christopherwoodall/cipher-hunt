# Battery `nom-ellipsis-760` — verdict: PROMOTE

- Target id: `nom-ellipsis-760` (P3)
- Claim: test whether the 'la premiere' nominalization-ellipsis premise is independently licensed at @754-759; all three live 20-roles share it as a load-bearing assumption.
- Date: 2026-10-09
- Worker: battery worker (subagent 68ef8c4b)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). Verified in-session: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- Offset note: all @-offsets are 0-based pair indices.

Terms (ASD-STE100): "bare nominalization" = an adjective standing alone as a noun phrase with no head noun (e.g. "the first [one]"). "Bar" = the pass/fail test the battery must run. "Battery grade" = the evidence standard of this pipeline.

## Bar (verbatim from battery-queue.json, pre-registered before testing)

> Licensed iff a byte-grounded precedent exists for bare 'la premiere' nominalization in the stream or 1841 French; else fence.

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** a byte-grounded precedent for bare 'la premiere' nominalization exists in the repaired cipher stream (an occurrence outside the disputed @754-759 locus functioning as a bare nominal).
2. **C2:** a byte-grounded precedent for bare 'la premiere' nominalization exists in 1841 French (hand-classified corpus examples in the lane's standing period corpus).
3. **C3:** verdict = licensed (PROMOTE) iff C1 or C2 passes; else fence (NULL).

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/nom-ellipsis-760.lock` on start (agent id + UTC timestamp); deleted on completion. No stale lock was present.
2. Re-derived the repaired stream in-session; re-ran all asserts (1,847 pairs, 96 types).
3. Adopted as premises, not re-litigated: §7 banked ground truth (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e); the manuscript pencil gloss "la pre m i er e" over row a5_03 groups "11 70 82 34 29 40" (byte-verified: raw digit substring "117082342940" at raw offset 1532, even pair-phase — see `code/side-keyhunt/repair_parse.py` gloss (i)); R19 red-team rulings; §7 sole polyvalence (67 et/veut).
4. Corpus: the lane's standing 1841 period corpus (`code/side-period/corpus/`, 63+ period texts — diplomatic memoirs/correspondence, 1841 press, revue des deux mondes; provenance in `code/side-period/corpus/PROVENANCE.md`). Normalized whitespace (OCR double-spacing), case-insensitive search for "la premiere", then hand-classified every hit as bare nominalization vs. head-noun-following.

## Window evidence (byte-exact, 0-based, independently re-derived)

- The "la premiere" 6-gram `11 70 82 34 29 40` occurs exactly **2x stream-wide**: @754 (row a5_03, the disputed locus: `... 40 67 11 70 82 34 29 40 20 62 94 59 39 88 66 98 ...`) and @1034 (row a6_03: `... 96 43 87 01 03 29 80 77 11 70 82 34 29 40 17 77 82 63 11 67 76 85 ...`).
- The "70 82 34 29 40" syllable chain (without 11) occurs only in those same two windows. The bigram "11 70" occurs only 2x. So there is no third in-stream locus to adjudicate.
- @1034 is followed by 17 (=fois, red-team granted): "la première fois" — head noun PRESENT. Not a bare nominalization.
- @754 (the locus) is followed by 20: "la première" with NO head noun — the bare-nominalization reading under test.

**C1 result: FAIL.** The stream supplies no independent bare-nominalization precedent; the only other occurrence carries an overt head noun (fois).

## Corpus evidence (1841 French, hand-classified)

113 occurrences of "la premiere" / "La premiere" (whitespace-normalized, case-insensitive) in the period corpus. Hand-classified by what follows:

- **30 bare nominalizations** (no head noun; the ordinal stands alone as an NP), all in Metternich's *Papiere* v4/v6 (French diplomatic correspondence — the cipher's own register):
  - bare subject, finite verb follows: "La premiere exige peu de developpement" ; "La premiere est celle de savoir si les Cabinets n'auraient pas pu..." ; "La premiere conduira a tout; la seconde ne conduira a rien" ; "La premiere joue son jeu, et en cela eile a raison" ; "la premiere serait marquee par la proposition peremptoire" ; "Si la premiere etait noire et la seconde grise, la presente est blanche" ; "et la premiere pourrait avoir tout le mauvais efFet de la derniere" ; "La premiere de ces periodes est passee" ; "la premiere de ces causes est intolerable a la longue" ; "Si la premiere de ces influences est insurmontable"
  - bare partitive ("la premiere de ces X"): "guerir de la premiere de ces maladies" ; "Dans la premiere de ces hypotheses" ; "La premiere de ces periodes est passee" ; "la probabilite est en faveur de la premiere de ces chances" ; "la premiere de ces Puissances a manque son but"
  - bare object/complement: "La seconde mesure est traitee par M. Canning comme la premiere" ; "Traitera-t-il la nouvelle entreprise comme la premiere ?" ; "faire lever la premiere" ; "qui ainsi se confond avec la premiere"
  - bare topicalized: "Quant a la premiere, nous nous sommes rencontres" ; "Dans la prise en consideration de la premiere de ces parties"
- 83 with a following head noun ("la premiere fois/nuit/question/lettre/nouvelle/epoque/campagne/partie/occasion/demarche/...") — the ordinary determined-adjective shape.

**C2 result: PASS, overwhelmingly.** 30 hand-classified bare "la première" nominalizations in 1841 diplomatic French, in subject, object, partitive, and topicalized positions. The shape "la première ; ..." (bare ordinal heading a clause, followed by punctuation or a verb) is attested: e.g. "La premiere exige peu de developpement, parce qu'elle concerne des objets..." and "La premiere conduira a tout; la seconde ne conduira a rien".

## Per-clause results

1. **C1 (in-stream precedent): FAIL** — no independent bare precedent; @1034 = "la première fois".
2. **C2 (1841 French precedent): PASS** — 30 genuine bare nominalizations in the period diplomatic corpus.
3. **C3 (bar disjunction): FIRES → LICENSED.** The bar is satisfied by C2.

## Verdict: PROMOTE

The 'la premiere' nominalization-ellipsis premise is independently licensed. Bare "la première" is ordinary 1841 diplomatic French, with 30 byte-grounded precedents in the lane's standing period corpus, in the cipher's own register (diplomatic correspondence). The three live 20-roles at @760 that load on this premise carry a licensed assumption, not an unlicensed one.

**Scope (explicit):** this battery licenses only the grammatical premise — that "la première" can stand as a bare NP. It does NOT name 20's role at @760, resolve the @760 boundary, or ratify the "la première ; mais..." clause parse; those remain battery/red-team venue. No standing or red-team verdict is contradicted or downgraded; §7 intact; canonical-stream caveat stands (rows a5_03/a6_03 unvalidated). R5005, sealed gates, red-team adjudication queue untouched.

**Recorded negative:** the cipher stream itself supplies no second bare occurrence (@1034 has the head noun "fois"), so the stream-internal channel carries no precedent; the license rests on the 1841-French channel alone.

## Bookkeeping

- Adverses: none listed.
- Per §4, promotes regenerate no follow-ups.
- Lock created on start, deleted on completion.
