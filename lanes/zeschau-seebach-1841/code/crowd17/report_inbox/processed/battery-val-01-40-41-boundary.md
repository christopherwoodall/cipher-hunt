# Battery report: val-01-40-41-boundary

## Bar (verbatim, pre-registered)

"fence the '[41]en'/'[41]tain' composition arms terminally, or find the one composition frame with a standing license"

Numbered clauses:
- C1: fence the '[41]en' composition arm terminally (no battery-grade re-open path).
- C2: fence the '[41]tain' composition arm terminally.
- C3: find the one composition frame with a standing license at the window (alternative outcome).

Adverses (pre-registered): none listed in the queue entry. The parent
(val-01-census) adverse — 24's §7 tension with 'en' — is adopted but NOT
engaged: the fence below rests on clitic order and cell grouphood, both
independent of 24's class.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed like `code/side-keyhunt/repair_parse.py`. Asserts held (1,847 pairs,
96 types). `canonical.py` never used. All offsets 0-based. Tested only 1841
diplomatic French.

Offset note: the claim's "@40 '64 41 01 24 88'" maps to 0-based
@38=64, @39=41, @40=01, @41=24, @42=88 (row a1_01). The claim names the
window by its 64 position; all work below is 0-based.

## Window evidence

Byte-confirmed 0-based @38–42, row a1_01:
`64('qui',prom) @38 | 41(open) @39 | 01(open) @40 | 24(verb-class, registry; class contested — battery-24-en-verb-conflict escalated the en-vs-verb mutual kill to red team) @41 | 88(gov-class) @42`

Standing context:
- 01 grouphood (independent word-level cell): n(01)=28; "01 24"×3
  (@40, @828, @984); "37 01"×3 (A12 unit frame); "45 01"×1 = 'ceci'
  (R20-113 GRANT, conditional). "41 01"×1 — this window only.
- 41 profile: n(41)=19; standalone-word at @808 (41-808-role PROMOTE);
  zero 29='er' contact in either direction stream-wide (no completion
  neighbor); followers word-level ('n'×2, 'fois'×1, verbs).
- val-01-census (2026-10-09, NULL): no uniform 01 value nameable;
  'en' 9 kill-grade deaths, 'tain' zero legs, 'on' 5 kills + homophony
  problem. Adopted, not re-litigated.

## C1 — '[41]en' composition arm: FENCED terminally

Three independent fence causes, each terminal at battery grade:

- **F1 — clitic order (value-independent).** French 'en' as clitic is
  strictly preverbal ("il en parle"). A composition "41-word + en"
  places 'en' postverbally — ungrammatical under every value assignment
  to 41 and 01. No future battery naming re-opens this.
- **F2 — 01's grouphood.** Reading 01 as a sub-lexical 'en' cluster at
  @40 contradicts its independent word-level grouphood (n=28,
  "01 24"×3, A12 "37 01"×3, R20-113 "45-01"='ceci'). A sub-lexical-01
  at one window is a conditioned split — §7 red-team venue, not
  battery-licensable.
- **F3 — 41's word status.** 41-808-role PROMOTE established 41 as a
  standalone word; stream-wide zero stem+completion evidence for 41
  (0× 29-contact either direction). A stem-41 composing with 'en' at
  @39 needs a §7 word/stem split declaration — red-team venue.

All three hold without naming any open value. Re-open requires red-team
§7 action on 01 or 41 — no battery path exists.

## C2 — '[41]tain' composition arm: FENCED terminally

- **F1 — zero positive legs.** 'tain' has no composition leg under
  standing values at any 01 window (adopted from val-01-census §'tain',
  verified: no 01 window has a neighbor with standing letter content
  completing a "-tain" word).
- **F2 — no composition partner at @39–40.** 41's value is open and
  24's class is contested; no standing letter content at either cell
  completes a French "-tain" word with a 'tain' 01.
- **F3 — 01's grouphood** (C1-F2, identical): the bound-syllable reading
  needs a §7 conditioned split — red-team venue.

Fenced terminally at battery grade. The only re-open path is red-team §7
(sub-lexical 01) plus a future named 41 value forming a French "-tain"
word — no battery-grade path.

## C3 — composition frame with a standing license: NONE EXISTS

Checked every standing-licensed composition frame against the byte facts
at @38–42:
- A12 (37-01 unit): prev of 01 is 41, not 37. Fails.
- A10 (33+29 stem+completion): neither cell present. Fails.
- 45-01='ceci' (R20-113): prev of 01 is 41, not 45. Fails.
- 41-internal compositions: none licensed in the standing record.

No composition frame with a standing license exists at this window. The
default 41|01 word boundary holds: "qui [41] | [01] [24] [88] …".

## Verdict: NULL (fence executed)

C1 FIRES (fenced terminally) / C2 FIRES (fenced terminally) / C3 moot
(no licensed composition frame exists). Both composition arms are closed
at battery grade with re-open gated on red-team §7 action only. No
standing or red-team verdict contradicted, downgraded, or re-litigated;
§7 intact; R5005, sealed gates, red-team adjudication queue untouched.
Canonical-stream caveat stands.

## Follow-ups (§4; both verified ABSENT from battery-queue.json)

1. `val-41-39-value` (P3) — name 41's value at 0-based @39 ("qui [41]
   [01] [24]"); a named word-41 hardens the 41|01 boundary from the 41
   side and closes the composition question independently of 01.
2. `boundary-41-01-corpus` (P4) — corpus census of "qui [word] [word]
   [verb]" shapes matching "64 41 01 24" in 1841 French; confirms the
   two-word boundary as the productive parse (negative control for any
   future composition re-open).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-01-40-41-boundary.md` (this file).
- Queue: `val-01-40-41-boundary` queued → `verdict`/`null`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; target-id-unique tmp
  `battery-queue.json.val-01-40-41-boundary.tmp` + atomic rename; disk
  re-validated; own entry only; no downgrade).
- Lock `locks/val-01-40-41-boundary.lock`: created on start
  (2026-10-09T19:50:00Z, no stale lock), deleted on completion.
