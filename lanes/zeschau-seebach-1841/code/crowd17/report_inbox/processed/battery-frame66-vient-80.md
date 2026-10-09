# Battery `frame66-vient-80` — verdict: PROMOTE

- Target id: `frame66-vient-80`
- Claim: test the "[66] vient [80]" clause completion at @766–768: 80's infinitive reading under the A8 verb-frame grant.
- Date: 2026-10-09
- Worker: battery worker (subagent ca2c05b3-5ffb-4f70-8340-638fbf35eac0)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). Verified in-session: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Parent: follow-up 2 of `val-66-767-frame` (verdict null, 2026-10-09).

Terms (ASD-STE100): "infinitive-shaped" = the cipher number fills a governed-infinitive slot (e.g. "vient [80]" = "[80]-to-V"). "Rival" = an alternative grammatical role for 80 at this window. "Battery grade" = the evidence standard of this pipeline.

## Bar (verbatim, pre-registered before testing)

> Bar: 80 infinitive-shaped at @768 with zero rivals -> the "[66] vient [80]" clause is complete, and the C3 frame-closure stands on a finished clause rather than a half-open one.

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** 80 is infinitive-shaped at @768 under standing values (A8 verb-frame grant + 98='vient' finite semi-auxiliary + 66 as its nominal subject).
2. **C2:** zero rivals — every non-infinitive reading of 80 at @768 is killed at battery grade.
3. **C3 (consequence):** the "[66] vient [80]" clause is complete, so the parent's C3 frame-closure stands on two finished clauses.

Adverses listed: none.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/frame66-vient-80.lock` on start (agent id + UTC timestamp); deleted on completion. No stale lock was present.
2. Re-derived the repaired stream in-session. All @-offsets below are 0-based.
3. Adopted premises (not re-litigated): 98='vient' finite semi-auxiliary (`vient-98-name` PROMOTE); 66 = nominal subject of 98 at @766–767 (parent `val-66-767-frame` C1/C2, window-level); A8 verb-frame grant for 80 (§7); 29='er' banked GT.
4. Notable: this locus sits on row **a5_03** — the pencil-gloss-validated row (gloss (i), "la pre m i er e"), so the canonical-stream caveat does not apply to this window.

## Window-level evidence (byte-exact)

- **Locus:** @765=88, @766=66, @767=98, @768=80, @769=10, @770=22 (row a5_03): `…39(à) [88] [66] [98] [80] [10] [22]…` = "…à [88-inf] [66-subj] vient [80]…".
- **"[98] 80" cluster:** exactly **3×** stream-wide — @441 ("43 98 80 50 78"), @768 (locus), @1662 ("98 98 80 22 94"). In all three, 80 sits immediately post-98. The infinitive reading gives a uniform parse across the cluster ("vient [80-inf]").
- n(80)=17 confirmed; predecessors {29 x4, 98 x3, 79 x3, 24 x2, 52 x2, 77/50/21 x1}; followers {06/03/77/04 x2, 50/09/97/10/78/17/08/67/22 x1}. "80 10" is a singleton — zero repetition leverage for any 80-10 unit reading.

## Per-clause pass/fail

- **C1 — PASS.** "[66-subj] vient [80]" parses as subject + finite 'vient' + governed infinitive under adopted premises: 98='vient' is finite (vient-98-name), French is not pro-drop so 66 supplies the subject (parent C1), and 'vient' + infinitive is the standard semi-auxiliary construction ("il vient manger"). 80 fills the infinitive slot under the A8 verb-frame grant. Zero new assumptions.
- **C2 — PASS. All rivals killed:**
  1. 80=finite — **KILLED** at grammar level: "vient [80-fin]" = two adjacent finite verbs. At @1662 ("98 98 80") a finite-80 reading would stack three finite verbs.
  2. 80=noun — **KILLED**: 'venir' takes no bare noun complement (requires à/de + NP), every period.
  3. 80=determiner/quantifier — **KILLED**: the locus-level promote (`det-80-1156-1011`) is @1156-scoped and not extended here; "vient [80-det] [10?]" violates 'venir' government, 10's class is open, and "80 10" is a hapax.
  4. 80=imperative (bare or '80-77' enclitic) — **KILLED**: post-'vient' position cannot host an imperative; the enclitic diagnostic needs 77 after 80 (follower is 10); `imp-80-bare-1156-1596` already fenced bare readings elsewhere.
  5. 80=adverb — **KILLED** at the lane naming standard: no battery license for adverb-80 exists anywhere in the lane; A8 frames 80 as verb; §3 bars inventing a reading with zero byte support.
  6. 80=infinitive-subject — **KILLED**: 'vient' already has its overt subject (66); `infsub-80-frame`'s kill of R-SUBJ is consistent with (not contradicted by) this window.
- **C3 — PASS (consequence).** The "[66] vient [80]" clause is complete: subject (66) + finite verb (98='vient') + governed infinitive (80). Combined with the parent's closed 'est à' frame ("62 94 59 39 [88-inf]"), the @760–768 span now parses as **two complete clauses**. This hardens the parent's C3 relatively; it does not force the @760 boundary (parent C4's fence stands — 20's clause-initial roles remain fenced-live, owned by `boundary-760-20role`).

## Verdict: PROMOTE

C1 and C2 pass; no adverses were listed. Scope is @768 only — window-level, not a global class claim. 80's global verb/determiner split stays red-team venue (`poly-80-docket` queued, untouched); no polyvalence declared; §7 intact. No standing or red-team verdict is contradicted or downgraded: `vient-98-name`, `det-80-1156-1011` (locus-scoped), and `infsub-80-frame` are adopted as premises. No value named for 80.

## Follow-ups

Promote needs none per §4. One narrow continuation, verified ABSENT from battery-queue.json:

1. `val-80-768-inf` (P3) — name 80's infinitive value at @768 via the "vient [80-inf]" frame (e.g. transitivity/agreement probes against the "80 10 22" tail). Bar: one candidate value parsing all three "[98] 80" windows, or fence the value as locus-bound.

## Bookkeeping

- Queue: `frame66-vient-80` → status `verdict`, result `promote`, 2026-10-09 (pre-write assert passed — was `queued`/verdictless; temp-file + rename; JSON re-validated post-write; own entry only; no downgrade).
- Lock `locks/frame66-vient-80.lock` created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
