# Battery report — laisser-unique-sweep (with porter+envoyer eliminated, 'laisser' is the unique surviving -er candidate)

Worker: battery-worker-laisser-unique-sweep (session 015a3828-0ef0-4e43-bb15-8864b224ee74). Date: 2026-10-09.
Lock: `code/crowd17/next-token/locks/laisser-unique-sweep.lock` created 2026-10-09T17:57:58Z, no prior lock existed; deleted on completion.
Stream: repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`), parsed per `code/side-keyhunt/repair_parse.py` (replicated, not `canonical.py`; asserts held: 1,847 pairs, 96 types). R5005 not touched. Sealed gates and red-team adjudication queue untouched.

Gate: SATISFIED — R19-188 (red-team round 19) RATIFY'd the porter+envoyer eliminations: "@1477-0b re-derived ('veut [33]er m[16] vient'): post-infinitive clitic after non-causative -er verb kill-grade ungrammatical under every 16-class; envoyer ditransitive not causative; erstem-33-id vs x-33-laisser-test tension resolved on word order. 'laisser' unique among TESTED candidates (value not promoted here). Condition: kills assume the standing '82 16'='m''+verb segmentation (a word-internal re-segmentation re-opens @1477)."

## Bar (pre-registered verbatim, from task brief)

`(a) re-check erstem-33-id's full candidate list against the @1477 kill (donner/montrer/prouver/trouver/porter/envoyer/prononcer); (b) confirm 'laisser' uniquely survives with byte evidence.`

(Numbered clauses, pre-registered BEFORE testing, not modified after.)

1. Clause (a): each of donner / montrer / prouver / trouver / porter / envoyer / prononcer dies at the @1477 "veut [X]er m[16]" frame at kill grade, 16-class-independent.
2. Clause (b): 'laisser' is confirmed as the unique surviving -er candidate with byte evidence; no other -er verb parses all 5 stem windows.

Note: the queue's bars text adds "confirm no new -er candidate parses all 5 windows" — covered by clause (b) via the causative-class filter below.

## Method

Re-derived the repaired stream in-session. Re-derived all five `33-29` stem windows byte-exact (identical set to erstem-33-id / rival-porter-envoyer). Re-tested each of the 7 candidates against the @1477 discriminator frame under 1841 French grammar and the standing values (§7): 29="er", 82="m" (banked), 87="ce" (promoted), 84="on" (A15), 47="ce" (A4 allophone tier), 67 et/veut positional rule, sole-polyvalence law. Ran an independent period-corpus check (56 French files, 29,487,677 chars; German allgemeine-zeitung/adb-zeschau/metternich files excluded) for post-infinitive clitic placement after -er verbs, with hand-verification of every hit. Verified the R19-188 condition (standing "82 16" segmentation) against battery-frame-82-16 (null, 2026-10-09).

## Window-level evidence (@-offsets are repaired-stream pair indices, re-derived this run)

Five `33-29` stem windows, byte-exact:
- @273 (a2_03) `47 11 06 67 33 29 89 84 91` — "veut [X]er [89], on [91]"
- @626 (a4_01) `82 14 59 37 33 29 87 78 67` — "est [37] [X]er ce [78]"
- @1232 (a7_01) `82 48 29 47 33 29 85 56 10` — "[ce/se] [X]er [85] [56]"
- @1424 (a7_08) `15 33 21 67 33 29 87 63 91` — "dire [21], veut [X]er ce [63]"
- @1477 (a7_10) `53 60 06 67 33 29 82 16 98` — "veut [X]er m[16] [98]" ← the discriminator

The @1477 kill (re-derived, not cited): with 82="m" banked, the surface order is `[X]er` + clitic `m'` + `16`, i.e. a POST-INFINITIVE clitic. In French, post-infinitive clitic position is licensed only for the causative class and imperatives; for every non-causative verb the clitic must climb ("veut me [X]er"). The kill is 16-class-independent:
- 16 = infinitive → "veut [V]er me [inf]" ungrammatical for non-causative V;
- 16 = noun → "m'" + noun ungrammatical (82="m" banked forces vowel-initial 16);
- 16 = finite verb → clause broken.
The kill is also 67-polyvalence-independent: under 67="et" the frame is "et [X]er m[16]" — the [X]er+m[16] adjacency is unchanged.

### Clause (a): candidate-by-candidate at @1477

All seven are non-causative -er verbs; all die at @1477 under every 16-class:

| candidate | class | @1477 verdict |
|---|---|---|
| donner | transitive, non-causative | DEAD — "veut donner me [16]" ungrammatical, 16-class-independent |
| montrer | transitive, non-causative | DEAD — same |
| prouver | transitive, non-causative | DEAD — same |
| trouver | transitive, non-causative | DEAD — same |
| porter | transitive, non-causative | DEAD — same (R19-188 ratified) |
| envoyer | ditransitive, non-causative | DEAD — "envoyer qqn [inf]" requires clitic climbing ("veut m'envoyer [16]"); observed post-infinitive order ungrammatical (R19-188 ratified: "envoyer ditransitive not causative") |
| prononcer | transitive/pronominal, non-causative | DEAD — "veut prononcer me [16]" ungrammatical, 16-class-independent |

Independent corpus confirmation (this run, 29.5M chars 1841 French): post-infinitive "me"/"moi" after these verbs = donner 1, montrer 0, prouver 1, trouver 0, porter 3, envoyer 0, prononcer 0, laisser 0 — and ALL 5 hits hand-verified as emphatic "moi-même" ("porter moi-même ce drapeau", "prouver moi-même au peuple", …), not the clitic+infinitive frame. Genuine "V(-er, non-causative) + me + INF" post-infinitive: **0/29,487,677 chars**. Pre-infinitive climbing ("me donner" 80, "me trouver" 47, "me laisser" 38, …) is the grammatical norm — the asymmetry is exactly what the kill predicts.

Clause (a): PASS — all 7 dead at kill grade, 16-class-independent, 85-independent (no gate can rescue any of them).

### Clause (b): 'laisser' uniquely survives

'laisser' parses all 5 windows (conditional on the two known open slots, unchanged from erstem-33-id):
- @273 "veut laisser [89], on" ✓ ("vouloir laisser" top collocate)
- @626 "[37] laisser ce [78]" ✓ (transitive)
- @1232 "se laisser [85] [56]" ✓ IF 85 = infinitive ("se laisser [inf]" idiomatic; 85 open, stem-85 null)
- @1424 "veut laisser ce [63]" ✓ (transitive)
- @1477 "veut laisser m[16] [98]" ✓ IF 16 = infinitive — laisser is causative-class, the only -er verb licensing V + me + INF order (cf. "laissez-moi passer")

Uniqueness (the extension beyond "tested candidates"): the @1477 frame admits ONLY causative-class verbs. The French causative periphrastic class is closed: {faire, laisser}. faire is not -er. Therefore 'laisser' is the SOLE -er verb that can occupy the @1477 frame — no untested -er candidate can survive it, by grammatical class membership, not by enumeration. This is consistent with (not contradicting) R19-188's "unique among TESTED candidates": the class argument closes the untested remainder.

Byte evidence for (b): the five windows above (re-derived); @1477's `67 33 29 82 16` adjacency; corpus 0/29.5M for the non-causative frame.

Clause (b): PASS.

### R19-188 condition check (the "82 16" segmentation)

R19-188's ratification is conditional: "kills assume the standing '82 16'='m''+verb segmentation (a word-internal re-segmentation re-opens @1477)". battery-frame-82-16 (null, 2026-10-09) finds 82-16 x11 = "m'a"/"m'est" (elided "me" + vowel-initial verb) and kills the "même"/"mais"/noun/infinitive alternatives at stated windows. NO battery has proposed a word-internal re-segmentation of "82 16". The condition holds; @1477 is not re-opened.

## Per-clause pass/fail

1. Clause (a) — all 7 candidates dead at @1477, kill grade, 16-class-independent: **PASS**.
2. Clause (b) — 'laisser' confirmed unique surviving -er candidate with byte evidence: **PASS**.

## Adverses disposition (from queue entry)

- "gated on rival-elim-ratify (red-team docket) - do not run before ratification": ANSWERED — R19-188 ratified; gate satisfied before this run.
- "coordinate with erstem-33-id (coordinate, do not duplicate its candidate sweep)": ANSWERED — consumed its candidate list and 5-window set; re-derived the stream, the windows, and the @1477 kill independently; added new evidence (29.5M-char corpus check with hand-verified hits; R19-188 condition verification against frame-82-16; causative-class closure argument). No duplication.

## Standing-verdict check

No contradiction with any standing verdict: §7 banked/promoted values, sole-polyvalence law, A4 (47="ce" tier), A10 HOLD (both 33 faces retained — this battery adjudicates the STEM face only; under the whole face 33="dire", "dire" is likewise non-causative, but that face is out of this target's scope), R19-188 (extended, not contradicted) all untouched. 16 and 85 unnamed by this worker. Canonicality caveat stands (row a7_10's offset unvalidated; under a re-pairing the @1477 window could dissolve — same caveat as all prior batteries on this locus).

Scope: this PROMOTES the candidate-elimination claim only. It does NOT name 33="laisser" as a value — that identification remains gated on 16=inf (frame-82-16) and 85=inf (stem-85), both open. Registry change: none (consistent with R19-188's "value not promoted here").

## Verdict: PROMOTE

Both bar clauses pass at battery grade with the R19-188 gate satisfied: all seven tested -er rivals are dead at the @1477 discriminator (kill grade, 16-class-independent, gate-independent), and 'laisser' is confirmed as the unique surviving -er candidate — extended from "tested" to "all -er" by the closed causative-class argument (faire/laisser; faire not -er), with 0/29.5M-char corpus confirmation that no non-causative -er verb takes the post-infinitive clitic frame.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-laisser-unique-sweep.md`
- Queue: `laisser-unique-sweep` → `status: verdict`, `verdict: {result: promote, ...}`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; own entry only; no downgrade)
- Lock created on start (2026-10-09T17:57:58Z, no stale lock), deleted on completion
- R5005, sealed gates, red-team adjudication queue untouched
