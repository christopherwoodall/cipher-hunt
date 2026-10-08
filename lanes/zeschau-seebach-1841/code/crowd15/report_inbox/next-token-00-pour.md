# Battery A9 — 00 = "pour" ("00 que" ×4)

Date: 2026-10-07. Runner: battery-runner (resumed, round 15).
Stream: repaired 1,847-pair parse recomputed in-session
(`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
per `code/side-keyhunt/repair_parse.py`).

Source: finder Q3 (next-token-findings-que-ce.md).
Standing: 00 is the top-frequency group (55×, 2.98%), unidentified; "pour"
was already the standing "00 elsewhere" hypothesis; 96-00="par le" is
compositional (00="le" only as pre=96 islet per contexts.json).
Windows: "00 que" ×4 @107, @546, @1546, @1681.

## Pre-registered bar (written BEFORE touching data)

- **PROMOTE 00="pour"** iff: (a) ≥2 of the four "00 que" windows parse as
  "pour que"+verb (subjunctive-shaped or "pour que"-compatible) with zero
  board contradiction; (b) the @107 tension ("00-46-11-21-67": 67=et/veut
  fork, not subjunctive) is resolved or fenced with a stated cause —
  an unresolved @107 does not kill by itself (one window can be a
  different "00"), but it must not be hidden; (c) 00's global contact
  profile is "pour"-compatible (prepositions precede nouns/verbs/clitics;
  "pour" should NOT show determiner-like or finite-verb-like slots).
- **HOLD** (lead, not promotion) if exactly 1 clean "pour que" window or
  the profile is mixed.
- **KILL** if ≥2 windows contradict "pour" (e.g. 00 in a slot "pour"
  cannot occupy) or the profile is anti-prepositional.
- Note the rival: 00="le" exists as a pre=96 islet (F54) — the claim here
  is 00="pour" ELSEWHERE (unconditioned). A "pour" promotion does not
  disturb the 96-00 islet.

## Data

### "00 que" ×4 windows

| pos | window | "pour que" read |
|---|---|---|
| @106 | 28-00-46-11-21-[67] | "pour que la [21] [67]" — parses; 67-tension conditional (see below) |
| @545 | 06-00-46-24-47-55 | "pour que en/de ce [47]" — unparsed, fenced (not contradictory) |
| @1545 | 43-00-46-70-12 | "**pour que pre[12]**" — "pour que [prenne/prévienne]"-shaped; 70="pre" is pencil GT. Cleanest window. |
| @1680 | 44-00-46-79-65 | "**pour que tout [65]**" — "que tout [verb]" frame (A5/A7). Clean. |

### @106/@107 tension — fenced with cause

"pour que la [21] [67=et/veut]": IF 67="veut" (indicative), "pour que"+indicative
is ungrammatical. But 67 is the unresolved et/veut FORK — if 67="et", no
tension ("pour que la [21] et [X]"). The tension is fork-conditional, not a
contradiction. Fenced pending the 67 fork; not hidden.

### @545 — fenced as unparsed

"00-46-24-47" = "pour que [24] ce": neither "en"- nor "de"-reading of 24
yields clean French ("pour qu'en ce [55]"? "en ce"+noun is possible but
strained). Unparsed ≠ contradictory — the window's left ("48-42-06") is
itself unparsed. Not a "pour"-killer.

### 00's global profile (n=55) — the "pour" signature

Successors: **86×12, 33×8** (INF-class — see below), 66×7, 92×6, 97×4,
11×4 ("pour la"), 46×4 ("pour que"), 36×3.
**00→{86,33} = 20/55 (36%)** — "pour"+infinitive is 00's dominant frame.
Predecessors: 11, 06, 16, 63, 81, 96, 28, 43, 26, 98, 44 (×3–4 each) —
preposition-like spread; zero finite-verb or determiner slots.

### 86's INF-class confirmation (needed for leg 1)

86 (n=32): pre=00 ×12 (37%!), suc=29 ("er") ×4 — the same signature as
33 (INF-class: pre=00 ×8, suc=29 ×5). **86 is infinitive-class** by the
33-parallel: "pour [86]" ×12, "[86]er" ×4. (Also pre=77 ×5 "le [86]" —
substantivized-infinitive-shaped, feeds finder §4.)

### Corpus prior

"pour" is a top-10 French word; 00 is the top cipher group (2.98%).
"pour que"+subjunctive and "pour"+infinitive are register-ubiquitous
(not re-counted here — grammatical bedrock).

## Verdict: PROMOTE

**00="pour" is PROMOTED** (unconditioned; the 96-00="par le" islet is
undisturbed). Four legs: (1) 00→INF-class {86,33} ×20/55 — the dominant
"pour"+infinitive signature; (2) "pour que pre[70]" @1545
(subjunctive-shaped, GT "pre"); (3) "pour que tout [65]" @1680;
(4) "pour que la [21]" @106. Profile is preposition-compatible throughout.
Fenced with cause: @545 (unparsed), @106's 67-tension (fork-conditional).
**Weakest leg (red team):** leg 1 leans on 86's INF-class, which itself
rests on the 33-parallel — if 86's classification slips, leg 1 softens to
"00→86 ×12 unexplained".
**Downstream:** confirms the "pour" half of finder §4's "par le [X]"
frames — "pour [86/33]" are "pour"+infinitive, feeding the §4 discriminator.
