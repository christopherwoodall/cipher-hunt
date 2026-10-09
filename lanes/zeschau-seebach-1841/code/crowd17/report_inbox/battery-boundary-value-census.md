# Battery report: boundary-value-census

Target: `boundary-value-census`. Claim: "the 'verdict' value arm has (or lacks) legs outside ver-78's bar".
Date: 2026-10-09. Worker session: c62a3ebf-5229-4048-a69e-bb7ddb7f0473 (battery worker).
Lock `code/crowd17/next-token/locks/boundary-value-census.lock` created 2026-10-09T03:57:19Z (no pre-existing lock); deleted on completion.

## Bar (verbatim, pre-registered BEFORE testing)

> census all 31 windows of 78 on the repaired stream; count 'ver'-word-shaped continuations vs 'er'/nominal shapes; the value arm gains a leg iff >=2 windows parse 'ver'-shaped under standing values with stated cause each

Numbered clauses (frozen before testing):

1. Census all 31 windows of 78 on the repaired 1,847-pair stream.
2. Count 'ver'-word-shaped continuations vs 'er'-shaped vs nominal shapes.
3. The 'verdict' value arm gains a leg iff >=2 windows parse 'ver'-shaped under standing values, with stated cause for each.

## Method

Re-derived the repaired stream byte-exactly per `repair_parse.py` (`repaired_offsets.json` + `data/upstream-ct_R5005.txt`): 1,847 pairs / 96 types asserted in-session. `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched. All @-offsets below are 1-based pair indices. Standing values per protocol §7: GT 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que; promoted 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce; provisional 59=est, 77=le; R17: 48='e', 12='n'; 45="dict" is a LEAD (word-internal candidate), 45="ce" HOLD A11; 78="ver" is LEAD (R16-005), not granted.

## Census: all 31 windows of 78 (1-based @, pre / suc)

| @ | context (pre 78 suc) | shape class |
|---|---|---|
| 9 | 77 78 18 | nominal (le) |
| 215 | 77 78 06 | nominal (le) |
| 298 | 11 78 40 | nominal (la); "vere" completion killed |
| 314 | 37 78 45 | 'ver'-shaped candidate — resolved A11 'ce' (see below) |
| 353 | 67 78 40 | misc; "et vere" killed |
| 365 | 47 78 48 | nominal (ce); "ce vere" killed |
| 416 | 37 78 49 | predicative-frame (37, A1) |
| 436 | 16 78 63 | misc (open) |
| 444 | 50 78 41 | misc (open) |
| 477 | 37 78 74 | predicative-frame (37, A1) |
| 493 | 67 78 42 | misc (67 positional) |
| 574 | 87 78 45 | 'ver'-shaped — LEG (conditional, see below) |
| 630 | 87 78 67 | nominal determiner-profile ("ce ver" + 67) |
| 649 | 77 78 52 | nominal (le) |
| 820 | 47 78 40 | nominal (ce); "ce vere" killed |
| 880 | 86 78 17 | misc (fois-context) |
| 983 | 47 78 45 | 'ver'-shaped — fenced NEUTRAL (circularity) |
| 1013 | 80 78 47 | misc (verb-frame 80) |
| 1079 | 77 78 64 | nominal (le) |
| 1106 | 47 78 65 | nominal determiner-profile ("ce ver[65]", 65 value open) |
| 1141 | 98 78 62 | misc (open) |
| 1165 | 67 78 45 | 'ver'-shaped — double-residual (W4) |
| 1182 | 77 78 94 | nominal (le) |
| 1353 | 77 78 94 | nominal (le) |
| 1398 | 47 78 48 | nominal (ce); "ce veree" killed |
| 1544 | 77 78 43 | nominal (le) |
| 1622 | 84 78 66 | pronominal (on) |
| 1671 | 11 78 55 | nominal (la) |
| 1759 | 17 78 41 | misc (fois-context) |
| 1772 | 37 78 62 | predicative-frame (37, A1) |
| 1844 | 67 78 49 | misc (67 positional) |

## Count

- **'ver'-word-shaped continuations: 4** — exactly the four 78-45 windows (@314, @574, @983, @1165; the only loci where 45 can sit inside a French "dict"-word per the closed host inventory, battery-dict-45-host-inventory). No other 78 window composes a "ver…" word under standing values: 78-40/48 → "vere"/"veree" are killed non-words (@298/@353/@365/@820/@1398); 78-65 is open (65 value unnamed); 78-67 is determiner-profile, not a completing word.
- **'er'-shaped: 0 surviving.** No 78-29 contact exists; no stem+78="…er" composition is demonstrable; the five "vere"/"veree" windows are killed completions, not 'er'-shapes.
- **Nominal/pronominal-shaped: 15** (77-le x7: @9/@215/@649/@1079/@1182/@1353/@1544; 47-ce x4: @365/@820/@1106/@1398; 87-ce x1: @630; 11-la x2: @298/@1671; 84-on x1: @1622).
- **Predicative-frame (37, A1): 3** (@416/@477/@1772).
- **Misc/open: 9** (@353/@436/@444/@493/@880/@1013/@1141/@1759/@1844).

Check: 4 + 0 + 15 + 3 + 9 = 31. All windows accounted for.

## Leg adjudication (Clause 3): the four 'ver'-shaped windows

- **@574 (1-based; "52 87 78 45 13", row a3_02): LEG — conditional.** "ce verdict" parses under the granted 87="ce" with 78="ver" (LEAD) + 45="dict" (lead) composing one word; the 78-45 boundary is promoted by verdict-w2-574-gate. Stated cause: determiner present (87), granted values throughout the frame. Recorded in battery-verdict45-value as the surviving positive leg; not re-litigated, cited.
- **@314 (1-based; "24 37 78 45 64", row a2_04): NOT a leg.** battery-dict-313-w1-adjudicate (2026-10-08) already decided this locus: the 'ce qui' (A11 two-word) reading beats the 'verdict qui' (one-word) reading on ungranted-assumption count. The 'verdict' reading is not available here without re-litigating a settled battery verdict; never-downgrade applies.
- **@983 (1-based; "76 47 78 45 01", row a6_01): NOT a leg — fenced NEUTRAL.** battery-verdict45-value: the 78="ver" ↔ 45="dict" readings are mutually conditional here (double-counting the same circularity); recorded neutral, not positive.
- **@1165 (1-based; "21 67 78 45 13", row a6_09, W4): NOT a leg — double-residual.** battery-dict-45-ce-rival-1165: ungrammatical under BOTH the 78="ver"+45="dict" two-token reading and the 78="ver"-word+45="ce" reading; needs the fenced 5-gram unit reading, a red-team-declared polyvalence, or a third 78 value. The determiner-gap question is owned by queued w4-dict-det-gap — not duplicated.

**Legs: 1 of 4.** The Clause-3 iff condition (>=2 windows parse 'ver'-shaped) is not met. The value arm gains **no new leg** from this battery.

## Adverses

- **R16-005 LEAD grading:** answered — 78="ver" stays LEAD (conditional, red-team territory). This battery changes nothing about the lead's grade.
- **Do not contradict ver-78's null:** answered — no value is promoted by this battery. The census is banked as evidence only; 78="ver" is not promoted, and ver-78's null verdict stands untouched.

## Per-clause results

- **C1 (census all 31): PASS** — 31/31 windows listed with pre/successor context from the repaired stream.
- **C2 (count): PASS** — 4 'ver'-word-shaped, 0 'er'-shaped surviving, 15 nominal/pronominal, 3 predicative-frame, 9 misc/open.
- **C3 (gain a leg iff >=2): FIRES on the negative arm** — exactly 1 window parses 'ver'-shaped as a leg (@574, conditional); @314 resolved A11, @983 fenced neutral, @1165 double-residual. The arm gains no second leg.

## Verdict

**PROMOTE (census finding — promotes no value).** The 31-window census is complete and byte-exact: the 'verdict' value arm has exactly **one** conditional leg (@574, "ce verdict") and no second leg — the other three 78-45 loci are accounted for (@314 = A11 'ce' resolved; @983 = fenced neutral; @1165 = double-residual). The "four 78-45 windows = four legs" notion is retired at battery grade. No value is promoted; R16-005 LEAD and ver-78's null are untouched.

## Standing-state check

No standing verdict contradicted or downgraded. Coordinated (not duplicated) existing queued items: `w4-dict-det-gap` (determiner-gap adjudication), `ver78-65-completion` (@1106's "ce ver[65]" venue), `ver78-non45-positive-leg` (break the 78↔45 conditionality from the 78 side). No new follow-ups proposed — the census is conclusive as stated and the residual questions already have queued venues.
