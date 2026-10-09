# Battery report — x-07-verb-stem

Worker: 22ec7fde-3fb0-4ae2-8ba3-bdcbb1779dd8. Date: 2026-10-09.
Lock: `code/crowd17/next-token/locks/x-07-verb-stem.lock` (fresh, this worker).

## Bar (verbatim, from battery-queue.json)

`census all 07 windows; promote a stem value iff >=2 independent [07]-ent/[07]-verb frames parse with 07's follower profile verb-consistent; else fence 07 as open`

Numbered clauses (pre-registered BEFORE testing):

1. C1 — census all 07 windows on the repaired stream.
2. C2 — promote a stem value iff >=2 independent `[07]-ent` / `[07]-verb` frames parse AND 07's follower profile is verb-consistent.
3. C3 — else, fence 07 as open.

Note: the queue's bar (authoritative per §2) supersedes the sibling report's
suggested wording and the dispatch brief's paraphrase; it is the same test.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
tokenized like `code/side-keyhunt/repair_parse.py`. Asserts held (1847 pairs,
96 types). `code/side-keyhunt/canonical.py` never used. R5005, sealed gates,
red-team queue untouched. Standing values per BATTERY-PROTOCOL.md §7.
@-offsets are 1-based stream positions (0-based index + 1).

## Window-level evidence

n(07) = 8, byte-exact. Context ±6, 07 bracketed:

- @682 (a5_00): `64 37 77 45 23 09 [07] 00 92 64 29 40 65` — "[09] [07] pour [92]"
- @772 (a5_03): `66 98 80 10 22 94 [07] 06 94 15 33 73 37` — "ne [07] ent ne [15]"
- @794 (a5_04): `65 84 06 77 64 46 [07] 64 56 37 44 77 86` — "que [07] qui [56]"
- @942 (a5_10): `00 33 21 64 37 01 [07] 50 40 08 62 98 96` — "[01] [07] [50]"
- @980 (a6_01): `51 45 08 01 00 92 [07] 76 47 78 45 01 24` — "[92] [07] [76]"
- @1094 (a6_06): `00 33 79 80 06 43 [07] 55 81 06 29 67 86` — "[43] [07] [55]"
- @1193 (a7_00): `59 42 06 84 59 46 [07] 24 82 16 96 82 16` — "que [07] [24] m'"
- @1751 (a8_08): `46 56 40 06 65 34 [07] 28 89 26 24 85 58` — "i [07] [28]"

The exact bigram `94 07 06` ("ne [07]ent") occurs exactly **once** stream-wide
(@771–773, 0-based). Predecessor census of 07: 09×1, 94×1, 46×2, 01×1, 92×1,
43×1, 34×1. Follower census: 00×1, 06×1, 64×1, 50×1, 76×1, 55×1, 24×1, 28×1.

## Per-clause pass/fail

- C1 — PASS. Full 8-window census above.
- C2 — **FAIL at kill grade.** Two independent failures:
  - (a) Only ONE `[07]-ent` frame exists stream-wide (@772); the bar demands
    >=2. The remaining seven windows contain no `[07]-ent` or `[07]-verb`
    frame: @682 has `[07] pour` (a bare stem before `pour` is ungrammatical);
    @942/@980/@1094 have open neighbors with no verb licensing.
  - (b) The follower profile is verb-INCONSISTENT at kill grade in three
    independent windows:
    - @794 `que [07] qui`: 64=`qui` is a standing grant. A bare verb stem
      cannot be the antecedent of relative `qui`; interrogative
      `que X qui ?` is ungrammatical in French. 07 is forced
      nominal/pronominal. A finite-verb reading fails identically (a finite
      verb cannot head `qui`).
    - @1193 `que [07] [24]`: 24 is modal/finite-verb class
      (battery-promoted). `que [07-N] [24-V]` is a clean nominal-subject +
      finite-verb clause; a bare stem cannot be a subject. 07 forced nominal.
    - @1751 `i [07] [28]`: 34=`i` is ground truth. A bare verb stem after
      `i` is ungrammatical; nominal fits. 07 forced non-stem.
  - Under §7 (67 is the sole true polyvalence; batteries declare no
    polyvalence), the three nominal-forcing windows and the one stem-shaped
    window cannot coexist in a uniform `07 = verb stem` class. The class is
    forced false at kill grade.
  - Circularity note on the sole leg window: at @772, the `ne [07]ent`
    parse (sibling battery `formula-94-07-06-94` F4) attaches 06 as `-ent`
    only iff 07 is a verb stem — the battery-promoted 06 rule is
    "06 = `-ent` iff left neighbor is a verb stem; else standalone `ent`".
    The leg's parse therefore assumes the very class under test. With the
    stem class killed, the honest re-read is `ne [07-N] ent …` with 06 as
    standalone `ent` (its promoted standalone behavior), not a 3pl verb.
- C3 — superseded: the failure is kill-grade, not inconclusive (see §4).

Adverses: none listed.

## Verdict

**KILL.** The `07 = verb stem` avenue — including the `ne [07]ent` leg as a
naming device — is dead at kill grade. Three independent windows (@794,
@1193, @1751) force 07 non-verb-stem; the sole stem-shaped window (@772)
parses as such only under the claim itself; the follower profile is
verb-inconsistent; the >=2-frame threshold is unmet (exactly 1).

## Scope and consequences

- Kills ONLY the verb-stem avenue for 07. No value is named; 07's class
  returns to open/fenced (nominal legs at @794/@1193/@1751 are live leads,
  not promotions — the bar did not cover them).
- Sibling `formula-94-07-06-94`'s verdict (KILL of the mirror frame) is
  untouched — it does not depend on 07's class. BUT its supporting parse F4
  (`ne [07]ent`, "07 an open stem") and F6 ("both 94s are preverbal
  negators") assumed the stem reading that is now killed. F4 was an
  adverse-answer, not a promoted value, so nothing is downgraded — but the
  @771–773 window needs a re-read (`ne [07-N] ent ne [15]…`), and the two
  "clean ne-frame" legs F4/F6 supplied to the ne-94 / ent-06 promotions
  should be re-audited. Flagged for the supervisor; the re-audit is
  red-team/supervisor venue, not changed here.
- No standing or red-team verdict contradicted or downgraded; §7 intact.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-x-07-verb-stem.md`
- Queue: `x-07-verb-stem` → status `verdict`, result `kill`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; temp-file + rename;
  JSON re-validated; own entry only; no downgrade)
- Lock created on start, deleted on completion (verified gone).
- `canonical.py` never used; R5005, sealed gates, red-team queue untouched.
- Kill verdict: no follow-ups mandated by §4. Observations for the
  supervisor (not mandated): a `nominal-07` battery (the @794/@1193/@1751
  legs), and a re-audit of the @771–773 leg for the ne-94/ent-06 line.
