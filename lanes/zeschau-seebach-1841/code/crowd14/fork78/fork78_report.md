# FORK-78 resolution report (round 14, WO6) — 2026-10-07

**Verdict: H1 CONFIRMED with refinement** — 78 is positional-polyvalent:
**78="ver" word-initial; 78="er" at non-initial er|ne boundaries.**
Refinement vs the work order as stated ("ver-INITIAL vs er-FINAL"): the er-arm
is boundary-specific (er|ne), not generic-final — zero word-final 78 windows
exist, so "er-FINAL" per se is UNTESTED; the tested claim is ver-INITIAL /
er-NON-INITIAL. Fork status: **RESOLVED** (même-4 fenced, @1352 contested).

PREREG: `PREREG.md` (written before the table was computed). Code+data:
`fork78.py`, `fork78_results.json`. Banked constraint honored throughout:
76 and 78 treated as separate cells; no 76↔78 homophone tie, no window merging.

## 1. Position contingency table (Leg 1)

Position source: F107's 32 segments first (coverage 0/31 78-windows, 0/21
76-windows — the F107 instrument is honestly NULL here, 3.9% coverage), then
neighbor rules: pre78 a complete-word cell → INITIAL (tiers: {11,46} GT;
{87,64,96} prov; {37} MED; {77} prov-cond). Frames: ver-frame = pre∈{37,11,87}
("le/la/ce ver[…]", mirroring 76); er-frame = suc=94 (94="ne" prov-strong,
the h3a er|ne diagnostic). The four 78-45 même-windows excluded (F50 "même"
LEAD = live third value); @1352 excluded as contested (R-c solo vs killed
R-b medial).

```
               ver-frame   er-frame
INITIAL            6          0
NON-INITIAL        0          1
```

Fisher exact one-sided p = **0.143** — directionally perfect, underpowered;
the pre-registered p<0.05 bar is NOT met (expected; n small by construction).
Sensitivities: S1 (+@1352 as INITIAL) [[6,1],[0,1]] p=0.250; S2 (GT-only
positions) [[2,0],[0,1]] p=0.333; S3 (drop pre=77) = primary; S4 (+même as
ver-frame, adversarial) = primary. No sensitivity flips the direction.

Cell members — INITIAL×ver-frame (6): @297 (11-78-40, GT "la"), @415
(37-78-49, "le"), @476 (37-78-74, "le"), @629 (87-78-67, "ce" prov), @1670
(11-78-55, GT "la"), @1771 (37-78-62, "le"). NON-INITIAL×er-frame (1): @1181
(77-78-94, MEDIAL via gouv|er|ne|m|ent LEAD). Zero off-diagonal in every
specification. 16/31 78-windows remain UNCERTAIN (honest residual).

## 2. Leg 2 — H0-er (78="er" uniformly) KILLED, strong

@297 and @1670: pre=11=la GT → 78 word-initial, certain. "la er" is
ungrammatical: era corpus (nesselrode-v8, 92,594 tokens) has ~zero er-initial
common words — only "erreur" (which obligatorily elides: "l'erreur"; a by-ear
cutter hearing /lɛ.ʁœʁ/ never writes 11="la"+78). Two independent GT-anchored
contradictions of uniform-er. Instrument: French grammar + GT anchor —
independent of Leg 1's provisional tiers.

## 3. Leg 3 — H0-ver (78="ver" uniformly) contradicted, weak grade

78-94 ×2 (@1181 MEDIAL, @1352 CONTESTED). Under H0-ver these read "ver|ne" —
zero genuine common words in French. h3a: 52 er|ne tokens/22 types vs 5
ver|ne tokens/3 types (all proper/foreign), p=3.2e-11. Re-derived on the
clean-pool v8 file: 16 vs 4 tokens, binomial p=0.0059 — direction reproduced.
Graded WEAK per h3a's own PREREG ("language stat ≠ encipherer cut; cannot
kill a tine alone"). Supporting datum: 76→94 is 0/21 — the er|ne boundary
attaches to 78 only. Instrument: era-corpus boundary survey — independent.

## 4. Leg 4 — the 76 contrast; {76,78} tension ADDRESSED

76 (21 windows, same position rules): 6 INITIAL — incl. @833/@892/@969
"le ver[…]" (F103's ver-tine); 2 FINAL — @200 (67-76-87) and @1273
(47-76-87), both "76 ce" = "-ver ce" ("trouver/prouver ce"-type ver-finals,
provisional tier); 13 uncertain; **0 er-frames** (suc=94: 0/21).

Resolution of the tension: 76 is uniform "ver" across initial AND final
positions with zero er-evidence; 78 is ver-initial AND er-at-er|ne. They
differ on er because er is licensed only at er|ne boundaries, and 76 never
occurs at one (0/21) while 78 does (2/31). The split is positional-inventory,
not value-arbitrary — it EXPLAINS the divergence rather than deepening it.
Precedent: {52,59} positional-allophone split (F103). The F103 group split
stands (no merger; 1690 law); whether initial-76 and initial-78 share the
"ver" cell is fenced for the solver side.

## 5. Leg 5 — Frenchman (required)

Corpus correction to the PREREG expectation: "ver-initial-only" is WRONG.
nesselrode-v8: ver-final 104 tokens/23 types ("trouver", "prouver",
"observer", "enlever", "hiver", "lever"…) vs ver-initial 69/26. French "ver"
is positional-broad — 76's initial+final ver is fully French-plausible, and a
final-"ver" cell has genuine inventory need. This does NOT rescue H0-ver for
78: 78's non-initials are specifically er|ne-boundary, never generic finals.

Ear-checks: @297/@1670 "la 78" → "la ver[…]" (la vertu/verve/verrine class);
@1181 gouv|er|ne|m|ent (78="er" medial, LEAD); @1352 «le [78] ne ment pas»
(R-c granted) — solo-78, reading open; a solo "er" is not a French word, and
the F68 German-"er" watch-item is dismissed (R5005 is French). Frenchman
concurs: a {ver,er}-forked cell at both edges MUST be positional-polyvalent —
no uniform reading survives Legs 2+3.

## 6. Cross-check answers

- **er|ne diagnostic (52 vs 0):** predicted, not just consistent. Under H1
  every 78-94 is word-non-initial "er" → "er|ne" (productive, 52/22). Under
  H0-ver the two 78-94s are "ver|ne" (zero genuine common words) — double
  anomaly. The diagnostic's existence is H1's er-arm signature.
- **"No surviving ver-internal window"** (french-blitz re-read): confirmed —
  the R-b gou|ver|ne|m|ent window died with F70's R-c grant at @1351; the
  surviving 5-mer @1181 reads gouv|er|ne|m|ent (er-internal). All surviving
  ver-evidence for 78 is word-initial.

## 7. Caveats & fences

- même-confound: 78-45 ×4 (@313/@573/@982/@1164) excluded — F50 "même" LEAD
  is a live third value for 78. If confirmed, H1's ver-arm restricts to
  non-même windows. Not adjudicated here.
- @1352 contested (R-c solo vs killed R-b medial) — excluded from primary,
  S1 sensitivity only.
- "er-FINAL" untested: zero word-final 78s observed (no suc∈{11,46,87,…}).
- 94="ne" is provisional-strong: Legs 1-er-frame and 3 inherit its status.
- 16/31 78-windows positionally UNCERTAIN — the mapping is proven on the
  classifiable subset, not the whole inventory.

## 8. Verification

5 random 78 windows (seed 1407) re-derived from an independent fresh parse
of the raw rows + repaired offsets: @297 (11-78-40), @313 (37-78-45), @819
(47-78-40), @1181 (77-78-94), @1621 (84-78-66) — all byte-exact OK.

## Bottom line

78's fork resolves as **positional polyvalence: ver-initial / er-non-initial
(at er|ne)** — CONFIRMED on 4 independent legs (grammar+GT kill of uniform-er;
corpus-diagnostic contradiction of uniform-ver; 76-contrast explaining the
split; Frenchman ear+lexicon), with a directionally-perfect but underpowered
contingency table (p=0.143, all sensitivities same direction). The {76,78}
tension is explained by positional inventory (76 never reaches an er|ne
boundary), the groups stay split per F103, and the même-4 plus @1352 stay
fenced.
