# Battery PRIN-81 — analysis (crowd14/prin81)

## 1. Byte-exact window re-derivation (repaired 1,847-pair stream)

Stream rebuilt from `code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt` (drag `common.load_stream`; asserts pass:
1847 pairs, 96 groups, "la première" anchors @754/@1034). Never canonical.py.

**Window @1240** (pairs 1239–1247):
`67 - 77 - 81 - 87 - 11 - 00 - 33 - 16 - 00`
- @1239=67 → "et" via ISLET-4 standing rule (suc==77, pre=40∉{21,11}, veut-conditions false)
- @1240=77 → "le" (provisional, F37); @1241=81 → ? ; @1242=87 → "ce" (provisional)
- @1243=11 → "la" (GT); @1244=00 → "pour" (STRONG LEAD, F46/F47)
- Reading A: "et le prince la pour [33-inf] …"
- Reading B: "et le [81] cela pour [33-inf] …"

**Window @1401** (pairs 1400–1408):
`67 - 77 - 81 - 87 - 11 - 00 - 11 - 95 - 46`
- @1400=67 → "et" (ISLET-4, suc==77, pre=40∉{21,11})
- @1401=77 → "le"; @1402=81 → ? ; @1403=87 → "ce"
- @1404=11 → "la" (GT); @1405=00 → "pour" (STRONG LEAD)
- Reading A: "et le prince la pour la [95] …"
- Reading B: "et le [81] cela pour la [95] …"

Byte-parallelism confirmed: both windows are `67-77-81-87-11-00`
(Leg A positional: PASS). Both windows lie outside the repaired region
(pairs 748–772) — no re-pair caveat. The 68-unvalidated-offsets caveat is
the standing lane conditional, unaffected.

## 2. Post-context adverse ("la pour") — corpus test, pre-registered

Pool: 34 corpus files, 4,220,440 tokens, lane tokenizer verbatim.

| test | pattern | hits | verdict |
|---|---|---|---|
| T1 | la+pour | 12 | all constituency-read (below) |
| T2 | cela+pour | 25 | grammatical, era-solid |
| T3 | le+prince+la | **0** | reading-A frame unattested |
| T4 | le+prince | 809 | baseline sane |
| T5 | prince+pour | 7 | "prince" takes "pour" directly — never via "la" |
| T6 | et+le+prince | 33 | pre-context frame sane |

**T1 constituency reading (12 hits):**
- 8× "là" (adverb "there") mis-OCR'd/tokenized as "la": "n'était là pour
  avaler", "trouvée là pour traverser", "sera là pour appuyer",
  "nous sommes là pour empêcher", etc.
- 3× "poursuite" split across line-break/OCR: "dans la poursuite de
  l'affaire grecque", "contre la poursuite d'un plan" (×2).
- 1× genuine pronoun+preposition: "prenez-la pour évangile" (Pozzo di Borgo)
  — "prendre la pour X" = take it for X. **Frame: transitive verb +
  object pronoun + "pour".** Inapplicable to "le prince la pour [inf]"
  (noun + pronoun + "pour", no governing verb).

**Adverse verdict:** "la pour" in the cipher's post-context — bare
article/pronoun "la" directly before preposition "pour" with no governing
verb — is **era-fenced: 0 genuine hits on 4.22M tokens.** Reading A
("et le prince la pour …") is ungrammatical in 1840s diplomatic French.
The adverse does NOT force re-reading of 11="la" (GT) or 00="pour"
(STRONG LEAD): both stand untouched; it is the "le prince" reading that
dies. **No conflict to escalate — the GT/strong-lead are not disturbed.**

## 3. "cela" ambiguity adjudication (F107)

The two readings are mutually exclusive (share cell 87):
- A: 77-81-87 = "le prin|ce", 11 = "la" (stranded article)
- B: 77-81 = "le [81]", 87-11 = "cela" (standing unit)

Evidence:
- "cela" = 87-11 ×7 standing unit (crowd5, frenchman-verified ear-spelling;
  87→11 P=0.219) — pre-existing, not battery product.
- "cela pour": 25 era attestations (T2), incl. "n'attend que cela pour
  remplir", "tout cela pour faciliter", "je tiens cela pour évident".
- Reading A: "le prince la" era-0 (T3); "la pour" in-frame era-0 (T1).
- Bonus structural leg for B: @1244-1245 = 00-33 = "pour [33-infinitive]",
  the independently established F-C "pour 33" frame (round-12
  identifier33) recurring a third time right after "cela".

**Adjudication: reading B kills reading A at both windows, decisively.**
"cela"@1242/@1403 confirmed; recommend clearing the segmenter `live*`
flag to `live` (red-team gate). The F107 "unresolvable" is resolved:
it was resolvable via post-context grammaticality once tested.

## 4. F-C@1088 anchor assessment

F-C = 00-33-79-80-06 @1087–1091 ("pour [33-inf] tout 80 06"; 79="tout"
per F109). 81 flanks at @1086 (55-81-00) and @1095 (55-81-06).

Under 81="prin":
- @1086: forward pairing blocked (00="pour" is a complete word) → needs
  backward "X-prin" word. Corpus check (4.22M tokens): word-final "-prin"
  outside the prin* family = 144 tokens, ALL OCR garbage — 142× German
  Fraktur fragments ("prin zessin"=Prinzessin, "prin cip"=Prinzip,
  "prin zen"=Prinzen) + "entsprin"/"ronprin" fragments. **Zero French
  words end in the syllable "prin."** @1086 cannot form a word under
  81="prin" — hard tension.
- @1095: "prin"+06; 06's oracle value "ent" requires pre==82 (pre is 81
  → unvalued); no "printemps"/"principe" support for 06.

**Verdict: TENSION, not strengthening.** If 81 promoted to "prin", both
F-C flanks would need re-explanation. 81="prin" is not an anchor pair
for F-C; it is a second independent strike against the value.

## 5. Remaining 81s (14 total)

Only @1241/@1402 have the 81-87 ("prin-ce") shape. @745 (77-81-85),
@1599 (77-81-82) are "le 81 X", X≠87 — no "prin" support. No independent
leg for 81="prin" exists anywhere in the stream.

## Battery verdict: KILL

- Leg A (positional): PASS — but it is the docket item itself, not an
  independent leg.
- Leg B (corpus): FAIL — reading-A frame era-0; post-context fenced.
- Adverse: resolved AGAINST the lead (no GT/strong-lead disturbed).
- Ambiguity: resolved for "cela", killing "le prince".
- F-C anchor: tension, not support.
- F108 context: drag real 9 vs null 13.1±5.2 (0.8σ BELOW null mean,
  FDR≈1.4) — the hit is FDR-consistent noise, as predicted.

81 stays UNIDENTIFIED. The bytes at @1240–1243/@1401–1404 are
"et le [81] cela pour …" with "cela" confirmed. Recommend: segmenter
clears `live*`→`live` on "cela"@1242/@1403; drag docket item "le prince"×2
closed as chance artifact; no change to 11="la" (GT), 00="pour"
(STRONG LEAD), 77="le" (provisional), 87="ce" (provisional).

Lane gate: red-team adjudication required before merge (standing rule).
