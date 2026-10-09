# Battery verdict: inflect-19e-48

## Bar (verbatim from queue)
"resolve iff 48 = 'e'-inflectional at @1780 (if not, the single leg dissolves); if 19 inflects like 32, the adjective-class lead gains a second independent leg"

Restated as numbered clauses:
- C1: 48 = 'e'-inflectional at @1780. If not, adj-19's single predicative leg
  dissolves (kill-grade failure mode).
- C2: 19 inflects like 32 (stem + R17 letter-tier '-e', "est X-e" frame) — if
  so, the adjective-class lead gains a second independent leg.
- C3: every listed adverse answered (re-parsed cleanly, fenced with stated
  cause, or shown to be a misread — not ignored).

## Method
Read BATTERY-PROTOCOL.md first. Created `locks/inflect-19e-48.lock` on start
with agent id + UTC timestamp. Re-derived the repaired 1,847-pair / 96-type
stream in-session from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json` (parsed per `repair_parse.py`;
1,847 pairs, 96 types verified). `canonical.py` never used. R5005, sealed gate
instances, red-team adjudication queue untouched. All @-offsets below are
1-based stream indices (adj-19 convention), verified against the stream.

Standing values used: 48="e" letter-tier PROMOTED (R17-003); 32 = one verb
lexeme, class-level PROMOTE (R17-008); 59="est" provisional; 87="ce" promoted;
64="qui" banked GT. 1841 diplomatic French only. Every number re-derived on
the repaired stream.

## Window-level evidence

**The locus.** @1774-1783 (1-based) = `94 24 87 64 59 19 48 74 65 23`, all
mid-row a8_09 (no row boundary within +-3): @1776=87 "ce", @1777=64 "qui",
@1778=59 "est" (provisional), @1779=19, @1780=48, @1781=74. = "ce qui est 19[e]".

**C1 evidence.**
- Bigram census: "19 48" exactly once stream-wide (@1779-1780); "48 19" zero.
  Left-attachment morphology, parallel in kind to "32 48" (exactly 4 bigrams
  at 1-based 450/856/1177/1212, zero "48 32").
- R17-003 (red-team GRANT PROMOTE, letter tier) ratified @1780's 48 as one of
  five feminine/mute-'e' windows, stem positions (1-based)
  @283/@450/@1212/@1779/@1177 — i.e. the 48 at @1780 is already red-team
  certified 'e'-inflectional. Three of the five are the clean "32e" windows;
  @1779 is our 19.
- No A7-L2 conflict: the conditioned verb-stem frame's exclusive legs are the
  two "48 29" bigrams (@1230, @1590); @1780's 48 is followed by 74, not
  29="er". n(48)=38, 19 distinct predecessors, 28 distinct successors —
  letter-tier mobility, consistent with the grant.
- Kills hold (48="est"/"ne"/"de" killed); no window forces 48 != 'e' at @1780.
- Sub-distinction fenced: R17-003 bundles "feminine/mute-'e'" and the
  "ce qui" frame is gender-neutral, so feminine-vs-mute at @1780 is not
  battery-resolvable. The bar's operative test ('e'-inflectional) is met.

**C2 evidence.**
- Morphological antecedent HOLDS: "19e" = stem + R17 '-e' exactly as
  "32e" = stem + R17 '-e'; same "est X-e" copular frame shape; both stems'
  '-e' windows sit inside R17-003's ratified feminine/mute-'e' set.
- Class consequent FENCED: R17-008 re-tiered the invoked parallel —
  32 = one VERB LEXEME (class-level promote); "32e" is its feminine past
  participle ("est [32](e)" @449/@1211 0-based; participle-modifier
  @1176/@130/@532/@1283/@1572), and "the participle analysis dissolves the
  adjective/verb tension." The bar's consequent ("the adjective-class lead
  gains a second independent leg") was written against fem-32e's superseded
  adjective framing. Under standing red-team verdicts the "19e" ∥ "32e"
  parallel points verb-lexeme-ward (19 as verb lexeme with feminine past
  participle "19e" in the "est" frame) — or is class-neutral — not
  adjective-ward.
- Independence caveat: both "legs" live in the same single window
  (@1779-1780); the second leg is morphological-vs-syntactic, not
  locationally independent. The 9-window / one-copular-frame census from
  adj-19 is confirmed unchanged (19's other 8 windows: @91/@122/@212/@329/
  @486/@585/@966/@1822, none a second copular frame).

## Per-clause results
- **C1 — PASS** (at red-team grade, R17-003; stream-verified). The single
  predicative leg does NOT dissolve.
- **C2 — ANTECEDENT PASS, CONSEQUENT FENCED.** 19 inflects like 32
  morphologically, but the bar's adjective-class consequent does not follow
  under R17-008; the parallel's class implication needs red-team
  adjudication (verb-lexeme-shaped vs class-neutral).
- **C3 — adverses answered.** "single leg - 9 windows, one copular frame":
  partially answered — the predicative leg survives and a second,
  morphological leg ("19e" ∥ "32e") is established, but its class address is
  disputed (fenced, see C2). "promote blocked at battery grade": honored —
  no promote issued; the class question is escalated to the red team.

## Verdict: NULL
Not kill-grade: nothing forces the claim false — C1 passes at red-team grade
and the morphological parallel is real. Not promote: the adverse blocks
promote at battery grade, and C2's class consequent does not follow under
standing red-team verdicts (R17-008). Headline for the red team: the bar's
"adjective-class second leg" consequent is conditioned on fem-32e's
superseded adjective framing; under R17-008 the "19e" ∥ "32e" parallel
re-tiers 19 verb-lexeme-ward. Recorded findings: (a) @1780's 48 is
'e'-inflectional (R17-003, stream-verified); (b) "19e" ∥ "32e" holds
morphologically (same R17 '-e', same "est X-e" frame shape); (c) feminine-vs-
mute at @1780 unresolved (R17-003 bundles them); (d) both legs share one
window — morphological/syntactic independence only.

No standing verdict contradicted or downgraded. §7 intact.

## Follow-ups proposed (for supervisor queuing)
1. `verb19-lexeme-test` (P3) — test 19 as verb lexeme under R17-008's
   parallel: do all 9 windows parse under one verb lexeme (finite slots?
   participle frames?)? Classify each window's 19 slot (@91 "98 19 41",
   @966 "41 19 24" with 24='faire' finite, @486 "01 19 64" relative head,
   etc.). All-9-parse promotes 19 to 32's class; any forced non-verbal
   window fences/kills.
2. `participle-19e-frame` (P3) — "ce qui est 19e" @1778-1780 as
   passive/adjectival: does the frame select a past participle (verb-lexeme
   19) or an adjective? Discriminators: "par"-agent continuation (cf.
   fem-32e @1211 "est 32e par"), gender/number agreement behavior.
3. `fem-mute-48-1780` (P4) — discriminate feminine vs mute-'e' at @1780
   (R17-003 left it bundled). Parked until 19's class/value resolves; needs
   19's value or a gendered subject.

## Bookkeeping
- Report: `code/crowd17/report_inbox/battery-inflect-19e-48.md` (this file).
- `battery-queue.json`: `inflect-19e-48` -> status `verdict`, result `null`,
  date 2026-10-09 (temp-file + rename, own entry only; pre-write assert
  confirmed queued/verdictless; JSON re-validated post-write).
- Lock `locks/inflect-19e-48.lock`: deleted on completion.
- No standing verdict contradicted or downgraded. R5005, sealed gates,
  red-team queue untouched; `canonical.py` never used.
- 1841 diplomatic French only; every number re-derived on the repaired stream.
