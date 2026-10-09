# Battery report: stem-40-06-1748

- Target id: `stem-40-06-1748`
- Claim: "test the left word's class at @1748: vowel-final verb stem vs 'e'-final non-verb word"
- Date: 2026-10-09
- Worker: battery worker (subagent 5fd19eaa-f5d1-45a7-9def-7a0b41bd2522)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). Verified in-session: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Offset note: the brief uses 1-based @1748 = 0-based @1747 = `06`. "The left word" = the `56 40` unit (0-based @1745–1746). Fork A: `56 40` = vowel-final verb stem ("Xé"), `06` = finite 3pl ending → "Xéent"-shaped ("créent"-class). Fork B: `56 40` = "e"-final non-verb word, `06` = separate syllable.

Terms (ASD-STE100): "fork" = one of the two possible readings. "Verb stem" = the word part before the ending. "3pl" = third-person plural, "ils créent". "Hapax" = occurs exactly once in the stream. "Strand" = leave a piece with no valid parse.

## Bar (verbatim, pre-registered before testing)

"state which fork the left context supports"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** The left context licenses the verb-stem fork (fork A) at battery grade.
2. **C2:** Fork B is excluded at battery grade (strands unlicensed material or requires invention).

Adverses listed: none.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/stem-40-06-1748.lock` on start (agent id + UTC timestamp); deleted on completion. No stale lock was present.
2. Re-derived the repaired stream in-session. All @-offsets below are 0-based.
3. Byte-exact censuses: `56 40` bigram, `40 06` bigram, full `06`-predecessor profile, `56`-successor profile.
4. Standing premises used, not re-litigated: 46="que" (banked pencil GT), 40="e" (banked GT), 06="ent" (promoted, ent-06), 82="m" (banked GT), 94="ne" (battery-promoted), 65 noun-class (R18), §7 (67 et/veut is the sole true polyvalence — a noun/verb class alternation for 56 needs red-team declaration).
5. Adopted as premises (not re-litigated): `rightedge-56-1745` C2 PASS ("46 56 40 06" = "que" + 3pl verb "[56]e-ent", zero contradiction); `stem-56-whole` forced-stem finding at @1745 (whole-word 56 strands "40 06": "e"+"ent" is not a French word, no alternative segmentation parses); `form-56-1627` PROMOTE (bare 56 = 3sg finite, "crée"-shaped).

## Window-level evidence

Locus byte-confirmed, head of row a8_08 (offset 0):

- 0b@1745=56, @1746=40, @1747=06, @1748=65, @1749=34. Left: @1740–1744 = `12 34 94 82 46` ("[12] i(34) ne(94) m(82) que(46)").

Distributional facts (byte-exact, re-derived in-session):

- **`56 40` = 1x stream-wide** (@1745). **`40 06` = 1x stream-wide** (@1746). The trigram `56 40 06` is a complete hapax.
- **`06` is always bound:** 29 predecessor types censused (41, 14×2, 37, 42×5, 78, 11, 94, 01, 17, 48, 80×2, 77, 82×4, 06×2, 62×2, 07, 84, 86, 24, 64×2, 81, 12×2, 30×4, 16, 60, 68, 40, 93) — `06` never stands word-initial anywhere in the stream. The lane's "word-internal iff X is bound" standard therefore keeps `06` bound here too.
- **56's successors:** 14 distinct followers; `40` is one of them (this window only).

## Per-clause pass/fail

- **C1 — PASS (fork A supported by the left context).** The immediate left context is banked `46="que"` (@1744). "que" as subordinator demands a finite verb — fork A supplies exactly that: "que [56]e-ent" = "que" + 3pl finite verb ("ils Xent", Xéent-class: cf. "créent", "agréent"), which parses with zero contradiction under standing values (46=que banked, 40=e banked, 06=ent promoted, 56 verb-stem). The left context therefore actively selects the verb-stem fork: only fork A gives the "que"-clause its verb.
- **C2 — PASS (fork B excluded).** Fork B requires `56 40` to be an "e"-final non-verb word with `06` as a separate syllable. Three independent failures:
  1. `06` stranded or standalone is unlicensed: `06` is bound stream-wide (never word-initial); standalone "ent" is not a French word; rightward fusion "ent"+65 has no license (65 is a free noun-class word, R18) and inventing "entX" violates §3.
  2. Naming `56 40` non-verb is invention: 56's class is battery-promoted verb at 22/23 windows (w5-pas-verb; form-56-1627 3sg finite). A noun/verb class alternation for 56 needs red-team declaration under §7.
  3. The "que"-clause goes verbless: "que [Xe nominal]" leaves no finite verb in the clause — ungrammatical.

## Verdict: PROMOTE (fork A)

The left context supports **fork A**: the `56 40` unit is a vowel-final verb stem ("Xé"), and `06` is the finite 3pl ending → "Xéent"-shaped ("créent"-class). Fork B is excluded at battery grade. Scope is this window only: 56's value stays open (the Xéent family: créer, agréer, suppléer, recréer, gréer, dégréer, procréer, maugréer), and the stem-vs-whole alternation for 56 (bare-56 whole at 22 windows vs stem-56 here) remains §7 red-team venue — no polyvalence is declared here.

## Caveats (stated, not hidden)

- The subject of the 3pl verb is still missing (French does not pro-drop): `rightedge-56-1745` C3 fenced this as red-team-owned ("ne m que" strain @1742-1744; subject must be found left of @1744 or right of @1747). The fork decision does not depend on it.
- `65`'s value is open (class noun, R18); `48`/`12` at @1736-1737 are open; the "94 82 46" = "ne m que" leftward residual is fenced (ni-1740-1742), inherited status.
- Canonical-stream caveat stands (row a8_08 offset unvalidated).

## Follow-ups

None required for a promote (protocol §4). Forced next steps are already owned: the 3pl subject search (`rightedge-56-1745` C3, red-team venue) and 56's value naming (queued Xéent-family targets).

## Bookkeeping

- Queue: `stem-40-06-1748` → status `verdict`, result `promote`, 2026-10-09 (pre-write assert passed — was `queued`/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/stem-40-06-1748.lock` created on start, deleted on completion (verified gone).
