# Battery verdict: prof-65

- Target: `prof-65`
- Claim: "65 full profile"
- Date: 2026-10-08
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`). `canonical.py` not used. All counts re-derived in-work. @-offsets are 0-indexed token positions.

## Bar (verbatim from battery-queue.json)

"profile iff class assigned (noun? verb?) with >=3 frame-legs"

Restated as numbered pass/fail clauses (pre-registered before testing):

- **C1:** A word class (noun or verb) is assigned to 65.
- **C2:** The assignment rests on >=3 independent frame-legs (distinct distributional frames, each with window evidence at @-offsets).

Listed adverses: none.

## Method

Parsed the repaired stream (1,847 pairs, 25 tokens of 65). Census of preceders/followers of 65; verified each finder evidence claim byte-by-byte; tested noun vs verb class against French grammar (1841 diplomatic French); checked the report inbox for standing verdicts touching 65.

## Evidence verification (finder's claims, re-derived)

1. `'e 65 94' x2 byte-identical exclusive` — **CONFIRMED.** `40 65 94` x2 (@687, @1712); `48 65 94` x0, so "e" = 40=e (ground truth). Both extend to byte-identical `29 40 65 94` x2. Exclusive: 94 follows 65 nowhere else (65-followers: 94 x2, both in these windows).
2. `'65 qui' x3` — **CONFIRMED.** `65 64` x3 (@724, @1208, @1340); 64=qui granted.
3. `'21 65' x4` — **CONFIRMED** (@135, @372, @1208, @1530). (Worker note: an early manual count said x5; the byte census gives x4 — @138's 65 is preceded by 91, not 21. Finder's count was right.)
4. `dominates '-ere' followers (3/9)` — **CONFIRMED.** `29 40` occurs x9; followers: 65 x3, six others x1 each. 65 is the modal follower (3/9, 3x any rival).
5. `'29-40-65' x3 '[X]ere [65]' direct-object slot` — **CONFIRMED** (@293, @687, @1712). 29=er, 40=e ground truth, so `[X]ere` = word ending "-ere" (cf. `11 70 82 34 29 40` = "la premiere").

## Frame legs for 65 = NOUN

- **L1 — qui-relative head x3.** @724 (`91 65 64 11 00`: "65 qui la pour..."), @1208 (`21 65 64 59 32`: "65 qui est 32" — textbook, 59=est provisional), @1340 (`08 65 64 52 38`: "65 qui 52 38"). A verb cannot antecede "qui" (64=qui granted); the head must be nominal.
- **L2 — que-relative head x1.** @1253 (`06 65 46 01`: "65 que 01" — object relative, "the 65 that..."; 46=que ground truth).
- **L3 — post-finite-verb direct object x2.** @811 (`...12 48 24 65 14...`: "ne [24] [65]" — 12=n, 48=e banked, 24=finite verb granted; negated verb + object slot), @1382 (`13 24 65 68`: verb + 65 + 68).
- **L4 — post-"-ere" slot x3** (@293, @687, @1712; see evidence item 5).
- **L5 — post-verb x1.** @511 (`98 65 88`; 98="vient" is a battery-level lead pending red-team ratification, so this leg is supporting only).
- **L6 — subject-NP member x2.** `21 65 63` x2 byte-adjacent (@371, @1529). 63 is verb-shaped: `63 00` ("63 pour", 00=pour granted A9) x4 of 12 tokens, plus `12 63` ("n 63") x1 — verb taking pour-complements. So "21 65" is the subject NP (noun-noun apposition/compound) and 63 the verb. This turns the NN-adjacency adverse into a supporting leg.

## The verb rival is killed at kill grade

`65=verb` is forced false by L1: @1208 (`21 65 64 59 32`) — under verb-65, "qui" (granted) would follow a finite verb with no nominal antecedent, ungrammatical in French at any period; @724 and @1340 corroborate independently. Note: battery-suite-21-qui-que called @1207 "grammatical under verb-65" ("suite [65-verb] qui est [32]" with the relative attaching across the verb to "suite") — that parse is ungrammatical: a "qui"-relative cannot skip an intervening finite verb to reach a distant antecedent. The kill stands on grammar, not on values.

## Adverses

None listed. Self-found adverse: `21 65` x4 noun-noun stacking — **ANSWERED** by L6 (2 of 4 windows have verb-shaped 63 after, making "21 65" a subject NP) and by NN apposition/compounds, which occur in diplomatic French (titles, proper names); not kill grade against noun-65. @135/@138 (`64 21 65 23 ...`, "qui 21 65 23"): parses as "qui [NP: 21 65] [VP: 23]" with 23 in the relative's verb slot (23's class unassigned — provisional re-parse, fenced).

Fenced with stated cause: @293's internal segmentation (`09 64 29 40 65`: the qui-relative's verb is unidentified — concerns 29/40, not 65's class); the `65 94 29` sequence in the `29 40 65 94` windows ("ne er" unparsed under the 94="ne" lead — the 12/94 duality is unresolved lane-wide; does not affect 65's class).

## Per-clause pass/fail

- **C1:** PASS — class assigned: 65 = NOUN.
- **C2:** PASS — 6 independent frame-legs (L1–L6), each with @-offset window evidence; well above the >=3 bar.

## Verdict: PROMOTE

65 = **noun-class**. The verb rival is killed at kill grade (L1, three windows). No listed adverses; the self-found NN adverse is answered. No standing verdict is overwritten (no prior class verdict on 65 exists; the suite-21-qui-que kill was value-grade on 21="suite" and explicitly fenced 21's noun class).

## Cross-battery interaction (recorded, not hidden)

battery-suite-21-qui-que (verdict: kill on 21="suite" VALUE) escalation #2 set a conditional: "if 65=noun, @1529 joins @134 as a second contradiction against ANY bare-noun value at 21." That consequence assumed no verb in @1529's window. This battery's L6 (`63 00` x4 → 63 verb-shaped, lead-level) supplies the missing verb: @1529 = "que [NP: 21 65] [63-verb] pour..." parses grammatically, so @1529 does **not** become a second contradiction **if** 63 is verb-class. 63's class is ungranted — the hinge is now 63, not 65. The 21="suite" value-kill itself is untouched by this verdict.

Related queued targets now informed by 65=noun: `ver78-65-completion`, `ellipsis-65-62-60-profile`, `clitic-44-65-discriminator`, `stem48-65-value` (supervisor's queue; not touched here).

## Recommended follow-ups (verdict is promote; these are live ends, not required null follow-ups)

1. **verb-63-frames** (priority 2): test 63=verb-class with >=3 frame-legs (`63 00` x4 pour-complements, `12 63`, distribution vs 24/88 verb frames). Decides the @1529/@371 parses and closes the suite-21-qui-que escalation #2 hinge.
2. **noun-65-value** (priority 3): now that 65 is noun-class, test value hypotheses — candidates from `29 40 65` ("[X]ere 65": 65 as head noun after "-ere" word) and `65 64 59 32` ("65 qui est 32": predicative complement 32 constrains 65's semantics).

## Provenance

R5005, sealed gate instances, and the red-team adjudication queue untouched. No invented data: n(65)=25; preceders {21:x4, 40:x3, 91/74/24/08/06:x2, ...}; followers {63:x4, 23:x3, 64:x3, 13:x3, 94:x2, ...}. Lock `locks/prof-65.lock` created on start, deleted on completion.
