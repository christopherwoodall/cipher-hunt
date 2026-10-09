# Battery report: pour-que-lexicon-close

- Target: `pour-que-lexicon-close`
- Claim: the 'pour que' discriminator's positive set within French feminine nouns is exactly {condition, mesure} (both dead) — formalize the discriminator as exhausted so no future battery re-runs it.
- Worker: battery worker pour-que-lexicon-close (5efa02f4-7ada-4b8a-b907-93db72cb1a58)
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt), parsed per code/side-keyhunt/repair_parse.py. 1,847 pairs re-derived in-session. `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched. No data invented. @-offsets are 0-based stream indices.
- Lock: created `code/crowd17/next-token/locks/pour-que-lexicon-close.lock` on start (agent id + UTC timestamp), deleted on completion. No fresh lock existed at start.

## 1. Bar (verbatim from battery-queue.json)

"census which French feminine nouns license bare 'N pour que [subj]' in 1841 diplomatic/administrative French with period-dictionary evidence (Littre / Dictionnaire de l'Academie); certify the set = {condition, mesure}"

Numbered clauses (pre-registered BEFORE testing; not changed after seeing data):

1. The census runs on the full candidate space {condition, mesure, suite, manière, façon, raison, fin, cause, intention, précaution, disposition} with period-dictionary evidence (Littré) for bare "N pour que [subj]" in 1841-era French.
2. The certified positive set is exactly {condition, mesure}.

## 2. Method

- Re-derived the repaired stream in-session (1,847 pairs; 43 census n=16 at @21/@43/@244/@258/@343/@386/@439/@563/@1027/@1092/@1126/@1204/@1303/@1305/@1544/@1724 — matches prior batteries).
- Fetched the full Littré (Émile Littré, Dictionnaire de la langue française, 1863–1877; period dictionary named in the bar) entries for all 11 candidate nouns from littre.org (primary source, unmodified HTML, 2026-10-09). All 11 entries mark the noun "s. f." (feminine).
- Tested each noun at two tiers:
  - Tier A (literal): the entry records the bare string "N pour que". Zero hits for all 11 (headword-adjacent grep).
  - Tier B (government): the entry records bare "N pour + infinitif" purpose-government (the French final construction "pour + inf" licenses the finite counterpart "pour que + subj").
- The Dictionnaire de l'Académie 6e éd. (1835) check was attempted (Wikisource /C page is a scan index without inline entry text; artflx unreachable from this VM). Grading rests on Littré, which the bar names first. The Académie gap is recorded, not filled by guesswork.

## 3. Window-level evidence (@-offsets, re-derived)

- @1544 discriminator window (a8_00): `62 06 21 62 93 88 77 78 [43] 00 46 70 12 94 92 45 23` — matches the queue evidence string `62 06 21 62 93 88 77 78 [43]`. 00=pour (A9), 46=que (banked) = "pour que"; 70-12-94 = "prenne" (subjunctive).
- Correction to prior reports: "43→00" occurs 3x stream-wide, not once — @244 (`56 [43] 00 66`, "43 pour [66]"), @1126 (`37 [43] 00 86`, "43 pour [86-INF]"), @1544 (`78 [43] 00 46`, "43 pour que"). Only @1544 carries the full "pour que" tail. "00-46" occurs 4x: @106, @545, @1545, @1680. The correction does not change this battery's bar, but the supervisor should note the earlier under-count.

## 4. Dictionary census (Littré, per noun)

- **condition** — Littré: "À condition que, locut. conjonct. qui régit l'indicatif, ou le subjonctif, ou le conditionnel, et signifie pourvu que." / "On dit aussi à condition de, avec l'infinitif." / jurisprudence: "Faire une donation sous la condition que le donateur survivra au donataire." The que-government is always mediated by "à" or "sous". No bare "condition pour que" anywhere in the entry. → Tier A ✗, Tier B ✗.
- **mesure** — Littré (supplément): "Prendre des mesures pour réussir dans une affaire. Prendre bien ses mesures." / "Prendre des mesures, prendre les dispositions nécessaires pour effectuer quelque chose." Bare noun + "pour" purpose-government, dictionary-recorded. → Tier A ✗, Tier B ✓.
- **disposition** — Littré, sense 6: "Au plur. Préparatifs. Il faisait ses dispositions pour partir." Same bare "N pour + inf" structure as mesure. → Tier A ✗, Tier B ✓.
- **précaution** — Littré, sense 1: "Ce qu'on fait par prévoyance, pour éviter un mal." Citations: "Rien n'est pareil aux précautions de Vauban pour conserver tout le monde, Sévigné, 468." ("précautions … pour + inf", noun directly complemented by "pour"); "Je m'étais purgée par précaution, Dancourt." → Tier A ✗, Tier B ✓.
- **suite** — Littré: "Être à la suite d'un ambassadeur", "à la suite de". "de"-mediated only. No "pour". → ✗/✗.
- **manière** — Littré: "De manière que, loc. conj." / "De manière à, loc. prép. avec le verbe à l'infinitif". "de"-mediated only. → ✗/✗.
- **façon** — Littré: "De façon que, ou de telle façon que, loc. conj." / "De façon à, loc. prépositive, avec l'infinitif". "de"-mediated only. → ✗/✗.
- **raison** — Littré: "À raison de, loc. prépos." / "en raison de". Preposition-mediated; the "pour" citations are "donner pour raison" (different sense). → ✗/✗.
- **fin** — Littré: "À telle fin que de raison (pour une fin telle que la raison indiquera), se dit, dans le style d'affaires" — administrative French, but "à"-mediated. → ✗/✗.
- **cause** — Littré: "À cause de, locut. prép." / "À cause que, locut. conj." → ✗/✗.
- **intention** — Littré: "En intention de ou que, avec la volonté de." "en"-mediated. → ✗/✗.

Certified positive set on period-dictionary evidence: {mesure, disposition, précaution}. Under strict Tier A literalism the certified set is {} — also not {condition, mesure}.

## 5. Per-clause pass/fail

1. **Clause 1 (census with period-dictionary evidence): PASS.** All 11 candidates tested against full Littré entries with exact citations; method and tiers fixed before grading.
2. **Clause 2 (certified set = {condition, mesure}): FAIL at kill grade.** Littré does not certify bare "condition pour que" (condition's que-government is "à condition que" / "sous la condition que" — mediated), while it does certify bare "N pour" purpose-government for disposition ("faire ses dispositions pour partir") and précaution ("précautions … pour conserver"), which the bar's exact set omits. The bar's {condition, mesure} is wrong in both directions. The claim "positive set = {condition, mesure}" is rejected by the primary source.

## 6. Adverses

- "period-corpus defense of bare 'par mesure'/'par condition'" — fenced: belongs to queued par43-adverbial-attestation / red-team venue. This battery's dictionary kill of the pour-que formalization stands independently of it.
- "@21 polyvalence ruling" — fenced: red-team act only per §7 (67 et/veut is the sole true polyvalence), already escalated by battery-43-29-segment. Not decided at battery level.
- No standing verdict is contradicted or downgraded: the suite/manière kills, cond-mesure-43full's empty survivor set, 43-29-segment's segmentation promote, and noun-43's null all stand. R5005, sealed gates, red-team adjudication queue untouched.

## 7. Verdict: KILL

The bar's certification clause fails at kill grade on primary-source evidence: the 'pour que' discriminator's positive set is not {condition, mesure}. Littré certifies {mesure, disposition, précaution} (Tier B) and does not certify bare "condition pour que" at all. The discriminator is NOT formalizable as exhausted in the bar's terms — it was misformalized. No future battery should re-run the {condition, mesure} formalization; any future discriminator work must use the corrected set.

## 8. Consequence notes for the supervisor (not mandated follow-ups; kill verdicts need none)

1. The noun-43 exhaustion argument is thinner than stated: Littré attests bare "par précaution" ("Je m'étais purgée par précaution", Dancourt), so précaution's only battery-grade killer is @21, not par-43. The noun-43 null verdict itself is not contradicted (@21 still kills every monovalent noun), but a future par-43 re-examination should not claim précaution dies on the par arm.
2. Worker correction for the record: "43→00" is 3x stream-wide (@244, @1126, @1544), not once as noun-43 §3 stated; only @1544 has the "00-46" tail.
3. Suggested (not mandated) follow-up the supervisor may queue: `pour-que-set-rerun` — re-run the discriminator's downstream consequences with the corrected positive set {mesure, disposition, précaution} (all three still die at @21, so this is a formalization repair, not a re-opening).
