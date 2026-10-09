# Battery `syll-52-locus-1334` — locus-only syllable-composition test

- Target id: `syll-52-locus-1334` (priority 3)
- Date: 2026-10-09
- Worker session: e62db497-7d32-4752-b1b2-fd181f354b38
- Lock: `code/crowd17/next-token/locks/syll-52-locus-1334.lock` (created 2026-10-09T11:28:23Z, deleted on completion)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; 1,847 pairs / 96 types re-derived in-session, asserts hold). `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Offset convention: this report uses **1-based** @-offsets like the parent battery (target's "@1334" = 1-based index of 39; 0-based @1333). 0-based equivalents stated where material.

Terms (ASD-STE100): "syllable" = a sound block inside a word ("scri", "ser", "voi"). "word-internal" = inside one word (not a word by itself). "locus" = the single cipher position under test. "precedent" = a standing battery verdict used as a rule. "orphan" = a window where a value leaves a non-word (stem-56-whole nameability standard). "uniformity" = the default that one group has one sound value everywhere.

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"Name the surviving subset with the wordinternal-battery-family precedent cited per exclusion; kill a candidate iff a precedent excludes it at this locus."

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** For each candidate in {scri, ser, voi}, every wordinternal-battery-family precedent is checked for locus-level exclusion at @1334; each exclusion cites the precedent.
2. **C2:** A candidate is KILLED iff a precedent excludes it at this locus at kill grade (forces 52 ≠ that syllable here, or demonstrates a cleaner rival on this exact frame).
3. **C3:** The surviving subset is named explicitly (possibly the full set, possibly empty, with the consequence stated).

Parent context (adopted, not re-litigated): `profile-52-host-word` NULL (2026-10-09) — three-way tie among "prescrira de" (52='scri'), "préserva de" (52='ser'), "prévoira de" (52='voi') + INF at @1334; tie unbreakable stream-wide; this battery narrows to the single locus. `seg-528294-word` PROMOTE (2026-10-09) — "52 82 94" = "amne..." word-unit with 52="a" as the single new assumption, C2 compatibility-tested across all 27 windows of 52. `de83-39-1334` PROMOTE — conditional collision matrix ("a de [INF]"/"à de [INF]" ungrammatical iff 39='a/à' AND 83='de' ratify). `a-39` PROMOTE — 39 = /a/ (word "a"/"à" or word-internal 'a').

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/syll-52-locus-1334.lock` on start; deleted on completion.
2. Re-derived the repaired stream in-session (1,847 pairs, 96 types; n(52)=27 verified).
3. Byte-confirmed the locus: 1-based @1332=70('pre'), @1333=52, @1334=39('a'), @1335=83('de'-lead), @1336=86(INF-class) — 0-based @1331–@1335, rows a7_04/a7_05 (70 last of a7_04; 52 first of a7_05). "70-52" and "52-39" each exactly 1x stream-wide (hapaxes). Left: 1-based @1328=06('ent'), @1329=62, @1330=131=94('ne'), @1331=30('pas').
4. Surveyed the wordinternal-battery-family verdicts for precedents bearing on 52's phonetic value or the "pre[52]a" composition: wordinternal-37-01, stem-56-whole, stem-03 (+nounfamily, +value), stem-85 (+then-1700), stem-86, stem-44-nominal, stem-44-1839, stem-42-verb, stem-62-ent-665-1536, stem-68-id, stem-14-id, stem-14-84-retest, en43-wordinternal-census, er89-wordinternal-govern, erstem-33-id, qui-94-syllabic-rival, sub02-wordinternal, prefix-08-31, a-39, seg-528294-word, seg-52-80-unit, seg-52-86-unit, unit-52-37-name, adj-52-37-value, ne52inf-adverb, leftedge-52-86-1736.
5. Checked the "ne" @1330's right context for "pas"(30)/"que"(46) completers (±50): nearest 30 is @1368 (0-based), which belongs to the local "[60] [03] pas [82]" clause, not to 94@1330; no 46 in range. The "ne" is bare (no pas/que partner) — confirms the parent's finding; strains all three finite candidates equally, discriminates none.

## Window-level evidence

The locus (1-based @1326–@1340, 0-based @1325–@1339):
`98 56 30(pas) 06(ent) 62 94(ne) 70(pre) | 52 39 83 86 71 64(qui) 60 08 65`
= "…[56] pas [06] [62] ne pre[52]a de [86-INF] [71] qui [60]…"

Candidate parses (all with 83='de'-lead, 86 INF-class — adopted, not re-litigated):
- 52='scri' → "ne prescrira de [86-INF]" (fut. 3sg, prescrire; "prescrire de + INF" vetted by parent)
- 52='ser' → "ne préserva de [86-INF]" (passé simple 3sg, préserver; "préserver de + INF" vetted by parent)
- 52='voi' → "ne prévoira de [86-INF]" (fut. 3sg, prévoir; "prévoir de + INF" vetted by parent)

### Precedent survey (per-candidate exclusion check)

**P1 — seg-528294-word PROMOTE (52="a", "amne..." word-unit).** The only wordinternal precedent naming 52's phonetic value. Exclusion argument tested: 52="a" + syllabary-uniformity default → 52 ≠ {scri,ser,voi} everywhere incl. @1334. REJECTED at kill grade, three independent grounds:
  (a) 52="a" is compatible-not-forced: C2 tested compatibility across 27 windows (zero forced contradictions), not forcing; the lane's naming standard needs FORCED (stem-03-value precedent, via ne52inf-adverb).
  (b) The promotion is scoped ("word-unit only") and conditional on the fenced red-team 94 ruling at the trigram windows (A1: if 94 is the negator there, the "amne..." reading dies on re-read).
  (c) At THIS locus, 52="a" does not demonstrate a cleaner rival parse — it parses worse: "pre"+"a"+"a" = "préaa" is not French (if 39 word-internal), and 39-as-separate-word gives "a de [INF]"/"à de [INF]", ungrammatical per de83-39-1334's own matrix. Under the stem-56-whole nameability standard, @1334 is an ORPHAN of the 52="a" status (strands a non-word), while 'scri'/'ser'/'voi' each yield a clean French word. A precedent that orphans the locus cannot exclude the candidates that parse it cleanly.
  → P1 excludes none of {scri, ser, voi} at @1334. (Recorded tension, not adjudicated: 52="a" uniformity vs the locus parse — see follow-up 1.)

**P2 — the 52-37 conditional (unit-52-37-name NULL → adj-52-37-value-rerun QUEUED).** Would kill all three via uniformity IF 52-37 resolves to "même"/"seule" (52='mê'/'seu'). The antecedent is QUEUED, not a verdict — not a precedent. Cannot fire. (Parent's own decider, adopted.)

**P3 — ne52inf-adverb NULL / leftedge-52-86-1736 NULL.** Concern 52 as a whole word in "ne [52] [INF]" frames; the {plus, jamais} tie and the §7 adverb/adjective tension show 52 resists uniform whole-word naming, but neither battery constrains 52's word-internal syllable value at @1334. No exclusion.

**P4 — wordinternal-37-01** ("satisfait"/"contrefait" finite-verb compounds). Precedent shape: word-internal composition can yield a finite verb — SUPPORTS the candidates' shape (finite "pre[52]a"), excludes none.

**P5 — stem-56-whole, stem-03, stem-85, stem-86, stem-44, stem-42, stem-62-ent, stem-68, stem-14, en43, er89, erstem-33, sub02, prefix-08-31, qui-94-syllabic-rival.** All concern other cells' stem/whole status; none names or constrains 52's syllable. No exclusion.

**P6 — a-39 PROMOTE (39=/a/ word-internal licit).** Licenses the 'a' in "pre[52]a" as word-internal — SUPPORTS the composition frame, excludes none.

**P7 — seg-52-80-unit KILL, seg-52-86-unit KILL** ("52-80"/"52-86" one-word units dead; 52 is a free word). These kill 52-as-bound-prefix readings at @1294/@1738 — a different locus and a different composition direction. At @1334 the claim is 52 word-INTERNAL (medial syllable), not prefixal; P7 does not bear on it. No exclusion. (Noted: the free-word-52 finding is in mild tension with any word-internal-52 reading, but §7 bars only polyvalence of VALUE, and the parent already scoped this battery locus-only precisely to avoid the uniformity burden.)

**Candidate-specific checks:** no precedent selects tense (future "prescrira"/"prévoira" vs passé simple "préserva") at this locus — no selector in the window; no precedent selects among the three de+INF governments (parent vetted all three viable; not re-litigated). The bare-"ne" strain (no pas/que partner within ±50) applies identically to all three.

## Per-clause pass/fail

- **C1 — PASS.** All wordinternal-family precedents surveyed; each checked against @1334 with the exclusion logic stated above.
- **C2 — no kill fires.** No precedent excludes any of {scri, ser, voi} at this locus at kill grade. P1 (52="a") is the nearest miss and fails on three independent grounds (compatible-not-forced; scoped + 94-conditional; orphans the locus rather than parsing it cleaner). P2 is queued, not a precedent. P3–P7 do not bear on the locus.
- **C3 — surviving subset: {scri, ser, voi}** (full set). The parent's three-way tie stands unbroken by the wordinternal-battery family.

## Verdict: NULL

No wordinternal-battery precedent excludes 'scri', 'ser', or 'voi' at the @1334 locus. The three-way tie among "prescrira" / "préserva" / "prévoira" (+ "de" + INF) survives this battery. New material vs. the parent: (1) the exclusion survey is now explicit and on record per candidate; (2) the 52="a" uniformity threat is defused at kill grade but its locus-orphan tension is recorded (follow-up 1); (3) the bare-"ne" at @1330 is confirmed partnerless within ±50 (nearest 30='pas' @1368 belongs to the "[60] [03] pas" clause), so the expletive/distant-"ne" strain is locus-factual, not assumed.

No standing or red-team verdict contradicted or downgraded (seg-528294-word's PROMOTE stands untouched — this battery only declines to extend 52="a" to @1334 via uniformity; profile-52-host-word's NULL stands un-narrowed); §7 intact; canonical-stream caveat stands (rows a7_04/a7_05 unvalidated; the "70-52-39" trigram straddles the row boundary per the parent).

## Follow-ups proposed (null regenerates work; all verified ABSENT from battery-queue.json)

1. **`unif-52a-1334-orphan`** (P3) — A10-orphan test: apply the stem-56-whole nameability standard to 52="a" at @1334 ("preaa" non-word; "a de [INF]" ungrammatical per de83-39-1334). Bar: orphan confirmed iff the status strands a non-word under standing values; then fence the uniformity extension of 52="a" to @1334 (escalate the 52="a"-vs-syllable tension to the red team if the global orphan rate otherwise holds).
2. **`ne-1330-bare-corpus`** (P3) — corpus check: bare "ne" + finite verb with no "pas"/"que"/"point" partner in 1841 main clauses — attested or absent? Bar: ≥1 genuine main-clause attestation keeps the finite-verb reading unstrained; confirmed zero across the lane's period corpora kills the finite-verb arm at @1334 (all three candidates die together; the word-internal-39 reading dies with them).
3. **`subj-62-1329-agree`** (P3) — name 62 at @1329 (the "ne pre[52]a" subject slot). Bar: if 62 names plural, all three 3sg candidates die by agreement (fence, not kill, pending 62's own standing); if 62='il' (battery-promoted) holds, the 3sg agreement leg is banked for the surviving subset.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-syll-52-locus-1334.md`
- Queue: `syll-52-locus-1334` → status `verdict`, result `null`, date 2026-10-09 (pre-write assert passed — was `queued`/verdictless; temp-file + rename; JSON re-validated post-write; own entry only; no downgrade)
- Lock `locks/syll-52-locus-1334.lock` created on start, deleted on completion (verified gone)
- `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
