# Battery verdict: finiteness-88-86

- Target id: `finiteness-88-86`
- Claim: "decide 88's role at @86 vs 14-06"
- Date: 2026-10-09
- Worker: subagent session 70c0af3f (parent: next-token-supervisor)
- Lock note: no pre-existing lock in `code/crowd17/next-token/locks/` at start;
  created `locks/finiteness-88-86.lock` 2026-10-09T06:16Z, deleted on completion.

## Bar (verbatim, pre-registered)

"resolve iff @86 parses under the same governor-88 value with 14-06's class stated; else fence with stated cause"

## Numbered clauses (fixed before testing, not modified after)

- **C1:** @86 parses with 88 in the same governor role granted class-level by
  battery-governor-88-value (2026-10-08, PROMOTE: 88 = VERB-CLASS,
  verb stem/governor; no value named) — i.e. the '88 le 66' transitive frame
  under 77='le' (provisional), with no contradiction of standing values and
  no new value or polyvalence declared.
- **C2:** 14-06's class is STATED with evidence: adverb-class X-"ent" vs
  finite-verb rival decided on the stream, with the value question left
  explicitly open ('sou' and 'souv' both killed 2026-10-09; no value claimed).
- **Verdict rule (pre-registered):** resolve (promote) iff C1 and C2 pass AND
  both adverses are answered; kill iff a window forces @86 out of the
  verb-governor role; else null, fenced with stated cause.

## Method

Read BATTERY-PROTOCOL.md in full before touching anything. Re-derived the
1,847-pair / 96-type stream from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json` parsed exactly like
`code/side-keyhunt/repair_parse.py` (byte-exact
`[s[i:i+2] for i in range(o, len(s)-1, 2)]`; 1847 pairs, 96 types verified).
`code/side-keyhunt/canonical.py` never used. R5005, sealed gate instances,
and the red-team adjudication queue untouched. All @-offsets are 0-based
repaired-stream pair indices. Standing values used: banked 11=la, 70=pre,
82=m, 34=i, 29=er, 40=e, 46=que; promoted 87=ce, 64=qui, 96=par, 17=fois,
79=tout (A5), 00=pour (A9 class-level), 84=on (A15), 47=ce (A4), 39=a/a;
provisional 59=est, 77=le; standing 06=ent (red-team round-17 per
souvent-14-06-retest; battery-promoted per governor-88-value); 88 VERB-CLASS
class-level (battery-governor-88-value). Every count below re-derived from
the stream by this worker, none copied.

## Window-level evidence

### The locus @84-88 (row a1_02, mid-row, no boundary)

`@80-96: 98 51 62 16 | 14 06 | 88 77 66 98 19 98 81 97 46 29`
i.e. `@84=14 @85=06 @86=88 @87=77 @88=66`, all on row a1_02.

### Census facts (re-derived)

- **88-77 windows: exactly 3** — @86 (follower 66), @646 (follower 78),
  @1541 (follower 78). Confirms the adverse: @86 is the one 88-77 window
  not followed by 78.
- **77->66: x1 stream-wide** (only @87). 77 n=44; top successors 78 x7,
  84 x7, 86 x5, 81 x4.
- **"14 06" bigrams: exactly 2** — @84 (`16 14 06 88`, a1_02) and @1121
  (`70 12 06 14 06 11`, a6_07). 14 n=15 at @72, 84, 117, 141, 178, 339,
  424, 458, 586, 623, 813, 896, 1121, 1365, 1689 (matches prior census
  byte-exact).
- **06 n=44**; 06->88 x1 (only @85, this window); 06 predecessors include
  14 x2 (the two bigrams), 12 x2, 42 x5, 30 x4, 82 x4.
- **16 n=28**; predecessors 82 x11, 62 x4; successors 00 x4, 24/01/91/76 x2,
  14 x1 (@83), 88 x1 (@903), 29 x1. Verb-class distributionally supported
  ("m 16" x11, "62 16" x4, "16 pour" x4 — per souvent-14-06-retest,
  re-derived identical here).
- **66 n=19**; 00->66 x7 ("pour 66"); 66 object-head open.

### C1: @86 under the governor-88 role

Under 77='le' (provisional), `@86-88 = "88 le [66]"`: verb + direct-object
noun phrase = the transitive frame of a verb-class governor. This is L4 of
the class-level grant (battery-governor-88-value), re-derived unchanged:
no new value named, no standing value contradicted, 66's profile offers
no hostility (00->66 x7 shows 66 takes pour-complements; object-head
reading open and consistent). **C1: PASS.**

### C2: 14-06's class, stated

Two class candidates for the bigram type 14-06 (06='ent' standing):

- **(A) Adverb-class X-"ent"** ("souvent"-shaped; value open). Class-level
  survivor of today's souv-14-06-repair KILL: "The [14]ent adverb frame
  shape survives at CLASS level ... only the VALUE 'souv' is killed."
- **(B) Finite verb, 3pl** (stem 14 + "ent" 3pl ending).

Decisive test at @1121: `70 12 06 | 14 06 | 11` = "prennent [14-06] la"
(70='pre' banked, 12='n' battery-promoted, 06='ent' standing: "prennent"
exact). Under (B) this reads "prennent Xent la": two finite verbs
adjacent with no coordinator and no intervening subject — ungrammatical
French, with no standing lane frame licensing zero-marked finite-verb
juxtaposition. Under (A): "prennent souvent la" — clean. **(B) rejected
at @1121.**

Bridge to @84: §7 sole polyvalence (67 et/veut) bars the bigram type
14-06 from being adverb-class at @1121 and finite-verb at @84 without a
red-team ruling. Both windows share one class.

**14-06's class, stated: X-"ent" ADVERB-class; value open**
('sou' killed souvent-14-06-retest 2026-10-09; 'souv' killed
souv-14-06-repair 2026-10-09; no third value tested). **C2: PASS.**

Consequence for the claim: 14-06 is not finite and cannot govern an
infinitive, so 88@86 is not "infinitive after 14-06". 88 heads its own
verb phrase in the transitive frame — the same verb-class governor role
as @646/@1541 (there with infinitive complements, here with a nominal
object). Finiteness decided at the bar's scope: **88@86 = finite
transitive verb-governor; 14-06 = adverb, independent of 88.**

### Residual fenced (not a bar failure)

Whether 88@86 is finite with a clause boundary after the adverb, or a
non-finite complement of a modal-shaped 16, is NOT decided here: 16's
complement profile (16->00 x4 main-verb+pour frame; 16->24 x2 finite-verb
follower, anti-modal; 16->88 x1 @903) forces neither reading, and both
keep 88 in verb-class. Narrower follow-up material if the lane wants it;
the bar's C1 is the class-level governor parse, which passes either way.

## Adverses answered

- **"@86 is the one 88-77 window not followed by 78": ANSWERED.** The
  difference is complement type, not governor class: @646/@1541 =
  governor + infinitive-complement frame; @86 = finite transitive frame
  ('88 le 66', NP object; 77->66 x1 stream-wide). Both are verb-class
  governor slots; the class-level grant's L3/L4 already integrate both.
  Not hostile to the governor role.
- **"14's class open": ANSWERED.** 14's VALUE is open (two kills today,
  none revived here); 14-06's CLASS is stated as X-"ent" adverb with the
  finite-verb rival rejected at @1121 and bridged to @84 by sole
  polyvalence. The bar asks for the class stated — done, with no value
  over-claimed.

## Per-clause results

- C1 (@86 parses under the same governor-88 role): PASS
- C2 (14-06's class stated with evidence): PASS
- Adverses: both answered (see above)

## Verdict: PROMOTE (relational decision; no value named)

88's role at @86 is decided: **finite transitive verb-governor**
('88 le 66'), the same verb-class governor role granted class-level by
battery-governor-88-value; **14-06 is an X-"ent" adverb** (value open),
not a finite verb and not governing 88. No standing red-team verdict is
contradicted (R16-005's 78='ver' LEAD untouched; the lever-77-78
composition not re-litigated; the souv-14-06-repair KILL respected, not
downgraded; §7 sole polyvalence invoked, not extended). No new value,
class, or polyvalence declared — class-level only, per the grant's own
constraint. No follow-ups required by a promote; the fenced 16-relation
residual above is available if the supervisor wants a narrower target.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-finiteness-88-86.md` (this file).
- Queue: `battery-queue.json` `finiteness-88-86` queued -> verdict/promote,
  date 2026-10-09 (pre-write assert: no prior verdict; own entry only;
  temp-file + rename; JSON re-validated).
- Lock: created 2026-10-09T06:16Z (no pre-existing lock); deleted on completion.
- canonical.py never used; R5005, sealed gates, red-team queue untouched.
