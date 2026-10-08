# Battery report: tout-14-rerun (re-test tout-[14] parallelism once noun-60 lands)

Worker: 18febb37-ceaf-4600-a754-12847d0ece5e. Date: 2026-10-08.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt), parsed per code/side-keyhunt/repair_parse.py.
canonical.py never used. R5005 never touched. @i = 0-based pair index.
No red-team verdict on 14 exists — no contradiction, no escalation.
Note: noun-60 has landed (battery-noun-60.md, 2026-10-08): 60's
masculine-noun value is KILLED; the live rival is 60=masculine-adjective
+ 03=masculine-noun. Verbal-60 windows (@1338, @700) are live but their
polyvalence question is fenced to the red team per §7 — not used here.

## Bar (verbatim, pre-registered before testing)

"name 14='le' (determiner) iff 'tout le [60-noun]' parallelism holds AND
the '62-94-79-14-60' SVO wall falls; coordinate with
frame-62-94-79-reparse, do not duplicate noun-60's bar"

Numbered clauses (fixed before data examination):

1. (C1) The 'tout le [60-noun]' parallelism holds under the LANDED
   noun-60 outcome (60 nominal KILLED; adjective rival live). Per the
   brief, the adjective rival's effect on the frame is recorded with
   stated consequences, not forced into the old bar.
2. (C2) The '62-94-79-14-60' SVO wall falls: the frame parses under
   standing values. (Frame resolution itself is owned by queued
   frame-62-94-79-reparse — this clause records only whether the wall
   fell for the purpose of naming 14.)
3. (C3) Adverse answered: "determiner reading was SVO-killed inside the
   unparsed frame."

## Method

Fresh parse per protocol; no prior counts trusted. All 15 windows of 14
scanned (@72, 84, 117, 141, 178, 339, 424, 458, 586, 623, 813, 896,
1121, 1365, 1689). '79 14' bigrams, '14 60' bigrams, 79-predecessor and
94-successor censuses re-derived. Standing values used: banked 11=la,
29=er, 46=que, 82=m; granted 64=qui, 47=ce (A4), 79=tout (A5),
84=on (A15); provisional 77=le, 59=est; battery-promoted 94=ne, 30=pas,
12=n (letter), 39=a/a. 62's value is open (collision-62-84 killed
62='on' unconditioned; 62='il' rival not promoted). noun-60's verdict
used as input, not re-tested (no duplication).

## Window-level evidence

W1 — '79 14' is frame-exclusive. Re-derived: '79 14' occurs x2 only
(@1365, @1689), both inside the '62-94-79-14-60' family. '79 77',
'79 11', '79 47' occur x0 anywhere — 'tout' never precedes another
determiner outside this frame. '79 87' x2 (@460, @1799) is 'tout
cela' (A5), a different construction.

W2 — the frame, re-derived on the repaired stream. @1362-1366:
'62 94 79 14 60' (row a7_06); @1686-1690: '62 94 79 14 60' (row a8_05).
'94 79' is a 2-window exclusive bigram (79's predecessor census: 94 x2,
92 x2, 64 x2, 02 x2, 33 x2, others x1; 79 n=18).

W3 — C1 under the landed outcome. The parallelism required 60 nominal.
60 nominal is KILLED. Under the live adjective rival the frame tail
re-reads as '79 14 60 03' = "tout le [60-adj] [03-N]" — a grammatical
NP shape ("tout le [adj] [N]", cf. "tout le beau monde"), with 60-adj
+ 03-noun coherent per the noun-60 battery (W2/W4: "[adj] [N] a [74]
que", "[adj] [N] qui [V]", zero unattested assumptions). But this is
NOT the pre-registered parallelism: it no longer parallels 'tout me
[48-verb]' (A7-L2, clitic+verb construction, granted frame) — the
construction type differs. And "tout le [60-adj]" without the 03-noun
head is ungrammatical French ('le' + bare masculine adjective heads
nothing). Under the live verbal-60 windows (@1338 'qui 60', @700 'ne
60'), 'tout le [60-V]' is ungrammatical word order (clitic 'le' would
precede the verb). So under every live reading of 60, the
'tout le [60-noun]' parallelism fails.

W4 — C2: the wall is load-bearing on 94/79, not on 60. With 94='ne'
(battery-promoted) the frame reads "on/il ne tout le [X]" — 'ne'
requires a verb after it; 79='tout' (granted A5) is not a verb. This
holds for every value of X: killed 60-nominal, live 60-adjective,
live 60-verbal, and 62's open value ('on' or 'il' both precede 'ne'
cleanly per the collision battery's 'il ne' re-read). The '94 79'
bigram stays a 2-window exclusive anomaly. The wall does not fall.
Frame resolution stays with queued frame-62-94-79-reparse.

W5 — C3: the adverse is not answered. The determiner reading remains
unable to rescue the frame. New consequence of the adjective rival:
14='le' (determiner) is now TAIL-compatible — it would head the NP
"le [60-adj] [03-N]" at @1365-1367/@1689-1691 — but the frame head
('94 79') still blocks the full parse. So the adverse stands, re-framed:
the blocker moved from the 60-slot to the 'ne tout' head.

W6 — no kill-grade window against 14='le'-determiner itself. The
breaker windows (@424 '47 14 62', @623/@896 '82 14', @1121 '06 14 06')
were fenced with stated cause by tout-slot-14; none forces 14's class.
The clitic-vs-determiner tie is unchanged.

## Per-clause pass/fail

- C1: FAIL. The parallelism's noun premise is dead under the landed
  outcome. Under the adjective rival the tail re-shapes to
  'tout le [adj] [N]' — coherent as an NP but not the pre-registered
  parallelism (different construction from 'tout me [48-verb]').
- C2: FAIL. The SVO wall stands under all live readings of 60 and 62;
  it is load-bearing on 'ne'+'tout', independent of 14's value.
- C3: FAIL (unanswered, re-framed). Determiner reading still cannot
  rescue the frame; the blocker is now the 'ne tout' head, not the
  60-slot.

## Verdict

**null** — the pre-registered bar is unsatisfiable under the landed
noun-60 outcome, but the claim 14='le' (determiner) is NOT forced
false: under the live adjective rival, 14='le' heads a coherent
"le [60-adj] [03-N]" NP tail at both frame windows. No window forces
the claim false; no cleaner rival is demonstrated (clitic tie
unchanged). Not a kill. Work regenerates below.

Coordination note: noun-60's bar was not duplicated (its verdict used
as input); the frame's resolution was not attempted (owned by queued
frame-62-94-79-reparse).

## Follow-ups (work regenerates; none duplicate queued targets)

1. **le14-adj60-tail** (priority 2). Claim: 14='le' (determiner) heads
   the frame tail under the adjective rival. Bars: "resolve iff
   '14 60 03' @1365/@1689 parses as 'le [60-adj] [03-N]' with the
   '94 79' head resolved per frame-62-94-79-reparse; gated on adj-60
   naming 60's adjective value; else fence 14's value as
   frame-dependent." Evidence: noun-60 battery shows 60-adj + 03-noun
   coherent on these exact windows, zero unattested assumptions.
   Adverses: '94 79' head still anomalous; adj-60 not yet run.
2. **clitic-14-82-breakers** (priority 3). Claim: the '82 14' x2
   windows break the clitic-vs-determiner tie. Bars: "name 14's class
   iff '82 14' @623 ('82 14 59') and @896 ('82 14 98') both parse under
   one class with 82='m' banked (clitic cluster vs determiner after
   elided 'm''), <=1 stated assumption; else fence as tie." Evidence:
   the only two 14-windows with a banked-value predecessor; tie
   recorded by tout-slot-14. Adverses: 59='est' provisional at @623;
   98's value open at @896.
3. **det14-elsewhere** (priority 3). Claim: 14='le'-determiner has legs
   outside the frame. Bars: "record a determiner leg iff >=2 of
   @72/@141/@339/@586 parse as determiner + named nominal head with
   zero contradictions; else fence 14's determiner value to the frame
   tail." Evidence: @339 '31 14 45 64' ("[31] [14] ce qui"), @586
   '18 14 00 97' ("[14] pour [00]" — determiner-hostile), @72
   '87 14 24' ("cela [14]..."), @141 '66 14 74'. Adverses: several
   windows look determiner-hostile; heads unnamed.
