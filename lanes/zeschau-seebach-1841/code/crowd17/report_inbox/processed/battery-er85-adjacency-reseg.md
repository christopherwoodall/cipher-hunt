# Battery `er85-adjacency-reseg` — verdict: NULL

- Worker: battery worker er85-adjacency-reseg, agent 4113ac2e-250e-4bbe-a635-566880e4168c
- Date: 2026-10-09 (lock created 2026-10-09T20:29:42Z; no prior lock, fresh run)
- Stream: repaired 1,847-pair / 96-type parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed like repair_parse.py). Re-derived in-session; asserts held: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched. All @-offsets are 0-based repaired-stream pair indices.

## Bar (verbatim, pre-registered)

"exclude 'laisser' at these windows iff a licensed re-segmentation parses with stated values; keep iff all three license it; package as conditioned-split input iff exclusion is locus-local with cause stated"

Numbered clauses (derived before testing, not modified after):
- C1: Exclude 'laisser' at a window iff a licensed re-segmentation of that window parses with stated values (under which 'laisser' cannot stand).
- C2: Keep 'laisser' iff all three windows license it.
- C3: If 'laisser' is excluded at (some of) these windows but viable elsewhere, package the locus-local exclusion as conditioned-split input for the red team.
- Adverse: do not declare a split at battery grade — package as red-team input only.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/er85-adjacency-reseg.lock` on start; deleted on completion.
2. Re-derived the repaired stream in-session. "29 85" occurs exactly 3x stream-wide — these are the only three windows. Byte-confirmed (0-based 85-positions; the parent's "@97/@375/@1234" are 0-based indices of 85 — identical loci):
   - W1 @97: `41 98 81 97 46 29 [85] 08 21 62` (0-based @91–100)
   - W2 @375: `17 06 21 65 63 29 [85] 82 48 00` (0-based @369–378)
   - W3 @1234: `82 48 29 47 33 29 [85] 56 10 03` (0-based @1228–1237)
3. Adopted, never re-litigated: 29='er' pencil GT; 46='que' GT (registry); 47='ce' granted (A4); 85 verb-stem frame (A3, value open); er85-word-census PROMOTE ('29 85' never composes as a word); A10 ("33+29" composition); registry 33=["INF","cls"], 63=["verb","cls"]; 97 infinitive-class (frame-97-profile PROMOTE, class-level); wordbound-63-29-373 NULL (both arms fenced, 2026-10-09); laisser-85-15window NULL (parent, 2026-10-09); stem-85-value-rerun NULL (2026-10-09); laisser-85-1699 (locus kill of the @1699 causative leg, 2026-10-09).

## Findings

### Re-segmentation inventory (per window)

Standing attachment licenses for 29 between X and 85: (a) 29→X leftward (inflectional ending on a stem); (b) 29→85 rightward — KILLED at battery grade (er85-word-census PROMOTE); (c) 29 bare — ungrammatical ("er" is not a French word). No standing license exists for any 85-rightward composition at these windows ("85 08" / "85 82" / "85 56" — all unlicensed; "85 48" fenced at @1278; 08='t' is battery-grade unratified in any case).

- **W3 (@1234): `47 33 29 [85] 56`.** Licensed re-segmentation parses: `47 | 33+29 | 85 | 56` = "ce" (granted) + "[33]er" (A10 grants "33+29"; 33 INF-class) + 85 + 56 (open). Parses with standing values. ✓
- **W2 (@375): `65 63 29 [85] 82`.** wordbound-63-29-373 (NULL, today) fenced BOTH arms at kill grade: fused "[63]er" dies (63=[verb,cls] has no licensed stem-tier reading for infinitive composition; "bare infinitive after a noun" killed by locus-368-fullparse route 7) and split "63 | er" dies ("29 85" composition exhausted per er85-word-census; bare "er" not a word). NO licensed re-segmentation parses. W2 is a segmentation residual.
- **W1 (@97): `97 46 29 [85] 08`.** 29→46 yields "46 29" = "que"+"er" — not a licensed word (46='que' GT; "queer"/"quer" is not French). The parent's "[X]er infinitive" premise is unlicensed here as stated. Only structurally-live candidate: three-cell "97 46 29" = "[97]quer" (-quer infinitive; 97 is infinitive-class PROMOTE, but stem-tier vs whole-word tier is unproven and 97's value is open, so wordhood is unproven). NO licensed re-segmentation fully parses with stated values. W1 is a segmentation residual pending 97's tier/value.

### 'laisser' exclusion (per window)

French syntax (battery grade): a bare infinitive immediately followed by "laisser" (any form) has no licensed frame — no "[V-inf] [V-fin]", no "[V-inf] [V-inf]" without preposition or coordinator, and the "faire laisser" causative stack requires finite "faire" governing "laisser" directly. The three windows' left contexts supply no governor and no coordinator (W3: "ce"; W2: "21 65" nouns; W1: "81 97"), and the only nearby "pour" (W2 @378) sits after 85 and cannot govern retroactively (adopted wordbound-63-29-373).

- **W3:** Under the licensed parse "ce [33]er | 85 | 56", 'laisser' is EXCLUDED at kill grade — "[33]er laisser" instantiates the ungrammatical "[V-inf] laisser" adjacency, and no licensed re-segmentation avoids it (29→85 killed; 85→56 unlicensed; X+29+85 fused unlicensed).
- **W2:** 'laisser' excluded a fortiori — the window admits no licensed word segmentation at all (residual); the "[X]er laisser" frame cannot be constructed. Cause: the "63 29" boundary fenced both ways (adopted wordbound-63-29-373).
- **W1:** 'laisser' excluded a fortiori — "46 29" is not a licensed word, so the parent's "[X]er laisser" premise fails as stated; under the only live candidate ("97 46 29" = "[97]quer" | 85), the "[V-inf] laisser" adjacency is ungrammatical. Cause stated; the three-cell candidate's wordhood is unproven (pending 97).

### Rival -er-stem test

The "[V-inf] [V]" exclusion is class-wide, not 'laisser'-specific: under the windows' contexts, no -er verb lexeme in any form (finite, infinitive, or stem) can follow a bare infinitive in French. Zero rival -er stems survive at any of the three windows. These loci cannot discriminate among -er stems and cannot support any -er-verb value-naming at 85.

### Realization-layer note (recorded, not relied on — red-team venue)

Under A3 (85 verb-stem), surfacing "laiss-" as "laisser" would need 85+29 (29 sits left of 85 at all three windows; "29 85" killed), and as "laisse" would need an -e completion (right neighbors 08/82/56 supply none). This argument has GLOBAL force (29='er' is 0x after 85 stream-wide per stem-85-value-rerun) and would implicate the parent's other-window parses; it is recorded for the red team, not litigated here. The exclusions above rest on the window-specific syntax argument, which is independent of it.

### Per-clause assessment

- **C1:** FIRES for W3 — a licensed re-segmentation parses with stated values, and 'laisser' is excluded under it at kill grade. For W2/W1 the iff-condition fails: no licensed re-segmentation parses (both are segmentation residuals), so the bar as written is untestable there; the exclusion holds a fortiori with stated cause. → Clause not satisfied as written across all three windows.
- **C2:** Antecedent false — no window licenses 'laisser' under any live segmentation. Correctly does not fire; 'laisser' is NOT kept.
- **C3:** The exclusion is locus-local with cause stated per window — 'laisser' excluded at the three "[X]er _" loci but viable at the parent's other windows (adopted laisser-85-15window: 11 parse; CAVEAT for the red team: @1699's causative leg — the parent's strongest — was locus-killed today by laisser-85-1699, and @1278 is uncertain, so the viable set needs a recount). → PACKAGE DELIVERED below. Adverse honored: no split declared at battery grade.

### §7 conditioned-split package (for the red team)

- Shape: 'laisser' viable at the non-"[X]er" windows vs excluded at the "[X]er _" ×3 loci (W3 kill grade; W2/W1 as residuals with stated cause).
- Adjudication options: (a) conditioned split ('laisser' iff not post-"[X]er"); (b) global kill of 'laisser' (if the realization-layer argument is pressed — it has global force); (c) re-parse of the W1/W2 residuals (follow-ups 1–2 below).
- Inputs: this report + laisser-85-15window (parent) + wordbound-63-29-373 + er85-word-census + stem-85-value-rerun + laisser-85-1699 + frame-97-profile.

## Verdict: NULL

The re-segmentation audit ran to completion on all three windows, but the bar's C1 mechanism (exclude-via-licensed-re-segmentation) is untestable as written at W1/W2 — no licensed re-segmentation parses there; both are segmentation residuals. Per protocol §2/§4 this is recorded as a finding and the verdict is NULL. Firm deliverables stand regardless: W3's kill-grade exclusion of 'laisser', the class-wide rival -er-stem exclusion (zero survivors), and the C3 conditioned-split package. No standing or red-team verdict contradicted, downgraded, or re-litigated; §7 intact (no split declared). Canonical-stream caveat stands.

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `seg-97-46-29-quer` (P4) — W1: test the three-cell "97 46 29" = "[97]quer" re-segmentation (97 is infinitive-class PROMOTE; determine stem-tier vs whole-word tier, or constrain 97's onset); license or fence the -quer reading.
2. `reseg-375-repair` (P4) — W2: the "63 29" boundary fenced both ways (wordbound-63-29-373); audit the wider ±4 context for any licensed repair, or confirm W2 as a hard residual.
3. `stem-85-er-windows-surface` (P4) — given the class-wide -er exclusion at the three "29 85" windows, audit whether 85 can surface at ALL under A3 at these loci (realization), or whether the loci force a non-stem reading (escalate to red team if so).

## Scope

Excludes the 'laisser' lexeme at @97/@375/@1234 only (W3 kill grade; W2/W1 a fortiori as segmentation residuals with stated cause). The rival test excludes every -er stem at these loci equally. Untouched: the parent's other-window assessments (adopted, with the @1699/@1278 caveat noted for red-team recount), the A3 frame grant, 85's global value, er85-word-census, all standing/red-team verdicts, §7. No value named, no class named, no split declared. Canonical-stream caveat stands.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-er85-adjacency-reseg.md`
- Queue: `er85-adjacency-reseg` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique temp file `battery-queue.json.er85-adjacency-reseg.tmp` + atomic rename; disk re-validated; own entry only; no downgrade)
- Lock `locks/er85-adjacency-reseg.lock`: created on start, deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
