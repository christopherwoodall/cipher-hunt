# Battery verdict: val-98-702-importe

- Target: `val-98-702-importe` (battery-queue.json, priority 3, status queued)
- Claim: test 98='importe' at @702: "n'[98]" → "n'importe" with 20's battery relative-adverb reading at @703. (Strongest near-miss of seg-94-60-12 arm (iii).)
- Date: 2026-10-09
- Stream: repaired 1,847-pair / 96-type parse re-derived in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed like `code/side-keyhunt/repair_parse.py` (asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gate instances, and the red-team adjudication queue untouched.

## Bar (verbatim, pre-registered)

"name 98='importe' with >=2 independent legs or fence (strongest near-miss of seg-94-60-12 arm (iii))"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1 (name):** 98='importe' is named iff ≥2 independent battery-grade legs parse — i.e., ≥2 windows where 98 reads as 'importe' under standing values with zero ungranted assumptions. → PROMOTE.
2. **C2 (fence):** otherwise the value-naming is fenced. → NULL (fence executed).

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/val-98-702-importe.lock` on start (agent 315eb7f3-5865-4839-994b-f4786a659c81, 2026-10-09); deleted on completion.
2. Census: all 40 windows of 98 (n(98)=40, byte-confirmed) swept for every French 'importe' frame: "n'importe" (+ interrogative), "peu importe", "qu'importe", "il (m')importe (de/que)", "ce qui importe", "importe de", transitive "importer".
3. Adopted, not re-litigated: 98=[verb,cls] (R19-171/176) with 'vient' value-LEAD (R19-172); 94='ne' STRONG LEAD (R17-001); 12='n' PROMOTE letter tier (R20-008); 83='de' LEAD (R19-128); 30='pas' PROMOTE with fused "n'importe" (94+30, n'-elision, 30='importe') confined as terminal singleton at @1701-1702 (importe-1702-singleton PROMOTE; ne30-1701-tail-reconcile PROMOTE; R20-029(b) fused-lexical-item confirmation); 20 at @703 = forced infinitive (census-20-open-windows PROMOTE: "vient [20-INF]"); expletive-"ne" at @699 fenced as structurally impossible (2,531-frame corpus study); 62='il' killed at kill grade (R19-106, R20-125).

## Window-level evidence

### 'importe'-shaped contacts stream-wide: exactly 2

Full bigram census around all 40 98-windows:

- **"12 98" (n' + importe): exactly 1×** — @702 (the locus): `699:94(ne) 700:60 701:12(n) 702:98 703:20 704:12(n)`.
- **"46 98" (que + importe = "qu'importe"): exactly 1×** — @227: `224:96(par) 225:47(ce) 226:46(que) 227:98 228:83(de-lead) 229:82(m) 230:96(par)`.
- **"94 98" (ne + importe): 0×.** "87/47 94 98": 0×. No 'il' subject available anywhere (62='il' killed). No 'peu' cell. No "ce qui 98".

### Leg 1 (@702, "n'importe [20]"): FAILS — four independent blocks

1. **20's class contradicts the frame.** The claim needs 20 as relative adverb at @703 ("n'importe où"-shaped). Standing battery verdict (census-20-open-windows PROMOTE): @703's 20 is **forced infinitive** — "vient [20-INF]" via the licensed "venir faire" construction; noun-20 dies without "de". "n'importe [INF]" is ungrammatical. The claim's "relative-adverb reading at @703" is stale (the locus-level relative-adverb PROMOTE, reladv-20-1703, is at @1703, not @703). Kill-grade block on the frame's right edge.
2. **Left clause unlicensed.** "94 60" = "ne [60]": expletive-"ne" at @699 fenced as structurally impossible (zero genuine inside-clause licensers in 2,531 frames); plain "ne" needs "pas" — no 30 within ±15 of @699–702. Neither side of the arm-(iii) clause boundary parses.
3. **Clause boundary unlicensed.** No licensed boundary between 60 and 12 under standing values.
4. **Elision composition unlicensed.** "12 98" as "n'importe" needs letter-tier 12='n' eliding as "n'" with following word 98. The lane's letter-composition precedents ("ne mentent" = 94-word + letters; "en"/"un" = letter+letter; A10 "33+29") never cover letter-as-elided-negator + word. Ungranted.

### Leg 2 (@227, "qu'importe"): FAILS — frame does not complete

"46 98" = "qu'importe" is morphologically licensed (46='que' pencil GT elides before vowel-initial 98). But:
- Left: "96 47" = "par ce" — 96='par' granted, 47='ce' A4 granted; "par ce qu'importe" leaves "par ce" dangling (no licensed "par ce" phrase; "parce que" resegmentation would need 46 and yields "parce qu'importe", not idiomatic French).
- Right: 228=83('de'-lead), 229=82('m'): "qu'importe de m par" — "qu'importe de" is not an idiomatic frame ("qu'importe le prix" takes a bare noun, not "de").
- No grammatical completion under standing values with zero ungranted assumptions.

### Exhaustion of remaining frames

- **"98 83" ("importe de") ×5** (@227/@897/@930/@1060/@1783): @930 "par [48] m'importe de" — no subject ("il m'importe" needs 'il', unavailable); @1601-adjacent "82 98" ("m'importe") ×2 (@930/@1601) — subjectless; @897 "[98] m [14] importe de" — subjectless; @1060 "on [09] importe de" — 09 intervenes, "de" unlicensed; @1783 "[23-verb] importe de" — two finite verbs adjacent. All dead.
- **"62 98" ×5**: 62's value open ('il' killed) — no battery-grade subject leg.
- **"64 98" ×2** (@19 "fois qui [98]", @511 "ne qui [98]"): "qui importe" needs a complement; "ne qui" ungrammatical. Dead.
- **"47 98" @192** ("[24] ce [98]"): "ce importe" ungrammatical. Dead.
- **Transitive "importer"**: no subject+object window. Dead.
- **"peu importe" / "il importe"**: no 'peu', no 'il'. Absent.

**Result: 0 battery-grade legs.** C1's ≥2 requirement is not met; it is not even approached.

## Per-clause pass/fail

1. C1 (name with ≥2 independent legs): **FAIL** — 0 legs; the two 'importe'-shaped contacts (@227, @702) both fail at battery grade on independent grounds.
2. C2 (fence arm): **FIRES** — 98='importe' value-naming is fenced (evidentiary, not kill-grade: no window forces 98≠'importe', e.g. "le [66] importe" remains grammatical where "le [66] vient" holds).

## Verdict: NULL (fence executed)

## Adverse

"94='ne' STRONG LEAD intact: fence, don't declare" — honored. 94 untouched; no second 94 value proposed. Note the lane already realizes "n'importe" as the fused "94+30" item (30='importe' via n'-elision) confined as terminal singleton at @1701-1702 (importe-1702-singleton PROMOTE; ne30-1701-tail-reconcile PROMOTE); the 'importe' word-formation rivalry is settled there at battery level, and this battery adds the distributional fact that 98 supplies zero 'importe' legs anywhere.

## Scope

Fences only the 98='importe' value-naming. Untouched: 98=[verb,cls], 'vient' value-LEAD (R19-172), 94='ne' STRONG LEAD, 30's fused-"n'importe"/'pas' complementary distribution, 20's @703 infinitive classification, §7 (no split declared or needed — there is nothing to split over). No standing or red-team verdict contradicted, downgraded, or re-litigated. Canonical-stream caveat stands (row a4_05/a8_06 offsets unvalidated).

## Follow-ups (for supervisor queuing; all verified ABSENT from battery-queue.json)

1. `nimporte-702-reseg` (P4) — resegmentation test at @699–704: if "60 12" composes leftward or 94's scope re-parses, the "n'importe" frame at @702 re-opens (currently blocked on four independent grounds, §"Leg 1" above).
2. `quimporte-227-frame` (P4) — test the "96 47 46" = "parce que" resegmentation at @224–226; if licensed, re-test 98's slot at @227 under the new left edge.
3. `imp-98-zero-leg-package` (P4, gather-only) — package this zero-leg census (all 40 windows, 2 'importe'-shaped contacts, both fenced) as red-team input: 98='vient' LEAD stands unchallenged stream-wide.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-98-702-importe.md`
- Queue: `val-98-702-importe` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.val-98-702-importe.tmp` + rename; disk re-validated; own entry only; no downgrade; no tmp leftover)
- Lock `locks/val-98-702-importe.lock`: created on start (2026-10-09), deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
