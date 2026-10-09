# Battery report: noun-09-916

**Target:** `noun-09-916` (P3)
**Date:** 2026-10-09
**Worker:** battery worker noun-09-916 (subagent 4926c7d0-cc83-450a-be0c-332376a50bc9)
**Verdict:** NULL (fence executed per the bar's else-branch)

## Bar (verbatim from queue — derived numbered bars, parent brief)

"(1) parse the @916 window with 09 nominal under standing values; (2) name 09's noun value iff it parses with zero new assumptions; (3) else fence with stated cause."

## Bar restated as numbered clauses

1. (C1) The @916 window parses with 09 nominal under standing values.
2. (C2) Name 09's noun value iff it parses with zero new assumptions.
3. (C3) Else fence with stated cause.

## Method

Read BATTERY-PROTOCOL.md first; created `locks/noun-09-916.lock` on start
(deleted on completion). Re-derived the repaired 1,847-pair / 96-type stream
in-session from `code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`, tokenized like `code/side-keyhunt/repair_parse.py`
(asserts: n=1847, 96 types). `canonical.py` never used. R5005, sealed gate
instances, and the red-team adjudication queue untouched.

The queue's @916 is 1-based; the window on the 0-based stream is @915.
Window bytes (row a5_09): `… 912:59 913:37 914:96 915:09 916:02 917:24 918:49 …`

Standing values used: 59='est' (provisional), 96='par' (granted), 37=
predicative (A1 frame grant, value open), 24=finite-modal (promoted class),
02 value/class open (modal arm fenced by adv-02-858 NULL; 'fait' candidate
unpromoted), 09 value open.

## Window-level evidence

**The nominal parse (C1):** `59 37 96 09` = "est [37-pred] par [09-noun]".
The passive-agent frame is grammatical under standing values (A1 predicative
37 + granted 96='par'): e.g. "est [pp] par [agent]". The local contact is
licensed. **C1: PASS (locally; edge caveats below).**

**C2 — no nameable noun value:** no independent noun value for 09 exists
anywhere in the lane record. 09's 12-window census (n=12: @0/@173/@289/@518/
@591/@680/@915/@1059/@1223/@1262/@1765/@1820) shows no noun-shaped frame,
no distributional anchor, and no standing value. The lane's only shape
reading for 09 is the verb-shaped arm at the two "84 09" windows (@1058
"84 09 98", @1765 "84 09 24" — `lon-09-verb`, NULL): 84='on' followed by 09
followed by a verb-class group forces verb-shaped 09 there. The 09~92 hold
(A6) and the killed "-ère" value give no noun. Naming any noun at @915
would be invention, which the bar explicitly forbids ("iff it parses with
zero new assumptions"). **C2: FAIL.**

**Edge caveats on C1's pass:** the right edge `916:02 917:24 918:49`
does not continue the nominal parse cleanly — 02 is class-open and the
promoted modal 24 has no licensed infinitive complement at @918–919
("24 49 74"). The nominal reading survives only as a window-local parse
with a dangling right edge.

## Adverses

- **Verb-shaped 09 arm (`lon-09-verb` NULL):** the two "84 09" windows
  tension the nominal hypothesis — 09 reads verb-shaped there. This is
  recorded as a live tension, not ignored. A nominal 09 at @915 alongside
  verbal 09 at @1058/@1765 would require a conditioned split, which is
  red-team venue under §7 (no polyvalence declared at battery level).
- No other adverses listed.

## Verdict: NULL — 09 fenced as class-open at this window

The passive-agent frame licenses the local contact, but no noun value for
09 is nameable from independent windows, and the two verb-shaped "84 09"
windows keep the noun arm unfenced only at the cost of a red-team-level
split. Per bar clause 3, fence with stated cause.

No standing or red-team verdict contradicted or downgraded; §7 intact.

## Follow-ups (all verified absent from queue, for supervisor queuing)

1. **`val-09-noun-search`** (P3): full 12-window class census for 09;
   decide whether the two verb-shaped "84 09" windows kill the noun arm
   or condition it.
2. **`rightedge-09-02-24`** (P3): resolve the @916–918 "[02] [24] 49"
   right edge; a grammatical continuation is a gate on any nominal-09
   parse at @915.
3. **`par09-agent-rival`** (P4): census "est [37-pred] par X" agent frames
   stream-wide; test whether 96 licenses an agent reading at @914 at all,
   or is positional.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/noun-09-916.lock` created on start,
  deleted on completion.
- `battery-queue.json`: `noun-09-916` queued → verdict/null (temp-file +
  rename; pre-write assert confirmed no prior verdict; own entry only;
  JSON re-validated).
- `canonical.py` never used; R5005, sealed gates, red-team adjudication
  queue untouched.
