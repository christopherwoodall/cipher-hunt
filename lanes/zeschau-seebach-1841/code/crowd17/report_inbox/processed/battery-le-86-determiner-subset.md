# Battery verdict: le-86-determiner-subset — 86='le' on the determiner-shaped subset

Date: 2026-10-08. Worker: 9100ed62-822b-40f1-912a-ac4537809d92.

## Bar (verbatim from battery-queue.json)

"promote iff all nine determiner-shaped windows parse under 'le' with
50/01/52/56/66 in nominal slots + the 'ce le'/'la le' windows (#0, #6, #24)
explained by re-segmentation or fenced with cause."

### Numbered clauses (operative, pre-registered)

1. All nine determiner-shaped windows (#5, #14, #16, #17, #18, #19, #27,
   #28, #30) parse under 86='le' with the follower (50/01/52/56/66) in a
   nominal slot.
2. Windows #0 (@175), #6 (@671), #24 (@1345) are explained by
   re-segmentation or fenced with stated cause.

Listed adverses: #0 ('ce le') and #6 ('la le') force 86='le' false as a
GLOBAL value at kill grade (pencil/granted neighbors only) — this test is
subset-scoped only, never global; the global kill is not re-litigated.

## Method

Parsed the repaired 1,847-pair stream exactly per
code/side-keyhunt/repair_parse.py (repaired_offsets.json +
data/upstream-ct_R5005.txt); canonical.py never touched. Re-derived all 32
windows of 86 with @-offsets independently (n=32 confirmed; all @-offsets
match battery-stem-86). Banked values used: pencil 11=la, 70=pre, 82=m,
34=i, 29=er, 40=e, 46=que; granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout,
00=pour, 47=ce, 84=on, 12=n, 48=e, 30=pas, 06=ent; provisional 59=est,
77=le. 67 et/veut positional rule applied (67="veut" iff follower
infinitive-shaped; 86 followed by 52/66 is not infinitive-shaped, so 67="et"
in #18/#27 — also forced grammatically since "veut le [N]" is
ungrammatical). No R5005 contact, no sealed gates, no red-team queue contact.

## Clause 1 — the nine windows (re-derived @-offsets)

Nominal-slot evidence for each follower (independent of the nine windows):

- 50 (n=11): "11 50" x2 (@379 "48 00 11 50 82 16" = "e pour la [50] m [16]";
  @1263). Follows 11=la (pencil) twice → nominal. STRONG.
- 01 (n=28): "87 01" x2 (@344 "96 43 87 01 06 70" = "par [43] ce [01] ent
  pre"; @1028). Follows 87=ce (granted) twice → nominal. STRONG.
- 52 (n=27): "11 52" x3 (@1006 "47 91 11 52 35 18" = "ce [91] la [52] [35]
  [18]"; @1123, @1721). Follows 11=la three times → nominal. STRONG.
- 66 (n=19): "00 66" x7 (@188 "33 16 00 66 24 87"; @245, @253, @714, @1108,
  @1493, @1532). Follows 00=pour (granted) seven times → nominal. STRONG.
- 56 (n=23): "96 56" x1 (@131 "02 26 32 96 56 64 21 65" = "[26] [verb] par
  [56] qui [21] [65]"). 56 takes the relative "qui" (64=qui granted) with
  21=NOUN/65=noun in the relative clause → nominal. WEAK-POSITIVE (single
  independent leg; no verb frames for 56 anywhere: never followed by
  29='er', never in 24/67-verb slots as verb).

Per-window results under 86='le':

- #5 @661 "62 16 00 86 50 80 03": "pour le [50]" — 50 nominal (la-frame).
  PASS.
- #14 @948 "62 98 96 86 01 77 86": "par le [01]" — 01 nominal (ce-frame).
  PASS. Caveat (fenced, see §Caveats): R2-R3 "77 86" is window #15's
  occurrence; under provisional 77='le' it reads "le le", but 77='le' is
  provisional, not granted, and #15 is a separate 86 occurrence under
  separate adjudication.
- #16 @962 "67 96 00 86 56 41 19": core "00 86 56" = "pour le [56]" parses
  (56 nominal-weak @131), BUT the full window reads "et par pour le [56]":
  "96 00" = "par pour" is ungrammatical under GRANTED values (96=par,
  00=pour). No re-segmentation available (groups atomic; 96 polyvalence
  barred by the 67-sole-polyvalence law). The defect is ORTHOGONAL to 86's
  value — any value of 86 leaves "par pour" broken — so it does not refute
  86='le', but the window as a whole does not parse. FAIL (strict).
- #17 @1002 "82 33 00 86 56 47 91": "m [INF] pour le [56] ce [91]". PASS.
- #18 @1099 "06 29 67 86 52 82 94": "ent er et le [52] m [94]" — 67="et"
  (positional + grammatical force). 52 nominal (la-frame x3). PASS.
- #19 @1128 "37 43 00 86 52 37 86": "pour le [52]" core. PASS. Caveat:
  R2-R3 "37 86" belongs to window #20's occurrence (separate
  adjudication); noted, not litigated here.
- #27 @1458 "61 21 67 86 66 79 17": "[61] [21] et le [66] tout fois" —
  67="et"; 66 nominal (pour-frame x7). PASS.
- #28 @1506 "42 33 00 86 56 41 12": "pour le [56]". PASS.
- #30 @1792 "47 03 00 86 56 42 94": "ce [03] pour le [56] [42] [94]". PASS.

Clause 1 score: 8/9 windows parse fully; #16's determiner core parses but
its L2 "par pour" adjacency is ungrammatical under granted values,
orthogonal to 86. Per the pre-registered bar ("all nine ... parse"),
Clause 1 FAILS strictly.

## Clause 2 — #0, #6, #24 (re-segmentation or fence)

Re-segmentation attempts on bytes (all fail to demonstrate):

- #0 @175 "60 09 87 86 21 69 14" ("ce [86] [21]", 87=ce granted,
  21=NOUN class): 87-86 as one word would be "cele" — no such French word;
  86-21 as one word undemonstrable (21's class is group-scoped); 86 as
  word-final "-le" of a word starting at 09/87 undemonstrable (87=ce is a
  complete word). No clean re-segmentation.
- #6 @671 "20 67 11 86 24 80 03" ("la [86] [24]", 11=la pencil, 24=finite
  verb class): "la le [24]" ungrammatical whether 11 is determiner ("la le
  V" needs a noun) or pronoun (clitic cluster "la le" invalid); 11-86 =
  "lale" no; 86-24 = clitic "le" + finite verb needs a subject, but 11 is
  not one. No clean re-segmentation.
- #24 @1345 "52 38 47 86 66 73 34" ("ce [86] [66]", 47=ce granted,
  66 nominal): "ce le [66]" ungrammatical (same frame as #0); 47-86 =
  "cele" no; 86-66 = "le [66]" is a clean NP but L1 47=ce breaks it.
  No clean re-segmentation.

FENCE with cause: the three windows place 86 immediately after a
determiner (87/11/47 = ce/la/ce), a frame where standalone 'le' is
ungrammatical in 1841 French; no word-internal re-segmentation is
demonstrable on current bytes (neighbors open or class-only). They are
fenced as non-determiner-life occurrences of the 86 digit-pair. The fence
is distributionally grounded, not circular: on the repaired stream, the
bigram pattern [left ∈ {00,96,67}] + 86 + [follower ∈ {50,01,52,56,66}]
occurs EXACTLY 9 times — precisely the subset, no more, no fewer — while
determiner-left windows (left ∈ {87,11,47}: #0, #6, #24) never take those
followers. This left-frame split is exceptionless and stated as a
byte-level fact; it predicts any future 'le'-life window of 86 will have a
non-determiner left. Deeper re-segmentation of #0/#6/#24 is owned by
reseg-86-problem-windows (queued) — cited, not duplicated. Clause 2:
FENCED (pass by fence).

## Per-clause verdicts

- Clause 1: FAIL (strict). 8/9 parse; #16's "par pour" L2 defect is real
  under granted values, though orthogonal to 86 (it discriminates
  nothing about 86's value — it breaks under every 86 value).
- Clause 2: PASS BY FENCE (re-segmentation not demonstrable; fence
  grounded in the exceptionless left-frame distributional split).

Adverses: honored — the global 'le' kill (#0, #6 at kill grade) was not
re-litigated; this battery stayed subset-scoped throughout.

## Verdict: NULL

The bar's promote condition ("all nine ... parse") is not met because of
#16's orthogonal "par pour" defect. This is NOT a kill: no subset window
forces 86≠'le' — the defect discriminates nothing about 86, and the
remaining 8/9 windows parse cleanly under 'le' with independently
nominal followers (50/01/52/66 strong, 56 weak-positive). The subset is
distributionally coherent (exceptionless left-frame split). The 'le'-life
of 86 survives as a battery-level lead; the single exception needs its own
adjudication.

## Follow-up targets (null regenerates work)

1. `par-pour-962-adjudicate` (priority 2): adjudicate the "96 00"
   adjacency @960-961 ("et par pour le [56] ..."). Bar: under granted
   96=par / 00=pour, state whether any rescue parses (ellipsis,
   re-segmentation, 96/00 re-value with red-team polyvalence declaration);
   kill each rescue or fence the adjacency with cause. This is the gate
   for the subset re-run.
2. `le-86-subset-rerun` (priority 3, CONDITIONAL on #1): re-run Clause 1 of
   this battery iff par-pour-962-adjudicate resolves #16's L2 in favor of
   the determiner frame. Bar: the nine windows as listed here; promote iff
   all nine parse.
3. Coordinate note (not a new target): reseg-86-problem-windows (queued)
   owns deeper re-segmentation of #0/#6/#24; homophone-86-split already
   returned null — its positional-split framing is not re-proposed here.

R5005, sealed gate instances, and the red-team adjudication queue were not
touched. No standing verdict contradicted or downgraded. 86 polyvalence
NOT declared.
