# Battery report: trans-60-1690

- Target id: `trans-60-1690`
- Claim: "Test the bare-60 verb's transitivity at @1690 (the -dre family). A transitive-60 licenses the nominal-27 direct-object frame ('en [V-ger] [27-N]') and gives 27 its first battery-grade frame-leg"
- Date: 2026-10-09
- Worker: battery worker (subagent 6b8c23b7-2f14-4e60-b0dc-7925b03401b1)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847 pairs / 96 types held in-session). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.

Terms (ASD-STE100): "object-taking window" = a window where 60 is a verb (finite, infinitive, or gerund) with a direct object, every element of the frame carrying a standing lane license (granted/promoted/battery-grade) with zero ungranted assumptions. "Battery grade" = standing values only, no open-neighbor premises.

## Bar (verbatim, pre-registered before testing)

"Transitive iff >=2 independent object-taking windows at battery grade; else the N1 leg stays assumption-bound"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1 (transitive arm):** >=2 independent object-taking windows for bare-60 at battery grade -> 60 is transitive.
2. **C2 (else arm):** else, the N1 leg ("en [V-ger] [27-N]") stays assumption-bound on the ungranted "60's verb is transitive".

Adverses: "val-27-1691-np already queued - not re-proposed" - honored; not re-proposed.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/trans-60-1690.lock` on start (agent id + 2026-10-09T20:33:30Z); no prior/stale lock; deleted on completion.
2. Re-derived the repaired stream byte-exact in-session; censused group 60: n(60)=18 at 0-based offsets [119, 172, 197, 232, 322, 454, 637, 690, 700, 995, 1338, 1366, 1474, 1563, 1644, 1674, 1690, 1735].
3. Adopted standing record (not re-litigated): 60 verb-class at battery grade, value open (-dre family: repondre/vendre/tendre/rendre/attendre/entendre/defendre/descendre/pretendre, per dre-60-rerun); bare-60 verb vs ent-60 verb are two items sharing syllable 60 (split-60-verbs PROMOTE); '60 08' x2 (@197, @1338) excluded per the vient hypothesis (intransitive "vient" anyway); "79 14 60" x2 (@1366, @1690) licensed gerundif (gerund-60-1688 PROMOTE); @995 "[60] et la" mildly disfavors strongly-transitive candidates but below kill grade (dre-60-rerun); noun-60 KILL, adj-60 KILL, dit-60-syncretic KILL; 65 noun-class (R20-047); 77='le' provisional; 94='ne' STRONG LEAD; 98='vient' LEAD; 06='ent' granted-conditional; 67 positional rule (et/veut sole polyvalence); 03/09/12/15/71/90 class-open.

## Object-taking sweep (all 18 windows)

For each window: is 60 a verb with a direct object licensed by standing values only?

- @119: "21 [60] 90" - follower 90 open, predecessor 21 open. No.
- @172: "21 [60] 09 87 86" - "[60] [09] ce[87] [86-INF]": 09 open. No licensed object. No.
- @197: '60 08' vient arm (excluded; intransitive). No.
- @232: "21 [60] 71" - 71 open. No.
- @322: "92 [60] 15" - 15 open. No.
- @454: "79 17 77 [60] 65 13" = "tout[79] fois[17] le[77] [60] [65] en[13]" - the only window with a licensed noun (65) adjacent to 60. Tested both arms:
  - Arm 1 ("le" as object clitic + finite 60): needs a subject before "le"; 17='fois' is a noun, not a subject. Fails.
  - Arm 2 ("[60] [65-N]" verb + noun object): needs 77='le' to attach leftward ("fois le"), which is ungrammatical (77='le' provisional masculine vs 17='fois' feminine; no licensed "fois le" frame). Fails.
  - Consistent with the standing fence (ellipsis-65-62-60-profile; npframe series). No.
- @637: "46 [60] 67 77 89" = "que[46] [60] et[67] le[77] [89]" - relative "que" + finite 60, but no direct object (follower is coordination "et le [89]"). No.
- @690: "65 94 29 [60] 03 39" = "[65] ne[94] er[29] [60] [03] a[39]" - "29 60" order is 'er'-before-60 (no licensed word formation); 03 open. No.
- @700: "94 [60] 12 98" = "ne[94] [60] n[12] vient[98]" - ungrammatical under every French verb (verb-60-bare, adopted). No.
- @995: "03 [60] 67 11" = "[03] [60] et[67] la[11]" - no object ("[60] et"). No.
- @1338: '60 08' vient arm (excluded; intransitive). No.
- @1366: "14 [60] 03 30" = "en[14] [60] [03] pas[30]" - gerund; follower 03 open. No.
- @1474: "53 [60] 06 67" = "[53] [60]ent[06] veut[67]" - 3pl finite; no object. No.
- @1563: "06 [60] 71 50" (ent-60 verb, V5) - 71 open. No.
- @1644: "98 [60] 03 64" = "vient[98] [60] [03] qui[64]" - infinitive 60; 03 open. No.
- @1674: "92 [60] 03 39" - 03 open. No.
- @1690: "14 [60] 27 46" = "en[14] [60] [27] que[46]" - gerund; 27 is the open item under test (the conclusion, not a leg). No.
- @1735: "06 [60] 12 48" (ent-60 verb, V6) - 12 open. No.

Follower census for 60: {90, 09, 08x2, 71x2, 15, 65, 67x2, 03x4, 12x2, 06, 27}. Licensed among them: 08 (vient arm, excluded/intransitive), 06='ent' (inflectional, not nominal), 65 (fenced at @454 above). Preverbal object clitic contact: only @454 ("77 60"), fenced above. **Zero object-taking windows at battery grade.**

## Per-clause pass/fail

- C1: FAIL. Zero battery-grade object-taking windows; the bar needs >=2.
- C2: FIRES. The N1 leg ("en [V-ger] [27-N]") stays assumption-bound on the ungranted "60's verb is transitive" - exactly the state class-27-independent left it in. This battery adds the negative result: no stream window supplies the transitivity leg at battery grade.

## Verdict: NULL

Not kill: failing to find >=2 object windows does not force 60 intransitive (absence of evidence; object drop/ellipsis and open neighbors keep every -dre candidate alive per dre-60-rerun). The bar's else-arm is the verdict: N1 stays assumption-bound. No standing/red-team verdict contradicted, downgraded, or re-litigated; §7 intact. Canonical-stream caveat stands.

## Follow-ups (for supervisor queuing; all verified ABSENT from the queue; val-27-1691-np not re-proposed per adverses)

1. `obj-60-454-resolve` (P4) - resolve @454's "le [60] [65]" frame: re-test if 77='le' gains a subject via a banked clause boundary, or if 65's value licenses a "[60] [65-N]" verb-object parse with 77 attaching elsewhere.
2. `val-03-690-class` (P4) - name 03's class at @690/@1644/@1674; a nominal 03 turns the four "[60] [03]" windows into candidate object frames.
3. `subj-60-finite` (P4) - name 60's subject at the finite windows (@637 "que [60]", @700 "ne [60]", @995); a forced subject plus any postverbal licensed noun completes an object leg.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-trans-60-1690.md`
- Queue: `trans-60-1690` queued -> `verdict`/`null`, 2026-10-09 (pre-write assert passed - was queued/verdictless; target-id-unique tmp `battery-queue.json.trans-60-1690.tmp` + rename; disk re-validated; own entry only; no downgrade)
- Lock `locks/trans-60-1690.lock`: created on start, deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
