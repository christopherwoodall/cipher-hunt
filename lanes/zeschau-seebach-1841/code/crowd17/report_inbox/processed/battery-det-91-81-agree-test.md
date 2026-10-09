# Battery report: det-91-81-agree-test

**Target:** `det-91-81-agree-test` (priority 3). Worker session 7a8c6e94-4564-4fe3-a77c-e0967d4889e0 (supervisor-dispatched).
**Date:** 2026-10-09. **Verdict: KILL** (W2 la-frame instance; route-level consequence stated).
**Parent:** battery-det-91-11-frame (NULL, 2026-10-09) — follow-up 2 of that fence.

## Bar (verbatim from battery-queue.json — pre-registered BEFORE testing)

"if no parse survives the clash, harden the W2 fence into a kill of the la-frame route for 91; else record the surviving parse"

## Bar as numbered pass/fail clauses (frozen before testing; not modified after seeing data)

1. **C1 (enumerate):** all candidate parses of "la [78] [55] [81]" at 1b @1669–1673 are enumerated under standing values only.
2. **C2 (clash test):** each candidate is tested against the la/81 agreement clash (11='la' feminine pencil GT vs 81 promoted masculine abstract noun).
3. **C3 (resolve):** if no candidate survives → KILL (harden the W2 fence into a kill of the la-frame route for 91). If ≥1 survives → record the surviving parse (null).

## Method

1. Read `BATTERY-PROTOCOL.md` in full. Created `code/crowd17/next-token/locks/det-91-81-agree-test.lock` on start (no stale lock; deleted on completion).
2. Re-derived the repaired 1,847-pair stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py` (1,847 pairs, 96 types asserted). `canonical.py` never used. R5005, sealed gate instances, red-team queue untouched.
3. Standing values used (protocol §7 + battery queue): pencil GT 11='la'; noun-81 **PROMOTE** 81='masculine abstract noun' (2026-10-09, battery grade — adopted, not re-litigated per adverse); 78 open ('ver' is battery LEAD only, R16-005 not settled — respected per adverse, never used to license or kill); 55 open (class-55-det KILLED the determiner-particle claim; seg-55-61-21-stem promoted 55 word-internal before 61 only — here the follower is 81, not 61, so the promote does not transfer).
4. Canonicality caveat stands: row a8_05 is among the 68 unvalidated upstream row offsets.

## Window-level evidence

**W2 locus — 1b @1669–1673 (0b @1668–1672), row a8_05:**
`…06(ent, promoted) | 91 | 11(la, GT) | 78 | 55 | 81 | 92 | 60 | 03 | 39 | 74 | 77 | 44 | 00(pour) | 46(que)…`
Byte-exact: `…06 91 11 78 55 81 92 60 03 39…` (verified in-session).

### C1: candidate parses under standing values

- **P1 — single NP "la [78] [55] [81]" with 81 as head.** The only candidate in which every token has a standing-supported role. Killed by the clash (C2).
- **P2 — "la [78]" NP, 81 a separate constituent.** Requires 78 = feminine nominal. 78's class/value is open at every grade; no standing battery names a 78 nominal, feminine or otherwise. Unlicensed.
- **P3 — "la [78] [55]" NP with 55 as feminine head, 81 separate.** Requires 55 = feminine nominal. 55's class is open; the only live 55 reading is word-internal before 61 (seg-55-61-21-stem), inapplicable here (follower 81). Unlicensed.
- **P4 — "la" as object clitic + [78] as finite verb.** Requires finite-verb 78; zero legs anywhere. Also elision "l'a" is impossible before a consonantal group. Unlicensed.
- **P5 — "la [78] [55]" + appositive/vocative [81].** Appositives agree with their head; the head is unlicensed (see P2/P3). Unlicensed.
- **P6 — "[55 81]" as one word.** No composition license exists for 55+81: class-55-det tested the '55 81' x6 family and killed the determiner arm; no word-internal promote covers 55 before 81. Unlicensed.
- **P7 — "la" as interjection / musical note.** No standing support. Unlicensed.
- **P8 — 78 as some feminine value via another battery.** No battery-grade 78 value names a feminine noun; the sole lead ('ver', masculine) is unsettled and adverse-barred from use. Unlicensed.

### C2: clash test

- P1 dies at kill grade on the agreement clash: feminine article "la" (11, pencil GT — invariable) cannot head an NP whose head is the promoted masculine noun 81. No French re-segmentation rescues it: "la" has no masculine allomorph, and 81's masculine is a standing battery promote.
- P2–P8 do not survive either — not because the clash kills them, but because each needs a value/class (feminine 78, feminine 55, verb-78, composed 55-81) that standing values do not supply. Unlicensed is not kill-grade; these arms are fenced, not dead.

### C3: resolution

**No parse of "la [78] [55] [81]" is licensed under standing values; the single standing-supported reading is killed by the clash. KILL fires.**

## Scope of the kill (stated cause)

- **Killed:** the W2 instance of the la-frame route — "la [78] [55] [81]" at 1b @1669–1673 admits no grammatical parse under standing values. The W2 fence from det-91-11-frame is hardened into a kill at this window.
- **Preserved, not overreached:** W1 (1b @1006, "la [52] [35]") remains FENCED, not killed — the clash evidence does not touch W1, and 52's open class could still license a feminine "la 52" NP. Killing W1's instance would exceed the bar's evidence.
- **Route-level consequence:** the la-frame route for 91 now has **zero live windows** (W2 killed, W1 fenced pending 52). Per the bar's wording, the kill is recorded against the la-frame route for 91.

## Adverses (answered, none ignored)

- "78='ver' is R16-005 LEAD-not-settled, respected": honored — 'ver' was neither used to license a parse (P2/P8) nor invoked as a kill leg.
- "do not re-litigate 81's promote": honored — noun-81's masculine abstract noun was used as a premise (the clash's second term), never re-tested.

## Standing-state check (no contradiction, no downgrade)

- No red-team verdict on 91 exists; 91's value stays open. The kill constrains the licensing route, it does not kill any 91 value.
- det-91-la-clitic-test (queued) is untouched and is now the sharpest remaining la-frame question: if "la" proves clitic at W2, the det-frame dies independently of this kill.
- nom-91-ce-head (queued) is untouched — the "ce [91]" nominal route at W1's left frame stays live.
- §7 intact; no polyvalence declared; 67 untouched.

## Verdict: KILL

The W2 la-frame candidate "la [78] [55] [81]" is unparseable under standing values (the one standing-supported reading dies on the la/81 agreement clash; every rescue is unlicensed). The la-frame route for 91 has no live window: W2 killed, W1 fenced on 52.

## Supervisor observations (not findings; no follow-ups proposed — §4: kills regenerate none)

- `det-91-la-clitic-test` (queued P3): article-vs-clitic at both windows — if clitic, the det-frame route dies at both windows independently of this kill.
- `nom-91-ce-head` (queued P4): the remaining live nominal route for 91 via W1's "ce [91]" left frame.
- `val-78-class-census`-shaped work (not queued): a landed feminine 78 would revive P2 at battery grade; no such target exists — proposed only if the supervisor wants it.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-det-91-81-agree-test.md` (this file).
- Queue entry `det-91-81-agree-test` updated via temp-file + rename (pre-write assert: status `queued`, verdict null; post-write JSON re-validated; own entry only).
- Lock `code/crowd17/next-token/locks/det-91-81-agree-test.lock` created on start, deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
