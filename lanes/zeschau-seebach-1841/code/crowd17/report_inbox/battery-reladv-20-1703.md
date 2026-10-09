# Battery verdict: reladv-20-1703

**Verdict: PROMOTE** (relative-adverb reading named at battery grade, locus-level).

## Target

- id: `reladv-20-1703` (priority 3)
- claim: "test 20 as the relative-adverb subclass ('où'/'quand'/'comment') that confined 'n'importe' uniquely licenses"
- Parent: `adverb-20-wide` NULL (2026-10-09) — follow-up 2 of 3.
- adverses: none listed.

## Bar (verbatim from battery-queue.json)

"name the relative-adverb reading with zero ungranted assumptions; kill iff a window forces 20 non-adverb; else fence"

Numbered pass/fail clauses (pre-registered before testing — bar not modified after data):

1. **C1 (name):** PASS iff the relative-adverb reading of 20 at @1703 ("où"/"quand"/"comment") is nameable with zero ungranted assumptions — premises restricted to standing red-team verdicts, battery-grade promotes/leads, and French grammar as test apparatus.
2. **C2 (kill):** PASS iff a window forces 20 non-adverb at the @1703 locus.
3. **C3 (fence):** if C1 fails and C2 does not fire, fence the relative-adverb arm with stated cause.

Verdict rule: promote iff C1 passes (adverses: none); kill iff C2 passes; else null.

## Method

Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/reladv-20-1703.lock` on start (agent id bf7ff2ec-c6a8-4c69-a9c9-e1f00a4a93ef, 2026-10-09T15:33:45Z); no prior/stale lock. Re-derived the repaired 1,847-pair / 96-type stream in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (byte-exact tokenization per `repair_parse.py`; asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gate instances, and the red-team adjudication queue untouched. Standing values held fixed per §7; adopted, never re-litigated: `importe-1702-singleton` PROMOTE (terminal singleton confinement), `adverb-20-wide` NULL (clause-adverb fence; its window table re-verified), `census-20-open-windows` PROMOTE (@703 forced infinitive, @873 forced finite verb), R20-029(b) ("n'importe" is a fused lexical item), R20-125 (62='il' REJECTED, 'il' killed at kill grade, 62's cell absent), R20-126 (poly-20-docket FENCE; 20 has no cell; polyvalence NOT declared).

## Locus (byte-exact, row a8_06)

`@1698=91 @1699=85 @1700=33 | @1701=94 @1702=30 | @1703=20 | @1704=62 @1705=94 @1706=88 @1707=26`

i.e. `…[33] n'importe [20] [62] ne [88-fin]…`, with:
- "n'importe" = fused lexical item over the unique stream-wide '94 30' adjacency (adopted singleton confinement; R20-029(b) confirms fused status),
- 88 finite (battery-grade, pron730-clause-wide),
- 94="ne" strong lead (R17-001, confirmed R20-007),
- 62 class-open, cell absent (R20-125); its subject position is forced by French word order ([X] before "ne" + finite verb = subject slot) — grammar as apparatus, not a value assumption.

## Window-level evidence: rival arms at @1703

French lexicon constrains "n'importe" continuations to the interrogative/relative set: où, quand, comment, qui, quoi, quel(le)(s). Every other role dies on grammar alone:

| rival role for 20 | test | result |
|---|---|---|
| noun | "n'importe [noun]" is ungrammatical (bare noun never licensed after "n'importe") | dead at kill grade |
| verb | "n'importe [verb]" ungrammatical | dead at kill grade |
| adjective | "n'importe [adj]" ungrammatical | dead at kill grade |
| general clause adverb (ainsi/donc/cependant) | "n'importe ainsi" ungrammatical; "n'importe" licenses only the relative subclass (adopted parent finding) | dead at kill grade |
| determiner "quel" | "n'importe quel" requires a following noun; @1704=62 is class-open (62='il' killed, R20-125), so the arm is unnameable | fenced with stated cause (needs 62 nominal — ungranted) |
| pronouns "qui"/"quoi" | "n'importe qui/quoi" as a fused NP needs a comma break ("n'importe qui, il ne vient pas"); the stream marks no punctuation | fenced with stated cause (needs unmarked punctuation — ungranted) |
| **relative adverbs où/quand/comment** | "n'importe où/quand/comment [62] ne [88-fin]" — fully grammatical with zero punctuation and zero new assumptions | **named** |

The three surviving candidates are not discriminable at battery grade (où/quand/comment all parse identically here); the subclass is named, the exact word stays open.

## Per-clause results

1. **C1: PASS** — the relative-adverb reading (où/quand/comment) at @1703 is named with zero ungranted assumptions. Premises: (a) "n'importe" fused at @1701–1702 — battery PROMOTE, confirmed fused by R20-029(b); (b) 88 finite — battery PROMOTE; (c) 94="ne" — strong lead; (d) 62's subject slot — forced by French word order, grammar as apparatus; (e) the "n'importe" continuation lexicon — French grammar as apparatus. No value named for 20 beyond the subclass; no value named for 62, 88, 33, 91, or 85. No global class claim for 20 (R20-126 respected: 20 stays cell-less, polyvalence undeclared — this is a locus-level naming, same standing as the parent's per-window practice).
2. **C2: does not fire** — no window forces 20 non-adverb at @1703. (The standing @703 infinitive and @873 finite-verb loci concern other windows and are untouched; they are exactly why no global claim is made.)
3. **C3: not reached.**

No standing or red-team verdict contradicted or downgraded: the clause-adverb fence (parent), the conj/prep fence, the @703/@873 verb classifications, R20-125 (62), R20-126 (20 docket), and R20-029(b) all stand; §7 intact. Canonical-stream caveat stands (row a8_06 offset unvalidated).

## Verdict: PROMOTE

The relative-adverb arm for 20 is named at battery grade at the @1703 locus: 20 = relative adverb of the "n'importe"-licensed subclass (où/quand/comment), in the frame "…[33] n'importe [20] [62] ne [88-fin]…". Exact word among the three undiscriminated at battery grade. Per §4 (promote), no follow-ups required; none proposed. The exact-word discrimination and any global-20 consequence belong to the red-team venue (poly-20-docket, R21 triggers per R20-126).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-reladv-20-1703.md` (this file).
- Queue: `reladv-20-1703` queued → verdict/promote via temp-file + rename, own entry only; pre-write assert confirmed queued/verdictless; JSON re-validated post-write.
- Lock `reladv-20-1703.lock`: created on start, deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
