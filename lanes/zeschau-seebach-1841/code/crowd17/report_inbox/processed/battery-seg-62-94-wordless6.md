# Battery verdict: seg-62-94-wordless6

**Target:** `seg-62-94-wordless6` (P2)
**Date:** 2026-10-09
**Worker:** battery worker (subagent 4d35395c-2675-4c35-af08-d455010d69a8)
**Claim:** "scope the word-final-'ne' segmentation to the 6 D3-un-attachable windows only (@101, @509, @762, @841, @1363, @1687)"
**Stream:** repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847 pairs / 96 types held). `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

## Bar (verbatim from battery-queue.json)

"name W's class per window (noun vs verb) with >=4/6 parsing under one class; resolve the @1363/@1687 left-class tension ('donne'-verb at @1363 vs noun-needed at @1687)"

## Numbered clauses (restated before testing; not modified after)

1. C1 — For each of the 6 windows (94 at @101, @509, @762, @841, @1363, @1687; 62 at -1 each), name W's class (noun vs verb) from the syntactic slot W occupies under standing values. W = the French word formed as [62-value]+"ne" (94 = word-final "ne" syllable); 62's value itself is NOT named.
2. C2 — The word-final-'ne' segmentation is supported iff >=4/6 windows parse under ONE class (noun or verb).
3. C3 — Resolve the @1363/@1687 left-class tension: the parent battery's WEAK 'donne'-verb pass at @1363 vs the noun needed at @1687. PASS iff the tension is resolved with stated reasoning under standing values.

Verdict mapping (pre-registered): promote iff C2 and C3 PASS; kill iff a window forces the word-reading false at kill grade under standing values; else null with 1-3 follow-ups.

## Method

1. Read BATTERY-PROTOCOL.md first; created `locks/seg-62-94-wordless6.lock` on start (2026-10-09T08:03:02Z), no prior lockfile present.
2. Re-derived the repaired stream independently; asserted 1,847 pairs, 96 types.
3. Verified the 62-94 bigram census byte-exact: exactly x9 (62 at @100 @508 @761 @840 @1329 @1362 @1686 @1704 @1772; 94 at +1 each). Matches parent.
4. Adopted (not duplicated): seg-62-94-wordfinal KILL (x9 word-claim dead; @1772 forces break; word-reading DEMONSTRATED at @508); verbless-ne-family PROMOTE (D3-un-attachable family; @508 re-framed); ne-24-profile (24 = finite-modal); verb-93 (93 = verb class); prof-92 (92 = verb class, subset-scoped; nominal subset 2 legs < 3 standard); R18 (65 = noun; 92 = verb class subset-scoped); ent-06 (06 = "ent"); 21 = noun, 26 = noun (battery promotes); 69 = 'ce' (battery); 88 = verb class (battery).
5. The D3-un-attachable premise (particle-'ne' dead/strained at the 6 windows) is adopted from verbless-ne-family + seg-62-94-wordfinal, not re-derived.
6. Class test is SLOT-based: W's class = the syntactic category its position requires under standing values (nominal slot → noun; verbal slot → verb). 62's value stays open; no lexical item is named.

## Window-level evidence (all 0-based; 94 idx cited)

### W1: 94 @101 (62 @100), row a1_02
`99:21(noun) [62 94] 102:93(verb-class) 103:59(est,prov) 104:45(ce)`
- W-as-noun: "[21] [W]" = noun+noun adjacent. Ungrammatical (no genitive juxtaposition in French; 21 = noun, not determiner). FAIL.
- W-as-verb: "[21-subj] [W-verb] [93-?]". 93 adjacent; 93 = verb class with open form. Two finite verbs adjacent = ungrammatical; making 93 non-finite invents data. FAIL.
- **Class: NEITHER.** No grammatical slot under standing values. Compatible-only (does not kill; bar allows <6/6).

### W2: 94 @509 (62 @508), row a3_00 — ANCHOR
`507:77(le,prov) [62 94] 510:64(qui) 511:98`
- "et le [W]ne qui [98]": determiner + W + relativizer. W occupies a DET _ REL nominal slot.
- W-as-noun: CLEAN. ("le [moine/trone/prone/cone/hymne] qui ..." — masculine -ne noun, cf. w508-noun-ne candidates.)
- W-as-verb: "le" + verb ungrammatical. FAIL.
- **Class: NOUN (clean).** Re-verified; consistent with parent's DEMONSTRATED anchor.

### W3: 94 @762 (62 @761), row a5_03
`760:20 [62 94] 763:59(est,prov) 764:39`
- W-as-noun: "[W] est" — W as subject of copula "est" = nominal slot. ("20" is a left-edge modifier; whether determiner or adverb, W heads/is the subject NP.) An infinitive-subject reading is impossible ("-ne" is not an infinitive ending); finite-verb before "est" ungrammatical.
- W-as-verb: "[W-verb] est" = verb+verb adjacent. FAIL.
- **Class: NOUN.** (Full-clause cleanliness is load-bearing on open 20/39; W's NOMINALITY is fixed by the subject-of-copula slot.)

### W4: 94 @841 (62 @840), row a5_06
`839:20 [62 94] 842:26(noun) 843:12`
- W-as-noun: "[W] [26]" = noun+noun adjacent. FAIL.
- W-as-verb: "[20] [W-verb] [26-noun]" = S-V-O; V+O core "[W] [26]" clean (26 = noun, battery-promoted). Subject "20" open but not contradicted.
- **Class: VERB (weak — V+O core clean, subject 20 open).** Noun fails, so verb is the only viable class.

### W5: 94 @1363 (62 @1362), row a7_06
`1361:92(verb-class) [62 94] 1364:79(tout) 1365:14`
- W-as-noun: "[92-verb] [W-noun]" = V+O; direct-object slot. 92's verb class is PROMOTED (R18, prof-92-confirmed). "tout en [60]" frame coherent (cf. core-14-622-bank). W's nominality rests on a promoted premise.
- W-as-verb: "[92] [W-verb]" = V+V adjacent. Requires 92-as-noun (subject) — the nominal subset has 2 legs < 3 standard (prof-92). WEAK at best, below-standard premise.
- **Class: NOUN (preferred).** The noun reading uses 92's promoted class; the parent's 'donne'-verb weak pass used the below-standard nominal subset.

### W6: 94 @1687 (62 @1686), row a8_05
`1683:65(noun,R18) 1684:13 1685:93(verb-class) [62 94] 1688:79(tout)`
- W-as-noun: "[93-verb] [W-noun]" = V+O; "[65-noun] [93-verb] [W-noun] tout" = S-V-O-Adv (13 sub-lexical). 65 = noun (R18), 93 = verb class (promoted). Clean nominal object slot.
- W-as-verb: "[93] [W-verb]" = V+V adjacent. FAIL.
- **Class: NOUN.**

## Per-clause pass/fail

1. C1 (name class per window): DONE — W1 neither, W2 noun, W3 noun, W4 verb, W5 noun, W6 noun.
2. C2 (>=4/6 under one class): **PASS** — noun covers W2, W3, W5, W6 = **4/6**. (Verb 1/6, neither 1/6.)
3. C3 (resolve @1363/@1687 tension): **PASS** — The tension dissolves. The parent's 'donne'-verb at @1363 was a WEAK pass load-bearing on the below-standard 92-nominal subset (2 legs < prof-92's 3-leg standard). The noun reading ("[92-verb] [W-noun]" V+O) rests on 92's PROMOTED verb class and is the preferred parse. Both @1363 and @1687 thus parse with W-as-noun. No verb-shaped W is required at @1363 under the best parse.

## Adverses

None listed. Standing tensions noted (not adverses of this target):
- il-62's battery PROMOTE (62='il') vs class-62-fullcensus NULL: pre-existing; this battery names W's class, never 62's value — untouched.
- 62's global value (règne/trône narrowed; redteam-62-conditioned live): untouched; W's class is syntactic, not lexical.

## Verdict: PROMOTE (battery grade; scoped)

The word-final-'ne' segmentation is SUPPORTED for the 6 D3-un-attachable windows, with W predominantly noun-class (4/6: W2 clean, W3/W5/W6 slot-clean). The @1363/@1687 tension is resolved (both noun; the 'donne'-verb weak pass is superseded).

**Explicitly fenced (NOT promoted):**
- 62's VALUE (not named; W's class is syntactic).
- W1 (@100): no grammatical slot under either class — compatible-only; a gap, not a kill (bar allows <6/6).
- W4 (@840): verb-class outlier (weak); the 4/6 noun majority stands.
- The 3 attachable windows (@1330, @1705, @1773): out of scope; particle-'ne' stands there per ne-94/ne-24-profile.
- Canonicality: all rows carry unvalidated upstream offsets; verdict holds on the canonical stream per protocol.
- Battery grade only; red-team ratification needed before banked use. No §7 polyvalence declared (segmentation, not value).

## Standing verdicts (checked, none downgraded)

- R17-001 (94='ne' STRONG LEAD): untouched (segmentation-only; 94 stays 'ne' as syllable).
- seg-62-94-wordfinal KILL: upheld and narrowed — the x9 claim stays dead; this scopes the live residue to the 6 windows.
- verbless-ne-family PROMOTE: consistent (D3-un-attachable premise adopted).
- ne-24-profile, verb-93, prof-92, R18 registry, ent-06: used as premises, not contradicted.
- R17-018 (94 duality): the 6 windows still need non-particle 94; word-final 'ne' at 4/6 noun is the battery's answer, red-team owns the declaration.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/seg-62-94-wordless6.lock` created on start (2026-10-09T08:03:02Z), no prior lockfile; deleted on completion (verified gone).
- `battery-queue.json`: `seg-62-94-wordless6` status `queued` -> `verdict`, `verdict: {"result": "promote", "report": "code/crowd17/report_inbox/battery-seg-62-94-wordless6.md", "date": "2026-10-09"}` (temp-file + rename; pre-write assert confirmed queued/verdictless — no downgrade; JSON re-validated; only this entry touched).
- R5005, sealed gates, red-team adjudication queue untouched. No invented numbers: every @-offset traces to the repaired stream re-derived in-session.
