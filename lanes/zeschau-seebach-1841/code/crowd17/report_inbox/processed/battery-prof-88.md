# Battery report: prof-88 — name 88's class (n=23), unblock W1's left edge

- Target id: `prof-88` (priority 3)
- Claim: "name 88's class (n=23) with >=2 frame-legs; unblocks W1's left edge (`29 88 37` @619–621)."
- Date: 2026-10-09
- Lock: `locks/prof-88.lock` created on start, deleted on completion (verified gone).
- Stream: re-derived in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`. Asserts held: 1,847 pairs, 96 types. n(88)=23 confirmed. `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.

## Bar (verbatim from battery-queue.json, copied before any window analysis)

"class assigned iff >=2 independent frames parse under one class with zero hard contradictions; else fence as residual."

## Numbered clauses (fixed before testing, not modified after seeing data)

- **C1:** ≥2 independent frames parse under ONE class for 88.
- **C2:** zero hard contradictions of that class across all 23 windows.
- **Verdict rule:** promote iff C1 and C2 pass AND all adverses answered (adverses: none recorded); else fence as residual (null).

## Method

Full n=23 census re-derived byte-exact (0-based indices): @42, @86, @210, @304, @306, @334, @402, @497, @513, @616, @619, @646, @730, @765, @904, @1049, @1117, @1260, @1267, @1514, @1541, @1706, @1727. Each window was tested against verb-class (infinitive and finite arms) using standing values only: banked GT (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce); provisional (59=est, 77=le); battery-grade 94='ne' (STRONG LEAD R17-001), 24='faire', 45='ce' (HOLD A11), 39='à' (infinitive frame).

Prior batteries used as premises only (not re-litigated): governor-88-value (2026-10-08, PROMOTE: 88=VERB-CLASS, no value), finiteness-88-86 (PROMOTE: 88@86 finite transitive verb-governor), noun-88-subject (KILL: plural-noun 88 killed at @1117/@496), verb88-26-stem (KILL: uniform vient/tient-family stem killed), 88-prep-rival (PROMOTE: preposition rival killed, six verb frame-legs), ce88-pronoun-frame (PROMOTE: "88 le X" transitive frame).

## Findings

### C1 — six independent verb frame-legs (each re-verified on bytes)

1. **"[88]er" — @1049 (a6_04):** "41 88 29 40" — 88 directly bears 29='er' (banked GT), the infinitive ending on the 88 stem. Verb-deciding, unconditional on open values.
2. **"à [88]" infinitive — @765 (a5_03), @1727 (a8_07):** @765 "59 39 88 66" = "est à [88-inf]" (passive-infinitive construction); @1727 "98 39 88 24" = "vient à [88-inf]". After "à", 1841 French licenses an infinitive — not a bare noun (needs an article) and not a preposition ("à [prep]" ungrammatical).
3. **"ne [88]" — @1706 (a8_06):** "62 94 88 26" = "[62-il] ne [88-verb] …" (the (c1) loophole closure from nepas-20-adverb-gate: "il" is a subject pronoun; the only licensed parse of "62 94 88" is "il ne [88-verb]"). Conditional on the standing 94='ne' lead.
4. **"faire [88]" — @42 (a1_01):** "24 88 43" — causative "faire" takes an infinitive complement; "faire [preposition]" ungrammatical. Conditional on battery-promoted 24='faire'.
5. **"la [88]" nominalized infinitive — @1117 (a6_07):** "11 88 70" = "la [88]" — "le/la + infinitive" grammatical in 1841 French ("le boire"); noun-88-subject's kill shows "la" + plural noun is agreement-dead, while the infinitive arm parses cleanly.
6. **"ce [88]" — @402 (a2_08):** "45 88 53" — demonstrative-pronoun subject + finite verb grammatical ("ce semble"); conditional on the A11 45='ce' HOLD.

**Governor frame (reinforcing, counted as a seventh leg):** "88 le X" transitive-object frame at @86 ("06 88 77 66" = "[06-ent] [88] le [66]"), @646 and @1541 (byte-identical "88 77 78" trigram x2 stream-wide, re-verified: `88 77 78` @646 == `88 77 78` @1541; n("88 77")=3 total). All show 88 governing a post-verbal 'le'-headed object NP under provisional 77='le'.

**C1: PASS** (seven legs; bar requires two).

### C2 — hard-contradiction sweep across all 23 windows

- **Verb-compatible clean:** @42, @86, @402, @616 (@616 is 70='pre' prefix zone — analytic, not word-level), @646, @765, @1049, @1117, @1541, @1706, @1727 (11 windows).
- **Multi-open, no contradiction:** @210 ("pas [88-inf]" conditional on 50), @304/@306 (89 verb-frame; 02 open; non-finite required — verb fits), @334 (54 open; "[88]e" inflection on a verb stem is grammatical), @904 (16 open), @1260/@1267 (69 open), @1514 (81 open; "à [88-inf]" conditional), @730 (48='e' letter zone — analytic), @619 (see W1 below), @497 (79-split open; "tout" pronoun + finite verb parses: "tout [88-verb] [47=ce]").
- **@513 (fenced, not a kill):** "62 94 64 98 65 88 56" = "…qui vient [65-noun] [88] [56]". Under verb-88 the "vient à/de + inf" frame is blocked by 65, but a clause boundary after 65 lets 88 open a new clause as finite verb — grammatical under verb-class. The strain localizes to 65's slot (per 88-prep-rival), not to 88's class. No hard contradiction.
- **Zero windows force 88 non-verbal at kill grade.** The noun class is kill-grade dead (noun-88-subject); the preposition rival is kill-grade dead (88-prep-rival); no uniform VALUE can be named (verb88-26-stem), but the bar asks for CLASS, not value.

**C2: PASS.**

### W1's left edge (@619–621, 0-based @619)

Bytes: `70 88 10 29 88 37 76` (@615–621, spanning a4_00/a4_01). With 88 assigned VERB-CLASS:
- @616 (70='pre' prefix zone) is analytic — word-internal/analytic composition, not word-level; no class test applies.
- @619 ("29 88 37"): with 88 a verb stem, the noun/preposition/adjective arms are fenced out. The live shapes are (a) word-internal "[...]er[88]-" composition with 37 predicative, or (b) a new verb phrase "…er ‖ [88-verb] [37-pred]…" (37 is a granted predicative frame, A1). The exact segmentation stays residual — this battery does not promote a specific parse.
- The class assignment unblocks W1's left edge by eliminating the class question: 88 at @620 (1-based @620 = 0-based @619) is verb-stem, whatever its word boundaries.

## Adverses

None recorded in the queue entry. The standing counter-evidence ("est a [88]", "88 le" x3 being "noun-compatible") is answered by prior batteries and re-confirmed here: both are verb legs (legs 2 and 7 above), not noun legs. §7 sole-polyvalence is not invoked or extended — infinitive vs finite is normal verb morphology.

## Per-clause results

- C1 (≥2 independent frames under one class): PASS (7 legs).
- C2 (zero hard contradictions): PASS.
- Adverses: none; answered where prior counter-evidence existed.

## Verdict: PROMOTE

**88's class is assigned: VERB (verb stem / verb-governor)** at battery grade, with seven independent frame-legs and zero hard contradictions across all 23 windows. No VALUE is named (verb88-26-stem's kill of the uniform vient/tient-family stem stands untouched; the locus-level @1706 fused-3pl package stays red-team venue). W1's left edge is unblocked at the class level: @619's 88 is verb-stem; its exact segmentation remains residual. Consistent with governor-88-value, finiteness-88-86, 88-prep-rival, ce88-pronoun-frame, and noun-88-subject's kill (used as premises, none downgraded). No standing red-team verdict contradicted; §7 intact. Ratification is red-team venue like all battery promotes.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-prof-88.md` (this file).
- Queue: `battery-queue.json` `prof-88` queued → verdict/promote, date 2026-10-09 (pre-write assert: queued, no prior verdict; temp-file + rename; JSON re-validated; own entry only).
- Lock: `locks/prof-88.lock` created on start, deleted on completion (verified gone).
- `canonical.py` never used; R5005, sealed gates, red-team adjudication queue untouched.
