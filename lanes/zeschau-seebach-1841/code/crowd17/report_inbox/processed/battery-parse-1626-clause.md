# Battery report: parse-1626-clause

- Target id: `parse-1626-clause`
- Claim: "Resolve the clause structure of 'que [56] [69] [26] pour [33]' (56's subject/object assignment); the assignment constrains the verb's valency."
- Date: 2026-10-09
- Worker: battery worker (subagent 44f7af4d-7573-48fa-bc4a-fe3b9538bfec)
- Stream: repaired 1,847-pair / 96-type parse, re-derived in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

Terms (ASD-STE100): "subject assignment" = which group is the grammatical subject of 56's clause. "Valency" = whether the verb takes a direct object (transitive) or not. "Xéent" = the eight French verb candidates for 56's value forming 3sg -ée / 3pl -éent (créer, agréer, suppléer, recréer, gréer, dégréer, procréer, maugréer; réer killed by xeent-register-tiebreak).

## Bar (verbatim, pre-registered before testing)

"Resolve the clause structure of 'que [56] [69] [26] pour [33]' (56's subject/object assignment); the assignment constrains the verb's valency."

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** Enumerate the live subject/object assignments for 56 at @1627 with byte evidence; state which are forced vs open.
2. **C2:** Test whether any live assignment differentially constrains valency among the Xéent candidates.
3. **C3:** Resolve iff one assignment is forced AND it constrains valency; else fence with stated cause.

Adverse (listed, must be answered): "the ambiguity is structural, not valency-driven; all five Xeent candidates equally compatible under every live assignment."

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/parse-1626-clause.lock` on start (agent id + UTC timestamp); deleted on completion.
2. Re-derived the repaired stream in-session; all offsets below are 1-based `@` on the 1,847-pair stream.
3. Full n-censuses: 56 (n=23), 69 (n=12), 26 (n=17), 33 (n=25), each with ±2 context, re-derived (not copied from prior reports).

## Window-level evidence

### The locus and its twins

- **W2 @1627 (row a8_03):** `…[1624]67 [1625]33 [1626]46(que) [1627]56 [1628]69 [1629]26 [1630]00(pour) [1631]33 [1632]21 [1633]64(qui) [1634]37 [1635]01 [1636]74 [1637]87(ce) [1638]74…` Left matrix: `…[1620]11(la) [1621]84(on) [1622]78 [1623]66 [1624]67 [1625]33`.
- **W1 @933 (row a5_10):** `[925]71 [926]17 [927]61 [928]96(par) [929]48 [930]82(m) [931]98 [932]83 [933]56 [934]69 [935]26 [936]00(pour) [937]33 [938]21 [939]64(qui) [940]37 [941]01 [942]07 [943]50 [944]40 [945]08`. **No "que" before 56 at W1.**
- **W3 @406 (row a2_07–a2_08):** `[398]82(m) [399]48 [400]06 [401]11(la) [402]45 [403]88 [404]53 [405]34 [406]69 [407]26 [408]00(pour) [409]33 [410]01 [411]02…` — the `69 26 00 33` kernel **without 56**.
- Census: `69 26 00 33` occurs exactly **3×** stream-wide (W1, W2, W3); `56 69 26 00 33` occurs exactly **2×** (W1, W2). W1 and W2 share the byte-identical 8-group formula `56 69 26 00 33 21 64 37`.

Structural consequence: `69 26 00 33` is the stable kernel; 56 is a W1/W2-specific addition. The subject/object assignment cannot be read off the kernel — it depends on 56's own form, which is open.

### Live assignments (C1)

- **H1 — 56 finite 3sg verb, subject = 69 (inversion), 26 = adverb:** "que [56-V] [69-S] [26-adv] pour [33]". Live: 69 is nominally capable (see @1836 below); inversion is licensed in subordinates. Blocked by: 69's value/class unratified (69=`ce` is battery-promoted, pending red team; bare `ce` as inverted subject of a lexical verb is strained); 26's adverb arm live but unlanded.
- **H6 — 56 finite verb, 69 = subject, 26 = object NP:** "que [56-V] [69-S] [26-O] pour [33]". Live only if 26 is nominal; 26's nominal arm is open (the @1753 subject-kill was locus-specific; @1770 `87 64 [26] 37` shows a verbal arm for 26 too).
- **H4 — 56 non-finite, clause verb = 33:** "que [56-inf] [69-S] [26-?] pour [33-V]…". Blocked by: "que + infinitive" relative is unlicensed in French; 33's verbal class unlanded.
- **H7 — 56 3pl verb ("-éent"), subject = 69 26 plural NP:** live as a shape (all eight Xéent candidates form 3pl -éent); blocked by 69's number and value both open.
- **W1 variant:** at W1 there is no "que"; left is `[96]par [48] [82]m [98] [83]` then 56 — a paratactic/main-clause frame. The W1 and W2 assignments need not be identical, which doubles the ambiguity rather than resolving it.

**C1 result: PASS (enumerated). No assignment is forced.** Every arm has an open dependency: 56's form (3sg/3pl/infinitive all live), 69's value/class (battery-pending `ce`), 26's class (nominal/adverb/verbal all live), 33's class.

### 69's nominal leg (new, byte-exact)

- **@1836 (row a8_11):** `[1834]59 [1835]36 [1836]69 [1837]64(qui) [1838]22` — 69 as antecedent of the `qui`-relative ⇒ 69 is nominally capable at battery grade. This keeps H1/H6 alive but does not select between them (antecedent-hood does not fix the subject/object role inside the locus).

### Valency test (C2)

Tested all **eight** live Xéent candidates (target text says "five"; xeent-register-tiebreak closed the set at eight after killing réer) against every live assignment:

- Under H1 (no object slot): every candidate has a licensed absolute/intransitive use (valency-56-wide: "emploi absolu is licensed", strain gradient not kill-grade). All 8 fit.
- Under H6 (26 = object): every candidate has a transitive arm (maugréer: TLFi transitive "maudire quelqu'un" vx/littér). All 8 fit.
- Under H4/H7: no candidate is excluded by form or valency.

**C2 result: the adverse is CONFIRMED, not answered away.** The ambiguity is structural, not valency-driven; no live assignment differentially constrains valency among the candidates.

### C3

Does not fire. **Fence executed** with stated cause: (a) 56's form is a three-way open tie; (b) 69's value is battery-pending; (c) 26's class is a three-arm split; (d) W1 lacks "que", so the two formula instances may not even share one structure; (e) the stable kernel `69 26 00 33` parses without 56 (W3), so 56's role is the variable, not the anchor.

No standing or red-team verdict contradicted; §7 intact; no polyvalence declared. Canonical-stream caveat stands (row a8_03 offset unvalidated).

## Verdict: NULL

## Follow-ups proposed (nulls regenerate work; all verified absent from battery-queue.json)

1. `form-56-1627` (P3) — decide 56's form (3sg -ée vs 3pl -éent vs infinitive) at @933/@1627 via spelling/shape constraints; a landed finite-56 forces the subject search and collapses H4.
2. `class-69-nominal` (P3) — land 69's nominal class beyond the @1836 qui-antecedent leg (12-window census); a landed nominal 69 plus a subject-hood test selects H1 vs H6.
3. `kernel-6926-frame` (P3) — parse the stable `69 26 00 33` kernel at W3 (@406, 56-less) as the base frame; 56 then attaches to a known structure instead of an unknown one.

## Bookkeeping

- Queue: `parse-1626-clause` → status `verdict`, result `null`, 2026-10-09 (pre-write assert passed — was `queued`/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/parse-1626-clause.lock` created on start, deleted on completion (verified gone).
