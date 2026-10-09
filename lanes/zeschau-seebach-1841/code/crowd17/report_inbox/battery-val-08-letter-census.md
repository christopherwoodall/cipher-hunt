# Battery verdict: val-08-letter-census

- Target: `val-08-letter-census` (battery-queue.json, priority 3, status queued at dispatch)
- Claim: census 08's 18 windows for a uniform letter value (lead with 'h'/'f'/'b' from seg-08-ier-61); a named 08 re-opens seg-41-08-leftedge.
- Worker: 7a2deedc-5877-4e56-be89-f3501b09ddc5. Date: 2026-10-09.
- Stream: repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed exactly per `code/side-keyhunt/repair_parse.py`; asserts held in-session: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- All @-offsets are 0-based pair indices in the repaired stream.
- Lock: `code/crowd17/next-token/locks/val-08-letter-census.lock` created on start (agent id + UTC timestamp; no stale lock pre-existed); deleted on completion.

## Bar (verbatim, pre-registered)

"name 08's letter value iff it parses with byte evidence at >=2 windows with zero kill-grade contradictions."

**Restated as numbered pass/fail clauses (frozen before testing):**
1. **C1:** a single uniform letter value for 08 parses with byte evidence (a complete licit French word spelled from standing values + the candidate) at >=2 windows.
2. **C2:** zero kill-grade contradictions for that letter across all 18 windows of 08.
3. **C3:** the listed adverse is answered (adverse: "08's value open (N189)").

Standing values adopted, never re-litigated (protocol §7): pencil GT (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce); provisional (59=est, 77=le); 65 noun-class (R20-047); 62 pronominal; 94=ne STRONG LEAD; 83=de lead; 98=vient lead; 48=e letter-cell. Adopted batteries: `08-letter-geometry` PROMOTE (positional signature: word-initial-letter 5/18, internal junctions 4/18, word-final 1/18, rest open), `stem-08-letter-probe` PROMOTE (08 letter-tier; value set = single letters only), `ce-08-31-frame` PROMOTE ("87 08 31" = "ce"+[08][31]-word, 08 word-initial letter), `08-position-profile` PROMOTE, `on-08-homophony` KILL, `prefix-productivity-08` KILL (prefix-08 parse dead at @1339), `08-leftattach-944-1323` NULL (left-attachment of "40 08" failed; its gated follow-up `08-final-rerun-gated` explicitly re-fires "iff 08's letter value" is named — this battery is that trigger).

## Method

1. Read BATTERY-PROTOCOL.md in full before testing.
2. Re-derived the repaired stream in-session; confirmed n(08)=18 byte-exact with ±3 context per window.
3. Tested the lead candidates 'h'/'f'/'b' (from seg-08-ier-61, where each was a locus-specific arm at @60) for UNIFORMITY across all 18 windows.
4. Tested the emergent candidate 't' (found via the "40 08" junction at @922/@944) the same way.
5. Kill-grade standard: a window kills a candidate iff no grammatical French parse exists for 08=letter there under standing values without inventing words or licenses.

## Findings

### The lead candidates {h, f, b} all fail uniformity at kill grade

- **'h' dies at @60** ("41 08 34 29 40"): the "08 34 29"="hier" arm is kill-grade dead — seg-08-ier-61 C2 proved "hier en ne [92]" ungrammatical ("en" can never precede "ne" in the French clitic order). "hiere"/"hière" is not a French word. As second letter of an onset ("41h-ière"): no French word of the shape onset-h+"ière" exists (h-final onsets are ch/ph/rh/th; "chière"/"phière"/"rhière"/"thière" are not words), regardless of 41's open value. No licit parse remains.
- **'f' dies at @922** ("74 74 40 08 65 71"): "40 08"="ef" is not a French word; "40 08" word-internal continuation is blocked by 65 (noun word-cell, R20-047 — a word cannot continue into a word-level noun cell); "e"+"f"+65 (letter + word cell) is unlicensed; "f" standalone is unlicensed. **'f' dies identically at @944** ("07 50 40 08 62 98"): "ef" not a word; continuation blocked by 62 (pronominal word-cell).
- **'b' dies at @922 and @944** on the identical "eb" reasoning ("eb" is not a French word; same blocks).

### 't' passes: C1 and C2 both fire

- **@922: "40 08" = "e"+"t" = "et"** — a complete, licit French word spelled entirely from GT 'e' + the candidate. Parse: "74 74 | et | 65-N 71 17" = "…et [65-noun]…" — grammatical conjunction + noun. Zero new assumptions beyond 08='t'. (The rival one-word parse "74-74-e-t" = "sommet"/"bonnet"-shaped is also consistent with 08='t'; it needs 74=letter, an extra assumption — the "et" parse is strictly cheaper.)
- **@944: "et [62-pron] [98-vient]"** — "07 50 | et | 62 98" = "…et [pronominal-62] vient…" ("et il vient"-shaped). Grammatical with standing values only. This independently resolves `08-leftattach-944-1323`'s open C2: no left-attachment of "40 08" to "07 50" is needed at all — "et" is already a complete word. That battery's gated follow-up fired on exactly this trigger.
- **C1 PASS:** two independent windows (@922, @944) with full byte evidence, zero new assumptions.
- **C2 PASS — remaining 16 windows, zero kill-grade contradictions:**
  - Word-initial-letter windows (adopted geometry @631/@881/@1488/@1520/@1592): t-initial words are abundant in French ("tout", "tenir", "t[31]"-shapes) — no contradiction.
  - @975 ("ce t [01] pour"), @1302 ("pre [37] t [43]"), @1323 ("[80] t [62] vient"), @35 ("[01] t [91]"), @1610 ("[23] t [55] de"): t-initial or t-final letter positions, all open neighbors — no contradiction.
  - Word-final windows (@198 adopted "[60]t et/veut"; @534 "[16]t [24-V]"; @1339 "[60]t [65] qui"): 't' is among the commonest French word-final letters — no contradiction. (The prefix-08 parse stays dead per its own kill; 't' as final letter of the [60]-word does not revive it.)
  - @60 ("41 t 34 29 40"): "entière" with 41="en" — one non-granted assumption (41's value is open, §7 split candidate), not a contradiction; a third conditional leg.
  - @779 ("37 t 29 89"): "ter[89]" with 89 at open tier — not contradicted (89's tier ungranted, but the parse needs no new license).
  - @98 ("85 t 21 62"): "t" word-initial ("t[21]") or stem+[t] inflection on verb-stem 85 — neither contradicted (the "en [85]" gerund legs are at other windows).
- **C3 PASS:** the adverse (08's value open) is answered by the naming itself.
- **Standing compatibility:** single-letter set (stem-08-letter-probe) ✓ — 't' collides with no standing single-letter value ('m'/'i'/'e'); on-08-homophony KILL unaffected ✓; positional signature (initial/internal/final) — 't' instantiates all three flavors ✓; "08 31" = "t[31]"-words ✓; 65 noun / 62 pronominal / 94 ne-lead / 98 vient-lead respected ✓. No standing or red-team verdict contradicted, downgraded, or re-litigated; §7 intact.

## Verdict: PROMOTE

**08 = 't'**, named at battery grade. The bar's conditions are met exactly: byte evidence at two independent windows (@922, @944) with zero new assumptions, zero kill-grade contradictions across all 18 windows, adverse answered. Registry ratification is red-team venue; this battery names the value, it does not bank it.

## Scope

Value naming only, battery grade. Untouched: 74's tier at @922 (the "sommet"-shaped one-word rival parse stays live as an alternative, not a contradiction); 41's value at @60; 89's tier at @779; 85's value; the red-team docket. Per §4 (promote), no follow-ups required. Natural next questions (not queued by this worker): re-fire `08-leftattach-944-1323` C2 with 08='t' (its own gated follow-up); test "et"-parse consequences at the remaining "40 08" windows; re-open `seg-41-08-leftedge` (its bar's assumption budget drops: with 08='t', only 41's letter content remains unbudgeted — "41t-ière" = "entière" iff 41="en").

## Bookkeeping

- `battery-queue.json`: `val-08-letter-census` queued → verdict/promote (temp-file + rename, own entry only; pre-write assert confirmed no prior verdict; JSON re-validated from disk; no downgrade).
- Lock `locks/val-08-letter-census.lock`: created on start, deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched.
