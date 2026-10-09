# Battery `nom-97-526-adverb` — verdict: PROMOTE

## Bar (verbatim, pre-registered)

> "class named at battery grade"

Restated as numbered pass/fail clauses (before testing):
- **C1:** 81's class at the @526 window (0-based @524) is named — nominal vs adverbial decided — with battery-grade evidence.
- **C2:** the consequence of the naming for the 97 INF/NOM tiebreak at @526 is stated (the "Partir, c'est…" infinitive-topic revival condition met or unmet).

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
(parsed like `code/side-keyhunt/repair_parse.py`); asserts held
(1847 pairs, 96 types). `canonical.py` never used.

Adopted standing values, including post-R19 law: R19-123 (noun-81 class
promote FENCED; "le [81]" ×3 frames granted as findings; @1096
"[81]ent" 3pl hostile window fenced, red-team venue), R24 (24 =
finite/modal unless follower=85), R19-045 (43 = noun class).
81="prin" value kill (§7) adopted, not re-litigated (value, not class).

Offset note: the parent battery (`battery-val-97-verb-test.md`) uses
1-based cell indices; its "@526" names the 97 focal cell. The 81 cell at
that window is 1-based @525 = **0-based @524**, row a3_00. All @-offsets
below are 0-based unless marked 1b.

## Window-level evidence (all byte-exact on the repaired stream)

**Locus:** 0b@520–528, row a3_00:
`91 77 06 55 [81] 97 47 44 59`
= "…[91] le(77,prov) ent(06,prom) [55] [81] [97] ce(47,prom)
[44] est(59,prov)". The @526 window per the parent: `81 [97] 47 44 59
37 64` = "[81] [97] ce [44] est [37]".

**81 census (0-based): n=14** — @26, @44, @93, @524, @551, @745, @1086,
@1095, @1241, @1402, @1513, @1593, @1599, @1672.
Predecessors: 55×6, 77×4, 43×1, 98×1, 39×1, 08×1.
Successors: 00×3, 97×2, 87×2, 30/85/06/88/03/82/92 ×1.
10/14 windows sit after determiner-position cells (55×6, 77×4).

**55 (the @524 predecessor):** n=12; successors 81×6, 61×3, 83×2, 68×1.
Registry null (unvalued). "55 61" ×3 = "prend" word-internal (standing
PROMOTE `seg-55-61-21-stem`) — 55's determiner reading is ungranted;
stated caveat, red-team venue.

**The adverbial arm at @524:**
- In 1841 French an adverb cannot directly follow a determiner. At @524,
81 follows 55, the head of the uniform "55 81" ×6 collocation.
- Stream-wide, adverbial-81 has zero license. The only positionally
non-determiner windows: @44 ("[43-noun] [81] pas" — adverb between noun
and "pas" is ungrammatical), @93 ("98=verb [81] 97 46" — no clean
adverbial frame), @1593 ("08 [81] 03=verb-stem" — 08 is a letter-cell, so
this is a word-boundary question, red-team venue per the noun-81
battery's 11-vs-1 segmentation flag). None licenses adverbial-81.
- The val-97-verb-test parent made the INF-topic reading ("Partir,
c'est…"-shaped dislocated infinitive) conditional on adverbial-81 and
judged it "strained" — the condition was never licensed.

**The nominal arm at @524:**
- "[81] [97-noun]" appositive NP + "ce [44] est [37]" copula clause —
the parent battery judged this parse "clean" (NOM favored at @526).
- Consistent with the red-team-granted "le [81]" ×3 frames (R19-123)
and the 10/14 determiner-predecessor population.

**Verbal-81 at @524:** dead — finite-verb 81 needs a subject and
agreement; none present. (The verbal arm lives only at @1096,
"[81]ent" 3pl, a different window, fenced hostile per R19-123.)

## Per-clause pass/fail

- **C1 PASS:** 81's class at @524 is named **NOMINAL** at battery grade.
Adverbial-81 is unlicensed at this window (determiner-position
predecessor; zero stream-wide license); verbal-81 is unlicensed at this
window (no subject/agreement); nominal is the only licensed parse
("[81] [97-noun]" appositive NP + copula). Scope: window-level only
(see below).
- **C2 PASS:** adverbial-81 dead at @524 → the infinitive-topic reading's
revival condition fails → the INF leg at @526 stays strained (it never
reaches "clean") → **NOM-97 is hardened at @526**. The global 97
INF/NOM tie survives via the four "pour [97]" windows (@3/@289/@589/
@1824); only this window's INF leg is closed.

## Verdict: PROMOTE

81 = nominal at the @526 window (0b@524), battery grade. The
"Partir, c'est…" infinitive-topic revival route is closed at this
window; NOM-97 hardened.

## Scope and caveats (stated, not ignored)

- **Window-level only.** No registry change; 81 stays unvalued in the
registry. This is a parse-premise finding, not a class promote.
- **R19-123 untouched:** the red team's global noun-81 class fence
stands. A window-level nominal finding is consistent with it — R19-123
itself granted the "le [81]" ×3 frames as window-level findings. The
global class question remains red-team venue.
- **@1096 untouched:** the "[81]ent" 3pl hostile window is a different
window and stays fenced (red-team venue). No polyvalence declared;
§7 intact (67 sole polyvalence).
- **55 caveat:** the "55 81" determiner reading loads on unvalued 55,
and 55 has a demonstrated word-internal use ("prend", "55 61" ×3).
The naming rests on the collocation's uniformity (×6), the 10/14
determiner-predecessor population, and the zero adverbial license —
not on a granted 55 value. 55's class is red-team venue.
- Canonical-stream caveat stands (row a3_00 offsets unvalidated).

## Follow-ups

None required (promote per §4). Natural continuations already live
elsewhere: 55's class (red-team venue), @1096 verbal-81 (R19-123
fenced), 77="le" resolution (R20 open call, load-bearing for the
"le [81]" frames).

## Bookkeeping

- Queue: `nom-97-526-adverb` → `status: verdict`, `result: promote`,
2026-10-09 (pre-write assert passed — was queued/verdictless;
temp-file + rename; JSON re-validated from disk; own entry only; no
downgrade).
- Lock created on start (2026-10-09T12:50:40Z), deleted on completion
(verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
No standing/red-team verdict contradicted or downgraded.
