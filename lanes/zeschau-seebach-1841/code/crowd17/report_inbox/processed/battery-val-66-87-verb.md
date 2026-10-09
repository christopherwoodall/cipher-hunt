# Battery verdict: val-66-87-verb

- Target id: `val-66-87-verb` (battery-queue.json, priority 3, status queued)
- Claim: name 66's class at @87
- Date: 2026-10-09
- Worker: subagent session 6078c13f (parent: next-token battery dispatch)

## Bar (verbatim, pre-registered)

"verb-66 (infinitive-shaped) revives the @86 pronoun leg as '[88-fin] le [66-inf]' ('il veut le voir'-shaped); non-verb kills it"

## Numbered clauses (fixed before testing, not modified after)

- **C1 (verb arm):** verb-66 (infinitive-shaped) at @88 revives the @86 pronoun leg as "[88-fin] le [66-inf]" ("il veut le voir"-shaped).
- **C2 (non-verb arm):** non-verb 66 at @88 kills the @86 pronoun leg ("[88-fin] le [66-inf]" has no verb host).

Adverses listed: none.

## Method

Read BATTERY-PROTOCOL.md in full before touching anything. Re-derived the
repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
(parsed exactly like `code/side-keyhunt/repair_parse.py`; asserts held:
1,847 pairs, 96 types). `code/side-keyhunt/canonical.py` never used. R5005,
sealed gate instances, and the red-team adjudication queue untouched. All
@-offsets are 0-based repaired-stream pair indices.

Adopted (not re-litigated): subclass-66-98-noun PROMOTE (2026-10-09) — 66 is
a plain noun in the X-66-98 subject windows (@88, @123, @766); the
substantivized-infinitive rival is killed at grammaticality grade (0 genuine
infinitive subjects of "vient" in 57.4M chars of 1841 French, exhaustive
-infinitive shape coverage, semantic ground: "venir" selects subjects
capable of coming). finiteness-88-86 PROMOTE (88 verb/governor at @86).
objpron-88-77-11 NULL (2026-10-09) — its C1 fenced the @86 pronoun leg on the
ground that the reading needs 66=verb, an invented value at the time.

## Window-level evidence (byte-exact, re-derived in-session)

- @84=14, @85=06, @86=88, @87=77, @88=66, @89=98, @90=19, @91=41, @92=98
  (row a1_02): "...ent [gov-88] le(77,prov) **[66] vient** [19] [41] vient".
- n(66)=19: [88, 123, 140, 153, 189, 246, 254, 457, 705, 715, 766, 1018,
  1109, 1150, 1346, 1459, 1494, 1533, 1622] — exact match to
  poly-66-split's census.

### C1 — the verb-66 arm is forced false at kill grade

The pronoun-leg reading ("[88-fin] le [66-inf]") requires 66 to be the
proclitic's verb host — an infinitive. This is contradicted at battery grade
by two independent standing results at this exact window:

1. **Class:** subclass-66-98-noun PROMOTE names 66 a plain noun at @88
   ("le [66] vient", 98='vient' LEAD as finite host). A noun cannot host a
   proclitic object ("il veut le maison"-ungrammatical).
2. **Grammaticality:** the infinitive-shaped rival is killed at
   grammaticality grade — 0 genuine infinitive subjects of "vient" in
   57.4M chars of 1841 French (exhaustive shape search). 66 sits directly
   before 98="vient" as its subject in this window; an infinitive-shaped 66
   is ungrammatical here independent of the clitic question.

The only rescue (66=verb at @88 vs 66=noun at @88) is a conditioned split —
a second polyvalence, a red-team act per §7 (67 et/veut sole true
polyvalence; redteam-66-polyvalence P1 queued). This battery cannot declare
it. → C1 FAILS at kill grade.

### C2 — the non-verb arm fires

With 66=noun at @88, the "[88-fin] le [66-inf]" construction has no verb
host for the proclitic "le" (77 provisional): 66 cannot be the host, and no
other cell in @86–@89 is a candidate verb host (88 is the candidate head,
98 is the finite host of the noun subject). The @86 pronoun leg is therefore
killed. This hardens objpron-88-77-11's C1 fence (which stopped at "needs
66=verb, an invented value") to kill grade: the value is no longer merely
unvalued — it is forced false at this window by a standing promote and a
corpus-grade grammaticality kill. No adverse pending: the imperative+enclitic
rival was already priced out of budget there (≥2 ungranted assumptions), and
the article+NP reading ("le [66-noun]") is the live rival, not this
target's scope. → C2 HOLDS.

## Verdict: KILL

C1 fails at kill grade (verb-66 forced false at @88 by standing promote +
grammaticality-grade corpus kill); C2 fires (non-verb 66 kills the @86
pronoun leg, hardening objpron-88-77-11's fence to a kill).

## Scope

Kills only the verb-66 arm of the @86 pronoun leg — the "[88-fin] le
[66-inf]" ("il veut le voir"-shaped) reading at @86–@88. Untouched:
88's finiteness at @86, 77='le' provisional, 98='vient' LEAD, the live
article+NP reading ("le [66-noun] vient"), poly-66-split's pour-governed
non-finite arms and the queued redteam-66-polyvalence §7 venue, noun-66-98's
value-naming fence, §7. No standing or red-team verdict contradicted or
downgraded; canonical-stream caveat stands (row a1_02 offsets unvalidated).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-66-87-verb.md`
- Queue: `val-66-87-verb` queued → `verdict`/`kill`, 2026-10-09 (pre-write
  assert passed — was queued/verdictless; target-id-unique tmp
  `battery-queue.json.val-66-87-verb.tmp` + atomic rename; disk
  re-validated; own entry only; no downgrade; no tmp leftover).
- Lock: created 2026-10-09T20:17:08Z (no stale lock), deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched.
