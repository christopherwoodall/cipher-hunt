# Battery verdict: det-20-window-local-paradigm — **NULL** (paradigm decided affirmative at battery grade; escalated to red team)

**Target:** `det-20-window-local-paradigm` (priority 3)
**Date:** 2026-10-09 (UTC)
**Worker:** b663a675-21a6-488b-90d1-01f68e2d8325
**Lock:** `code/crowd17/next-token/locks/det-20-window-local-paradigm.lock` created on start (agent id + UTC 2026-10-09T08:15:18Z); no stale lock present.

## Pre-registered bar (stated by worker per §2 — queue `bars` field was null)

> CLAIM (resolvable restatement): 20 admits per-window values — i.e., different windows of 20 force mutually incompatible value-classes for 20, so no monovalent value can cover the distribution and window-local treatment is forced. This bounds all future @307-style fenced batteries: if true, fenced window-local batteries are legitimate and necessary; if false, monovalent naming remains the right tool.
> ADVERSES: none listed on the queue entry. Standing law honored: §7 (67 et/veut sole true polyvalence — this battery declares nothing; polyvalence-class findings escalate to the queued P1 `poly-20-docket`).

**Numbered clauses (fixed before window-level grammatical testing):**
- (c1) @760 test: the determiner block "la première" (`11 70 82 34 29 40`, all pencil GT — the repair_parse.py gloss-(i) crib) does NOT force a valueless-20 nominal-ellipsis reading. Record whether @760 admits a grammatical 20-valued parse (re-derived) or forces valueless-20.
- (c2) Incompatibility test: @1703 forces a verbal slot for 20 ("ne pas [20]" — 94-30 is the stream's unique "ne pas"; "ne pas"+X requires X verbal in French) AND @307 forces a determiner/adjective slot for 20 ("[20] fois que" — the stream's unique 20–17 adjacency; round-14 fois corpus: 91 "X fois que" predecessors exclusively det/adj, zero nouns/verbs). PASS iff both slot-forcings hold at battery grade AND no single value-class satisfies both (a determiner cannot complement "ne pas"; an infinitive cannot premodify "fois" in "[X] fois que").
- (c3) Decision rule (pre-registered): if (c2) PASS → 20's windows force incompatible value-classes → per-window values DECIDED AFFIRMATIVE at battery grade → verdict NULL with escalation to the red team (`poly-20-docket`, queued P1), since declaring conditioned polyvalence is a red-team act per §7 (precedents: ver-78, fork-78-45-adjudication, frame-37-reexam). If (c2) FAIL → paradigm not forced → NULL with follow-ups.

## Method

Read BATTERY-PROTOCOL.md in full first. All stream facts re-derived in-session from the repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`: `load_rows` + `parse`; 1,847 pairs / 96 types asserted). `canonical.py` never touched. R5005, sealed gates, and the red-team adjudication queue untouched. Standing values used: pencil GT (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); banked (17=fois); promoted (30=pas 2026-10-08, 84=on, 87=ce, 64=qui, 79=tout, 00=pour, 47=ce); leads (94='ne' R17-001 strong lead / battery-promoted 2026-10-07 pending ratification; 62='il' demonstrated on 62-94 frames per collision-62-84, not promoted; 59='est' provisional). Kills honored: 20="fois" (§7), 20~17 split, uniform-20-particle (ellipsis-760), uniform-verbal-20-value (inf-20-nepas). Prior reports used as background and cited; no prior count trusted without re-derivation.

## Window-level evidence (re-derived, @-offsets 0-based)

**20 census: n=15** — @280 @307 @490 @642 @668 @703 @741 @760 @839 @873 @958 @1135 @1224 @1270 @1703 (byte-exact, matches prior batteries). Followers: 62 x4, 67 x3, 61/17/24/12/30/74/57/64 x1. Structural facts re-derived: `20→17` x1 (@307); `17→46` ("fois que") x1 (@308), preceded by 20; `94→30` ("ne pas") x1 (@1701, unique); `30→20` x2 (@1270, @1703); `20 62 94` trigram x3 (@760, @839, @1703).

### (c1) @760 — `40 67 11 70 82 34 29 40 20 62 94 59 39 88 66 98 80` (a5_03)

"…[40=e] [67=et/veut] **la première** [20] [62] [94] [59] [39] [88]…". Grammatical 20-valued parses exist (re-derived, confirming ellipsis-760 c1 without re-litigating it):
- (a) Noun leg: "la première [20-noun]" — 20 as feminine noun (value unnamed; 20="fois" killed, other feminine nouns open; battery-noun-20-value nulled on naming, leg not killed).
- (b) Particle leg: "la première" nominalized (noun elided) + 20 as clause-initial particle: "la première ; [20], il ne est à [88]…" (ellipsis-760 c1, PASS — stands; only the UNIFORM particle account was killed, at @1703).
No valueless-20 parse is constructible at battery grade (no standing word-frame re-segments `40 20` or `20 62`). **The determiner block does not force a valueless-20 reading** — the claim's example dichotomy ("nominal-ellipsis reading RATHER THAN a 20-value") is dissolved: at @760 the ellipsis applies to "la première", and 20 carries a value under every surviving parse.

### (c2) @1703 vs @307 — the incompatibility

**@1703** — `…85 33 94 30 20 62 94 88 26…` (a8_06) = "…[85] [33] **ne pas** [20] [62] [94] [88]…":
- `94 30` @1701–1702 is the stream's UNIQUE "ne pas" (30='pas' promoted; 94='ne' strong lead). In French, "ne pas"+X requires X verbal (infinitive); a determiner/adjective/noun cannot complement "ne pas" (*"ne pas chaque" — det-20-value c2 confirmed ungrammatical at kill grade).
- Convergent batteries: ellipsis-760 c3 (kill-grade: "'ne pas' positively requires a verbal complement, which a particle cannot satisfy"); inf-20-nepas (2026-10-09, face STANDS: "20 sits in a verbal slot at both 'pas [20]' windows, and @1703's 'ne pas [20-inf]' is a clean negative-infinitive frame" — what died there was the cross-window VALUE uniformity, killed by @1270's value-independent right-edge defect, not the @1703 slot-forcing).
- Residual loophole (stated, fenced to follow-up #3): "ne pas [20-adv] [62-inf]" — blocked only by 62='il' demonstrated (not promoted) on the 62-94 frames at @1703. The slot-forcing is kill-grade conditional on 62 non-verbal there.
- **@1703 forces: 20 ∈ verbal slot. Excludes: determiner, adjective, noun, particle.**

**@307** — `…88 02 88 20 17 46 84 24…` (a2_04) = "…[88] [02] [88] [20] **fois que** on [24]…":
- `20→17` x1 stream-wide (@307); `17→46` ("fois que") x1 (@308); 17='fois' banked, 46='que' pencil GT.
- Round-14 fois corpus (cited via det-20-value / det-20-307-fenced): 91 "X fois que" bigrams in 1840–42 diplomatic French; X exclusively determiners/adjectives ("chaque", "cette", "dernière", "plusieurs", "une", "deux"); ZERO nouns, ZERO verbs. An infinitive cannot premodify "fois" in "[X] fois que" (*"[inf] fois que" unattested, ungrammatical).
- det-20-307-fenced (2026-10-09, re-verified): only "chaque"/"une" parse "[X] fois que" standalone; leg fenced at n=1.
- **@307 forces: 20 ∈ {determiner, adjective} slot. Excludes: verbal, noun, particle.**

**Incompatibility:** {verbal} ∩ {determiner, adjective} = ∅ for a monovalent value. A determiner cannot complement "ne pas"; an infinitive cannot stand in "[X] fois que". No re-segmentation is in evidence at either window. The two slot-forcings are kill-grade (modulo the stated 62-loophole at @1703 and the 94='ne'-lead premise, both fenced not hidden).

Corroborating faces (not re-litigated): @1270 "pas [20] qui…" verbal slot (inf-20-nepas — window independently defective at its right edge, face stands); @839 "…fois vient [20] 62 94…" particle face (ellipsis-760 c2 marginal); @280 "61 [20] 61" sandwich — det values fail (det-20-value c2; 61-20-61-frame nulled 2026-10-09), a fourth window-class awaiting its own fenced battery.

## Per-clause pass/fail

- **(c1) @760 determiner-block test — "FORCES" CLAIM FAILS.** @760 admits grammatical 20-valued parses (feminine-noun leg; nominalized-"la première" + clause-initial-particle leg). The block forces no valueless-20 reading; the example dichotomy is dissolved, not decided.
- **(c2) Incompatibility test — PASS.** @1703 forces a verbal slot for 20; @307 forces a det/adj slot; the classes are mutually exclusive for any monovalent value. (Conditioned on 94='ne' lead + 62 non-verbal at @1703; the adverb loophole is fenced to follow-up #3, not ignored.)
- **(c3) Decision rule — FIRES.** (c2) PASS → per-window values DECIDED AFFIRMATIVE at battery grade.

## Verdict: **NULL** — paradigm decided affirmative at battery grade; escalated to red team

**Headline for the red team:** 20's windows force mutually incompatible value-classes — verbal slot at @1703 ("ne pas [20-inf]", clean negative-infinitive frame, face confirmed by two convergent batteries) vs determiner/adjective slot at @307 ("[20] fois que", 91/91 corpus predecessors det/adj, zero nouns/verbs). No monovalent value covers both; monovalence is refuted at battery grade. Whether the mechanism is conditioned polyvalence, a homophone set, or another multi-value scheme is a **red-team act** per §7 (67 et/veut sole true polyvalence) — this battery states the forced candidacy and routes it to the queued P1 `poly-20-docket`; it declares nothing.

**The bound for future @307-style fenced batteries** (the claim's requested deliverable): fenced window-local batteries for 20 are now legitimate AND necessary — monovalent batteries will keep nulling against the incompatibility. Each future 20 battery MUST (a) scope exactly one window-class (@307 det/adj leg; @1703/@1270 verbal face; @760/@839 particle face; @280 sandwich), (b) make no cross-window uniformity claim, and (c) route value-naming to `poly-20-docket` rather than promoting. The det-20-307-fenced null is thereby explained: it tested correctly, but "chaque vs une" discrimination cannot bound a paradigm question — only the cross-window incompatibility could, and it does.

**Standing verdicts:** none contradicted or downgraded. §7 honored (no polyvalence declared). ellipsis-760's KILL (uniform particle) and inf-20-nepas's KILL (uniform verbal value) both honored — this battery proposes neither; it uses their surviving faces. 20="fois" kill, 20~17 split untouched. R5005, sealed gates, red-team adjudication queue untouched.

## Follow-ups proposed (null regenerates work; none duplicate queued or verdict'd targets)

1. `particle-20-760-839` (P3) — Fenced window-local battery for the surviving "20 62 94" particle face at @760/@839. Bar: name the clause-initial particle value parsing BOTH windows ("la première" nominalized @760 with the ellipsis stated; the @839 clause boundary after 98 stated); @1703/@307/@280 explicitly out of scope (fenced, not explained). Feeds `poly-20-docket`.
2. `census-20-open-windows` (P3) — Slot-classify 20's nine unexamined windows (@490/@642/@668/@703/@741/@873/@958/@1135/@1224) window-local: for each, record the forced slot (verbal / det-adj / noun / particle / unforced) with the licensing frame; no cross-window value claim. Completes the per-window map the red team needs for `poly-20-docket`.
3. `nepas-20-adverb-gate` (P2) — Close the (c2) loophole: test "ne pas [20-adv] [62-inf]" at @1703. Bar: KILL the adverb rescue iff 62 is non-verbal at @1703 (62='il' holds there) — hardening this battery's verbal-slot forcing to unconditional; or DEMONSTRATE 62 verbal there, which re-opens (c2) and this verdict with it.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-det-20-window-local-paradigm.md` (this file)
- Queue: `det-20-window-local-paradigm` → status `verdict`, result `null`, report path above, date 2026-10-09 (temp-file + atomic rename; only this entry touched; JSON re-validated after write)
- Lock created on start, deleted on completion. `canonical.py` never used; R5005, sealed gates, red-team adjudication queue untouched.
