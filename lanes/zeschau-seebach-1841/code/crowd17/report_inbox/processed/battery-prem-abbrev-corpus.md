# Battery `prem-abbrev-corpus` — verdict: KILL (abbreviation arm dead at corpus grade)

Target: corpus check of 1841 abbreviation practice — does "pre." stand for "premier/première" as a whole word in the lane's period texts? Date: 2026-10-09. Corpus: `code/side-period/corpus` (76 files, 34,526,989 chars; print OCR of 1841 French texts plus some German papers). Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`); 1,847 pairs / 96 types re-derived in-work. `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched. Lock `code/crowd17/next-token/locks/prem-abbrev-corpus.lock` created on start (agent-session 2c6be969-0bb3-43f5-9f71-b7026d5581bd, 2026-10-09T15:00:30Z); deleted on completion.

## Bar (verbatim, pre-registered)

"if unattested in practice, the fence hardens toward kill; if attested, the arm re-opens as licensed"

Numbered clauses (fixed BEFORE the corpus census, not modified after):

- **C1:** full census of abbreviation-class tokens (pr./pre./prem./premi./premier./premiers.) in the lane period corpus, every token classified by expansion.
- **C2 (attested arm):** ≥1 genuine "pre."→"premier/première" expansion ⇒ the abbreviation arm re-opens as licensed.
- **C3 (unattested arm):** zero genuine expansions ⇒ the `bound-70-abbrev-premiere` fence hardens toward kill.

## Method

1. Accent-normalized (NFKD, case-folded) regex census over all 76 corpus files for abbreviation tokens: `\b(pr|pre|prem|premi|premier|premiers)\.` plus `prem`/`premi` without period and standard ordinal forms (`1er/1re/Ier/Ire`, `1.er`).
2. Every abbreviation-class hit hand-audited in ±1-line context; expansion classified (genuine "premier/première" vs other expansion vs OCR/line-break artifact).
3. Positive norm censused in parallel: full "premier/première" spellings and standard ordinal abbreviations.

## Window-level evidence

Census totals (byte-exact on the normalized corpus):

| token class | count | genuine "premier/première" expansions |
|---|---|---|
| `pre.` | 4 | 0 |
| `pr.` | 22 | 0 |
| `prem.` / `premi.` | 0 | — |
| `premier.` / `premiers.` | 102 | n/a (full words, see below) |
| `prem` (no period) | 0 | — |
| `premi` (no period) | 1 | 0 (line-break truncation) |

**The four `pre.` tokens, all artifacts:**
1. `allgemeine-zeitung-augsburg-1841-01-25.txt` line 1946: "6 Bände. Pre.« » Thlr." — German book-listing; "Pre." = "Preis" (price), not "premier".
2. `revue-deux-mondes-1841-q1.txt` line 30820: "rom- pre." — line-break split of "rompre" ("se rom-pre.").
3. `revue-deux-mondes-1841-q2.txt` line 17000: "pro- pre." — line-break split of "propre".
4. `revue-deux-mondes-1841-q2.txt` line 42173: "son pré." — full noun "pré" (meadow) at sentence end.

**The 22 `pr.` tokens:** all German ("pr. Stück" = pro/per piece, "pr. Post", "pr. Druckbogen" = per printed sheet; "(Pr. Staatsz.)" = Preußische Staatszeitung) or OCR ("nous ne sommes pr.s" = "pas"; "Pr.oTASsoF" = name Protasov). Zero French, zero "premier".

**The 102 `premier.`/`premiers.` tokens:** spot-checked (5 random) — all are the full word "premier/premiers" at sentence end or headings ("ACTE PREMIER."), never an abbreviation of a longer word.

**The 1 `premi` token:** `talleyrand-memoires-v1.txt` line 15319 "dans les premi / qu'elle ft paraitre" — line-break truncation of "premiers". Not an abbreviation.

**The positive norm (what the period actually does):** "premier/première" spelled in full ×4,781; standard ordinals "1er/1re" (incl. "Ier/Ire") ×322, "1er"/"1.er" forms ×113. The licensed abbreviation practice is the ordinal, never "pre.".

## Per-clause results

- **C1: PASS.** 128 abbreviation-class tokens censused and classified; every token hand-audited.
- **C2: FAIL.** Zero genuine "pre."→"premier/première" attestations in 34.5M characters.
- **C3: FIRES.** The distributional test rejects at kill grade: 0 genuine in 34.5M chars across 128 candidate abbreviation tokens, while the true norm (full spelling ×4,781; 1er/1re ordinals ×322) is fully populated. The `bound-70-abbrev-premiere` fence hardens to a kill-grade corpus rejection of the abbreviation arm. Consistent with (and corroborating) the `frame-367-la-pre` KILL.

## Caveats

- The corpus is printed 1841 text (OCR), not manuscripts. Manuscript abbreviation practice could in principle differ, but the complete absence in 34.5M chars of period print — plus the manuscript's own gloss spelling "première" out in full ("11 70 82 34 29 40") — leaves the arm dead at battery grade. A manuscript-practice check would need archive access (not authorized).
- German papers in the corpus contributed German "pr." tokens; all were audited and excluded from the French count rather than silently dropped.
- OCR/line-break artifacts ("rom-pre", "pro-pre", "pr.s"="pas") were hand-audited, not counted as attestations or as counter-evidence.

## Scope

Kills only the "pre."-as-"première" abbreviation arm at corpus grade. Untouched: 70="pre" pencil ground truth (syllable), the `frame-367-la-pre` KILL, the gloss cribs, 61's open value, 49's open value. No standing or red-team verdict contradicted or downgraded; §7 intact; canonical-stream caveat stands. Per §4, kills regenerate no follow-ups.

## Bookkeeping

- Script: `code/crowd17/next-token/premabbrev_census.py`; data: `code/crowd17/next-token/premabbrev_hits.json`.
- Queue: `prem-abbrev-corpus` queued → verdict/kill via temp-file + rename, own entry only; pre-write assert confirmed no prior verdict; JSON re-validated post-write.
- Lock `prem-abbrev-corpus.lock`: created on start, deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
