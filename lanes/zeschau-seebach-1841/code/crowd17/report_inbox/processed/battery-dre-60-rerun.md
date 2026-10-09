# Battery report: dre-60-rerun

Worker: dre-60-rerun subagent (session b0265e95-291a-42e1-9909-f66a0a6defc7).
Date: 2026-10-09.
Stream: repaired 1,847-pair / 96-type parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt), re-derived byte-exact in-session (n=1847 asserted).
canonical.py never used. R5005, sealed gates, and the red-team adjudication queue untouched.
@i = 0-based pair index.
Lock: code/crowd17/next-token/locks/dre-60-rerun.lock created at start
(2026-10-09T19:19:00Z, agent id + timestamp); no prior/stale lock; deleted on completion.
No red-team verdict on 60's value exists — no contradiction, no escalation.

## Bar (verbatim, pre-registered from battery-queue.json BEFORE testing)

"name one -dre verb (répondre/vendre/tendre/rendre/attendre/entendre/défendre/descendre/prétendre) with 60=stem parsing @995 ('[03] [60] et'), @1474 ('[53] [60]ent'), and the 'tout [60]' windows, using banked/granted/promoted values only; else fence."

Numbered clauses (fixed before data examination):

1. (C1) ONE -dre verb from the listed nine is named, with 60 as its stem,
   parsing @995, @1474, and the 'tout [60]' windows, using only
   banked/granted/promoted values.
2. (C2) If C1 fails, the lexeme-naming question is fenced with stated cause.

## Adopted standing record (not re-litigated)

- 60 is verb-class at battery grade; bare-60 verb vs ent-60 verb are two items
  sharing syllable 60 (split-60-verbs PROMOTE). No value named either side.
- verb-60-bare (NULL, 2026-10-08): V1/V3/V4 cohere under the -dre family
  (3sg = stem, 3pl = stem+"ent", zero allomorphy) but V2 @700 ("ne [60]n [98]")
  is ungrammatical under every French verb — naming defeated, class not.
- The '60 08' windows (@197, @1338) are excluded per the vient hypothesis
  (redteam-60-vient-split-input, gather-only).
- "79 14 60" occurs exactly 2x stream-wide (@1366, @1690, 0-based for 60);
  gerund-60-1688 PROMOTEd "tout en [60]" as licensed gérondif at both
  ("en [stem]", -ant unspelled per en85-gerund-reaudit; 14='en' battery-grade).
- 67 positional rule (sole polyvalence): 67='et' iff follower not
  infinitive-shaped; 67='veut' iff follower infinitive-shaped.
- dit-60-syncretic KILL, adj-60 KILL, noun-60 KILL, nir-value-60-68 KILL adopted.

## Method

Fresh parse per protocol. The bar's four loci re-derived byte-exact:

- @995: pairs 986–1005 = `89 48 01 76 49 24 26 30 03 60 67 11 96 82 33 00 86 56 47 91`
  → `...[24-verb] [26-noun] pas[30] [03] [60] et[67] la[11] par[96] m[82] [33-INF] pour[00] [86-INF]...`
  (67='et': follower 11='la' banked, non-infinitive-shaped.)
- @1474: pairs 1465–1485 = `48 21 02 62 38 26 12 41 53 60 06 67 33 29 82 16 98 62 46 77 84`
  → `...[38-verb] [26-noun] n[12] [41] [53] [60]ent[06] veut[67] [33]er[29] m[82] [16] [98-verb]...`
  (67='veut': follower 33 INF-class; "veut [X]er". The "[60]ent veut [inf]"
  adjacency stays fenced as a clause boundary per verb-60-bare — it fences
  the clause, not 60's verb-hood.)
- @1366: pairs 1357–1375 = `37 64 35 13 92 62 94 79 14 60 03 30 82 16 91 67 98 00 86`
  → `...qui[64] [35-noun] [13] [92-verb] [62] ne[94] tout[79] en[14] [60-gérondif] [03] pas[30] m[82]...`
- @1690: pairs 1681–1697 = `46 79 65 13 93 62 94 79 14 60 27 46 24 85 58 15 23`
  → `...que[46] tout[79] [65-noun] [13] [93-verb] [62] ne[94] tout[79] en[14] [60-gérondif] [27] que[46] [24-verb]...`

Each of the nine listed -dre verbs was tested at all four loci for (a) clean
structural parse as 60=stem, and (b) any kill-grade incompatibility.

## Window-level evidence

### All nine candidates parse all four loci identically

| verb | 60=stem | @995 "[03] [60] et" (3sg) | @1474 "[53] [60]ent" (3pl) | @1366/@1690 "tout en [60]" (gérondif) |
|---|---|---|---|---|
| répondre | répond | "répond et" ✓ | "répondent" = répond+ent ✓ | "en répondant" ✓ |
| vendre | vend | "vend et" ✓ | "vendent" ✓ | "en vendant" ✓ |
| tendre | tend | "tend et" ✓ | "tendent" ✓ | "en tendant" ✓ |
| rendre | rend | "rend et" ✓ | "rendent" ✓ | "en rendant" ✓ |
| attendre | attend | "attend et" ✓ | "attendent" ✓ | "en attendant" ✓ |
| entendre | entend | "entend et" ✓ | "entendent" ✓ | "en entendant" ✓ |
| défendre | défend | "défend et" ✓ | "défendent" ✓ | "en défendant" ✓ |
| descendre | descend | "descend et" ✓ | "descendent" ✓ | "en descendant" ✓ |
| prétendre | prétend | "prétend et" ✓ | "prétendent" ✓ | "en prétendant" ✓ |

-dre verbs have 3sg = stem and 3pl = stem+"ent" with zero allomorphy, and the
lane's gérondif model is "en [stem]" with unspelled -ant — so one group 60
covers finite and participial uses uniformly. 08/53/03/27 stay open and fenced
as unvalued neighbors; no assumption about any of them is needed for the
structural parse.

### No kill-grade incompatibility for any candidate at any bar locus

- Transitivity: at @995 no object is adjacent ("[60] et la"), which mildly
  disfavors the strongly transitive candidates (vendre/rendre/attendre/
  entendre/défendre/prétendre) — but object drop/ellipsis and the open 03
  left neighbor keep this below kill grade. répondre (intransitive) and
  tendre/descendre (ambitransitive) are clean.
- At @1474 the 3pl "Xent" is followed by fenced clause boundary ("veut [inf]");
  no candidate's complement structure is forced or violated.
- At @1366/@1690 the gérondif takes no complement in either window; all nine
  present participles are valid.
- Morphology: all nine have exact 3sg=stem / 3pl=stem+"ent" with no allomorphy
  (prendre/mettre-type nn-allomorphy excluded from the bar's list).

### No named neighbor selects a unique lexeme

The discriminating neighbors at every bar locus are open cells (03, 53, 27)
or class-level frames — none names a complement, subject, or selectional
restriction that picks one -dre verb over the other eight. Semantic selection
cannot fire on the bar's window set.

## Per-clause pass/fail

- **C1 (name one -dre verb): FAIL.** Nine candidates parse all four loci
  identically at the structural level; no window discriminates among them;
  no candidate suffers kill-grade incompatibility; no named neighbor selects
  a unique lexeme. Naming any one would be arbitrary.
- **C2 (fence arm): FIRES.**

## Verdict

**NULL (fence executed)** — the lexeme-naming question is fenced: 60's
-dre-family membership holds at battery grade across @995, @1474, @1366, @1690
(60=stem uniformly: 3sg bare, 3pl stem+"ent", gérondif stem with unspelled
-ant), but the specific lexeme is underdetermined at battery grade — nine
live candidates, zero discriminators. Per the verb-60-bare precedent, the
verbal class is not defeated, only the naming. No standing or red-team
verdict contradicted or downgraded; §7 intact. Canonical-stream caveat stands.

## Follow-ups proposed (all verified ABSENT from battery-queue.json, left for supervisor)

1. `trans-60-995` (P3) — force transitivity at @995 by resolving 03's role
   ("pas [03] [60]"): a forced-transitive 60 kills répondre and the
   intransitive uses of tendre/descendre; a forced-intransitive 60 kills the
   six transitives.
2. `val-53-1473-subj` (P4) — name 53 at @1473 (subject of "Xent"); a named
   subject's selectional restrictions may select the lexeme.
3. `val-03-994-role` (P4) — name 03's role at @994; resolving the "[03] [60]"
   contact (auxiliary? adverb? second verb?) constrains the frame.

## Scope

Window-set limited to the bar's four loci. Untouched: the vient hypothesis at
the '60 08' windows (red-team venue), split-60-verbs' two-item model,
gerund-60-1688's gérondif license, 60's adjective NP-frames (poly-60-redteam
queued), V2 @700's impossibility proof, dit-60-syncretic's kill. The -er
family rival (weaker on V1/V3 exactness per verb-60-bare) is not re-litigated.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-dre-60-rerun.md` (this file).
- Queue: `dre-60-rerun` queued → `verdict`/`null`, 2026-10-09 (pre-write assert
  passed — was queued/verdictless; target-id-unique temp file
  `battery-queue.json.dre-60-rerun.tmp` + atomic rename; disk re-validated;
  own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/dre-60-rerun.lock`: created on start
  (2026-10-09T19:19:00Z, no stale lock), deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
