# Battery report: seg-81-30-trepas-kill

- Target id: `seg-81-30-trepas-kill`
- Claim: "Kill-grade adjudication of 81='tre' (the 'trepas' word-medial reading of the @44-45 junction)."
- Date: 2026-10-09
- Worker: battery worker (subagent 5ada4956-eaba-427f-9a81-8a9e5df9de8c)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). Verified in-session: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

Terms (ASD-STE100): "word-medial" = inside one word. "hapax" = occurs once in the whole stream. "purpose complement" = a "pour + infinitive" phrase that says why (as in "the means to act"). "uniform value" = one value must hold at every window (§7: 67 is the only polyvalence).

## Bar (verbatim, pre-registered before testing)

"(a) corpus test - 'trepas pour + infinitive' in 1841 diplomatic French (zero hits expected); if the @552/@1087 purpose-complement windows cannot host 'trepas', kill 'trepas' as 81's value; (b) any second '[81]pas' contact stream-wide kills or saves the compound arm. Discriminator: the purpose-complement leg set."

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1 (corpus):** "trépas" + "pour" + infinitive (purpose clause) has zero attestations in the 1841 side-period corpus.
2. **C2 (host windows):** the purpose-complement windows @552 (1-based @553) and @1087 (1-based @1088) cannot host 'trepas' as 81's value → kill 'trepas' as 81's value.
3. **C3 (second contact):** any second "81 30" contact stream-wide kills or saves the compound arm; absence = no corroboration.

Adverses listed: "'contrepas' (81='contre') already rejected (zero evidence; 'contre' attribution elsewhere is a red-team tension); the rival-phase offset-1 reparse may dissolve this junction entirely."

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/seg-81-30-trepas-kill.lock` on start (agent id + UTC timestamp); deleted on completion. No stale lock was present.
2. Re-derived the repaired stream in-session. All @-offsets below are 0-based unless marked 1b.
3. Standing premises used, not re-litigated: 00="pour" (A9 grant); 81 class = masculine abstract noun (battery class promote, rests on the purpose-complement family); §7 (67 et/veut is the sole true polyvalence — a value must be uniform across its windows).

## Window-level evidence

**The junction (byte-confirmed).** 0b@44–48, row a1_01: `81 30 62 96 00` (left context `88 43`). The 'trepas' hypothesis reads 81-30 as "tre"+"pas" = "trépas" (death), one word across the junction. Under the standing parse, 30 = "pas" is a free word (30 is not bound anywhere: 30 has its own 44-window profile).

**81's full window census (n=14, byte-exact):** 0b@26, @44, @93, @524, @551, @745, @1086, @1095, @1241, @1402, @1513, @1593, @1599, @1672.

The purpose-complement leg set (the discriminator), all byte-confirmed:
- 0b@26 (a1_00): `55 81 00 34 24` — "[55] [81] pour [34]i…"
- 1b@553 (0b@552, a3_01): `46 55 81 00 86 59` — "que [55] [77=le] [81] pour [86]er est(59)"
- 1b@1088 (0b@1087, a6_05): `02 55 81 00 33 79` — "[02] [55] [81] pour [33]er tout(79)"

Three windows of the frame "le [81] pour + infinitive" — the standing moyen/ordre/droit/besoin family ("the means/the order/the right/the need to [INF]"). 81 must be a complete noun here that licenses a purpose complement.

## Per-clause pass/fail

- **C1 — PASS (corpus zero confirmed).** Systematic search of the 1841 side-period corpus (`code/side-period/corpus/`, 64 texts) for `tr[eé]pas`: 6 noun tokens of "trépas" total, all in RDM-1841-q2/q4 and musset-comedies-proverbes-1850. Every context read and classified: "son trépas ne…", "le trépas de Ronsard", "me conduit au trépas" (verse), "je pleurais votre trépas" (verse), "le trépas du jeune médecin", "la gloire du trépas". **Zero** tokens have "pour" within the next 12 words; zero show "trépas pour + infinitive" anywhere in the corpus. The bar's expected zero is confirmed: "trépas" takes "de"-genitives and direct-object positions (pleurer le trépas), never "pour + infinitive" purpose clauses — death does not take purpose complements.
- **C2 — FAIL at kill grade → KILL 'trepas' as 81's value.** Two independent kill legs:
  - (a) **The frame needs a complete noun; 'tre' is a fragment.** At all three purpose-complement windows (@26/@552/@1087) 81 sits between two free words: "[55] [81] pour(00)". 00='pour' is a standing A9 grant — a free word. Under 81='tre' the windows read "…le tre pour [INF]…" — "tre" is not a French word. The windows force the claim false at kill grade, value-independently (no open value is involved: the neighbors are 55/00/banked verbs).
  - (b) **The junction composition is a hapax with no license anywhere else.** The ONLY window where 81 can fuse into "trépas" is the @44-45 junction (81-30 = "tre-pas"). At the other 13 windows, 81 stands free against neighbors that bar composition: banked 00='pour' (×3), promoted 85 verb-stem (@745), promoted 92 verb (@1672), bound 06 (@1095), granted 87=ce (@1241/@1402), 82='m' (@1599). Under §7 no polyvalence can rescue it. Uniform 81='tre' forces a non-word at 13/14 windows.
- **C3 — MOOT (uninformative).** "81 30" is a stream hapax (1×, byte-confirmed at 0b@44). No second contact exists: the compound arm has zero repetition support, but C3's kill/save condition never fires. The kill rests on C2.

## Adverses answered

- **'contrepas' (81='contre'):** already rejected at battery level (zero evidence); not re-litigated. This battery kills only the 'tre'/'trepas' arm; 81's value stays open.
- **Rival-phase offset-1 reparse:** answered, not ignored. The junction is byte-exact on the repaired (red-team R1) stream with both pencil glosses (i) and (ii) satisfied. The offset-1 reparse would resurrect the 1,846-pair parse that red team killed for violating gloss (i) ("la pre m i er e" at raw 1532). It is not standing; the junction stands on the lane's canonical parse.

## Verdict: KILL

81='tre' is dead as a value, and with it the 'trepas' word-medial reading of the @44-45 junction. The kill is value-independent (rests on banked/standing neighbors, not on any open value) and §7-clean (no polyvalence declared or needed).

## Scope

Kills only the 'tre'/'trepas' value arm. Untouched: 81's masculine-abstract-noun class grant (rests on the purpose-complement leg set, which this battery corroborates); the purpose-complement windows @26/@552/@1087 themselves; the 81-30 junction's segmentation under a different 81 value (the junction is byte-real; only the 'tre'+'pas' composition is dead). Per §4, kills regenerate no follow-ups. 81's value stays open.

## Bookkeeping

- Queue: `seg-81-30-trepas-kill` → status `verdict`, result `kill`, 2026-10-09 (pre-write assert passed — was `queued`/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/seg-81-30-trepas-kill.lock` created on start, deleted on completion (verified gone).
- No standing/red-team verdict contradicted or downgraded; §7 intact; R5005, sealed gates, red-team adjudication queue untouched. Canonical-stream caveat stands (row a1_01 offset unvalidated).
