# Battery report: split-38de-redteam-input

- Target id: `split-38de-redteam-input` (priority 2, gather-only)
- Claim: "Package the section-7 split evidence (verb-form uniform 38 x6 windows vs sub-lexical 38 at @1828) for red-team adjudication."
- Date: 2026-10-09
- Worker: battery worker (subagent e3223e4f-6a7b-4fb2-9421-fd756beec362)

## Bar (verbatim, pre-registered before testing)

"package delivered; no battery-level split declaration"

Numbered pass/fail clauses (restated before testing, not modified after):

- **C1:** The §7 split evidence package is delivered — verb-form uniform 38 evidence for the six non-@1828 windows AND sub-lexical 38 evidence at @1828, with stated sources, loci, and conditions.
- **C2:** No battery-level split declaration is made — no class named, no value named, no adjudication performed.

## Method

Read BATTERY-PROTOCOL.md first. Re-derived the repaired stream in-session from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (parsed
like `code/side-keyhunt/repair_parse.py`): 1,847 pairs / 96 types confirmed.
n(38)=7, byte-confirmed at 0-based @384/@826/@1113/@1343/@1469/@1650/@1828.
`canonical.py` never used. R5005, sealed gate instances, red-team adjudication
queue untouched. No invented data; every number below traces to the stream.

All battery evidence below is ADOPTED (never re-litigated); each key locus was
independently spot-checked at the byte level. Standing premises per
BATTERY-PROTOCOL.md §7. Parent: battery-noun-38de-1829-host (NULL, 2026-10-09)
proposed this package as its follow-up #2; its follow-up #1 (bare-subj-corpus,
PROMOTE, 2026-10-09) and #3 (val-16-1832-class, queued P4) are the live
companions.

## Package: Arm A — verb-form uniform 38 at the six non-@1828 windows

**Source battery:** `noun26-38-profile` (PROMOTE, 2026-10-09). Standing:
38 = verb-form, UNIFORM class. Distribution of the seven windows:

| Window | @ | Context | Leg |
|---|---|---|---|
| W1 | @384 (a2_07) | `16 52 [38] 37 43` | Indeterminate (52/37 classes open); verb-form uncontradicted |
| W2 | @826 (a5_06) | `87 59 [38] 82 01 24` = "ce est [38] m [01] [24]" | Verb-form leg: past participle ("c'est [pp]"-shaped; conditional on provisional 59='est') |
| W3 | @1113 (a6_07) | `65 [38] 30 69 11 88` = "[65-noun] [38] pas cela [88]" | Verb-form leg: finite 3sg at KILL GRADE ("[65] [38-V] pas cela"; 65 noun-class R18-001 ratified; 69-11="cela" locus-level) |
| W4 | @1343 (a7_05) | `64 52 [38] 47 86` = "qui [52] [38] ce [86-INF]" | Fenced with stated cause (`adj-38-w4-parse` KILL: verb-38 strands on "ce [86-INF]"; predicative-38 strands "qui" verbless). No class forced. |
| W5 | @1469 (a7_09) | `62 [38] 26 12 41` | Verb-form leg: modal ("ne peut [inf]"-shaped) |
| W6 | @1650 (a8_04) | `03 [38] 82 16` = "[03] [38-V-fin] me [16-inf]" | Verb-form leg: finite governor ("veut me voir"-shaped; conditional on 03-nominal, 16-infinitive, both battery grade) |

**No window forces non-verbal 38.** The finite/participle/modal distribution is
inflectional (one verb lexeme in different forms), not a polyvalence — §7 intact
(67 et/veut remains the sole true polyvalence).

**Value narrowing (two NULL batteries):** `val-38-verb` and `val-38-vouloir-devoir`
(2026-10-09) narrow 38's verb value to a symmetric {"vouloir" (veut/voulu),
"devoir" (doit/dû)} 2-way tie, unbreakable at battery grade; `syll-38-value-census`
(NULL) confirms the tie is symmetric across all four legs. 38's spelling value is
open: zero battery-grade spelling evidence — no 29='er' contact at any of the 7
windows (verified in-session: 29 is 0× adjacent to 38 stream-wide).

**Unit hypothesis killed:** `val-52-38-unit` (KILL, 2026-10-09) rejects '52 38' as
a prenominal-adjective unit at kill grade (@1343); W1's unit parse is
conditional-only. 38 is not a compositional partner at @384/@1343.

## Package: Arm B — sub-lexical 38 at @1828

**Locus byte-verified in-session:** @1825=86 @1826=29('er') @1827=82('m')
@1828=38 @1829=83 @1830=24 @1831=82('m') @1832=16 @1833=59 — row a8_11.
Core: `82 [38] 83 24` = "m [38] [83] [24-finite]".

**The "38 83" contact is a stream hapax** (verified in-session: exactly 1 of
1,846 bigrams; the sub-lexical fork lives or dies at @1828 alone).

**Sub-lexical reading:** 38 as a syllable inside a "-de"-final word, i.e.
"m[38]de" = "m" + [38] + "de". Candidate spellings (all underdetermined):
"monde" (38="on"/"mon"), "garde" (38="gar"), "demande" (38="deman"), "aide"
(38="ai"), "mode" (38="mo"), "corde" (38="cor"), "bande" (38="ban").
**No window discriminates among them** — naming any one would be arbitrary
(lane precedent: masc-noun-86-name). 38's open spelling value blocks C1 of the
noun-naming bar.

**Dependent premises:**
- 83 as syllabic 'de': `syll-83-de-1829` (NULL, 2026-10-09) — the '-de'-final
  VERB fork is fenced at KILL GRADE (finite+finite adjacency ungrammatical);
  the '-de'-final NOUN fork survives as a live residual. 83='de' is LEAD.
- `noun-38de-1829-host` (NULL, 2026-10-09): the noun fork is FENCED with two
  independent causes —
  - **(a) Determiner absence (grammatical):** the -de host word has no determiner
    (@1827=82 is a pencil-GT letter, not a determiner; "m'"+noun ungrammatical).
    The BARE COMMON-NOUN fork is dead.
  - **(b) §7 block (structural):** sub-lexical 38 contradicts 38's promoted
    uniform verb-form class (6/7 windows verb-shaped); licensing it requires
    the split decision that is red-team venue.
- `bare-subj-corpus` (PROMOTE, 2026-10-09): corpus census, 61M chars of 1841
  French — **77 genuine attestations of bare -de-final PROPER NOUNS as
  finite-verb subjects** ("Aristide avait pris" x17, "Mathilde est l'exemple"
  x4, "M. Baude a essayé" x6); **zero bare common-noun attestations.**
  The PROPER-NOUN fork is licensed at grammaticality grade only. For @1828 to
  use it, "[38]de" would need to be a proper noun — a VALUE claim 38's open
  spelling value cannot support.
- `syll-38-value-census` (NULL): W7 @1828 is fenced for the verb class under
  EVERY live 83-branch (83-fork-independent): finite-38 gives double finite
  verbs; infinitive-38 gives stacked infinitives then finite 24; participle-38
  has no auxiliary. So @1828 parses under NEITHER the uniform-verb reading NOR
  the named-noun reading at battery grade — it is a live residual in both
  directions.

## The split shape for red-team adjudication

The evidence presents the classic §7 conditioned-split shape, parallel to
poly-66-split and the 09 nominal/adverbial package:

- **Arm A:** verb-form 38 — 4 positive legs (past participle @826, finite 3sg
  @1113 kill-grade, modal @1469, finite governor @1650 conditional), 1
  indeterminate (@384), 1 fenced-but-class-open (@1343), zero non-verbal
  legs. Value narrowed to {vouloir, devoir}, spelling value open.
- **Arm B:** sub-lexical 38 — only at @1828 (stream hapax "38 83"); common-noun
  fork dead (determiner absence + zero corpus attestations); proper-noun fork
  grammatically licensed but needs a named value 38 cannot supply; uniform-verb
  parse at @1828 independently fenced.

**Adjudication options (for the red team, not the battery):**
1. Declared §7 split: verb-form 38 at the six windows, sub-lexical syllable 38
   at @1828 (within a "-de"-final word whose exact spelling stays open or
   takes the proper-noun fork).
2. Reject the sub-lexical reading: 38 stays uniform verb-form; @1828 is a
   segmentation residual (both directions fenced at battery grade).
3. Keep fenced: the proper-noun fork is grammatically licensed but unnameable;
   the split question waits on 38's spelling value or a red-team tie-break
   between the two directions.

**Relevant queued/next-step targets (coordinator owns):** noun-38de-premise-reconcile
(queued P4), val-16-1832-class (queued P4, parent's follow-up #3), w1-38-384-reread
(queued P4), w4-38-1343-revisit (queued P4), homophone-38-67-veut (queued P4,
gated on a "vouloir" naming), val-38-corpus-modal-owe (queued P4),
val-38-que-signature-widen (queued P3). No new follow-ups proposed here per the
gather-only precedent (the docket owns the next step; the parent's follow-up
list already covers the open paths).

## Per-clause pass/fail

- **C1 — PASS.** The package is delivered: Arm A (verb-form uniform evidence,
  six windows, with legs/fences/indeterminate stated), Arm B (sub-lexical @1828
  evidence, hapax verified, both fork dispositions, dependent premises with
  verdict citations), and the split shape with adjudication options — all above.
- **C2 — PASS.** No battery-level split declaration made: no class named, no
  value named, no option selected among the three adjudication options; §7 intact.

## Verdict: NULL (gather-only package delivered)

No bankable content added beyond the record. No standing battery or red-team
verdict contradicted, downgraded, or re-litigated. No red-team verdict exists
on 38 (verified: R20's only 38-adjacent text is R20-135's @1115 context
re-derivation, which does not rule on 38). §7 intact — one verb lexeme in
inflected forms is inflectional, not polyvalence. Canonical-stream caveat
stands (68 of 70 upstream row offsets unvalidated; all @-offsets 0-based
repaired-stream).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-split-38de-redteam-input.md`
- Queue: `split-38de-redteam-input` queued → `verdict`/`null`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; target-id-unique temp
  file `battery-queue.json.split-38de-redteam-input.tmp` + atomic rename;
  disk re-validated; own entry only; no downgrade; no tmp leftover).
- Lock `locks/split-38de-redteam-input.lock`: created on start
  (agent e3223e4f-6a7b-4fb2-9421-fd756beec362, 2026-10-09T20:15:00Z, no stale
  lock), deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
