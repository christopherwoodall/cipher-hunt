## arm1248: @1248 arm-strengthener (round 11) — "peu" STRENGTHENED 4/8, infinitive-class stays WEAK-FENCED 3/7

- Context: Round-10 (F73) left two WEAK fenced arms at @1248 — "peu" 2/4
  (L2+L3; L1 failed hapax, L4 indeterminate) and infinitive-class
  "empêcher" 2/4 (L2+L3; L1 failed singleton, L4 indeterminate). Work
  order 5: strengthen with genuinely NEW legs (new era attestations, new
  structural arguments, new window interactions) or fence with an honest
  missing-leg inventory. Prereg written BEFORE any new-corpus content was
  examined (`code/crowd11/arm1248/PREREG.md`); every bar pre-registered;
  no round-10 leg re-run; no re-litigation of "cela"/médiatrice-class.
  New-corpus pool: Revue des Deux Mondes 1841 q1–q4 (~12.3 MB, Paris 1841
  formal prose) + Guizot Mémoires t.5–6 (~2.0 MB, printed diplomatic
  despatches/instructions 1840–42). Rate bars stay v8-only per constraint —
  all new legs are attestation/structural/window-kind.

- Decision: "peu" STRENGTHENED (2 new legs pass: P-A, P-B; 0 adverse fired
  → 4/8). Infinitive-class "empêcher" stays WEAK-FENCED (1 new leg: E-A;
  E-B/E-C fail → 3/7). Per-arm details:
  - P-A PASS: 13 genuine "pour peu que"+subjunctive in the pool (11 RDM,
    2 Guizot-DIP incl. Palmerston/Aberdeen diplomatic contexts) — every hit
    constituency-read, 0 artefacts. Arm no longer hapax-anchored in the
    broader 1841 record (v8 L1 bar stays failed — not re-scored).
  - P-B PASS: shape S=(verb-offset 3, clause-length 4) from the primary
    exemplar; PA-5 "pour peu que cette lutte dure encore" matches exactly;
    verb-offset 3 is modal (5/13). Cipher clause 26-30-06-65 (06@offset 3,
    length 4) matches the stable era shape. Bears on L4's subjunctive-host
    question; does not retro-score L4.
  - P-C no leg: sole v8 "X peu que" is comparative-adverbial ("aussi"),
    06-incompatible under all standing readings → @471 "06 peu que"
    unhosted in v8. Adverse bar as written did not fire (one comparative
    host exists) — recorded as adverse-leaning, not a fired adverse.
  - P-D FAIL: "pour W1 W2 pour peu que" ×0 in ~16.5MB — the double-pour
    stack unlicensed.
  - E-A PASS (massively): 28 DISTINCT genuine infinitives in "pour INF que"
    (croire, demander, démontrer, obtenir, montrer, soutenir, comprendre,
    reconnaître, signifier, convaincre, découvrir, prouver, rappeler,
    établir, savoir, éviter, déclarer, constater, témoigner, indiquer,
    empêcher, dire, prétendre, proclamer, débarquer, agir, désirer,
    entrevoir). "empêcher" itself re-attested ×2, incl. EA-39 "nous serions
    là pour empêcher que l'armée égyptienne ne vînt à franchir le canal" —
    Eastern-Question diplomatic context, ne-explétif + subjunctive, the
    exact register of the target despatch. Class-breadth problem solved in
    substance (v8 L1 bar stays failed).
  - E-B FAIL: "MODAL empêcher que" ×0 in v8 (regex self-tested) → @471
    "06 empêcher que" unhosted.
  - E-C FAIL: "pour W1 W2 pour INF que" ×0 in ~16.5MB.
  - Unscored descriptive (not legs, maps what's missing): E-B in pool ×0
    (the @471 gap is pool-wide); P-C in pool finds verb-compatible hosts
    "il (lui) importe peu que" and "se souciait peu que" (Guizot-DIP) —
    a pool-registered P-C re-run is a concrete follow-up.

- Why: The pre-registered verdict rule (≥2 new PASS + 0 adverse →
  strengthened; exactly 1 → weak-fenced) is what it is — the bar is the
  bar (F72 precedent). "peu" cleared it; "empêcher"-class didn't. The new
  corpora dissolved the singleton/hapax worries (the v8 zeros now read as
  Nesselrode-idiolect, not construction-absence) but exposed a sharper
  structural gap: the double-pour stack "pour 33 16 pour 67 que" — the
  window's most distinctive feature — has NO era license anywhere checked,
  for either arm.

- Enlightenment: Two surprises. (1) The "pour INF que" class is wildly
  productive in 1841 (28 lemmas) — the round-10 singleton framing was a
  v8-corpus artefact, and one of the new "empêcher" hits sits in the exact
  Eastern-Question diplomatic register of the despatch. (2) The clause-shape
  leg worked better than expected: the cipher's 4-group clause with the
  verb-morphology group at offset 3 mirrors the modal era shape
  (verb-offset 3 in 5/13 new hits), and PA-5 is a byte-shape twin of the
  primary exemplar. The honest surprise in the other direction: BOTH arms
  fail to host @471, and BOTH fail the double-pour — the arms are stronger
  on era attestation than on window structure.

- For the report: new section or F73 amendment — per-arm verdicts above.
  Numbers that matter: P-A 13/13 genuine; P-B 1 exact S-match (PA-5) +
  modal offset-3 in 5/13; E-A 28 distinct infinitives (49/52 genuine,
  3 excluded: 2 noun false-positives, 1 restrictive ne...que); E-B 0;
  E-C 0; P-D 0; P-C 1 comparative host, 0 verb-compatible. Arm totals:
  peu 4/8, empêcher-class 3/7. Files:
  `code/crowd11/arm1248/PREREG.md`,
  `code/crowd11/arm1248/arm1248_strengthen.py`,
  `code/crowd11/arm1248/arm1248_strengthen_raw.json` (all hit contexts),
  `code/crowd11/arm1248/arm1248_strengthen_results.json` (adjudication).

- Caveats: (1) New-corpus hits are OCR text; frames counted only where
  unambiguous (OCR splits noted per hit in the results JSON). (2) Register
  assessment is the executor's — flagged for frenchman review, not claimed
  on his authority. (3) P-B/P-C cipher-side claims are conditional on 06's
  fenced verb-morphology standings; 06's value is unidentified.
  (4) n_eff=1 stands — any @1248 reading is a singleton. (5) Unscored
  pool checks must not be promoted to legs without a registered re-run.
  Missing-leg inventory (peu): v8 L1 rate, L4 window closure, @471 host
  (pool re-run follow-up), double-pour license, n_eff=1. (empêcher-class):
  v8 L1 rate, @471 modal license (pool-wide zero), stacked-pour license,
  L4 agent subject ("le 81 cela" doesn't parse as agent), n_eff=1.
