# Battery verdict: w2-pas-nelicense

## Bar (verbatim, pre-registered)

"name ONE grammatical mechanism covering >=2 of them (e.g. word-internal '[verb]pas', 'pas'-noun, clause-boundary) or confirm ne-drop as lane precedent; if word-internal '[X]pas' wins, re-test W2's '[26]pas' under it"

Restated as numbered clauses:
- **C1:** ONE grammatical mechanism (word-internal '[X]pas', 'pas'-noun, clause-boundary, or other) covers >=2 of the four windows (@1269, @1729, @1222, @742 — 0-based indices of the 30 token per the brief's convention), OR
- **C2:** ne-drop is confirmed as lane precedent (the cipher writes bare "pas" for negation as its normal habit).
- **C3 (conditional):** if word-internal '[X]pas' wins, re-test W2's '[26]pas' under it.

## Method

Read BATTERY-PROTOCOL.md first. Created `locks/w2-pas-nelicense.lock` on start (agent id + UTC timestamp). Re-derived the repaired stream in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `repair_parse.py` (upstream tokenization, byte-exact). Verified: **1,847 pairs / 96 types**. `canonical.py` never touched. R5005, sealed gates, red-team adjudication queue untouched.

Offset convention: the brief's @-offsets are **0-based indices of the 30 token**. 1-based equivalents: @1269→1270, @1729→1730, @1222→1223, @742→743. I cite the brief's 0-based form below with 1-based in parentheses on first use.

## The four windows (byte-exact, ±7 context, 1-based)

- **@1269** (1b @1270, row a7_02): `01 09 11 50 | 46 69 88 24 30 20 64 47 76 | 87 76` = "[01] [09] la [50] que [69] [88] [24] pas [20] qui ce [76] ce [76]"
- **@1729** (1b @1730, row a8_07): `11 52 37 43 98 39 88 24 30 15 01 56 30 06 60` = "la [52] [37] [43] vient à [88] [24] pas [15] [01] [56] pas [06] [60]"
- **@1222** (1b @1223, row a7_01): `45 36 77 83 92 61 24 48 30 09 20 57 64 79 82` = "ce [36] le de [92] [61] [24] e pas [09] [20] [57] qui tout m…"
- **@742** (1b @743, row a5_02): `93 76 18 82 06 00 36 20 30 67 77 81 85 28 00` = "[93] [76] [18] m ent pour [36] [20] pas et le [81] [85] [28] pour"

Standing values used: 30='pas' (promoted, never re-litigated), 94='ne' (STRONG LEAD R17-001), 24 = finite verb class / infinitive-taking (battery-promoted, value NOT named — 'faire' was explicitly not promoted), 88 = verb class (promote; locus-level infinitive), 98 = finite verb class-level, 67 = et/veut positional rule, 48='e' letter-tier (R17), 46='que' GT, 96='par' GT, 00='pour' A9, 77='le' provisional.

## Distributional result: "ne" is absent at 16 of 19 'pas' windows

For each of the 19 windows of 30, I scanned ±10 pairs for 94:

| 30 (0-based) | 94 within ±10 | genuine "ne…pas"? |
|---|---|---|
| 30 | none | no |
| 45 | none | no |
| 483 | none | no |
| 560 | 94 at -2 ("94 59 30" = "ne est pas") | **yes** |
| 656 | 94 at -5 ("82 94 76 49 24 26 30" — "ne [76-noun]" ungrammatical; different clause) | no |
| **742** | **none** | no |
| 993 | none | no |
| 1114 | none | no |
| **1222** | **none** | no |
| 1251 | none | no |
| **1269** | **none** | no |
| 1309 | none | no |
| 1327 | 94 at +3 ("30 06 62 94 70" — "ne" opens the following "ne pre…" clause) | no |
| 1368 | 94 at -5 ("62 94 79 14 60 03 30" — separated by 4 pairs; different clause) | no |
| 1561 | none | no |
| 1702 | 94 at -1 ("33 94 30" = "ne pas"; the 'n'importe' window) | **yes** |
| 1716 | 94 at -3 ("65 94 44 59 30" = "ne [44] est pas") | **yes** |
| **1729** | **none** | no |
| 1733 | 94 at +9 (following clause) | no |

Only **3 of 19** 'pas' windows show a genuine "ne…pas" (@560 "ne est pas", @1702 "ne pas", @1716 "ne [44] est pas"). **16 of 19 lack "ne"**, including all four audited windows (zero 94 within ±10 pairs at @1269, @1729, @1222, @742). The cipher writes "ne" when it writes it (the three genuine frames prove the capability); its normal habit is bare "pas".

## Mechanism tests (C1)

**'pas'-noun ("step"):** FAILS at all four windows. A bare noun "pas" after a verb requires a determiner in 1841 French ("faire un pas", not "faire pas"); no determiner is present at any window. @1222's "[48] pas" = "e pas" is not a French word under the letter-tier 48='e'. Covers 0/4.

**Clause-boundary:** FAILS. No byte evidence for a boundary at any window (all four mid-row: a7_02, a8_07, a7_01, a5_02). The resulting fragments are ungrammatical: @1269 "Pas [20] qui…" (verbless "pas" + relative without verb), @742 "Pas et le…" ("pas et" ungrammatical), @1729's "pas …, pas …" (bare "pas X, pas Y" is colloquial, not 1841 diplomatic French). Covers 0/4.

**Word-internal '[X]pas':** FAILS. No French word is statable at any window under standing values: "24 30" with 24 = finite verb class cannot form a word (no French verb ends "-pas"); "30 20", "30 15", "30 09", "30 67" with open followers form no word; @1222 "48 30" = "e pas" is not a word. Covers 0/4.

**"pas même" / "pas un" spot-check:** would require 20/15/09 to each be "même"/"un" — three distinct groups cannot share one value. Not statable; rejected without inventing values.

**Result: no grammatical mechanism covers ≥2. C1 FAILS.**

## Ne-drop precedent (C2): CONFIRMED

**C2 PASSES.** The distributional table above is the confirmation: 16/19 'pas' windows have no "ne", the cipher demonstrably can write "ne…pas" (3 windows), and all four audited windows are ne-less. The pas-30 battery's "Parses." marks stand undisturbed — this audit supplies the missing mechanism: **bare "pas" carries negation; "ne" is dropped as the cipher's normal habit** (whether plaintext ellipsis or encoder economy is not decidable from bytes and is not claimed).

## C3 (conditional)

Word-internal '[X]pas' did not win (0/4). The antecedent is false; **no re-test of W2's '[26]pas' is owed**. (Independently, battery noun26-26n-exclude, verdict/null 2026-10-09, already fenced the '[26n]' one-word rival at 2 of 3 la-windows.)

## Verdict: PROMOTE (finding grade)

C2 passes with byte-grade evidence; no adverses were listed; no standing verdict is contradicted or downgraded (30='pas' promote untouched — this audit explains its ne-less windows, it does not re-grade them; 94='ne' STRONG LEAD untouched). Promotes no value; confirms a lane precedent.

## Standing-state check

- pas-30 (promote): undisturbed — its "Parses." marks are now mechanized, not overturned.
- ne-24-profile (promote, class-level): used as stated — 24's value remains open; 'faire' was never promoted and is not assumed here.
- 94-duality / R17-001: untouched — 94='ne' stands where 94 appears.
- §7: no polyvalence declared.
- `canonical.py` never used; R5005, sealed gates, red-team queue untouched.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-w2-pas-nelicense.md` (this file)
- Queue: `battery-queue.json` `w2-pas-nelicense` → status `verdict`, result `promote`, date 2026-10-09 (temp-file + rename; pre-write assert confirmed queued/verdictless; JSON re-validated post-write)
- Lock: created on start, deleted on completion.
