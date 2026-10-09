# Battery report: 88-prep-rival

Target: `88-prep-rival`
Claim: "decide preposition vs verb for 88"
Date: 2026-10-09
Worker: 8582904a-8894-4ffe-9567-a7c1970c9563
Lock note: no stale lock existed; created locks/88-prep-rival.lock 2026-10-09T03:57:18Z, deleted on completion.

## Bar (verbatim from battery-queue.json)

">=2 frame-legs deciding preposition vs verb for 88. A prep-88 reframes 'qui vient [65] [88=prep] [56]' and the @513 slot"

## Numbered clauses (fixed before testing)

1. Produce >=2 frame-legs deciding preposition vs verb for 88. A frame-leg = a window that parses grammatically under one reading and is ungrammatical under the other (1841 diplomatic French).
2. Test the bar's candidate prep reframe: 'qui vient [65] [88=prep] [56]' at the @513 slot (0-based; @514 1-based).

Offset convention: all @-offsets below are 1-based repaired-stream pair indices.

## Method

Repaired 1,847-pair / 96-type stream only: code/side-keyhunt/repaired_offsets.json over data/upstream-ct_R5005.txt, parsed exactly like code/side-keyhunt/repair_parse.py (byte-exact `[s[i:i+2] for i in range(o, len(s)-1, 2)]`). code/side-keyhunt/canonical.py never used. R5005, sealed gates, red-team adjudication queue untouched.

88 census: n=23. Predecessors: 39 x2, 69 x2, 24, 06, 50, 89, 02, 54, 45, 79, 65, 70, 29, 61, 48, 16, 41, 11, 81, 93, 94 (all x1). Successors: 77 x3, 11 x2, 24 x2, 43, 19, 02, 20, 40, 53, 47, 56, 10, 37, 66, 18, 29, 70, 01, 26 (all x1).

Standing values used: banked 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que; promoted 87=ce, 64=qui, 96=par, 17=fois, 79="tout" (A5), 00="pour" (A9), 84="on" (A15), 47="ce" (A4); provisional 59=est, 77="le"; battery-level (pending ratification) 94='ne' STRONG LEAD (R17-001), 24='faire', 93=verb-class, 45='ce' HOLD (A11), 65=noun-class, 06='ent'.

## Clause 1 — verb-deciding legs

Six independent frame-legs decide VERB. Zero legs decide preposition.

**Leg A — "à [88]" x2 (@766 a5_03, @1728 a8_07).** "20 62 94 59 39 [88] 66 98 80 10 22" and "52 37 43 98 39 [88] 24 30 15 01 56". Locus-level PROMOTE per battery 88-1727-shape (2026-10-09): 88 is infinitive-shaped at @1728 ("98 39 [88]" = "vient à [88-inf]"); @766 "est à [88-inf]" is the passive-infinitive construction. After "à", 1841 French licenses an infinitive — not a bare noun (needs an article, shown ungrammatical in the same battery) and not a preposition ("à [prep]" ungrammatical). Prep-88 dies at both windows.

**Leg B — "[88]er" (@1050 a6_04).** "11 67 76 85 41 [88] 29 40 29 74 74": 88 directly bears 29='er' (banked GT) — "[88]er", the infinitive ending on the 88 stem. A preposition cannot carry a verbal inflectional ending. Verb-deciding, unconditional on open values.

**Leg C — "ne [88]" (@1707 a8_06).** "94 30 20 62 94 [88] 26 12 06 29 40": 94='ne' STRONG LEAD (R17-001). The negation frame requires a verbal host; "ne [preposition]" is ungrammatical in 1841 French (bare-'ne' license covers modal/fixed-frame verbs only — never prepositions). Verb-deciding, conditional on the standing 94 lead.

**Leg D — "faire [88]" (@43 a1_01).** "39 64 41 01 24 [88] 43 81 30 62 96": 24='faire' (battery-promoted). Causative "faire" takes an infinitive complement; "faire [preposition]" is ungrammatical. (Mirrors the imp-80-set battery's "faire [03]er" causative finding.) Verb-deciding, conditional on 24='faire'.

**Leg E — "la [88]" (@1118 a6_07).** "65 38 30 69 11 [88] 70 12 06 14 06": 11='la' (banked GT). Nominalized infinitive — "le/la + infinitive" is grammatical 1841 French ("le boire", "la dire"); 88 is independently infinitive-capable (Legs A, B). "la [preposition]" is ungrammatical. Verb-deciding.

**Leg F — "ce [88]" (@403 a2_08).** "82 48 06 11 45 [88] 53 34 69 26 00": 45='ce' HOLD (A11). "ce" as demonstrative-pronoun subject + finite verb is grammatical ("ce semble", "ce fut"); "ce [preposition]" is ungrammatical. Verb-deciding, conditional on the A11 HOLD.

**Preposition legs: none.** Exhaustive check of all 23 windows: every window either parses under a verbal reading of 88 (infinitive or finite) or is fenced below as analytic/multi-open. No window requires prep-88, and six windows forbid it. The preposition rival is killed.

## Clause 2 — the bar's candidate prep reframe: FAILS (fenced)

@514 (1-based; 0-based @513), a3_00: "62 94 64 98 65 [88] 56 87 77 80 09" = "qui vient [65] [88] [56]". The proposed "qui vient [65] [88=prep] [56]" does not parse: 65 is noun-class (prof-65 promote, 2026-10-08), "venir" is intransitive, and "vient [65-noun] [prep] [56]" admits no grammatical parse in 1841 French. It does not parse under verb-88 either ("vient [65] [88-inf]" — 65 blocks the "vient à/de + inf" frame). Fenced with cause: unparseable at battery grade under both readings; the strain localizes to 65's slot, not 88. Not a prep leg — a fence.

## Fenced windows (neither leg, cause stated)

- @617/@620 (a4_00/a4_01): "70 [88] 10 29 [88] 37" — 70='pre' (GT) prefix zone; 88 possibly word-internal/analytic (the second [88] follows "er"). Analytic zone, not word-level.
- @731 (a5_02): "48 [88] 11" — 48='e' (R17 promoted) letter zone; "[e][88]" possibly one word. Analytic.
- @335 (a2_05): "54 [88] 40" — 40='e' (GT) follows 88 ("[88]e"?); 54 open. Multi-open.
- @498 (a2_11): "79 [88] 47" — 79 word/syllable split open (79-split battery); "tout [88]" unparseable under both word-tout readings. Fenced on 79.
- @211 (a2_00): "50 [88] 19" — 50 open; "pas [88-inf]" conditional only.
- @305/@307 (a2_04): "89 [88] 02 [88] 20" — 89 verb-frame; 02 open; 88 non-finite required but prep vs infinitive undecidable.
- @905 (a5_09): "16 [88] 18" — 16 open (frame-82-16 null). Multi-open.
- @1261/@1268 (a7_02): "69 [88] 01" / "69 [88] 24" — 69 open (fenced "ce"). Multi-open.
- @1515 (a7_11): "81 [88] 11" — 81 open; "à [88-inf]" conditional only.
- @1542 (a8_00): "93 [88] 77 78" — verb-93 + 88 + 'le' (provisional) + 78; enclitic/proclitic ambiguity. Multi-open.
- @647 (a4_02), @87 (a1_02): "[X] [88] 77 ..." — "[88]-le" enclitic pattern possible (77='le' provisional); supports verb, not a numbered leg.

## Adverse answered

"88's class is governor/verb-class at class level only" — resolved: the governor/prepositional reading has zero supporting windows across the full n=23 census and is contradicted at six independent legs. Verb-class stands, now with word-level frame-legs. No polyvalence declared (§7 intact — infinitive vs finite uses are normal verb morphology, not polyvalence). Consistent with battery 88-1727-shape (promote, locus-level infinitive) and battery lever-88-governor (null — tested 88 governing an infinitive, i.e. verb-side; nothing contradicted).

## Verdict: PROMOTE

Preposition-vs-verb is decided for VERB at battery grade (six frame-legs, bar requires two). The preposition rival for 88 is killed: no window requires it, six windows forbid it. Needs red-team ratification like all battery promotes; no banked map change proposed here.
