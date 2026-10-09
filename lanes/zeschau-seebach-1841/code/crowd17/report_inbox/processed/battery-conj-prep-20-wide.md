# Battery verdict: conj-prep-20-wide

**Verdict: NULL** (fence executed).

## Target

- id: `conj-prep-20-wide` (priority 3)
- claim: "test conjunction/preposition roles for 20 across its full 15-window profile."
- Parent: `nondet-20-sandwich` NULL (2026-10-09) — its sandwich conjunction/preposition arms fenced at @279–281 with stated cause.
- adverses: none listed.

## Bar (verbatim from battery-queue.json)

"revive the sandwich arms iff a role is forced at >=2 independent windows; else fence"

Numbered pass/fail clauses (pre-registered before testing — bar not modified after data):

1. **C1 (conjunction):** PASS iff a conjunction role for 20 is *forced* (not merely compatible) at ≥2 independent windows under standing values.
2. **C2 (preposition):** PASS iff a preposition role for 20 is *forced* at ≥2 independent windows under standing values.
3. **C3 (fence):** if C1 and C2 both fail, fence the conjunction/preposition route with stated cause.

Verdict rule: revive (promote the arms back into play) iff C1 or C2 passes; else null with fence.

## Method

Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/conj-prep-20-wide.lock` on start (agent id 9ad1687c-c2b1-4efb-b81e-80a6a2c6290d, 2026-10-09T10:51:18Z); no prior/stale lock. Re-derived the repaired 1,847-pair / 96-type stream in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (byte-exact tokenization per `repair_parse.py`; asserts held). `canonical.py` never used. R5005, sealed gate instances, and the red-team adjudication queue untouched. Standing values held fixed per §7 (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que; 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce; 59=est / 77=le provisional; 67 et/veut sole polyvalence). Adopted, never re-litigated: `census-20-open-windows` PROMOTE (2026-10-09 — @703 forced infinitive, @873 forced finite verb, 7 windows unforced), `nondet-20-sandwich` NULL, `det-20-307-fenced` NULL, `importe-1702-singleton` PROMOTE (@1702 'n'importe' confinement), `poly-20-docket` (queued P1 — the 20-paradox venue; no ruling on 20's global class/value here).

## Window-level evidence (all 15 windows, byte-exact, ±4 context)

| @ | context | conj/prep test |
|---|---|---|
| 280 (a2_03) | `84 91 37 61 \|20\| 61 42 48 52` | sandwich "61 20 61" — the parent battery fenced both arms here (no French conjunction/preposition composes "premier [X] premier" under standing values); adopted. |
| 307 (a2_04) | `89 88 02 88 \|20\| 17 46 84 24` | "[88] [20] fois(17) que(46)" — conj: no clause after 20 ("fois que" is the temporal noun, not a clause); prep: "[20] fois" needs article/determiner ("à la fois" shape) — unlicensed. Not forced; det-route separately fenced (`det-20-307-fenced`). |
| 490 (a2_11) | `64 76 42 41 \|20\| 67 78 42 94` | "[41] [20] et(67) [78] [42]" — 67="et" (follower 78 not infinitive-shaped). If 20 were a conjunction, it would join 41 to the "et [78] [42]" phrase — a double-conjunction frame, ungrammatical. Not forced. |
| 642 (a4_01) | `67 77 89 48 \|20\| 24 87 61 88` | "[48] [20] [24-fin]" — the one subordinator-shaped window (24 finite/modal class-level, R17-009). But 48's class is open here (the A7-L2 "tout me [48-verb]" frame does not fire at this window — left is "89 48"), and 20 as adverb ("[48] [adv] [24]") is equally live. Compatible, NOT forced. |
| 668 (a5_00) | `03 62 06 00 \|20\| 67 11 86 24` | "pour(00) [20] et(67) la(11) [86]" — prep-20 dies ("pour [prep]" ungrammatical); conj-20 dies ("pour [conj] et" ungrammatical). Adopted census: noun/infinitive tie. Route *excluded* here, not forced. |
| 703 (a5_01) | `94 60 12 98 \|20\| 12 66 21 35` | "vient(98) [20] [12]" — infinitive forced (adopted census: "vient [INF] — noun dies without de"). A conjunction needs a clause after 20; follower is "12 66 21 35", no clause. Conj/prep incompatible. |
| 741 (a5_02) | `82 06 00 36 \|20\| 30 67 77 81` | "[36] [20] pas(30) et(67) le(77) [81]" — conj: "[36] [conj] pas..." ungrammatical; prep: no complement NP. "pas" stranded under every 20-role. Not forced. |
| 760 (a5_03) | `82 34 29 40 \|20\| 62 94 59 39` | "première [20] il(62) ne(94) est(59) [39]" — gloss-anchored row. Conj: "…première, et il n'est [39]" is *compatible* (needs clause boundary); prep: "première [prep] il..." ungrammatical. Compatible-not-forced. |
| 839 (a5_06) | `35 56 17 98 \|20\| 62 94 26 12` | "vient(98) [20] il(62) ne(94) [26]" — conj: "vient [conj] il ne [26]" needs "vient" to be a complete clause (no subject before 20 — subject "il" comes after 20). Possible with punctuation; not forced. |
| 873 (a5_07) | `87 77 89 48 \|20\| 74 49 16 77` | finite verb forced (adopted census: "le [89]e [20] 74" S-V-X, zero new assumptions). Conj/prep incompatible. |
| 958 (a6_00) | `46 24 85 04 \|20\| 67 96 00 86` | "[04] [20] et(67) par(96) pour(00) [86]er" — conj: "[04] [conj] et..." double conjunction, ungrammatical; prep: "[20] et" ungrammatical. Adopted census: "par pour" rupture, value-independent. Not forced. |
| 1135 (a6_08) | `86 24 77 86 \|20\| 62 98 00 98` | "[86] [20] il(62) vient(98) pour(00) [98]" — subordinator before "il vient" is compatible ("quand/si il vient"), but adverb ("ainsi, il vient") is equally live. Not forced. |
| 1224 (a7_01) | `24 48 30 09 \|20\| 57 64 79 82` | "[09] [20] [57] qui(64) tout(79) m(82)" — left edge opaque (adopted census); 57's class open. No frame forces anything. |
| 1270 (a7_02) | `69 88 24 30 \|20\| 64 47 76 87` | "pas(30) [20] qui(64) ce(47) [76] ce(87)" — conj: "pas [conj] qui..." ungrammatical; prep: "pas [prep] qui..." ungrammatical. Not forced. |
| 1703 (a8_06) | `85 33 94 30 \|20\| 62 94 88 26` | "n'importe [20] il(62) ne(94) [88] [26]" — 'n'importe' confined (adopted PROMOTE). "n'importe [où/quand] il ne [88]" is compatible, but "n'importe que il..." is non-standard and adverb/noun 20 equally live. Not forced. |

## Per-clause results

1. **C1: FAIL** — zero windows *force* a conjunction role. The compatible windows (@642, @760, @839, @1135, @1703) are all compatible-not-forced; the bar's stem-03-value precedent applies (compatible ≠ forced at battery grade). @668/@703/@873 actively exclude conj.
2. **C2: FAIL** — zero windows *force* a preposition role. No window has the licensed prep-complement geometry with named values; @668 kills prep locally.
3. **C3: FIRES — fence executed.** The conjunction/preposition route for 20 is fenced across the full 15-window profile. Stated cause: the strongest subordinator-shaped window (@642) is blocked by 48's open class at that locus; every other compatible window admits an equally-live adverb/nominal/infinitive rival; two windows (@668, @703) kill prep outright and one (@873) forces a finite verb, incompatible with both roles. The fence inherits the parent's sandwich fence — the arms stay dead.

No standing verdict contradicted or downgraded: the @703 forced-infinitive and @873 forced-finite-verb classifications adopted as premises; the 20-paradox stays in `poly-20-docket` (red-team venue); §7 intact (no polyvalence declared — the fence is per-window, no cross-window class claim). Canonical-stream caveat stands (68/70 row offsets unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `conj-20-642-subordinator` (P3) — the one live subordinator-shaped window: test "[48] [20] [24-fin]" once 48's class at @641 is named. Bars: name 48's class; a nominal/verbal 48 + finite-24 + forced subordinating slot revives the conjunction arm at this window alone; else fence @642 too.
2. `adverb-20-wide` (P3) — the untested competing role: test 20 as clause-adverb across the 15-window profile (the "compatible" windows above all admit it). Bars: adverb role forced at ≥2 independent windows → promote; else fence.
3. `coord-20-490-958` (P4) — kill-seek on the coordinator arm: @490 ("[41] [20] et...") and @958 ("[04] [20] et...") both put a second conjunction (67="et") two groups right of 20. Bars: if no French frame licenses double conjunction under standing values, kill the coordinating-conjunction arm at battery grade; else fence.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-conj-prep-20-wide.md` (this file).
- Queue: `conj-prep-20-wide` queued → verdict/null via temp-file + rename, own entry only; pre-write assert confirmed no prior verdict; JSON re-validated post-write.
- Lock `conj-prep-20-wide.lock`: created on start, deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
