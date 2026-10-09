# Battery verdict: val-74-unaccusative

- Target: `val-74-unaccusative` (battery-queue.json, priority 3, status queued)
- Claim: Name 74's value with >=2 independent legs; if 74 names an unaccusative/presentational verb (venir/arriver/rester/entrer/sortir/naitre/tomber/paraitre...), the '[74-fin] le ver' subject-NP reading at @212 revives and this fence lifts.

## Bar (verbatim, numbered)

"value named with >=2 legs AND attested in the unaccusative inventory; else fence the subject-NP arm permanently"

- C1. 74's value named with >=2 independent legs.
- C2. The named value attested in the unaccusative/presentational inventory.
- C3. If C1/C2 fail: fence the @212 subject-NP arm permanently (adverse: "fence is permanent if the bar fails - do not re-open without new legs").

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/val-74-unaccusative.lock` on start (agent df703a57-b6b3-4a2b-b32f-193139c7e2d0, 2026-10-09T20:38Z); deleted on completion.
2. Re-derived the repaired stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` via `repair_parse.py`: 1,847 pairs, 96 types, n(74)=34. `canonical.py` never used.
3. Byte-verified the verb-forced windows (0-based): @212 "19 74 77 78", @261 "77 84 74 45", @350 "12 94 74 67 78", @786 "42 94 74 65 84", @1103 "82 94 74 47 78". Tested all 8 inventory candidates (vient, arrive, reste, entre, sort, naît, tombe, paraît) against each.
4. Byte-verified the uniformity blockers: six "74 74" doublings @417/@816/@861/@919/@1053/@1637; noun windows @1307 "77 74" (le [74]) and @1637 "87 74" (ce [74]).

## Findings

### C1 — FAIL: no unaccusative value is selectable

All 8 candidates parse all five verb-forced windows identically; no window supplies selectional pressure:

- @212 "[19] V le(77) ver(78)": presentational-inversion shape "V le ver" — vient/arrive/reste/entre/sort/naît/tombe/paraît all parse identically.
- @261 "le on V ce": all 8 parse identically.
- @350 "ne V et(67) ver": all 8 parse identically.
- @786 "ne V [65-noun] on": all 8 parse identically.
- @1103 "m ne V ce ver": all 8 parse identically.

No agreement controller beyond 3sg, no object, no complement, no selectional restriction anywhere in the five windows. Per the val-03-value-census / masc-noun-86-name precedent, parsing != naming. Zero selective legs; naming any one candidate would be arbitrary. C1 FAILS.

### Uniform verb-74 is independently kill-grade dead

Even a named verb value could not hold uniformly: the six "74 74" doublings (@417/@816/@861/@919/@1053/@1637) put two finite verbs in sequence under uniform verb-74 — ungrammatical at kill grade — and the noun windows @1307 ("le [74]", provisional 77) and @1637 ("ce [74]", granted 87) force noun class. Any verb naming is at most a conditioned split (verb at @212/@261/@350/@786/@1103 vs noun/letter elsewhere) — a §7 declaration the battery cannot make; the shape is already packaged in `split-74-redteam-input` (verdict/null, 2026-10-09).

### C2 — moot

No value named; all 8 tested candidates are in fact unaccusative/presentational, so the inventory condition cannot rescue the bar.

### C3 — fires: subject-NP arm fenced permanently

The @212 "[74-fin] le ver" subject-NP reading is fenced TERMINALLY (permanent per the adverse) — not on grammar (presentational inversion is a real frame) but on value: no unaccusative value is nameable at battery grade, and no future naming at these legs re-opens it without new legs. Re-open conditions (new legs only): a named 74 value from an independent tier (e.g. `val-74-letter`), or a red-team §7 split declaration naming the verb arm.

## Verdict: NULL (fence executed, permanent per adverse)

C1 FAIL / C2 moot / C3 FIRES. No standing or red-team verdict contradicted; §7 intact; canonical-stream caveat stands.

## Follow-ups (for supervisor queuing; all verified ABSENT from queue)

1. `subj-74-212-corpus` (P4) — corpus census: presentational inversion "V + definite-NP subject" for the 8 candidates in 1841 French; a zero for all candidates fences the subject-NP frame itself at grammaticality grade (new leg about the frame, not the value).
2. `val-19-211-class` (P4) — name 19's class at @211; 19's class constrains the @212 frame (new locus leg).
3. `val-74-letter` (P3) — ALREADY QUEUED; noted for convergence, not duplicated: a named letter content for 74 is the independent-tier new leg that re-opens the value question.

## Scope

Value-naming at 74's verb windows only. Untouched: split-74-redteam-input's §7 package, noun-74 windows, the '74 74' letter-tier residual (val-74-letter queued), A15, 94='ne' STRONG LEAD, 98='vient' LEAD, §7. R5005, sealed gates, red-team adjudication queue untouched.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-74-unaccusative.md`
- Queue: `val-74-unaccusative` queued -> `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.val-74-unaccusative.tmp` + atomic rename, disk re-validated, own entry only, no downgrade, no tmp leftover)
- Lock `locks/val-74-unaccusative.lock`: created on start (no stale lock), deleted on completion (verified gone).
