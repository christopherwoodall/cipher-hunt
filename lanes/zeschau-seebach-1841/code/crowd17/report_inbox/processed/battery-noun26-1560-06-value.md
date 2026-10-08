# Battery report: noun26-1560-06-value — 06's class on the '30 06' windows

Target: `noun26-1560-06-value`. Worker: battery worker (supervisor-dispatched).
Date: 2026-10-08. Stream: repaired 1,847-pair parse
(`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`),
parsed with logic replicated from `code/side-keyhunt/repair_parse.py`.
`canonical.py` never used. R5005 untouched. No invented data; every number
below re-derived on the repaired stream. Lock
`code/crowd17/next-token/locks/noun26-1560-06-value.lock` created on start,
deleted on completion.

## Bar (verbatim from battery-queue.json)

"decide 06's class on the four '30 06' windows (@1251/@1327/@1561/@1733) plus
the 06->77 bigram and 06/77 ratio evidence; the named class must resolve the
licensing of the fenced @1561-1563 span ('pas de [60]'-ellipsis vs 'pas. Ne
[clause]')."

## Bar as numbered pass/fail clauses (frozen from the bar before testing; not modified after seeing data)

1. 06's class is DECIDED on the four '30 06' windows (@1251/@1327/@1561/@1733):
   exactly one class of {'de', 'ne', 'other'} is named, with every one of the
   four windows parsing at battery grade under the named class using standing
   values only (no invented values; no un-fenced open-value assumptions).
2. The 06->77 bigram and 06/77 ratio evidence SUPPORT the named class: the
   bigram parses under the named class at a clear majority of its windows,
   and the ratio is consistent with the named class while discriminating
   against the rejected classes at the lane's standard.
3. The named class RESOLVES the licensing of the fenced @1561-1563 span: the
   span parses as 'pas de [60]'-ellipsis (de), 'pas. Ne [clause]' (ne), or a
   stated construction (other), with both 'pas' and 06 constructionally
   licensed — not fenced.

## Method

Replicated `repair_parse.py` tokenization inline (upstream byte-exact
`[s[i:i+2] for i in range(o, len(s)-1, 2)]` with `repaired_offsets.json`).
Verified: 1,847 pairs, 96 unique groups. Located all four '30 06' windows
(30-positions @1251/@1327/@1561/@1733 — exactly 4 stream-wide), the
'30 06 60' x2 (@1561/@1733), full 06 census, 06->77 / 77->06 bigrams, and
n(06)/n(77). Attempted parses of each window under three readings —
E (06='ent', standing per battery-promoted ent-06), D (06='de'),
N (06='ne') — using standing values only: banked 11=la, 70=pre, 82=m,
34=i, 29=er, 40=e, 46=que; granted 87=ce, 64=qui, 96=par, 17=fois,
79=tout, 00=pour, 84=on, 47=ce; provisional 59=est, 77=le;
battery-promoted 94=ne, 12=n, 48=e. ent-06's promote taken as standing —
not re-litigated (adverse). Companion target noun26-1560-1733-fragment
(queued) owns the @1733 letter-foothold — not duplicated here.

## Window-level evidence (@-offsets, all re-derived)

Census: n(06)=44, n(77)=44, n(30)=19. n(06)/n(77) = 1.0 exactly.
06->77 = 6x at 06-positions @6/@206/@789/@890/@967/@1762.
77->06 = 1x at @521 (06 at @522).
CORRECTION to ent-06's successor census: its "77 x7" list
(@6/@206/@522/@789/@890/@967/@1762) mixes one reverse bigram — @522 is
77->06, not 06->77. True forward count is 6.

### The four '30 06' windows (±8 context)

- @1251: `11 00 33 16 00 67 46 26 | 30 06 65 46 01 61 31 29 69 88`
  = "...que [26-verb] pas [06] [65] que..." (@1250 = 26 verb branch;
  '26 30' = "[verb] pas" per R17-011 grant).
- @1327: `24 03 29 80 08 62 98 56 | 30 06 62 94 70 52 39 83 86 71`
  = "...[56] pas [06] [62] ne pre [52]..." (94=ne, 70=pre standing).
- @1561: `99 13 93 61 40 17 11 26 | 30 06 60 71 50 29 24 74 62 48`
  = "...la [26-noun] pas [06] [60] [71] [50] er..." (the fenced span
  @1561-1563 = "30 06 60"; 40=e, 17=fois, 29=er banked/granted).
- @1733: `98 39 88 24 30 15 01 56 | 30 06 60 12 48 52 86 12 34 94`
  = "...[56] pas [06] [60] n e..." (12=n, 48=e letters; double-30
  @1729/@1733 per pas-30 battery).

### Per-reading parse attempts

Reading E — 06='ent' (standing): all four windows = "pas"+"ent" with no
verb stem available (30='pas' is a granted word, not a stem). 0/4 parse.
Consistent with ent-06's own fencing of @1252/@1328/@1562/@1734 as
conditional on an unproven clerk single-consonant spelling ("pasent";
pair-misaligned in any case: "passent" = pa-ss-en-t needs 'ss' at 06,
not 'ent'). No window forces E false; none parses under E.

Reading D — 06='de' ("pas de [X]" ellipsis):
- @1251 "que [26] pas de [65] que": shape-clean; needs an unlicensed
  ellipsis matrix ("[il n'y a]") + 65 noun-shaped (65 open). CONDITIONAL.
- @1327 "pas de [62] ne pre [52]": shape-clean "pas de [62]"; the
  "ne pre" tail is odd. CONDITIONAL.
- @1561 "pas de [60] [71] [50] er": shape-clean; needs matrix + 60 noun
  (60 open). CONDITIONAL.
- @1733 "pas de [60] n e [52]...": shape-clean; needs matrix.
  CONDITIONAL.
0/4 at battery grade. 'de' is shape-compatible everywhere but licensed
nowhere: asserting it would invent the matrix (§3).

Reading N — 06='ne' ("pas. Ne [clause]"):
- @1251 "pas. Ne [65] que": needs 65 verb-shaped + clause boundary.
  CONDITIONAL, plus polyvalence problem (below).
- @1327 "pas. Ne [62] ne pre": HARD FENCE — "Ne [62] ne..." is a double
  'ne', ungrammatical under any reading.
- @1561 "pas. Ne [60]...": needs 60 verb-shaped (60 open). CONDITIONAL.
- @1733 "pas. Ne [60] n e...": needs 60 verb-shaped. CONDITIONAL.
0/4; one hard fence. Naming 'ne' would additionally require a second 06
value alongside battery-promoted 06='ent' — a second polyvalence, which
only the red team may declare per §7 (67 sole true polyvalence;
94='ne' already promoted). Blocked at battery level regardless of parses.

### 06->77 bigram + ratio (clause 2 evidence)

- @6: `51 47 41 06 77 78 18` = "[41] [06] le [78]"
- @206: `92 63 42 06 77 44 50` = "[42] [06] le [44]"
- @789: `74 65 84 06 77 64 46` = "on [06] le qui" (84=on granted, 64=qui granted)
- @890: `02 00 86 06 77 76 01` = "[86] [06] le [76]" (86 INF-class A9)
- @967: `41 19 24 06 77 76 01` = "[24] [06] le [76]"
- @1762: `41 15 93 06 77 84 09` = "[93] [06] le on" (84=on granted)

Under N ("ne le"): @6/@206/@890/@967 conditional (78 verb-shaped?
ver-78 is LEAD-not-settled; 44/76/24 open); @789 FENCED ("on ne le qui");
@1762 FENCED ("ne le on" — 'on' cannot follow "ne le").
Under E ("[X]ent le"): @6 conditional (41 verb-stem? open); @206
conditional/fenced (42 = A1-predicative tension); @789 FENCED
("on ent le qui"); @890 fenced (86 INF-class, not a stem); @967
conditional (24 open); @1762 conditional ("[93]ent l'on" — parses IFF
93 verb-shaped; verb-93 is queued).
Neither reading dominates: both fenced at @789; N loses @1762 outright
while E holds it conditionally. Ratio 1.0 (44/44) is compatible with a
function-word pair ('ne'/'le') and with an ending/article pair alike —
non-discriminating at the lane's standard. The bigram+ratio evidence does
not support a single named class.

## Per-clause pass/fail

- Clause 1 (class decided on the four windows): FAIL for all three
  candidates. E: 0/4 parse (fenced, as ent-06 already recorded). D: 0/4
  at battery grade (shape-clean, license-free). N: 0/4 with a hard fence
  at @1327, and barred by §7 in any case. No class is decided.
- Clause 2 (bigram+ratio support the named class): FAIL as a
  discriminator — no class named; and on the merits neither reading
  dominates the six 06->77 windows (both fenced at @789; E conditional
  at @1762 where N is fenced; ratio 1.0 non-discriminating).
- Clause 3 (named class resolves @1561-1563): FAIL — no class named.
  The span's licensing stays undecided: 'pas de [60]'-ellipsis vs
  'pas. Ne [clause]' vs residual.

## Adverses (answered, none ignored)

(a) "06 value contested (de/ne)": ANSWERED — both tested window by
window. Neither is forced: 'de' is shape-compatible but unlicensed at
all four windows; 'ne' is hard-fenced at @1327 and needs a forbidden
second polyvalence. The contest is not resolved by these windows.
(b) "06's class is ent-06's lane — coordinate, do not re-litigate the
ent-06 promote": ANSWERED — ent-06's promote stands untouched (its
three clean frames "ne mentent" x2 @578/@1182 and "entreprenne" @346
not re-tested; its fencing of the '30 06' windows confirmed, not
revised). This battery tested only the four windows ent-06 itself had
fenced. No standing verdict contradicted, none downgraded.

## Verdict: NULL

Headline: the four '30 06' windows force neither a 'de' nor a 'ne'
reading of 06; under standing 06='ent' they remain fenced (as ent-06
already recorded); the @1561-1563 span stays a residual. The
'pas de [60]'-ellipsis vs 'pas. Ne [clause]' choice is undecidable at
battery level on these windows.

## Follow-up targets (null-regeneration; for the supervisor to queue)

1. ellipsis-65-62-60-profile — bar: profile the right-neighbors 65
   (@1251), 62 (@1327), 60 (@1561/@1733) via contact censuses on the
   repaired stream; promote the 'pas de [X]' ellipsis leg iff >=2 of the
   three profile noun-shaped (determiner/article contact, adjective
   followers) with the third fenced with stated cause. (Tests the 'de'
   shape without assuming the ellipsis matrix.)
2. ne-06-polyvalence-question — red-team adjudication packet: the 06->77
   bigram (6x, re-derived) parses as "ne le" no worse than "[X]ent le"
   (both fenced at @789 "on [06] le qui"; @1762 favors 'ent'
   conditionally via "[93]ent l'on" iff verb-93 lands); crib_surgeon H3's
   ratio+bigram checks for 06='ne' passed pre-ent-06; @1327 hard-fences
   'ne' ("Ne [62] ne"). Question for red team: does 06 get a second
   value ('ne') at any window, or do the '30 06' / 06->77 windows stay
   fenced under single-value 'ent'? Battery may not declare per §7.
3. spell-pasent-test — bar: test ent-06's fenced "clerk-'passent'"
   hypothesis for the four '30 06' windows: census the stream's other
   3pl '-ent' verbs for single-consonant clerk spellings; kill the
   spelling hypothesis iff zero supporting instances stream-wide, which
   hardens the four windows as genuine residuals rather than spelling
   variants.

## Standing constraints observed

- §7 respected: standing values only; 67 sole-polyvalence rule
  untouched — nothing declared; ent-06 not re-litigated; noun-26's
  positional rule used as context only; R5005 untouched; sealed gates
  and red-team queue untouched.
- No invented numbers: every count re-derived above on the repaired
  1,847-pair parse.
