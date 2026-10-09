# Battery report: trans-60-995

- Target id: `trans-60-995`
- Claim: "Force transitivity at @995 by resolving 03's role ('pas [03] [60]'): a forced-transitive 60 kills repondre and the intransitive uses of tendre/descendre; a forced-intransitive 60 kills the six transitives."
- Adverses: "never invent data; R5005 untouched; canonical-stream caveat"
- Date: 2026-10-09
- Worker: battery worker (subagent 49260e84-b558-4c42-883a-325e644ab6cd)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- @i = 0-based pair index (same convention as the parent `dre-60-rerun`). "03's role at @995" = the 03 at 0-based @994, immediately before 60 at 0-based @995.

## Bar (verbatim, pre-registered from battery-queue.json BEFORE testing)

"name 03's role at @995 with stated values; then name 60 transitive iff the frame forces an object, intransitive iff the frame forbids one; kill-grade contradiction decides"

Numbered clauses (fixed before data examination):

1. **C1:** 03's role at 0-based @994 (the "pas [03] [60]" window) is named with stated values at battery grade.
2. **C2a:** 60 is named TRANSITIVE iff the @995 frame forces an object.
3. **C2b:** 60 is named INTRANSITIVE iff the @995 frame forbids an object.
4. **C3:** a kill-grade contradiction decides where C2a/C2b are silent.

## Method

1. Read BATTERY-PROTOCOL.md in full before touching anything. Created `code/crowd17/next-token/locks/trans-60-995.lock` on start (agent id + 2026-10-09T20:12:30Z; no prior/stale lock); deleted on completion.
2. Re-derived the repaired stream in-session; byte-confirmed the window and n(03)=20 with full ±4 contexts.
3. Adopted standing record (not re-litigated): R19-178 (stem-03 verb-stem grant CONDITIONED to "03 29" frames only), `battery-val-03-value-census` window #7 (@994: "pas [03]" kills bare-stem-03), `battery-split-03-redteam-feed` P2 (uniform-verb-03 fence, 12/20 windows), R20 finite-03 rejection (ne-W6-pas-verb), `dre-60-rerun` (nine -dre candidates parse @995 identically; object-absence below kill grade).
4. 1841 diplomatic French throughout; corpus check for the "pas [Adv]" pre-verbal slot in `code/side-period/corpus/`.

## Window-level evidence

Byte-confirmed window (0-based):

- @991=24, @992=26, @993=30, @994=03, @995=60, @996=67, @997=11, @998=96, @999=82, @1000=33, @1001=00, @1002=86
- Standing values: 30=pas; 60=verb-class (-dre stem, 3sg bare); 67=et (positional rule: follower 11=la banked, non-infinitive-shaped); 11=la (pencil); 96=par (granted); 00=pour (A9); 29=er (banked).
- Frame: `[24] [26] pas [03] [60] et la par m [33-INF] pour [86-INF] …`
- Sibling "30 03" windows (n=3 stream-wide): @31 "30 03 64(qui) 32", @657 "24 26 30 03 62 16 00 86" (identical left context "24 26 30 03" to @994), @994 "24 26 30 03 60 67".

### C1 — 03's role at @994: arm-by-arm

1. **Verb-stem: KILL-grade DEAD (adopted).** `val-03-value-census` window #7 = exactly @994: "pas [03]" — the "ne…pas" frame governs an infinitive word, not a bare stem. `split-03-redteam-feed` P2 carries it. R19-178's verb-stem grant is conditioned to "03 29" frames; the follower here is 60, so the conditioned grant does not apply.
2. **Finite verb: DEAD.** "*pas [V-fin] [V-fin]" is ungrammatical; finite-03 independently rejected at R20 (ne-W6-pas-verb).
3. **Infinitive: DEAD.** "pas [INF] [V-fin]" is ungrammatical; 03 is not in a "03 29" frame here.
4. **Noun: FENCED with stated cause (locus-level).** Default parse "pas [N] [V-fin]" is ungrammatical (bare noun between negation and finite verb). The only rescue invents a clause boundary after 26 + "pas" as a standalone answer-particle "non" (register-dubious in 1841 diplomatic French) + 03 as a determinerless proper-noun subject — three ungranted assumptions. Fenced, not viable at battery grade.
5. **Adjective / pronoun-"ce" / clitic (y/en/le): DEAD.** "*pas [Adj] [V]", "*pas ce [V]", "*pas [clitic] [V]" (clitic word-order violation).
6. **Adverb: SURVIVES — the only grammatical arm.** "pas encore / seulement / déjà / toujours / même [V-fin]" is clean French; "pas encore" is period-attested in the 1841 corpus (Chateaubriand, outre-tombe: "pas encore fini", "pas encore vécu", "pas encore paru"). Sibling @657 ("pas [03] [62] … pour [INF]") is adverb-consistent.
- Locus scope: @31 ("pas [03] qui [32]") would kill a GLOBAL adverb-03, but 03 uniformity is red-team §7 venue (R20 deferred "03 conditioned split vs second polyvalence"); the bar asks for @995 only, and no global claim is made.
- Residuals: the exact adverb lexeme is unnameable (encore/seulement/déjà/toujours all fit "pas _ [V-fin]"); 60's subject is unidentified under every arm (shared clause-level residual, not a discriminator).

**C1: PASS** — 03's role at @994 = ADVERB (value open), with stated values (30=pas standing; 60=verb-class; "pas [Adv]" slot corpus-attested).

### C2 — transitivity of 60 at @995

- **Forcing (C2a):** no object is forced. No preverbal object clitic ("pas [adv]" intervenes between any nominal and 60); no postverbal NP ("[60] et" — 67=et conjoins forward; "la" after "et" cannot be 60's object). 26 stands left of "pas" in the prior clause and cannot serve as a postposed object.
- **Forbidding (C2b):** nothing forbids an object. No reflexive, no intransitive-only construction, no complement-blocking frame.
- Object-obligatory candidates (vendre/rendre/prétendre) are at most mildly disfavored by the objectless frame — absolute uses exist (attendre/entendre/défendre freely; vendre/rendre/prétendre marginally), and `dre-60-rerun` already placed object-absence below kill grade. Adopted, not re-litigated.

**C2a: FAIL. C2b: FAIL** — the frame neither forces nor forbids an object; transitivity is unnameable from this frame.

### C3 — kill-grade contradiction

No kill-grade contradiction bears on 60's transitivity at @995. The nine -dre candidates remain exactly as `dre-60-rerun` left them: répondre (intransitive), tendre/descendre (ambitransitive), and the six transitives all parse the frame. Nothing fires.

## Per-clause pass/fail

- **C1 (name 03's role): PASS** — adverb, locus-level, value open.
- **C2a (transitive iff forced): FAIL** — no object forced.
- **C2b (intransitive iff forbidden): FAIL** — no object forbidden.
- **C3 (kill-grade decides): MOOT** — no kill-grade contradiction available.

## Verdict

**NULL** — 03's role at @994 is narrowed to adverb (the only surviving arm: verb-stem kill-grade dead by adoption, all other arms ungrammatical or fenced), but the @995 frame is transitivity-neutral for 60: it neither forces an object (killing répondre / the intransitive uses of tendre-descendre) nor forbids one (killing the six transitives). The bar's decision procedure cannot fire.

## Follow-ups proposed (both verified ABSENT from battery-queue.json; the two already-queued convergences noted, not duplicated)

1. `abs-60-transitives-corpus` (P4) — corpus census of absolute (objectless) finite uses of vendre/rendre/attendre/entendre/défendre/prétendre across the 1841 corpus; a zero at scale would make @995's objectless frame kill-grade against the object-obligatory lexemes and narrow the nine.
2. `subj-60-995` (P4) — name 60's subject at @995 (26-shared? postverbal?); resolving the clause may re-open transitivity through the subject's selectional restrictions.
- Convergence (already queued, not proposed): `val-03-994-role` (queued) directly overlaps C1; `val-53-1473-subj` (queued) is the parent's companion follow-up.

## Scope

Locus limited to @991–@996. Untouched: 03's global value and the §7 conditioned-split-vs-polyvalence question (red-team venue, R20 deferred); 60's lexeme (nine candidates stand); R19-178/179/180; R20 deferrals; the '60 08' vient windows (red-team venue); gerund-60-1688's gérondif license; `dre-60-rerun`'s four-locus findings. No standing or red-team verdict contradicted, downgraded, or re-litigated. Canonical-stream caveat stands (row a6_01/a6_02 offsets unvalidated).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-trans-60-995.md` (this file).
- Queue: `trans-60-995` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique temp file `battery-queue.json.trans-60-995.tmp` + atomic rename; disk re-validated; own entry only; no downgrade; no tmp leftover).
- Lock `code/crowd17/next-token/locks/trans-60-995.lock`: created on start (2026-10-09T20:12:30Z, no stale lock), deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
