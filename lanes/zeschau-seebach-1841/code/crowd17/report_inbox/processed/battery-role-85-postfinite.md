# Battery verdict: role-85-postfinite

- Target: `role-85-postfinite` (battery-queue.json, priority 3, status queued)
- Claim: "Name 85's grammatical role after finite-verb-shaped 24 across all five '24 85' windows (@732/@955/@1438/@1693/@1754): non-finite dependent vs composition with follower vs re-segmentation. Discriminates blocker (2) independently of 24's class."
- Parent: battery-que-1692-relative-test (NULL, 2026-10-09): five 24 85 windows; blocker (2) = "85's role after a finite 24 — ungranted" (escape routes: (a) 85 non-finite dependent, (b) 85+58 composition).
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; re-derived in-session, 1847 pairs / 96 types, asserts held). `canonical.py` never used. R5005 sealed instance untouched (data file read as the mandated stream input only).

## Bar (verbatim, pre-registered BEFORE testing)

> name 85's role iff it holds across >=4/5 windows with stated values at battery grade; else fence the windows individually

Numbered clauses (fixed before testing, not modified after):

- **C1:** One of the three candidate roles (non-finite dependent of finite 24 / composition with follower / re-segmentation) names 85's role across >=4 of the 5 windows.
- **C2:** The role is stated WITH VALUES at battery grade (85's value/class in that role is given, not merely the role label).
- **C3 (else-branch):** If C1 or C2 fails, each window is fenced individually (per-window: what holds, what is excluded).

## Method

Re-derived the repaired stream in-session. Located all '24 85' bigrams: exactly 5, at 0-based pair indices 732, 955, 1438, 1693, 1754 (matches the claim's @-offsets). Built 85's stream-wide profile: 85 occurs 15x at [54, 97, 375, 595, 733, 746, 956, 1047, 1173, 1234, 1278, 1439, 1694, 1699, 1755]; leaders {79:2, 29:3, 24:5, 81:1, 76:1, 21:1, 56:1, 91:1}; followers {58:3, 01:2, 08:1, 82:1, 93:1, 28:1, 04:1, 41:1, 36:1, 56:1, 48:1, 33:1} — 12 distinct follower types. Tested each candidate role against all five windows with byte-exact window dumps. 24's class was not re-litigated (adverse): "finite-verb-shaped 24" used only as the claim's framing premise; no 24-value assumed or concluded.

## Window-level evidence (@ = 0-based pair index)

**W1 @732 (row a5_02):** `88@730 11@731 [24]@732 [85]@733 93@734 76@735 18@736 82@737 06@738 00@739 36@740 20@741`
- 85's follower is 93. '85 93' is hapax stream-wide (1x). No composition license; no 33 (no licensed non-finite form); no digit anomaly. Fenced: role indeterminate; composition with 93 excluded at battery grade (hapax pair, unvalued 93).

**W2 @955 (row a6_00):** `87@953 46@954 [24]@955 [85]@956 04@957 20@958 67@959 96@960 00@961 86@962 56@963`
- 85's follower is 04. '85 04' is hapax stream-wide (04 occurs 3x total, leaders 80x2/85x1). No composition license; no 33. Fenced: role indeterminate. (Note: 87=ce, 46=que precede 24 — "ce que" frame per parent — but 24's class is not litigated here.)

**W3 @1438 (row a7_08):** `82@1436 16@1437 [24]@1438 [85]@1439 01@1440 52@1441 68@1442 59@1443 37@1444 64@1445 77@1446 84@1447`
- 85's follower is 01. '85 01' occurs 2x (@595: `79@594 85@595 01@596 29@597`; @1439). The @595 parallel shows '85 01' WITHOUT a preceding 24, weakening any 24-specific composition claim. 01 is common (28x, leaders 37/16/87/85/86) — not a dedicated 85 partner. No 33. Fenced: role indeterminate; composition excluded at battery grade.

**W4 @1693 (rows a8_05/a8_06):** `27@1691 46@1692 [24]@1693 [85]@1694 58@1695 15@1696 23@1697 91@1698 85@1699 33@1700 94@1701 30@1702`
- 85's follower is 58. '85 58' occurs 3x (@54: `79@53 85@54 58@55`; @1694; @1755) — the only recurrent '85 X' pair; 85 is 58's most common leader (3 of 58's 7 occurrences). Strongest composition candidate of the five windows. BUT: the composition's value is unstated (85=verb-stem + nominal-58 compound is morphologically odd in French; no value granted), and the same window's tail contains the licensed '85 33' shape @1699-1700 with a DIFFERENT leader (91) — 85 takes two different followers inside one window, undercutting a fixed-composition reading of 85. No 33 after the @1694 85. Fenced: '85 58' composition plausible but unstatable at battery grade; role indeterminate.

**W5 @1754 (row a8_08):** `89@1752 26@1753 [24]@1754 [85]@1755 58@1756 17@1757 78@1758 41@1759 15@1760 93@1761 06@1762 77@1763`
- 85's follower is 58 ('85 58', 3x — see W4). Same fencing as W4: composition candidate, value unstated, below battery grade.

## Candidate-role tests (all five windows)

**Option A — non-finite dependent (bare-85 = infinitive/participle complement of finite 24):**
- For: 85 is verb-stem (A3 frame, granted); French permits finite verb + bare infinitive.
- Against: the only stream-internal license for an 85-headed non-finite form is '85 33' (1x, @1699-1700, leader 91 — NOT 24). All five '24 85' windows lack 33. No unambiguous non-finite frame elsewhere licenses bare-85 (its non-24 leaders are 79, 29=er, 81, 76, 21, 56, 91 — none a licensed non-finite governor). The mapping bare-85 -> non-finite is an ungranted assumption.
- Coverage at battery grade: 0/5 (permitted by French syntax but unstatable with values).

**Option B — composition with follower (85+X = one word):**
- 85's followers across the five windows are FOUR distinct types: 93, 04, 01, 58, 58. A uniform composition role would need four separate composition licenses; only '85 58' recurs (3x) and its value is unstated. '85 93' and '85 04' are hapax; '85 01' 2x with a non-24 parallel (@595) that breaks 24-specificity.
- Coverage at battery grade: 2/5 at best (W4, W5 under an unstated '85 58' value). Fails >=4/5.

**Option C — re-segmentation (the 24|85 boundary is a pairing artifact):**
- The repaired parse is byte-exact; the gloss asserts (crib pair-alignment, a8_05 ends 46) hold in-session. No digit-level anomaly at any of the five windows (rows a5_02, a6_00, a7_08, a8_06, a8_08). A local re-pairing would be row-wide and would break the validated alignment; no alternative pairing is licensed anywhere in the standing record.
- Coverage at battery grade: 0/5. Unsupported.

## Per-clause verdicts

- **C1 — FAIL.** Best coverage is 2/5 (Option B on W4/W5, and only under an unstated value). Options A and C: 0/5 at battery grade. No candidate reaches >=4/5.
- **C2 — FAIL.** No candidate can be stated with values: 93/04/01 are unvalued; the '85 58' compound value is unstated; the bare-85 non-finite mapping is ungranted. The "stated values" demand cannot be met from the standing record.
- **C3 — PASS.** All five windows fenced individually above (W1-W5).

## Verdict: NULL (epistemic, not substantive)

No uniform role for 85 reaches battery grade; the bar's else-branch fired and each window is fenced. This is not a KILL: no window forces all three options false (French syntax permits finite+bare-infinitive; '85 58' recurs and may yet compose with a stated value). Blocker (2) from the parent — "85's role after a finite 24" — stands UNRESOLVED, independently of 24's class (the adverse is answered: 24's class was neither assumed nor concluded; the mutual-kill on 24 was not re-litigated).

Adverses: "independent of 24's class per parent - do not re-litigate 24" — ANSWERED. The analysis uses "finite-verb-shaped 24" purely as the claim's framing premise. No finding depends on 24's class; the red-team 24 venue is untouched.

## Follow-ups proposed (all three verified ABSENT from battery-queue.json, 2026-10-09)

1. `comp-85-58-trigram` (P4) — Test the '85 58' trigram as a composition: it occurs 3x ('24 85 58' @1693/@1754 + '79 85 58' @54), and 85 is 58's most common leader (3/7). Bar: state a VALUE for the '85 58' unit (e.g. verb-stem + nominal compound with a French gloss) that holds across all 3 occurrences, or kill the composition. Discriminates W4/W5.
2. `role-85-non24-leaders` (P4) — 85's non-24 leaders are 29=er (3x: @97/@375/@1234) and 79 (2x: @54/@595). If bare-85 is a licensed non-finite dependent after 'er' or 79, that license transfers to the '24 85' windows (Option A with a stated licensing frame). Bar: exhibit the licensing frame with stated values, or kill bare-85-as-non-finite.
3. `seg-85-boundary-digit-audit` (P4) — Byte-exact digit audit of rows a5_02/a6_00/a7_08/a8_06/a8_08 at the five windows for local pairing anomalies. Bar: produce a concrete alternative pairing with the gloss asserts re-verified, or kill re-segmentation lane-wide for these windows.

## Scope

Window-level only. Untouched: 24's class (red-team venue, not re-litigated), 27's class, 85's A3 frame, 58's nominal class, §7 (no polyvalence declared). Canonical-stream caveat stands (rows a5_02/a6_00/a7_08/a8_06/a8_08 offsets unvalidated beyond the repair's global asserts; pencil gloss is on a5_03).

## Bookkeeping

- Queue: `role-85-postfinite` queued -> `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique temp file `battery-queue.json.role-85-postfinite.tmp` + atomic rename; disk re-validated; own entry only; no downgrade; no standing/red-team verdict contradicted).
- Lock `next-token/locks/role-85-postfinite.lock`: created on start (agent e0d17135-a9d3-4f9a-9c34-13f07494d087, 2026-10-09T19:47:39Z; no stale lock pre-existed), deleted on completion (verified gone).
- R5005 sealed instance, sealed gates, red-team adjudication queue untouched. No standing verdict contradicted or downgraded.
