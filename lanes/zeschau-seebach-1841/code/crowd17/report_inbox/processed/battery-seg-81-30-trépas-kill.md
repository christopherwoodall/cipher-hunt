# Battery report: seg-81-30-trépas-kill

- Target id: `seg-81-30-trépas-kill`
- Claim: "kill-grade adjudication of 81=\"tré\" via corpus test of \"trépas pour + infinitive\""
- Date: 2026-10-09
- Worker: battery worker (subagent 663c0461)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). Verified in-session: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

Terms (ASD-STE100): "hapax" = occurs once in the whole stream. "purpose complement" = a "pour + infinitive" phrase that says why (as in "the means to act"). "uniform value" = one value must hold at every window (§7: 67 is the only polyvalence).

## Bar (verbatim, pre-registered before testing)

"(a) corpus test — \"trépas pour + infinitive\" in 1841 diplomatic French (zero hits expected); if the @552/@1087 purpose-complement windows cannot host \"trépas\", kill \"trépas\" as 81's value; (b) any second \"[81]pas\" contact stream-wide kills or saves the compound arm. Discriminator: the purpose-complement leg set."

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1 (corpus):** "trépas" + "pour" + infinitive (purpose clause) has zero genuine attestations in the lane's 1841 side-period corpus.
2. **C2 (host windows):** the purpose-complement windows (1b@552 and 1b@1087, the "55 81 00" frames) cannot host "trépas"/"tré" as 81's value → kill "trépas" as 81's value.
3. **C3 (second contact):** any second "81 30" contact stream-wide kills or saves the compound arm; absence = no corroboration.

Adverses listed: none.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/seg-81-30-trépas-kill.lock` on start (agent id + UTC timestamp); deleted on completion. No stale lock was present.
2. Re-derived the repaired stream in-session. All @-offsets below are 0-based unless marked 1b.
3. Standing premises used, not re-litigated: 00="pour" (A9 grant); 30="pas" (R17-004); 81 class = masculine abstract noun (battery promote, rests on the purpose-complement leg set); §7 (67 et/veut is the sole true polyvalence — a value must be uniform across its windows).
4. **Duplicate-target note (found before testing):** the queue holds a byte-identical sibling target `seg-81-30-trepas-kill` (no accent) at `status: verdict`, result `kill`, report `code/crowd17/report_inbox/processed/battery-seg-81-30-trepas-kill.md`, completed 2026-10-09. Same claim, same bars, same id modulo the accent — a naming artifact, not a new question. Per §5 ("never downgrade an existing verdict") I did not re-litigate the bar from scratch; instead I independently spot-verified the sibling's decisive byte facts and its corpus conclusion, corrected one writeup-level indexing slip, and record the same kill here. The supervisor should merge the two queue entries.

## Window-level evidence (independently verified)

**81's full window census (n=14, byte-exact):** 0b@26, @44, @93, @524, @551, @745, @1086, @1095, @1241, @1402, @1513, @1593, @1599, @1672.

**The junction (byte-confirmed).** 0b@44–48, row a1_01: `81 30 62 96 00` (left context `88 43`). The "trépas" hypothesis reads 81-30 as "tré"+"pas" = "trépas" (death), one word across the junction.

**The "81 30" contact is a stream hapax:** exactly 1 window stream-wide (0b@44). No second contact exists.

**The purpose-complement leg set (the discriminator), byte-confirmed:**
- 0b@26 (a1_00): `55 81 00 34 24` — "[55] [81] pour [34]i…" (cells 21–30 = `43 29 47 33 55 81 00 34 24 30`).
- 1b@552 (0b@551, a3_01): `46 55 81 00 86 59` — "…[46] [55] [81] pour [86]…" (cells 546–556 = `46 24 47 46 55 81 00 86 59 34 17`).
- 1b@1087 (0b@1086, a6_05): `02 55 81 00 33 79` — "…[02] [55] [81] pour [33]…" (cells 1081–1091 = `52 89 24 02 55 81 00 33 79 80 06`).

Three windows of the frame "[55] [81] pour + [INF]" — the standing moyen/ordre/droit/besoin family ("the means/the order/the right/the need to [INF]"). 81 must be a complete noun here that licenses a purpose complement.

**Correction to the sibling report's writeup:** its 0-based @-labels for the second and third windows are off by one (it prints 0b@552 and 0b@1087; the 81 cells are byte-exact at 0b@551 and 0b@1086). The printed frames and the 1-based labels (1b@552, 1b@1087 — matching this target's bar) are correct. No byte fact changes.

## Per-clause pass/fail

- **C1 — PASS (corpus zero confirmed, re-verified).** Re-ran the corpus test on the current 76-text lane corpus (`code/side-period/corpus/`, ~35M chars) with word-boundary regex `[Tt]r[ée]pas` excluding the "outrepasser" verb family: 35 genuine noun tokens of "trépas". Nine have "pour" within 120 chars after, but every one dissolves on reading: "pour" precedes the token ("j'affrontais le trépas"), starts a new verse clause ("Pour la femme innocente"), is dative ("un bienfait pour moi"), is exchange-"pour" ("trépas pour trépas"), or governs the main verb, not the noun ("J'ai semé par milliers les trépas entre nous Pour t'apprendre mon nom" — the purpose clause attaches to "semer"). **Zero genuine "trépas pour + infinitive" purpose complements.** The bar's expected zero holds on the larger corpus: "trépas" takes "de"-genitives and direct-object positions (pleurer le trépas), never "pour + infinitive" purpose clauses — death does not take purpose complements.
- **C2 — FAIL at kill grade → KILL "trépas" as 81's value.** Two independent kill legs:
  - (a) **The frame needs a complete noun; "tré" is a fragment.** At all three purpose-complement windows (0b@26/@551/@1086) 81 sits between free words: "[55] [81] pour(00)". 00="pour" is a standing A9 grant — a free word. Under 81="tré" the windows read "…[55] tré pour [INF]…" — "tré" is not a French word. The windows force the claim false at kill grade, value-independently (neighbors are 55/00/banked verbs; no open value involved). Under 81="trépas" (full word) the frame reads "…[55] trépas pour [INF]…" — but C1 proves that construction does not exist in the register.
  - (b) **The junction composition is a hapax with no license anywhere else.** The only window where 81 can fuse into "trépas" is the 0b@44 junction (81-30 = "tré-pas"). At the other 13 windows, 81 stands free against neighbors that bar composition: banked 00="pour" (×3), promoted 85 verb-stem (@745), promoted 92 verb (@1672), bound 06 (@1095), granted 87="ce" (@1241/@1402), 82="m" (@1599). Under §7 no polyvalence can rescue it. Uniform 81="tré" forces a non-word at 13/14 windows.
- **C3 — MOOT (uninformative).** "81 30" is a stream hapax (1×, byte-confirmed at 0b@44). No second contact exists: the compound arm has zero repetition support, but C3's kill/save condition never fires. The kill rests on C2.

## Adverses

None listed.

## Verdict: KILL

81="tré" is dead as a value, and with it the "trépas" word-medial reading of the 0b@44 junction. The kill is value-independent (rests on banked/standing neighbors and the corpus construction test, not on any open value) and §7-clean (no polyvalence declared or needed). This adopts and re-verifies the sibling target's KILL; no standing verdict contradicted or downgraded.

## Scope

Kills only the "tré"/"trépas" value arm. Untouched: 81's masculine-abstract-noun class grant (rests on the purpose-complement leg set, which this battery corroborates); the purpose-complement windows themselves; the 81-30 junction's segmentation under a different 81 value (the junction is byte-real; only the "tré"+"pas" composition is dead). Per §4, kills regenerate no follow-ups. 81's value stays open.

**Supervisor note:** queue entries `seg-81-30-trepas-kill` and `seg-81-30-trépas-kill` are the same claim under two ids (é vs e); consider merging.

## Bookkeeping

- Queue: `seg-81-30-trépas-kill` → `status: verdict`, `result: kill`, 2026-10-09 (pre-write assert passed — was `queued`/verdictless; temp-file + rename; JSON re-validated from disk; own entry only; no downgrade of any existing verdict).
- Lock `locks/seg-81-30-trépas-kill.lock` created on start, deleted on completion (verified gone).
- No standing/red-team verdict contradicted or downgraded; §7 intact; R5005, sealed gates, red-team adjudication queue untouched. Canonical-stream caveat stands (row a1_01 offset unvalidated).
