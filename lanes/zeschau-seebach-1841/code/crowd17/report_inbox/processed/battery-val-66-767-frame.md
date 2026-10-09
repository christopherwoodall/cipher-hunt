# Battery `val-66-767-frame` — verdict: NULL (chain breaks at the boundary re-test)

## Bar (verbatim, pre-registered)

> Bar: name 66's class at @767 ("88 66 98", 66→98 'vient'-class follower). Bar: 66's role named with zero rivals → the 'est à' frame closes → re-test whether the boundary hardens.

Numbered clauses (restated before testing, not modified after):

- **C1.** 66's role at @767 (frame "88 66 98") is named. Claim arm: 66 = nominal subject of 98='vient'.
- **C2.** The naming has zero rivals at @767: every non-subject role for 66 is killed at kill grade.
- **C3.** Given the naming, the 'est à' right-context frame "62 94 59 39 88" closes as a complete clause with zero new ungranted assumptions.
- **C4.** Given the closed frame, the @760 clause boundary hardens (after-20 forced).

Adverses: none stated.

## Method

Read BATTERY-PROTOCOL.md first. Created `locks/val-66-767-frame.lock` on start (agent id + UTC timestamp). Re-derived the repaired stream in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` with the `repair_parse.py` tokenization: **1,847 pairs / 96 types**, asserts held. `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched.

@-offsets below are **0-based** pair indices. @767 0-based = 98; the claim's frame "88 66 98" = @765–767 (1-based @767 = 66 — same window either way).

Adopted premises (not re-litigated): 98='vient' finite semi-auxiliary (battery-promoted, vient-98-name); 88 infinitive-shaped (PROMOTE locus-level, battery-88-1727-shape); 59='est' provisional (§7); 62='il' and 94='ne' battery-level leads (R17); 39='/a/' → 'à' battery-level lead (R17-005); 80 verb-frame (A8). Inherited distributional fact: 66 n=19, census exact-matches poly-66-split; X-66-98 x3 is a real cluster (exact p=1.03e-03, Bonferroni-passing).

## Window evidence (byte-exact)

The X-66-98 x3 windows, re-derived (±4):

```
@88:  14 06 88 [77 66 98 19] 41 98      = "le [66] vient [19]"   (77='le' provisional)
@123: 60 90 19 [58 66 98 82] 48 11      = "[58] [66] vient m'[48]"
@766: 94 59 39 [88 66 98 80] 10 22      = "[88-inf] [66] vient [80]"
```

66 census re-derived: predecessors {00 x7, 86 x2, 13 x2, 77/58/46/12/88/15/33/78 x1}; successors {98 x3, 73 x3, 14 x2, 84 x2, 91 x2, 01/21/86/24/79/15/67 x1}. 98='vient' is the only successor shared by a tight triple, and in all three windows 66 is the sole token in subject position before finite 98.

## Per-clause results

**C1: PASS.** 66's role at @767 is named: **nominal subject of 98='vient'**. The logic: 98='vient' is finite (adopted promote); French is not pro-drop, so finite 'vient' needs an overt subject; in "88-66-98-80" the only subject-position token is 66 (88 is infinitive-shaped per its locus PROMOTE and cannot be a subject; 80 is post-verbal). The same subject position holds in the other two X-66-98 windows (@88 "le [66] vient", @123 "[58] [66] vient"). The role is named at role grain: subject of the 'vient' clause.

**C2: PASS at role grain (one sub-class rival fenced, immaterial to closure).** Rivals at @767:

1. 66 = finite-verb-shaped (the "que [66] on" group-b demand) — **KILLED**: finite 66 adjacent to finite 'vient' is ungrammatical; no compound-tense reading is available.
2. 66 = adverb — **KILLED**: leaves finite 'vient' without a subject; no other subject candidate exists in the window.
3. 66 = determiner / relative pronoun — **KILLED**: no noun head is available.
4. 66 = complement/object of the 'est à' frame ("est à [88-inf] [66]") — **KILLED**: one token cannot be both 88's object and 'vient's subject; 'vient' needs its subject and 66 is the only candidate, so 66 is the subject, not the complement.
5. 66 = disjunctive pronoun as subject — **FENCED (strained)**: not standard subject position in 1841 French; no resumptive pronoun present.
6. 66 = bare/substantivized infinitive as subject ("[88]. [66-inf] vient [80]") — **FENCED**: grammatical in principle, but no infinitive subject of 'vient' is attested in any of 98's 40 windows (attested subjects: 'ce' x2, 'qui' x2, nouns), and at @88 the provisional 77='le' article favors a plain noun. This sub-rival does not affect frame closure: noun and infinitive-as-subject both place 66 outside the 'est à' frame.

Zero rivals to the *role* (subject of 'vient', frame-external). The role is named.

**C3: PASS.** The 'est à' frame closes. "62 94 59 39 88" reads "[il] [ne] [est] [à] [88-inf]" — the passive-infinitive "est à + infinitif" construction, syntactically complete with 88 as its infinitive complement (88's locus PROMOTE). C2's kill of rival 4 removes 66 as a candidate complement: 66 heads the next clause ("[66] vient [80]"), so the frame needs nothing more. Zero new ungranted assumptions (all premises adopted from the parent battery and standing verdicts). Carried fence (not a closure block): the parent's negated-shape corpus strain ("n'est à + inf" unattested in 32.5M side-period chars) still stands as idiomaticity strain.

**C4: FAIL (partial hardening only — boundary not forced).** Re-test of the @760 boundary with the closed frame: the parent's fence had three causes — (a) 66's undetermined role: **REMOVED** by this battery; (b) negated-shape corpus strain: **STANDS**; (c) the boundary could precede 20 via 20's fenced clause-initial roles: **STANDS** (owned by `boundary-760-20role`, in flight — its lockfile is present in `locks/`). The after-20 reading is strictly stronger than before (complete right clause, one fewer block), but the boundary is not forced: 20's clause-initial roles remain fenced-live, and the fence cause is not fully removed. The boundary hardens relatively; it does not harden to forced.

## Verdict: NULL

Clauses C1–C3 pass; C4 fails at non-kill grade. No window forces the chain false (no kill). The role naming and the frame closure are demonstrated; the boundary re-test is genuinely undecided pending `boundary-760-20role` and the negation-strain line. No standing red-team or battery verdict is contradicted or downgraded: the naming is window-level role grain (not a global value, not a polyvalence declaration — §7 intact); vient-98-name and battery-88-1727-shape are adopted as premises, not re-litigated.

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `subclass-66-98-noun` (P3) — discriminate 66's sub-class inside the X-66-98 subject role (plain noun vs substantivized infinitive), the fenced C2 rival 6. Bar: 77='le' ratification at @88 decides article-headedness; or number/agreement probes across @88/@123/@766. A plain-noun resolve hardens the subject naming to class grain.
2. `frame66-vient-80` (P3) — test the "[66] vient [80]" clause completion at @766–768: 80's infinitive reading under the A8 verb-frame grant. Bar: 80 infinitive-shaped at @768 with zero rivals → the "[66] vient [80]" clause is complete, and the C3 frame-closure stands on a finished clause rather than a half-open one.
3. `boundary-760-combine` (P2) — once `boundary-760-20role` (in flight) reports, combine its 20-role verdict with this battery's closed 'est à' frame for the final @760 call. Bar: 20 clause-initial killed AND frame closed → boundary forced after 20; any 20 role live → fence stands with both causes stated.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-66-767-frame.md` (this file).
- Queue: `val-66-767-frame` queued → `verdict`/`null`, 2026-10-09 (temp-file + rename; JSON re-validated post-write; own entry only; no downgrade; no prior verdict existed).
- Lock `val-66-767-frame.lock`: created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
