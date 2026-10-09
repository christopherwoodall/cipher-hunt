# Battery report: noun-74-formula

- Target: `noun-74-formula`
- Claim: "Test 74 as a nominal/formula head — '49 74 74 [46/47/48/40]' chains x4, 49-prev x5, self-loop x6."
- Date: 2026-10-09
- Worker: battery worker (subagent 0c9fb7cf-79b3-4efd-8b45-4ee60a8914e2)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed like
  `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs, 96 types).
  `canonical.py` never used. R5005, sealed gates, red-team adjudication queue
  untouched.
- Lock: `code/crowd17/next-token/locks/noun-74-formula.lock` (created at start,
  deleted at end; no prior lock existed).

## Bar (verbatim from battery-queue.json, pre-registered BEFORE testing)

"Promote iff a French nominal/formula frame parses the chains; kill iff 74 shows verb-frame contact."

## Numbered pass/fail clauses (restated before testing, not modified after)

1. **C1 (promote arm)** — a French nominal/formula frame parses all four
   '49 74 74 [46/47/48/40]' chains with stated boundary evidence.
2. **C2 (kill arm)** — 74 shows verb-frame contact (lane's distributional
   standard: the `ne-alone-02-74` follower test set {80, 89, 29, 85, 33}).

## Adopted premises (not re-litigated)

- `ne-alone-02-74` KILL (2026-10-09): 51 combined 02+74 windows, zero
  verb-frame contact in the bar's stated test set; '74 74' x6 resists
  verb-shape.
- `noun-74-census` NULL/fence (2026-10-09): 74 is class-open; the doubling
  family ('74 74' x6, 12 windows) contradicts every whole-word class at kill
  grade — no noun, verb, adjective, pronoun, adverb, or determiner doubles
  adjacently in French.
- Standing values: 46=que (GT), 47=ce (prom, A4), 48=e (prom), 40=e (GT),
  84=on (prom, A15 conditions C1–C3), 33=INF (class), 36=noun (class, R18),
  65=noun (class, R18), 32=verb (class). 49 and 74 are unvalued (§3 bars
  inventing values for them).

## The four chains (byte-exact, 0-based)

- W1 @416 (row a2_08): `37 78 [49 74 74] 46 49` — "49 [74 74] que(46)"
- W2 @815 (row a5_05): `14 29 [49 74 74] 47 78` — "49 [74 74] ce(47)"
- W3 @860 (row a5_07): `02 24 [49 74 74] 48 47` — "49 [74 74] e(48)"
- W4 @918 (row a5_09): `02 24 [49 74 74] 40 08` — "49 [74 74] e(40)"
- 49-prev x5 confirmed: the four chains + @1844 (a8_11, row-final
  `78 49 74 93`, no doubling).
- Self-loop '74 74' x6 confirmed: @417, @816, @861, @919, @1053, @1637
  (first-74 indices; the @1053 and @1637 loops are not 49-prev).

## C1 test — can a French nominal/formula frame parse the chains?

**Nominal-head reading: FAIL.** All four chains contain the '74 74'
doubling. Per the adopted `noun-74-census` finding, two identical adjacent
content words are ungrammatical in French prose — this kills any whole-word
nominal head at all four chains at kill grade, independent of 49/74 values.

**Formula reading: FAIL.** A formula is an invariant fixed expression, but
the four chains vary on both edges:
- right followers: 46 (que), 47 (ce), 48 (e), 40 (e) — four distinct cells;
- left contexts: "37 78", "14 29", "02 24", "02 24".
No single French formula frame covers "49 74 74" + {que, ce, e, e}. The two
non-chain loops (@1053 "29 74 74 45", @1637 "87 74 74 35") further break any
fixed-formula shape.

**Naming a frame is blocked by §3.** 49 and 74 are both unvalued. Any named
French frame ("le [N] que", "[formula] que", …) would require inventing a
value for 49, for 74, or both. The unit reading ("49 74 74" as one word with
sub-lexical 74, e.g. doubled consonant) remains the leading hypothesis per
the census's C4, but it is already queued as `unit-49-74-74` — it is not a
namable nominal/formula frame at battery grade, and re-testing it here would
duplicate a queued target.

**C1: FAIL** — no French nominal/formula frame parses the chains with stated
boundary evidence.

## C2 test — does 74 show verb-frame contact?

Independent re-run of the lane's distributional test on all 34 74-windows:
- Followers in {80, 89, 29, 85, 33}: **0/34**. Confirmed byte-exact.
- The adopted `ne-alone-02-74` zero-contact finding is corroborated, not
  contradicted.

Two positional subject-contact windows were examined and do NOT meet kill
grade:
- @261 (a2_02): `43 77 le(77) on(84) [74] ce(45) 93 52` — "on 74" puts 74 in
  the verb slot of a promoted subject, BUT the reading loads on A15's
  conditions C1–C3 holding at this window (untested; the census flagged the
  same caveat) and on 93's class (now verb-class per R19, which breaks the
  old "governor + ce + NOUN" parse — a red-team-level tension, out of
  battery scope).
- @1500 (a7_11): `89 41 [74] on(84) 33(INF)` — "74 on [INF]" is
  inversion-shaped ("[V]-on [INF]"), BUT the reading loads on 84='on' holding
  at @1501 (A15 conditions untested here) and on "41 74" not being a word
  unit (cf. the "82-84 = mon" word-unit precedent).
- Both windows were visible to the standing batteries; the doubling family
  independently contradicts whole-word verb-74 at 12 windows.

**C2: does NOT fire** — no verb-frame contact at kill grade under the lane's
distributional standard. The subject-contact windows are recorded as the
lead follow-up, not as a kill trigger (firing here would re-litigate the
standing `ne-alone-02-74` kill on untested conditions).

## Verdict: NULL

C1 fails (no frame parses the chains); C2 does not fire (no kill-grade
verb-frame contact). 74 stays class-open; the chains stay unparsed at battery
grade. No standing or red-team verdict contradicted or downgraded; §7 intact
(67 et/veut remains the sole true polyvalence); canonical-stream caveat
stands (all four chains sit on offset-0 rows with unvalidated upstream
offsets).

## Adverses answered

- None listed on the target.

## Follow-up targets (nulls regenerate work; all three verified ABSENT from battery-queue.json)

1. `subj-74-261-1500` (P3): test the subject-contact windows @261 ("on 74")
   and @1500 ("74 on 33-INF") — decide whether A15's 'on' conditions C1–C3
   hold at @260/@1501. Bar: if 'on' is licensed at both, 74 shows
   subject-frame contact (kill-seek the formula hypothesis); else fence the
   contact as conditional. Kill iff contact is licensed under stated
   conditions.
2. `formula-49-value` (P3): name 49's class/value via its full contact
   profile (n(49)=12: 49-prev x5 of 74, plus 7 non-74 windows). Bar: name
   49's class at battery grade with byte evidence, or fence 49 as
   class-open; a named 49 unlocks the '49 74 74' chain parse.
3. `chain-follower-class` (P4): test whether the four chain followers
   (46=que, 47=ce, 48=e, 40=e) form one licensed complement class for a
   single head word. Bar: state the single complement class with a French
   frame, or fence the single-word "49 74 74" reading on heterogeneous
   government.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-noun-74-formula.md` (this file).
- Queue: `battery-queue.json` — `noun-74-formula` status `queued` ->
  `verdict`, result `null`, date 2026-10-09 (temp-file + rename; pre-write
  assert confirmed queued/verdictless; JSON re-validated post-write; only
  this entry's keys touched; 1,239 targets total).
- Lock created at start, deleted at end (verified gone).
