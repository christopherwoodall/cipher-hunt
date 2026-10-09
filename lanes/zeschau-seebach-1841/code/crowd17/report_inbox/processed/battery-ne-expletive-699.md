# Battery verdict: ne-expletive-699

- Target: `ne-expletive-699` (battery-queue.json, priority 3, status queued)
- Claim: "test expletive-'ne' at @699"
- Bar (verbatim, pre-registered): "name the licensed governor among @694-698 (02/50/28 all open) with stated values, or fence the expletive arm."
- Numbered clauses:
  - C1: Name a licensed expletive-'ne' governor among {02@695, 50@696, 28@698} with stated values.
  - C2: Fence the expletive-'ne' arm at @699 with stated cause.

## Method

1. Re-derived the repaired parse in-session (1,847 pairs / 96 types; asserts held). Never used `canonical.py`. R5005 not touched.
2. Byte-confirmed the locus and a ±20 window; checked for 30 ('pas') in the clause.
3. Adopted standing values (not re-litigated): 46='que', 45='ce', 39='a/à' (LEAD), 94='ne' STRONG LEAD (R17-001); @699 already classified clean verbal-negator ("28 ne [60-V] 12", ne-94-right-context PROMOTE).
4. Corpus structural test: 98 files / ~59M chars of 1841 French (code/side-period/corpus/). Census of bare-'ne' (no pas/point/jamais/plus/guère/rien/personne in +6 tokens) expletive frames: licenser inventory = matrix fear verbs (craindre/redouter/appréhender/trembler), prevention (empêcher/éviter, prendre garde), affirmative doubt (douter), 'avant (que)', comparatives (plus/moins/mieux/autre…). Recorded licenser position relative to the governing 'que'.

## Window-level evidence

- Locus (row a5_01): `@694=46(que) @695=02(?) @696=50(?) @697=45(ce) @698=28(?) @699=94(ne) @700=60(?) @701=12(n) @702=98(verb)`. Full: "que [02] [50] ce [28] ne [60] n [98]…".
- No 30 ('pas') in @690–730: the negative/expletive question is not settled by a second negator.
- Candidate governors per the bar: 02 (n=17; "qui [02]"×2, "on [02]"×2, "[02] tout"×2), 50 (n=11; "la [50]"×2, "[50] ce"×2), 28 (n=6; "ce [28]"×2, "[28] pour"×3, "[28] ne"×1 = this window).

## Corpus result (structural)

- 2,531 bare-'ne' expletive frames with the licenser BEFORE the governing 'que' (matrix verb, 'avant', comparative).
- 48 apparent "licenser AFTER que (inside the ne-clause)" hits — hand-inspected, ALL false positives: infinitive negation ("craignait de ne pouvoir"), literary bare negation ("je ne saurais"), double-'que' misparses ("craignaient … que il ne y eût" — licenser before the second 'que'), adverbial 'avant' ("avant elle … ne").
- True inside-clause licenser count: **0 / 2,531**.

## Per-clause verdict

- **C1 FAIL.** All three candidates sit AFTER the governing 'que' (@694), i.e. inside the ne-clause — a position where expletive licensers occur 0/2,531 in the corpus. Positions are fixed; no future value naming moves 02/50/28 outside the clause. Per-candidate: 02-as-fear-verb dies on position (a licenser cannot govern its own clause's 'que'); 50-as-'peur' needs "de peur que" order (peur before que); 28-as-prevention-verb needs a second 'que' after it (none in @695–760). No stated-values assignment satisfies the bar.
- **C2 FIRES.** The expletive arm at @699 is fenced. Matrix alternatives checked and dead: fear/prevention/doubt verbs require bare "que … ne" but the matrix has "à [74] que" (@692–694) — the "à" breaks every licenser frame; no comparative in the matrix (@690–693 = 60 03 à 74); "avant que" would need "à [74=avant] que" (ungrammatical). The one theoretical opening, "à moins que" via 74='moins', is value-speculative: "39 74 46" is a stream hapax (@693 only), 74 is class-open with zero 'moins' legs — naming it would be single-window value invention, not battery grade.

## Verdict: NULL (fence executed)

The expletive-'ne' reading at @699 is fenced with stated cause (structural impossibility of an in-clause governor, corpus 0/2,531). The 'ne' stands as the negative verbal negator per the standing census (ne-94-right-context PROMOTE, clean window). No standing/red-team verdict contradicted or downgraded; §7 intact; canonical-stream caveat stands.

## Follow-ups proposed (nulls regenerate work)

1. `moins-74-test` (P4) — name-or-fence 74='moins' at @693: the only unclosed expletive path ("à moins que"). Bar: ≥2 independent 'moins' legs with zero kill-grade contradictions, or fence the 'moins' arm.
2. `ce28-697-subject` (P4) — resolve "ce [28]" @697–698: if 45='ce' is the ne-clause subject, it hardens the negative-negator parse ("ce [28] ne [60]"). Bar: subjecthood named with stated values or fenced.
3. `mood-60-700` (P4) — 60's mood at @700: expletive 'ne' requires subjunctive; an indicative 60 kills the expletive arm finally (including the 74='moins' path). Bar: mood named at battery grade or fenced as unresolvable.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-ne-expletive-699.md`
- Queue: `ne-expletive-699` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique temp file `battery-queue.json.ne-expletive-699.tmp` + atomic rename; disk re-validated; own entry only; no downgrade).
- Lock `locks/ne-expletive-699.lock`: created on start (agent 3e24e7a1, 2026-10-09T19:18:58Z, no stale lock), deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
