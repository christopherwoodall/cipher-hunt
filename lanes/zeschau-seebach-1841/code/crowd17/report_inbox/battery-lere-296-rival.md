# Battery report: lere-296-rival

Target: lere-296-rival | priority 3
Claim: the standing 'l'ere' rival read of 11-78-40 @296 is tested directly
Worker: f9e8aaf1-e8f3-4779-8f70-3587ad48e32e | 2026-10-09

## Bar (verbatim, pre-registered)

"(a) name the word 78-40 completes (coordinate with noun/adjective batteries; 'la [X]ère'-shaped candidates); (b) or kill the rival at kill grade with the window re-parsed under 78='ver'"

## Bar restated (numbered pass/fail clauses; frozen before testing)

1. (a) Name ONE French word X = 78-40, 'la [X]ère'-shaped, forced at
   battery grade (coordinated with the noun/adjective batteries).
2. (b) OR kill the rival at kill grade, with the window re-parsed
   under 78='ver' (standing LEAD, R16-005/R17-006).

## Method

Read BATTERY-PROTOCOL.md first. Created `locks/lere-296-rival.lock` on
start. Re-derived the repaired stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed exactly like `code/side-keyhunt/repair_parse.py` (stride-2 pairing
per row offset). Verified: 1,847 pairs, 96 distinct groups.
`canonical.py` never used. R5005, sealed gates, red-team queue untouched.
@-offsets are 0-based stream indices (queue convention).

## Window-level evidence

78-40 occurs exactly 3x stream-wide (0-based index of 78):

- @297 (row a2_04, offset 0):
  `29 40 65 16 01 [11@296] [78@297] [40@298] 97@299 86@300 91 18 89 88`
  = "...01 la [78] e [97] [86]..."
- @352 (row a2_06, offset 0):
  `06 70 12 94 [74@350] [67@351] [78@352] [40@353] 92@354 98@355 ...`
  = "...74 [67] [78] e [92] [98]..."
- @819 (row a5_05, offset 1):
  `14 29 49 [74@816] [74@817] [47@818] [78@819] [40@820] 95@821 13 24 ...`
  = "...74 [47] [78] e [95] [13]..."

n(78) = 31. Standing values used as premises only: 11='la' (banked GT,
pencil), 40='e' (banked GT), 47='ce' (A4 granted, allophone tier),
78='ver' LEAD (R16-005/R17-006), 67 et/veut positional rule (§7).

The rival: @296/297 reads "la 78 e" as 'l'ere'-shaped — i.e. 78-40 is
one French word ending "-ère" ("la mère"/"la terre"-shaped, or "l'ère").
It "votes 'er'" (battery-ver-78.md): it agrees 78 contains "er" but
gives 78 a different value ("èr"/"Xèr") than the 'ver' LEAD.

### Clause (a): naming test

Candidate inventory for "la [X]ère" at @297 (feminine "-ère" words):
mère, terre, guerre, bière, fièvre, lèvre, lumière, matière, manière,
poussière, rivière, bannière, frontière, misère, prière, vipère,
fougère, bruyère, chaudière, litière, civière, salière, l'ère, ...
No battery-grade discriminator exists among them: 01, 97, 86 are all
open at @297, and nothing in the window selects one candidate.
Naming one would be a guess, not a forced value.

Worse, no UNIFORM word can cover all three 78-40 windows:

- @297 forces X feminine: 11='la' is banked GT. "la" + masculine noun
  is ungrammatical in 1841 French.
- @819 forces X masculine-or-nothing: 47='ce' is A4-granted. "ce" +
  feminine noun is ungrammatical under BOTH "ce" readings (as
  determiner it needs a masculine singular noun; as a pronoun it takes
  no bare noun at all).
- No French "-ère" spelling is both feminine and masculine. Nouns are
  gendered ("la mère" vs "le père" are different words). Adjectives
  agree in gender; the few epicene-spelling "-ère" adjectives
  ("sévère", "austère") cannot stand bare ("la sévère", "ce sévère"
  are ungrammatical without a head noun).
- @352 kills noun-X independently: 67='et' here (follower 78 is not
  infinitive-shaped under any live reading, so the positional rule
  gives "et"; and "veut" + bare noun is equally ungrammatical).
  "et [Xère]" with a bare feminine noun is ungrammatical — no
  determiner is present.

Therefore no single French word X satisfies @297 + @352 + @819.
Clause (a) FAILS (unnameable; uniformity impossible).

Coordination with noun/adjective batteries: battery-adj-78-fence
(NULL, 2026-10-08/09) already closed the adjective frame at @297
("Not an adjective frame"); battery-ver78-la78-census (NULL). The
noun reading of 78 is the standing 'ver' LEAD. Nothing here
contradicts those batteries.

### Clause (b): kill at kill grade

Re-parse the window under 78='ver' (standing LEAD, per the adverses):

`11 78 40 97 86` = "la" + "ver" + "e" + [97] + [86].

The rival ESSENTIALLY requires 78-40 to compose as one "-ère" word.
Under 78='ver', 78-40 = "vere", which is not a French word.
battery-ver78-296-reparse (NULL) ran the full one-word lexical sweep:
the only completions ("lavèrent", "véreux"/"véreuse") demand 97/86
values their own contact profiles reject at frame level, and
"la véreuse" is two words and noun-less. Adopted as premise, not
re-litigated. So under the standing 78='ver', the window CANNOT
realize the rival's one-word requirement.

The rival can only survive with 78 = "èr"/"Xèr" (a different value
from "ver"). That is a second 78 value. §7: 67 et/veut is the sole
true polyvalence; the battery cannot declare a second. And 78="èr"/
"Xèr" is independently impossible under uniform 78:

- It is ungrammatical at @352 ("et/veut [Xère]" bare) and @819
  ("ce [Xère]" feminine), shown above at kill grade.
- The "l'ère" sub-variant (78="èr", vowel-initial) is additionally
  killed by elision evidence: six "77 78" windows (@8/@214/@648/
  @1078/@1181/@1352) write "77 78" unelided. "le" + vowel-initial
  word obligatorily elides to "l'" in 1841 French, and this cipher
  writes elision elsewhere (82='m' banked). A vowel-initial 78 would
  force "l'78" at all six windows; the bytes show "77 78". (Caveat:
  77='le' is provisional — supporting argument, not the primary kill.)

The only escape is 78-polyvalence ("èr"/"Xèr" at @297, "ver"
elsewhere). That is a red-team act under §7, not a battery-grade
reading. At battery grade, with uniform 78, the rival is DEAD.

Clause (b) PASSES at kill grade.

### Phase caveat (stated, not hidden)

All three 78-40 bigrams are phase-fragile: under each row's rival
offset (a2_04 0->1, a2_06 0->1, a5_05 1->0) the 78-40 bigram vanishes
from that row (zero novel groups; legal re-parses). They are
canonical-offset objects, like seg-a1_01/reseg-1481-98/frame-43-21-43-
doublet. Per protocol the kill is tested on the repaired stream; the
canonicality caveat stands. Note this caveat does NOT rescue the
rival: under rival offsets the rival's own locus dissolves too.

## Per-clause pass/fail

1. (a) FAIL — no forced naming exists (dozens of "-ère" candidates at
   @297, no discriminator; no uniform word covers @297/@352/@819).
2. (b) PASS at kill grade — the rival is dead: under 78='ver' the
   window cannot realize its one-word requirement, and its required
   78-value ("èr"/"Xèr") is ungrammatical at @352/@819 under §7
   uniformity. Survival needs red-team 78-polyvalence.

## Verdict: KILL

The standing 'l'ere' rival read of 11-78-40 @296 is killed at battery
grade.

## Standing state

- 78='ver' LEAD stands (R16-005/R17-006) — untouched, used as the
  re-parse basis per the adverses. Nothing downgraded.
- R16-005 fence RESPECTED: @296 remains the red-team-fenced 1-window
  residual. Only the fence REASON updates: it is fenced for lack of a
  licensed 97/86 completion (battery-ver78-296-reparse), no longer for
  the 'l'ere' rival.
- 78='er' kill (R17-014) untouched. §7 intact (no polyvalence
  declared; the polyvalence escape is flagged as red-team territory).
- No red-team verdict contradicted. No values named.

## Adverses answered

- "78='ver' LEAD stands (R16-005/R17-006)": honored — the kill is
  built on it, not against it.
- "R16-005 fence respected": honored — the window stays fenced; the
  rival no longer stands as the fence reason.

## Follow-ups (optional; kill ends the line)

1. `rere-296-residual` (P4) — re-examine @296's fence reason
   post-rival: the residual now rests solely on 97/86 lacking
   battery values (gated on frame-97-profile + stem-86).
2. Red-team note: reviving the rival requires a §7 polyvalence
   declaration for 78 ("èr"/"Xèr" at @297 vs "ver" elsewhere) —
   red-team act, not battery work.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-lere-296-rival.md` (this file)
- Queue: `battery-queue.json` `lere-296-rival` -> status `verdict`,
  result `kill`, 2026-10-09 (temp-file + rename; pre-write assert
  passed: status was `queued`; JSON re-validated post-write)
- Lock `locks/lere-296-rival.lock` created on start, deleted on completion
- Stream re-derived in-session: 1,847 pairs / 96 types verified
- `canonical.py` never used; R5005, sealed gates, red-team queue untouched
