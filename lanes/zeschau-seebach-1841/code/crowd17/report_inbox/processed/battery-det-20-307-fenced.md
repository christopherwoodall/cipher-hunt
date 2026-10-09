# Battery verdict: det-20-307-fenced — **NULL**

**Target:** `det-20-307-fenced` (priority 2)
**Date:** 2026-10-09 (UTC)
**Worker:** 9f7f3dc6-ff6f-47ff-b66e-016dc99dfc96 (clean re-run; prior worker died in a runtime restart, orphaned lock cleared)
**Lock:** `code/crowd17/next-token/locks/det-20-307-fenced.lock` created on start; no stale lock present.

## Pre-registered bar (verbatim from battery-queue.json)

> CLAIM: name the @307 value with the other 14 windows of 20 out of scope
> BARS: discriminate "chaque" vs "une" on the @307 continuation; name iff one parses @307's "[X] fois que"
> ADVERSES: monovalent determiners kill-grade at @760
> EVIDENCE: battery-det-20-value.md null follow-up #1: only "chaque" and "une" parse @307; det/adj leg fenced at n=1

**Numbered clauses (pre-registered before testing):**
- (c1) Discriminate "chaque" vs "une" on the @307 continuation. PASS iff the continuation admits exactly one of the two readings at battery grade.
- (c2) Naming rule: name the @307 value iff exactly one of {chaque, une} parses @307's "[X] fois que" frame. Otherwise no name.

## Method

Read BATTERY-PROTOCOL.md in full first. All numbers re-derived from the repaired 1,847-pair stream (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`). `canonical.py` never touched. R5005, sealed gates, and the red-team adjudication queue untouched. Standing values: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que (pencil GT); 17=fois (banked), 84=on (promoted), 87=ce (granted). Scope: @307 only; the other 14 windows of 20 are out of scope per the claim.

**@307 re-derived (0-based, byte-exact):** `88 02 88 [20] 17 46 84 24 37` at offsets 304–312, i.e. `[88] [02] [88] [X] fois que on [24] [37]` (17='fois' banked, 46='que' pencil GT, 84='on' promoted, 24 verb-class, 37 open).

## Window-level evidence

### (c1) Discrimination on the continuation

The @307 continuation is `46 84 24 37` = "que on [24] [37]":

| X | "[X] fois que on [24] [37]" | c1 |
|---|---|---|
| chaque | "chaque fois que on …" — canonical habitual frame ("each time that") | parses |
| une | "une fois que on …" — canonical completive frame ("once / when") | parses |

Both readings admit the continuation. The only grammatical discriminator between them is the subordinate verb's tense: "une fois que" selects a completed-tense verb (passé composé / future anterior), "chaque fois que" a habitual present. 24's value is open (verb class only, unnamed) — its tense is unresolvable at battery grade. No other @307-local feature discriminates: elision, agreement ("fois" is feminine; both "chaque fois" and "une fois" agree), and the subject "on" are neutral to both readings.

Corpus check: "17 46" ("fois que") occurs exactly **once** stream-wide (@308) — no paradigm of other "fois que" windows exists to discriminate by analogy.

**(c1): FAIL** — the continuation does not discriminate; both readings parse and the single potential discriminator (24's tense) is unresolvable.

### (c2) Naming rule

Both "chaque" and "une" parse @307's "[X] fois que" (re-verified; confirms the parent battery det-20-value's c1). The naming condition — exactly one parses — is not met.

**(c2): NO NAME.**

### Adverse: monovalent determiners kill-grade at @760

Answered by scope, not ignored. This battery names only the @307 value (window-local, per the lane's @1714 "ne l'est pas" precedent — a window-local reading without a global value claim). It never asserts 20="chaque" or 20="une" globally, so the @760 kill-grade block on monovalent determiners does not apply within the fenced scope.

## Per-clause pass/fail

- **(c1) discriminate on the continuation — FAIL.** Both readings parse "que on [24] [37]"; 24's tense (the true discriminator) is open.
- **(c2) naming rule — NO NAME.** Both candidates parse; the bar's iff-condition is not satisfied.

## Verdict: NULL

The @307 window admits both "chaque fois que" and "une fois que" with no battery-grade discriminator. The det/adj leg stays fenced at n=1 per the parent battery.

## Follow-ups proposed (for supervisor queuing)

1. `tense-24-307` (P2) — name 24's tense/form at @311. "une fois que" requires a completed-tense subordinate verb; "chaque fois que" a habitual one. This is the true @307 discriminator; the bar is untestable until 24 resolves.
2. `left-88-02-88-307` (P3) — parse the left context @304–306 ("88 02 88"). A prepositional or clausal construction there may select one reading independently of the continuation.
3. `det-20-window-local-paradigm` (P3) — test whether 20 admits window-local values at other windows (e.g., whether @760's determiner block forces a nominal-ellipsis reading rather than a 20-value). Decides whether 20 has per-window values at all, which bounds all future @307-style fenced batteries.
