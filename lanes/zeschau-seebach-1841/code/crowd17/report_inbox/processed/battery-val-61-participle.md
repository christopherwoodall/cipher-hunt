# Battery verdict: val-61-participle

- Target: `val-61-participle` (battery-queue.json, priority 3, status queued)
- Claim: "Name 61's class at @927 ("71 fois [61] par [48]"): feminine past participle locking the "[Q] fois [part-fem] par [agent]" frame, or re-derive the frame."
- Date: 2026-10-09
- Stream: repaired 1,847-pair / 96-type parse (repaired_offsets.json + upstream-ct_R5005.txt, re-derived in-session; asserts held). `canonical.py` never used.

## Bar (verbatim, pre-registered)

"61 named as feminine past participle at battery grade with zero contradiction, else fence the participle frame."

Numbered clauses:
- C1: 61 is named as feminine past participle at @926 (0-based; the claim's "@927" is 1-based) with battery-grade evidence and zero contradiction → PROMOTE.
- C2: else fence the participle frame → NULL.

## Method

1. Byte-confirmed the window on the repaired stream.
2. Rendered all 18 windows of 61 (n(61)=18) with standing values to check for contradictions.
3. Corpus test of the "[Q] fois [part] par [agent]" frame (97 files, ~59M chars 1841 French).
4. Corpus test of gender agreement in the "fois [part] par" slot (feminine forced?).
5. Tested the "par [agent]" arm against standing 48='e'.

## Findings

### Window (byte-exact)

`@923=65 @924=71 @925=17 @926=61 @927=96 @928=48 @929=82 @930=98`
= "[65-N] [71] fois [61] par e m vient..." (17=fois granted, 96=par granted, 48='e' promoted letter tier R17-003, 82='m' pencil GT).

### The frame is corpus-real — but the slot is participle-only, gender-open

"fois X par" census: **34 raw hits, all participles** ("révélée", "protégée", "consacrée", "établie", "indiquée", "appuyée", "renouvelées", "interrompues", ...). Full-shape examples:
- "première fois révélée par la découverte de la correspondance"
- "cette fois protégée par son mari"
- "plusieurs fois reçu par des cheicks arabes"
- "une fois consacrée par leur génie"
- "une fois établie par les mœurs"

So the "[Q] fois [part] par [agent]" construction is productive 1841 French, and the "fois _ par" slot admits **only participles** (no noun/adjective/adverb/infinitive fits). Participle is the sole grammatical class for 61 at @926.

### C1 fails on two independent grounds

**Ground 1 — feminine is not forced.** Masculine participles occur in the identical slot:
- "une fois ému par ses témoignages" (ému, masc.)
- "plusieurs fois reçu par des cheicks arabes" (reçu, masc.)
- "une fois fini par triompher" (fini, masc.)
The participle agrees with an implied subject, not necessarily with "fois". At @926 no gendered neighbor forces feminine (71 gender-open, 65 gender-open). The bar's "feminine" specification cannot be established at battery grade.

**Ground 2 — the "par [agent]" arm does not parse.** The frame needs "par [agent]"; at @927–928 we have "par [48]" = "par e". 48='e' is promoted letter tier (R17-003); val-48-initial NULL (2026-10-09) fenced 48 as letter-tier everywhere it parses. "par e" is not a grammatical agent (agents are NPs: "par la découverte", "par son mari", "par des cheicks"). No composition rescues it ("par em" via 82='m' is a non-word; "emvient" via 98 is a non-word).

### No contradiction with standing verdicts

61 is class-open globally (absent from table-registry.json). "pren" killed globally (seg-61-pren-polyvalence) — a participle is not "pren", no conflict. Adjective fenced at @645 (val-61-646-secondleg-sweep) was locus-level. val-61-premier locus-level @1556 ("première fois") does not conflict (no uniform 61 grant). n(61)=18; no window forces a class contradicting participle-61 at @926.

### Verdict: NULL (fence executed per C2)

C1 FAIL (feminine unforced; agent arm unparsed) / C2 FIRES.

**Fence (stated cause):** the "[Q] fois [part-fem] par [agent]" frame as specified does not hold at @926 at battery grade. The participle CLASS remains the sole grammatical occupant of the "fois _ par" slot, but naming 61 as *feminine* past participle — and completing the frame with an agent — is blocked on (a) the agreement controller and (b) the "par e" residual.

## Scope

Fences only the bar's specified frame at @926. Untouched: 61's class-open status, the "pren" global kill, the @645 adjective fence (locus-level), val-61-premier @1556 (locus-level), 48='e', 98='vient' LEAD, §7 (no split declared), all standing/red-team verdicts. No value named. Canonical-stream caveat stands.

## Follow-ups proposed (§4, all verified ABSENT from battery-queue.json)

1. `part-61-gender-ctrl` (P4) — determine 61's agreement controller at @926: does the participle agree with "fois" (feminine) or an implied subject (gender open)? A feminine controller names the feminine participle.
2. `par48-e-agent` (P4) — resolve "par [48]" at @927: test composition of 48 with following cells, or re-parse "par" as heading a non-agent constituent. A parsing agent re-opens the frame.
3. `fois-part-abs-frame` (P4) — corpus census of agentless "fois [part]" (absolute use, no "par"): if productive, the frame survives without the agent arm.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-61-participle.md`
- Queue: `val-61-participle` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.val-61-participle.tmp` + atomic rename; disk re-validated; own entry only; no downgrade)
- Lock `locks/val-61-participle.lock`: created on start (agent c4d374cc, 2026-10-09T19:50:00Z, no stale lock), deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
