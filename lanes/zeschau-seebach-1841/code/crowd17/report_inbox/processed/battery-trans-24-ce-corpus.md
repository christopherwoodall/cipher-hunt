# Battery verdict: trans-24-ce-corpus

- Target: `trans-24-ce-corpus` (battery-queue.json, priority 3, status queued)
- Claim: Corpus census: do 24's narrowed rivals ("savoir"/"vouloir") take "ce" as direct object at scale in 1841 French?
- Parent: null-mandated follow-up from `battery-obj-87-closure.md` (verdict NULL, 2026-10-09). That battery fenced @824/@830 as 24-load-bearing: the "[24] ce" closure parse needs ungranted assumption **A1 — 24 is transitive (accepts "ce" as direct object)**. 24's value is narrowed to savoir/vouloir (neither named).

## Bar (verbatim, pre-registered)

> A positive result discharges A1 and re-fires @163/@824/@830 as closure; a zero hardens the fence

Restated as numbered clauses before testing:

- **C1 (positive arm):** >=1 genuine attestation of bare "savoir/vouloir + ce" (ce = standalone demonstrative-pronoun direct object) in the 1841 corpus → A1 discharged, @163/@824/@830 re-fire as closure.
- **C2 (zero arm):** zero genuine attestations at scale (with the corpus shown capable of attesting the grammatical alternative) → the A1-discharge hypothesis is rejected at the lane's standard; the @824/@830 fence hardens.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/trans-24-ce-corpus.lock` on start (agent 42e1b158-22f9-47c6-bc95-ba137b8078c7, 2026-10-09T21:08:00Z); deleted on completion.
2. Re-derived the repaired stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` via `repair_parse.py`: 1,847 pairs, 96 types. Asserts held. `canonical.py` never used.
3. Loci re-confirmed (1-based, as cited): @163 = `52 94 24 87 11` ("[52] ne [24] ce la", row a1_05); @824 = `13 24 87 59` ("[13] [24] ce est", row a5_05); @830 = `1 24 87 11` ("[1] [24] ce la", row a5_06). All three are "24 87" windows: 24 = finite verb class (R17-009, value narrowed savoir/vouloir), 87 = "ce" (granted value; function open).
4. Corpus: `code/side-period/corpus/`, 97 files, 61,067,439 chars (the 170-byte HTTP-500 stub `revue-deux-mondes-1840-q1.txt` excluded). Searched all major conjugated forms of savoir (sait, savent, sais, savez, savons, savais, savait, savaient, saura, saurait, sauront, sut, sût, su, sachant, sache, sachent, savoir) and vouloir (veut, veulent, veux, voulez, voulons, voulais, voulait, voulaient, voudra, voudrait, voudront, voulut, voulût, voulu, voulant, veuille, veuillent, vouloir) followed by bare "ce". Every hit hand-classified by what follows "ce".
5. Did NOT touch R5005, sealed gate instances, or the red-team adjudication queue.

## Findings

**Total "V + ce" tokens: 416.**

- **395 (95%) are the licensed relative frames:** "ce que" / "ce qui" / "ce qu'il/elle/on/ils" / "ce dont" / "ce où" — e.g. "sait ce que", "veut ce que", "savoir ce qui se passe". These are grammatical but irrelevant to A1: "ce" there heads a relative clause, it is not a bare direct object.
- **21 non-relative hits, ALL resolved as non-evidence:**
  - 6 are OCR misreads of the relative frames: "savoir ce (jue c'est" (= "ce que c'est"), "sais ce avi en arrivera" (= "ce qui en arrivera"), "sachant ce (lu'elle voulait" (= "ce qu'elle voulait"), "savoir ce (|ui arrivera" (= "ce qui arrivera"), "sais ce «|ue nous eu pensez" (= "ce que vous en pensez"), "savoir ce (jue c'est que l'Egypte" (= "ce que c'est que l'Egypte").
  - 14 are "ce" as demonstrative DETERMINER + noun, a different syntactic slot: "savons ce matin par dépêche" (= "we learn this morning by dispatch"), "voulait ce matin louer" (= "wanted this morning to rent"), "sais ce soir", "sut ce point", "su ce grand complot", "veut ce Prince / prince", "veux ce mariage", "saura ce secret", "voulut ce fils", "savait ce bonheur". Inapplicable at the loci: @824 has 87 followed by 59 ("est"), @163/@830 by 11 ("la") — no noun for a determiner reading.
  - 1 is "savoir ce à quoi" — a relative construction.
- **Genuine bare-pronoun-DO attestations: 0.**
- **Surface-shape check:** "V + ce + la" (the exact @163/@830 surface): **0 hits** stream-wide in the corpus.
- **Positive control:** "V + cela" (the grammatical bare demonstrative DO): **22 hits** — e.g. "Voltaire savait cela", "Tout le monde sait cela ici", "Vous savez cela aussi bien que moi", "Tu sais cela, souviens-toi". The corpus attests the grammatical alternative, so the zero for bare "V ce" is meaningful, not a corpus gap.

**C1 FAILS. C2 FIRES.** When 1841 French wants a bare demonstrative direct object after savoir/vouloir, it uses "cela" — never bare "ce". The A1-discharge hypothesis is rejected at the lane's distributional standard (0 genuine / 416 tokens, ~61M chars, positive control attested).

## Verdict: KILL (of the A1-discharge hypothesis)

The corpus route to discharging A1 is dead at battery grade: no scale, no residue, no near-miss — 95% of "V ce" tokens are relative frames and the remaining 5% are OCR noise or determiner uses. The @824/@830 fence (24-load-bearing) hardens per the bar. @163's closure parse remains standing only with A1 recorded as ungranted and now corpus-rejected; its "ne [24] ce la" surface has zero corpus precedent ("V ce la" = 0).

## Scope

- Kills only the corpus-discharge route for A1. Does NOT kill "ce = object" readings outright (a "cela"-composition resegmentation at @163/@830, i.e. 87+11 = "cela", is a separate untested route — see follow-up).
- Does NOT name 24's value, does NOT touch 87's class/function, 94's lead, or any standing/red-team verdict. §7 intact. Canonical-stream caveat stands.

## Follow-ups proposed (verified ABSENT from battery-queue.json, left for supervisor)

1. `cela-87-11-reseg` (P4) — test 87+11 = "cela" word composition at @163/@830; "ne [24] cela" / "[24] cela" is grammatical under savoir/vouloir (22 corpus hits) and re-opens the closure parse without A1.
2. `trans-24-cela-scale` (P4, gather-only) — extend the positive control: full census of "V + cela" across all 24-rival verb forms as standing corpus evidence for the 24-value docket.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-trans-24-ce-corpus.md`
- Queue: `trans-24-ce-corpus` → `status: verdict`, `result: kill`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.trans-24-ce-corpus.tmp` + atomic rename; disk re-validated; own entry only; no downgrade; no tmp leftover).
- Lock created 2026-10-09T21:08:00Z (no stale lock), deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
