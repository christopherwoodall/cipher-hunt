# Battery verdict: lon-09-verb

## Bar (verbatim, pre-registered)

"resolve iff 09's 12-window profile supports verb with zero noun-forcing window; else fence"

Restated as numbered clauses:
- C1: 09's 12-window profile supports verb (class-level verb-shape).
- C2: zero noun-forcing windows in the profile.
- C3 (else-branch): fence the 09-verb claim.

## Method

Read BATTERY-PROTOCOL.md first; created/deleted `locks/lon-09-verb.lock` per protocol.
Re-derived the repaired stream from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json` (parsed per `repair_parse.py`):
1,847 pairs / 96 types verified. `canonical.py` never touched. R5005, sealed
gates, red-team adjudication queue untouched.

Note on offsets: the brief's @1058/@1764 are 0-based indices; the windows are
1-based @1060 (row a6_04) and @1766 (row a8_08). Both are `77 84 09` = "l'on 09"
(77='le' provisional, 84='on' A15-granted).

Standing values used: GT 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que;
granted/promoted 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce;
provisional 59=est, 77=le; kills honored incl. 09/92 "-ère" (A6, NOT re-litigated
per the adverse).

## 09 census (n=12, all re-derived, 1-based @)

| @ (1b) | row | context (09 centered) |
|---|---|---|
| 1 | a1_00 | START [09] 00 97 51 47 |
| 174 | a1_05 | 12 48 21 60 [09] 87 86 21 69 |
| 290 | a2_03 | 89 28 00 97 [09] 64 29 40 65 |
| 519 | a3_00 | 56 87 77 80 [09] 70 91 77 06 |
| 592 | a4_00 | 00 97 41 41 [09] 00 92 79 85 |
| 681 | a5_00 | 37 77 45 23 [09] 07 00 92 64 |
| 916 | a5_09 | 83 59 37 96 [09] 02 24 49 74 |
| 1060 | a6_04 | 45 23 77 84 [09] 98 83 82 96 |
| 1224 | a7_01 | 61 24 48 30 [09] 20 57 64 79 |
| 1263 | a7_02 | 29 69 88 01 [09] 11 50 46 69 |
| 1766 | a8_08 | 93 06 77 84 [09] 24 87 64 26 |
| 1821 | a8_10 | 29 37 01 02 [09] 19 00 97 00 |

## Window-level evidence

- **@290 (noun-forcing):** `97 09 64 29 40 65` = "[97] [09] qui(64, granted)
  er(29, GT) e(40, GT)". 09 is the antecedent of the "qui"-relative. A verb in
  09's slot ("*[verb] qui [verb]") is ungrammatical in 1841 French; the
  interrogative-"qui" rescue ("…[verb]. Qui ere…?") is equally ungrammatical.
  09 is nominal here (whether as head noun, 97-09 word, or adjective — all
  non-verb).
- **@916 (noun-forcing):** `83 59 37 96 09 02 24 49 74` = "[59=est, prov] [37]
  par(96, banked GT) [09] [02]…". 09 directly complements the preposition
  "par", which requires a nominal complement — "par [verb]" is ungrammatical
  at any period. 09 is nominal here regardless of the 09-02 boundary.
- **@1060 / @1766 (flagship "l'on 09" windows):** `77 84 09 98` / `77 84 09 24`
  = "l'on [09] [98/24-verb-class]". Under verb-09 this reads "on [verb]
  [verb]" (two finite verbs, no boundary) — ungrammatical. These windows do
  not support the claim; they are at best neutral (word-boundary or clause
  questions for later work), at worst verb-hostile.
- **@519:** `80 09 70` — 80 is verb-frame (A8); verb-09 gives "verb verb",
  ungrammatical. Verb-hostile.
- **@1263:** `01 09 11` — 09 directly before 11='la' (GT determiner); verb +
  determiner is ungrammatical. Verb-hostile (09 plausibly word-final before
  "la [50]").
- **@1:** stream-initial 09 — finite-verb reading impossible (no subject).
- **@174:** `60 09 87=ce` — "…[09] ce [86]…": verb+"ce"-object is the only
  weakly verb-compatible window (besides @1224).
- **@1224:** `30 09 20` = "pas(30, R17-conditional) [09] [20]" — weakly
  verb-compatible ONLY if 30='pas' holds.
- **@592, @681, @1821:** neutral (open neighbors).

## Per-clause results

- **C1 (profile supports verb): FAIL.** At most two weakly verb-compatible
  windows (@174, @1224-conditional); two noun-forcing windows; four
  verb-hostile windows (@290, @519, @916, @1263); the two flagship windows do
  not parse under verb-09.
- **C2 (zero noun-forcing windows): FAIL.** @290 ("[09] qui"-antecedent) and
  @916 ("par [09]" with banked 96='par') both force nominal 09 at battery
  grade.
- **C3 (else-branch): FIRES — 09-verb FENCED.** The verb-shape claim is fenced,
  not killed (n=12 thin per the adverse; word-boundary reframes remain
  logically possible). 09's class stays open.

## Adverses answered

- "n=12 thin": acknowledged — this is exactly why the bar prescribes a fence
  rather than a kill. The two noun-forcing windows are byte-exact on granted
  values (64='qui', 96='par'), not thin-data artifacts.
- "09's killed '-ère' value is NOT re-litigated": honored — no value claim
  made or tested; class-shape only. A6's kill and the 09~92 HOLD are untouched.

## Standing-state check

No standing verdict contradicted or downgraded. No red-team verdict on 09's
class exists. §7 honored — no polyvalence declared. The nominal readings at
@290/@916 are noted as leads, not promoted (beyond this battery's bar).

## Verdict: NULL (fence executed)

09-verb is fenced. 09's class remains open; nominal leads exist at @290 and
@916 for follow-up work.

## Follow-ups proposed (for supervisor queuing)

1. `noun-09-916` (P3): test 09 as nominal complement of "par" at @916 —
   "est [37] par [09] [02]" — name 09's nominal value via the prepositional
   frame.
2. `rel-09-290` (P3): test 09 as "qui"-antecedent at @290 —
   "[97] [09] qui [29][40]…" — discriminate the 97-09 boundary and name 09's
   nominal value.
3. `lon-09-reseg` (P3): re-segment "l'on 09 [98/24]" at @1060/@1766 — test
   word-initial 09 in a longer word with the following verb-class group, or a
   clause boundary between 09 and 98/24.
