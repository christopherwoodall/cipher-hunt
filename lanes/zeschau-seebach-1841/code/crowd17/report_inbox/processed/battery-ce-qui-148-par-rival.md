# Battery report: ce-qui-148-par-rival

- Target id: `ce-qui-148-par-rival`
- Claim: "@148 'ce qui par ce que': test whether 96=par after qui kills the relative reading there or licenses an elliptical-agent reading."
- Date: 2026-10-09
- Parent: battery-ce-qui-87-subject (NULL, 2026-10-09) — follow-up 2 of its three.
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). Verified in-session: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

Terms (ASD-STE100): "relative-subject" = the pronoun "qui" used as the subject of a relative clause ("ce qui est arrivé"). "Kill grade" = the window forces the claim false under standing values. "Battery grade" = the evidence standard of this pipeline.

## Bar (verbatim, pre-registered before testing)

> Bar: kill-or-license at battery grade, or fence.

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** Locus byte-confirmed at 0-based @148: "87 64 | 96 47 46" ("ce qui par ce que"), row a1_04.
2. **C2 (kill arm):** "96=par" immediately after 64=qui kills the relative-subject reading of "87 64" at @148 at battery grade — no licensed relative-clause parse under standing values.
3. **C3 (license arm):** "96=par" licenses an elliptical-agent reading at @148 at battery grade — a licensed grammatical parse with <=1 stated assumption.
4. **C4 (fence):** If neither C2 nor C3 fires at battery grade, fence with stated cause.

Adverses listed: none.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/ce-qui-148-par-rival.lock` on start (agent id + UTC timestamp); deleted on completion. No stale lock was present.
2. Re-derived the repaired stream in-session. All @-offsets below are 0-based.
3. Standing premises used, not re-litigated: 87=ce (promoted), 64=qui (promoted), 96=par (promoted/granted), 47=ce (promoted A4), 46=que (pencil GT), 67=et (positional rule), 84=on (promoted A15). 66, 26, 35, 58 have no standing value.
4. Corpus control: full `code/side-period/corpus/` scan (31,662,676 chars of 1841 French) for the word sequence "qui par", every hit context-read.

Lock note: no lockfile existed at start. Created `code/crowd17/next-token/locks/ce-qui-148-par-rival.lock` 2026-10-09T11:56:16Z; deleted on completion.

## Window-level evidence

### The locus — 0-based @141–158 (row a1_04)

`...141:14 142:74 143:67(et) 144:64(qui) 145:77(le) 146:84(on) 147:29(er) | 148:87(ce) 149:64(qui) | 150:96(par) 151:47(ce) 152:46(que) 153:66 154:84(on) 155:26 156:35 157:58 158:35...`

The focal frame: "ce(87) qui(64) par(96) ce(47) que(46) [66]". Left closure adopted from the parent battery ("…on [29]-er" infinitive closes cleanly before 87). No standing verb anywhere after "qui".

### Collocation facts (byte-exact, re-derived)

- "87 64": exactly 5x stream-wide — @148, @180, @1767, @1775, @1800 (matches the parent's census).
- "64 96" ("qui par"): exactly 3x stream-wide — @149 (this locus), @341 ("64 96 43": "qui par [43]"), @1025 ("64 96 43": "qui par [43]").
- n(96)=21; 96's successors include preposition-shaped followers only (00, 09, 21, 40, 43, 45, 47, 48, 56, 82, 86, 87); no standing verb use of 96 exists.

### C1: PASS — locus byte-confirmed.

### C2: PASS (kill grade) — the relative-subject reading is forced false at @148.

A relative-subject "qui" requires a finite-verb predicate. At @148, "qui" is immediately followed by "par", a preposition (standing grant — no polyvalence at battery level per §7). "Ce qui par ce que" therefore has no licensed relative-clause parse: the relative clause's predicate is missing, and a preposition cannot supply it. This is grammar-level, value-independent, every period.

Corpus control confirms the kill rather than softening it: 46 "qui par" hits in 31,662,676 chars of 1841 French were all context-read. Every genuine hit is "qui par [adjunct] [FINITE VERB]" — the relative verb always arrives after the adjunct ("ceux qui par devoir ne peuvent se dispenser…", "qui par là même décidait…", "qui par ses travaux… avait mérité…"). The attested construction requires the verb; at @148, after "par ce que [66]" there is no finite verb under standing values (66, 26, 35, 58 all open; 84=on). The construction's required element is absent.

The sibling "qui par [43]" windows (@341, @1025) do not rescue this window: they have a nominal 43 after "par", but the clause predicate is still absent there too (they are the red team's "ce qui par [43]" verbless-left-edge venue — untouched, not decided here).

### C3: FAIL — no licensed elliptical-agent reading exists at battery grade.

Four candidate rescues, all dead:

1. **Interrogative "qui":** dead. "Ce qui" is always relative; "ce" binds "qui" ("qu'est-ce qui" is the interrogative form). "Ce qui, par ce que…?" is not a licensed question in any period.
2. **Passive-participle ellipsis** ("ce qui [est fait] par ce que"): dead. French never elides the participle before an agent phrase ("*ce qui par ce que" is ungrammatical every period).
3. **Causal "par ce que" ("because"):** dead twice over. "Par ce que" with a demonstrative "ce" is not the one-word "parce que" (different construction), and even granted the causal reading, the matrix "ce qui" still lacks its predicate.
4. **Parenthetical insertion** ("qui, par exemple, [verb]"): dead. The parenthetical license requires the clause verb to follow; none exists under standing values.

## Verdict: KILL

The "87 64" relative-subject frame is **dead at @148 at battery grade**. The parent battery's "does NOT license" is upgraded to forced-false: "par" after "qui" kills the relative reading, and no elliptical-agent reading is licensed.

## Scope and non-contradictions

- **No standing verdict contradicted or downgraded.** 64=qui, 96=par, 87=ce, 47=ce are all adopted as premises, not re-decided. The "ce qui" adjacency stays byte-real (5x); only the full relative-subject FRAME at @148 is killed.
- **The qui-subject-recoverability PROMOTE is untouched.** Its @149 count is antecedent-recoverability (87=ce as a licensed antecedent of "qui"), not frame-licensing. The antecedent stands; what is killed here is the clause's missing predicate — a different measurement. Both results hold.
- **@341 and @1025 ("qui par [43]") are out of scope** — they belong to the red team's "ce qui par [43]" verbless-left-edge call (see ce01-1029-redteam-package). Not decided here.
- §7 intact — no polyvalence declared. Canonical-stream caveat stands (row a1_04 offset unvalidated).

## Bookkeeping

- Queue: `ce-qui-148-par-rival` → `status: verdict`, `result: kill`, 2026-10-09 (pre-write assert passed — was `queued`/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/ce-qui-148-par-rival.lock`: created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
