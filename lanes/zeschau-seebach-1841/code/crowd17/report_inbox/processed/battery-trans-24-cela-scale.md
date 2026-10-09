# Battery verdict: trans-24-cela-scale

- Target: `trans-24-cela-scale` (battery-queue.json, priority 4, status queued)
- Claim: Gather-only census: "V + cela" across all conjugated forms of 24's narrowed rivals (savoir/vouloir) as standing corpus evidence for the 24-value docket.
- Parent: worker-proposed follow-up from `battery-trans-24-ce-corpus` KILL (2026-10-09). That battery found ZERO genuine bare "savoir/vouloir + ce" (bare pronoun DO) in 61M chars but 22 attestations of bare "V + cela" as the positive control (the grammatical bare-demonstrative-DO alternative). This battery scales up the positive control across all conjugated forms.

## Bar (verbatim, pre-registered)

> census of bare "savoir/vouloir + cela" hits in the 1841 corpus, classified by verb form; no pass/fail bar, feeds the 24-value docket

Restated as gather-complete clauses before testing:

- **G1 (gather):** census of bare "savoir/vouloir + cela" hits collected across all major conjugated forms of both verbs in the 1841 corpus → the census IS the deliverable; no pass/fail bar.
- **G2 (classification):** every hit hand-classified by verb form, with non-evidence (OCR misreads, determiner/relative readings) fenced out.
- **G3 (contradiction check):** if a kill-grade finding emerges (e.g. a contradiction with a standing red-team verdict), escalate instead of filing a gather verdict.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/trans-24-cela-scale.lock` on start (agent cd1cba00-62f5-4748-86bc-407ee091b2cf, 2026-10-09T21:21:29Z); no fresh lock existed; deleted on completion.
2. Corpus: `code/side-period/corpus/`, 97 text files, 61,067,439 chars (the 170-byte HTTP-500 stub `revue-deux-mondes-1840-q1.txt` excluded; the same corpus as the parent battery).
3. Grep, case-insensitive, `\b<FORM>\s+cela\b`, FORMS = savoir: sais, sait, savons, savez, savent, savais, savait, savions, saviez, savaient, saurai, sauras, saura, saurons, saurez, sauront, saurais, saurait, saurions, sauriez, sauraient, sache, saches, sachons, sachiez, sachent, sachant, su, sue, sus, sut; vouloir: veux, veut, voulons, voulez, veulent, voulais, voulait, voulions, vouliez, voulaient, voudrai, voudras, voudra, voudrons, voudrez, voudront, voudrais, voudrait, voudrions, voudriez, voudraient, veuille, veuilles, veuillions, veuilliez, veuillent, voulu, voulue, voulus, voulues, voulant, voulut; plus infinitives savoir/vouloir as a separate classification class. Every hit hand-read in context; archaic spellings (sçavoir, sçait, savoist, veult, vouloit) swept as a control: 0 hits.
4. Did NOT use `canonical.py`, the repaired stream, or R5005 (corpus battery, per brief). Did not touch sealed gate instances or the red-team adjudication queue.

## Findings: the classified census

**Total genuine bare "V + cela" attestations: 25.** All 25 are genuine bare demonstrative direct objects after the verb. Zero OCR misreads, zero determiner/relative contaminations, zero non-DO readings. (Contrast the parent's 416 "V + ce" tokens, 95% of which were licensed relative frames.)

### SAVOIR — 24 hits (21 finite + 3 infinitive)

Present indicative (12): sais ×3 ("Tu sais cela, souviens-toi", vigny-chatterton-1835:2581; "Oui, oui, je sais cela", musset-lorenzaccio:1447; "Oui, oui, je sais cela", musset-comedies-proverbes-1850:7637); sait ×4 ("Tout le monde sait cela ici", revue-deux-mondes-1841-q3:42430; "Lord Clinton sait cela sur le bout du doigt", hugo-marie-tudor:21; "Thiers sait cela.", chateaubriand-outre-tombe-t5:10738; "Qui sait cela?", chateaubriand-outre-tombe-t2:11483); savez ×2 ("Vous savez cela aussi bien que moi.", nesselrode-v8:248; "vous savez cela et vous le direz à merveille", chateaubriand-outre-tombe-t4:16839); savent ×3 ("Ah! les pères savent cela, mais non les enfants.", musset-lorenzaccio:1342; "Ah! les pères savent cela, mais non les enfants.", musset-comedies-proverbes-1850:7337; "les vieux seigneurs, messieurs, savent cela", hugo-roi-samuse:406).

Imperfect (2): savait ×1 ("Voltaire savait cela.", revue-deux-mondes-1841-q1:10853); savions ×1 ("Si nous savions cela, nous saurions tout.", revue-deux-mondes-1841-q4:30859).

Future (2): sauras ×2 ("tu sauras cela!", musset-lorenzaccio:1697; "que m'importe? tu sauras cela?", musset-comedies-proverbes-1850:8649).

Subjunctive present (2): sache ×2 ("Il faut que je sache cela, entends-tu?", musset-lorenzaccio:636; "Il faut que je sache cela, entends-tu?", musset-comedies-proverbes-1850:5286).

Past participle (3): su ×3 ("si j'avais su cela plus tôt!", musset-comedies-proverbes-1850:22173; "C'est ce soir seulement que j'ai su cela", dumas-tour-de-nesle:2308; "Tu as su cela?" (OCR "lu as su cela"), dumas-mariage-louis-xv-1841:1984).

Infinitive (3): savoir ×3 ("Je suis bien aise de savoir cela.", vigny-chatterton-1835:3842; "Tu dois savoir cela, toi qui sais tout", hugo-ruy-blas:5349; "Je n'ai nul besoin de savoir cela.", revue-deux-mondes-1840-q3:34118).

Savoir forms with ZERO bare-cela attestations at scale: savais, saviez, saura, saurai, saurons, saurez, sauront, saurait(s)/saurions/sauriez/sauraient, saches, sachons, sachiez, sachent, sachant, sue, sus, sut/sût. (Expected — low-frequency forms; not a gap.)

### VOULOIR — 1 hit

Present indicative (1): veux ×1 ("Je veux cela.", hugo-marie-tudor:410). Infinitive "vouloir cela": 0. All other vouloir forms: 0.

### Distributional note (not a verdict, feeds the docket)

The positive control is strongly savoir-skewed: 24/25 hits are savoir, 1/25 vouloir. When 1841 French puts a bare demonstrative DO after these two rivals, it is overwhelmingly after savoir. This does not adjudicate between savoir/vouloir as 24's value — vouloir's corpus absence of bare "cela" may be stylistic (vouloir prefers infinitive/nominal complements) — but it is standing corpus evidence the 24-value docket can cite: "ne [24] cela" / "[24] cela" resegmentation at @163/@830 is grammatical under savoir at scale, under vouloir only once.

## Verdict: NULL (gather-complete)

G1/G2 discharged: 25-attestation census collected and hand-classified, no contradictions with standing or red-team verdicts (G3 not triggered). This is the standing corpus evidence for the 24-value docket: bare "V + cela" is the grammatical bare-demonstrative-DO after savoir/vouloir, attested 25/25 genuine, vs ZERO genuine bare "V + ce" (parent battery). The evidence context for follow-up `cela-87-11-reseg` (87+11 = "cela" composition at @163/@830) is now scaled: 25 hits support "ne [24] cela" / "[24] cela" under savoir/vouloir as grammatical.

## Follow-ups proposed (all verified ABSENT from battery-queue.json, left for supervisor)

1. `vouloir-cela-gap` (P4, gather-only) — bar: census of "vouloir + cela/ceci/ça" with intervening material ("vouloir bien cela", "vouloir vraiment cela", negations "ne pas vouloir cela") in the 1841 corpus, classified; determines whether vouloir's bare-cela gap (1/25 here) is a bare-DO gap or a lexical/style gap; feeds the 24-value docket. Claim: the 1/25 vouloir share is a bare-DO gap, not a style gap.
2. `cela-subject-scope` (P4, gather-only) — bar: census of "cela" as SUBJECT of savoir/vouloir ("cela se sait", "cela se veut"?) in the 1841 corpus; closes the subject/object alternation question for the 24-value docket in case 24 resolves as something other than finite-verb DO-taker. Claim: "cela se sait" attested, "cela se veut" unattested (register asymmetry).
3. `trans-24-cela-window` (P4, gather-only) — bar: re-examine 24's 52 stream windows for any "24 + [value with bare-demonstrative-DO]" signature consistent with the 25-hit census (e.g. 24 followed by a DO-class value); a corpus-backed cross-check feeding the 24-value docket. Claim: at least one 24 window has a bare-DO-class follower.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-trans-24-cela-scale.md`
- Queue: `trans-24-cela-scale` → `status: verdict`, `result: null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.trans-24-cela-scale.tmp` + atomic rename; disk re-validated; own entry only; no downgrade; no tmp leftover).
- Lock created 2026-10-09T21:21:29Z (no fresh lock), deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched. canonical.py never used.
