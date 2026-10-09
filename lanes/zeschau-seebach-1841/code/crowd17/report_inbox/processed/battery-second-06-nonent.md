# Battery report: second-06-nonent — test second-06 != 'ent' at both '94-82-06-06' doublings (NULL — fenced)

- Target id: `second-06-nonent`
- Claim: "test second-06 != 'ent' at both '94-82-06-06' doublings"
- Date: 2026-10-09
- Worker: battery worker (subagent 9db3023d-6057-47a7-8229-d10ce48fa2f5)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). Verified in-session: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Offset note: all @-offsets below are 0-based (queue convention).

Terms (ASD-STE100): "doubling" = two 06 groups in a row ("06 06"). "second 06" = the right-hand 06 of the doubling. "ungranted assumption" = any value, edge rule, or frame reading not in protocol §7 or a red-team-adjudicated finding. "battery grade" = the evidence standard of this pipeline.

## Bar (verbatim, pre-registered before testing)

> name a value for the second 06 parsing both doubling windows with <=1 ungranted assumption

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** A non-'ent' value V for the second 06 parses window W1 (0b@578–587, row a3_02) with <=1 ungranted assumption.
2. **C2:** The same V parses window W2 (0b@1182–1191, row a6_10) with <=1 ungranted assumption.
3. **C3:** Else the second-06 value is fenced with stated cause; no standing red-team verdict is contradicted or downgraded.

Adverses listed: "06's global value ('ent' promoted) argues against a distinct second value; the doubling context is exactly where a distinct value could hide (F61 islet scope question is red-team venue)".

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/second-06-nonent.lock` on start (agent id + UTC timestamp); deleted on completion. No stale lock was present.
2. Re-derived the repaired stream in-session. Census: "94 82 06 06" occurs exactly **2x** stream-wide — 0b@578 (W1) and 0b@1182 (W2). Second 06 at 0b@581 (W1) and 0b@1185 (W2). This matches the parent `seg-94-82-06-f3` census (its @580/@1184 are the first-06 positions).
3. Read the parent battery `seg-94-82-06-f3` (NULL) and sibling `frameA-50-value` (NULL), not duplicated. Standing premises used, not re-litigated: 94="ne" (battery-promoted free word), 82="m" (banked GT letter), first 06 covered by the F61 conditioned islet (pre=82 → 'ent'), 59="est" (provisional; locally confirmed as 'est'-as-word at @1186 by f1), 84="on" (A15), 46="que" (banked GT), §7 (67 et/veut is the sole true polyvalence).
4. Enumerated candidate non-'ent' values V by segmentation family and tested each against both windows.

## Window-level evidence (byte-confirmed)

**W1** (row a3_02, all row-internal):
`0b@570–589 = 94 52 87 78 45 13 55 61 | 94 82 06 06 | 50 10 19 18 14 00 97`
Doubling at @578–581: `94(ne) 82(m) 06 06[V?]`, right follower 50 (value open; 50="ver" kill stands; `frameA-50-value` exhaustively closed the "ent"+X space against 50's 11-window profile).

**W2** (row a6_10 → a7_00 join):
`0b@1174–1193 = 36 74 32 48 59 37 77 78 | 94 82 06 06 | 59 42 06 84 59 46 07 24`
Doubling at @1182–1185, right followers 59 ("est", f1-confirmed word at @1186), 42 (open), 06 ("ent"), 84 ("on").

## Candidate-family elimination

Segmentation families for "94 82 06a 06b" with 94="ne", 82="m", 06a="ent" (F61 islet):

- **Family A — "ne m'ent"+V as one finite verb** (V = "ends"/"end"/"endent"/"erre"/… → "m'entends", "m'entend", "m'entendent", "m'enterre", …). **DEAD at W2, value-independently:** f1-confirmed 59="est" stands immediately right (@1186); a finite verb directly followed by "est" is two adjacent finite verbs — ungrammatical at kill grade. At W1 the family additionally needs an ungranted subject (2sg "tu" for "m'entends"; 3sg subject for "m'entend") from the open 55/61.
- **Family B — "ne m'ent"+V as infinitive/participle** (V = "endre"/"endu"/"ant" → "m'entendre", "m'entendu", "mentant"). **DEAD at both windows:** the infinitive needs a governor (modal/preposition) and the participle needs an auxiliary — neither window supplies one ("55 61" / "le [78]" are not governors at any grade). "ne mentant" without "en" is ungrammatical as an adverbial; as an adjective it needs a head noun, absent.
- **Family C — "ne ment"+V, V standalone word** (V = "pas"/"plus"/"point" → "ne ment pas"). "ment" = 3sg *mentir*, needs a subject. **W1:** subject must come from open 55/61 (1 ungranted) AND "pas [50]" needs 50's role (open; 2nd ungranted) = ≥2. **W2:** "le [78] ne ment pas est [42]" needs (1) 78 nominal-class (ungranted — used as premise in `x-33-37-licensing`, not §7-granted), (2) a clause boundary before "est", (3) a subject for "est [42]" = ≥3. **DEAD at both windows** (fails the ≤1 bar at each independently).
- **Family D — "ne ment"+V noun** (V = "eur" → "menteur"). **DEAD:** bare "ne menteur" — a noun with no determiner after "ne" — is ungrammatical at both windows.
- **Family E — V as standalone word after "ne m'ent".** **DEAD:** "m'ent" is not a French word; no parse exists.
- **Family F — re-segment 82 06a ("m'en…") or otherwise move 06a off 'ent'.** Not battery-grade: contradicts the F61 islet (pre=82 → 'ent') and 06's promoted global value. Fenced as red-team venue, not tested.

No candidate family yields a V parsing W1 within budget (C1 FAIL); no candidate family yields a V parsing W2 within budget (C2 FAIL). The two windows' right contexts (open 50 vs f1-confirmed "est") kill disjoint families, so no single V survives both.

## Adverses answered

1. **"06's global value ('ent' promoted) argues against a distinct second value" — adopted as structural fence cause.** Any successful V ≠ 'ent' would declare 06 polyvalent (ent vs V). Per §7, 67 et/veut is the sole true polyvalence; a new 06 polyvalence is red-team venue and cannot be promoted at battery grade. The bar's success condition is therefore structurally gated even before the empirical failure.
2. **"the doubling context is exactly where a distinct value could hide (F61 islet scope question is red-team venue)" — acknowledged and tested anyway.** The empirical search above came up empty, so the scope question stays open but unfed. F61 itself is unchanged (first 06 covered; second outside scope — that is the question, not a change).

## Scope notes (not re-litigated)

- The standing rival **"ne mentent"** (3pl *mentir*: 82="m" + 06a="ent" stem + 06b="ent" 3pl ending) has second-06 = 'ent' and is therefore **outside this battery's scope**; it is owned by queued `mentent-580-rival` / `w580-subject-61`. Note: at W2 it reads "ne mentent est" — adjacent finite "mentent"/"est" — so the rival is W1-only at best.
- `frameA-50-value`'s exhaustive "ent"+X closure at W1 and f1's 59="est" confirmation at W2 are adopted as premises, not re-run.

## Verdict: NULL — second 06's value fenced (C1 FAIL, C2 FAIL, C3 executed)

No non-'ent' value parses both doubling windows within the ≤1-ungranted-assumption bar, and any such value would additionally require a red-team polyvalence declaration. No standing or red-team verdict contradicted or downgraded; §7 intact.

**Canonicality caveat:** both doublings are canonical-offset objects (rows a3_02, a6_10 carry unvalidated upstream offsets). Verdict holds on the canonical stream per protocol; offset adoption is a red-team act.

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `f61-06-scope-precise` (P3) — byte-precise the F61 islet's scope: census all 44 06-windows for the pre=82 conditioning; confirm or fence which 06 positions the islet actually covers. Bar: conditioning rule stated with byte evidence at battery grade, or the islet fenced as underdetermined.
2. `mentent-w2-killseek` (P3) — kill-seek the "ne mentent" one-word rival at W2: "ne mentent est [42]" (@1182–1187) under f1-confirmed 59="est". Bar: kill iff no grammatical rescue parses W2; distinct from queued `mentent-580-rival` (W1-scoped).
3. `v06-syllabary-close` (P4) — lexicon-driven closure: enumerate every French single syllable V such that "m'ent"+V or "ment"+V is a French word, then test each survivor against both doubling windows. Bar: closed candidate list with per-candidate window verdicts; any survivor spawns a window battery.

## Bookkeeping

- Queue: `second-06-nonent` → status `verdict`, result `null`, 2026-10-09 (pre-write assert passed — was `queued`/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/second-06-nonent.lock` created on start, deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched. `canonical.py` never used.
