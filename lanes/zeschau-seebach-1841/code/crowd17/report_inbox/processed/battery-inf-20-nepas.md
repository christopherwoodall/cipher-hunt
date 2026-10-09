# Battery report: inf-20-nepas

- Target id: `inf-20-nepas` (P2)
- Claim: Test 20 as infinitive at @1703 ('ne pas [20-inf]') with @1270 ('pas [20]' without 'ne') as the second leg — a verbal-20 value that parses both 'pas [20]' windows feeds the poly-20 docket and discriminates the verbal face of 20 from the particle face killed here.
- Date: 2026-10-09
- Worker: battery worker (subagent 77b769f4-ba16-4a91-8036-750626f40dea)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- Indexing: @i = 0-based pair index in the repaired stream (matches the target's convention; verified: '30 20' bigrams at 0-based 1269–1270 and 1702–1703, so 20 sits at @1270 and @1703).
- Lock: code/crowd17/next-token/locks/inf-20-nepas.lock (created on start, deleted on completion).

## Bar (verbatim, pre-registered before testing)

"a verbal-20 value that parses both 'pas [20]' windows"

Numbered pass/fail clauses (restated before testing, not modified after):

1. A verbal (infinitive) value for 20 parses @1703 ('94 30 20 62' = 'ne pas [20] …') grammatically under standing values.
2. The same verbal value parses @1270 ('24 30 20 64 47 76' = '[24] pas [20] qui ce [76] …') grammatically under standing values.
3. Adverse: coordinates with, does not duplicate, the existing P1 poly-20-docket (from noun-20-value follow-up #3).

## Method

1. Re-derived the repaired stream in-session: 1,847 pairs, 96 types confirmed; n(20)=15 byte-exact (0-based @280/@307/@490/@642/@668/@703/@741/@760/@839/@873/@958/@1135/@1224/@1270/@1703).
2. Confirmed '30 20' occurs exactly 2× stream-wide (bigram starts @1269, @1702) — the two bar windows are the whole population.
3. Parsed both windows under standing values: banked GT (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce); provisional (59=est, 77=le); promoted/lead (06=ent, 30=pas conditional, 24=finite-modal, 76=noun battery-promoted 2026-10-08, 94=ne R17-001 strong lead, 98=vient battery-promoted, 62=il demonstrated on 62-94 frames). Kills respected: 20='fois', 20~17 split.
4. Tested whether any verbal value for 20 parses both windows; checked value-independence of any obstruction.
5. Read the parent battery (ellipsis-760, processed) and the poly-20-docket queue entry; did not duplicate them.

## Window-level evidence (@-offsets, 0-based)

**W1 @1703 (row a8_06, rowpos 10):** `… 85 33 94 30 [20] 62 94 88 26 12 06 29 40 …`
= `… [85] [33] ne[94] pas[30] [20] [62] ne[94] [88] [26] …`
- 'ne pas [20]' is the canonical French negative-infinitive frame. 20 sits in a verbal-complement slot (parent battery's finding, adopted).
- Right edge parses cleanly with a clause boundary after 20: '[62-il] ne[94] [88-verb]' = 'il ne [88-verb]' (literary 'ne' alone), so 'ne pas [20-inf]. Il ne [88-verb] …'. Any infinitive value is structurally licensed here.
- Caveat (stated, not hidden): the frame is conditional on 94='ne' (R17-001 strong lead, not granted) and on 62='il' (demonstrated on 62-94 frames, not promoted).

**W2 @1270 (row a7_02, rowpos 22):** `… 69 88 24 30 [20] 64 47 76 87 76 48 56 85 …`
= `… [69-'ce'] [88-verb] [24-modal] pas[30] [20] qui[64] ce[47] [76-noun] ce[87] [76] …`
- The 'pas [20]' frame selects a verbal element (parent battery's finding, adopted): 'ne [24] pas [20-inf]' with ne-drop.
- The right edge '64 47 76' = 'qui ce [76-noun]' is ungrammatical under standing values: 64=qui (granted) requires a verb directly after it; 'ce [47] [76-noun]' (47=ce A4, 76=noun battery-promoted) supplies none. 'qui ce [noun]' is not a French construction (not a cleft — no verb; not 'ce qui' — wrong order; not interrogative 'qui ça' — wrong register and semantics).
- The obstruction is VALUE-INDEPENDENT: whatever value X fills 'pas [X]', the continuation 'qui ce [76-noun]' remains ungrammatical. No infinitive, participle, finite verb, noun, adjective, or adverb value for 20 changes the grammaticality of 'qui ce [76-noun]'.
- '64 47' ('qui ce') occurs exactly 2× stream-wide (@1271 here, @1717 as '30 64 47' = 'pas qui ce [68]' — a 20-independent occurrence of the same unparseable bigram, confirming the construction is structural, not 20-specific).
- '47 76' and '87 76' each occur exactly 1× stream-wide, both inside this window — there is no stream precedent for either 'ce [76-noun]' resolving differently or for 76='est'.
- Sole grammatical escape: 'qui c'est' via 76='est' (e.g. 20='savoir': 'ne [24] pas savoir qui c'est'). This contradicts battery-promoted 76=noun (2026-10-08, 21 windows) and is red-team venue, not adoptable at battery grade. Recorded as the live escape hatch, not as a finding.

## Per-clause pass/fail

1. @1703 parses under a verbal-20 value: **PASS.** 'ne pas [20-inf]' is a clean negative-infinitive frame; the right edge resolves with a clause boundary ('il ne [88-verb]'). Consistent with the parent battery.
2. @1270 parses under the same verbal value: **FAIL AT KILL GRADE.** 'qui ce [76-noun]' admits no grammatical parse under standing values, and the obstruction is value-independent — no verbal value for 20 can satisfy this clause while 64=qui, 47=ce, and 76=noun stand. The window forces the existential claim false.
3. Adverse (poly-20-docket coordination): **PASS.** The P1 poly-20-docket ('RED-TEAM DECISION: conditioned-polyvalence candidacy, 20 = NOUN vs DET/ADJ') is untouched and unduplicated — this target tested the verbal face, a disjoint question. No red-team, R5005, or sealed-gate contact.

## Verdict: KILL

The bar — 'a verbal-20 value that parses both 'pas [20]' windows' — fails at kill grade at @1270. Under standing values no verbal value for 20 parses both windows, because 'qui ce [76-noun]' is ungrammatical value-independently.

**Explicitly NOT killed (scope fence):**
- The verbal FACE of 20: the parent battery's finding stands — 20 sits in a verbal slot at both 'pas [20]' windows, and @1703's 'ne pas [20-inf]' is a clean negative-infinitive frame. What dies is the VALUE-SEARCH (naming one verbal value for both windows), not the face.
- The P1 poly-20-docket (red-team venue, untouched).
- 76=noun (battery-promoted, untouched); the 'qui c'est' / 76='est' escape is flagged for red-team awareness, not adopted.
- No standing or red-team verdict contradicted or downgraded; §7 intact (no polyvalence declared or implied).

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-inf-20-nepas.md (this file)
- Queue: `inf-20-nepas` → status `verdict`, result `kill` (temp-file + rename; pre-write assert confirmed queued/verdictless; only this entry touched; JSON re-validated)
- Lock created on start, deleted on completion. `canonical.py` never used; R5005, sealed gates, red-team adjudication queue untouched.
- Kill verdict — no follow-ups required per protocol. Red-team note: if the red team ever revisits 76's class, the 'qui c'est' escape re-opens the @1270 leg and this kill re-opens with it.
