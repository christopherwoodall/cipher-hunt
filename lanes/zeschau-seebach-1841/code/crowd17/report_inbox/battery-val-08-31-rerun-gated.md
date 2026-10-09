# Battery report: val-08-31-rerun-gated

- Target id: `val-08-31-rerun-gated`
- Claim: gated re-fire of this target's bar once val-08-31-letter names 08's letter (or val-31-verb-test/val-31-1515-noun names 31's value): name the [08][31] word then.
- Date: 2026-10-09
- Worker: battery worker (subagent b7532b25-624d-4d71-8e48-f089b2868222)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.

Terms (ASD-STE100): "battery grade" = the evidence standard of this pipeline. "fence" = the question is closed at battery grade with a stated cause; it re-opens only on the stated condition.

## Bar (verbatim, pre-registered before testing)

"word named at battery grade with ≤1 remaining ungranted assumption, or fence again with stated cause."

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1 (name):** the [08][31] word is named — one specific French word — at battery grade with ≤1 remaining ungranted assumption.
2. **C2 (fence):** else the naming is fenced with a stated cause (which assumption fails, and what would re-open it).

Adverses listed: none.

## Gate check

Gate fired as briefed. `val-08-31-letter` → verdict PROMOTE on 2026-10-09 (report `code/crowd17/report_inbox/processed/battery-val-08-31-letter.md`): **08='t'** named with 7 independent spelling legs (L1–L7), all rivals dead. 08's letter is no longer open.

## Method

1. Read `BATTERY-PROTOCOL.md` first. Created `code/crowd17/next-token/locks/val-08-31-rerun-gated.lock` on start (agent id + 2026-10-09T21:24:00Z); no prior/stale lock; deleted on completion.
2. Re-derived the repaired stream byte-exact in-session (1,847 pairs / 96 types asserted). All @-offsets below are 0-based.
3. Adopted, never re-litigated: pencil GT (11=la, 34=i, 29=er, 40=e, 46=que); 87=ce (granted), 17=fois (granted), 79=tout (A5), 00=pour (A9), 67 et/veut positional rule (§7); `ce-08-31-frame` PROMOTE ([08][31] is one word, 08 word-initial letter); `word-class-08-31-3frames` PROMOTE (W jointly NOMINAL noun/adjective; 31's banked VERBAL class is cell-tier and does not project to the word head); R20-090; 08='t' (battery, today).
4. 31's standing: registry `31=['VERBAL','cls']` (class only, no value); `val-31-verb-test` → NULL (2026-10-09); `val-31-1515-noun` → KILL (2026-10-09, noun arm dead). **31's value is open.**

## Window-level evidence (byte-exact, 0-based)

The "08 31" bigram is 3× stream-wide (re-confirmed in-session); n(31)=8.

- **W1 @881:** `...86 78 17('fois') [08] [31] 79('tout') 68 37 03 02 00 86...` — "fois t[31] tout [68]". Favors adjective ("fois [adj]" on the "fois dernière" pattern) or a clause boundary with nominal W (adopted from word-class-08-31-3frames).
- **W2 @1488:** `...24 87('ce') [08] [31] 92 39 24 00 66 15 59...` — "que l'on [24-fin] ce t[31] [92-verb]…". Determiner-headed NP slot; "a bare adjective cannot head that slot", so W is noun here (adopted).
- **W3 @1520:** `...11('la') 91 67('et') [08] [31] 24 11 11 48...` — "la [91-nominal] et t[31] [24-fin]…". Coordinated nominal; W is noun here (adopted).

Joint standing: W is a **t-initial nominal** (noun/adjective), one cipher word across all three windows.

## Naming attempt

With 08='t' banked, the word is "t" + (31's value). Naming it requires 31's value (1 ungranted assumption) AND a unique selection among t-initial nominals fitting all three frames.

Candidate space (t-initial French nominals): dozens of nouns (temps, texte, ton, tour, toit, tort, travail, train, trait, trésor, trou, type, tableau, théâtre, timbre, titre, tombe, torrent, trace, tradition, traité, tribunal, troupe, tunnel, …) and noun/adjectives (tel, triste, traître, travailleur, tricheur, timbré, toqué, têtu, …).

No convergence at battery grade:

1. **F2/F3 force noun; F1 does not force the same word.** F1 ("fois W tout") is structurally ambiguous between an adjectival W and a clause boundary with nominal W. The frames therefore do not jointly isolate one word: any t-initial noun fits F2/F3, while F1's adjective arm points at a different (t-initial adjective) candidate set.
2. **31's value gives no phonetic traction.** 31 is open; its standalone verbal windows ("qui 31" ×2, "la 31" ×1) did not yield a value (val-31-verb-test NULL). There is no battery-grade "t"+X word-shape to test.
3. **Counting assumptions:** naming needs (a) 31's value, (b) selection of one candidate among dozens, (c) resolution of F1's structural ambiguity. That is ≥2 ungranted assumptions (b and c are independent of a). The bar allows ≤1.

Selecting any single word (e.g. "temps", "travail", "texte") would be parsing, not naming — no frame eliminates the rivals.

## Per-clause pass/fail

- **C1 (name) — FAIL.** No unique t-initial nominal is forced by the three frames; naming needs ≥2 ungranted assumptions against the bar's ≤1.
- **C2 (fence) — FIRES.** The [08][31]-word naming is fenced (evidentiary): the word stays a t-initial nominal (noun/adjective) with 31's value open.

## Verdict: NULL (fence executed)

The gate fired (08='t' banked) but the word cannot be named at battery grade within the bar's assumption budget.

**Stated cause:** 31's value is open AND the t-initial nominal candidate space does not converge on one word across the three frames (F1's adjective-vs-clause-boundary ambiguity points at a different candidate set than F2/F3's noun demand).

**Re-opens iff:** 31's value is named (then "t"+value is a dictionary check, 0 further assumptions), or a corpus census shows exactly one t-initial nominal occurring in all three frame shapes in 1841 French.

## Scope

- Names nothing; 08='t', the [08][31]-word geometry, and W's nominal class are adopted, not re-decided.
- 31's value/class untouched (open VERBAL/cls stands).
- No standing or red-team verdict contradicted, downgraded, or re-litigated; §7 intact.
- Canonical-stream caveat stands (rows a5_08/a7_10/a7_11 offsets unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json, left for supervisor)

1. `val-31-syllable-value` (P4) — name 31's phonetic value/syllable. Direct blocker: "t"+31's value reduces the word to a dictionary check.
2. `t31-frame-corpus` (P4) — corpus census of t-initial nominals in the three frame shapes ("fois [t-*] tout", "ce [t-*]", "[det] [N] et [t-*]") in 1841 French; a unique triple-frame attestation would name the word empirically.
3. `f1-881-structure` (P4) — resolve F1's "fois W tout" structure (adjectival W vs clause boundary with nominal W). Determines whether W must be adjective-capable, cutting the candidate space.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-08-31-rerun-gated.md` (this file).
- Queue: `val-08-31-rerun-gated` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; see below).
- Lock `code/crowd17/next-token/locks/val-08-31-rerun-gated.lock` created on start (2026-10-09T21:24:00Z, no stale lock), deleted on completion (verified below).
- R5005, sealed gates, red-team adjudication queue untouched.
