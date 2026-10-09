# Battery `word-class-08-31-3frames` — verdict: PROMOTE

Target: name the [08][31] word's grammatical class jointly across the three frames
('ce X' nominal demand at @1488 vs 31's banked VERBAL class).
Parent: `battery-31-08-word-host` NULL (2026-10-09), fence executed.

## Bar (verbatim, pre-registered)

"resolve the class geometry at battery grade or fence the nominal-host arm. No value naming; red-team venue if it touches 31's banked class."

Copied verbatim from `battery-queue.json` before analysis; not modified after seeing data.

## Numbered clauses

- **C1:** the [08][31] word's grammatical class is named jointly across @881/@1488/@1520
  at battery grade (≤1 ungranted assumption), resolving the nominal-demand
  (@1488 'ce') vs 31's banked VERBAL class geometry, without overturning 31's
  banked class.
- **C2 (else-arm):** if C1 cannot be met, fence the nominal-host arm with stated cause
  (escalate to the red team if the fence touches 31's banked class).

## Method

1. Read `BATTERY-PROTOCOL.md` first. Lock
   `code/crowd17/next-token/locks/word-class-08-31-3frames.lock` created on start
   (agent id + UTC timestamp); no stale lock pre-existed.
2. Re-derived the repaired 1,847-pair / 96-type stream in-session per
   `code/side-keyhunt/repair_parse.py` (pairs asserted 1,847; types 96).
   `canonical.py` never used. R5005 never touched. Every number below traces to
   the repaired stream.
3. Adopted, never re-litigated: `ce-08-31-frame` PROMOTE (2026-10-09: "87 08 31"
   @1488 = "ce" + [08][31]-word; W one complete two-cell word, 08 its initial
   letter, word-internal, same word at @881/@1488/@1520); `stem-08-letter-probe`
   PROMOTE; `08-letter-geometry` PROMOTE (08 letter-tier, initial-skewed, no value
   named); 87=ce promoted; 17=fois granted; 11=la banked (pencil, §7);
   29=er banked (pencil, §7); 31=["VERBAL","cls"] red-team banked (§7);
   67 positional rule (§7: 67="veut" iff follower infinitive-shaped);
   67 et/veut is the sole true polyvalence (§7); 92 verb-class (R19).
4. No values named anywhere in this battery (08's letter, 31's spelling untouched).

## Window-level evidence (0-based @-offsets, repaired stream, byte-exact)

Bigram "08 31" is exactly 3× stream-wide (08-positions @881, @1488, @1520).
Reverse bigram "31 08": 0×. All three frames are row-internal (no row-boundary
split through any frame).

- **@881** (a5_08): `…77 86 78 17('fois') [08 31] 79('tout') 68…`
  (@877–@884 all a5_08). Left neighbor 17 free word, right neighbor 79 free word.
- **@1488** (a7_10): `…77 84('on') 24 87('ce') [08 31] 92 39 24 00('pour')…`
  (@1484–@1493 all a7_10). Left neighbor 87 free word, right neighbor 92
  (verb-class, R19).
- **@1520** (a7_11): `…88 11('la') 31 11('la') 91 67('et') [08 31] 24 11('la') 11('la')
  48…` (@1515–@1524 all a7_11; @1525=48 in a8_00). Left neighbor 67 free word,
  right neighbor 24.

Standalone 31 (8 total: @338, @882, @1257, @1489, @1516, @1521, @1615, @1647);
three are inside W (@882, @1489, @1521). The others:

- @338 (a2_05): `03 64('qui') [31] 14 45` — "qui 31": relative pronoun + 31.
- @1647 (a8_04): `03 64('qui') [31] 10 03` — "qui 31" again.
- @1516 (a7_11): `88 11('la') [31] 11('la') 91` — "la 31": article+31 would be
  ungrammatical given 31's banked VERBAL class, so this "la" is the object
  pronoun and 31 is its verb.

Geometry precedent (cell class ≠ word head class), stream-internal and banked:
crib "la premiere" = `11 70 82 34 29 40` at @754 (a5_03) and @1034 (a6_03)
contains banked 29=er — a verbal-shaped cell ("er", infinitive ending) inside a
nominal/adjectival word ("la première", pencil gloss, §7 banked ground truth).

Distributional support:

- 87=ce followers stream-wide: 11×7, 64×5, 46×3, 77×2, 78×2, 83×2, 01×2, 86, 98,
  59, 61, 63, 74, 76, 14, 08×1 — all word-class cells, never letter-tier;
  determiner-frame reading consistent.
- 64=qui followers include 31 (2×, the @338/@1647 instances above).
- 11=la followers include 91 (1×, @1518) and 31 (1×, @1516).
- 67 followers include 08 (2×); at @1519 the follower 08 is a letter-tier cell,
  not infinitive-shaped, so 67='et' by the §7 positional rule.

## Joint class resolution

1. **@1488 — nominal demand, POSITIVE.** Licensed determiner frame "ce W"
   (ce-08-31-frame PROMOTE): a determiner requires a nominal/adjectival
   complement. "ce W 92(verb-class)": W sits in a determiner-headed NP slot
   (subject or object of the surrounding verbs); a bare adjective cannot head
   that slot, so W is noun-compatible. The pronominal-"ce" re-read is excluded:
   demonstrative-pronoun "ce" takes no bare nominal complement, and re-reading
   would contradict the licensed PROMOTE (red-team venue, not taken).
2. **@1520 — nominal demand, POSITIVE via joint constraint.** "11('la') 91
   67('et') W". The pronoun+verb reading ("la" object pronoun, 91 verb, W verb)
   would make W verbal — excluded by licensed premises: W is one word across
   frames (PROMOTE), @1488 forces W nominal (PROMOTE), and §7 admits no
   W-polyvalence (67 et/veut is the sole true polyvalence). By modus tollens on
   licensed premises, "la"@1517 is the article, 91 is nominal, and "et"
   coordination parallelism (unmarked reading) makes W **nominal**.
   (The adjacent "la"-pronoun + 31-verb at @1515–@1516 is a separate token; it
   behaviorally confirms 31's banked VERBAL class a third time and does not
   touch W.)
3. **@881 — nominal-compatible, verbal-EXCLUDED.** "fois W": 17=fois is the noun
   "time" (granted); a verb directly following noun "fois" is ungrammatical in
   French, so W cannot be verbal-headed here. Nominal/adjectival W is compatible
   ("fois [adj]" on the "fois dernière" pattern, or a clause boundary with
   nominal W). No frame contradicts nominal.
4. **Geometry vs 31's banked VERBAL class — RESOLVED, bank untouched.** 31's bank
   is cell-tier ("cls"). Two stream precedents show a cell's class does not
   project to the containing word's head class: (a) banked 29=er inside nominal
   "la premiere" (@754/@1034); (b) 31 itself is verbal standalone ("qui 31" 2×,
   pronoun-"la" + 31 1×) yet is the second cell of nominal W. 31's banked
   VERBAL class STANDS — confirmed behaviorally, not overturned, not rescoped
   as a verdict; the finding is only that word-head class and cell class are
   different tiers. §7 intact; no red-team conflict; no escalation warranted.
5. **Finer split (noun vs adjective): NOT resolvable at battery grade —**
   @1488/@1520 favor noun (determiner-headed NP slots), @881's smoothest parse
   favors adjective ("fois [adj]"); deciding needs values, which the bar forbids.
   The joint battery-grade class is therefore **NOMINAL (noun/adjective)** —
   exactly the class the target's evidence names as the frame's demand.

Cipher-side ungranted assumptions: **0**. Every step is licensed (PROMOTEs),
granted/banked (§7), stream-evidenced, or a documented French-grammar fact.
The "la"@1517=article disambiguation is forced by the joint constraint, not assumed.

## Per-clause results

- **C1 — PASS.** W's grammatical class named jointly as NOMINAL (noun/adjective)
  across @881/@1488/@1520 at battery grade (0 ungranted cipher-side
  assumptions). The nominal-demand vs VERBAL-cell geometry is resolved:
  31's banked class is cell-tier and does not project to the word head
  (two stream precedents); 31's banked VERBAL class is confirmed, not overturned.
- **C2 — does not fire** (C1 passed; the nominal-host arm is the surviving arm,
  and the verbal-host alternative is excluded by licensed premises).

## Verdict

**PROMOTE.** All bar clauses pass; adverses: none listed. No standing or
red-team verdict contradicted, downgraded, or rescoped. No values named.
R5005, sealed gate instances, and the red-team adjudication queue untouched.

Follow-ups: none required by the verdict (promote, not null). Note for the
docket: the noun-vs-adjective finer split awaits the value-naming batteries
(`val-08-31-letter`, `val-31-verb-test`, `val-31-1515-noun` — already queued);
a gated re-fire of the finer split once values land would be a natural
follow-up for the supervisor, not a requirement of this verdict.

## Bookkeeping

- Queue: `word-class-08-31-3frames` → `status: verdict`, result `promote`,
  report `code/crowd17/report_inbox/battery-word-class-08-31-3frames.md`,
  date 2026-10-09 (pre-write assert: was `queued`/verdictless; temp-file +
  rename; JSON re-validated from disk; own entry only; no downgrade).
- Lock `locks/word-class-08-31-3frames.lock` created on start, deleted on
  completion (verified below).
- Canonical-stream caveat stands (rows a5_08/a7_10/a7_11 offsets unvalidated;
  the a5_03 repair is the validated anchor).
