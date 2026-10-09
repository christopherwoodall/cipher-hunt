# Battery report: verb56-register-closeout

- Target id: `verb56-register-closeout`
- Claim: "xeent-register-tiebreak has landed: close out the register venue (greer/degreer nautical vs maugreer familiar vs diplomatic register) and check whether the valency tie survives"
- Date: 2026-10-09
- Worker: battery worker (subagent f39c9ac7-01cd-4cdb-a56f-7826934e1317)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). Verified in-session: 1,847 pairs, 96 types, n(56) = 23. `canonical.py` never touched. R5005, sealed gates, red-team queue untouched.

## Bar (verbatim, pre-registered)

"resolve iff the register axis kills survivors at register grade in 1841 diplomatic French; state whether the valency tie survives"

Numbered clauses (frozen before testing, not modified after):

1. C1 — the register axis kills one or more of the 8 surviving Xeent candidates at register grade in 1841 diplomatic French.
2. C2 — the report states whether the valency tie survives (and in what membership).

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/verb56-register-closeout.lock` on start; deleted on completion.
2. Adopted as premises (not re-litigated): xeent-register-tiebreak's closed 9-verb inventory, its Littré register table, its réer kill, and its fenced 8-way tie; valency-56-wide's valency fence over the nine. No duplication of either bar.
3. Byte-confirmed the three 56 windows on the repaired stream (0-based): @795 [a5_04] = `64 56 37`; @1626 [a8_03] = `66 67 33 46 56 69 26 00 33`; @1745 [a8_08] = `34 94 82 46 56 40 06 65 34`. Match the tiebreak's frames exactly.
4. Ran one NEW register-grade test the tiebreak did not run: a genre-level corpus check for "Terme de marine" verb forms in the diplomatic correspondence/memoir subset of `code/side-period/corpus/` (32M chars), with word-boundary disambiguation and English/noise filtering.

## Findings

### Survivor set under test (8, after réer's register kill)

| Candidate | Littré register mark | Corpus 3pl -éent (tiebreak) |
|---|---|---|
| créer | none | attested (9-10) |
| agréer | none | attested (1) |
| suppléer | none | attested (5) |
| recréer | none | 0 (sole hit was récréer, a different verb) |
| gréer | Terme de marine | 0 |
| dégréer | Terme de marine | 0 |
| procréer | none | 0 |
| maugréer | none (v.n.; "fam." premise unsupported) | 0 |

### New genre-level corpus evidence

Whole-word French marine-verb forms (`grée/grèent`, `dégrée/dégréent`) across the full 32M-char corpus: **zero genuine hits**. Raw hits in the diplomatic subset were all false positives: `levant-correspondence-1841-p3.txt` is an ENGLISH text ("Her Majesty's Government", "to the degree of again revolting" — English "degree"/"ree"); the Guizot t5-t6 "degree" hits are English OCR ("a certain degree"). Nesselrode-v9's "ree" and the Guizot/t3 "gree" hits are English fragments or agree-stems.

Reading: absence of nautical vocabulary from memoirs and correspondence that discuss no naval operations is topic-absence, not genre-exclusion. It does not reach kill grade for gréer/dégréer. "Terme de marine" is a domain mark, not a register-exclusion mark: the diplomatic genre admits technical vocabulary when the topic demands it. Only a provably non-naval letter topic would convert the strain to a kill — and that topic determination is the queued `nautical-56-topic` follow-up's venue, not this battery's.

### Per-candidate register-grade assessment

- créer / agréer / suppléer: no mark, corpus-attested. No kill.
- recréer: no mark; 0-corpus confounded by récréer. Weak signal, not kill grade. No kill.
- procréer: no mark; 0-corpus is weak signal, not kill grade (same standard the tiebreak applied). No kill.
- gréer / dégréer: "Terme de marine" domain mark stands; genre check does not exclude marine vocabulary from diplomatic French at kill grade; letter topic still open. Strain stands, kill withheld (no duplication of the tiebreak's graded outcome).
- maugréer: Littré carries no "fam." mark — the claim's "familiar" characterization stays unsupported by the bar's named authority. TLFi's "vx/littér." scoping (per valency-56-wide) attaches to the transitive arm ("maudire quelqu'un"), not to the verb as such, and the diplomatic register of 1841 is formal/literary-leaning — no register-grade kill. Kill withheld.

## Per-clause results

- C1: FAIL — no survivor is register-incompatible with 1841 diplomatic French at kill grade. The register axis exhausts its discriminating power at réer.
- C2: ANSWERED — the valency tie survives. Valency-56-wide fenced all nine on identical transitive valency profiles; réer's register kill removes it from the tie, leaving an **8-way valency tie** (créer, agréer, suppléer, recréer, gréer, dégréer, procréer, maugréer) with the tie's logic intact.

## Verdict: NULL (venue closed, tie standing)

The register venue is closed out: its full yield is one kill (réer) and a fenced 8-way tie. No register-grade kill is available against any survivor in 1841 diplomatic French. The valency tie survives as the 8-way set. No standing/red-team verdict contradicted; §7 intact.

## Adverses answered

- "do not duplicate xeent-register-tiebreak's bar; close the venue" — answered: the tiebreak's C1/C2/C3 outcomes were adopted as premises, not re-run; this battery added only the new genre-level corpus check and the closeout grading, then fenced the venue.

## Follow-ups proposed (nulls regenerate work; none duplicate queued follow-ups)

1. `marine-register-genre-deep` (P4) — deepen this battery's genre check: partition the diplomatic correspondence subset by topic and test whether "Terme de marine" vocabulary (broadened: gréement, agrès, vaisseau, frégate) occurs in naval-topic diplomatic letters. Confirms or weakens the domain-mark compatibility premise at genre grade; gates the queued `nautical-56-topic` kill.
2. `maugreer-fam-premise-trace` (P4) — trace the origin of the "maugréer familiar" premise (Académie 1835/1878, TLFi, Robert register marks) and close the premise-correction loop the tiebreak opened.
3. `transitive-arm-register-maugreer` (P4) — test whether TLFi's "vx/littér." scoping of maugréer's transitive arm ("maudire quelqu'un") makes that arm register-incompatible with 1841 diplomatic French at @795's "qui [56] [37]" object frame. If it dies, maugréer falls back to its v.n. arm, which the queued `valency-maugreer-56` battery then adjudicates.

## Bookkeeping

- Queue: `verb56-register-closeout` → `verdict`/`null`, 2026-10-09 (temp-file + rename; pre-write assert passed — was queued/verdictless; JSON re-validated; own entry only).
- Lock created on start, deleted on completion (verified gone). `canonical.py` never used; R5005, sealed gates, red-team queue untouched.
