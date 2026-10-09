# Battery report: ent-right-attach-sweep — 06's rightward attachment in the 6 word-initial legs

- Target: `ent-right-attach-sweep` (battery-queue.json, priority 3 in brief / 2 in queue, status queued)
- Claim: "classify 06's RIGHTWARD attachment in the 6 word-initial legs (@271/@370/@522/@789/@1080/@1667): does "ent"+follower ever form a real French word?"
- Worker: 2412a0ce-8a35-4262-bd0d-d093262fe224
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`). `canonical.py` NOT used. R5005 untouched.
- All @-offsets are pair indices in the repaired stream.
- Lock: `code/crowd17/next-token/locks/ent-right-attach-sweep.lock` created on start; no stale lock present.
- Predecessor: `battery-wordbound-30-06-importent` (null, 2026-10-09) — 06's left-attachment profile is bimodal (stem-attach vs word-initial); the 6 control legs below are its WORD-boundary (word-initial) legs. Follow-up 2 of that report is this target.

## Bar (verbatim, pre-registered)

"kill the two-word "pas"+"ent[65/62/60]" parse at the four target windows iff >=2 of the 6 control legs force non-words on the rightward attachment"

Numbered clauses (frozen before testing):
1. At least 2 of the 6 control legs (@271/@370/@522/@789/@1080/@1667) FORCE a non-word when 06 attaches rightward onto its follower, under licensed values only (standing promoted/provisional/ground-truth; battery-grade class verdicts where noted).
2. If clause 1 passes, the two-word parse "pas" + "ent[65/62/60]" (30 06 attaching rightward into one word) is KILLED at the four target windows @1251/@1327/@1561/@1733.

## Method

Re-parsed the repaired stream fresh (1,847 pairs confirmed). For each control leg read the 06 window byte-exact, took the immediate follower syllable, and spelled "ent"+follower under the follower's licensed value(s) from standing verdicts (protocol §7) and ratified registry tiers. A leg "forces" a non-word only if every licensed reading of the follower yields a non-French string and no longer French word begins with that string. Value-open followers are NEUTRAL (cannot force, cannot license). French test set: 1841 diplomatic French.

## Window-level evidence (byte-exact, repaired stream)

Control legs (06 at @n, follower at @n+1):

- @271 (row a2_03): `73 47 11 | 06 67 | 33 29 89` — left 11="la" (pencil ground truth), follower 67.
  67 is the standing et/veut polyvalence (sole true polyvalence, protocol §7; positional rule: 67="veut" iff follower infinitive-shaped). 67's follower here is @273=33, value open, so the rule cannot fire and BOTH arms stay live. "ent"+"et" = "entet" — not French. "ent"+"veut" = "entveut" — not French. No French word begins "entet"/"entveut". FORCES NON-WORD.
- @370 (row a2_06): `61 70 17 | 06 21 | 65 63 29` — left 17="fois" (promoted), follower 21.
  21 is ratified noun class-level, value open (registry ["noun","cls"]; battery value search closed at battery grade, val-21-reopen KILL). Unspellable. NEUTRAL.
- @522 (row a3_00): `70 91 77 | 06 55 | 81 97 47` — left 77="le" (provisional), follower 55.
  55 is battery-grade verb class, value open (ver78-1670-5581 PROMOTE: "'pren'-shaped stem implied", value not named). Unspellable. NEUTRAL. (Note: that same report fences W2 @523 as "06 syllabic here, not '-ent'" per the battery 06-attachment rule — either way the follower is value-open, so the leg stays neutral.)
- @789 (row a5_04): `74 65 84 | 06 77 | 64 46 07` — left 84="on" (promoted, A15), follower 77.
  77="le" (provisional, standing; registry ["le","prov"]; 228 battery mentions for "le", rival one-offs none live). "ent"+"le" = "entle" — not French, and no French word begins "entle". FORCES NON-WORD.
- @1080 (row a6_05): `77 78 64 | 06 52 | 89 24 02` — left 64="qui" (promoted), follower 52.
  52 value open ("telle" 52-37 candidate killed; absent from registry). Unspellable. NEUTRAL.
- @1667 (row a8_05): `94 84 64 | 06 91 | 11 78 55` — left 64="qui" (promoted), follower 91.
  91 value open (absent from registry). Unspellable. NEUTRAL.

Target windows (30 at @n; the parse under test is "pas" + "ent[65/62/60]" as two words):

- @1251 (row a7_02): `67 46 26 | 30 06 65 | 46 01` — follower 65, ratified noun class-level, value open.
- @1327 (row a7_04): `62 98 56 | 30 06 62 | 94 70` — follower 62="il" (lead tier; "entil" would be the two-word reading — non-word).
- @1561 (row a8_01): `17 11 26 | 30 06 60 | 71 50` — follower 60, value open (60="dit" killed at kill grade).
- @1733 (row a8_07): `15 01 56 | 30 06 60 | 12 48` — follower 60, value open.

## Per-clause results

1. >=2 control legs force non-words on rightward attachment: PASS. @271 ("entet"/"entveut") and @789 ("entle") each force a non-word under all licensed follower readings. The other four legs are neutral (followers value-open: 21 noun-cls, 55 verb-cls, 52 open, 91 open) — none licenses a positive "ent"+follower word either.
2. Two-word "pas"+"ent[65/62/60]" parse killed at the four target windows: FIRES. @1251, @1327, @1561, @1733 — the parse requiring 06 to attach rightward into "ent"+[65/62/60] is dead, because 06 demonstrably does not attach rightward where the attachment is testable.

## Answer to the claim

"ent"+follower NEVER forms a real French word in the testable legs (2/6 force non-words; 4/6 untestable with value-open followers, and no leg licenses a word). 06's word-initial profile is: standalone "ent", no rightward attachment.

## Adverses (answered, not ignored)

- Adverses listed: none.
- Natural adverse — "the 4 neutral legs could revive 'ent'+follower once 21/55/52/91 resolve": the kill does not depend on them. The 2 forced legs (@271, @789) already satisfy the bar under standing values, and no neutral leg currently licenses a counter-word. Re-open condition is explicit (see caveat).
- No standing or red-team verdict contradicted or downgraded. The wordbound-30-06-importent null's "two-word holds neutral" was a battery-level neutral under its own bar, not a red-team verdict; this target's bar explicitly authorizes the kill on new rightward-attachment evidence.

## Caveat (dependency)

@789's force rests on 77="le" (provisional tier). If the red team ever re-values 77, @789 re-opens; @271's force (standing et/veut polyvalence, both arms non-words) has no such dependency. The kill stands at battery grade under current standing values.

## Surviving parse space at the four targets

"pas" + "ent" (06 standalone, word-final or its own token) + follower; or a re-opening of 30's value (gated follow-up `importe-30-reopen-gate` already exists from the predecessor report). The @1327 lead 62="il" ("entil" non-word) independently corroborates the kill at that window.

## Verdict

**kill** — the two-word "pas"+"ent[65/62/60]" parse is killed at @1251/@1327/@1561/@1733. Bar clause 1 passes (2 of 6 control legs force non-words: @271, @789); clause 2 fires. No follow-ups required (kill, not null); the only re-opener is a red-team re-valuation of 77 or 67, which no battery target can supply.

## Record

- Queue: `code/crowd17/next-token/battery-queue.json` → `ent-right-attach-sweep` status `verdict`, verdict `{"result": "kill", "report": "code/crowd17/report_inbox/battery-ent-right-attach-sweep.md", "date": "2026-10-09"}` (temp-file + rename; pre-write assert confirmed queued/verdictless; only this entry touched; no downgrade).
- Lock `code/crowd17/next-token/locks/ent-right-attach-sweep.lock` deleted on completion.
