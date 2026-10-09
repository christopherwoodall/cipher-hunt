# Battery noun26-38-profile — verdict: PROMOTE (38 = verb-form)

**Target:** `noun26-38-profile` (P3)
**Date:** 2026-10-09
**Worker:** battery protocol §1–§8 followed. Lock `locks/noun26-38-profile.lock` created on start, deleted on completion. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

## Bar (verbatim, pre-registered)

> "state 38's class (n=7, zero prior profiles) by adjudicating predicative ('59 38' @825-826, load-bearing on provisional 59='est', subject-parse alternative available) vs verb-form ('38 30' @1113-1114, '[verb] pas'-shaped, bare-'pas' caveat) — stated class or fenced split"

**Numbered clauses (fixed before testing):**
- C1: The '59 38' frame (@825-826) adjudicated — 38's class options at this frame stated; the reading's dependence on provisional 59='est' recorded; the subject-parse alternative assessed.
- C2: The '38 30' frame (@1113-1114) adjudicated — 38 parses as verb-form ("[verb] pas") or not; the bare-'pas' caveat addressed via the ne-drop precedent.
- C3: 38's class stated (uniform) or a split fenced with cause. Uniform iff one class covers both C1 and C2. No polyvalence declared at battery level (§7: 67 et/veut remains the sole true polyvalence).
- C4: Adverses answered — 38's value open (class-level only, not re-litigated); 59='est' provisional (C1 conditional, stated); §7 respected.

## Method

Stream re-derived in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py` (byte-exact `[s[i:i+2] for i in range(o, len(s)-1, 2)]`). Result: 1,847 pairs / 96 types. n(38) = 7, byte-confirmed at 0-based @384/@826/@1113/@1343/@1469/@1650/@1828 — matching the brief's window list. All @-offsets below are 0-based.

Standing values used as premises only (never re-litigated): 11="la", 82="m", 29="er", 40="e", 46="que" (pencil GT); 87="ce", 64="qui", 96="par", 17="fois", 79="tout" (A5), 00="pour" (A9), 84="on" (A15), 47="ce" (A4 allophone); 59="est" provisional; 30="pas" battery-promoted; 65="noun" class (R18-001 ratified); "69 11"="cela" locus-level (battery-cela-69-11-word). Ne-drop is lane precedent (16/19 `pas` windows have no 94 within ±10; bare `pas` carries negation).

## Window-level evidence (all 7 windows, byte-traced)

- **W1 @384 (a2_07, mid-row):** `16 52 [38] 37 43 91 36`. 38 between 52 (adjective/adverb §7-split candidate) and 37 (A1 predicative-frame cell, value open). Neither verb-form nor predicative forced — 52's class and 16's class are both open. **Indeterminate.**
- **W2 @826 (a5_06, mid-row):** `87 59 [38] 82 01 24` = "ce(87) est(59) [38] m(82) [01] [24]". The core "ce est [38]" is a copula + predicative slot. Finite-verb-38 is kill-grade dead here ("ce est [V-fin]" = double finite verb); infinitive-38 dead ("c'est [INF]" ungrammatical in 1841 French). Surviving: noun, adjective, **past participle** ("c'est [pp]" — "c'est dit"-shaped, fully standard). Conditional on provisional 59='est' (stated, not hidden). The subject-parse alternative ("[38] as nominal subject of a new 'm [01] [24]' clause") is available but unnecessary — the participle reading unifies with C2 below. The "m [01]" tail is 38-independent (01's value open) and does not discriminate 38's predicative subclass.
- **W3 @1113 (a6_07, mid-row):** `65 [38] 30 69 11 88` = "[65-noun] [38] pas(30) cela(69-11) [88-verb]". **38 is forced as a finite verb at kill grade.** "pas" is a verbal negator: it must immediately follow the finite verb ("[V] pas [OBJ]"; "pas" after the object is ungrammatical, and no verb stands between 38 and 30). 65 is noun-class (R18-001, ratified) so it cannot be the verb; "cela" (@1115-1116, locus-level) is 38's direct object. Parse: "[65] [38-V-fin] pas cela" = "The [65] does not [38] this" — clean S-V-neg-O with dropped "ne" (ne-drop precedent). Predicative-38 (adjective/noun) is kill-grade dead: "[65-noun] [38-adj/noun] pas" is verbless — "pas" has no verb to negate.
- **W4 @1343 (a7_05, mid-row):** `64 52 [38] 47 86` = "qui(64) [52] [38] ce(47) [86]". Fenced for both classes (agrees with adj-37-385-gate): verb-form-38 gives "qui [52-adv] [38-V] ce" but "ce [86-INF]" is ungrammatical (86 = INF class; "ce" cannot subject or follow it here); predicative-38 strands "qui" verbless. **Fenced with stated cause.** (a7_05 carries the weak rival-phase note, −0.85 nats; fence holds on the canonical stream per protocol.)
- **W5 @1469 (a7_09, mid-row):** `62 [38] 26 12 41` — the @1470 gate window. Adopted (not re-litigated) from noun26-residual-adjud: parses iff 38 takes the modal reading ("[62] [38-modal] [26]"). **Verb-form leg (modal).** Predicative-38 has no clean parse here (verbless before 26 under every 26-branch).
- **W6 @1650 (a8_04, mid-row):** `03 [38] 82 16` = "[03] [38] m(82) [16]". Verb-form leg, conditional: "[03-noun] [38-V-fin] me [16-inf]" ("veut me voir"-shaped) — licensed iff 03 is nominal here (03 not followed by 29, so stem-03-nounfamily's noun arm applies, battery-promoted) and 16 is infinitive-shaped (battery infinitive-promote, pending ratification). Predicative-38 is verbless here. **Weak verb-form leg (conditional, stated).**
- **W7 @1828 (a8_11, mid-row):** `82 [38] 83 24` = "m(82) [38] [83] [24]". Fenced for both: finite-38 gives double finite verbs ("[38-V] [83] [24-V-fin]"); predicative-38 is verbless. No clean parse either way. **Fenced with stated cause.**

## Per-clause pass/fail

- **C1 — PASS.** "est [38]" @825-826 parses as predicative; the verbal member of the predicative set (past participle, "c'est [pp]"-shaped) keeps the uniform verb class viable. Finite-verb and infinitive readings dead at kill grade. Conditional on provisional 59='est' — stated; if 59's value ever changes, @826 re-opens.
- **C2 — PASS.** "[38] pas" @1113-1114 forces finite-verb-38 at kill grade ("[65-noun] [38-V] pas cela"); non-verbal predicative dead at kill grade (verbless). Bare-'pas' licensed by the ne-drop lane precedent.
- **C3 — PASS: uniform class stated — 38 = verb-form (verb class).** Distribution: past participle @826, finite @1113, modal @1469, finite @1650 (conditional). W1 indeterminate; W4/W7 fenced with stated cause. No window forces non-verbal 38. The finite/participle/modal distribution is inflectional — one verb lexeme in different forms — not a polyvalence; §7 intact (67 et/veut remains the sole true polyvalence). No split declared or needed.
- **C4 — PASS.** 38's value not named (class-level only). 59='est' provisional — C1 conditional, stated. No polyvalence declared.

## Correction to prior battery evidence

battery-adj-37-385-gate (NULL) read W3 @1113 as "[65-noun] [38-adj] pas [69]" = "postposed epithet + ne-drop negation." That read is ungrammatical: "pas" is a verbal negator and "ne"-drop removes "ne", not the verb — "[noun] [adjective] pas" leaves "pas" with no verb to negate. The window forces verb-38 (the "cela" locus reading at @1115-1116 independently confirms "[65] [38-V] pas cela"). The W3 epithet leg is therefore withdrawn. That battery's W2 assessment ("adjective-shaped") is compatible with the participle reading adopted here (a predicative participle is adjective-shaped in function); its W4 fence, W5 compatibility note, and its C2/C3 (@385 re-anchor not firing) are untouched. No queue entry modified.

## Standing-state check

No red-team verdict exists on 38; nothing contradicted or downgraded. §7 intact. Canonicality caveat stands (68 of 70 upstream row offsets unvalidated; verdict holds on the canonical stream per protocol).

## @1470 unblock

noun26-residual-adjud's gate condition ("'62 38 26' parses iff 38 takes the modal reading") is now satisfiable: 38 = verb-form licenses the modal reading, so @1470's 38-gate is cleared at battery grade. (26's own branch adjudication remains with the noun-26 thread.)

## Follow-ups proposed

1. `val-38-verb` (P3) — name 38's verb value. Bar: the value must license finite-3sg @1113 ("[65] [V] pas cela") AND past-participle @826 ("c'est [pp]") — i.e. a syncretic verb (cf. "dit": "il dit" / "c'est dit") or a stated form alternation. If no French verb covers both frames, re-open the fenced split.
2. `w4-38-1343-revisit` (P4) — re-test fenced W4 once 52's class and 86's class resolve; the "qui [52-adv] [38-V] ce" parse is one "ce"-as-object license away from parsing.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/noun26-38-profile.lock` created on start, deleted on completion.
- Queue update: temp-file + rename on `battery-queue.json`, own entry only; pre-write assert confirmed queued/verdictless; JSON re-validated after write.
- No standing verdict contradicted or downgraded. No red-team escalation needed (no contradiction with a red-team verdict found).
