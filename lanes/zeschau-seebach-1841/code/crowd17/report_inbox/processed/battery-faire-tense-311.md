# Battery report — faire-tense-311 — VERDICT: PROMOTE (fenced)

Worker: subagent session 030e8b96 (seebach battery).
Date: 2026-10-09. Target: `faire-tense-311` (priority 3).

## Claim

"if 24='faire' survives, decide finite 'fait' vs infinitive/participle at @311/@473 via contact profile"

## Bar (verbatim, pre-registered before testing)

"CONDITIONAL on 24='faire' LEAD (do not run if the LEAD dies): decide between finite 'fait' (which tense?) / infinitive 'faire' / participle 'fait' at @311/@473; test whether finite 'fait' governs [37-predicative][78]; 1841 diplomatic French only"

## Bar restated as numbered clauses (not modified after seeing data)

- **c0 (gate):** The 24='faire' LEAD survives (battery or red-team grade). If dead, do not run.
- **c1:** Infinitive 'faire' at @311/@473 — pass iff a grammatical 1841-French infinitive parse of the windows is licensed; kill iff the windows force it false.
- **c2:** Past participle 'fait' at @311/@473 — same test.
- **c3:** Finite 'fait' at @311/@473 — the surviving arm; name the tense.
- **c4:** Finite 'fait' governs [37-predicative][78] — the contact profile supports 24 governing the 37-78 frame.

## Method

1. Read BATTERY-PROTOCOL.md in full; created `locks/faire-tense-311.lock` (agent id + UTC 2026-10-09T18:54:09Z) on start. No pre-existing fresh lock for this id.
2. Copied the bar verbatim from `battery-queue.json` before seeing data; restated above.
3. Re-derived the repaired stream in-session (`repair_parse.py` byte-exact tokenization over `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`): **1,847 pairs / 96 types asserted**. Never `canonical.py`. Never touched R5005.
4. Exhaustive census (not sampled): every `84 24 37 78`, `24 37`, `84 24`, `37 78`, and 24/78 contact profile, re-derived from the bytes.
5. Standing premises used, not re-litigated: 46='que' (banked), 84='on' (A15 granted; R17-009 reads these exact windows as "qu'on 24" subordinate slots), 37=predicative frame (A1 granted), 17='fois' (promoted), 87='ce' (granted A4), 45='ce' (A11 hold), 00='pour' (A9), 59='est' (provisional), 77='le' (provisional), 78='ver' LEAD (R17-021, nominal).

## Indexing note

On the 0-based repaired stream the twin windows start at @310 and @473; 24 sits at @311 and @474. The target names 24's index in window 1 and the window start in window 2. Both windows are byte-identical `84 24 37 78`.

## Window-level evidence (bytes, repaired stream)

- W1 @307–@319: `20 17 46 84 24 37 78 45 64 59 32 94` → "[X] fois que | on | 24 | [37-pred] | 78 | ce | qui | est | [32] | ne"
- W2 @470–@482: `06 67 46 84 24 37 78 74 45 93 00 13 52` → "[06] et | que | on | 24 | [37-pred] | 78 | [74] | ce | [93] | pour | [13] | [52]"
- `84 24 37 78` occurs **exactly twice** stream-wide: @310, @473. Exhaustive.
- `24 37` occurs **exactly twice**: @311, @474 — both inside the twin windows. Exhaustive.
- `84 24` occurs 3x: @310, @473, @1485 (`84 24 87 08`, different follower family — fenced out of the frame, consistent with verb arm under R24).
- `37 78` occurs 4x: @312, @414 (`53 84 51 37 78 49…`), @475, @1770 (`87 64 26 37 78 62…`). The @414 and @1770 contacts are governed by 51 and 26 respectively — the [37][78] frame is reusable independent of 24.
- 24 census: n(24)=52. Followers: 87 x10, 85 x5, 82 x4, 30 x3, 89 x3, **37 x2**, 80 x2. No follower is an auxiliary-shaped or subject-shaped token at the twin windows.
- 78 contact profile (n=31): preceders 77 x7 ('le' provisional), 47 x5, 37 x4, 67 x4, 11 x2 — nominal/determiner-shaped, zero verb readings; followers 45 x4, 40 x3, 48 x2 — consistent with R17-021 78='ver' nominal LEAD. No 78 window supports a verb reading.
- R24 check at both windows: follower of 24 is 37, not 85 → **verb arm** (not the 'en' arm). No 94 ('ne') contact in either window → **non-lone-ne** windows.

## Per-clause results

### c0 — PASS (narrowed survival, recorded honestly)

R19-191 (red-team, 2026-10-09) killed the GLOBAL 24="faire"/"laisser" value at kill grade (@162/@1774 lone-"ne": "ne fait"/"ne laisse" without "pas" ungrammatical in 1841 French) and NARROWED R18-008's lead: 24="faire" survives **only as a value-candidate for verb-arm non-lone-ne windows**. My windows qualify on both tests: follower 37 ≠ 85 (verb arm under R24) and no 94 contact (non-lone-ne). The conditional is therefore satisfied in its narrowed, red-team-ratified form. (My task brief's evidence context predates R19-191; the narrowing is noted, not hidden.)

### c1 — FAIL AT KILL GRADE (infinitive 'faire' dead at both windows)

Frame: `46 84 24` = "que on 24" — overt subject pronoun directly before the verb slot, finite complementizer "que". In 1841 French exactly as in modern French, an infinitive cannot take an overt nominative subject; overt-subject infinitives are licensed only under prepositional government (pour/de/à) or perception-verb AcI. "que" is neither. "que on faire [pred]" is ungrammatical. The byte-identical contact kills the arm at both windows. (Attack considered: 84 as verb-syllable à la the @1188 -este rival reading — rejected: no verb stem precedes 84 here; @308=17='fois' promoted noun, @309=46='que' banked.)

### c2 — FAIL AT KILL GRADE (participle 'fait' dead at both windows)

A past participle requires its auxiliary immediately governing it; none stands between subject 84 and 24 (24 sits directly post-subject). Participial absolutes ("ceci fait") are subjectless — an overt subject "on" with a bare participle and no auxiliary is ungrammatical in 1841 French. "que on fait [pred]" reads as participle only by ignoring the subject. Kill grade at both windows.

### c3 — PASS (finite arm survives; tense = present indicative)

With the infinitive and participle arms dead at kill grade and the verb slot forced (only post-subject slot before the predicative frame; predicative 37 must follow its verb), 24 at @311/@474 is finite. Under the c0-narrowed 24='faire' value-candidate the finite surface form named by the bar is **'fait' = present indicative 3rd singular** ("qu'on fait [pred]") — the only finite spelling of faire realized as 'fait' (passé simple is "fit", imperfect "faisait", subjunctive "fasse"). No window discriminates a rival finite spelling; none is named by the bar.

FENCED TENSION (not a clause failure): @307 = `20 17 46` = "[X] fois que" with 20's value unresolved (20='fois' killed; split 20~17 holds; tense-24-307 nulled on exactly this). If 20 resolves to "une", a completed-tense subordinate verb is required and present "fait" would be ungrammatical; if "chaque", habitual present is licensed. 20's value is outside this bar's venue — fenced to the 20 battery, not ignored.

### c4 — PASS (finite 'fait' governs [37-predicative][78])

- Direct government: `24 37` occurs exactly 2x stream-wide, both at the twin windows — the 24→37 contact is exclusive to this frame.
- Frame reusability: `37 78` occurs 4x; the two non-24 contacts (@414 governed by 51, @1770 governed by 26) show [37][78] as a productive predicative+nominal frame independent of 24 — exactly what a governing verb would select.
- 78 is nominal-shaped (determiner preceders, R17-021 'ver' LEAD), i.e. a governable nominal, not a verb that could host or block government.
- Grammaticality: "faire" + predicative adjective + nominal object is licensed 1841 French ("faire bon accueil", "faire grand cas"). Nothing in either window contradicts government; the 24→37→78 chain is the only licensed parse of the post-subject span.

### Adverses

None listed on the target. Fenced rival noted: 'laisser' remains the live rival value-candidate per R18 (narrowed same as 'faire'); the bar's arms are faire-internal, so 'laisser' is out of venue — fenced, not ignored.

## Verdict: PROMOTE

All five clauses pass (c1, c2 fail-at-kill-grade = the arms die as the bar requires; c0, c3, c4 pass), no adverses listed. Promoted claim, fenced: **24@311/@474 = finite 'fait' (present indicative) under the R19-191-narrowed 24='faire' value-candidate (verb-arm, non-lone-ne windows), governing [37-predicative][78]**; the @307 "[X] fois que" completed-vs-habitual tension is fenced pending 20's value; the 'laisser' rival is fenced out-of-venue.

## Null follow-ups

None required (verdict is promote, not null).
