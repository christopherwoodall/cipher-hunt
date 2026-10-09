# Battery verdict: part-62-elsewhere

## Target
- id: `part-62-elsewhere` (priority 3)
- CLAIM: census 62's other windows (62-94 x9, 62-48 x6, 62-98 x5, 62-16 x4, 62-61 x2, 62-06 x2, 62-96 x1) for a participial-shaped environment with clean right edge
- Evidence (queue): @46 "30 62 96" trigram hapax; parent battery's word-class inventory at @46 now exhausted (adverb fenced, participle fenced)

## Bar (verbatim, pre-registered)
"find "pas/participle + agent" frame without 'pour' collision"

Restated as numbered pass/fail clauses (frozen before testing):
- **C1 (census):** enumerate all listed 62 windows with byte context under standing values.
- **C2 (promote):** >=80% (23/29) parse under one participle shape with a clean right edge (no 'pour' collision); residuals fenced.
- **C3 (kill):** kill iff a kill-grade window rules out the participle reading.

## Method
Read BATTERY-PROTOCOL.md first. Created `locks/part-62-elsewhere.lock` on start
(agent id + UTC timestamp), deleted on completion. Re-derived the repaired
stream in-session from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json` (parsed per `repair_parse.py`):
1,847 pairs / 96 groups verified. `canonical.py` never touched. R5005, sealed
gate instances, and the red-team adjudication queue untouched. 1841 diplomatic
French only. All @-offsets below are 1-based lane convention.

Standing values used: pencil GT (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que);
granted/promoted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour A9, 84=on,
47=ce, 06=ent verbal ending, 48=inflectional-'e' R17 letter-tier); provisional
(59=est, 77=le); battery leads used only where stated (94='ne' R17-001 STRONG
LEAD, 98='vient' finite, 62='il' at 62-94/62-98 windows).

## Window-level evidence (all 29 listed windows, byte-traced)

### 62-94 x9 — zero participle-compatible

| @ | frame (±3) | reading under standing values |
|---|---|---|
| 101 | 21 62 94 93 | wordless6: word-final '-ne' — 62 word-internal, not a standalone word |
| 509 | 77 62 94 64 | wordless6: word-final '-ne' — 62 word-internal |
| 762 | 20 62 94 59 | wordless6: word-final '-ne' — 62 word-internal |
| 841 | 20 62 94 26 | wordless6: word-final '-ne' — 62 word-internal |
| 1363 | 92 62 94 79 | wordless6: word-final '-ne' — 62 word-internal |
| 1687 | 93 62 94 79 | wordless6: word-final '-ne' — 62 word-internal |
| 1705 | 20 62 94 88 | "il ne [88-verb]" — 62='il' demonstrated at kill grade (collision-62-84 KILL); "[part] ne [verb]" is not a French constituent (nepas-20-adverb-gate value-independent corroboration) |
| 1773 | 78 62 94 24 | "il ne [24]" — 62='il' (ne-94-right-context clean verbal-negator leg) |
| 1330 | 06 62 94 70 | 62 before the 'ne' particle; participle reading ungrammatical (no "[part] ne [verb]" constituent) |

### 62-48 x6 — zero participle-compatible
@361, @426, @1316, @1350, @1465, @1570. 48='e' is the R17 letter-tier grant
(fem-e-48: stem-bound, word-final). A standalone participle followed by a bound
letter cannot parse; "62 48" can only compose as verb-stem + inflectional -e
("X-e", cf. parent report's stem-sized profile), which makes 62 a verb stem,
not a participle. (sel-62-48-94 KILL context.)

### 62-98 x5 — zero participle-compatible
@12, @803, @946, @1137, @1325. 98='vient' is battery-promoted finite.
"[62-part] vient" is ungrammatical — a past participle cannot be immediately
followed by a finite verb. The clean reading is 62='il' ("il vient" x5 legs,
per boundary-98-839's subject census).

### 62-16 x4 — residual, no participle license
@83, @659, @1142, @1298. 16's value is open and no left neighbor is an
auxiliary ("a"/"est"), so no passive frame exists. Participle reading
unlicensed but not kill-grade dead here — fenced as residual.

### 62-61 x2 — residual, no participle license
@447, @1455. Same: no auxiliary left, no passive frame. Fenced as residual.

### 62-06 x2 — participle morphologically impossible
@666, @1537. 06='ent' is the promoted verbal ending; "62 06" composes as
stem + ending ("donnent"/"mènent"-shaped 3pl finite). A French past participle
never ends in "-ent". (adv-62-bien-1482: "bienent is not a French word; manner
'bien' cannot split a stem from its ending" — the stem+ending composition
stands.)

### 62-96 x1 — already fenced
@47 ("30 62 96 00" = "pas [62] par pour"). The parent battery fenced the
participle reading here at kill grade: "par pour" is ungrammatical (96='par'
needs a nominal complement; 00='pour' cannot supply it; no byte-evidenced
clause boundary). This is the 'pour' collision the bar excludes; it is the
ONLY 'pas'-before-62 and the ONLY 'par'-after-62 window in the whole stream.

## Per-clause results

### C1 (census): PASS
All 29 listed windows enumerated with byte context; follower counts re-derived
match the claim exactly (9/6/5/4/2/2/1).

### C2 (promote): FAIL — 0/29
No "pas [62-part]" frame exists outside fenced @47 (no other window has 30
before 62); no "[62-part] par [agent]" frame exists outside fenced @47 (no
other window has 96 after 62). Participle-compatible windows: 0. The >=80%
antecedent does not fire.

### C3 (kill): FIRES
**@1705 rules out the uniform participle reading at kill grade.** Two
independent legs:
1. **Value-independent morphology/syntax:** a past participle (or any
   non-verbal/pronominal word) cannot be immediately followed by the particle
   'ne' as one constituent — there is no French construction "[part] ne
   [verb]". The only licensed parse of "62 94 88" is "il ne [88-verb]"
   (nepas-20-adverb-gate).
2. **Demonstrated value:** collision-62-84 (KILL) demonstrated 62='il' at this
   exact window; 62 is a subject pronoun — non-participial.

Under protocol §7 (one value per cell; 67 is the sole true polyvalence), a
global 62=participle is forced false at @1705. The 62-98 x5 family
("[part] vient" ungrammatical) and the 62-06 x2 family ("-ent" is not
participle morphology) independently corroborate; the wordless6 six windows
remove 62 from standalone-word status entirely there.

## Adverses answered
- "coordinates with queued seg-81-30-boundary": different locus (81-30
  boundary fence); untouched, no interaction.
- "no class named for 62 globally": satisfied — this kill removes the
  participle candidate reading only; no class is named for 62.

## Scope
Kills the uniform participle reading of 62 across the listed windows. A
conditioned/split participle arm (participle at some windows only) would be
§7 polyvalence — red-team venue, not declared here. No standing or red-team
verdict contradicted or downgraded (Round 18 assigns 62 no value; 62's
conditioned scope is an open red-team docket item). Canonical-stream caveat
stands (unvalidated upstream offsets on several rows).

## Verdict: KILL
