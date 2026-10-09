# Battery par43-suite-adverbial — report

Target: `par43-suite-adverbial` (priority 3).
Evidence chain: battery-par43-ce-scope.md NULL 2026-10-09, follow-up 1.
Status: queued. Verdict: **PROMOTE**.

## Bar (verbatim)

(a) bare "par suite" adverbial attested in Littré/TLF with the needed shape; (b) if unattested, the "par suite" escape closes with stated cause

## Numbered clauses (pre-registered before testing)

- C1: bare "par suite" as sentential adverbial ("consequently") is attested in Littré and/or TLF with the needed shape → PROMOTE leg.
- C2: if unattested, the "par suite" escape closes with stated cause → KILL.

## Method

- Read the 19th-century Littré (Dictionnaire de la langue française, 1872–1877, public domain) entry for "suite" in full via its published page; checked the numbered "Par suite" sub-entry for a bare adverbial gloss and example.
- Censused "96 43" windows byte-exact on the repaired 1,847-pair stream (repaired_offsets.json + data/upstream-ct_R5005.txt, parsed like repair_parse.py; assert len(pairs)==1847 held). canonical.py never used.

## Findings

**C1 PASS — attested in Littré with the needed shape.**

Littré's entry "suite" contains a dedicated sub-entry §27 for "Par suite":

- Gloss: "par une conséquence naturelle" (= consequently).
- Attestation example: "On rejeta cet article du projet, et, par suite, toutes les dispositions qui s'y rapportaient."
  - "par suite" is bare (no complement, no determiner), set off by commas in clause-initial position, with sentential scope: exactly the sentential-adverbial "consequently" shape the escape requires.
  - The needed shape is the sentential adverbial, not the prepositional "par suite de" (which Littré lists separately in the same sub-entry: "Par suite des arrangements pris, vous serez payé" — locution prépositive).

Littré's nominal sense for "suite" here is sense 15, fig.: "Conséquence, effet, résultat" — consistent with 43 as noun-class ("suite") followed by the preposition "par".

**Window geometry (repaired stream):**

"96 43" is exactly 2× stream-wide, byte-identical frames:
- @342 (row a2_05): `64 45 64 96 43 87 01 06` (context `14 45 64 96 43 87 01 06`)
- @1026 (row a6_03): `64 45 64 96 43 87 01 03` (context `64 45 64 96 43 87 01 03`)

Reading: `…[64=qui] [45=ce, A11] [64=qui] [96=par] [43] [87=ce] [01]…` — under the bare-adverbial route, "…qui, par suite, ce…" is syntactically licensable in 1841 French per Littré's attested shape ("et, par suite, toutes les dispositions…"). The adverbial escape therefore stays open at both windows.

C2 does not fire.

## Adverses

None listed.

## Scope

- This is a dictionary-attestation license, not a value naming: 43 stays at its Round-19 banked class (noun); "suite" is not claimed as 43's value here.
- The bare-adverbial license applies to both "96 43" windows identically (same byte frame).
- No standing or red-team verdict contradicted or downgraded; §7 intact (67 sole polyvalence); R5005, sealed gates, and the red-team adjudication queue untouched.
- Canonical-stream caveat stands (rows a2_05/a6_03 unvalidated).

## Per-clause pass/fail

- C1: PASS (Littré §27 attests bare "par suite" sentential adverbial "consequently").
- C2: does not fire.

## Verdict

**PROMOTE** — the "par suite" bare-adverbial escape is licensed in 1841 French at battery grade.

## Follow-ups

None required per §4 (promote).
