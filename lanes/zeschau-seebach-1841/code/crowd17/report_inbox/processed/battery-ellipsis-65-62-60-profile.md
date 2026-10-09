# Battery report: ellipsis-65-62-60-profile

Target: `ellipsis-65-62-60-profile`. Worker: battery worker
(16de7db5-38be-49b8-98ba-b2af11050ede, supervisor-dispatched).
Date: 2026-10-08. Stream: repaired 1,847-pair parse
(`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`),
tokenization replicated from `code/side-keyhunt/repair_parse.py`
(upstream byte-exact `[s[i:i+2] for i in range(o, len(s)-1, 2)]`).
Verified in-work: 1,847 pairs, 96 unique groups. `canonical.py` never used.
R5005 untouched. No invented data; every count below re-derived on the
repaired stream. @-offsets are 0-indexed pair positions.
Lock `code/crowd17/next-token/locks/ellipsis-65-62-60-profile.lock`
created on start (no stale lock existed), deleted on completion.

## Bar (verbatim from battery-queue.json — pre-registered BEFORE testing)

"promote the 'pas de [X]' ellipsis leg iff >=2 of the three profile
noun-shaped (determiner/article contact, adjective followers) with the
third fenced with stated cause"

## Bar as numbered pass/fail clauses (frozen from the bar before testing; not modified after seeing data)

- **C1:** 65 (@1251 window's X) profiles noun-shaped — determiner/article
  contact and adjective followers on the repaired stream.
- **C2:** 62 (@1327 window's X) profiles noun-shaped — determiner/article
  contact and adjective followers on the repaired stream.
- **C3:** 60 (@1561/@1733 windows' X) profiles noun-shaped —
  determiner/article contact and adjective followers on the repaired stream.
- **Promote** the 'pas de [X]' ellipsis leg iff >=2 of C1–C3 pass, with
  the failing clause fenced with stated cause.

Standing values used (protocol §7 only): banked 11=la, 70=pre, 82=m,
34=i, 29=er, 40=e, 46=que; granted 87=ce, 64=qui, 96=par, 17=fois,
79=tout, 00=pour, 84=on, 47=ce; provisional 59=est, 77=le;
battery-promoted 94=ne, 12=n, 48=e, 06=ent. 67 positional rule untouched.
Standing verdicts respected, none re-litigated: prof-65 (65=noun-class,
PROMOTE), noun-60 (60 masculine-noun value, KILL), adj-60 (60
masculine-adjective single-value, KILL), frame-20-62-94 (NULL, 62's class
open). No red-team verdict on 60/62/65 exists to contradict.

## Method

Replicated `repair_parse.py` tokenization inline. Contact censuses for
65 (n=25), 62 (n=35), 60 (n=18): full left-neighbor and right-neighbor
distributions; article/determiner contact against standing set
{11=la, 77=le (provisional), 87=ce, 47=ce} plus 79=tout (A5 granted,
determiner-shaped); adjective-follower check against every standing
adjective-class value in the lane. Confirmed the four '30 06' windows are
exactly @1251/@1327/@1561/@1733 stream-wide (no others).

Coordination (§7, per brief): spell-pasent-test (queued) owns the
clerk-'passent' spelling hypothesis — not tested here. The @1733 fragment
parse is owned by sibling worker noun26-1560-1733-fragment (its lock was
live during this run) — this battery profiles 60 stream-wide and does not
depend on the sibling's result. The '30 06' windows' 06 is taken as
standing (06='ent', battery-promoted); the de/ne readings of 06 were
settled NULL by noun26-1560-06-value and are not re-litigated.

## Window-level evidence (@-offsets, all re-derived)

The four windows (X = right-neighbor of 06):
- @1251: `30 06 65 46` (a7_02) — X=65, followed by 46=que.
- @1327: `30 06 62 94` (a7_04) — X=62, followed by 94=ne.
- @1561: `30 06 60 71` (a8_01) — X=60.
- @1733: `30 06 60 12` (a8_07) — X=60.

### 65 (n=25) — contact census

- Article contact {11,77,87,47}: **0/25** preceded, **0/25** followed.
- Determiner contact via 79='tout': **1/25** — @1683
  `77 44 00 46 79 65 13 93 62 94 79` = "...que[46] tout[79] [65] 13..."
  ("que tout [65]"): with 65's verb rival killed at kill grade (prof-65),
  'tout' here is determiner-shaped ("tout + noun"), not pronominal.
- Adjective followers: none identifiable on standing values. 65's
  followers: 63 x4 (verb-shaped per prof-65 L6), 23 x3, 13 x3, 64=qui x3,
  94=ne x2, 16, 88, 84=on, 14, 71, 38, 46=que, 68, 48, 34. No follower
  carries a standing adjective value.
- Standing: 65 = noun-class, PROMOTED (prof-65, 6 frame-legs:
  qui-relative head x3 @724/@1208/@1340, que-relative head @1253,
  post-finite-verb direct object x2, post-"-ere" slot x3, post-verb,
  subject-NP member x2). Not re-derived, not downgraded.

### 62 (n=35) — contact census

- Article contact {11,77,87,47}: **1/35** — @508
  `68 21 67 77 62 94 64 98 65` = "...21 67 le[77] [62] ne[94] qui[64]..."
  AMBIGUOUS: 'le' may be the object pronoun (not the article), and the
  article+noun parse strands on "ne qui" ('ne' requires a verb;
  64=qui granted is not one). Not a clean article contact.
- Determiner contact via 79='tout': 0/35.
- Adjective followers: none on standing values. 62's followers: 94=ne x9,
  48=e(letter) x6, 98 x5, 16 x4, 61 x2, 06 x2, 96=par, 91, 21, 18, 38,
  46=que, 93. (Note @46/@945 '62 96' = "62 par" — preposition follower,
  not adjective.)
- Noun diagnostics found (supporting, below promote grade):
  - Subject + "ne" + verb: '62 94' x9. Clean instances: @761
    `82 34 29 40 20 62 94 59 39` = "...[20] [62] ne[94] est[59]..."
    ("62 n'est", 59=est provisional); @1772
    `87 64 26 37 78 62 94 24 87` = "...78 [62] ne[94] 24..."
    ("62 ne [verb]", 24 granted finite verb); @1329
    `98 56 30 06 62 94 70 52` = "[62] ne[94] pre[70]..." ("ne pre[nd]",
    the '30 06' window itself). Looser: @100 "62 ne 93 est", @840
    "62 ne [26]" (26's branch open).
  - que-relative head x1: @1482 `33 29 82 16 98 62 46 77 84` =
    "...98 [62] que[46] le[77]..." ("the 62 that...").
  - No verb-slot hits: 62 never follows 94='ne' or 64='qui' (no
    "qui 62" / "ne 62" anywhere in 35 windows).
- Standing: 62's class OPEN (frame-20-62-94 NULL). This battery adds two
  noun frame-legs (subject+ne+verb, que-relative head) — below the lane's
  ≥3-leg standard for class assignment (prof-65's bar).

### 60 (n=18) — contact census

- Article contact {11,77,87,47}: **1/18** — @454
  `59 32 48 79 17 77 60 65 13` = "...tout[79] fois[17] le[77] [60] [65]..."
  ("le [60] [65]"). This is the frame both killed batteries fought over:
  coheres under the killed 60=noun ("le [60-N] [65-adj]" — needs
  unattested 65=adjectival) and under the killed 60=adjective
  ("le [60-adj] [65-N]" — clean, but killed as a single-value claim by
  the verbal windows).
- Determiner contact via 79='tout': 0/18.
- Adjective followers: none; followers include noun-shaped 03 x4
  ('60 03' x4 @690/@1644/@1674 + @995-adjacent; 03 nominal on 'le [03]'
  @722 / 'ce [03]' @1014/@1790 — under the killed claims this was
  "[60-adj] [03-N]"). Other followers: 08 x2, 71 x2, 67 x2, 12 x2,
  90, 09, 15, 65, 06, 27.
- Standing, fenced: noun-60 KILL (masculine-noun value; kill-grade
  windows @1338 "qui[64] [60]" and @700 "ne[94] [60]" force 60 into
  verb-only slots) + adj-60 KILL (masculine-adjective as single-value
  claim; same two verbal windows). verb-60 NULL (six verbal windows,
  unresolved). poly-60-redteam QUEUED — adjective-vs-verb is a live
  second-polyvalence question only the red team may declare (§7). **No
  noun value for 60 is available at battery level.**

### The adjective-follower prong is untestable at battery level

No adjective class or value is granted or promoted lane-wide.
est-59-frames (promote) covers 30/39/37 as *predicative* adjectives after
"n'est" only — none of {30,39,37} follows 65/62/60 anywhere.
val-42-nominal (promote) is a unified nominal class, not adjective-specific.
adj-frames-995-637 (null), det-adj-80-adjudicate (null), adj-32 (null)
establish no standing adjective value. Per protocol §2 this is recorded
as a finding: the bar's adjective-follower prong cannot discriminate on
standing values. It is not silently rewritten — it is reported absent.

## Per-clause pass/fail

- **C1 (65): PASS** — noun-shaped on standing verdict (prof-65 PROMOTE,
  not re-litigated; §5 forbids downgrading). Measured prongs: article
  contact 0/25 with {11,77,87,47}; sole determiner contact 'tout' @1683;
  no adjective followers on standing values. 65's nounhood rests on
  relative-head and direct-object diagnostics, not on the bar's two
  prongs — recorded, not hidden.
- **C2 (62): FAIL (inconclusive, not kill-grade)** — article contact
  1/35 and ambiguous (@508 'le 62', "ne qui" strands the article parse);
  no adjective followers; two noun frame-legs (subject+"ne"+verb with
  clean @761/@1772/@1329, que-relative head @1482) below the lane's ≥3-leg
  class standard; no verb-slot hits either. Class remains open, as
  frame-20-62-94 already held. 62 does not profile noun-shaped at battery
  grade.
- **C3 (60): FAIL — fenced with stated cause** — the single article
  contact (@454 'le 60') sits on a twice-killed nominal: noun-60 KILL and
  adj-60 KILL (single-value), with kill-grade verbal windows @1338
  ('qui 60') and @700 ('ne 60'); verb-60 NULL; poly-60-redteam queued for
  red-team ruling. No noun value for 60 exists at battery level, so the
  'pas de [60]' instances at @1561/@1733 cannot take a nominal X now.
- **Promote condition (>=2 pass): NOT MET** — 1 pass (65), 1
  inconclusive (62), 1 fenced (60).

## Adverses (answered, none ignored)

(a) "the ellipsis matrix itself is invented ('pas de [X]' needs an elided
matrix)": NOT ANSWERED — stands as the parent residual. This battery
tested only the X-side (noun-shapedness), per its bar; the matrix remains
unlicensed. Promoting the leg was conditional on the bar, which failed —
so the matrix question is untouched, not smuggled in.
(b) "coordinate with queued spell-pasent-test and
noun26-1560-1733-fragment, do not duplicate": ANSWERED — the
clerk-'passent' spelling hypothesis was not tested; the @1733 fragment
parse was not touched (sibling worker's lock live during this run; 60
profiled stream-wide only, no dependence on its result).

## Verdict: NULL

Headline: 65 is noun-shaped on standing verdict (prof-65) but shows zero
article contact in 25 windows; 62's profile is suggestive
(subject+"ne"+verb x9, que-relative head x1) yet below promote grade with
only one ambiguous article contact (@508) and no adjective followers;
60 — the X at two of the four windows (@1561/@1733) — is fenced with
stated cause (noun-60 KILL + adj-60 KILL, red-team polyvalence pending),
leaving 'pas de [60]' without a nominal X at battery level. The bar's
>=2 condition fails (1 pass / 1 inconclusive / 1 fenced), and its
adjective-follower prong is untestable on standing values (§2 finding).
The 'pas de [X]' ellipsis leg is neither promoted nor killed: it holds
in shape at @1251 (65 noun, "pas de [65] que"), is open at @1327 (62),
and is fenced at @1561/@1733 (60). No standing verdict contradicted;
nothing downgraded.

## Follow-up targets (null-regeneration; for the supervisor to queue)

1. **adj-groundwork-refollower** (priority 2): establish a standing
   adjective value/class (e.g. test whether est-59-frames' predicative
   30/39/37 extend to postnominal attributive use, or via det-adj-80),
   then re-census followers of 65/62/60 for adjective followers.
   Bar: name >=1 adjective value with >=2 independent legs, then re-test
   the adjective-follower prong of C1–C3. Adverses: predicative !=
   attributive — do not re-litigate est-59-frames; do not invent values.
   Evidence: this report (prong untestable, §2 finding).
2. **62-third-leg** (priority 2): give 62 its third noun frame-leg
   (subject+"ne"+verb @761/@1772/@1329 and que-relative head @1482
   already held) — seek a clean article/determiner contact or a
   direct-object slot — to promote 62's noun class at the lane's >=3-leg
   standard; then re-test 'pas de [62]' @1327. Bar: promote 62=noun-class
   iff >=3 independent frame-legs. Adverses: coordinate with
   frame-20-62-94 (do not re-litigate 20's noun-leg); 62's zero verb-slot
   hits ('qui 62'/'ne 62' x0 in 35 windows) is supporting, not a leg.
   Evidence: this report's 62 census.
3. **pasde60-redteam-gate** (priority 3): once the red team rules on
   poly-60-redteam, resolve the @1561/@1733 'pas de [60]' windows under
   the ruled value — fence both as non-elliptical with stated cause if 60
   lands non-nominal, or re-test the ellipsis leg if nominal. Bar:
   resolve iff both windows parse under the ruled value or are fenced.
   Adverses: do not preempt the red team; read (do not duplicate)
   noun26-1560-1733-fragment's report on @1733. Evidence: noun-60 KILL +
   adj-60 KILL + this report's 60 census.

## Standing constraints observed

- §7 respected: standing values only; 67 sole-polyvalence untouched;
  prof-65 / noun-60 / adj-60 / frame-20-62-94 verdicts respected, none
  downgraded; R5005, sealed gates, and red-team queue untouched; no
  second polyvalence declared.
- No invented numbers: every count re-derived above on the repaired
  1,847-pair parse.
