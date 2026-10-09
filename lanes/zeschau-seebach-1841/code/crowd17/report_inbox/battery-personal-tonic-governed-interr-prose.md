# Battery report: personal-tonic-governed-interr-prose — verdict: NULL

Target id: `personal-tonic-governed-interr-prose`
Claim: interrogative-force variant of the governed-exclamatory battery.
Date: 2026-10-09. Worker: agent 9ac71ef7-c299-43c9-8fa6-6fb0eb71cfa0.

## Bar (verbatim, pre-registered)

"run a targeted census for tonic-topic + pour/de/a-governed infinitive
terminated by '?' where the question force plausibly falls on the infinitive
itself ('Moi, pour quoi faire ?'): >=1 genuine names the interrogative shape;
0 genuine closes the force dimension"

Numbered clauses:
- C1 (name arm): >=1 genuine hit names the interrogative shape → FAIL
- C2 (closure arm): 0 genuine closes the force dimension → PASS (vacuous)

## Method

Copied the 20-file prose corpus and P1/P3 verbatim from the sibling
`personal_tonic_governed_excl_prose_recall_census.py`; changed ONLY the P2
filter: the window (pronoun through the next [?!.], capped at 400 chars) must
be FIRST-terminated by "?", so the interrogative force plausibly falls on the
infinitive phrase itself. Windows first-terminated by "!" are excluded (the
exclamatory arm is fenced separately).

- P1 (dislocation): `\b(moi|toi|lui|elle|nous|vous|eux)\s*[,;:]` (case-insens)
- P2 (interrogative): first terminator in the window is "?"
- P3 (governed infinitive): strict `\b(?:pour|de|d'|d’|à)\s+...{2,}(er|ir|re|oir)\b`;
  loose (clitic-tolerant, ≤2 short intervening words), tagged separately

Script: `code/crowd17/next-token/personal_tonic_governed_interr_prose_census.py`;
data: `code/crowd17/next-token/personal-tonic-governed-interr-prose_census.json`.

Corpus gate verified: 20 files, 27,656,185 chars, 4,495 pronoun-comma hits —
identical to the parent's counts.

Gates for genuine (stated in the bar): G1 dislocated tonic topic (understood
subject of the infinitive); G2 pour/de/à-governed infinitive; G3 the "?"
terminates the infinitive phrase itself (question force on the infinitive);
G4 no finite verb governing the infinitive inside the window (self-contained).

## Findings

Yield: **53 candidates (35 strict, 18 loose-only), all hand-read with
±700-char context: 0 genuine.**

- C1 FAIL: no candidate passes all four gates.
- C2 PASS (vacuous): the prose zero is not a window/termination artifact; the
  force dimension closes in prose at battery grade.

Dominant confound classes (all 53 with cause):
- Finite-matrix-governed infinitives (largest class): [8]–[13], [16], [18],
  [20]/[21], [23], [28], [31]–[33], [36]–[40], [45], [48], [49], [52] — the
  governed infinitive answers to a finite verb ("songeaient qu'à s'enrichir",
  "cherché à faire", "devions-nous perdre l'occasion de défaire"), and the
  "?" force falls on that finite verb (G3/G4 fail).
- Preposition-object pronouns: [0], [1], [5], [14], [15], [17], [22], [24]–[27],
  [34], [35], [37]–[39], [44], [46], [47], [50], [51] — "autour de lui",
  "contre elle", "jusqu'à eux", "suivant moi", "chez vous" (G1 fail).
- Vocatives / parentheticals: [2], [6], [7], [18], [19], [45] — "Croyez-vous,
  mylord" (G1 fail).
- Finite-subject pronouns: [3], [4], [9]–[13], [30], [32], [33], [41], [42] —
  pronoun is subject of a finite verb, not a dislocated topic (G1 fail).
- Nearest misses (genuine shape minus one gate):
  - [42] rdm-q4 "ai-je craint, moi, de me compromettre?" — "moi" IS a
    dislocated tonic topic (G1 PASS), but the infinitive is governed by the
    finite "ai-je craint" and the "?" force falls there (G4 fail).
  - [30] rdm-q2 "Lui, depuis six mois entiers qu'il est investi de la
    dictature, qu'a-t-il fait?" — "Lui" is a true dislocated topic (G1 PASS),
    but there is no governed infinitive at all ("de la dictature" is a noun
    phrase; G2 fail).
  - [23] rdm-q1 "Et vous, mon fils, auriez-vous poussé l'amour de l'art...
    jusqu'à vivre ici sans regret?" — dislocated "vous" (G1 PASS), but "vivre"
    is a purpose adjunct of the finite "auriez-vous poussé" (G3/G4 fail).

## Scope

Closes the interrogative-force dimension in prose only. Untouched: the drama
register (the parent's exclamatory shape lives there); the bare-shape
findings; the already-dead @1029 routes. §7 intact; no standing/red-team
verdict contradicted or downgraded. Canonicality caveat stands. `canonical.py`
never used.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-personal-tonic-governed-interr-prose.md`
- Script + data: `code/crowd17/next-token/personal_tonic_governed_interr_prose_census.py`,
  `code/crowd17/next-token/personal-tonic-governed-interr-prose_census.json`
- Queue: `personal-tonic-governed-interr-prose` → `status: verdict`,
  `verdict: {result: "null", report: ".../battery-personal-tonic-governed-interr-prose.md",
  date: "2026-10-09"}` (pre-write assert passed — was queued/verdictless;
  temp-file + rename; disk re-validated; own entry only; no downgrade)
- Lock created on start, deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched.

## Follow-ups proposed (all verified ABSENT from queue)

1. `personal-tonic-governed-interr-drama` (P3) — drama-register
   interrogative-force variant: the drama register licensed the parent's
   exclamatory shape; test whether '?' force does too. Same P1/P3, drama
   corpus, first-terminator-'?' filter.
2. `personal-tonic-interr-inf-negation-prose` (P4) — negation-scoped subclass
   ("Moi, pour ne pas rire ?"): negation may license a bare interrogative
   infinitive where the plain form fails.
3. `gov-interr-inf-ellipsis-shape` (P4) — ellipsis-interrupted variants where
   the '?' belongs to an elided later clause: hand-classified candidates of
   this shape were thin (3 analogous confounds in the drama exclamatory
   sibling); bound the subclass.
