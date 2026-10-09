# Battery verdict: obj-87-closure

- Target: `obj-87-closure` (battery-queue.json, priority 3, status queued)
- Claim: test the six "V/par ce" closure windows as a uniform object-closure frame once 24's class is banked
- Parent: `87-left-attach-census` (NULL, 2026-10-09), which graded six windows LEFT-CLOSING at battery grade

## Bar (verbatim, pre-registered)

> Bar: uniform parse with <=1 ungranted assumption, or fence @824/@830 as 24-load-bearing.

Restated as numbered clauses before testing:

- **C1 (uniform parse):** all six parent-identified closure windows (@163, @344, @1028, @824, @830, @1426) parse under ONE uniform object-closure frame ("87=ce is the direct object closing the left clause/phrase") with <=1 ungranted assumption total.
- **C2 (fence arm):** if C1 fails, fence @824/@830 as 24-load-bearing (their closure parse depends on 24's open value).

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/obj-87-closure.lock` on start (agent ce5e5b61-cd95-47a4-881f-d3b60136fb0e, 2026-10-09T20:23:00Z); deleted on completion.
2. Re-derived the repaired stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` via `repair_parse.py`: 1,847 pairs, 96 types. Asserts held. `canonical.py` never used.
3. Byte-confirmed all six loci (0-based): @163=`52 94 24 87 11` (a1_05), @344=`64 96 43 87 01` (a2_05), @1028=`64 96 43 87 01` (a6_03), @824=`24 87 59 38` (a5_05), @830=`82 01 24 87 11` (a5_06), @1426=`67 33 29 87 63` (a7_08).
4. Standing values used: 87=ce, 64=qui, 96=par, 94='ne' (STRONG LEAD), 24=['verb','cls'] class-level (R17-009; VALUE open, narrowed to savoir/vouloir, neither named), 67 et/veut positional rule, 33+29=A10 infinitive, 59=est (provisional), 11=la (pencil GT), 82=m (pencil GT). 43 class-open. 01 class-open.
5. Did NOT touch R5005, sealed gate instances, or the red-team adjudication queue.

## Findings

### The uniform frame under test

"87=ce is the direct object of the immediately preceding governor, closing the left clause/phrase." Governors: finite 24 (@163, @824, @830), the "par [43]" phrase (@344, @1028), the infinitive "[33]er" (@1426).

### Window-by-window

**@163 `52 94 24 87 11` = "[52] ne [24] ce la" — PARSES as closure.**
94='ne' STRONG LEAD forces 24 finite (R17-009 class-level grant); "ce" = direct object; 11=la opens a new clause. Unnatural rival ("ne [24]. Ce la…") is awkward French. Ungranted assumption: **A1 — 24 is transitive** (accepts "ce" as direct object). 24's class ("finite verb, modal-shaped") does not grant transitivity; it is value-dependent and 24's value is open.

**@824 `24 87 59 38` = "[24] ce est [38]" — PARSES as closure, BUT AMBIGUOUS.**
Closure parse: "[24] ce" (object) + "est [38]" (new clause, 59=est provisional). Needs A1. Rival parse: "[24]" (complete clause) + "ce est [38]" = "c'est [38]" (new clause, ce = subject). The rival needs ZERO ungranted assumptions and is natural French. The closure parse is therefore not forced; it is load-bearing on A1.

**@830 `82 01 24 87 11` = "m' [01] [24] ce la" — PARSES as closure.**
82='m' proclitic; "ce" = direct object of 24; 11=la opens a new clause. Needs A1. (Left edge "m' [01] [24]" has 01 open, but the "[24] ce" closure core is unaffected.)

**@1426 `67 33 29 87 63` = "veut [33]er ce [63]" — PARSES as closure, clean.**
67='veut' via the granted positional rule (follower 33+29 infinitive-shaped); 33+29 = infinitive (A10); "ce" = direct object of the infinitive ("veut faire ce" shape). Ungranted assumptions: **0**.

**@344 / @1028 `64 96 43 87 01` = "qui par [43] ce [01]" — DOES NOT PARSE as object-closure under standing values.**
The parent's grade ("ce = object of the par-phrase, phrase-final") was re-tested against the deeper `ce-frame-45-64-96-43-87-01` battery (2026-10-08), which established on this exact byte-identical 6-gram (x2):
- "par [43]" is grammatical ONLY as "par suite" ("consequently", adverbial) among noun-43's tested candidates — and that reading is CONDITIONAL on 43="suite" (not granted; 43's value arm belongs to noun-43).
- Under the "par suite" reading, the parse is "…ce qui, par suite, ce [01]…" — "ce" (87) is the SUBJECT of a NEW clause ("this [01]-s"), NOT a clause-final object. This directly contradicts the closure grade.
- For the parent's "object of the par-phrase" reading to work, "par [43] ce" would need 43 to be a verb/infinitive ("par [43-inf] ce" = "by [43-ing] this", ce = object of the infinitive). 43's class is open. This is ungranted assumption **A2 — 43 licenses the object-closure composition**.
- The "96 43" bigram is exactly 2x stream-wide (both = these twins), so there is no independent "par [43]" evidence to discharge A2.

### Assumption count (C1)

- A1: 24 is transitive. ONE assumption (covers @163, @824, @830). UNGRANTED.
- A2: 43 is a verb/infinitive licensing "par [43-inf] ce" as object-closure (covers @344, @1028). UNGRANTED. (The alternative conditional, 43="suite", removes the windows from the closure set entirely.)
- @1426: 0.

Total for the six-window uniform frame: **2 ungranted assumptions (A1 + A2) > 1. C1 FAILS.**

Note: the four-window subset (@163, @824, @830, @1426) DOES form a uniform "[V] ce" object-closure frame with exactly 1 ungranted assumption (A1) — but the bar is stated for the six, and @344/@1028 cannot join it at battery grade.

### C2 FIRES: fence @824/@830 as 24-load-bearing

- **@824:** the "[24] ce" closure parse is load-bearing on A1 (24 transitive, ungranted); the rival "c'est [38]" parse needs no ungranted assumption. FENCED as 24-load-bearing (and ambiguous). The closure reading is not battery-grade assertible until 24's transitivity resolves.
- **@830:** the "m' [24] ce" closure parse is load-bearing on A1. FENCED as 24-load-bearing.
- (@163 shares A1 but the bar names only @824/@830; @163's closure parse is the most secure of the three given the "ne"-forced finiteness, and is left standing with A1 recorded.)

### Additional fence (beyond the bar's letter, required by the findings)

- **@344 / @1028:** FENCED as 43-load-bearing and NOT battery-grade closure windows. The parent's LEFT-CLOSING grade is weakened: under the only grammatically licensed "par [43]" reading (conditional "par suite"), 87 opens a new clause rather than closing the left one. These two windows are removed from the closure set pending 43's value/class. This does not downgrade the parent battery (which was NULL); it refines its window inventory from six closure windows to four.

## Verdict: NULL

C1 fails (2 ungranted assumptions > 1); C2 fence arm executed. No standing or red-team verdict contradicted or downgraded (parent `87-left-attach-census` was NULL; `ce-frame-45-64-96-43-87-01` was NULL; R17-009 and all grants intact). §7 intact. Canonical-stream caveat stands (row offsets a1_05/a2_05/a5_05/a5_06/a6_03/a7_08 unvalidated beyond the byte-identical @344/@1028 twin).

## Scope

- Fences the closure CLAIM at @824/@830 (24-load-bearing) and @344/@1028 (43-load-bearing / not closure at battery grade).
- Does NOT kill "ce = object" at @163 or @1426 (both stand, @163 with A1 recorded, @1426 clean).
- Does NOT name any value or class; does not touch 24's value, 43's value, 01's class, or the red-team 94/66/78 venues.

## Follow-ups (for supervisor queuing; all verified ABSENT from battery-queue.json)

1. `trans-24-ce-corpus` (P3) — corpus census: do 24's narrowed rivals ("savoir"/"vouloir") take "ce" as direct object ("savoir ce", "vouloir ce") at scale in 1841 French? A positive result discharges A1 and re-fires @163/@824/@830 as closure; a zero hardens the fence.
2. `val-43-344-frame` (P4) — name 43's class at the @344/@1028 twins. Verb/infinitive re-opens the "par [43-inf] ce" object-closure parse (discharges A2); "suite" (or another adverbial) confirms the new-subject parse and permanently removes the twins from the closure set.
3. `cest-824-rival` (P4) — adjudicate @824's "[24] ce" closure parse vs the "c'est [38]" rival. If "c'est" wins on wider context, @824 drops from the closure set permanently regardless of A1.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-obj-87-closure.md`
- Queue: `obj-87-closure` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.obj-87-closure.tmp` + rename; disk re-validated; own entry only; no downgrade; no tmp leftover)
- Lock `locks/obj-87-closure.lock`: created on start (2026-10-09T20:23:00Z, no stale lock), deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
