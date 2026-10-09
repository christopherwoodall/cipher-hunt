# Battery report: xeent-register-tiebreak

- Target id: `xeent-register-tiebreak`
- Claim: "Littre/register tiebreak on the Xeent set in 1841 diplomatic French (greer/degrer nautical, maugreer familiar); verify candidate-set exhaustiveness (procreer, maugreer, degrer, reer) before any naming."
- Date: 2026-10-09
- Worker: battery worker (subagent 9f223563-84d3-4626-9739-889c32d6a747)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). Verified in-session: 1,847 pairs, 96 types. `canonical.py` never touched. R5005, sealed gates, red-team queue untouched.
- Parent: follow-up of the NULL `name-56-verb` (2026-10-09), whose C1 (valency discrimination among {créer, agréer, suppléer, recréer, gréer}) failed. This battery tests the REGISTER axis, not valency. Sibling `valency-56-wide` (running) owns valency; no duplication.

## Bar (verbatim, pre-registered)

"Littre/register tiebreak on the Xeent set in 1841 diplomatic French (greer/degrer nautical, maugreer familiar); verify candidate-set exhaustiveness (procreer, maugreer, degrer, reer) before any naming."

Numbered clauses (frozen before testing, not modified after):

1. C1 — enumerate the Xéent candidates with register evidence from Littré / 1841 corpus.
2. C2 — kill candidates whose register is incompatible with diplomatic French at kill grade.
3. C3 — else fence the tie with stated cause.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/xeent-register-tiebreak.lock` on start; deleted on completion.
2. Fetched Littré entries from littre.org (2026-10-09) for the four un-tested candidates (maugréer, dégréer, procréer, réer); adopted the parent's five fetched entries (créer, agréer, suppléer, recréer, gréer) as premises.
3. Corpus register check: grepped the lane's 19th-century French corpus (`code/side-period/corpus/`, ~32M chars: Allgemeine-Zeitung 1841, Guizot/Talleyrand/Nesselrode/Metternich/Pozzo correspondence and memoirs, RDM 1841, drama, comedy) for every 3pl -éent form, with substring-vs-word disambiguation.
4. Byte-confirmed the three windows on the repaired stream (0-based): @795 = `64 56 37` ("qui [56] [37]", row a5_04); @1626 = `33 46 56 69 26 00 33` (row a8_03); @1745 = `94 82 46 56 40 06 65` ("ne m que [56]e ent [65]", rows a8_07/a8_08).

## Findings

### C1 — candidate enumeration (exhaustiveness verified): PASS

French -éer verbs forming 3pl in -éent constitute a closed class. Full Littré-era inventory: **9 verbs** — agréer, créer, dégréer, gréer, maugréer, procréer, recréer, réer, suppléer. No other -éer verb exists in Littré ("égréer", "déer", "préer", "engréer" are not words). The queue's four to-verify candidates (procréer, maugréer, dégréer, réer) are all real Littré headwords; the set is now closed.

Littré register/valency facts (fetched 2026-10-09, littre.org):

| Candidate | Littré class | Register mark | Gloss |
|---|---|---|---|
| créer | v.a. | none | "Tirer quelque chose du néant"; "ils créent" |
| agréer | v.a. | none | "Recevoir favorablement, trouver bon" |
| suppléer | v.a. | none | "Ajouter ce qui manque, fournir ce qu'il faut de surplus" |
| recréer | v.a. | none | "Créer de nouveau" |
| gréer | v.a. | **Terme de marine** | "Garnir un bâtiment de voiles, poulies, manoeuvres, etc." |
| dégréer | v.a. | **Terme de marine** | "Ôter ou détruire les agrès, les cordages, etc. d'un vaisseau" |
| procréer | v.a. | none | "Engendrer"; usable "Absolument" |
| maugréer | **v.n.** | none | "Témoigner son mauvais gré, son mécontentement en pestant, jurant" |
| réer | **v.n.** | (archaic variant) | "Le même que RAIRE" (to bellow, of deer) |

Corpus 3pl-form counts (32M chars, 19th-c French; substring disambiguated):

| Form | Count | Note |
|---|---|---|
| créent | 9–10 | attested |
| suppléent | 5 | attested |
| agréent | 1 | attested ("Ils agréent chacun dans sa forme", RDM q1) |
| gréent (of gréer) | 0 | the 1 raw hit is "agréent" |
| recréent (of recréer) | 0 | the 1 raw hit is "récréent" = récréer (to amuse), a different verb |
| procréent | 0 | |
| maugréent | 0 | |
| dégréent | 0 | |
| réent (of réer) | 0 | sole raw hit is "réentendre" (infinitive), a false positive |

### C2 — kill-grade register kills

- **réer: KILLED at kill grade.** Three independent legs: (a) Littré: v.n., archaic variant of "raire" = to bellow (of deer) — semantic content is animal vocalization; (b) 0 genuine attestations in 32M chars of 19th-century French; (c) the document is an 1841 diplomatic dispatch (DECODE R5005: De Zeschau to De Seebach, Saxon legation in Russia) — a verb meaning "to bellow like a stag" is semantically impossible as 56's value in this genre. Register+semantic incompatibility with the document genre is forced: no diplomatic context licenses "ils réent".
- gréer / dégréer: NOT killed. "Terme de marine" is compatible with diplomatic correspondence when the topic is naval; the letter's topic is not established at battery grade. Strain noted, kill withheld.
- maugréer: NOT killed on register. **Premise correction:** Littré does NOT mark maugréer "fam." — the queue claim's "familiar" characterization is unsupported by the bar's named authority. Its real Littré fact is v.n. (intransitive), which is a VALENCY fact, not a register fact — handed to `valency-56-wide` (running) and the red team, not graded here (out of this battery's bar).
- procréer: NOT killed. v.a., no register mark; 0/32M corpus is a weak signal, not kill grade.
- créer / agréer / suppléer / recréer: NOT killed. v.a., no register mark, all corpus-attested.

### C3 — fence: FIRES

The tie among the remaining **8** candidates (créer, agréer, suppléer, recréer, gréer, dégréer, procréer, maugréer) is not broken by register at battery grade. Fenced with stated cause.

## Per-clause results

- C1: PASS — 9-candidate set enumerated and closed; Littré + corpus evidence tabled.
- C2: PARTIAL — réer killed at kill grade; no other candidate is register-incompatible at kill grade.
- C3: FIRES — 8-way tie fenced.

## Verdict: NULL (fence executed)

56's verb identity remains underdetermined at battery grade on the register axis. Kill-grade sub-finding: réer is dead (archaic v.n. "raire" = to bellow; 0/32M corpus; semantically impossible in a diplomatic dispatch). Premise correction: maugréer is not marked "fam." in Littré — it is v.n., and its intransitivity is a valency discriminator for `valency-56-wide`, not a register kill here. gréer/dégréer keep their "Terme de marine" strain but are not killed while the letter's topic is open. No standing/red-team verdict contradicted; §7 intact.

## Adverses answered

- "The claim's five-candidate set is not exhaustive: procreer, maugreer, degrer also form 3pl -eent." — closed: full 9-verb inventory verified; all four verified as real Littré headwords; "reer" is real but killed.
- "greer is 'Terme de marine' (Littre) - a register consideration, not a valency discriminator." — confirmed and scoped: register strain noted, kill withheld pending topic determination.

## Follow-ups proposed (nulls regenerate work)

1. `valency-maugreer-56` (P3) — test maugréer's intransitivity (Littré v.n.) against @795's "qui [56] [37]" predicative frame and @1745's frame; kill at valency grade iff "qui maugrée [37-predicative]" is ungrammatical. Coordinate with `valency-56-wide`; do not duplicate its bar.
2. `procreer-56-semantic` (P3) — test procréer ("engendrer") against the three windows' semantic frames; does an "engender" reading parse at @1626/@1745?
3. `nautical-56-topic` (P4) — once the letter's topic is established via decoded neighbor values, re-test gréer/dégréer: a provably non-naval topic converts the "Terme de marine" strain into a register kill.

## Bookkeeping

- Queue: `xeent-register-tiebreak` → `verdict`/`null`, 2026-10-09 (temp-file + rename; pre-write assert passed — was queued/verdictless; JSON re-validated; own entry only).
- Lock created on start, deleted on completion (verified gone). `canonical.py` never used; R5005, sealed gates, red-team queue untouched.
