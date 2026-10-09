# Battery report: gerund-60-1688

- Target id: `gerund-60-1688`
- Claim: "test 60 as gérondif at @1689 ('tout en [60]'); a licensed gerondif-60 re-opens the H-14 route with 27 as sole open"
- Date: 2026-10-09
- Worker: battery worker (subagent 8b6c78cd-739d-455a-9695-2743a3d68b30)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session). `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Offset note: the brief uses 1-based @1689 (the "tout" of the phrase). This report uses the queue convention, 0-based: the phrase "79 14 60" spans 0-based @1688–1690. Same locus.

Terms (ASD-STE100): "gérondif" = the French "en + present participle" form ("en marchant", "while walking"). "Licensed" = every element has a standing lane license (granted/promoted/battery-grade) and no standing verdict contradicts the parse. "Battery grade" = the evidence standard of this pipeline.

## Bar (verbatim, pre-registered before testing)

"promote iff \"tout en [60]\" parses as licensed gerondif at battery grade; else fence with stated cause"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** "tout en [60]" parses as a licensed gérondif ("tout en" + present participle of the 60-verb) at battery grade → PROMOTE.
2. **C2 (else-arm):** if it does not parse, fence with stated cause → NULL (fence executed).

Adverses listed: none.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/gerund-60-1688.lock` on start (agent id + 2026-10-09T12:06:30Z); no prior/stale lock; deleted on completion.
2. Re-derived the repaired stream byte-exact in-session (1,847 pairs / 96 types asserted).
3. Read the parent battery (`battery-complement-14-60-27-head.md`, NULL 2026-10-09) and the standing gerund/60 record before testing; adopted, never re-litigated:
   - 79="tout" granted (A5); 14="en" battery PROMOTE (en14-value-tighten; core-14-622-bank corroborated these very windows as 'en'-frames; red-team ratification pending, used as given per the parent battery).
   - 60 verb-class at battery grade (split-60-verbs: bare-60 verb, -dre family, vs ent-60 verb, two items sharing syllable 60 — no value named either side).
   - Gérondif model: "en [stem]" with unspelled -ant (en85-gerund-reaudit PROMOTE, 4/5 "en [85]" legs confirmed as gerund frames); 58='ant' KILLED (ant-58-ending), so no spelled participle ending is expected.
   - Present participle is an unkilled arm for 60 (npframe-60-454 enumerated finite verb / present participle / past participle; only the PAST participle "dit" was killed at kill grade by participle-60-newvalue).
4. 1841 diplomatic French throughout.

## Locus census (byte-exact)

"79 14 60" occurs exactly **2x stream-wide**:
- 0-based @1364, row a7_06: `…35 13 92 62 94 | 79 14 60 | 03 30 82 16 91 67 98 00 86 29 89 84`
- 0-based @1688, row a8_05: `…79 65 13 93 62 94 | 79 14 60 | 27 46 24 85 58 15 23 91 85 33 94 30`

The 5-gram "62 94 79 14 60" is likewise 2x (both loci). "14 60" is 2x — no other "en [60]" windows exist. 14's follower census: 60 is its only verb-stem-shaped follower pair (×2; other followers {24×2, 06×2, 21, 74, 45, 62, 02, 00, 59, 29, 98}).

## Per-clause pass/fail

### C1 — PASS

"tout en [60]" parses as a licensed gérondif at battery grade, element by element:

1. **79 = "tout"** — granted (A5). No assumption.
2. **14 = "en"** — battery PROMOTE (en14-value-tighten 15/15 census; core-14-622-bank used exactly these two "79 14 60" windows as the 'en'-frame corroboration). 14's rival arms are dead here: 'le' killed globally (le-14-kill-1121), verb class fenced lane-wide, determiner fenced to @117. 'en' is the forced reading at both windows.
3. **60 = present participle of the 60-verb** — 60 is verb-class at battery grade (split-60-verbs bare-60 verb, -dre family). The present-participle arm is live and unkilled (npframe-60-454; the kill was past-participle "dit" only). Under the lane's gérondif model ("en [stem]", -ant unspelled, en85-gerund-reaudit PROMOTE), "en [60]" is the gérondif of the bare-60 verb — the exact mold of the five confirmed "en [85]" legs.
4. **"tout en [gérondif]" is licensed 1841 French** — "tout en marchant"-shaped; the en14 battery's own theory note treats "tout en [60]" as the gerundive shape.
5. **Repetition:** both "79 14 60" windows take the identical parse with the identical "62 94" left frame — uniform, no window-specific pleading.
6. **No contradiction:** no standing or red-team verdict is contradicted or downgraded. §7 intact — a verb's gérondif is inflection of the same -dre-family item, not a new polyvalent item (consistent with split-60-verbs' "two items, not polyvalence" and npframe-60-454's treatment of present participle as a candidate reading).

The bar's promote condition is met. C2 moot.

## Scope (stated, not hidden)

- **Window/phrase-level only.** This licenses the gerundive reading of the "79 14 60" phrase at both windows. It does **not** name 60's value (still open), and it does **not** kill the R2 pronominal rival named by core-14-622-bank ("tout" neuter-pronoun subject + "en" clitic + finite 60, "tout en dépend"-shaped), which stays live — the bar was a license test, not a uniqueness test.
- **Claim consequence fires:** H-14 (head = 14="en") re-opens — 60's dependent role is now licensed as gérondif, leaving **27 as sole open**, exactly as the claim states. The 27 residual (hapax, class open) and the "62 94" frozen left frame remain the parent battery's fenced residuals; the already-queued continuations (`frame-1688-wide`, `class-27-independent`, `val-27-1691-np`) own them — no new follow-ups proposed.
- **Canonical-stream caveat stands:** rows a7_06/a8_05 offsets unvalidated (68/70).
- 14="en" global red-team ratification still pending — adopted as battery-grade premise per the parent battery, not re-litigated.

## Verdict: PROMOTE

"tout en [60]" parses as a licensed gérondif ("tout en" + present participle of the bare-60 -dre-family verb) at battery grade at both stream windows. H-14 re-opens with 27 as sole open.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-gerund-60-1688.md` (this file).
- Queue: `gerund-60-1688` queued → `verdict`/`promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/gerund-60-1688.lock` created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
