# Battery verdict: val-02-prep-sweep

## Bar (verbatim from battery-queue.json, pre-registered)

"promote iff a preposition value parses >=2 windows; else fence"

**Restated as numbered pass/fail clauses:**
- **C1:** a preposition value for 02 parses >=2 of the 17 windows (zero ungranted assumptions; 1841-French geometry).
- **Else-arm:** fence the 02-preposition-class claim with stated cause.

## Method
- Read BATTERY-PROTOCOL.md first; lock `locks/val-02-prep-sweep.lock` created on start (agent 7cdcb38a, 2026-10-09T15:40:15Z), deleted on completion.
- Re-derived the repaired stream in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `repair_parse.py` (pair up from row offset, drop trailing odd digit). Verified: **1,847 pairs, 96 types**.
- `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- @-offsets are 0-based pair indices. Test: for each of the 17 windows of 02, whether "X [02] Y" parses as "X [prep] Y" with zero new assumptions under standing values (§7 of the protocol).
- Parent: `left-88-02-88-307` (NULL, 2026-10-09) — its prepositional arm needed a licensed 02-prep; this battery is its proposed follow-up #1.

## Window-level evidence (byte-exact)

n(02)=17. Standing values used: pencil GT (11=la, 70=pre, 46=que), 64=qui, 84=on, 79=tout, 00=pour (granted), 94=ne (STRONG LEAD, R17-001), 88=verb class (value open).

| @ | window (L3 L2 L1 **[02]** R1 R2 R3) | preposition-02 verdict |
|---|---|---|
| 128 | 82 48 11 **[02]** 26 32 96 | UNLICENSABLE — 11="la" (article or object pronoun): "la [prep]" ungrammatical on both readings; 48 valueless |
| 305 | 18 89 88 **[02]** 88 20 17 | UNLICENSABLE — "88-V [prep] 88-V": two finite-class cells; prep complement would need an infinitive, 88 is finite class |
| 410 | 00 33 01 **[02]** 53 84 51 | UNLICENSABLE — 01 valueless; no standing license |
| 459 | 13 66 14 **[02]** 79 87 11 | UNLICENSABLE — 14 valueless; right side "tout ce la" itself strained |
| 495 | 78 42 94 **[02]** 79 88 47 | KILL-GRADE EXCLUDED — 94="ne" (STRONG LEAD) must be followed by the verb; "ne [prep]..." ungrammatical |
| 609 | 64 39 64 **[02]** 58 47 77 | KILL-GRADE EXCLUDED — 64="qui" (promoted); "qui [prep]" ungrammatical in French |
| 695 | 39 74 46 **[02]** 50 45 28 | KILL-GRADE EXCLUDED — 46="que" (pencil GT, object-form); "que [prep]" unlicensed |
| 718 | 66 86 01 **[02]** 21 80 77 | UNLICENSABLE — 01 valueless |
| 750 | 28 00 64 **[02]** 97 40 67 | KILL-GRADE EXCLUDED — 64="qui"; "qui [prep]" ungrammatical (same as @609) |
| 858 | 32 48 84 **[02]** 24 49 74 | KILL-GRADE EXCLUDED — 84="on" (A15, subject pronoun) must be followed by the verb; "on [prep]..." ungrammatical |
| 887 | 68 37 03 **[02]** 00 86 06 | KILL-GRADE EXCLUDED — 00="pour" (A9); preposition + preposition ("*[de] pour") impossible |
| 916 | 37 96 09 **[02]** 24 49 74 | UNLICENSABLE — 09 valueless; complement 24 is finite/modal verb class, not infinitive-shaped |
| 1084 | 52 89 24 **[02]** 55 81 00 | UNLICENSABLE — best geometry ("V [prep] 55") but 55's class is open; licensing it needs a new assumption |
| 1152 | 33 66 84 **[02]** 00 92 29 | KILL-GRADE EXCLUDED — 84="on" subject pronoun + 00="pour" preposition; "on [prep] pour" doubly ungrammatical |
| 1299 | 04 62 16 **[02]** 70 37 08 | KILL-GRADE EXCLUDED — 70="pre" is a bound pencil-GT syllable; a preposition's complement cannot be a bound syllable |
| 1467 | 62 48 21 **[02]** 62 38 26 | UNLICENSABLE — 21 valueless; 62's cell absent per R20-125 ('il' killed) |
| 1819 | 29 37 01 **[02]** 09 19 00 | UNLICENSABLE — 01 valueless |

Tally: **8 windows kill-grade exclude preposition-02 on standing values alone** (@495, @609, @695, @750, @858, @887, @1152, @1299); **9 windows unlicensable without new assumptions**; **0 windows license a preposition value**.

The strongest candidate geometry is @1084 ("24-V [02] 55"): the verb host is standing, but 55's class is open — naming it nominal would be a new assumption, which the bar does not license.

Note on @305 (the parent's "88 02 88" window): "88 [prep] 88" would need 02's complement to be infinitival (the only verb-complementing prepositions are de/à/pour/avec + INF); 88 is forced finite class, not infinitive-shaped. The prepositional arm of left-88-02-88 stays closed at this window.

## Per-clause results
- **C1: FAIL** — 0 of 17 windows parse a preposition value with zero new assumptions; 8 are kill-grade hostile.
- **Else-arm: TAKEN** — the 02-preposition-class claim is fenced with stated cause.

## Verdict: NULL (fence executed)

The fence covers the preposition class of 02, stream-wide. It is not a class kill: individual windows (notably @1084) could re-open if a neighbor's class names favorably later; but as of standing values no preposition value for 02 is licensed anywhere. The parent claim's prepositional arm (`left-88-02-88-307`) remains closed. No standing/red-team verdict contradicted or downgraded; §7 intact. Canonical-stream caveat stands (68 of 70 upstream row offsets unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `val-55-1084-frame` (P3) — name 55's class at @1084 ("24 [02] 55"): a nominal 55 re-opens the single most promising 02-preposition window.
2. `syllable-02-tier` (P4) — test 02 as a bound syllable/letter-tier cell across its 17 windows; the word-level preposition class is fenced, but 02's tier is still open.
3. `redteam-02-prep-fence-input` (P4, gather-only) — package this 17-window fence as red-team input for 02's class; no battery decision.

## Bookkeeping
- Report: `code/crowd17/report_inbox/battery-val-02-prep-sweep.md` (this file).
- Queue: `val-02-prep-sweep` queued → verdict/null via temp-file + rename, own entry only; pre-write assert confirmed no prior verdict; JSON re-validated post-write.
- Lock `val-02-prep-sweep.lock`: created on start, deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched.
