# Battery verdict: subj-20-642 — **PROMOTE** (class named at @642)

## Target
- id: `subj-20-642` (priority 3)
- claim: "resolve 20's class at @642 (the direct C2 blocker for finite-24 at @643)"
- Parent: `form-24-643` NULL (2026-10-09) — follow-up 1 of 3.
- adverses: none listed.

## Bar (verbatim from battery-queue.json)
"name 20's class at @642 with zero ungranted assumptions; fence if undecidable"

Numbered pass/fail clauses (restated before testing — bar not modified after data):
1. **C1:** 20's class is named at @642 with zero ungranted assumptions → promote.
2. **C2:** if C1 fails, fence @642 with stated cause.

Verdict rule: promote iff C1 passes; else null with fence.

## Method
Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/subj-20-642.lock`
on start (agent f8fa9655-a4d5-420a-8d75-c5a95376e736, 2026-10-09T11:34:44Z); no prior/stale
lock. Re-derived the repaired 1,847-pair / 96-type stream in-session from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
(byte-exact tokenization per `code/side-keyhunt/repair_parse.py`; asserts held:
1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gate instances,
and the red-team adjudication queue untouched.

Adopted standing premises (used, not re-litigated):
- §7: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que (pencil GT); 87=ce,
  64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce; 59=est / 77=le
  provisional; 67 et/veut sole polyvalence with the positional rule standing
  (67="veut" iff follower infinitive-shaped).
- R17-009: 24 finite/modal-shaped verb class (value open).
- "le [89]e" = closed NP, noun forced (arm A battery verdict); 48="e"
  inflectional (promoted).
- `det-87-644-function` PROMOTE (2026-10-09): 87 = determiner at @644, so
  "[24] ce [61]" = verb + NP object "ce [61]"; 61 nominal/adjectival at @645.
- `conj-prep-20-wide` NULL (2026-10-09): conjunction/preposition route for 20
  fenced across the full profile — adopted as fence, not re-litigated.
- `adverb-20-wide` NULL (2026-10-09): clause-adverb route for 20 fenced — adopted.
- `noun-20-value`, `det-20-value` NULL (global value searches; no window verdicts).
- `poly-20-docket` (queued P1): 20's GLOBAL class (NOUN vs DET/ADJ) is red-team
  venue — this verdict is window-level only and feeds the docket, not a
  global class claim.

## Locus (byte-exact, re-derived)
0-based @632–648, rows a4_01/a4_02:
`52 63 74 46(que) 60 67 77(le) 89 48(e) |20| 24 87(ce) 61 88 77(le) 78`

Focal geometry: `…67(et) 77(le) 89 48(e) |20| 24 87(ce) 61…`
- @638 67: follower 77="le" (provisional) is not infinitive-shaped → 67="et"
  by the standing positional rule.
- @639–641 "77 89 48": the closed NP "le [89]e" (noun forced, arm A).
- @643 24: finite/modal class (R17-009).
- @644–645 "87 61": the verb's NP object "ce [61]" (`det-87-644-function`).
- 20 sits between a complete subject-position NP and the verb of its clause:
  `…et le [89]e [20] [24] ce [61]…`

## Class elimination at @642

1. **Post-nominal adjective (a):** "le [89]e [20]" = determiner + noun + adjective
   as the subject NP of 24. Parses with zero new assumptions. **Survives.**
2. **Clause-adverb (b):** "*le [89]e [20-adv] [24-fin]" — a bare adverb cannot
   intervene between subject and finite verb in 1841 French (time adverbs front
   the clause; manner adverbs follow the verb). Grammar-level death, consistent
   with the `adverb-20-wide` fence.
3. **Noun / apposition (c):** "le [89]e, [20]" needs a comma plus a title-like
   20 — ≥1 ungranted assumption (naming + punctuation the cipher never
   supplies). Unlicensed at battery grade.
4. **Finite verb (d):** two finite verbs in sequence ("le [89]e [20-fin]
   [24-fin]") — ungrammatical every period. Dead.
5. **Infinitive (e):** noun + bare infinitive with no preposition ("*le livre
   écrire") — ungrammatical. Dead. (This does not touch the forced-infinitive
   20 at @1703 — window-level only.)
6. **Conjunction (f):** a subordinator needs "le [89]e" to be a complete matrix
   clause — it is a bare NP with no verb. Dead. A coordinator leaves 20
   dangling with no second conjunct. Dead. (`conj-prep-20-wide` fence adopted
   as an independent leg.)
7. **Preposition (g):** complement would be 24, a verb-class token, not an NP.
   Dead. (Same fence adopted.)
8. **Determiner (h):** post-nominal determiner with no following noun
   (24 is verb-class). Dead.
9. **Pronoun / second subject (i):** two subjects for one finite verb,
   uncoordinated. Dead.
10. **Word-internal with "89 48" (j):** 48="e" is a promoted inflectional
    ending; no license for 20 as bound word-final — dead under the lane's
    word-internal standard.

Arm (a) is the **unique grammatical survivor** at battery grade.

## Verdict: PROMOTE

**20's class at @642 = post-nominal adjective** ("le [89]e [20]" = "the [X] [20]").
C1 passes: the class is named with zero ungranted assumptions — the assumption
audit below lists every premise as standing, and every rival arm is dead or
fenced with stated cause. C2 moot.

**Assumption audit (all standing, none ungranted):**
1. 77="le" — provisional, protocol-listed standing premise (used the same way
   by `census-20-open-windows`).
2. "le [89]e" noun-forced — adopted arm-A battery verdict.
3. 67="et" — standing positional rule (follower 77 not infinitive-shaped).
4. 24 finite/modal class — R17-009 standing.
5. 87=ce granted; 61 nominal/adjectival — standing battery verdicts.
6. Rival-arm eliminations: 1841 French grammar (b, d, e, h) + adopted standing
   fences (`conj-prep-20-wide`, `adverb-20-wide`) + naming-standard bar (c, j).

## Scope and caveats
- **Window-level only.** 20's global class stays red-team venue in
  `poly-20-docket` (NOUN vs DET/ADJ); this verdict feeds it — a DET/ADJ-side
  datum — and does not name a global value or class.
- §7 intact: no polyvalence declared; 67 remains the sole true polyvalence.
- No standing or red-team verdict contradicted or downgraded. The forced
  infinitive-20 at @1703 and forced finite-verb-20 at @873 (adopted from
  `nepas-20-adverb-gate`/`census-20-open-windows`) are untouched — this verdict
  does not and need not name 20's class at those windows.
- Canonical-stream caveat stands: rows a4_01/a4_02 upstream row offsets
  unvalidated (protocol §7).
- Parent consequence: `form-24-643`'s C2 blocker is removed — with 20 placed
  inside the subject NP "le [89]e [20]", 24's finite/modal reading at @643
  stands free of the 20-class block (subject now cleanly identified).

## Follow-ups (promote needs none — one narrow continuation)
1. `agr-89-642-adj` (P3) — agreement check: does "le [89]e" admit an
   adjectival 20 (gender/number compatibility once 89's value resolves)?
   Bar: confirm or fence the adjective arm on agreement grounds.

## Bookkeeping
- Queue: `subj-20-642` → `status: verdict`, `result: promote`, 2026-10-09
  (pre-write assert passed — was `queued`/verdictless; temp-file + rename;
  JSON re-validated; own entry only; no downgrade).
- Lock `locks/subj-20-642.lock` created on start, deleted on completion
  (verified gone).
