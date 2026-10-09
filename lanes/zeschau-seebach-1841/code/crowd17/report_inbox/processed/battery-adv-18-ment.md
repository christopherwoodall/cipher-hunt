# Battery verdict: adv-18-ment

## Bar (verbatim, pre-registered)

"resolve iff 18 parses as an adjective stem with the '[18]ment pour [36]' frame clean under standing values; else retire the adverb candidate"

Numbered clauses:
1. 18 parses as an adjective stem (at the target window).
2. The '[18]ment pour [36]' frame is clean under standing values.
3. (Adverses) (a) the '-ment' compositional rival (82+06) is answered; (b) "the adverb fork lost everywhere else" is accounted for.

## Method

Read BATTERY-PROTOCOL.md first; created `locks/adv-18-ment.lock` on start (agent id + UTC timestamp). Re-derived the full stream from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` parsed per `repair_parse.py` (1,847 pairs / 96 types verified). `canonical.py` never touched. R5005, sealed gate instances, and the red-team adjudication queue untouched.

Offset convention note: the target brief's "@736-739" follows the ent-06 report's 0-based indexing (their "@736-739" = "18-82-06-00"). In 1-based lane convention: 18@737, 82@738, 06@739, 00@740, 36@741 (all row a5_02). Both are given below.

## Window-level evidence

Target window, 1-based @736-741, row a5_02:

`85 93 76 18 82 06 00 36 20 30 67`

Standing values at the frame: 76 = noun, masculine (battery-promoted; "77 76" = "le [76]" x3 re-derived); 82 = 'm' (banked GT); 06 = 'ent' (promoted 2026-10-08); 00 = 'pour' (A9 promoted); 36 = NOUN class (R18 registry).

18 census: n=7. Preceders {78, 91, 19, 76, 88, 35, 62} x1 each; followers {93, 89, 14, 82, 55, 79, 70} x1 each. Windows (1-based): @10 "77 78 18 93", @303 "91 18 89", @586 "19 18 14", @737 target, @906 "88 18 55", @1010 "35 18 79", @1067 "62 18 70".

"82 06" census (independent re-derivation): exactly 4 stream-wide. 1-based @580 "94 82 06 06" = "ne mentent" (verb, ent-06 F1); @738 target "18 82 06 00"; @1184 "94 82 06 06" = "ne mentent" (verb); @1355 "94 82 06 52" = "ne ment [52]" (verb, 3sg "mentir"). The target is the sole non-verbal "82 06" window.

## Analysis — elimination of rival segmentations

The substring "18 82 06" must form one morphological unit ("82 06" never strands independently). Candidate functions for "[18]ment":

- (a) Adverb: 18 = adjective stem + "-ment" (82+06 compositional spelling). Coherent; requires 18 adjective-stem.
- (b) Finite verb 3pl: "[18]m"-stem + "-ent". DEAD — needs a 3pl subject; only candidate 76 is singular ("le [76]" x3); French pro-drop ungrammatical.
- (c) Bare verb stem "ment-" (cf. "mentent"): DEAD — "ment" is not a finite form; infinitive would need "-ir"; 06='ent' is promoted and cannot be re-read here.
- (d) Deverbal noun "[18]ment": DEAD — needs 18 = verb stem (18 is never verb-shaped in 7 windows) AND "76 [18]ment" stacks two bare nouns, ungrammatical in French syntax.
- (e) 18 = free adjective modifying 76, "82 06" separate: DEAD — "m"+"ent" strands ("m'ent" is not French; 06 cannot reattach rightward onto "pour").
- (f) 18 = adverb/noun base: DEAD — adverbs and nouns do not take "-ment".

Only (a) survives. 18 is therefore FORCED to adjective-stem at this locus — by elimination, not by assumption.

Corroboration (not load-bearing): @10 "77 78 18 93" = "le 78 18" places 18 in postnominal adjective position under the free-noun reading of 78='ver' (live per the R16-005 lead). Conditional on 78's free/bound status, which remains open.

## Per-clause pass/fail

- **Clause 1 (18 parses as an adjective stem): PASS.** Forced by elimination of (b)-(f) above; corroborated by the @10 postnominal-adjective window. No window forces 18 non-adjectival at kill grade.
- **Clause 2 (frame clean under standing values): PASS.** Morphology: 18 + 82('m') + 06('ent') = "[stem]ment", the compositional "-ment" spelling (ent-06's own note). Syntax: "[18]ment pour [36-noun]" parses as adverb + "pour"-complement ("uniquement/spécialement pour [36]"-shaped); host clause "[93-verb] [76-object] [adv] pour [36]" is coherent. No standing value contradicted (76 noun, 82 'm', 06 'ent', 00 'pour', 36 NOUN all hold as-is).
- **Adverse (a) ('-ment' compositional rival 82+06): ANSWERED.** The compositional spelling is compatible with the adverbial function (ent-06: "fork A's '-ment' readings are 82+06 compositional, compatible with 06='ent' — not a rival value for 06"). The rival FUNCTIONS (verb-ending on "[18]m", pronoun "m'") are fenced in (b)/(e) above. 06="ent" and 82='m' values untouched; no polyvalence declared (§7 intact).
- **Adverse (b) (adverb fork lost everywhere else): ANSWERED.** Independently confirmed: "82 06" n=4, three are verbal ("mentent" x2, "ne ment" 3sg); the target is the SOLE adverbial candidate. This verifies the claim's "lone", exactly as ent-06's 06-census (n=44) found.

## Standing-verdict check

No contradiction. ent-06's promote (06="ent") is respected — this battery resolves ent-06's own stated conditional ("Sole candidate @736-739 ... conditional on open 18 (adjective stem?)"). No red-team verdict on 18 exists; registry has no 18 cell. Nothing downgraded.

## Verdict

**PROMOTE (locus-level, battery grade; needs red-team ratification).** "[18]ment pour [36]" (0-based 736-739 = 1-based @737-740, row a5_02) resolves as the lone "-ment" adverb in the stream. 18 is adjective-stem-shaped at this locus.

Scope limits (explicit): no global naming of 18 (n=7, class elsewhere underdetermined — this battery does not decide 18's class at @303/@586/@906/@1010/@1067); no value named for the stem (which French "-ment" adverb is open); the host-verb detail ("85 93") is out of scope; the @10 corroboration stays conditional on 78's free/bound status.

## Bookkeeping

Report: `code/crowd17/report_inbox/battery-adv-18-ment.md`. Queue: `adv-18-ment` → verdict/promote (temp-file + rename, pre-write assert confirmed queued/verdictless, JSON re-validated post-write). Lock created on start, deleted on completion.
