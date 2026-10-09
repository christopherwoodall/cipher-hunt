# Battery report: sel-37-913-agentive-par

- Target id: `sel-37-913-agentive-par`
- Claim: 37 = past participle at @913 ('est [37] par [09]', agentive-par frame) — parallel to the @1179 promote.
- Date: 2026-10-09
- Worker: battery worker (subagent 4612c2c7-cb03-4999-b8da-0a60f075ae45)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). Verified in-session: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Offsets below are 0-based stream indices (lane convention).

Terms (ASD-STE100): "name" = state a class/value with byte evidence at battery grade. "kill grade" = a window forcing the claim false under standing values. "fence" = set aside with stated cause, re-openable. "unique-survivor elimination" = every rival class excluded, exactly one arm parses.

## Bar (verbatim from queue `bars` field)

"name 37's class at @913 iff unique-survivor elimination under standing values forces past participle with zero new assumptions; do NOT adjudicate 37's global class (red-team venue, frame-37-reexam untouched); fence @913 as locus-scoped if premises fail"

Restated as numbered pass/fail clauses before testing:

1. **C1:** Unique-survivor elimination under standing values forces 37 = past participle at @913 with zero new assumptions → name the class at battery grade.
2. **C2:** If C1 fails, fence @913 as locus-scoped with stated cause.
3. **C3 (constraint):** Do NOT adjudicate 37's global class; frame-37-reexam untouched (red-team venue).

Standing premises used, not re-litigated: banked pencil 11=la/70=pre/82=m/34=i/29=er/40=e/46=que; granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce; provisional 59=est; A1 predicative grant for 37 (class open); 09 class open (nominal/adverbial split deferred, R20); 78='verre' lead (R16-005) not engaged (78 absent from the window); French grammar as test apparatus.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/sel-37-913-agentive-par.lock` (agent id + UTC timestamp); deleted on completion. No stale lock was present.
2. Re-derived the repaired stream in-session. All asserts held (1,847 pairs, 96 types).
3. Byte-confirmed the locus (row a5_09): `[910]64 [911]83 [912]59 [913]37 [914]96 [915]09 [916]02 [917]24`, i.e. "qui [83] est [37] par [09] [02] [24] …".
4. Enumerated every class arm for 37 in the "est [37] par [09]" frame against standing values.
5. Ran a period-corpus shape census of "est [X] par [Y]" (98 files, 170-byte HTTP-500 stub excluded; 693 hits) to test whether rival arms have genuine legs.

## Window-level evidence

**Locus:** 0-based @913 = 37, in the "59 37" window @912–913. The six "59 37" windows stream-wide: @528, @624, @912, @1178, @1443, @1796 (matches the @1179 battery's list). The "96 09" bigram ("par [09]") is a stream-wide hapax: exactly 1× @914. 09 occurs 12× stream-wide; its class is open.

**Left edge:** "qui [83] est" — 64='qui' (granted) is the relative subject of "est"; 83's class is open (adverb/clitic readings available; does not affect 37's class options).

**The @1179 parallel and where it breaks:** At @1179 ("est [37] le [78]"), the "le [78]" tail (determiner + noun, "le verre") admitted only the unaccusative-inversion reading, which requires a past participle — unique survivor. At @913, the tail is "par [09]", and "par" licenses three complement types in 1841 French. The parallel does not transfer.

### Class-by-class elimination at @913 ("est [37] par [09]")

- **Finite verb:** "est [37-fin]" = auxiliary + finite verb. Ungrammatical at kill grade. DEAD.
- **Infinitive:** "est [37-inf]" needs à/de/modal governor; none present. DEAD at kill grade.
- **Determiner / pronoun / adverb:** cannot stand predicatively after "est" in this frame. DEAD at kill grade.
- **Past participle:** "est [37-PP] par [09-agent]" — canonical passive. Corpus: "est [X] par [Y]" is dominated by past participles (hundreds of hits: prouvé, retenu, terminée, démontrée, faite, dominée, soutenue, défendue, signé, attestée, chargé, occupé, etc.). SURVIVES as the leading arm. Needs 09 nominal (live arm, not a new assumption).
- **Adjective:** "est [37-ADJ] par [09-cause]" — SURVIVES. Corpus-attested construction in 1841 French: "il est remarquable par…" (7×), "elle est célèbre par…" (4×), "il est supérieur par…", "il est contemporain par conséquent…", "gouvernement antirévolutionnaire par nature", "ouvrage moral par l'invention", "maison curieuse par…", "sénat judiciaire par la forme", "il est administratif par son objet", "évident par cela", "probable par cela", "possible par…". The "par"-phrase is causal/means ("by virtue of"), not agentive — but it is grammatical.
- **Noun:** "est [37-N] par [09-motive]" — SURVIVES. Corpus-attested: "il est citoyen par instinct", "on est architecte par tradition", "dont il est parent par sa femme", "si l'on n'est poète par les images", "Sylla… est vainqueur par l'aile opposée", "le pape est lion par la puissance temporelle", "il est Turc par sa soumission", "le peuple, qui est femme par l'ardeur des instincts", "elle est cause par institution divine". Bare status/profession nouns license the predicative slot; "par" supplies motive/means.

**Result:** three arms survive (participle, adjective, noun). The participle is the corpus-dominant and default reading, but dominance is not exclusion. The adjective and noun arms are not kill-grade dead — they are genuine, attested 1841-French constructions. Unique-survivor elimination FAILS.

### C1 — FAIL: 37's class at @913 cannot be named at battery grade

The "par [09]" tail, unlike the "le [78]" tail at @1179, does not force the participle. Three classes parse "est [37] par [09]" under standing values with zero ungrammaticality. Naming the participle would promote the leading arm over two live rivals — not battery grade.

### C2 — FIRES: fence @913 as locus-scoped

Stated cause: the "est [37] par [09]" frame is three-ways ambiguous at battery grade (past participle / adjective / noun), per the corpus census above. The fence is locus-scoped and evidentiary — it re-opens iff (a) 09's class/value resolves and the agentive-vs-cause reading of "par [09]" selects one arm, or (b) 37's cross-window class constraints eliminate the adjective/noun arms.

### C3 — honored

No global class adjudicated for 37. frame-37-reexam untouched. §7 intact.

## Adverses answered

1. **Provisional 59='est':** used as provisional (battery-usable per the @1179 precedent); the elimination does not depend on 59's ratification.
2. **78='verre' lead (R16-005):** not engaged — 78 is absent from the @913 window; not re-litigated.
3. **96='par' granted:** used as granted; the three-way ambiguity is in "par"'s complement type, not in 96's value.
4. **Canonical-stream caveat:** row a5_09 offsets are unvalidated upstream EM choices; the locus is as parsed under repaired_offsets.json.

## Verdict: NULL (fence executed per the bar's C2)

## Follow-ups proposed (per §4; all verified ABSENT from battery-queue.json)

1. `par09-915-rerun` (P4, gated): re-run the @913 class test once 09's class/value resolves (`nom09-open-windows` queued). If 09 names as an agent-capable noun/pronoun, "par [09]" is agentive and the participle arm is selected; if 09 names as an abstract/motive noun, the adjective/noun arms are selected. This is the key disambiguator.
2. `adj-37-913-elim` (P4): targeted battery-grade attempt to kill the adjective and noun arms at @913 — e.g., via 37's cross-window class constraints (does 37 show adjectival/nominal behavior elsewhere?) or a narrower corpus test conditioning on 09's eventual class.

## Scope and caveats

- Locus-level fence at @913 only. No value named for 37; 37's global class stays red-team venue.
- Does not disturb the @1179 promote (different tail, different elimination).
- No standing or red-team verdict contradicted, downgraded, or re-litigated; §7 intact. Canonical-stream caveat stands (row a5_09 offset unvalidated).
- The corpus census (693 "est X par Y" hits, 98 files) is filed as evidence in this report; the full hit list is reproducible via the regex `\best\s+(\w+)\s+par\s+(\w+)` over `code/side-period/corpus/`.

## Bookkeeping

- Queue: `sel-37-913-agentive-par` → status `verdict`, result `null`, 2026-10-09 (pre-write assert passed — was `queued`/verdictless; target-id-unique tmp `battery-queue.json.sel-37-913-agentive-par.tmp` + atomic rename; disk re-validated; own entry only; no downgrade; no tmp leftover).
- Lock `locks/sel-37-913-agentive-par.lock` created on start (no stale lock), deleted on completion (verified gone).
