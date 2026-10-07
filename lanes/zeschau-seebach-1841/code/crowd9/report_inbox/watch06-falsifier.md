# 06-FALSIFIER-WATCH — round 9 hunt report (2026-10-07)
## Target: 06="ent" iff pre=82 (F61, conditioned LEAD, F33-form, n=4, n_eff=3)

Pre-registration: `code/crowd9/watch06/PREREG.md` (bars written before the
census; partial-blindness on the window list disclosed there). Census code +
log: `code/crowd9/watch06/census06.py`, `census06.log`. Independent
re-enumeration from the repaired 1,847-pair stream (frenchman util loader).

Index note: the frenchman package's `islet_06_ent.windows=[579,737,1183,1354]`
are 82-positions; in 06-position convention W06=[580,738,1184,1355].

## Verified baselines
- **n06=44** ✓ (matches round-6 re-derivation).
- **82→06 census = exactly [580, 738, 1184, 1355]**, n=4 — identical to the
  F33 predicted list. **FIRE-PART (partition defect): DOES NOT FIRE.**

## Falsifier attempts vs bars

### 1. FIRE-IN — pre=82 06-window contradicting "ent"
By-ear audit (F34/F44) of all four, frame ±4:
- @580: `94=ne 82=m [06] 06 50` → "…nement" + boundary + second-06 word.
  Speakable ✓ (second 06 has pre=6, out-of-domain; polyvalence live per
  F21/N18 — not a contradiction).
- @738: `18 82=m [06] 0` → lone-82 (no 94 prefix); "X-ment" tail speakable
  regardless of unknown 18; successor 0 unknown — no forced re-parse. ✓
  (weakest leg of the four: the "m'en" frame is absent here, only "ment").
- @1184: `94=ne 82=m [06] 06 59=est` → "…nement est…" ✓.
- @1355: `94=ne 82=m [06] 52` → "…nement …" ✓.
**Verdict: NO FIRE.** Zero in-domain contradictions. (No manual-tiling
bearing counts scored, per standing rule.)

### 2. FIRE-OUT — pre≠82 06-window reading cleanly as "ent"
40 out-of-domain windows scanned under the pre-registered rule
(gloss(pre)+"ent"+gloss(suc) must be an acceptable French word tail;
unknown gloss ≠ support). Near-misses, all REJECTED under the rule:
- @319 `94=ne [06] 11=la`: "ne"+"ent" = "neent" — not French. Rejected.
- @271 `11=la [06] 67`: "la-ent" would require elision the cipher doesn't
  write (11=la, not l'). Rejected.
- 06→29 ×4 (@1096, @1388, @1709, @1815): **banked by N19 (red-team UPHELD)
  as "ent|er" UNGRAMMATICAL — cited, not re-spent.** Cannot be counted as
  clean "ent" reads without overturning N19.
- All other pre≠82 windows have unknown-gloss contact on at least one side.
**Verdict: NO FIRE.** The ← leg survives the census.

### 3. Coincidence probe — is pre=82 doing real conditioning work?
- n82=39, P82=0.0211; E[82→06]=0.93 under independence; obs=4.
- Enrichment 4.31×; **exact binomial P(X≥4)=0.0138**.
- Fragility check: at obs=3, P(X≥3)≈0.049 — the selection is **significant
  at 0.05 but one window away from the fence** (n_eff=3 is thin, as flagged
  in the work order).
**Verdict: neither pre-registered bar fires cleanly** (bar was p>0.05 ⇒
adverse to the conditioner; p<0.01 ⇒ selection real). Honest read: the
association is stronger than chance but fragile — the conditioner should
carry this fragility as a standing caveat, not as a kill.

### 4. Successor-profile check (islet-4 vs other-40)
Corrected for the index bug: islet-4 suc = {6:2, 0:1, 52:1}; only 2/44
windows in the whole stream have suc=6 (@580, @1184 — both islet),
hypergeometric P(X≥2)=0.0063. **This is post-hoc** (islet was defined by
pre=82, not suc=6) — NOT scored as a leg, NOT a falsifier; handed to the
conditioner as a shape observation: the islet's core loci are 94-82-06-06
4-grams (@578, @1182), i.e. the F33 partition may be under-describing the
frame. For the conditioner, not the registrar.

## Overall verdict: ISLET SURVIVES the hunt
- Banked falsifier: attempted on all three prongs — **did not fire**.
- Coverage: full census of all 44 06-windows; all 4 pre=82 windows
  by-ear audited; all 40 pre≠82 windows screened under the pre-registered
  rule; coincidence probe run with exact test; index-convention trap
  caught and corrected (frenchman windows are 82-positions).
- Adverses found: **zero**. Fenced: zero.

## For the red team to rule on
1. **N19 interaction:** the four 06→29 "enter"-shaped windows are the only
   out-of-domain "ent"-candidates with glossable contact, and N19 already
   banked "ent|er" as ungrammatical. If the red team ever re-opens N19,
   the iff's ← leg is the casualty — flagging the dependency, not
   re-litigating it.
2. **Fragility:** P=0.0138 at n_eff=3. Recommend the islet keep its
   conditioned-LEAD grade (not promoted) until n_eff grows or an
   independent leg lands; the conditioner should note the one-window
   margin in the registry.
3. **@738** (lone 82-06, no 94 prefix, pre-of-82=18 unknown) is the
   structurally weakest islet window — the "-nement" trigram frame holds
   for only 3/4. Not an adverse; recorded for the conditioner.
4. **Post-hoc 06-06 adjacency** (@580/@1184 suc=6, P=0.0063): suggest the
   conditioner consider whether the islet frame is really the 4-gram
   94-82-06-06 — as a registry refinement question, not a finding.

## Files
- `code/crowd9/watch06/PREREG.md` (bars + index-convention addendum)
- `code/crowd9/watch06/census06.py`, `census06.log` (full 44-window census)
