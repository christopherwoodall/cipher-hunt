# Battery verdict: pasX-adverb-census

## Bar (verbatim, pre-registered)

> if some other group parses as an adverb after 'pas', compare its contact profile to 62's to bound the adverb hypothesis distributionally

Numbered clauses (pre-registered before testing):
1. (Census clause) Census all "30 X" bigrams stream-wide (X including and excluding 62) and test each X for an adverb parse with a complement-bearing right edge.
2. (Comparison clause) If any X parses as an adverb after "pas", compare its contact profile to 62's contact profile and state the distributional bound on the adverb hypothesis.

Origin: null follow-up #3 of battery-adv-62-pas-par (2026-10-09). Task brief bars add: promote iff a clean adverb frame parses, fence iff none does, kill iff a kill-grade contradiction forces X≠adverb.

## Method

Read BATTERY-PROTOCOL.md first; lock `locks/pasX-adverb-census.lock` created on start (agent id + UTC), no stale lock present; deleted on completion. Re-derived the stream from the repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py` — same tokenization, re-run inline; asserts held: 1,847 pairs, 96 groups). `canonical.py` never touched. R5005, sealed gates, red-team queue untouched.

Standing values honored and not re-litigated: 30="pas" (prom), 64="qui" (prom), 96="par" (prom), 00="pour" (prom), 47="ce" (prom), 87="ce" (prom), 82="m" (gt), 92=verb (cls), 06="ent" (prom, syllabic "ent" when left neighbor is not a verb stem per the 06-function rule), 79="tout" (prom), 11="la" (gt), 77="le" (prov), 62="il" (lead), 65=noun (cls). Standing §7: 67 et/veut is the sole true polyvalence (67="veut" iff follower infinitive-shaped); 20~17 and 23~26 splits hold; kills hold (48="est"/"ne"/"de", 09/92 "-ère", 20="fois"). Battery-grade (not re-litigated, cited as the worker found them): 69=noun, 03 conditioned split (verb stem in "03 29" x3, noun elsewhere), 19=one verb lexeme.

## Census (repaired stream, re-derived): 19 "30 X" windows, 12 distinct X

| @ | row | window (30 X Y) | X standing value | adverb test |
|---|---|---|---|---|
| 30 | a1_00 | 30 03 64 | 03: noun arm (follower 64, not 29) | FENCE — noun ≠ adverb |
| 45 | a1_01 | 30 62 96 | 62: "il" (lead) | FENCE — window-local fence already executed by adv-62-pas-par; pronoun ≠ adverb |
| 483 | a2_11 | 30 01 19 | 01: OPEN; 19: verb lexeme | FENCE — no established adverb value for 01; naming one would invent data |
| 560 | a3_02 | 30 67 11 | 67: et/veut (§7) | FENCE — class closed by standing §7; follower 11="la" not infinitive → 67≠"veut"; neither arm adverb-shaped |
| 656 | a4_02 | 30 03 62 | 03: noun arm | FENCE — noun ≠ adverb |
| 742 | a5_02 | 30 67 77 | 67: et/veut (§7) | FENCE — 77="le" (prov) not infinitive → 67≠"veut"; neither arm adverb-shaped |
| 993 | a6_01 | 30 03 60 | 03: noun arm | FENCE — noun ≠ adverb |
| 1114 | a6_07 | 30 69 11 | 69: noun (battery) | FENCE — noun ≠ adverb |
| 1222 | a7_01 | 30 09 20 | 09: OPEN ("-ère" killed); 20: OPEN | FENCE — no established adverb value |
| 1251 | a7_02 | 30 06 65 | 06: "ent" (prom), syllabic here (left neighbor 30 not a verb stem) | FENCE — syllable ≠ adverb |
| 1269 | a7_02 | 30 20 64 | 20: OPEN; 64="qui" (prom) | FENCE — no adverb value for 20; right edge "qui" cannot complement an adverb |
| 1309 | a7_04 | 30 92 44 | 92: verb (cls) | FENCE — "pas [92-verb]" is the canonical negation frame; verb ≠ adverb |
| 1327 | a7_04 | 30 06 62 | 06: syllabic "ent" | FENCE — syllable ≠ adverb |
| 1368 | a7_06 | 30 82 16 | 82: "m" (gt, letter) | FENCE — letter ≠ adverb |
| 1561 | a8_01 | 30 06 60 | 06: syllabic "ent" | FENCE — syllable ≠ adverb |
| 1702 | a8_06 | 30 20 62 | 20: OPEN | FENCE — no established adverb value |
| 1716 | a8_06 | 30 64 47 | 64: "qui" (prom); 47="ce" (prom) | FENCE at near-kill grade — "qui" is a relative pronoun; a prom-tier value categorically excludes adverb |
| 1729 | a8_07 | 30 15 01 | 15: OPEN; 01: OPEN | FENCE — no established value; adverb reading unnameable |
| 1733 | a8_07 | 30 06 60 | 06: syllabic "ent" | FENCE — syllable ≠ adverb |

Successor inventory of 30: 06 x4, 03 x3, 67 x2, 20 x2, 01 x1, 09 x1, 15 x1, 62 x1, 64 x1, 69 x1, 82 x1, 92 x1.

Right-edge check (complement-bearing requirement): the right edges observed are qui (x2), par (x1, already shown ungrammatical as "par pour" at @45–48), la (x2), 19-verb (x1), 62 (x2), 77="le" (x1), 60 (x3), 20 (x1), 65 noun-cls (x1), 44 (x1), 16 (x1), 47="ce" (x1), 01 (x1). None bears an adverb complement; the only adverb-shaped right edge in the lane's grammar ("par" + nominal) is the one already killed at @45.

## 62's contact profile (reference for the distributional bound)

Re-derived from the repaired stream (see data-quality note below): 35 occurrences.

- Successors (n=35): 94 x9, 48 x6, 98 x5, 16 x4, 61 x2, 06 x2, 96 x1, 91 x1, 21 x1, 18 x1, 38 x1, 46 x1, 93 x1.
- Predecessors (n=35): 21 x5, 20 x4, 74 x3, 03 x2, 08 x2, 78 x2, 92 x2, 93 x2, 02 x1, 04 x1, 06 x1, 10 x1, 14 x1, 30 x1, 34 x1, 36 x1, 40 x1, 41 x1, 51 x1, 77 x1, 98 x1.

Bound (stated, not executed — the comparison's antecedent failed): any future adverb candidate X after "pas" must show a narrow, complement-bearing successor profile. 62's profile — 13-way successor spread, 21-way predecessor spread, top successor 94 ("ne"-family particle context) — is the reference anti-profile: it reads as a high-frequency function word (consistent with lead "il"), not an adverb.

## Data-quality note (for supervisor audit)

battery-adv-62-pas-par reported 62's successor distribution as n=38. This does not reproduce: the repaired stream contains exactly 35 occurrences of 62 (all with successors; positions listed in working notes), and the obsolete 1,846-pair parse contains 34. The n=38 figure is off by 3–4 on both parses. The adv-62 fence itself is unaffected (its killing argument was the right-edge "par pour" impossibility, not the counts), but its contact table should be corrected before any distributional argument cites it.

## Clause verdicts

1. (Census clause) PASS — census complete: 19 windows, 12 distinct X, zero clean adverb frames. Every X is fenced with a stated, byte-grounded cause.
2. (Comparison clause) INAPPLICABLE — antecedent false. No X parses as an adverb after "pas", so no contact-profile comparison executes. The distributional bound is stated above for future use.

Kill check (brief bars): kill requires a kill-grade contradiction forcing X≠adverb. The claim is existential; groups 01, 09, 15, 20 remain OPEN in the registry and are not forced ≠adverb at kill grade. No kill. No standing red-team verdict contradicted or touched.

## Verdict: NULL (fence executed)

The adverb-after-"pas" hypothesis is fenced stream-wide for the observed X inventory: no "30 X" window yields an adverb-shaped X with a complement-bearing right edge. The fence is window-local per X (class-level for 06, 64, 67, 82, 92, 69, 03; value-lack for 01, 09, 15, 20) and does not close any group's class beyond what standing values already close.

## Follow-ups (null regenerates work)

1. `adv-01-19-frame` (P3): test 01 as adverb at @483 ("30 01 19" = "pas [01] [19-verb]") — the only census window where an adverb+verb frame is positionally plausible ("pas encore [part]" shape). Bar: name 01's value from independent windows only (no invention); fence iff no independently-grounded value parses.
2. `audit-adv62-count` (P3): reconcile adv-62-pas-par's 62 successor distribution (n=38) against re-derived counts (repaired n=35, old-parse n=34); recount from the repaired stream and correct that report's contact table. The fence's right-edge argument stands; only the distributional numbers need repair.
3. `pasX-ellipsis-frames` (P3): the census leaves 19 "30 X" windows with no verb host in the immediate bigram — test whether ne-drop + ellipsis (bare "pas" negating a non-verbal constituent) parses at a sample, e.g. @1114 "pas [69-noun] la", @1368 "pas m [16]", @1716 "pas qui ce"; fence iff no elliptical frame parses.

## Bookkeeping

- Lock `locks/pasX-adverb-census.lock` created on start, deleted on completion.
- `battery-queue.json`: target `pasX-adverb-census` queued → verdict/null (own entry only, temp-file + rename; pre-write assert confirmed no prior verdict; JSON re-validated post-write).
- R5005, sealed gate instances, red-team adjudication queue untouched. `canonical.py` never used.
