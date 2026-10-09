# Battery verdict: domaine-kill-harden

- Target: `domaine-kill-harden` (battery-queue.json, priority 4, status queued)
- Claim: Harden val-62-ne-noun C1's 'domaient' elimination with a dictionary check (Littré): confirm no verb 'domaier'/'domainer' attested in 19th-c. French.
- Parent: `battery-val-62-ne-noun.md` (verdict NULL overall; C1 eliminated domaine at kill grade)

## Bar (verbatim, numbered)

From the queue entry's `bars` field:

1. C1. Dictionary confirms the gap (kill stands), or attestation revives 'domaine'.
2. C2. Source the dictionary entry verbatim in the report.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/domaine-kill-harden.lock` on start (agent 214409a6-2169-44fd-a1d3-4ca55354eab1, 2026-10-09T20:49:49Z); deleted on completion.
2. Re-derived the repaired stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` via `repair_parse.py` (load_rows + repaired_offsets): 1,847 pairs, 96 types. Asserts held (n=1847, types=96). `canonical.py` never used.
3. Adopted (not re-litigated) the parent's window-level attachment logic; independently re-verified the two "62 06" loci on the re-derived stream.
4. Dictionary check: Littré (Émile Littré, Dictionnaire de la langue française, 1863–1873; electronic edition littre.org) headword searches for "domaier"/"domainer"; web searches for French-verb attestations; full-text grep of the lane's 1841 corpus (`code/side-period/corpus/`, 98 .txt files) for "domaient"/"domaier"/"domainer".

## Findings — stream facts (re-verified in-session)

- "62 06" occurs exactly **2×** stream-wide:
  - @665 (rows a4_02..a5_00): `80 03 [62] [06] 00 20` — right neighbor 00='pour' (granted whole word)
  - @1536 (rows a8_00..a8_00): `73 41 [62] [06] 21 62` — left is 41 (no prefix candidate), right is 21 (word-level noun)
- Attachment (adopted from parent): 06 cannot stand alone ("ent" is not a French word); at both windows 06 cannot attach rightward (00='pour' and 21 are whole words); therefore 06 attaches leftward, forming the morphological word "[62]ent".
- Under 62="domain-", the forced word would be **\*"domaient"** — the 3pl present of a verb \*"domaier"/\*"domainer". The rival "dominer" gives "dominent" (different stem), not a rescue.

## Findings — dictionary check

- **Littré has no headword "DOMAIER" or "DOMAINER".** A site-scoped search of littre.org for "domaier" returned zero matching headwords (results were only unrelated entries: major, dôme, dosage, mémoire, dualisme, notaire, démagogue, final, majuscule).
- **Littré's "domaine" entry is noun-only.** Verbatim headword (Littré, littre.org):
  > ## « domaine », définition dans le dictionnaire Littré
  > *(do-mè-n')* **s. m. (substantif masculin)**
  No verb sense is listed for "domaine"; no denominative verb exists in the entry.
- **The only French verb in the dom- family is "dominer".** Verbatim headword (Littré, littre.org):
  > ## « dominer », définition dans le dictionnaire Littré
  > *(do-mi-né)* **v. n. (verbe neutre, notion grammaticale désuete)**
  "dominer" conjugates "dominent" — a different stem, irrelevant to "[62]ent" with the "n-e" content of 62.
- **"Domaier" on the open web is a German surname**, not a French verb. The only French-language hits are surname genealogy pages: "Domaier" is "une variante du nom allemand « Domäier » ou « Domeier »" (igenea.com / igenea.net).
- **"Domainer" in French lexica does not exist as a verb.** The only "domainer" entry found is English Wiktionary's English noun "domainer" ("An individual or company that engages in the buying, selling, marketing, monetization and publishing of Internet domain names") — not French, not a verb, modern English.
- **Corpus attestation check:** grep of the lane's 1841 corpus (59,197,733 characters across 98 files) for "domaient", "domaier", and "domainer": **0 hits**. (The 170-byte HTTP-500 stub file `revue-deux-mondes-1840-q1.txt` is excluded from lane censuses per standing note; its absence cannot contribute a hit.)
- No attestation of \*"domaient" found anywhere: no dictionary entry, no web attestation, no corpus attestation.

## Per-clause pass/fail

- C1 — Dictionary confirms the gap (kill stands): **PASS**. Littré lists no verb "domaier"/"domainer"; "domaine" is noun-only; corpus attestation is zero. No attestation revives 'domaine'.
- C2 — Source the dictionary entry verbatim in the report: **PASS**. Littré DOMAINE and DOMINER headword lines quoted verbatim above (Littré 1863–1873 is public domain; sources: https://www.littre.org/definition/domaine and https://www.littre.org/definition/dominer).

Adverses: none listed in the queue entry.

## Verdict: PROMOTE

Both bar clauses pass; no adverses. The dictionary check hardens val-62-ne-noun C1: the \*"domaient" elimination stands on a documented lexical gap, not an assumption.

## Scope

- This battery hardens only the **'domaient' elimination** (val-62-ne-noun C1). It does not name any value for 62, does not decide règne/trône, and does not touch Window A's re-prefix caveat (queued target `re-prefix-03-665` — not duplicated).
- Untouched: 62's open global value/class, the red-team docket items, §7. No standing or red-team verdict contradicted, downgraded, or re-litigated. Canonical-stream caveat stands (rows a4_02/a5_00 and a8_00 offsets unvalidated).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-domaine-kill-harden.md`
- Queue: `domaine-kill-harden` queued → `verdict`/`promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.domaine-kill-harden.tmp` + atomic rename, no leftover; disk re-validated; own entry only; no downgrade)
- Lock `locks/domaine-kill-harden.lock`: created on start, deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
