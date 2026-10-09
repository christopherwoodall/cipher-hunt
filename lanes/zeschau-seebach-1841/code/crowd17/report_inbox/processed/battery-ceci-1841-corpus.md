# Battery report — ceci-1841-corpus

Worker: battery-worker-ceci-1841-corpus (agent 26684549-b0cb-436d-ba59-dcca73efb460). Date: 2026-10-09.
Lock: `code/crowd17/next-token/locks/ceci-1841-corpus.lock` created 2026-10-09T18:17:07Z, no prior lock; deleted on completion.
Protocol: BATTERY-PROTOCOL.md read first. Repaired 1,847-pair / 96-type stream convention; corpus is period French, not the cipher stream. `canonical.py` never touched. R5005, sealed gates, red-team adjudication queue untouched.

## Claim
Corpus check that 'faire ceci' is attested in 1841 diplomatic French (strengthens E3 from grammaticality to attestation).

## Bar (verbatim, from dispatch brief)
"Attested or not with corpus evidence; strengthen or fence accordingly."

Numbered clauses:
1. If 'faire ceci' (infinitive) is attested in the period corpus → STRENGTHEN: E3 promoted from grammaticality to attestation.
2. If 'faire ceci' is unattested in a corpus where 'ceci' itself is live → FENCE: E3 stays at grammaticality grade; the attestation arm is closed on this evidence.

## Method
Searched `code/side-period/corpus/` (French files only; 18 German files — allgemeine-zeitung*, adb-zeschau*, metternich* — excluded, per lane convention). 56 French files, 29,487,621 chars. Accent-insensitive matching (NFD strip), case-insensitive, word-boundary regexes. Script inline in worker session; re-runnable.

## Findings

- **'ceci' itself: 397 occurrences** — well attested in the corpus. A zero for 'faire ceci' is informative, not corpus depletion.
- **'faire ceci' (infinitive): 0** in 29,487,621 chars.
- Conjugated-frame sweep for comparison:
  - 'fait ceci': 0 | 'font ceci': 0 | 'fasse ceci': 0 | 'faites ceci': 0 | 'faisons ceci': 0
  - **'fais ceci': 1** — raw-thtredecasim01dela-djvu.txt: "Fais ceci, fais cela ; maladroit! …" — imperative mood (drill-sergeant command), not the infinitive frame. Does not attest 'faire ceci'.
- Frame-existence control: **'faire cela': 4**, **'fait cela': 19**, 'faire le': 111 — the "faire + demonstrative" frame is live in the corpus, but with 'cela', not 'ceci'.

## Clause pass/fail
1. (strengthen arm) FAIL — 'faire ceci' unattested.
2. (fence arm) PASS — 'ceci' is live (397x), so the zero is a genuine attestation gap, not a depleted-corpus artifact.

## Verdict: NULL (attestation arm fenced)

E3 is NOT strengthened to attestation. The attestation arm is fenced on 29.5M chars of 1841 French: the infinitive 'faire ceci' does not occur. This does NOT refute E3's grammaticality basis — 'faire cela' is attested and 'ceci' is a normal demonstrative — but E3 cannot be promoted above grammaticality grade on this evidence. (Per §5.2: no standing red-team verdict contradicted; §7 intact.)

## Follow-ups (null regenerates work)

1. **ceci-inf-frame-widen** (P4) — sweep other infinitive+ceci frames ('dire ceci', 'penser ceci', 'voir ceci') across the same corpus: does 'ceci' systematically resist infinitive complements, or is the gap 'faire'-specific?
2. **faire-cela-register** (P4) — break the 4 'faire cela' hits by register (prose vs drama); if the cela/ceci split in "faire + DEM" is register-driven, E3's attestation arm may re-open under a register condition.
3. **e3-grammaticality-census** (P4) — full "faire + [demonstrative]" census to re-base E3 on cela-attestation plus ceci-parity reasoning, if the red team wants a strengthened grammaticality statement.

## Bookkeeping
- Report: `code/crowd17/report_inbox/battery-ceci-1841-corpus.md`
- Queue: `ceci-1841-corpus` → `status: verdict`, `result: null`, 2026-10-09 (pre-write assert: was queued/verdictless; temp-file + rename; own entry only; no downgrade).
- Lock created on start, deleted on completion.
