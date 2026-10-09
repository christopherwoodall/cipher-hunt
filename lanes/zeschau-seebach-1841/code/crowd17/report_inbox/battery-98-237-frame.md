# Battery `98-237-frame` — verdict: PROMOTE

- Target id: `98-237-frame`
- Claim: name 98 at @236 to ground the determiner arm's strong leg for val-41-1016's fence reasoning.
- Worker: subagent 9492ea1f-2efa-4b20-9970-bc1d18c87e67
- Date: 2026-10-09
- Follow-up #3 of `val-41-1016` NULL (2026-10-09).

## Bar (verbatim, pre-registered from battery-queue.json)

> "98's value named at battery grade at @236; else fence the leg."

Restated as numbered clauses (fixed before testing, not modified after):

1. **C1:** 98's value is named at battery grade at @236.
2. **C2 (else-arm):** if C1 fails, fence the leg — the determiner arm's strong leg for 41 at @237 (val-41-1016 D1 / val-41-det-windows W1).

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/98-237-frame.lock` (agent id + 2026-10-09T13:49:03Z) on start. No fresh lock was present.
2. Re-derived the repaired 1,847-pair / 96-type stream in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`. Asserts held: 1,847 pairs, 96 types. All @-offsets below are 0-based pair indices. `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched.
3. Premises adopted (not re-litigated): `vient-98-name` PROMOTE 2026-10-08 (98='vient' at battery grade, pending red-team ratification); `val-98-subject` PROMOTE 2026-10-09 (98 = finite clause-head verb, zero ungranted assumptions); R19 (98=verb class granted, 'vient' kept at lead grade); `val-41-det-windows` PROMOTE 2026-10-09 (determiner arm; @237 is the strong leg: "[98-fin] [41-det] fois la [26]"); banked pencil GT (70='pre', 17='fois', 11='la'); 26=[noun,lead]; §7 (67 sole true polyvalence; no second value declared at battery grade).

## Window-level evidence (byte-exact, 0-based, row a2_01)

```
@230=96  @231=21  @232=60  @233=71  @234=51  @235=70  [@236=98]  @237=41
@238=17  @239=11  @240=26  @241=12  @242=16  @243=56
```

Target frame: `71 51 70=pre [98] 41 17=fois 11=la 26` →
"[70=pre]-[98] [41] fois la [26]".

### C1 leg 1 — compositional 'pré-vient' (adopted standing leg)

70='pre' (banked GT syllable) + 98 reads 'pré-vient' = 'prévient' (prévenir, 3sg present). This leg was established at battery grade in `vient-98-name` (2026-10-08) and is adopted here, not re-derived: 'pré-revient' is not a word, so the composition selects 'vient' over the 'revient' rival. At @236, 98's value names as 'vient' with no new assumption beyond standing premises.

### C1 leg 2 — clause parse grounds the determiner arm

With 98='vient' (finite verb), the frame reads:

"[prévient] [41] fois la [26-noun,lead]"

= "prévient [det] fois la [NP]" — e.g. "prévient deux fois la cour". Grammatical 1841 French. The finite verb left of 41 keeps 41 in the determiner/numeral slot ("[V] [det] fois la") — this is exactly the determiner arm's strong leg (val-41-det-windows W1: "vient [41] fois" = "une/chaque/deux fois"-shaped). Naming 98='vient' at @236 grounds what that leg stands on.

### Adverse found in testing — 98='par' excluded at battery grade

The parent report's follow-up listed "98='par' licenses 'par [41] fois' (numeral arm)" as an option. Answered: 98='par' (preposition) is unnameable at battery grade — R19 granted 98 the verb class, and §7 bars a second class/value for 98 without a red-team act. It would contradict a standing red-team verdict, so it is closed at battery grade (red-team venue only).

### Kill-grade audit at @236

- No byte forces 98≠'vient' at this window.
- The doubled-98 residuals (@1073/@1145/@1660) and the 'pour 98' inflectional fence live at other windows; they do not touch @236 (standing fences adopted).
- The "vient de" inventory break at @930 concerns 56's class, not 98.

## Per-clause results

- **C1: PASS.** 98's value is named at battery grade at @236: 'vient' (finite verb; word "prévient" with 70='pre'). Two standing legs (compositional 'pré-vient' from vient-98-name; finite-verb class from val-98-subject) plus the grammatical clause parse "[V] [det] fois la [NP]" that grounds the determiner arm. No standing or red-team verdict contradicted (consistent with R19: 98=verb class, 'vient' lead). §7 intact — no polyvalence declared.
- **C2:** else-arm does not fire. The leg is grounded, not fenced.

## Verdict: PROMOTE

98='vient' named at @236 at battery grade. The determiner arm's strong leg for 41 at @237 now stands on a named finite verb: "prévient [41] fois la [26]". Red-team ratification still applies per pipeline rule (R19 keeps 'vient' at lead grade).

## Scope

Names 98's value at @236 only. Untouched: 41's value (still unnameable — val-41-1016 NULL stands), the W_C fence, `split-41-redteam` (queued), the doubled-98 cause, 83='de', and all §7 standings. No follow-ups required per §4 (promote).

## Bookkeeping

- Queue: `98-237-frame` → `status: verdict`, `result: promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated from disk; own entry only; no downgrade).
- Lock created on start, deleted on completion (verified gone).
