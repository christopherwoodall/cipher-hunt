# Battery verdict: 02-class-609

## Bar (verbatim, pre-registered)

"02's class named with >=2 frame-legs; 58's class constrained as stated consequence. Do not duplicate slot-24-fence"

Numbered clauses:

- **C1:** 02's class named with ≥2 frame-legs.
- **C2:** 58's class constrained as stated consequence (conditional: "if 02 is a finite verb, 'qui [02] [58]' constrains 58 (object/complement -> nominal signal) at the @614 locus").
- **C3 (procedural):** do not duplicate slot-24-fence.

## Method

Read BATTERY-PROTOCOL.md first; created `locks/02-class-609.lock` on start (agent id + UTC timestamp). Re-derived the repaired 1,847-pair / 96-type stream in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (parsed per `repair_parse.py`). `canonical.py` never touched; R5005, sealed gates, red-team queue untouched. Offsets below are 0-based repaired-stream indices unless marked 1-based.

## Census

n(02) = 17. Predecessors: 01 x3, 64 x2, 84 x2, 11/88/14/94/46/03/09/24/16/21 x1. Successors: 79 x2, 24 x2, 00 x2, 26/88/53/58/50/21/97/55/70/62/09 x1. **Zero verb-frame contacts** in the successor set (no 80, 89, 29='er', 85-stem, 33) — byte-confirms the ne-alone-02-74 distributional arm.

## Window-level evidence

- **@609 (0-based; 1-based @610, row a4_00):** `54 64 39 64 02 58 47 77 87` = "[54] qui(64) [39] qui(64) [02] [58] ce(47) le(77) ce(87)". The target window: "qui [02] [58]". 64='qui' banked GT; 47='ce' A4 granted; 77='le' provisional; 39 open.
- **@750 (0-based; 1-based @751, row a5_03):** `85 28 00 64 02 97 40 67 11` = "[85] [28] pour(00) qui(64) [02] [97] e(40) et/veut(67) la(11)". Second "qui [02]" window; 85 verb-stem A3; 40='e' GT.
- **@305 (0-based; 1-based @306, row a2_04):** `91 18 89 88 02 88 20 17 46` = "[91] [18] [89] [88] [02] [88] [20] fois(17) que(46)". 88 = verb (class-level, battery-promoted 2026-10-09).
- **@858 (0-based; 1-based @859, row a5_07):** `64 32 48 84 02 24 49 74 74` = "qui(64) [32] e(48) on(84) [02] faire(24)…". 84='on' A15 unconditioned; 24='faire' battery-promoted.
- **@128 (0-based; 1-based @129, row a1_03):** `98 82 48 11 02 26 32 96 56` = "[98] m(82) e(48) la(11) [02] [26]…". 11='la' banked GT; 82='m' GT.

## Per-clause results

- **C1 (name 02's class with ≥2 frame-legs): FAIL, split signature.** No class commands ≥2 consistent legs:
  - *Finite verb:* the two "qui [02]" windows (@609, @750) are verb-selecting — a relative "qui" requires a finite verb, and no word-boundary rescue is byte-evidenced (mid-row both; 64='qui' is a complete banked word, no elision available). But @305 ("[88-verb] [02] [88-verb]") forces 02 non-finite — three finite verbs in a row is ungrammatical, and no clause boundary is byte-evidenced. @858 ("on [02] faire") likewise forces 02 non-finite ("on [V-fin] faire" ungrammatical; boundary rescue "on. [02] faire" strands "faire" without subject — pro-drop ungrammatical in 1841 French). The full-profile distributional test (ne-alone-02-74, kill) independently found zero verb-frame contact in all 17 windows.
  - *Noun:* @128 "la [02] [26]" parses ("la [noun] [adj]"-shaped, 11='la' banked); @1467 "21 [02]" (1-based @1468) is noun-adjacent. But "qui [noun]" x2 (@609, @750) is ungrammatical in French at any period.
  - *Conjunction/adverb:* @305 "[88] [02] [88]" is conjunction-shaped ("verb [conj] verb") but @128 "la [02] [26]" kills it ("la [conj]" ungrammatical) and @858 "on [02] faire" kills adverb/noun readings too.
  - *Pronoun/determiner/adjective:* each dies at ≥1 of the five key windows (pronoun/determiner after "qui" ungrammatical; bare adjective readings lack a head).
  - The profile is irreducibly split: verb-signals at the qui-windows vs non-verb forced at @305/@858 vs nominal signals at @128. This is a §7 split candidate — red-team territory, not declared here.
- **C2 (58's class constrained): CANNOT FIRE.** The consequence was conditional on 02 being a finite verb at @609; the condition is not established (see C1). Noted for the record: *if* 02 were finite-verb at @609, "qui [02] [58] ce le" would require 58 as object/complement → nominal signal on 58. That conditional remains available to cede-614-subject's venue; nothing here blocks it.
- **C3 (no duplication of slot-24-fence): HONORED.** slot-24-fence concerns 24's slot; not re-litigated or duplicated.

## Standing-state check

Consistent with battery-ne-alone-02-74 (kill, 2026-10-09): its distributional arm (zero verb-frame contact) is re-confirmed byte-exact here; its killed claim ("02 is the negated verb in 42 ne 02") is not re-litigated. No red-team verdict on 02's class exists; nothing contradicted or downgraded. §7 honored — no polyvalence declared.

## Verdict: NULL

02's class cannot be named at battery grade. The qui-windows (x2) are genuine verb-selecting legs, but they are contradicted at battery grade by the non-finite-forcing windows (@305, @858); the resulting split is packaged for the red team.

## Follow-ups (for supervisor queuing)

1. `qui-02-750-parse` (P3) — deep parse of the second qui-window @750 ("64 02 97 40 67"); test whether 97's class or a word-boundary account dissolves the verb requirement there. If it does, the qui-legs drop to one and the anti-verb side wins outright.
2. `conj-02-306` (P3) — test 02 as conjunction at @305 and @858 jointly: name a French conjunction candidate fitting "[88] [02] [88]" while surviving "on [02] faire"; fence if none parses.
3. `sub02-wordinternal` (P3) — test sub-lexical 02 composing with its right neighbor (esp. "02 58" @609, "02 97" @750, "02 26" @128); a compositional account would dissolve the class question without §7.
