# Battery report: val-08-31-letter

- Target id: `val-08-31-letter`
- Claim: name 08's letter value inside the '87 08 31' word frames (@881/@1488/@1520) under the ce-08-31-frame PROMOTE.
- Date: 2026-10-09
- Worker: battery worker (subagent f196df19-f564-447b-9a48-a48c41d3118d)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.

Terms (ASD-STE100): "letter value" = the single French letter a cipher number spells. "word-initial letter" = the first letter of a word. "battery grade" = the evidence standard of this pipeline.

## Bar (verbatim, pre-registered before testing)

"name 08's letter value within the '87 08 31' frames @881/@1488/@1520 consistent with the ce-08-31-frame PROMOTE; else fence"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** 08's letter value is named — one specific French letter — with >=2 independent legs at battery grade.
2. **C2:** the named value is consistent with the ce-08-31-frame PROMOTE: 08 fills the word-initial-letter slot of the [08][31] word at all three frames (@881, @1488, @1520), with no frame forcing a different letter.
3. **C3 (adverse):** the listed adverse ("@881 '08-iere' spelling-letter window") is answered — re-parsed cleanly, fenced with stated cause, or shown to be a misread.

Adverses listed: "@881 '08-iere' spelling-letter window".

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/val-08-31-letter.lock` on start (agent id + 2026-10-09T19:10:00Z); no prior/stale lock; deleted on completion.
2. Re-derived the repaired stream byte-exact in-session (1,847 pairs / 96 types asserted). All @-offsets below are 0-based. The brief's "@881/@1488/@1520" are the 0-based 08-positions (confirmed against ce-08-31-frame's own 1-based/0-based note).
3. Adopted, never re-litigated: pencil GT (40=e, 34=i, 29=er), 87=ce (promoted/granted), 47=ce (A4), 45=ce (A11 hold), 17=fois (battery wordbound audit), 67 et/veut positional rule (§7), 85 verb-stem (A3), ce-08-31-frame PROMOTE, R20-090 GRANT-WITH-CORRECTIONS (reading-level: @1487-1489 = "ce" + [08][31]-word, 08 word-initial letter), val-08-successor-class PROMOTE (bidirectional attachment; particle killed), standalone-08-wordrole KILL (08 only ever prefixal/sub-lexical outside 08-31), 08-vs-94-profile NULL (no 'ne'-type value), homophone-08-12-n NULL ('n'-sibling rejected).
4. Re-verified the three "08 31" loci byte-exact in-session (see below). n(08)=18 re-confirmed.

## Window-level evidence

### The three frames (0-based, byte-exact)

- **W1 @880-882** (`17 08 31`, row a5_08): `...86 78 | 17('fois') [08] [31] | 79('tout') 68...` — left neighbor 17='fois' (granted standalone in all 15 windows), right neighbor 79='tout' (A5).
- **W2 @1487-1489** (`87 08 31`, row a7_10): `...24 | 87('ce') [08] [31] | 92 39...` — left neighbor 87='ce' (granted word), right neighbor 92 (verb class). This is the R20-090 granted frame.
- **W3 @1519-1521** (`67 08 31`, row a7_11): `...91 | 67('et') [08] [31] | 24 11...` — left neighbor 67='et' (positional rule: follower 08 is not infinitive-shaped), right neighbor 24 (verb class).

"08 31" is 3x stream-wide (these three); "87 08 31" is 1x (W2). At all three, the left neighbor is a proven complete word, forcing 08 to attach right: the [08][31] unit is word-initial-08 (ce-08-31-frame C1; val-08-successor-class C1; R20-090).

### Letter legs for 08='t' (all anchored by pencil/standing values, zero new assumptions)

| # | @ | geometry | reading | anchor |
|---|---|---|---|---|
| L1 | 922 | `40 08` | "et" | 40='e' PENCIL |
| L2 | 944 | `40 08` | "et" | 40='e' PENCIL (independent window) |
| L3 | 975 | `45 08` | "cet" (ce+'t' before vowel) | 45='ce' A11 hold |
| L4 | 1592 | `47 08` | "cet" | 47='ce' A4 (independent window) |
| L5 | 60 | `08 34 29` | "tier" (-tier ending) | 34='i', 29='er' PENCIL |
| L6 | 779 | `08 29` | "ter" (-ter ending) | 29='er' PENCIL |
| L7 | 98 | `85 08` | verb-stem + "-t" (3sg) | 85 verb-stem A3 |

Seven independent legs. Rival letters 'h'/'f'/'b' died at kill grade (val-08 PROMOTE: "40 08" reads "et", no other letter parses both windows); 'n'-sibling rejected (homophone-08-12-n NULL); 'ne'-type rejected (08-vs-94-profile NULL); particle reading killed (val-08-successor-class C6: bidirectional attachment + heterogeneous right-neighbors).

### Frame-consistency check (C2)

Under 08='t', the three frames read "fois t[31] tout", "ce t[31] [92-verb]", "et t[31] [24-verb]" — t-initial [08][31] words in determiner/conjunction/noun frames. No frame is ungrammatical under 't'; no frame forces a different letter (31's value is open, so no letter is excluded by the word's identity, and no letter is forced either — the discrimination comes from L1-L7). The standalone-08-wordrole census independently records all three as "consistent with t-initial strings". The R20-090 granted geometry (08 word-initial letter) is preserved exactly.

## Per-clause pass/fail

- **C1 — PASS.** 08='t' named with 7 independent legs (L1-L7), all anchored by pencil/standing values; every live rival letter is dead at kill grade or rejected.
- **C2 — PASS.** 't' is consistent with the ce-08-31-frame PROMOTE at all three frames: 08 stays the word-initial letter of [08][31], the R20-090 granted reading is untouched, and no frame forces or excludes 't'.
- **C3 (adverse) — PASS, answered as misread with a corroborating finding.** I searched the @881 window byte-exact (0-based @874-888: `74 49 16 77 86 78 17 08 31 79 68 37 03 02 00`) for any "08"+"iere" (34 29 [40]) spelling geometry: **none exists** — no 34/29 occurs within the window near 08. Stream-wide, the sole "08"+"iere" geometry is @60 (`41 08 34 29 40` = "[41]tiere"), which is leg L5 itself: it positively SUPPORTS 08='t' (the "-tier" spelling), it does not threaten it. So the adverse, on the literal reading, is a misread (no such window at @881); on the charitable reading (check the "-iere" spelling-letter pattern against the naming), it corroborates 't'.

## Verdict: PROMOTE

**08='t'** — named at battery grade within the '87 08 31' frames. Seven independent spelling legs, all rivals dead, frame geometry (R20-090 granted) preserved, adverse answered.

## Scope (stated, not hidden)

- This names 08's LETTER value only. It corroborates — and does not duplicate or overturn — the battery val-08 PROMOTE, val-08-successor-class PROMOTE, and syllable-08-letter-value PROMOTE (all 08='t', all battery grade, all unratified).
- It makes no registry change: battery workers do not promote to the registry; ratification is red-team venue. The R20-090 frame grant ("Registry: none") is built upon, not re-litigated.
- 31's value and the [t31]-word's identity stay open (out of scope; the word is t-initial, nothing more is claimed).
- No standing or red-team verdict contradicted, downgraded, or re-litigated; §7 intact (a letter value is not a polyvalence); canonical-stream caveat stands (rows a5_08/a7_10/a7_11 offsets unvalidated).
- No follow-ups required (promote, not null). The already-queued `cet-08-975-1592` (P4) hardens the "cet" left-attachment legs further and is not re-proposed.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-08-31-letter.md` (this file).
- Queue: `val-08-31-letter` queued -> `verdict`/`promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/val-08-31-letter.lock` created on start (2026-10-09T19:10:00Z), deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
