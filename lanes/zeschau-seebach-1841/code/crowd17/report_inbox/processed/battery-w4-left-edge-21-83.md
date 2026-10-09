# Battery report: w4-left-edge-21-83 — W4 left edge @1158-1163 ("77 82 44 83 21 67")

- Target id: `w4-left-edge-21-83` (priority 3, status queued)
- Claim: the W4 left edge @1158-1163 ('77 82 44 83 21 67') decides whether 'et' coordinates an antecedent NP
- Worker: 62240c34-b206-4ee7-a17c-52e7c1845871
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
  `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`;
  1,847 pairs / 96 types re-derived in-session before testing).
  `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- Lock: code/crowd17/next-token/locks/w4-left-edge-21-83.lock (created on start; deleted on completion).
- Evidence: dict-45-w4-adjudicate null (2026-10-09), follow-up #2.
- Offset convention: @n below = 0-based pair index in the repaired stream
  (queue's 1-based @1159-1164 = stream @1158-1163).

## Bar (verbatim, pre-registered before testing)

"(a) parse the 6-gram under standing values with 21 and 83 named or fenced
with stated cause; (b) if 'et' coordinates a named antecedent NP, state
whether the coordination rescues or deepens the W4 residual; (c) coordinate
with dict-frame clause-3's fence (21's value = the blocker)"

Numbered pass/fail clauses (frozen before judging):

1. The 6-gram parses under standing values with 21 and 83 each named or
   fenced with stated cause.
2. If 'et' @1163 coordinates a NAMED antecedent NP, the coordination's
   effect on the W4 residual (rescue vs deepen) is stated.
3. The finding is coordinated with dict-frame clause-3's fence, whose stated
   blocker is 21's (and 83's) open value — no contradiction introduced.

Adverses (queue field; the dispatch brief's "None" does not match the queue
record — queue is canonical): "83='de' lead (R17); 77='le' provisional".

## Method

1. Re-derived the repaired stream in-session (1,847 pairs / 96 types, byte-exact).
2. Byte-verified the window: seq[1158:1164] = ['77','82','44','83','21','67']
   (row a6_09; 1-based @1159-1164). Wider frame: @1148=67, @1156=80, @1157=17,
   @1164=78, @1165=45, @1166-1168=13-55-61 — matches dict-45-w4-adjudicate.
3. Censused 44 (n=15) and 21 (n=30) contact profiles; counted "82-44"
   (1/1847: this window only — hapax bigram) and "44 83 21" (2/1847: @1160
   and @1839, "22 42 44 83 21").
4. Standing values used: §7 banked (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e,
   46=que); granted (87=ce, 64=qui, 96=par, 17=fois, 79="tout", 00="pour",
   84="on", 47="ce" allophone tier); provisional 77="le", 59="est";
   R17 leads: 83='de' (83-'de' lead), 94='ne' STRONG LEAD;
   67 et/veut sole true polyvalence with positional rule (67='veut' iff
   follower infinitive-shaped); 21 noun-class battery-promoted, value open.

## Window-level evidence

The 6-gram (0-based @1158-1163): `77 82 44 83 21 67` = "le(prov.) m(82) [44]
de(R17) [21-noun] et(67)".

### Candidate parses of the 5-gram "77 82 44 83 21"

- **S1 (survives, fence): NP skeleton "le [X] de [21-noun]".** Determiner +
  [X] + "de" + noun = grammatical NP shape. X = "82 44", a stream-unique
  bigram (1/1847), value unnameable at battery level. Note X is genuinely
  two cells: 82='m' is banked GT, so X is not a single open cell.
- **S2 (killed): X = "même".** Needs 44='e'; 40='e' is banked pencil GT and
  §7 requires red-team-level homophony evidence (1690 frequency uniformity
  necessary but insufficient). Barred at battery level — kill grade within
  scope.
- **S3 (killed): clitic chain "le m'[44-verb] de [21]".** "le"+"m'" double
  object clitics need a subject before them; the preceding token @1157=17
  ('fois', granted) cannot host it. "le m' + [V] + de + [21]" is
  ungrammatical French — kill grade.
- **S4 (killed): word-internal "77 82 44" = one word "lem[44]".** No French
  word "lem…"; nothing in the lane record supports an 77-82-44 unit —
  kill grade by distributional rejection.
- **S5 (fenced, not adoptable): X = "[44]-coda syllable" of a longer word.**
  Needs 44's value; 44's profile (n=15, successors 00x3/59x2/74x2/83x2)
  names nothing. Unnameable without invention — fenced, not adopted.

The mirror window @1839-1841 ("22 42 44 83 21") shows "44 83 21" as a
two-window unit, but with predecessor 42, not 77-82 — no value transfer to
X is licensed.

### 'et' @1163

67='et' by the §7 positional rule: follower 78 is noun-shaped (per the
parent report's re-derivation: 77/47/37 determiner-predecessors), not
infinitive-shaped, so 67='veut' is excluded. Right conjunct = "78 45
13 55 61 94…" = "verdict [13-55-61] ne…" (conditional on 78='ver' LEAD +
undeclared one-word boundary, per dict-45-w4-adjudicate).

## Per-clause pass/fail

1. **PASS (fence).** The 6-gram parses under standing values as the NP
   skeleton S1: "le(prov.) [X] de(R17) [21-noun]" — with X unnameable
   (82-44 hapax; S2-S4 killed, S5 fenced). 83='de' is NAMED (R17 lead,
   answering the adverse). 21 is FENCED with stated cause: noun-class
   battery-promoted (pending red-team ratification), value open; the
   battery-grade lexical value search is KILL-closed (val-21-reopen KILL,
   2026-10-09 — re-open only if red team overturns 65=noun, grants a 21-65
   unit verb, or changes 21's class). 77='le' fenced as provisional
   (answering the adverse): if 77 resolves otherwise, the skeleton changes.
2. **CONDITION DOES NOT FIRE.** The left edge is not a NAMED antecedent NP:
   X is unnameable and 21's value is kill-closed at battery level. 'et'
   therefore does not coordinate a named antecedent NP at battery level, so
   no rescue/deepening statement is licensed. Consistency note (not a
   declaration): granting the coordination provisionally (as dict-frame
   clause-3 does) would DEEPEN, not rescue, the W4 residual — the right
   conjunct "verdict [13-55-61]" retains the determiner-gap kill-grade
   finding ("et" + bare singular countable noun, per dict-45-w4-adjudicate).
3. **PASS.** Fully consistent with dict-frame clause-3's fence: "67 forced
   by the positional rule; the blocker is 21's (and 83's) open value, not
   67." This battery tightens clause-3's "83's value open" to "83='de'
   named (R17 lead)" and confirms 21's value as the durable blocker — now
   kill-closed, not merely open. No standing red-team verdict contradicted.

Adverses:
- "83='de' lead (R17)": answered — adopted as the named parse; no
  battery-level rival for 83 appears at this window.
- "77='le' provisional": answered — fenced with stated cause (skeleton
  conditional; re-audit if 77 resolves otherwise).

## Verdict: NULL (fence executed)

Headline: the W4 left edge does NOT decide whether 'et' coordinates an
antecedent NP — the decision still pivots on 21's value, which is
kill-closed at battery grade (val-21-reopen KILL), and on 44's unnameable
hapax X. The surviving parse is the NP skeleton "le [X] de [21-noun]"
with X unnameable and 21 value-open-but-kill-closed. dict-frame clause-3's
fence stands, tightened: 83='de' is named (R17), 21's value is the durable
blocker. No standing or red-team verdict contradicted; §7 intact.

## Follow-ups (null regenerates work; all verified ABSENT from
battery-queue.json 2026-10-09)

1. **reseg-82-44-1160** (priority 3). Claim: the 82-44 hapax bigram resolves
   by re-segmentation. Bars: (a) enumerate admissible segmentations of
   @1159-1161 under standing values ("77 | 82 44", "77 82 | 44",
   word-internal "82-44"); (b) adopt one iff it parses with zero new
   assumptions and kills/fences all rivals; (c) else fence with stated cause.
   Evidence: this report (82-44 = 1/1847). Adverses: 82='m' banked GT —
   no homophony claim without §7 red-team evidence.
2. **w4-coord-21-44-de** (priority 3). Claim: conditional re-test of the
   left-edge coordination once the red team adjudicates 21's value/class.
   Bars: (a) re-run the bar (a)-(b) of this battery under the adjudicated
   21 value; (b) state whether the coordination rescues or deepens the W4
   residual; (c) declare nothing beyond the adjudicated frame.
   Evidence: this report. Adverses: gated on the red-team 21 docket;
   do not run before adjudication.
3. **val-44-noun-sweep** (priority 4). Claim: census 44's 15 windows for a
   noun value fitting both "44 83 21" units (@1160, @1839). Bars: (a) state
   44's forced slot at each window under standing values; (b) name a noun
   value iff one parses at both "44 83 21" windows with zero hard
   contradictions; (c) kill 44-noun iff no candidate survives.
   Evidence: this report (44 n=15 profile). Adverses: 44="l'" live at
   @1714 (antecedent-44-l-prime) — §7 sole-polyvalence respected, no
   battery-level polyvalence declared.

## Reproducibility

Stream re-derived in-session 2026-10-09 (1,847 pairs / 96 types);
seq[1158:1164] = ['77','82','44','83','21','67']; n(44)=15; n(21)=30;
"82-44" x1 (@1159); "44 83 21" x2 (@1160, @1839); 21 successors:
67x8/62x5/60x4/65x4. No writes outside this report, the queue edit (own
entry only, temp-file + rename), and the lockfile (deleted).
