# Battery verdict: ce88-pronoun-frame — test the 'ce [88-verb]' pronoun+governor frame at @401-402

- Target id: `ce88-pronoun-frame` (priority 3)
- Claim: test the "ce [88-verb]" pronoun+governor frame at @401-402
- Worker: battery worker (subagent session c5f58f0e-caf4-45c7-98f0-9020a7b1d106, parent: next-token-supervisor)
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, repair_parse.py tokenization). 1,847 pairs / 96 types re-verified. canonical.py never used. R5005 untouched. Sealed gates untouched. Red-team queue untouched. No invented numbers.
- Lock: code/crowd17/next-token/locks/ce88-pronoun-frame.lock created 2026-10-09T08:15:07Z (no pre-existing lock; nothing stale); deleted on completion.
- Verdict: **PROMOTE** — 53 parses as 88's complement/object at @402-403 under the verb-governor role, zero standing-value contradiction, cross-checked at @86/@646/@1541. 53's VALUE stays unnamed and open; 88's class stays battery-grade (red-team venue owns ratification).

## 1. Bar (verbatim from battery-queue.json)

"53 must parse as 88's complement/object under the verb-governor role with zero standing-value contradiction, cross-checked against 88's other governor windows (@86, @646, @1541); else fence with stated cause"

Numbered clauses (pre-registered BEFORE any window analysis; bar not modified after seeing data):

- **C1.** At @402-403, 53 occupies the post-verbal complement/object slot of 88 under the verb-governor role: subject 45='ce' (demonstrative pronoun, per parent battery ce88-leftedge-402 PROMOTE 2026-10-09), 88 finite transitive verb-governor (battery-grade class) — i.e. "Ce [88] [53...]" parses grammatically.
- **C2.** Zero standing-value contradiction: no banked, granted, provisional, or battery-grade value is contradicted by the C1 parse; 53's own stream profile does not force a non-object reading.
- **C3.** Cross-check: @86, @646, @1541 each show 88 in the same governor role with a post-verbal complement, with zero contradiction — the same role 53 fills at @402.
- **Adverse.** 88=verb-class is battery-grade (battery-governor-88-value PROMOTE 2026-10-08; battery-finiteness-88-86 PROMOTE 2026-10-09). Do not re-litigate the class; red-team venue owns ratification.

## 2. Method

Re-derived the stream independently (repair_parse.py tokenization over repaired_offsets.json; 1,847 pairs / 96 types confirmed). All @-offsets are 0-based repaired-stream pair indices. Census figures below are byte-exact, re-derived by this worker. Standing values used: banked pencil (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout A5, 00=pour A9 class-level, 84=on A15, 47=ce A4, 45=ce A11 hold); provisional (59=est, 77=le). Battery-grade items cited with status labels, never treated as ratified: 88=verb-class governor (battery-governor-88-value PROMOTE), @86 transitive frame (battery-finiteness-88-86 PROMOTE), 45='ce' demonstrative-pronoun role (ce88-leftedge-402 PROMOTE, the parent of this target). The parent battery's decisions are used, not re-litigated.

## 3. Window-level evidence

**The locus.** @395-411, row a2_07 tail into a2_08:
`395:64 396:79 397:82 398:48 399:06 400:11 401:45 402:88 403:53 404:34 405:69 406:26 407:00 408:33 409:01 410:02 411:53`
Under standing values: `... 64=qui 79=tout 82=m [48] [06] 11=la 45=ce [88] [53] 34=i [69] [26] 00=pour ...`
Parent battery (ce88-leftedge-402, PROMOTE) decided: 45 is non-determiner at @401 — demonstrative pronoun; the "ce [88-noun]" determiner frame FALLS; the contact survives only as pronoun + verb-governor. "45 88" is a hapax bigram (1x stream-wide, re-verified) — this window is the entire population of the frame.
"88 53": 88's successor 53 occurs exactly 1x (@402; re-verified against the governor battery's 23-window census: successors 77 x3, 11 x2, 24 x2, and 16 singletons incl. 53).

**C1 — "Ce [88] [53...]" parses.** Subject: 45='ce' demonstrative pronoun (parent promote; pronoun precedent "45 64" = 'ce qui' x3 re-verified @314 "37 78 [45 64] 59 32", @340 "31 14 [45 64] 96 43", @1024 "92 64 [45 64] 96 43"). Verb: 88 in its battery-grade finite transitive verb-governor role. Complement: 53 in the immediate post-verbal slot — the direct-object position. "ce + finite verb + NP" is standard French (parent report: "ce fut", "ce serait", "ce doit"). **C1: PASS.**

**C2 — zero standing-value contradiction.** 53's profile re-derived: n=11 at @16/@57/@168/@403/@411/@708/@804/@1020/@1280/@1473/@1581. Successors: 12 x4 (@57/@168/@708/@1581), 84 x2 (@411/@1020), 17/34/69/61/60 x1. Predecessors: 91 x2, 35 x2, 84/88/02/98/48/41/24 x1. No standing value (banked, granted, provisional) is assigned to 53 — nothing to contradict. The one killed hypothesis touching 53 ('donne': 53="donn"+12-48="ne") was KILLED by prof-53 (null 2026-10-08) via 53-12-41 @58 and 53-12-44 @1582 ("donnn" impossible) — so 53 is not verb-locked; nothing in its profile forces a non-object reading. Follower at the locus is 34='i' (banked letter): "53 34" may be word-internal ("53i..." — 34 is word-internal in the "la premiere" crib, 82-34-29) or a 53-word followed by an i-word; either way the 53-headed phrase remains 88's post-verbal complement. No standing rule pins 34's word position, and §7 (sole polyvalence 67, holds, kills, splits) touches nothing here. **C2: PASS.**

**C3 — cross-check @86/@646/@1541.** Re-verified: 88->77 occurs exactly 3x stream-wide, at exactly these windows (n88=23 re-verified).
- @86 (a1_02): `16 14 06 [88] 77 66 98` → "[88] le [66]" under 77='le' provisional. The finiteness battery (PROMOTE 2026-10-09) already resolved this as the "'88 le 66' transitive frame" in the governor role — cited, not re-litigated.
- @646 (a4_02): `24 87=ce 61 [88] 77 78 52` → "[88] le [78]".
- @1541 (a8_00): `21 62 93 [88] 77 78 43` → "[88] le [78]"; the "88 77 78" trigram is byte-identical to @646's (x2 stream-wide, re-verified) — a stable "88 le [78]" object frame.
All three show 88 governing a post-verbal 'le'-headed object NP: the same transitive governor role that 53 fills bare at @402 ("[88] [53]" vs "[88] le [X]" — a transitive verb takes both bare and article-headed objects). Zero contradictions: 77='le' used consistently with its provisional standing; 66/78/52/43 are open. **C3: PASS** (3/3 windows).

## 4. Per-clause pass/fail

- C1 (53 as 88's complement/object at @402-403): PASS — "Ce [88] [53...]" grammatical under the given roles.
- C2 (zero standing-value contradiction): PASS — 53 unconstrained by any standing value; 'donne' verb reading already killed; 34='i' follower does not contradict.
- C3 (cross-check @86/@646/@1541): PASS — all three show "88 le X" transitive-object frames, same governor role, zero contradictions.
- Adverse (88=verb-class battery-grade, not re-litigated): ANSWERED — the class is taken as given throughout; no argument for or against it is made; ratification explicitly left to the red-team venue.

No standing red-team verdict is contradicted; no battery verdict is downgraded (governor-88-value, finiteness-88-86, ce88-leftedge-402, prof-53 are used, not re-litigated).

## 5. Verdict

**PROMOTE.** All bar clauses pass and the adverse is answered, per §4.

Scope of the promote (explicit): the FRAME test promotes — "ce [88-verb]" pronoun+governor frame at @401-402 holds with 53 as 88's complement. NOT promoted: 53's value (unnamed, still open), 88's value (class-level battery-grade only; red-team venue owns ratification), 45='ce' beyond the parent battery's existing promote.

## 6. Optional follow-ups (verdict is promote; for supervisor queueing at discretion)

- F1. id: `ce88-53-value` | priority: 4 — name 53's value. Bars: name the value with >=2 independent frames parsing cleanly under the "88's object at @402" constraint + 53's 11-window profile cohering (successor 12 x4, predecessor spread). Evidence: this report §3 C2. Adverses: 'donne' KILLED (prof-53); 53's value must stay nominal-compatible at @403; do not touch R5005.
- F2. id: `ce88-53-wordbound` | priority: 4 — decide the "53 34" word boundary at @403-404. Bars: decide word-internal ("53i...") vs word boundary with 34's positional profile (34 n=11; word-internal in "la premiere" crib; 'ni'=12-34 word-final @1741) stated as evidence. Evidence: this report §3 C2. Adverses: 34='i' banked (do not revalue); either outcome preserves the complement role.

## 7. Bookkeeping

- Report: code/crowd17/report_inbox/battery-ce88-pronoun-frame.md (this file).
- Queue: battery-queue.json `ce88-pronoun-frame` queued -> verdict/promote, date 2026-10-09 (pre-write assert: no prior verdict; own entry only; temp-file + rename; JSON re-validated).
- Lock: created 2026-10-09T08:15:07Z (no pre-existing lock; nothing stale); deleted on completion.
- canonical.py never used; R5005, sealed gates, red-team queue untouched.
