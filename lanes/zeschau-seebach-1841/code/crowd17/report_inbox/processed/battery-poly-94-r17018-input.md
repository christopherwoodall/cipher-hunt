# Battery report: poly-94-r17018-input

- Target id: `poly-94-r17018-input` (P2)
- Claim: RED-TEAM INPUT — package the [42ne]/[62ne] word-final-'ne' segmentation family as ruling-ready input for the R17-018 red-team docket.
- Date: 2026-10-09
- Worker: battery worker (subagent df32dd61-8957-4875-891e-4ae808f38bc4)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`); `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.

Terms (ASD-STE100): "word-final-'ne'" = 94 as the bound syllable "-ne" at the end of a word ("...ne"), distinct from the free verbal negator particle ("ne"). "R17-018" = the red-team escalation on the 12/94 "ne" duality. This report packages evidence only. No value is named. No adjudication is made. No second 94 value is declared (§7: 67 et/veut is the sole true polyvalence; battery declares none).

## Bar (verbatim, pre-registered before testing)

"Package the [42ne]/[62ne] word-final-'ne' segmentation family (wordless6 + frame-42-94-leftward) as ruling-ready input for the R17-018 red-team docket; no battery-level duality declaration"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** the [42ne] and [62ne] word-final-'ne' segmentation family (adopting `seg-62-94-wordless6` and `frame-42-94-leftward` with their current verdicts, plus later deltas) is packaged with byte-exact window tables, standing values, adopted battery-grade readings, and the stated red-team questions.
2. **C2:** no battery-level duality is declared; the package is gather-only, R17-018's fence is not pre-empted, and no standing/red-team verdict is contradicted or downgraded.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/poly-94-r17018-input.lock` on start (2026-10-09T18:45:02Z); no prior/stale lock present.
2. Gather-only: no new stream testing. All @-offsets cited are 0-based repaired-stream indices as byte-verified by the adopted batteries (their reports give the derivations; none is re-litigated here).
3. Adopted (not re-litigated): `seg-62-94-wordfinal` KILL (2026-10-09); `seg-62-94-wordless6` PROMOTE (2026-10-09); `frame-42-94-leftward` NULL (2026-10-09); `val-42-ne-noun` KILL (2026-10-09); `dual94-r17018-scope` PROMOTE (2026-10-09); `ne-94-right-context` PROMOTE (2026-10-09); `ne-24-profile` PROMOTE (2026-10-08); R17-001 (94='ne' STRONG LEAD); R17-002 (12='n'); R17-018 (12/94 "ne" duality FENCED as compatible mechanism); R19-055 (42=['noun','cls']); R18 (65=['noun']).
4. Canonical-stream caveat stands (68/70 upstream row offsets unvalidated); every window below is a canonical-offset object.

## A. Docket reference — R17-018

Verbatim (next-token-redteam-r17, §C): "**R17-018: 12/94 'ne' duality — FENCED as compatible mechanism.** The analytic (12-48) vs syllabic (94) spellings of 'ne' are the homophonic cipher's ordinary mechanism, not a contradiction. Neither 12='n' (R17-002) nor 94='ne' (R17-001) is downgraded."

The docket question this package feeds: does R17-018's fenced 12/94 duality already cover **bound word-final "-ne"** (the [62ne] windows, and the now-weakened [42ne] windows), or does the word-final reading need a separate declaration (`redteam-94-functional-split`, queued, untouched)?

## B. The [62ne] family (62-94 windows)

Bigram census (adopted, byte-verified): **'62 94' exactly x9** — 62 at @100, @508, @761, @840, @1329, @1362, @1686, @1704, @1772 (94 at +1 each). n(94) = 37.

| Window (94 idx) | row | battery verdict |
|---|---|---|
| @101 | a1_02 | wordless6 W1: verb-less, NO clean reading either class (gap, not kill) |
| @509 | a3_00 | wordless6 W2: word-final-'ne' DEMONSTRATED ("et le [W]ne qui [98]"; resolves R17-022 residual) |
| @762 | a5_03 | wordless6 W3: nominal word-final-'ne' (subject of "est") |
| @841 | a5_06 | wordless6 W4: verb-less; weak verb-shaped word reading (outlier) |
| @1363 | a7_06 | wordless6 W5: nominal word-final-'ne' (V+O under promoted 92 verb-class) |
| @1687 | a8_05 | wordless6 W6: nominal word-final-'ne' (S-V-O-Adv under R18 65-noun + 93 verb-class) |
| @1330 | a7_04 | attachable: particle-'ne' stands (conditional) |
| @1705 | a8_06 | attachable: particle-'ne' stands (clean, "il ne [88-V] [26]") |
| @1773 | a8_09 | attachable: particle-'ne' stands (promoted, ne-24-profile; kill-grade falsifier of the x9 word claim) |

Standing results (all 2026-10-09, battery grade unless noted):
- `seg-62-94-wordfinal` KILL: the x9-as-word-final-'ne' claim is false at kill grade (@1772 forces a word break under standing promoted values).
- `seg-62-94-wordless6` PROMOTE (scoped): word-final-'ne' segmentation SUPPORTED at the 6 D3-un-attachable windows, W predominantly noun-class (4/6: W2 clean, W3/W5/W6 slot-clean; W1 gap; W4 weak-verb outlier). @1363/@1687 tension resolved (both noun under the best parse). 62's value not named; W1's gap not a kill.
- `dual94-r17018-scope` PROMOTE: the 6 + 3 package already delivered as ruling-ready input for R17-018 with the three-way red-team question: (a) declared positional/functional split, (b) R17-018 duality coverage, (c) stem-owned "-ne".
- `ne-94-right-context` PROMOTE: 37-window right-context census; 11/37 windows provably cannot be the verbal negator (6 word-final '-ne' + 5 other non-particle frames); 7 clean verbal-negator windows (+ 8 conditional).

## C. The [42ne] family (42-94 windows)

Bigram census (adopted, byte-verified by `frame-42-94-leftward`): **'42 94' exactly x3** — 42 at @493 (row a2_11), @784 (row a5_04), @1794 (row a8_09); 94 at +1 each.

- `frame-42-94-leftward` NULL (2026-10-09): "[42ne]" noun is the only live class (verb/adjective/adverb/pronoun arms dead or class-contradicting) but does not parse all three windows under standing values: W3 (@1794, '[42ne] [59=est] [37]') parses clean under provisional 59='est' + granted A1; W1 (@493) parses only with 78/02 X-slots fenced; W2 (@784) fails under standing values (finite-modal 24 + noun = ungrammatical) — live ONLY under the docketed 24='en' arm (red-team venue). No 'n'est' leg contradicted (only a conditional @1795 leg displaced, never kill-grade); no §7 polyvalence declared (segmentation framing per wordless6).
- **`val-42-ne-noun` KILL (2026-10-09, NEW since frame NULL): [42ne]-as-noun-word is dead.** Exhaustive inventory: 723 -ne-final noun types over a 41,923-word 1841-French vocabulary tested against the joint demands (i) standalone-word, (ii) "er"+S one word (T3), (iii) S+"ne" a noun, (iv) bare-capable — exactly ONE stem ("re") satisfied (i)+(ii)+(iii) and it was already killed on bare-noun grounds (`noun-42-value`, 1/20). All other candidates fail (i), (ii), or (iv). Window-level confirmation: no -ne noun parses as a BARE word at @493, @784, or @1794 under standing values (78='ver'-syllable lead is not a determiner; 24 is finite-modal; 56 is class-open).
- Consequence: the noun arm of [42ne] is battery-killed. The composition now survives only as the conditioned/docketed form (W2 under 24='en'); if 24 resolves modal, the noun-[42ne] promote is dead at W2 as well (see `w2-42-94-24en-gate`, still queued).
- Cross-cite: the [42ne] kill sharpens the R17-018 coverage question in §A — the word-final-'ne' segmentation family's surviving live residue is now essentially the 62-94 windows (4/6 nominal at battery grade) plus the docketed W2 remnant.

## D. The red-team question (packaged, not answered)

Two battery-promoted facts stand side by side, unchanged by this package:

1. At 7+8 windows, 94 is the free verbal negator particle (R17-001 STRONG LEAD; cleanest @1705, @1773).
2. At 6 windows, 94 is the bound word-final '-ne' syllable of a noun-shaped word at battery grade (cleanest @509 "et le [W]ne qui" — the R17-022 residual resolved — and @1687 S-V-O-Adv under R18 65-noun + promoted 93 verb-class).

The red team decides between:
- **(a)** a declared positional/functional split for 94 (preverbal negator vs word-final "-ne", cf. the 67 et/veut precedent) — the lane's second true polyvalence;
- **(b)** R17-018's fenced 12/94 duality already covering bound word-final "-ne" (analytic vs syllabic "ne" as ordinary homophonic mechanism) — open sub-question: does "compatible mechanism" extend to bound "-ne", or only to the free-particle vs analytic spellings?;
- **(c)** word-final "-ne" belonging to the stems, not 94 (boundary artifact) — killed for the x9 62-94 claim at @1772 but NOT tested at W2/W5/W6 (the "prenne" anchor x2 keeps a syllabic-94 precedent live: 70-12-94 = 'pre'+'n'+'ne', battery-verified).

This package declares none of (a)/(b)/(c).

## E. Jurisdictional ledger

| Item | state | red-team venue |
|---|---|---|
| R17-001 94='ne' STRONG LEAD | stands | — |
| R17-002 12='n' | stands | — |
| R17-018 12/94 "ne" duality | FENCED (compatible mechanism) | owns the declaration |
| [62ne] word-final-'ne' (4/6 nominal, battery grade) | segmented, not valued | `redteam-94-functional-split` (queued) |
| [42ne]-as-noun-word | KILLED (`val-42-ne-noun`, 2026-10-09) | — |
| [42ne] conditioned (W2 under 24='en') | docket-gated | 24-en-verb-conflict + `w2-42-94-24en-gate` (queued) |
| Any second 94 value | NOT declared | §7: 67 only |
| Canonical offsets | 68/70 unvalidated | red-team offset adjudication |

## Per-clause pass/fail

1. **C1 PASS** — the [42ne]/[62ne] word-final-'ne' segmentation family is packaged above (§A–E) with byte-exact window tables, standing values, adopted battery-grade readings (seg-62-94-wordless6 PROMOTE, frame-42-94-leftward NULL, val-42-ne-noun KILL, dual94-r17018-scope PROMOTE), and the red-team question stated without adjudication.
2. **C2 PASS** — no battery-level duality is declared; the package is gather-only; R17-018's fence is adopted, not pre-empted; no standing/red-team verdict is contradicted, downgraded, or re-litigated.

## Verdict: PROMOTE (evidence package delivered; no adjudication)

Ruling-ready input for the R17-018 red-team docket: the [62ne] family (4/6 nominal word-final-'ne' at battery grade, W1 gap, W4 weak-verb outlier, 3 attachable windows keeping particle-'ne'), the [42ne] family (noun-word arm battery-killed 2026-10-09; composition survives only conditioned on the docketed 24='en'), and the (a)/(b)/(c) red-team question with the battery evidence for each. No cipher value named. No polyvalence declared.

Continuation: `redteam-94-functional-split` (queued, untouched) owns the adjudication; `w2-42-94-24en-gate` (queued) owns the 24-gated [42ne] remnant. No follow-ups proposed (promote; the docket owns the continuation).

## Scope

- Gather-only: every byte fact above is adopted from its cited battery report; nothing was re-tested or re-litigated in this target.
- The val-42-ne-noun KILL is a battery verdict, not red-team ratified; the red team may weigh it as it pleases.
- Canonicality caveat stands on all windows (68/70 upstream row offsets unvalidated).
- §7 intact. No standing/red-team verdict contradicted.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/poly-94-r17018-input.lock` created on start (2026-10-09T18:45:02Z), no prior/stale lockfile; deleted on completion (verified gone).
- `battery-queue.json`: `poly-94-r17018-input` status `queued` -> `verdict`, `verdict: {"result": "promote", "report": "code/crowd17/report_inbox/battery-poly-94-r17018-input.md", "date": "2026-10-09"}` (temp-file + rename; pre-write assert confirmed queued/verdictless — no downgrade; JSON re-validated; only this entry touched).
- R5005, sealed gates, red-team adjudication queue untouched. No invented numbers: every figure traces to a cited lane report.
