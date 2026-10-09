# Battery report: satisfait-contrefait-lex

- Target id: `satisfait-contrefait-lex`
- Claim: "discriminate the compound stem behind 37 in 37-01: 'satis' (satisfait) vs 'contre' (contrefait), given promoted battery-level reading 37-01 = one 'faire'-compound 3sg finite verb, 37=[stem], 01='fait'"
- Date: 2026-10-09
- Worker: battery worker (subagent c539c4af-7a7f-4d97-ac89-42a2c44fc949)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed per
  `code/side-keyhunt/repair_parse.py`). Re-derived in-session: 1,847
  pairs, 96 types. All @-offsets are 0-based repaired-stream indices.
  Never used `canonical.py`. R5005 not touched. Sealed gates and
  red-team adjudication queue untouched.
- Lock: `code/crowd17/next-token/locks/satisfait-contrefait-lex.lock`
  (created at start, deleted on completion; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

1. "Do NOT re-litigate the parent verdict: 37-01 is a single word-internal unit reading 01='fait' (promoted at battery level 2026-10-09); stem choice is residual."
2. "Coordinate with red-team S5 / s5-foundation on 37's stem value — do not duplicate red-team work; this is lexeme discrimination, not value re-adjudication."
3. "Ground stem choice in: period-corpus attestation of 'qui satisfait' / 'qui contrefait' government with the observed followers ([07] @941, [74] @1635, [02] @1819), or 37's stem value from S5 territory."
4. "Fail closed: if neither stem discriminates, return NULL with follow-ups, not a guess."

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1) The parent verdict (wordinternal-37-01 PROMOTE) is adopted as a
   premise, not re-tested.
2. (C2) Red-team S5 territory is consulted for 37's stem value; no
   red-team work is duplicated (no stem value decided here).
3. (C3) A discriminating attestation is found: either the period
   corpus shows differential government of 'qui satisfait' vs
   'qui contrefait' binding to the observed followers, or S5 names
   37's stem value.
4. (C4) If no discriminator exists, fail closed (NULL + follow-ups,
   no guess).

## Method

1. Re-derived the repaired parse in-session (1,847 pairs / 96 types).
2. Confirmed the three 37-01 windows byte-exact: 37 at 0-based
   @939 (row a5_10), @1633 (row a8_03), @1817 (row a8_10); followers
   07 @941, 74 @1635, 02 @1819.
3. Read the parent battery report (`battery-wordinternal-37-01.md`)
   and adopted its verdict as premise (C1).
4. Searched the red-team territory: `battery-s5-foundation-r2.md`,
   `next-token-redteam-r18.md` (R18-016 qui37-rival-values), and the
   round-7 S5 fence record.
5. Searched the lane period corpus (`code/side-period/corpus/`,
   1840–42 diplomatic/journal French) for 3sg 'satisfait' and
   'contrefait' with 'qui' and with infinitive government.
6. Checked battery-queue.json for any class/value profile of the
   followers 07 (n=8), 74 (n=34), 02 (n=17).

## Window-level evidence (adopted from the parent battery, not re-run)

- W1 @939: `...qui(64) [37-01] [07]...` = "qui satisfait/contrefait [07]" —
  relative + 3sg finite verb + direct object. Grammatical under BOTH stems.
- W2 @1633: `...qui(64) [37-01] [74]...` — identical frame; grammatical
  under BOTH stems.
- W3 @1817: `[06]er [37-01] [02]` — infinitive-subject + 3sg verb +
  direct object; grammatical under BOTH stems.
- Government identity: both 'satisfaire' and 'contrefaire' are plain
  transitive 3sg verbs. There is no syntactic difference between the
  two at any window (the parent battery's own conclusion: "same
  segmentation shape, same parses").

## Period-corpus findings (C3)

Both stems are period-attested in 3sg present with 'qui' + direct
object, in the same registers:

- 'satisfait' (3sg): "Le journal de Francfort satisfait ma curiosité"
  (Nesselrode v9 — nominal DO); "qui satisfait à son gré tous les
  caprices" (Revue des deux mondes 1841-q1 — nominal DO); "qui me
  satisfont" (Guizot mémoires, plural — pronominal DO); "ne satisfait
  aucun de nous" (RDM 1841-q1 — pronominal DO).
- 'contrefait' (3sg): "On le contrefait à Paris en ce moment" (RDM
  1841-q1 — pronominal DO, a book); "ceux qui la contrefont" (RDM
  1841-q2, plural — pronominal DO).

Differential government: NONE. Both govern a direct object
(nominal or pronominal) after 'qui'. 'Satisfaire' additionally
attests à-government ("satisfaire à la charge", "satisfaire au
vœu"), but no preposition intervenes between 37-01 and any follower
window, so that frame cannot fire here. Neither verb attests 3sg
government of a bare infinitive in the corpus — the W3
infinitive-subject frame is licensed by French grammar
(infinitive-as-subject), not by corpus attestation, and applies
equally to both stems.

Follower classes: no battery-level class or value profile exists for
07, 74, or 02. Their values are open, so no selectional-restriction
evidence (e.g. contrefaire's producible-object requirement) can be
applied at any window.

## Red-team S5 coordination (C2)

- S5 standing fence (round-7): 37='le' MEDIUM — confirmed contradicted
  at battery level (s5-foundation-r2), downgrade is red-team's call.
- R18-016 qui37-rival-values: GRANT (ranking only) — "no polyvalence
  declared; no value named for 37."
- S5 has NOT named 37's stem value for the 37-01 unit. Per bar C2, I
  do not duplicate red-team work and decide nothing about 37's stem.

## Per-clause pass/fail

1. C1 (parent verdict adopted, not re-litigated): PASS.
2. C2 (S5 coordination, no duplication): PASS.
3. C3 (discriminating attestation or S5 stem value): FAIL — both stems
   period-attested with identical government; followers open; S5 names
   no stem value.
4. C4 (fail closed): FIRES — return NULL with follow-ups.

## Verdict: NULL

Neither stem discriminates. 'satis' and 'contre' are both
period-attested 3sg finite verbs with the same transitive government
('qui V DO'), both fully grammatical at all three windows, and the
followers' open values admit no selectional test. Guessing would be
inventing evidence. No standing or red-team verdict contradicted or
downgraded; §7 intact.

## Follow-ups proposed (for supervisor queuing)

1. `lex-37-stem-07-value` (P3): once 07's value is named at W1
   (@939–941), apply selectional restriction — a producible/document
   object favors 'contre', a broad object favors 'satis'. Bar: one
   stem licensed by the named object, the other excluded at kill
   grade; else fence.
2. `lex-37-stem-02-value` (P3): same test at W3 (@1817–1819) once 02's
   value is named; coordinate with (do not duplicate) val-02 work.
3. `s5-stem-ranking-feed` (P4): package both stems' corpus attestations
   (with line references above) as battery evidence for the red-team
   S5/37 stem-value adjudication — evidence feed only, no
   adjudication at battery level.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/satisfait-contrefait-lex.lock`
  created on start, deleted on completion.
- Queue update: temp-file + rename on `battery-queue.json`, own entry
  only; pre-write assert confirmed queued/verdictless; JSON re-validated
  after write.
- No standing verdict contradicted or downgraded. R5005, sealed gates,
  and the red-team adjudication queue untouched.
