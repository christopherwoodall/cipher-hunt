# Battery report: subj-42-class

- Target: `subj-42-class` (P3)
- Verdict: **PROMOTE** (bar passes at battery grade; scope is confirmation + the two mandated tests — no value named, no class upgrade claimed)
- Date: 2026-10-09
- Worker: battery worker, session 362b87ff
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- Lock: `locks/subj-42-class.lock` created on start, deleted on completion (verified gone).
- Offsets: 0-based repaired-stream indices.

## Bar (pre-registered BEFORE testing)

Verbatim from `battery-queue.json`:

> name 42's class with ≥2 frame-legs (test the '42 06' x5 legs under the ent-06-host-census decision rule: 06 is finite "-ent" 3pl iff its left neighbor is a verb stem — is 42 verb-stem-shaped?); re-state the '42 94 X' frame under the named 42

Numbered clauses (frozen before testing):
- **C1**: 42's class named with ≥2 frame-legs (byte-evidenced windows).
- **C2**: the five '42 06' windows tested under the ent-06-host-census decision rule — 06 is finite "-ent" 3pl iff 42 is (or composes) a verb stem; state whether 42 is verb-stem-shaped at each window and therefore whether 06 is finite or syllable-tier there.
- **C3**: the '42 94 X' frame re-stated under the named 42.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/subj-42-class.lock` on start (no prior lock existed; entry was queued/verdictless).
2. Re-derived the repaired stream in-session (asserts held).
3. Census: n(42)=20 byte-exact. Followers: 06 x5, 98 x3, 94 x3, 16 x2, 44 x2, 48/63/96/41/33 x1. Predecessors: 29 x3, 76 x3, 33 x2, 59 x2, 63/61/78/48/24/74/52/56/50/22 x1. Matches the brief.
4. '42 06' windows (0-based): @205, @266, @543, @1187, @1814 — exactly x5. '42 94' windows: @493, @784, @1794 — exactly x3.
5. Adopted as premises (completed battery verdicts, not re-litigated):
   - `ent-06-host-census` PROMOTE (2026-10-09): decision rule — 06 is a finite "-ent" 3pl ending iff its left neighbor is (or composes) a verb stem; otherwise syllable (word-initial "ent" after a complete word, or word-internal "ent").
   - `stem-42-verb` NULL (2026-10-08): "42 takes 'ent' as a verb stem" — resolve iff 42 shows verb-class contact in ≥3 of the 5 windows with A1 intact; did not resolve (fence-equivalent).
   - `subj-42-ne-frame` NULL (2026-10-09): '42 94 X' frame fenced; control @1794 parses as "[42] n'est [37-pred]" (B1 PASS); @493 (02) and @786 (74) slots fenced on the X side; verbal arm dead via `ne-alone-02-74` KILL.
   - `val-42-det-gap` PROMOTE (2026-10-09): 42's value inventory restricted to bare-capable nouns (proper nouns / "rien"-family; pronoun leg flagged for R20).
   - `noun-42-value` NULL (2026-10-09): 'erreur' dead; joint-unsatisfiability — "29 42" x3 demands syllable-42, subject/predicate windows demand word-42 (red-team venue).
6. Standing values used (never re-litigated): GT (11=la, 29=er, 40=e, 46=que); granted (47=ce A4, 79=tout A5, 84=on A15, 96=par, 64=qui); provisional (59=est, 77=le); R19-055 (42=["noun","cls"], class-tier); A1 (37/32/42 predicative frames); R17-001 ('94 59' x3 = 'n'est', STRONG LEAD); R19-167 (94="ne", single-'ne'); `verb-63-frames` PROMOTE (63=verb-class); 98='vient' battery-grade (`vient-98-name` PROMOTE).

## Window-level evidence

All 20 42-windows (±3, 0-based @, row):

- 0b@79 (a1_02): `00 11 29 [42] 98 51 62`
- 0b@205 (a2_00): `11 92 63 [42] 06 77 44`
- 0b@219 (a2_01): `59 46 29 [42] 16 24 89`
- 0b@266 (a2_02): `93 52 33 [42] 06 73 47`
- 0b@282 (a2_03): `61 20 61 [42] 48 52 89`
- 0b@428 (a2_09): `62 48 76 [42] 63 77 86`
- 0b@464 (a2_10): `87 11 59 [42] 96 00 33`
- 0b@488 (a2_11): `19 64 76 [42] 41 20 67`
- 0b@493 (a2_11): `20 67 78 [42] 94 02 79`
- 0b@543 (a3_01): `44 29 48 [42] 06 00 46`
- 0b@784 (a5_04): `89 11 24 [42] 94 74 65`
- 0b@1072 (a6_05): `11 44 74 [42] 98 98 12`
- 0b@1144 (a6_08): `62 16 29 [42] 98 98 86`
- 0b@1187 (a6_10): `06 06 59 [42] 06 84 59`
- 0b@1410 (a7_07): `95 46 52 [42] 16 97 69`
- 0b@1503 (a7_11): `74 84 33 [42] 33 00 86`
- 0b@1617 (a8_03): `48 31 76 [42] 44 11 84`
- 0b@1794 (a8_09): `00 86 56 [42] 94 59 37`
- 0b@1814 (a8_10): `15 93 50 [42] 06 29 37`
- 0b@1838 (a8_11): `69 64 22 [42] 44 83 21`

### C1 — class named: NOUN (≥2 frame-legs)

- **Leg 1 — subject of "n'est", @1794:** `56 [42] 94 59 37` = "[56] [42] n'est [37-pred]". Adopted B1 PASS (`subj-42-ne-frame`): '94 59' is R17-001's 'n'est'; 37 predicative (A1). `val-42-det-gap`: determiner-less subject, forced by no-pro-drop. Subject slot = nominal.
- **Leg 2 — subject of "vient", @1072:** `74 [42] 98 98` = "[74] [42] vient [98]". 98='vient' battery-grade. Subject slot = nominal.
- **Leg 3 — subject of "vient", @1144:** `29 [42] 98 98` = "er [42] vient [98]". Same frame, second window.
- **Leg 4 — predicative "est [42]", @464:** `59 [42] 96 00` = "est(59,prov) [42] par(96) pour(00)". A1 predicative frame grant on 42 directly instantiated.
- **Leg 5 — object of prendre-stem, @1410:** `52 [42] 16` = "[52] [42] [16]". 52 is the lexicon-verified prendre-family stem (transitive). Object slot = nominal.
- **Leg 6 — "76 [42]" + "42 44", @1617:** `[76-N] [42] [44-pred] la(11)`. 76 carries the promoted masculine-noun class; "42 44" instantiates 42's A1 predicative frame (44 predicative).

Six frame-legs, all nominal. **C1: PASS — 42 = noun class**, consistent with (not an upgrade to) R19-055's class-tier grant.

### C2 — the '42 06' x5 legs under the decision rule

Question: is 42 verb-stem-shaped at any of the five windows (which would make 06 the finite "-ent" 3pl)?

- **@205** (a2_00): `63 [42] 06 77` — pre=63 (verb-class, `verb-63-frames` PROMOTE). 42 sits post-verbally (complement/object position), not as a verb stem. 06's follower 77="le" (provisional) is a complete word: "ent le" cannot compose, so 06 cannot be word-initial "ent-" of a following word; it attaches left.
- **@266** (a2_02): `33 [42] 06 73` — pre=33 (verb-shaped; `val-33-verb` NULL on value, verb contact standing). Post-verbal 42 = object position. Follower 73's value is open: "ent[73]" composition ("entre"-shaped) is geometrically possible but needs 73's value — fenced, not battery-decidable.
- **@543** (a3_01): `48 [42] 06 00` — pre=48 ('e' letter-tier; 48's "est"/"ne"/"de" kills hold; `verb-48` NULL). 48 is a particle, not a verb; 42 is not verb-stem-shaped via left context. Follower 00="pour" (A9) cannot compose with "ent" → 06 attaches left.
- **@1187** (a6_10): `59 [42] 06 84` — pre=59='est' provisional (copula). "est [42]" is the A1 predicative frame — 42 predicative-nominal, the opposite of verb-stem-shaped. Follower 84="on" cannot compose with "ent" → 06 attaches left.
- **@1814** (a8_10): `50 [42] 06 29` — pre=50 (class open; `val-50-crosswindow` queued). No standing license makes 50 a verb stem composing with 42. Follower 29="er" (GT) cannot compose with "ent" ("enter" is not a French word) → 06 attaches left.

**Result: 42 is not verb-stem-shaped under any standing license at any of the five windows.** Post-verbal/post-copular positions (@205, @266, @1187) actively favor nominal 42; @543's particle left context and @1814's open left context offer no verb-stem route. Under the decision rule, **06 is syllable-tier — not finite "-ent" 3pl — at all five windows**, attaching left as word-final "-ent" ("[42]ent"; @266's "ent[73]" alternative fenced pending 73's value).

**Headlined tension (not resolved):** syllable-06 attaching left makes 42 stem-shaped at these five windows ("[42]ent" word-internal "-ent"), while Legs 1–3 demand standalone word-42. This is the `noun-42-value` joint-unsatisfiability (syllable-vs-word), already queued as red-team input (`poly-42-syllable-word`). Resolving it needs either a second 42 value (polyvalence — §7 bars battery declaration; R20 42-polyvalence venue) or overturning an adopted fence. Battery does not touch it.

**C2: PASS** — the five legs are tested and decided under the rule: 06 = syllable at all five; the verb-stem-42 hypothesis fails at every window (corroborates, does not re-litigate, `stem-42-verb` NULL).

### C3 — '42 94 X' re-stated under noun-42

Under named noun-42, the frame reads **[42-N] + clausal "ne" + X**, with 42 as the pre-verbal nominal (subject) of a "ne"-negated clause:

- **@1794** (control): "[42] n'est [37-pred]" — resolves (adopted B1 PASS). Bare-"ne" + "est" is the licensed construction (`ne-1330-bare-corpus` PROMOTE).
- **@493**: "[42] ne [02]" — 42's side holds (pre-verbal nominal); the X slot (02) is fenced (adopted: 02's class split/unnamable, `02-class-609` NULL).
- **@784**: "[42] ne [74]" — 42's side holds; the X slot (74) is fenced (adopted: noun-74 contradicted at kill grade at this window, `noun-74-census` NULL).

No window forces 42 non-nominal; the frame's unresolved part is entirely on the X side. **C3: PASS.**

## Per-clause pass/fail

- **C1: PASS** — 42 = noun, six frame-legs (subject of "n'est" @1794; subject of "vient" @1072/@1144; predicative "est [42]" @464; object of prendre-stem @1410; "[76-N] [42]" + "42 44" @1617).
- **C2: PASS** — all five '42 06' windows tested under the ent-06-host-census decision rule: 42 not verb-stem-shaped at any window → 06 syllable-tier (word-final "-ent") at all five; @266's "ent[73]" alternative fenced on 73's value.
- **C3: PASS** — '42 94 X' re-stated as "[42-N] ne [X]"; @1794 resolves, @493/@784 fenced on X, 42's side holds everywhere.
- Adverses: none stated.

## Verdict: PROMOTE

Scope (explicit): this is a battery-grade **confirmation** of the standing R19-055 noun-class grant with six new frame-legs, plus the two mandated tests. It is not a class upgrade (class-tier already granted), names no value, requests no registry change and no red-team act. Untouched: 42's open value, the `val-42-det-gap` bare-capable-noun inventory restriction, the `stem-42-verb` fence, the syllable-vs-word tension (red-team venue: R20 42-polyvalence docket, `poly-42-syllable-word` input queued), the fenced X-slots of '42 94 X', 73's value. No standing or red-team verdict contradicted or downgraded; §7 intact; canonical-stream caveat stands. Per §4 (promote), no follow-ups required.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-subj-42-class.md` (this file)
- Queue: `subj-42-class` → `status: verdict`, `result: promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated from disk; own entry only; no downgrade)
- Lock created on start (2026-10-09T15:11:29Z), deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
