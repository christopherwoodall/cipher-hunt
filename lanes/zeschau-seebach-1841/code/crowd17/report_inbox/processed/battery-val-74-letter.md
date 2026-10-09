# Battery verdict: val-74-letter

- Target: `val-74-letter` (battery-queue.json, priority 3, status queued)
- Claim: "Test 74 as a letter cell: the '74 74' doubling kill is scoped to whole-word 74; a letter reading (doubled 'ss'/'ll'-type) would dissolve the kill."
- Bar (verbatim, pre-registered): "Name the letter with byte evidence (collocation profile a la 40='e') or fence letter-74."

**Restated as numbered pass/fail clauses (frozen before testing):**
1. **C1 (name):** name 74's letter value with byte evidence (collocation profile à la 40='e').
2. **C2 (fence arm):** if C1 cannot be met, fence letter-74 with stated cause.

## Verdict: NULL (fence executed)

C1 FAIL / C2 FIRES.

## Method

1. Read BATTERY-PROTOCOL.md in full before testing. Created `locks/val-74-letter.lock` on start (agent 52e96c4a-8c7b-472d-8122-55aca004ac1a, 2026-10-09T20:39:08Z); deleted on completion.
2. Re-derived the repaired stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` via `repair_parse.py`: 1,847 pairs, 96 types; asserts held. `canonical.py` never used.
3. Byte-confirmed all 34 of 74's windows (offsets below). Tested every candidate letter against value-fixed neighbors; checked letter-diagnostic bigrams; compared collocation profiles with banked letters.
4. Adopted (not re-litigated): 94='ne' STRONG LEAD (R17-001); 84='on' (A15); 87='ce' (granted, A4); 77='le' (provisional); 46='que' (pencil GT); 40='e' (pencil GT); 48='e' (promoted); 29='er' (pencil GT); 34='i' (pencil GT); 45='ce' (granted, A4); 67 et/veut polyvalence (§7 intact); split-74-redteam-input package (5 verb-forced / 2 noun-forced windows); unit-49-74-74 KILL (letter-tier 74 at the four "49 74 74" chains dead); noun-74-census / noun-74-formula (whole-word 74 killed by the '74 74' ×6 doubling: "no noun, verb, adjective, pronoun, adverb, or determiner doubles adjacently in French"); val-49-74-frame NULL/fence (this battery is its follow-up #1); val-74-212 NULL (letter arm failed at @212).

## Findings

### C1 — naming: FAIL

- **Collocation profile (à la 40='e'):** 74's 34 windows show 20 distinct predecessors / 19 distinct followers — a free-word scatter, identical in shape to the banked letters (29: 26/18 over 45; 82: 18/16 over 39; 34: 9/9 over 11; 40: 11/14 over 21). The scatter marks 74 a free word-level cell (adopted: inf-37-78-475) and gives **zero letter-selective legs** — no letter candidate is picked by the profile. Per the val-03-value-census precedent, profile-compatibility is not naming.
- **Letter-diagnostic bigrams (byte-exact):** "74 29" ×0 (74 never precedes 'er'), "74 06" ×0 (never precedes 'ent'), "48 74" ×1 = the @862 doubling window, "29 74" ×1 = the @1053 doubling window. A letter cell would routinely close "-er"/"-ent" formations; 74 never does. Zero positive letter evidence.
- **The only naming route in the record is dead:** unit-49-74-74's exhaustive word-formation test named the sole contact-compatible family — 49='ce' (via "49 64=qui" ×2) + 74='t'/'l'/'s' = "cette"/"celle"/"cesse" — and KILLed it: "cette que" (W1), "cette ce" (W2), "celle que"/"cesse que" (W1–W3) are syntactically impossible at kill grade. No other (49, 74) pairing yields a French word (49's word-tier values are all killed/fenced; letter-49 + letter-74 has zero selective legs — open neighbors). No letter is nameable with byte evidence.

### C2 — fence: FIRES (per-window, byte-exact)

- **Uniform letter-74 — kill-grade dead at 4 windows:** 'ne [74]' @350 ("94 74 67 78"), @786 ("94 74 65 84"), @1103 ("94 74 47 78") — 94='ne' STRONG LEAD standalone negator licenses a finite verb only; a letter cannot host finiteness. 'on [74]' @261 ("84 74 45 93") — 84='on' subject pronoun requires a finite verb; same kill. (Adopted: split-74-redteam-input Arm A, battery grade.)
- **Letter-74 at the four "49 74 74" chains — killed:** unit-49-74-74 KILL stands (syntactic impossibility at W1–W3). The doubling dissolution does not rescue anything — the letter hypothesis dies on French grammar, not on the doubling.
- **Letter-74 at @1053–1054 ("29 74 74 45") — fenced:** "29 74 74" = 'er'+"LL" cannot close (no French word ends in a doubled consonant — adopted unit-49-74-74 Step 1) and cannot extend rightward into 45='ce' (granted standalone word) without an ungranted §7 composition.
- **Letter-74 at @1637–1638 ("87 74 74 35") — fenced:** composition "ce"+"74"+"74" needs ungranted §7 with granted 87='ce'; also contradicts the battery-grade "ce [74]" noun-force at @1637 unless a conditioned split is declared (red-team venue).
- **All remaining 26 windows — fenced, no positive leg:** a letter reading strands a non-word between value-fixed standalone words (e.g. @1307 "77(le) L [52]" — 77='le' is a complete standalone word; @1635 "01 L 87(ce)" — 87='ce' granted standalone; @1414 "69 L 34(i)" — needs three-cell §7 composition; @635 "63 L 46(que)" — 46='que' granted standalone). Adopted: val-74-212's letter-arm failure at @212.

The only rescue for any locus is a conditioned split (letter-tier at some windows, word-tier elsewhere) — a §7 red-team act per the battery protocol; this battery declares none.

## Scope

- Fences letter-tier 74 at all 34 windows (kill-grade at the 8 named above; evidentiary elsewhere). No letter value named.
- Untouched: the 74 verb/noun split package (split-74-redteam-input), unit-49-74-74 KILL, noun-74-census/formula fences, 74's open global value/class, §7 (intact), all standing and red-team verdicts. No verdict contradicted, downgraded, or re-litigated. Canonical-stream caveat stands (row offsets unvalidated).

## Follow-ups (for supervisor queuing; all verified ABSENT from queue)

1. `letter-74-split-package` (P4, gather-only) — package the locus-by-locus letter-74 results (kill-grade at the four chains + @350/@786/@1103/@261; fenced elsewhere) as §7 input for the split-74-redteam docket.
2. `seg-69-74-34-1414` (P4) — test @1414 "69 74 34" for a three-cell letter composition ("69 L i", 34='i' GT) — the only window with a letter-tier fixed neighbor; re-opens letter-74 at one locus iff a real French word composes, else fence letter-74 terminally there.
3. `doub-74-1053-1637-residual` (P4) — close the two non-chain doublings (@1053–1054 "29 74 74 45", @1637–1638 "87 74 74 35") as residuals: test syllable-tier 74 vs word-internal resegmentation arms with stated values.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-74-letter.md`
- Queue: `val-74-letter` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.val-74-letter.tmp` + atomic rename; disk re-validated; own entry only; no downgrade; no tmp leftover)
- Lock `locks/val-74-letter.lock`: created 2026-10-09T20:39:08Z (no stale lock), deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
