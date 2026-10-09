# Battery verdict: frame-43-00-boundary

Target: `frame-43-00-boundary` — "adjudicate the boundary alternative at @1543-1549 ('78 43 00 46' boundary, not 'pour que' governed by 43)".
Worker: 5dbd9649-5774-48e0-9735-968c81f1a6c7. Date: 2026-10-09.
Lock: created `code/crowd17/next-token/locks/frame-43-00-boundary.lock` on start (no prior lock, no stale-lock note needed).

## Bar (verbatim from battery-queue.json, pre-registered before testing)

> "resolve iff one boundary parse covers 78-43-00-46 with stated values; else fence the window with stated cause"

"Stated values" is read as: the standing battery values of the involved cells, with zero new ungranted assumptions.

Numbered clauses:
1. **C1:** Non-surviving boundary parses die with stated cause: Parse A (boundary at 78|43) and Parse C (boundary at 00|46).
2. **C2:** One boundary parse (Parse B, boundary at 43|00) covers 78-43-00-46 with stated values alone.
3. **C3:** Else-arm: if no parse resolves, fence @1543-1549 with stated cause.

## Method

Read BATTERY-PROTOCOL.md first. Re-derived the repaired 1,847-pair / 96-type stream in-session exactly like `code/side-keyhunt/repair_parse.py` (byte-exact `[s[i:i+2] for i in range(o, len(s)-1, 2)]`; asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched. No data invented. @-offsets are 0-based pair positions (battery convention).

Adopted, not re-litigated (protocol §5 — never downgrade):
- battery-frame-43-pour-que-1544 (NULL, 2026-10-09): government reading ("43 pour que") dead — 43's value candidate set {suite, manière} killed at kill grade; {condition, mesure} killed at kill grade on par-43 x2 + @21 plus terminal corpus closure; extended set (façon, raison, fin, cause, intention, précaution, disposition) all dead on independent windows.
- battery-fin-88-1541-parallel (KILL, 2026-10-09): @1539–1544 = "Il [93-fin] [88-inf] le [78]" — 88 is 93's infinitive complement.
- battery-prenne-subject-S1545 (PROMOTE, 2026-10-08): "pour que ∅ prenne" genuinely subjectless, with stated cause.
- battery-ver-78 (NULL/LEAD, R16-005): 78='ver' graded LEAD, red-team venue; 78's value open, bounded to ver-words; never verb-shaped.
- Standing values: 62='il' (lead), 93 verb-class, 77='le' (provisional), 78 nominal-class (value open), 43 value open (no registry entry), 00='pour' (A9), 46='que' (banked pencil GT), 70='pre' (GT), 12='n', 94='ne', 92 nominal (prenne battery), 45='ce' (A11 hold).

## Window-level evidence

### The target window — @1536–1552 (row a8_00, byte-confirmed)

```
1536=62 1537=06 1538=21 1539=62 1540=93 1541=88 1542=77 1543=78 1544=43
1545=00 1546=46 1547=70 1548=12 1549=94 1550=92 1551=45 1552=23
```

Matrix clause (adopted clause split, il-62 battery): `…il [06] [21] ‖ Il [93] [88-inf] le [78] [43]`.
Subordinate: `pour que ∅ prenne` (@1545–1549: 00='pour', 46='que', 70='pre', 12='n', 94='ne').

### Distributional census (re-derived byte-exact)

- **"43 00"**: exactly 3x stream-wide — @244 (`…56 [43] [00] 66 91 32…`), @1126 (`…37 [43] [00] 86 52…`), @1544 (target). Only the target continues with 46='que'.
- **"78 43"**: exactly 1x stream-wide (@1543). Stream hapax — zero repetition leverage; the locus is the sole instance of the 78-43 contact.
- **"00 46" ("pour que")**: exactly 4x — @106, @545, @1545, @1680. Matches the parent census; no pour-que window stream-wide is noun-governed.
- **43 predecessors**: {96 x2, 37 x3, 11 x1, 47 x1, 82 x1, 88 x1, 56 x1, 32 x1, 46 x1, 06 x1, 08 x1, 21 x1, 78 x1}. The 96='par' x2 ("par [43]", byte-identical "45 64 96 [43] 87 01" at @343/@1027) is a nominal-class leg for 43, not a battery-grade class naming.
- **43 followers**: {00 x3, 77 x2, 87 x2, 98 x2, 29/81/91/24/07/55/21 x1}.

### Boundary parse enumeration

- **Parse A — boundary at 78|43:** "…le [78] ‖ [43] pour que ∅ prenne". The left fragment ends complete; 43 would head a clause whose only content is "pour que [subjunctive]". A bare noun cannot head a "pour que" complement — that is exactly the government reading ("X pour que"), which is dead at kill grade (candidate exhaustion, zero noun-governed pour-que windows stream-wide). As a verbless fragment it has no licensed construction in 1841 French. Dead.
- **Parse C — boundary at 00|46:** "…[43] pour ‖ que ∅ prenne". 46='que' is banked pencil GT; "pour que" is the unit. "pour" takes infinitive/noun complements; "que ∅ prenne" alone is a fragment. Ungrammatical. Dead.
- **Parse B — boundary at 43|00:** "…Il [93-fin] [88-inf] le [78] [43] ‖ pour que ∅ prenne". Sole survivor family. The subordinate parses under standing values (subjectless "pour que prenne", confirmed genuine by prenne-subject-S1545). The matrix is complete under standing values **iff** 43 has a licensed role after "le [78]":
  - (a) post-nominal adjective: 43's class is open → ungranted assumption, cannot assert.
  - (b) appositive noun: needs punctuation → ungrammatical without a stated license.
  - (c) second direct object of 88: bare asyndetic double object → ungrammatical in 1841 French.
  - (d) 43 as head noun with 78 adjectival: ver-78 LEAD bounds 78 to ver-words; no adjective value named → cannot force.
  No member is licensed at battery grade.

## Per-clause verdicts

1. **C1 — PASS.** Parse A dies: it collapses into the government reading, dead at kill grade (adopted candidate exhaustion). Parse C dies: splitting the "pour que" unit is ungrammatical (46='que' banked GT).
2. **C2 — FAIL.** Parse B is the sole surviving boundary parse, but it does not cover 78-43-00-46 with stated values alone: "le [78] [43]" has no forced structure without 43's value (candidate set exhausted at battery grade — adopted) or 78's value (open, ver-78 LEAD, red-team venue).
3. **C3 — FIRES.** Fence @1543–1549.

## Adverse

**"78's value open; the only reopen paths are red-team acts" — ANSWERED as the fence cause.** The fence rests on exactly the two open values named in the adverse: 78's value is open (bounded to ver-words by the ver-78 LEAD, red-team R16-005 venue), and 43's value candidate set is exhausted at battery grade (adopted: {suite, manière, condition, mesure} + extended set all dead). The "78 43" hapax gives zero distributional leverage to resolve either independently. Reopen paths are red-team acts: a 43 value ruling (or the @21 polyvalence ruling), a 78 value adjudication, or a red-team ruling on the "43 pour que" collocation. No standing red-team verdict is contradicted.

## Verdict: NULL — @1543-1549 fenced

The government rival is dead and Parse B (boundary at 43|00) is the sole surviving reading of the window, but the matrix-complete leg cannot be satisfied at battery grade: 43's role after "le [78]" needs 43's value (exhausted) or 78's value (open). @1543–1549 is therefore definitively non-discriminating for noun-43 — the red team can close the discriminator on the boundary reading without naming 43. No polyvalence declared; §7 intact.

Canonical-stream caveat stands (row a8_00 offset unvalidated; 68/70 caveat).

## Follow-ups (null regenerates work; both verified ABSENT from battery-queue.json)

1. **np-tail-78-43-apposition** (P3): test "le [77] [78] [43]" @1542–1544 as determiner + head + post-nominal modifier once 43's class is named (or test which of the four Parse-B sub-members the NP structure forces). Bar: resolve iff one licensed NP structure parses with <=1 ungranted assumption under standing values; else fence. Stated trigger: needs 43's class or 78's value — queued, not dispatchable until one lands.
2. **par-43-class** (P3): name 43's class at the "par [43]" windows (0b@343/@1027: byte-identical "45 64 96 [43] 87 01" = "ce qui par [43] ce [01]"); "par" takes a nominal complement in 1841 French. Bar: class named at battery grade with zero contradiction across all 43 windows' predecessors; else fence. Narrower than noun-43 (class only, value open); does not duplicate it.

Not re-proposed (already queued): `pour-que-leftclass-4win`, `frame-77-78-43-slot`, `pour-que-lexicon-close`.

## Bookkeeping

- Queue: `frame-43-00-boundary` → status `verdict`, verdict {"result": "null", "report": "code/crowd17/report_inbox/battery-frame-43-00-boundary.md", "date": "2026-10-09"} (pre-write assert passed — was `queued`/verdictless; temp-file + rename; JSON re-validated post-write; own entry only; no downgrade).
- Lock `locks/frame-43-00-boundary.lock` created on start, deleted on completion (verified gone).
- No standing/red-team verdict contradicted or downgraded; §7 intact. R5005, sealed gate instances, red-team adjudication queue untouched.
