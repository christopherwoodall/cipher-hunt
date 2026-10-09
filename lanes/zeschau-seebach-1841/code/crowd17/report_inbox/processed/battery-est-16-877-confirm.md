# Battery report: est-16-877-confirm

- Target id: `est-16-877-confirm`
- Claim: re-test @877 once 77's value is decided; if 77='le' holds, "[49] a le" becomes forced contradiction of 16='a'.
- Date: 2026-10-09
- Worker: battery worker (subagent 063b7038-82b2-4388-bc32-0409c8af9b57)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`), re-derived in-session; asserts held (1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Parent: `val-16-a-vs-est` (null, 2026-10-09) follow-up #3.

Terms (ASD-STE100): "forced contradiction" = no grammatical parse survives under the tested value, so the value is impossible at the window. "provisional" = lane-standing tier below promote (protocol §7: 77='le' is provisional). "article le" = "le" as determiner before a noun ("le livre"). "pronoun le" = "le" as object pronoun, which must precede the verb ("il l'a", never "*il a le"). "nominalized infinitive" = an infinitive used as a noun with an article ("le vouloir").

## Bar (verbatim, pre-registered before testing)

"conditional on 77='le' holding"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** 77='le' holds — at least at provisional standing (the bar's condition).
2. **C2:** Given C1, "[49] a le" is a FORCED contradiction of 16='a' at @877: no grammatical parse survives under 16='a', while 16='est' survives.

Adverses (queue): "currently conditional on provisional 77='le'" — answered by the C1 standing check below.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/est-16-877-confirm.lock` on start; deleted on completion.
2. Re-derived the repaired stream in-session (asserts 1,847 pairs / 96 types). All @-offsets below are 0-based repaired-stream pair indices (queue convention).
3. Checked 77's standing: registry `77 -> ['le', 'prov']`; protocol §7 provisional; `le-77` battery returned NULL (2026-10-09, did not kill the value); `le-77-residual-adjudicate` is queued for red-team decision, undecided.
4. Checked neighbors: registry `86 -> ['INF', 'cls']` (infinitive class); `78 -> ['ver', 'lead']`; 49 and 74 unvalued; 17='fois' promoted; 89 verb-frame (A8); 48='e' promoted.
5. Tested 16='a' vs 16='est' at the locus under both functions of 77 (article, pronoun), adopting only standing values.

## Window-level evidence

- **Locus byte-confirmed:** 0-based @875–877, row a5_08: `49 16 77`.
- Wider window @871–880: `89 48 20 74 | 49 16 77 | 86 78 17` = "…[89]e [20] [74] [49] [16] le [86-INF] [78] fois…".
- The claim's frame is "[49] [16] le [86]": under 16='a' → "[49] a le [86]"; under 16='est' → "[49] est le [86]".
- 16's standing class is infinitive (promote `gate-satisfiability-16-85`, §5-protected, not re-litigated); the 'a'/'est' refinement is the parent's value dispute, tested here as framed.

## Per-clause pass/fail

- **C1 — PASS.** 77='le' holds at provisional standing: registry `['le','prov']`, protocol §7 provisional tier, `le-77` NULL did not kill it, red-team adjudication queued but undecided. The bar's condition is met.
- **C2 — FAIL at kill grade.** "[49] a le" is NOT a forced contradiction of 16='a'. Three independent blockers:
  - (a) The parent's "a le → l'a" argument requires 77 to be the **object pronoun** at @877. 77's function there is undecided, and the **article reading is available**: "le" + 86 as a nominalized infinitive ("le vouloir"-shaped) is grammatical 1841 French, which rescues "a le [86]" from the pronoun-order rule. A forced claim admits no grammatical rescue.
  - (b) Under the pronoun reading, the argument is **symmetric**: "*est le" is just as ungrammatical as "*a le" with a post-verbal object pronoun. The window then cannot discriminate 'a' vs 'est' — at most a universal residual, never a contradiction of 'a' specifically.
  - (c) The argument additionally needs **49 as subject** — ungranted. 49 is unvalued (registry None); its dominant "49 74" x5 frame is open (`val-49-74-frame` queued).
  - As bare bigrams, both "est le" ("c'est le…") and "a le" ("il a le temps") are grammatical French sequences; the only asymmetry is idiomatic, not grammatical, and cannot carry a "forced" verdict at battery grade.

## Verdict: KILL

The conditional claim — "[49] a le" **becomes a forced contradiction** of 16='a' — is false at battery grade. The bar's condition (77='le') holds at provisional tier, but the consequent does not follow: the contradiction is not forced under any consistent assignment of 77's function.

**Scope:** kills only the forced-upgrade. Untouched: 77='le' provisional, the standing 16=infinitive promote (§5), and the parent's original weak conditional signal toward 'est' (which stands as weak/conditional only, not forced). No standing or red-team verdict contradicted or downgraded; §7 intact (67 sole polyvalence; no new polyvalence declared). Canonical-stream caveat stands (row a5_08 offset unvalidated).

Per §4, kills regenerate no follow-ups.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-est-16-877-confirm.md` (this file).
- Queue: `est-16-877-confirm` → status `verdict`, result `kill`, 2026-10-09 (pre-write assert passed — was `queued`/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/est-16-877-confirm.lock`: created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
