# Battery report — tense-24-311-formclass — VERDICT: PROMOTE

Worker: subagent session 9ebbe3de-7fd4-431c-8c32-87a025d3def3 (seebach battery).
Date: 2026-10-09. Target: `tense-24-311-formclass` (priority 2).

## Claim

"decide FORM CLASS of 24 at @311/@473 from the byte-identical '84 24 37 78' twin windows"

## Bar (verbatim, pre-registered before testing)

"resolve iff 24 at @311 is finite-verb (killing the infinitive/participle arms of F124 at these windows) OR the 24='en' arm dies at these windows (verb-less 'on en [37-predicative]' unlicensed); no tense named"

## Bar restated as numbered clauses

- **c1:** 24 at @311 is FINITE-VERB — the infinitive and participle arms of F124 are killed at these windows.
- **c2 (OR):** the 24='en' arm dies at these windows — a verb-less "on en [37-predicative]" parse is unlicensed.

Either clause passing resolves the bar. No tense is named; no value is named.

## Method

1. Read BATTERY-PROTOCOL.md fully; created `locks/tense-24-311-formclass.lock` on start.
2. Copied the bar verbatim from `code/crowd17/next-token/battery-queue.json` (target `tense-24-311-formclass`) before seeing data.
3. Re-derived the repaired stream in-session: `code/side-keyhunt/repair_parse.py` byte-exact tokenization (`[s[i:i+2] for i in range(o, len(s)-1, 2)]`) over `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`. Asserted 1,847 pairs / 96 types. Never `canonical.py`. Never touched R5005.
4. Exhaustive census (not sampled): every occurrence of `84 24 37 78`, `24 37`, `84 24`, and the 78 contact profile, all re-derived from the bytes.

## Indexing note (notation, not a data discrepancy)

The target writes "@311/@473". On the 0-based repaired stream the twin windows START at @310 and @473; 24 sits at @311 and @474. The target names 24's index in window 1 and the window start in window 2. Both windows are byte-identical `84 24 37 78` with identical left frame `46 84`. The form-class decision below applies to 24@311 and 24@474 alike.

## Window-level evidence (bytes, repaired stream)

- W1 @307–@319 (row a2_04): `20 17 46 84 24 37 78 45 64 59 32 94`
- W2 @470–@482 (rows a2_10/a2_11): `06 67 46 84 24 37 78 74 45 93 00 13 52`
- `84 24 37 78` occurs **exactly twice** stream-wide: @310, @473. Exhaustive.
- `24 37` occurs **exactly twice**: @311, @474 — both inside the twin windows. Exhaustive.
- `84 24` occurs exactly 3x: @310, @473, @1485. The @1485 contact (`84 24 87 08`) is a different follower family — fenced out, not evidence for or against.
- Granted frame values in play: 46="que" (banked ground truth), 84="on" (A15 granted; R17-009 reads these exact windows as "qu'on 24" subordinate slots), 37=predicative (A1 frame granted, class level; the bar's own "[37-predicative]" premise), 64="qui" (promoted), 59="est" (provisional), 17="fois" (promoted), 45="ce" (A11), 00="pour" (A9).
- 78 contact profile (31 tokens): dominant frames `37 78 X` and `47 78 X` are pronominal/nominal-shaped, not adjectival (battery-adj-groundwork-refollower); "le 78 qui" @1078 nominal; 78="ver" stays LEAD (R17-021); 78 sits in a noun slot @1839 ("de [21] et [78-word]", R18-011). No 78 window supports a verb reading; several force nominal.

## Per-clause results

### c1 — PASS: 24@311 (and twin 24@474) is finite-verb; infinitive/participle arms killed

The clause frame is `46 84 24 [37] 78` = "que on 24 [37] 78" at both windows. With 84="on" the clause's subject (A15; the "qu'on" parse of these exact windows is the standing R17-009 grant):

1. An overt subject pronoun forces a finite verb in the same clause. **Infinitive arm dies at kill grade:** French licenses overt-subject infinitives only under prepositional government (pour/de/à) or perception-verb AcI — "que" is neither. "que on faire [pred]" is ungrammatical in 1841 diplomatic French exactly as in modern French.
2. **Participle arm dies at kill grade:** a bare past participle with an overt subject and no auxiliary is ungrammatical ("que on fait [pred]" — the auxiliary is absent; participial absolutes are subjectless, and none is present here).
3. The verb slot is 24: the only post-subject slot before the predicative frame is 24 (predicative 37 must follow its verb in French; nothing precedes 24 except the subject). Therefore 24 at these windows is finite-verb, form class decided. **No tense named, no value named** — the bar asks for neither, and none is supportable at battery grade.

### c2 — PASS: the 24='en' arm dies at these windows

If 24='en', the clause reads "que on en [37] [78] …" with 'en' a proclitic needing an immediately preverbal host:

1. Candidates after 24: only 37 and 78. 37 is the predicative frame (A1 class-level grant; the bar's premise) — not a verb. 78 is nominal-shaped (R17-021, battery-adj-groundwork) — not a verb.
2. Even granting arguendo a verb at 78, "on en [predicative] <verb>" is ungrammatical: a predicative cannot precede its verb in French clause order (outside poetic inversion, absent from 1841 diplomatic prose).
3. No zero copula exists in French of any era — there is no verb-less rescue.
4. 'en' cannot cliticize backward (French 'en' is never enclitic to a subject pronoun; imperative enclisis needs an imperative verb, and 'on' is not one) and cannot skip 37/78/45 to a distant verb (clitics are immediately preverbal).

So "on en [37-predicative]" at these windows is verb-less and unlicensed → the 24='en' arm dies at kill grade. This also independently confirms c1: the only remaining occupant of the verb slot is 24, finite.

## Adverses answered (not ignored)

- **R18-008 (24='faire' LEAD, 'unique survivor' proof broken):** reckoned. R18-008 is a VALUE-level demotion — "faire" demoted from promote to conditional LEAD, rival "laisser" live. My verdict is FORM-CLASS only (finite-verb), which is value-independent: it holds whether the finite verb is "fait", "laisse", or the unnamed modal of R17-009. I name no value and no tense. The R18-008 LEAD is itself conditional on R17-009's finite-verb frame, which my verdict affirms — no contradiction, no overwrite.
- **The byte-identical @473 twin:** reckoned. The 4-gram `84 24 37 78` and its left frame `46 84` ("que on") are byte-identical at @310 and @473; 24→37 occurs only at @311/@474. The right contexts diverge (W1: `45 64 59 32 …` "ce qui est [32]"; W2: `74 45 93 00 …`), but the subject–verb–predicative frame that the bar tests is identical, and the 'en'-kill argument (no preverbal host for 'en' before 37/78) is structurally identical at both windows. The verdict transfers to 24@474.

## Verdict

**PROMOTE.** Both disjuncts of the bar pass at kill grade on re-derived bytes: c1 — 24@311/24@474 is finite-verb (infinitive/participle arms of F124 dead at these windows); c2 — the 24='en' arm dies (verb-less "on en [37-predicative]" unlicensed). Adverses answered. No standing red-team verdict contradicted — this agrees with R17-009's class-level promote on these exact windows and is consistent with R18-008's value-level demotion. Scope: the twin windows only; @1485 (`84 24 87`) fenced out; no tense and no value named, per the bar.

(Null follow-ups: none required — verdict is promote, not null.)

## Provenance

- Stream: `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py` (1,847 pairs / 96 types asserted in-session).
- Queue: `code/crowd17/next-token/battery-queue.json`, target `tense-24-311-formclass`.
- Protocol: `code/crowd17/next-token/BATTERY-PROTOCOL.md` (§1–§8 followed; lock created on start, deleted on completion).
- Standing: R17-009 (24=finite-verb class promote, "qu'on 24" @311/@474), R18-008 (24='faire' LEAD, unique-survivor broken), R17-021 (78="ver" LEAD), A1 (37 predicative frame), A15 (84="on"), A11 (45="ce"), plus battery-adj-groundwork-refollower (78 nominal-shaped), battery-dict-313-w1-adjudicate (twin-window census, 'ce qui' A11 reading @313–317), battery-tense-24-307 (parent NULL that spawned this target).
- No invented numbers. Every offset above is a 0-based index into the repaired 1,847-pair stream.
