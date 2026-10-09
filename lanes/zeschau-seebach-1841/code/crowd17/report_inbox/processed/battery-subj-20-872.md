# Battery verdict: subj-20-872 — **NULL** (fence executed per the bar's else-arm)

## Target
- id: `subj-20-872` (priority 3)
- claim: "Re-run the subj-20-642 method at the @872 twin (87 77 89 48 20 74); tests whether 20's post-nominal-adjective class replicates at the second '89 48 20' window."
- Parent chain: `conj-20-642-subordinator` NULL (2026-10-09) — follow-up 2 of 2; grandparent `subj-20-642` PROMOTE (2026-10-09, 20 = post-nominal adjective at @642).
- adverses: none listed.

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"class named with zero ungranted assumptions, or fence @872."

Numbered pass/fail clauses (restated before testing — bar not modified after data):
1. **C1:** 20's class is named at the twin with zero ungranted assumptions → promote.
2. **C2:** if C1 fails, fence @872 with stated cause.

Verdict rule (adopted from the parent battery): promote iff C1 passes; else null with fence.

## Method
Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/subj-20-872.lock`
on start (agent dc37c084-298d-43ea-9273-168ff527d2db, 2026-10-09T19:07:50Z); no prior/stale
lock. Re-derived the repaired 1,847-pair / 96-type stream in-session from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
(byte-exact tokenization per `code/side-keyhunt/repair_parse.py`; asserts held:
1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gate instances,
and the red-team adjudication queue untouched.

Adopted standing premises (used, not re-litigated):
- §7: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que (pencil GT); 87=ce,
  64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce; 59=est / 77=le
  provisional; 67 et/veut sole polyvalence with the positional rule standing.
- `subj-20-642` PROMOTE: 20 = post-nominal adjective at @642 (window-level),
  geometry `67(et) 77(le) 89 48(e) |20| 24-fin 87(ce) 61` — 20 between a
  complete subject-position NP "le [89]e" and the finite verb 24.
- `conj-20-642-subordinator` NULL: "89 48 20" occurs exactly 2x stream-wide;
  the twin named as `@872` under the trigram's 48-position convention
  (cf. that report's "'89 48 20' occurs 2x (@641, @872)").
- "le [89]e" = closed NP, noun forced (arm A battery verdict); 48="e"
  promoted inflectional letter tier.
- `ce-le-verb-frame` NULL (2026-10-08): the preverbal "87 77" ce+le stack is
  fenced as a 77-value residual at @515/@611/@869 — no grammatical account
  survives battery-grade testing.
- `celle-7780-fusion-515-869` KILL (2026-10-09): the '87 77' = 'celle' fusion
  is closed at kill grade at both loci (@515, @869).
- `conj-prep-20-wide` NULL, `adverb-20-wide` NULL: conjunction/preposition and
  clause-adverb routes for 20 fenced profile-wide — adopted as fences.
- 74, 49, 16: no class or value verdict anywhere (all absent from
  `table-registry.json`).
- `poly-20-docket` (queued P1): 20's GLOBAL class is red-team venue — this
  verdict is window-level only.

## Index note (recorded, not hidden)
The claim's "@872" follows the conj report's trigram convention (naming by the
48 position). On the repaired 0-based stream the pattern "87 77 89 48 20 74"
is byte-exact at **0-based @869–874**: `87@869 77@870 89@871 48@872 |20@873| 74@874`,
row a5_07. The parent id `subj-20-642` named 20's own position (0-based @642);
this id names the trigram's 48 position. All offsets below are 0-based.

## Locus (byte-exact, re-derived)
0-based @860–886, row a5_07:
`49 74 74 48 47(ce) 46(que) 00(pour) 86 70(pre) 87(ce) 77(le) 89 48(e) |20@873| 74 49 16 77(le) 86 78 17(fois) 08 31 79(tout) 68 37`

Focal geometry: `…87(ce) 77(le) 89 48(e) |20| 74 49 16…`

Twin vs parent — two structural differences:
1. **Left:** parent had `67(et) 77(le) 89 48` (coordinator cleanly outside the
   NP). The twin has `87(ce) 77(le) 89 48` — "ce le [89]e" stacks two
   determiners. Under standing values this contact is not a licensed NP
   opening: the '87 77' = 'celle' fusion is KILLED at this exact locus
   (@869), and the two-word "ce le" reading is fenced as a 77-value residual
   with no grammatical account (`ce-le-verb-frame`).
2. **Right:** parent had 24 in the finite/modal verb class (R17-009) — the
   clause verb that the subject NP "le [89]e [20]" governed. The twin has
   74/49/16, all class-open, and no finite-class verb anywhere in the window.

## Class elimination at @873 (parent method re-run)

1. **Post-nominal adjective (a):** "le [89]e [20]" as subject NP of a following
   finite verb. Fails twice: (i) the NP cannot open — the preceding "87 77"
   contact is a standing residual (fusion killed, two-word reading fenced, no
   grammatical account); (ii) there is no finite verb for the NP to govern —
   74/49/16 are all class-open, and naming 74 finite is an ungranted
   assumption. **Cannot be named with zero ungranted assumptions.**
2. **Clause-adverb (b):** dead on 1841 French grammar (bare adverb between
   subject and verb), and the `adverb-20-wide` fence is adopted profile-wide.
3. **Noun / apposition (c):** needs a comma plus a title-like 20 — ungranted
   naming + punctuation the cipher never supplies.
4. **Finite verb (d):** needs a subject; the only left candidate ("ce le
   [89]e") is itself unlicensed (see above). Ungrammatical without ungranted
   repairs.
5. **Infinitive (e):** noun + bare infinitive with no preposition —
   ungrammatical. (Does not touch the forced-infinitive 20 at @1703 —
   window-level only.)
6. **Conjunction (f):** subordinator needs a complete matrix clause — left is
   a bare NP with no verb; coordinator leaves 20 dangling. Dead; the
   `conj-prep-20-wide` fence is adopted as an independent leg.
7. **Preposition (g):** complement would be 74, a class-open token, not an NP.
   Dead; same fence adopted.
8. **Determiner (h):** post-nominal determiner with no following noun. Dead.
9. **Pronoun / second subject (i):** needs a finite verb — none present. Dead.
10. **Word-internal with "89 48" (j):** 48="e" is promoted inflectional; no
    license for 20 as bound word-final — dead under the lane's word-internal
    standard.

No arm names a class with zero ungranted assumptions. C1 FAILS.

## Verdict: NULL (fence executed per the bar's else-arm)

**20's post-nominal-adjective class does NOT replicate at the twin.** The twin
window is fenced with stated cause: the left NP cannot open under standing
values ("87 77" is a standing residual at @869 — fusion killed, two-word
reading fenced with no grammatical account), and the right side offers no
finite verb (74/49/16 all class-open). The post-nominal-adjective arm would
need ≥2 ungranted assumptions (a licensed "87 77" parse; a finite 74).

**The twin keeps the @642 fence company, not the @642 promote.** The
@642 post-nominal-adjective PROMOTE (`subj-20-642`) is untouched and stands;
this verdict records that its conditions do not transfer to the second
"89 48 20" window.

## Scope and caveats
- **Window-level only.** 20's global class stays red-team venue in
  `poly-20-docket`; this verdict feeds it a fenced-window datum.
- §7 intact: no polyvalence declared; 67 remains the sole true polyvalence.
- No standing or red-team verdict contradicted or downgraded. The @642
  post-nominal-adjective PROMOTE, the @642 conjunction fence, the forced
  infinitive-20 at @1703, and the forced finite-verb-20 at @873 (adopted from
  `census-20-open-windows`) are all untouched.
- Canonical-stream caveat stands: row a5_07 upstream row offset unvalidated.

## Follow-ups (nulls regenerate work; all verified ABSENT from battery-queue.json)

1. `verb-74-874-class` (P3) — name 74's class at @874; a finite-74 would
   supply the clause verb the twin's adjective arm needs. Bar: finite class
   with ≥2 independent frame-legs at battery grade, else fence.
2. `agr-89-872-adj` (P3) — twin of `agr-89-642-adj`: agreement check for
   "le [89]e" at @871 against 20's adjective candidacy once 89's value
   resolves. Bar: confirm or fence the adjective arm on agreement grounds.
3. `ce-le-869-residual-input` (P4, gather-only) — package the @869 "87 77"
   residual (`ce-le-verb-frame` fence + `celle-7780-fusion-515-869` kill) as
   red-team input for the 77-value venue; the twin's NP frame cannot complete
   until 77's value resolves. No adjudication.

## Bookkeeping
- Report: `code/crowd17/report_inbox/battery-subj-20-872.md` (this file).
- Queue: `subj-20-872` → `status: verdict`, `result: null`, 2026-10-09
  (pre-write assert passed — was `queued`/verdictless; temp-file + rename;
  JSON re-validated; own entry only; no downgrade).
- Lock `locks/subj-20-872.lock` created on start, deleted on completion
  (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
