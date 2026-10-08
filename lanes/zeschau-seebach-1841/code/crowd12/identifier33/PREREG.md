# PRE-REGISTRATION — 33-INFINITIVE IDENTIFIER, round 12 (work order 1)
**Executor:** 33-IDENTIFIER
**Timestamp: 2026-10-07 21:26:21 UTC** (written BEFORE any round-12 battery
computation; only standing/recorded numbers consulted)
**Work dir:** `code/crowd12/identifier33/` · **Report note:**
`code/crowd12/report_inbox/identifier33-33-id.md`

**Task (STATE.md WO1):** name 33's specific infinitive. The 8 "pour 33"
frames (@186/@408/@467/@846/@936/@1088/@1245/@1630, repaired 1,847-pair
stream, positions per `code/crowd4/REINDEX.md`) are an identification battery
on Nesselrode v8 — which infinitive follows "pour" at these frame positions
given each frame's surrounding context (pencil-GT anchors nearby, crib
windows, by-ear syllable chunks)?

## Standing record (not re-derived)
- F79 (GRANTED): 33 = infinitive-class (C1: I1 pre==00 ×8, I4 suc==29 ×5,
  I2 ×1; nominal signatures effectively zero). The 8 I1 windows are exactly
  the battery frames: pre==00 at @186/@408/@467/@846/@936/@1088/@1245/@1630.
- Board relied on: GT 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que;
  provisional 87=ce, 64=qui, 96=par, 59=est, 77="le"-conditioned;
  leads 00="pour" (strong), 16="i", 47="ce". 33 is infinitive-CLASS, not a value.
- F81: the double-pour stack "pour 33 16 pour 67 que" (pairs[1244:1255],
  label-corrected) has NO era license in ~16.5MB of 1840s formal French.
- F22 (inference): encipherer systematically stripped final "-er" (parl|er)
  — groups are sub-word chunks; 29 = the "-er" ending chunk.
- F77: Nesselrode v8's 54 "ment" tokens are archive.org OCR word-splits,
  VOID as French — no battery query may depend on "ment" tokens.
- F59: never score manual-tiling bearing counts — per-window/per-bigram
  counts only.
- Crib windows: "la première" (11 70 82 34 29 40) at pairs @754 and @1034
  (REINDEX.md). Frames @846/@936 sit ~90 pairs from these windows.

## Battery frames (verified against the repaired stream just now; 0-based)
| cluster | positions | cipher shape (00="pour"-lead) | tail gloss |
|---|---|---|---|
| F-A | @186, @1245 | 00 33 **16** 00 | 16="i"-lead, then 00="pour" (pour-stack) |
| F-B | @408 | 00 33 **01** 02 | 01, 02 unglossed |
| F-C | @467, @1088 | 00 33 **79** 80 | 79, 80 unglossed |
| F-D | @846 | 00 33 **96** 40 | 96="par"-prov, 40="e"-GT |
| F-E | @936, @1630 | 00 33 **21** 64 | 21 unglossed, 64="qui"-prov |

GT anchors within ±10 (for check A hand-reads):
- @186: none (prov: 87@180 "ce", 64@181 "qui", 87@191)
- @408: 11@400 "la", 34@404 "i"
- @467: 11@462 "la", 46@472 "que" (prov: 87@461 "ce", 96@465 "par")
- @846: 40@848 "e" (prov: 94@841 "ne"-strong, 96@847 "par", 64@854 "qui")
- @936: 82@929 "m", 40@943 "e" (prov: 96@927 "par", 64@938 "qui")
- @1088: 29@1097 "er" (prov: 64@1079 "qui")
- @1245: 40@1238 "e", 11@1243 "la", 46@1249 "que", 46@1254 "que"
  (prov: 87@1242 "ce", 77@1240 "le"-cond); pre-context "87 11" = "ce"+"la"
- @1630: 46@1625 "que" (prov: 64@1632 "qui", 87@1636 "ce")

## Structural fork (SURFACED, not resolved — conditions the battery)
Under fixed substitution + F22 granularity, 33 = ONE phonetic chunk:
- Fork S (stem): 33 = infinitive stem; infinitive = 33+suc. Consistent with
  I4 "33 29" = stem+"er" (F79). But then F-D's suc=96="par"-prov would be an
  infinitive-ending chunk — no French infinitive ends in /paʁ/ ⇒ Fork S
  REFUTES 96="par" (at least at @847). F-A's suc=16="i"-lead as an ending
  (/i/ alone) fits no standard infinitive ending either.
- Fork W (whole-word): 33 = complete monosyllabic infinitive; suc = next
  word. Then F-D = "pour INF par e…" is clean, but I4 "33 29" = "INF er"
  is ungrammatical ⇒ Fork W REFUTES the I4 stem+"er" reading (F79 GRANTED).
Both forks break something banked. The battery therefore runs the empirical
whole-word queries AND banks whichever fork the data supports as an explicit
conditional: any F-D ID is CONDITIONAL on 96="par" (provisional); any
monosyllabic-F-D ID additionally forces the Fork-S/Fork-W choice to the red
team. If F-D's tail queries come back empty, the fork is moot (recorded NULL).

## Candidate set (mechanical — fixed BEFORE tail queries)
- Pool: the clean 3.96M diplomatic corpus = all of
  `code/side-period/corpus/*.txt` EXCEPT `allgemeine-zeitung-*` (newspaper),
  `harvest-log.txt`, `adb-zeschau-heinrich-anton-von.txt`
  (verified: 3,960,009 tokens with the lane tokenizer, verbatim from
  round-11 arm1248: lowercase, ’-normalize, `[a-zà-ÿ]+`).
- `is_inf(w)`: w endswith ("er","ir","re") and len(w) > 3 (lane standing).
- Candidate set C = { X : is_inf(X), n_pool("pour X") ≥ 3 }, ranked by n.
  Hand-review drops non-infinitive false positives (e.g. adjectives like
  "premier"); every drop recorded with reason. C is frozen before any
  per-frame tail query runs.
- F77 compliance: no query depends on "ment" tokens; is_inf can't match
  "ment" (ends "nt").

## Checks (per cluster; all counts consecutive-token on the lane tokenizer)
- **R (rate prior):** X ∈ top-10 by n("pour X") on pool∖v8 (pool minus
  Nesselrode v8 — DISJOINT from the v8 tail corpus, so R⊥T by construction).
- **T (tail match, v8 only, NW=92,677):** X = UNIQUE argmax with n ≥ 2 of:
  - F-A: T_A(X) = n_v8("pour X W pour"), any single W.
  - F-B: n/a — tail (01, 02) unglossed; T cannot fire (recorded, not scored).
  - F-C: n/a — tail (79, 80) unglossed; T cannot fire.
  - F-D: T_D(X) = n_v8("pour X par W"), W[0] ∈ {e, é} — CONDITIONAL on
    96="par"-prov. Fallback datum (unconditional): n_v8("pour X W1 W2").
  - F-E: T_E(X) = n_v8("pour X W qui"), any single W — CONDITIONAL on
    64="qui"-prov. Fallback datum: n_v8("pour X W1 W2").
- **L (frame license, v8):** L_c = Σ_{X∈C} T_c(X) ≥ 1. If 0 → cluster
  FENCED (frame shape itself unlicensed; no ID possible). F-A pre-registered
  expectation: L fails per F81 (verified, not assumed).
- **A (anchor hand-read, v8):** for the R/T winner X, I hand-read v8 for a
  "pour X …" window compatible with the frame's GT anchors (±10 inventory
  above); record the window or "not found". Confirmation only — never a
  standalone leg. For F-A@1245/F-C@467 the pre-context "cela pour"
  (87+11) gets its own supplementary query n_v8("cela pour X").

## Recommendation bar (I recommend; the red team adjudicates — no status
changes applied by me)
- **ID:** R ∧ T fire for the SAME X, L passes, A found. (R,T independent
  via disjoint corpora = the lane's ≥2 independent checks.)
- **LEAN:** exactly one of {R, T} fires for X with L passing; OR R∧T same X
  but A not found. For T-n/a clusters (F-B, F-C): R alone → NULL (base-rate
  only is not an identification); LEAN requires R + STRIKING A.
- **NULL:** R/T fire for different X, or neither fires, or T-argmax ties
  without n≥2 separation.
- **FENCED:** L fails.
- Ties in T at top (n≥2 each, X among tied): cap at LEAN, never ID.

## What counts as "done"
`identifier33_results.json` (candidate set C with pool∖v8 ranks, per-cluster
R/T/L/A tables with exact counts, fallback datums, dropped false positives),
this PREREG.md, the script, and the report note at
`code/crowd12/report_inbox/identifier33-33-id.md` with per-cluster findings,
the recommendation per cluster, the structural-fork analysis, evidence
paths, and what would break ties. All positions 0-based repaired; no
ciphertext invented — every position verified against the 1,847-pair stream.
