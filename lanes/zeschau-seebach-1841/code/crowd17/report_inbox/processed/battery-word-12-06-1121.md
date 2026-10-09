# Battery report: word-12-06-1121 — identify the word containing "12-06" @1119/@1708

Worker: 3cc6f45e-4a07-48d0-8b2c-533b29515612 | 2026-10-09T17:35Z–17:45Z
Target: `word-12-06-1121` (priority 3). Lock `locks/word-12-06-1121.lock`
created on start (agent id + UTC timestamp), deleted on completion. No prior
lock existed. Parent: ent-06-host-census PROMOTE (residual gates §1).

## Bar (verbatim, pre-registered)

"state the word or fence as a hard residual with the failure stated"

Numbered clauses (fixed before testing):
- C1: The French word containing the "12 06" bigram is stated at @1119
  (0-based; target's "@1121" = bigram start + 2) with byte evidence, parsing
  under standing values with no ungranted assumption. PASS iff named.
- C2: Same at @1708 (target's "@1710" = bigram start + 2). PASS iff named.
- C3 (else): The locus is fenced as a hard residual with the failure stated:
  every boundary alternative is shown to yield a non-word or to depend on a
  kill-grade-dead license. PASS iff the fence is complete.

## Method

Repaired 1,847-pair / 96-type stream only:
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed per `code/side-keyhunt/repair_parse.py` (1,847 pairs, 96 types
re-asserted in-session; `canonical.py` never used). R5005 untouched.
@-offsets are 0-indexed pair positions (queue convention). Standing values:
11=la, 70=pre, 82=m, 34=i, 29=er, 40=e (pencil GT); 12="n" PROMOTED letter
tier (R17-002); 06="ent" promoted (ent-06); 30=pas, 00=pour (promoted);
59=est, 77=le (provisional). 1841 diplomatic French throughout.

"12 06" bigrams re-derived stream-wide: exactly 2 — @1119 (row a6_07:
`11 88 70 12 06 14 06`) and @1708 (row a8_06:
`94 88 26 12 06 29 40`). The target's @1121/@1710 are bigram-start + 2
(the 06 is at 0-based @1120/@1709); the loci are unambiguous.

Corpus: 57 French files under `code/side-period/corpus/` (German
allgemeine-zeitung/adb-zeschau/metternich files excluded), accent-sensitive
whole-word counts.

## Window evidence

### Locus 1 — @1119, row a6_07

Full local surface @1113–1129:
`38 30 69 11 88 70 [12 06] 14 06 11 52 37 43 00 86 52`
Under standing values:
`[38] pas [69] la [88] pre-n-ent [14]-ent la [52] [37] [43] pour [86] [52]`

The word containing "12 06" has the surface shape "70 12 06" =
"pre"+"n"+"ent" = **"prenent"**.

- Corpus: "prenent" = **0/57 files** — not a French word.
- The only French word it resembles is "prennent" (108/57 files), which
  requires TWO licenses, both kill-grade dead:
  1. Clerk single-n spelling ("prennent" written with one n): KILLED at
     kill grade (spell-pasent-test; spell-single-consonant null — the clerk
     writes the doubled n in "prenne").
  2. Plural subject agreement ("la [88]" as plural NP): KILLED at kill
     grade (prennent-70-12-06 — banked singular 11="la" cannot head a
     plural NP; no plural-NP reading of "11 88" is grammatical).
- Boundary alternatives, all dead:
  - "pre | nent": "nent" is not a French word (corpus "nent" hits are
    line-break hyphenation artifacts: "soutien-nent", "don-nent" — verified
    by context inspection).
  - "pren | ent": same "prenent" non-word.
  - 12 word-final + 06 word-initial ("pren" | "ent[14]…"): "pren" is not a
    French word; the "ent[14]" ("souvent"-shaped) parse is breaker-b4-1121's
    window-local null, not a naming of the "12-06" word.
  - Left extension over 88 ("[88]prenent"): 88's value is open; every
    French "-prenent" word ("reprennent", "comprennent") doubles the n —
    the single-n defect is independent of 88. DEAD by the same kill.
- French 3pl -ent verbs with n-final stems (prennent, viennent, tiennent,
  deviennent, reviennent, souviennent, appartiennent, contiennent,
  retiennent, obtiennent, maintiennent, soutiennent) ALL double the n.
  No single-n "pren-" stem takes -ent in French.

### Locus 2 — @1708, row a8_06

Full local surface @1702–1718:
`30 20 62 94 88 26 [12 06] 29 40 65 94 44 59 30 64 47`
Under standing values:
`pas [20] [62] ne(lead) [88] [26] n-ent-er-e [65] ne(lead) [44] est(prov)
pas qui ce`

- "12 06 29 40" = "n"+"ent"+"er"+"e" = **"nentere"**: 0/57 files — not a
  French word.
- Boundary alternatives, all dead:
  - "12 | 06 29 40": "n" + "entere" — "entere" 0/57 files, non-word.
  - "12 06 | 29 40": "nent" + "ere" — "nent" non-word (hyphenation
    artifacts only); "29 40" as "ère" (73/57 files) is a real word but
    leaves "nent" unparsed.
  - "12 06 29 | 40": "nenter" + "e" — "nenter" non-word.
  - "26 12 | 06 29 40": "[26]n" + "entere" — non-word.
  - "26 | 12 06 29 40": "[26]" + "nentere" — non-word.
  - "26 12 06 | 29 40": "[26]nent" + "ere" — "[26]nent" is a coherent
    3pl-verb word-shape ("viennent"-shaped) IFF 26 is a verb stem; 26's
    class is open (n=17; followers 12x4/30x4/00x3; noun26 batteries lean
    noun-class). LIVE fork but unnameable — fenced downstream of 26's
    class (follow-up 1).
  - "06 29" = "enter": not French ("enterrer" needs double r; 29="er" is
    pencil GT, single).
- The ent-06-host-census fence ("wordbound's mechanism leg only") is
  confirmed, not re-litigated.

## Per-clause pass/fail

- C1 (name the word @1119): FAIL. The surface word-shape is "prenent", a
  corpus-attested non-word; both rescue licenses are kill-grade dead; no
  alternative boundary yields a French word.
- C2 (name the word @1708): FAIL. "nentere"-shaped; every boundary
  alternative is a non-word except the "[26]nent" 3pl-verb shape, which is
  unnameable while 26's class is open.
- C3 (fence as hard residual with failure stated): PASS at both loci.
  Locus 1 failure: "prenent" is one 'n' short of "prennent", and the
  single-n license plus the plural-subject license are both kill-grade
  dead — the residual is a defective verb surface with no live reading.
  Locus 2 failure: "nentere" is not a French word under any boundary;
  the only coherent word-shape ("[26]nent", 3pl verb) is gated on 26's
  open class.

No standing or red-team verdict is contradicted or downgraded: the
breaker-b4-1121 null (window-local "souvent" parse, 14="sou" killed
globally), the prennent-70-12-06 kill, and the ent-06-host-census fences
are all cited, not re-litigated. §7 intact (no polyvalence invoked).

## Verdict

**null.** Neither "12-06" word can be identified as a French word under
standing values. Both loci are fenced as hard residuals with the failures
stated above.

## Follow-ups (per §4; all IDs verified absent from battery-queue.json)

1. `stem-26-nent-verb` (P3): decide 26's class at @1707 via its 17-window
   distributional profile (followers 12x4/30x4/00x3; predecessors 69x3/11x2/
   64x2/24x2). The "[26]nent" 3pl-verb word-shape at @1707–1709
   ("viennent"-shaped) is live iff 26 is verb-stem-class; kill the verb
   fork on the profile if 26 is noun-class. Bar: 26 takes a verb-stem value
   making "[26]n-ent" a grammatical 3pl French verb, or the fork is killed
   on 26's distributional profile.
2. `word-12-06-84-control` (P4): the other "[14]ent" locus @84
   ("16 14 06 88") as a control on the "12-06"-free "ent"-adverb shape;
   tests whether the @1119 "prenent" defect is locus-specific or part of a
   wider defective-verb-surface pattern. Bar: state the control's reading
   or fence it with cause.
3. `seg-88-70-1119-left` (P4): test the left word boundary at @1117–1118
   ("88 70"): 88 word-internal in a "[88]pre…"-shaped word vs word boundary
   before 70="pre". 88's class is open; a word-internal 88 does not rescue
   the single-n defect (all "-prenent" words double the n), so this is a
   boundary-hygiene target only. Bar: boundary stated with the 88-class
   dependence made explicit, or fenced.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-word-12-06-1121.md`
- Queue: `word-12-06-1121` queued → verdict/null (own entry only,
  temp-file + rename; pre-write assert confirmed queued/verdictless; JSON
  re-validated post-write; no downgrade; no other entries touched).
- Lock `locks/word-12-06-1121.lock` created on start, deleted on
  completion. R5005, sealed gates, and the red-team adjudication queue
  untouched.
