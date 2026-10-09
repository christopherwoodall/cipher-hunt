# Battery report: w4-dict-det-gap

- Target id: `w4-dict-det-gap`
- Claim: "the determiner gap at the 78-45 loci is adjudicated"
- Date: 2026-10-09
- Worker: battery worker (subagent e47e03b2-16e4-400f-b8cd-0d634df5e0f3)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed per
  `code/side-keyhunt/repair_parse.py`; n=1847 asserted, 96 types asserted).
  `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Lock: `code/crowd17/next-token/locks/w4-dict-det-gap.lock` (created at
  start, deleted on completion; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"(a) census all four 78-45 windows' left edges (re-derive or cite); (b) name
a period-attested zero-determiner construction fitting W4's 'et verdict
[13-55-61]', or certify none exists (-> determiner gap is kill-grade for the
two-token 'verdict' reading, conditional on 78='ver' LEAD); (c) do not
declare polyvalence (§7)"

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1) All four 78-45 windows' left edges are censused (re-derived or
   cited).
2. (C2) Either a period-attested zero-determiner construction is named that
   fits W4's "et verdict [13-55-61]" on the byte evidence, or none is
   certified to exist; in the latter case the determiner gap is kill-grade
   for the two-token 'verdict' reading (78='ver'+45='dict'), conditional on
   78='ver' LEAD.
3. (C3) No polyvalence is declared (§7: 67 et/veut remains the sole true
   polyvalence).

## Method

1. Re-derived the repaired stream in-session (1,847 pairs, 96 groups).
   Never used canonical.py. R5005 not touched.
2. Enumerated all '78 45' bigrams byte-exact: exactly 4 stream-wide
   (@313, @573, @982, @1164 — 0-based). All four are row-internal (no row
   boundary straddle).
3. Checked standing values: 45='ce' is an A11 HOLD (allophone tier); 78='ver'
   is a red-team LEAD (R16-005, confirmed R17-006/R17-021); 45='dict' is a
   lead (battery evidence only, "verdict" its sole host); 67='et' forced by
   the §7 positional rule (67="veut" iff follower infinitive-shaped; 78 is
   noun-shaped at W4 per R17-014 / fork-78-45-rerun).
4. Tested every period-attested zero-determiner construction against W4's
   window on the byte evidence: proper name, fixed locution, vocative,
   exclamation, apposition, adverbialized noun, shared-article coordination
   ellipsis, bare enumeration, telegraphic register, predicate.
5. Coordinated with (did not re-run) the fenced
   dict-frame-78-45-13-55-61 battery and fork-78-45-rerun.

Offset note: @n below = 0-based pair index in the repaired stream.

## Window-level evidence

### C1: census of the four 78-45 left edges (re-derived)

- **W1 @313 (row a2_04, row-offset 16):**
  `@307:20 @308:17 @309:46 @310:84 @311:24 @312:37 | 78 45 | @315:64 @316:59
  @317:32 @318:94 @319:06 @320:11`
  Left edge: `24 37`. Right edge: 64='qui' (granted), 59='est'
  (provisional), 32.
  Two-token read: "…[24] [37] verdict qui est [32]…" — "verdict" heads a
  "qui" relative clause with no determiner anywhere left (37's class is
  open; predicative frames granted at A1, no determiner evidence).
  **Determiner gap present** (parallel to W4; see below).
- **W2 @573 (row a3_02, row-offset 15):**
  `@571:52 @572:87 | 78 45 | @575:13 @576:55 @577:61 @578:94 @579:82 @580:06`
  Left edge: `52 87('ce')`. Right edge: 13 55 61, then "ne mentent".
  Two-token read: "ce(87) verdict [13-55-61] ne mentent…" — determiner
  "ce" present. **No gap.**
- **W3 @982 (row a6_01, row-offset 10):**
  `@980:76 @981:47 | 78 45 | @983:01 @984:24 @985:89 @986:48 @987:01 @988:76`
  Left edge: `76 47('ce')`. Right edge: 01 24.
  Two-token read: "ce(47) verdict [01]…" — determiner "ce" present.
  **No gap.**
- **W4 @1164 (row a6_09, row-offset 11):**
  `@1158:77 @1159:82 @1160:44 @1161:83 @1162:21 @1163:67 | 78 45 |
  @1166:13 @1167:55 @1168:61 @1169:94 @1170:87 @1171:83 @1172:21`
  Left edge: `21 67('et')`. Right edge: 13 55 61, then the stream-unique
  "94 87" ("ne ce") hapax.
  Two-token read: "…[83] [21] et verdict [13-55-61] ne ce [83]…" —
  "verdict" is a bare singular count noun after the conjunction "et".
  **Determiner gap present.** 67='et' is forced by the §7 positional rule
  (follower 78 is noun-shaped, so 67≠'veut').

This census matches fork-78-45-rerun's W1–W4 byte-exactly (independent
corroboration of the enumeration).

### C2: zero-determiner constructions tested at W4

Under 78='ver' (LEAD) + 45='dict' (lead), "67 78 45" = "et verdict". In
1841 French a singular count noun after "et" requires a determiner.
Candidate rescues, tested on the byte evidence:

1. **Proper name** — "verdict" is a common noun, not a name. Dead.
2. **Fixed locution** ("nuit et jour"-shaped) — "verdict" belongs to no
   attested fixed phrase with "et". Dead.
3. **Vocative / exclamation** — "et" cannot introduce either. Dead.
4. **Apposition** — apposition takes no "et". Dead.
5. **Adverbialized noun** — "verdict" is not adverbializable. Dead.
6. **Shared-article coordination ellipsis** ("les officiers et soldats") —
   requires the article on the FIRST conjunct; the preceding conjunct is
   "21" with no determiner either ("…44 83 21 et verdict…"). Dead on the
   byte evidence.
7. **Bare enumeration** ("officiers, soldats et marins") — period-attested,
   and the ONLY candidate that is grammatical in principle. But it does not
   FIT on the byte evidence: the list head would have to be established in
   the left run "…44 83 21", where 83's value is fully open and 21's is
   open (noun-class only). No byte evidence shows a bare list is in
   progress. Adopting it spends unstated assumptions the bar does not
   allow. Recorded as the sole conceivable rescue (follow-up 1), not a
   fit.
8. **Telegraphic / headline register** — not attested in 1841 diplomatic
   prose mid-sentence. Dead.
9. **Predicate** ("est verdict") — left token is 67='et', not 59='est'.
   Dead.

**Certified: no period-attested zero-determiner construction fits W4's
"et verdict [13-55-61]" on the byte evidence.** Per the bar's arrow, the
determiner gap is therefore kill-grade for the two-token 'verdict'
reading at W4.

**W1 parallel:** the same gap applies at W1 @313 ("[37] verdict qui est
[32]"): under 78='ver'+45='dict', "verdict" heads the "qui" relative
clause with no determiner (37's class open, no determiner evidence; and
as a bare direct object of a 37-verb it would be equally
ungrammatical — French does not license bare singular count nouns in
either slot). The two-token reading fails at W1 under the same logic.
W2 and W3 are unaffected ("ce verdict" has its determiner).

### C3: polyvalence

None declared. §7 intact: 67 et/veut remains the sole true polyvalence.

## Per-clause pass/fail

1. C1 (census): **PASS** — all four left edges re-derived byte-exact.
2. C2 (construction or certification): **PASS via the certification
   disjunct** — no fitting construction exists on the byte evidence;
   the gap is real and kill-grade for the two-token 'verdict' reading at
   W4 @1164 (parallel gap at W1 @313). Conditional on 78='ver' LEAD and
   the 45='dict' lead (both unratified).
3. C3 (no polyvalence): **PASS** — none declared.

## Verdict: KILL

The two-token 'verdict' reading (78='ver' + 45='dict' as one word) is
kill-grade dead at **W4 @1164** ("et verdict [13-55-61]" — bare singular
count noun after "et", no period-attested zero-determiner construction
fits on the byte evidence). The same gap applies at W1 @313
("[37] verdict qui est [32]"). W2 @573 and W3 @982 are unaffected ("ce
verdict" carries its determiner). Kill is conditional on the standing
leads 78='ver' (R16-005/R17-006) and 45='dict' (battery lead); if either
lead falls, the reading dies for other reasons or the question is moot.

## Adverses answered

- "5-gram unit escape owned by dict-frame-78-45-13-55-61 (fenced, not
  re-run)": answered — that battery was cited, not re-run; its null
  verdict stands untouched (no downgrade, no overwrite). This kill
  targets the two-token word reading only. Note for the red team: if the
  78-45 'verdict' word is dead at W4, the fenced 5-gram unit's remaining
  life at W4 is confined to its left-context fence (already recorded),
  since no French word can begin "verdict…" with a different 78-45
  account — but the 5-gram's null is not reopened here.

## Standing state

- No standing or red-team verdict contradicted or downgraded.
- No battery verdict re-run: fork-78-45-rerun's census was adopted as
  corroboration, not duplicated; dict-frame-78-45-13-55-61's null
  stands.
- Caveats (stated, not hidden): canonicality caveat stands (a6_09's
  upstream offset is unvalidated — 68 of 70 rows unvalidated); 67='et'
  is forced by the §7 positional rule; the W4 right edge carries the
  "94 87" hapax anomaly (flagged for red-team awareness by the
  dict-frame battery).

## Follow-up targets (for supervisor queuing)

1. **w4-list-head-hunt** (priority 4): test the sole conceivable rescue
   at W4 — a bare-enumeration list head. Bar: name the byte-evidenced
   bare list head left of @1162 (@1153–1161: "77 82 44 83 21") under
   standing values with 21/83 as bare list items; kill the rescue iff
   no head parses (then the W4 kill is unconditional on construction
   search).
2. **verdict-1841-attestation** (priority 4): corpus check — is "verdict"
   attested as a common noun in 1841 diplomatic French (per the
   venir-a-1841-corpus precedent)? Bar: attested iff ≥2 period sources;
   if unattested, the two-token reading's premise weakens globally.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-w4-dict-det-gap.md`
- Queue: `battery-queue.json` → `w4-dict-det-gap` status `verdict`,
  result `kill`, date 2026-10-09 (pre-write assert passed — was `queued`,
  no prior verdict; temp-file + rename; JSON re-validated post-write;
  only this entry touched).
- Lock created at start, deleted on completion.
- `canonical.py` never used. R5005, sealed gates, red-team adjudication
  queue untouched.
