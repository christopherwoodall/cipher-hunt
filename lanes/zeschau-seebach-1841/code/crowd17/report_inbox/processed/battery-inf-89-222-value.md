# Battery `inf-89-222-value` — verdict: NULL (fence executed)

## Bar (verbatim, pre-registered)

> "one value for 89 parsing @222 with <=1 ungranted assumption; kill the infinitive-value route iff no value does."

Restated as numbered clauses (before testing):

- **C1** — one (unique) infinitive value for 89 is named that parses @222 with ≤1 ungranted assumption → the naming claim promotes.
- **C2** — kill the infinitive-value route iff NO value parses @222 with ≤1 ungranted assumption (the value space is empty).

Adverses: none listed.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
(asserts held: 1,847 pairs, 96 types). `canonical.py` never used.

Standing premises adopted (not re-litigated):
- R24 (R19-191, red-team §7 act): 24='en' iff follower=85; 24=finite/modal
  verb elsewhere. At @222 the follower is 89 → 24 is finite/modal.
  This supersedes the queue claim's "24=modal (R17-009)" premise with the
  stronger red-team declaration; the modal arm survives unchanged.
- A8 verb-frame grant for 89 (value open); 89 takes the governed-infinitive
  role after modal 24 at @222 ("24 89" ×3: @222/@986/@1498).
- 16=infinitive (promoted); 61 nominal-ish (battery-grade "ce [61]" NP
  licensed by 87-determiner at @644–645, adopted).
- "[89]e" word finding (battery-grade): at all three "89 48" windows
  (@640/@871/@986), 48='e' is the word-final 'e' of 89's word, so 89's
  word ends in 'e'. Cross-window transfer licensed by §7 (67 sole
  polyvalence at battery level; R24 excepts 24 only — 89 has no
  polyvalence declaration, so @222's 89 and @986's 89 are one lexical item).
- No prior battery has named an infinitive value for 89
  (`battery-val-89-mirror.md` → null; `battery-class-89-adjudicate.md` →
  packaging verdict; report-inbox grep: only class-level readings
  89=noun / 89=infinitive / 89=verb ever appear).

## Window-level evidence

**Target locus byte-confirmed** (0-based, row a2_01):
`@219=42 @220=16 @221=24 @222=89 @223=61 @224=96`
→ "[42] [16-inf] [24-modal] [89-inf] [61-nominal] …"

**89 census (n=14, byte-exact):** @113, @222, @275, @285, @303, @640, @781,
@871, @986, @1082, @1377, @1393, @1498, @1752.
Predecessors: 29×5, 24×3, 52×2, 77×2, 18×1, 28×1.
Successors: 48×3 (@640/@871/@986 — the "[89]e" windows), 84×2, 68×1,
61×1 (@222), 28×1, 88×1, 11×1, 24×1, 16×1, 41×1, 26×1.

**The 'e'-final constraint:** 89's word ends in 'e' (granted finding, not an
assumption). A French infinitive ending in 'e' is the -re family. The
transitive -re field is large: faire, dire, mettre, prendre, écrire, lire,
suivre, connaître, rendre, vendre, perdre, attendre, entendre, répondre,
boire, croire, vivre, … (dozens).

**Non-uniqueness demonstration** — each of these parses
"[24-modal] [inf] [61-nominal]" at @222 with ZERO ungranted assumptions
(61's nominal status is adopted battery-grade; modal+infinitive government
is the standing frame; transitivity is lexicon, not assumption):
- 89="faire" → "…[modal] faire [61]…" parses.
- 89="dire" → "…[modal] dire [61]…" parses.
- 89="mettre" → "…[modal] mettre [61]…" parses.
No window, letter, or distributional evidence in the 14-window census
distinguishes among them: 89's only letter-tier neighbors are 29='er' ×5
(predecessor — 'er' is word-final, so 89 is word-initial there, giving no
interior letter) and 48='e' ×3 (successor — word-final, already consumed).
16's infinitive and 42's predicative class add no selectional pressure on
89's value.

## Per-clause results

- **C1 FAIL** — no UNIQUE value is forced. At least three (in fact dozens
  of) distinct -re infinitives parse @222 with ≤1 ungranted assumption, so
  no name can be given at battery grade. Naming any one of them would
  invent the value (§3 bars invention).
- **C2 does not fire** — the kill condition ("no value does [parse @222
  with ≤1 ungranted assumption]") is false: the value space is non-empty
  (faire/dire/mettre demonstrated above). The route is not dead.

## Verdict: NULL (fence)

89's infinitive value at @222 is underdetermined at battery grade: the
infinitive-value route is live (a value exists) but uncloseable on current
premises. Fence, not kill — a named 61 (the direct object selects the
verb) or letter-tier interior evidence re-opens it. No standing or
red-team verdict contradicted or downgraded (R24, A8, §7 intact; the
89-noun-locus split and its 77-gate untouched — this battery never
re-litigated Arm A). Canonical-stream caveat stands (row a2_01 offsets
unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `val-61-223-object` (P3) — Name 61's value at @223. A named direct
   object selects among the -re candidates via verb–object selection
   ("faire [61]" vs "dire [61]" vs "mettre [61]"). Bar: name 61 iff one
   value parses @223 with ≤1 ungranted assumption; else fence.
2. `inf89-letter-interior` (P3) — Census 89's 14 windows for letter-tier
   neighbors that could sit word-internal to the "[89]e" word; bar: name
   ≥1 interior letter of 89's word with byte evidence, or fence the
   letter route as exhausted.
3. `inf89-222-rerun-gated` (P4) — Gated re-fire of this bar once 61's
   value is named or 77's value resolves (Arm A cross-constraint via the
   89-noun-locus-rearm trigger); gated, not dispatchable now.

## Bookkeeping

- Queue: `inf-89-222-value` → `status: verdict`, `result: null`, 2026-10-09
  (pre-write assert: was queued/verdictless; temp-file + rename; JSON
  re-validated; own entry only; no downgrade).
- Lock created on start, deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
