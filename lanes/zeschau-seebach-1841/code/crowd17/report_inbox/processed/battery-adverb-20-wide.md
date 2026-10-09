# Battery verdict: adverb-20-wide

**Verdict: NULL** (fence executed).

## Target

- id: `adverb-20-wide` (priority 3)
- claim: "test 20 as clause-adverb across the 15-window profile (the \"compatible\" windows all admit it)"
- Parent: `conj-prep-20-wide` NULL (2026-10-09) — follow-up 2 of 3.
- adverses: none listed.

## Bar (verbatim from battery-queue.json)

"adverb role forced at >=2 independent windows -> promote; else fence"

Numbered pass/fail clauses (pre-registered before testing — bar not modified after data):

1. **C1 (adverb forced ≥2):** PASS iff an adverb role for 20 is *forced* (not merely compatible) at ≥2 independent windows under standing values.
2. **C2 (fence):** if C1 fails, fence the clause-adverb route for 20 with stated cause.

Verdict rule: promote iff C1 passes; else null with fence.

## Terms

- **Clause adverb:** a word that modifies a whole clause ("ainsi", "donc", "cependant"). It sits at a clause edge, not inside a noun phrase and not between a verb and its required object.
- **Forced:** the frame admits the role and no other role fits under standing values. "Compatible" (the role merely fits) is not enough.
- **Independent windows:** windows with different left/right frames, not copies of one frame.

## Method

Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/adverb-20-wide.lock` on start (agent id cbf62482-4be6-4ecd-a4f5-f40f36f617a3, 2026-10-09T11:16:06Z); no prior/stale lock. Re-derived the repaired 1,847-pair / 96-type stream in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (byte-exact tokenization per `repair_parse.py`; 15 windows of 20 at the same @-offsets as the parent report; asserts held). `canonical.py` never used. R5005, sealed gate instances, and the red-team adjudication queue untouched. Standing values held fixed per §7 (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que; 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce; 59=est, 77=le provisional; 67=et/veut sole polyvalence). Adopted, never re-litigated: `census-20-open-windows` PROMOTE (@703 forced infinitive, @873 forced finite verb, 7 windows unforced), `conj-prep-20-wide` NULL (fence of the conj/prep arms), `det-20-307-fenced` NULL, `importe-1702-singleton` PROMOTE ('n'importe' confined @1700-1702), `poly-20-docket` (queued P1 — the 20-paradox venue; no global class claim here).

## Window-level evidence (all 15 windows, byte-exact, ±6 context)

| @ | context | adverb test |
|---|---|---|
| 280 (a2_03) | `84 91 37 61 \|20\| 61 42 48 52` | "premier(61) [20] premier(61)". Parent fenced the sandwich. A clause adverb inside a mirrored noun pair is ungrammatical. Excluded. |
| 307 (a2_04) | `89 88 02 88 \|20\| 17 46 84 24` | "[88] [20] fois(17) que(46)". 17="fois" is a noun. French puts no adverb between an article/adjective and its noun ("la déjà fois" is wrong). 20 would have to sit inside the noun phrase, so the adverb role is excluded here. |
| 490 (a2_11) | `01 19 64 76 42 41 \|20\| 67 78 42 94` | "[41] [20] et(67) [78]". French does not put a clause adverb directly before the conjunction "et" ("[X] donc et [Y]" is wrong). Excluded. |
| 642 (a4_01) | `46 60 67 77 89 48 \|20\| 24 87 61 88 77 78` | "[48] [20] [24-finite] ce(87)". 48's class is open at this locus, so 20 as adverb is possible ("[48] [adv] [24]"). But most French adverbs cannot sit between a subject and its finite verb ("il souvent vient" is wrong). Compatible only under narrow assumptions, and noun/verb rivals are equally live. Not forced. |
| 668 (a5_00) | `03 62 06 00 \|20\| 67 11 86 24` | "pour(00) [20] et(67) la(11)". "pour [adv] et" is ungrammatical. Excluded. |
| 703 (a5_01) | `94 60 12 98 \|20\| 12 66 21 35` | "vient(98) [20] [12]". Infinitive forced at 20 (adopted census). An adverb cannot stand where the infinitive is forced. Excluded. |
| 741 (a5_02) | `82 06 00 36 \|20\| 30 67 77 81` | "[36] [20] pas(30) et(67) le(77)". An adverb before "pas" is ungrammatical here ("[X] donc pas et le [81]" is wrong). Excluded. |
| 760 (a5_03) | `11 70 82 34 29 40 \|20\| 62 94 59 39 88 66` | "la première [20] il(62) ne(94) est(59) à(39)". Gloss-anchored row. A clause adverb at the clause edge reads naturally ("la première, ainsi il n'est à…"). But noun/adjective/verb rivals are equally live: 20 could close the first clause instead. Compatible, not forced. |
| 839 (a5_06) | `76 59 35 56 17 98 \|20\| 62 94 26 12 16 00` | "vient(98) [20] il(62) ne(94) [26]". A boundary adverb is possible ("vient. Cependant il ne [26]"), but it needs punctuation, and the subordinator rival ("quand") is equally live (raised by the parent). Not forced. |
| 873 (a5_07) | `87 77 89 48 \|20\| 74 49 16 77` | Finite verb forced at 20 (adopted census). An adverb cannot stand where the finite verb is forced. Excluded. |
| 958 (a6_00) | `46 24 85 04 \|20\| 67 96 00 86` | "[04] [20] et(67) par(96)". Adverb directly before "et" is ungrammatical. Excluded. |
| 1135 (a6_08) | `52 37 86 24 77 86 \|20\| 62 98 00 98 78 62` | "[86] [20] il(62) vient(98) pour(00)". A boundary adverb is possible ("…[86]. Alors il vient pour [98]"). But a noun rival ("[86], [noun], il vient") and the subordinator rival are equally live. Not forced. |
| 1224 (a7_01) | `92 61 24 48 30 09 \|20\| 57 64 79 82 48 29` | Left edge opaque, 57's class open. Nothing forces any role. Not forced. |
| 1270 (a7_02) | `69 88 24 30 \|20\| 64 47 76 87` | "pas(30) [20] qui(64) ce(47)". An adverb between "pas" and the relative pronoun "qui" is ungrammatical. Excluded. |
| 1703 (a8_06) | `23 91 85 33 94 30 \|20\| 62 94 88 26 12 06` | "n'importe [20] il(62) ne(94) [88]". 'N'importe' confined (adopted). The adverb subclass "n'importe" licenses is the relative adverb ("où", "quand", "comment"), not a general clause adverb, and noun rivals are equally live. Not forced. |

## Per-clause results

1. **C1: FAIL** — zero windows *force* an adverb role. Four windows are compatible-not-forced (@642 weak, @760, @839, @1135), one (@1703) admits only the relative-adverb subclass, and the rest exclude the adverb. Compatible ≠ forced at battery grade (same standard as the parent's C1/C2).
2. **C2: FIRES — fence executed.** The clause-adverb route for 20 is fenced across the full 15-window profile. Stated cause: the four compatible windows all have equally-live noun/verb/subordinator rivals (plus punctuation or clause-boundary assumptions the stream does not fix); six windows (@280, @490, @668, @741, @958, @1270) place 20 in adverb-impossible slots (before "et"/"pas"/"qui", inside noun phrases); two windows (@703, @873) force a verb at the locus. The adverb arm never reaches "forced" anywhere.

No standing verdict contradicted or downgraded: the parent fence (conj/prep) and the adopted @703/@873 verb classifications stand; the 20-paradox stays in `poly-20-docket` (red-team venue); §7 intact (no polyvalence declared — the fence is per-window, no global class claim). Canonical-stream caveat stands (68/70 row offsets unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `adv-20-760-boundary` (P3) — strongest candidate window: @760 "la première [20], il(62) ne(94) est(59) à(39)". Test whether the clause boundary at @760/@761 is forced (via the right-context frame "est à [88] [66]": if the right side requires a clause break before 20, the boundary-adverb parse becomes leading). Bars: boundary forced + ≥1 other window forcing a boundary-adverb parse → revive the adverb arm; else fence @760 too.
2. `reladv-20-1703` (P3) — the surviving subclass: test 20 as *relative* adverb ("où"/"quand"/"comment") after confined "n'importe" (@1700-1702), which is the one frame that licenses exactly that subclass. Bars: if "n'importe [20] il ne…" admits only the relative-adverb parse with zero rivals → name the value at battery grade; else fence the relative-adverb arm.
3. `adv-20-1135-parse` (P3) — @1135 "[86] [20] il vient pour [98]": test once 86's INF-class arm is named whether the clause-boundary adverb parse hardens (a finite reading of 86 forces the boundary and kills the noun rival). Bars: boundary forced → revive adverb at this window; else fence @1135.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-adverb-20-wide.md` (this file).
- Queue: `adverb-20-wide` queued → verdict/null via temp-file + rename, own entry only; pre-write assert confirmed no prior verdict; JSON re-validated post-write.
- Lock `adverb-20-wide.lock`: created on start, deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
