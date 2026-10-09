# Battery verdict: pas-bare-corpus

**Target claim:** corpus test: bare 'pas' (no 'ne') as clause negator in 1841 diplomatic prose.
**Date:** 2026-10-09. **Priority:** 3.

## Bar (verbatim, pre-registered)

">=1 genuine attestation licenses @1561; confirmed zero hardens this fence. Distinct from ne-1330-bare-corpus (bare 'ne' test)"

Numbered clauses (fixed before testing, not modified after):

1. **C1 (license arm)** — ≥1 genuine attestation of bare "pas" (no "ne") as a clause negator in 1841 diplomatic prose → licenses the bare "pas" at @1561.
2. **C2 (fence arm)** — confirmed zero genuine attestations → hardens the reseg-1564-pasent fence.

Adverses: none listed.

## Method

Read BATTERY-PROTOCOL.md first. Lock `pas-bare-corpus.lock` created on start, deleted on completion. Re-derived the repaired 1,847-pair / 96-type stream in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (parsed per `repair_parse.py`; 1,847 pairs / 96 types asserted). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched. 1841 diplomatic French throughout. 0-based indices below unless noted.

Locus context (adopted from `battery-reseg-1564-pasent`, not re-litigated): @1561 = 30='pas' sits mid-clause ("la [26] pas ent[60-verb]…") with no 94='ne' in the clause. The question is only whether 1841 diplomatic prose ever uses bare "pas" as a clause negator.

Census design (script `code/crowd17/next-token/pasbare_census.py`, triage `pasbare_triage.py`):
- Corpus: lane period corpus, 75 files, 34,525,238 chars (provenance: `code/side-period/corpus/PROVENANCE.md`).
- Normalization: curly apostrophes → "'"; lowercased.
- Candidate rule: a "pas" token is a candidate iff no "ne"/"n'"/elided "n'X" occurs to its left in the same clause.
- Two real bugs found and fixed mid-run (methodology notes):
  1. Elided "n'X" tokenizes whole ("n'a", "n'est") — first run missed them; fixed with `startswith("n'")`.
  2. Sentence splitting on newlines stranded "ne" across line breaks (e.g. Gutenberg "Je ne\ncommettrai pas" became a false candidate). Fixed: split only on `[.!?…]`, never on newlines; leftward "ne" scan bounded by the nearest ";" or ":" or 120 tokens.
- OCR noise handled: fused "dene"/"quene" (= "de ne"/"que ne"), "ne'" spacing, bare "n" token (= dropped "n'").

Scale: 32,095 "pas" tokens → 2,611 bare candidates → triage classes: 1,083 det/non+pas ("un pas", "non pas", "pas mal"), 117 prep+noun-pas ("à grands pas"), 246 pas+de/à, 1,165 other prime. Of the prime, 516 verb-adjacent; 269 immediately verb-adjacent (finite verb token directly before/after "pas"). **All 269 hand-audited in full sentence context.**

## Audit results

**Formal/diplomatic texts (157 candidates: guizot mémoires, revue des deux mondes, nesselrode, metternich, pozzo-di-borgo, talleyrand, levant-correspondence): ZERO genuine.** Every hit is one of:
- OCR "ne"/"n'" drop: "suffisait pas" (= "ne suffisait"), "navions pas" (= "n'avions", apostrophe dropped), "nousne demandons" (fused), "né prendrait" (= "ne prendrait"), "ue changeaient" (= "ne changeaient"), "ignorez pas" (= "n'ignorez"), "l'avons pas" (= "ne l'avons"), "ilne voudra" (fused), "in'ont-ils pas" (= "ne m'ont-ils"), "is'opérons" (= "n'opérons"), and dozens more. The djvu OCR systematically drops short "ne"/"n'".
- Hyphenation: "pas-sait" (= "passait"), "pas-ser" (= "passer"), "pas-sible" (= "passible"), "pas-sionné" (= "passionné").
- Noun "pas" (steps): "mauvais pas", "grands pas", "à grands pas", "cinquante pas".
- Elliptical fragments, not clause negators: "pas assez", "pas encore", "pas d'affront", "pas d'explications", "mais pas plus loin", "pas le moins du monde ébranlé", "pas vrai" (tag), "pas mal" (= beaucoup, idiom).
- ";" clause-bound artifacts: "Ne vous y\nlaissez pas tomber" split at ";" hid the "Ne" (verified in raw bytes).

**Comedy/drama dialogue (112 candidates: labiche, dumas, hugo, musset, scribe, vigny, delavigne): ~10 genuine bare-"pas" clause negations** — all colloquial "ne"-drop in speech, e.g. "connais pas" (Labiche ×6), "je sais pas ousqu'elle a passé", "c'était pas pour les mettre", "faut pas faire la petite bouche", "faut pas dire de bêtises", "je prendrai pas turin". **All are post-verbal** ("V pas"); none is pre-verbal "pas V". None is in diplomatic prose.

## Per-clause results

- **C1 FAILS:** zero genuine attestations of bare "pas" as clause negator in 1841 diplomatic prose across 34.5M chars, with the entire 269-item verb-adjacent candidate set hand-audited. The only genuine hits are colloquial dialogue "ne"-drops, a different register, and all post-verbal.
- **C2 FIRES:** confirmed zero hardens the reseg-1564-pasent fence.

## Verdict: KILL

The existential claim — bare "pas" as clause negator in 1841 diplomatic prose — is rejected at the lane's distributional standard (34,525,238 chars; full hand-audit of the verb-adjacent set). The reseg-1564-pasent fence hardens: "pas" @1561 has no corpus license.

## Scope

- Kills only the bare-"pas" license claim. Untouched: 30='pas' standing value, the reseg-1564-pasent NULL (its fence is now harder, not re-litigated), the sibling follow-ups `reseg-1564-26pas` and `ent60-71-complement`, and the "non pas" construction (licensed formal French, but it does not license bare "pas" and is out of scope for @1561, which has no "non").
- Positional note: even the colloquial dialogue license is post-verbal ("connais pas"); @1561 needs pre-verbal "pas" + finite verb ("pas ent[60]"), a geometry with zero attestations in any register. No standing/red-team verdict contradicted or downgraded; §7 intact; canonical-stream caveat stands.
- Per §4 (kill), kills regenerate no follow-ups.

## Bookkeeping

- Report: this file (`code/crowd17/report_inbox/battery-pas-bare-corpus.md`).
- Scripts + data: `code/crowd17/next-token/pasbare_census.py`, `pasbare_triage.py`, `pasbare_candidates.json`, `pasbare_triage.json`, `pasbare_adj.json`.
- `battery-queue.json`: `pas-bare-corpus` → status `verdict`, result `kill`, date 2026-10-09 (pre-write assert confirmed queued/verdictless; temp-file + rename; own entry only; no downgrade).
- Lock `locks/pas-bare-corpus.lock`: created on start, deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched.
