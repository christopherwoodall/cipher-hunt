# Battery report: adj-68-postnominal

**Target:** `adj-68-postnominal` (priority 3)
**Date:** 2026-10-09
**Worker:** df6d9b7c-c6e5-4ff1-97e2-7cb0f4bbb914
**Verdict:** NULL (no stream-anchored adjective value; noun/adjective split unresolved)

## Bar (verbatim from queue)

"promote iff a named adjective value parses at all three post-nominal windows with zero hard contradictions; a gendered naming (feminine -e or masculine form) re-opens the gender-65 agreement test at the contact window"

## Bar restated as numbered clauses (frozen before testing)

- (C1) A named adjective value for 68 is stated.
- (C2) The named value parses at all three post-nominal windows (@1383 contact window, @1442, @1788) with zero hard contradictions.
- (C3) If the naming is gendered (feminine -e or masculine form), the gender-65 agreement test at the contact window is re-opened.

Lane @ = 0-based stream index. The queue's "0b1383/0b1442/0b1788" are the window start offsets; 68 itself sits at @1384/@1442/@1788 (0-based). All re-derived below.

## Method

Read `BATTERY-PROTOCOL.md` in full first. Created `locks/adj-68-postnominal.lock` on start (agent id + UTC timestamp; deleted on completion — no pre-existing lock, no stale lock). Re-derived the repaired 1,847-pair / 96-type stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` parsed per `code/side-keyhunt/repair_parse.py` (asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gate instances, the red-team adjudication queue untouched. Prior verdicts used as premises (cited, not re-litigated): 11=la (pencil), 47=ce (A4), 79=tout (A5), 59=est (provisional), 48=e letter (n-e-12-48), 06=ent (battery PROMOTE), fem32e-subject-gender (PROMOTE, 65 unmarked), 67 = sole true polyvalence (§7). Parent: battery-follower-65-adjclass-census (NULL, 2026-10-09); val-68-noun-sweep in flight (not a verdict).

## Window-level evidence (byte-exact, 0-based @)

n(68) = 8. Followers: 21 x2, 37, 00, 52, 59, 06, 47 (x1 each). Predecessors: 89, 39, 79, 55, 65, 52, 47, 21 (x1 each). 68->48 = 0x; 48->68 = 0x. No gender mark anywhere on 68.

**W1 — @1384 (a7_06):** `24 65 [68] 52 82 16 06`
Frame: "65 [68] 52". Adjective parse: "[65-N] [68-adj] | [52]..." — "65" is the subject-noun (fem32e PROMOTE), 68 post-nominal adjective, clause boundary before 52 (52 = noun-shaped, see below). Noun rival fails ("la [65] [68-N]" noun-noun ungrammatical). W1 FAVORS adjective.

**W2 — @1442 (a7_09):** `52 [68] 59 37 64`
Adjective parse: "52 [68-adj] est [37-pred]" = "[N] [adj] est [pred]" — grammatical, and 37 is independently adjective-class (A1 predicative grant; "52 37" x4 post-nominal frames at @1124/@1129/@1356/@1722; "la 52" x3 at @1006/@1123/@1721 = "la" + feminine noun, so 52 is a feminine noun).
Two hard tensions found:
- (a) Gender: "la 52" x3 makes 52 feminine; an agreeing 68 would need the feminine mark (68-48), which occurs 0x anywhere in the stream (and 48->68 also 0x). A feminine naming is unsupported; a masculine naming in a feminine agreement slot is ungrammatical.
- (b) Rival re-parse: "[68] est [37]" = subject-noun + est + predicative — "X 59 37" is a real frame-type with six instances on the stream: X in {44@528, 14@624, 83@912, 48@1178, 68@1443, 94@1796}. The subject-noun reading of @1442 is structurally licensed and avoids the gender tension entirely.
W2 is SPLIT: adjective parse live but tensioned; noun re-parse clean.

**W3 — @1788 (a8_09):** `21 [68] 47 03 00 86`
Frame: "21 [68] 47(ce)". Adjective parse: "[21] [68-adj] | ce [03]..." — post-nominal adjective with clause boundary before 47='ce'; "ce [03] pour [86]" parses as "ce [03-être] pour [inf]" ("c'est pour [inf]" grammatical, conditional on 03's open value). Noun rival fails ("21 [68-N]" noun-noun ungrammatical). W3 FAVORS adjective.

**Out-of-bar 68 windows (constrain a global value):**
- @1719 (a8_07): `47 [68] 06 11 52 37` = "ce [68] [ent] la [52] [37-adj]". "ce [68] ent" reads "ce [N] [V-ent]" (06='ent' verb ending) — noun-favoring; meanwhile "la [52] [37]" confirms 37 in the adjective slot two pairs later. Directly tensions a global adjective value for 68.
- @884 (a5_08): `79 [68] 37` = "tout [68] [37]": if both 68 and 37 are adjectives, "tout [adj] [adj]" is ungrammatical — stacked-adjective tension, forces a class decision at @884.
- @504: `39 [68] 21` (39='a/à' promoted); @114: `89 [68] 21`; @1286: `55 [68] 00`.

## Per-clause pass/fail

- (C1): FAIL at battery grade. No stream-anchored adjective value exists for 68: no compositional value frame (no 68-48 mark, no formula, no GT-anchored leg), and every French adjective parses W1–W3 grammatically — any naming (e.g. "grand") would be stipulative, and promote on a stipulation is circular. The value-naming requirement of the bar is unsatisfiable at battery grade. Recorded as a finding per §2 (counts toward null).
- (C2): NOT MET. Class-level: W1 and W3 favor the adjective parse; W2 is split (gender tension + licensed noun re-parse "68 est 37"). Global zero-hard-contradictions fails: @1719 ("ce [68] [ent]", noun-favoring) and the stacked-adjective tension at @884 cannot coexist with a uniform adjective 68 under the §7 sole-polyvalence rule (67 et/veut); resolving the split is red-team venue per the parent report and/or pending the in-flight val-68-noun-sweep — not decidable at battery level.
- (C3): DOES NOT FIRE. No gendered naming can be earned: feminine -e needs 68-48 (0x, and 48->68 0x; "la 52" x3 shows the @1442 noun is feminine, so an unmarked 68 cannot agree there); a masculine naming would be stipulative. The gender-65 agreement test stays closed, consistent with the parent fence.

## Verdict: NULL

Not promote: C1 unsatisfiable (no nameable value) and C2's zero-hard-contradictions fails on the §7 noun/adjective split (@1719, @884, @1442 rival re-parse). Not kill: no window forces the three post-nominal windows non-adjective, and no cleaner rival value is demonstrated on the same frames (the noun rival is in flight as val-68-noun-sweep, not a verdict). No standing red-team verdict contradicted or downgraded. Adverses answered (65 unmarked confirmed; 59='est' provisional flagged at W2 and the @1442 rival re-parse). Canonical-stream caveat stands.

## Follow-ups (for supervisor queuing; all verified absent from battery-queue.json)

1. `adj-68-value-anchor` (P3) — value-anchoring battery for 68's adjective arm: census all 8 windows for a compositional value frame; no anchored value found at battery grade; required before any adjective promote can be re-run.
2. `split-68-class-adjudication` (P3) — adjudicate 68's noun/adjective split with discriminating frames: @884 "79 68 37" stacked-adjective tension ("tout [adj] [adj]" ungrammatical); @1442 rival re-parse as subject-noun "[68] est [37]" (one of six X-59-37 frames: X in {44,14,83,48,68,94}); @1719 "47 68 06" ("ce [68] [ent]", noun-favoring) vs the same row's "11 52 37" (adjective-confirming for 37). Resolve at battery grade or escalate to red team.
3. `gender-68-fence` (P4) — fence 68's gender route: 68↔48 zero contact both directions; "la 52" x3 makes 52 feminine so a feminine 68 at @1442 would need the absent mark; record the fence so the gender-65 agreement re-open stays closed pending any future marked 68.

## Bookkeeping

- Queue: `adj-68-postnominal` → status `verdict`, result `null`, date 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; 979 targets intact; no downgrade).
- Lock `locks/adj-68-postnominal.lock` created on start, deleted on completion (verified gone).
- `canonical.py` never used; R5005, sealed gates, red-team adjudication queue untouched.
