# Battery report: rival-elim-ratify

- Target id: `rival-elim-ratify`
- Claim: "Red-team ratifies the porter+envoyer eliminations (V+me+order ungrammaticality, envoyer non-causative, tension resolution); claim promotes on ratification."
- Date: 2026-10-09
- Worker: battery worker (subagent 701e78bd-b9ab-4ece-a793-6d87bacb9830)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.

Terms (ASD-STE100): "causative class" = the French verbs that license a post-infinitive object clitic ("faire", "laisser"). "Clitic" = a small word like "me" that must attach to a verb. "Proclitic" = the clitic stands BEFORE the verb ("me porter"). "Post-infinitive" = the clitic stands AFTER the infinitive ("porter me"). "Ratify" = a red-team act; a battery cannot ratify. This report VERIFIES an existing ratification, it does not perform one.

## Bar (verbatim, pre-registered before testing)

"(a) confirm the V+me+order ungrammaticality for non-causative -er verbs under every 16-class; (b) confirm envoyer is not causative-class; (c) ratify the erstem tension resolution; then the claim promotes."

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** the V+me+order ungrammaticality for non-causative -er verbs holds under every live 16-class at the @1477 discriminator → PASS.
2. **C2:** envoyer is not causative-class → PASS.
3. **C3:** the erstem-33-id vs x-33-laisser-test tension resolution is ratified in the red-team record and stands → PASS.

Queue adverses: "gates moot (kills gate-independent) - state explicitly." Stated in Scope. Supervisor note (red-team decision target, do not dispatch as battery worker): recorded, not obeyed — dispatched by parent with the gate-satisfied determination; this report verifies the existing R19-188 ratification rather than performing a new one.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/rival-elim-ratify.lock` on start (agent id + 2026-10-09T18:45:01Z); no prior/stale lock; deleted on completion.
2. Re-derived the repaired stream byte-exact in-session (1,847 pairs / 96 types asserted).
3. Re-derived the @1477 locus byte-exact. Read the R19 red-team report (R19-188 ruling text) and the R20 red-team report (standing check). Read battery-frame-82-16 (2026-10-09) and battery-laisser-unique-sweep (2026-10-09) as lane-record evidence (adopted, not re-litigated).
4. Ran an independent corpus check on the widened 80-file period corpus (54,161,871 chars; German files excluded): targeted "porter|envoyer + me/m' + verb" post-infinitive pattern, plus the proclitic control.
5. 1841 French throughout. No invented numbers.

## Locus re-derivation

0-based @1477, row a7_10: `... 53 60 06 67 | 33 29 | 82 16 | 98 62 46 77 ...`
Standing values: 29="er" banked, 82="m" banked, 06="ent" promoted (R17-007), 67 et/veut positional rule, 98="vient" LEAD. Reads: "[67=veut] [33]er m[16] vient" — an infinitive (33+er) followed by clitic "me" (82) followed by 16, then "vient".

## Per-clause pass/fail

### C1 — PASS

- The violation is at the "[33]er + me" contact, which sits BEFORE 16. Under every live 16-class (finite verb vowel-initial per battery-frame-82-16's live hypothesis; infinitive per the contested battery promote; all other classes killed), a non-causative -er infinitive followed by postposed "me" is kill-grade ungrammatical in 1841 French. Clitics must precede the verb they govern ("veut me porter [16]"); post-infinitive placement is licensed only by the causative class and imperatives. 16's class cannot move the clitic, so the kill is 16-class-independent.
- Independent corpus check (54,161,871 chars, 80 French files): pattern `\b(port|envoy)er\b` + `m[e']` + verb (post-infinitive clitic): **1 raw hit**, hand-classified as OCR noise ("porter \\nen m<>me temps" — not a verb). **0 genuine.** Proclitic control (`m[e'] + porter|envoyer`): 13 hits (e.g. "me porter" x4 in Revue des deux mondes / Metternich / Pozzo di Borgo). The grammatical order is attested; the ungrammatical order is a zero at 54M chars.
- Lane-record corroboration: laisser-unique-sweep (2026-10-09) independently re-tested all 7 erstwhile -er candidates (donner, montrer, prouver, trouver, porter, envoyer, prononcer) against the @1477 frame — all 7 die at kill grade, 16-class-independent; its own corpus check found 0 genuine "V(-er, non-causative) + me + INF" in 29,487,677 chars.
- R19-188 already RATIFY'd this kill ("post-infinitive clitic after non-causative -er verb kill-grade ungrammatical under every 16-class").

### C2 — PASS

- The French causative periphrastic class is closed: {faire, laisser}. "envoyer" is a ditransitive verb of sending/transfer, not a causative. "envoyer qqn [inf]" requires clitic climbing ("veut m'envoyer [16]"), which contradicts the observed post-infinitive order at @1477.
- The corpus zero in C1 covers envoyer explicitly (pattern included porter|envoyer).
- R19-188 already RATIFY'd: "envoyer ditransitive not causative".

### C3 — PASS (verification of existing ratification)

- R19-188 ruling text (red-team round-19 report, `code/crowd17/report_inbox/processed/next-token-redteam-r19.md`, section "R19-188: rival-elim-ratify (P1) — RATIFY the porter+envoyer eliminations"): "@1477-0b re-derived ('veut [33]er m[16] vient')... erstem-33-id vs x-33-laisser-test tension resolved on word order. 'laisser' unique among TESTED candidates (value not promoted here)."
- Standing at R20: the R20 red-team report (`code/crowd17/report_inbox/processed/next-token-redteam-r20.md`, line 33) states "Every other standing R15–R19 grading is confirmed, none overwritten." R20 contains no re-litigation of R19-188 (zero mentions of porter/envoyer/rival-elim). R19-188 stands.
- R19-188's condition ("kills assume the standing '82 16'='m''+verb segmentation"): battery-frame-82-16 (2026-10-09) found 82-16 x11 = "m'a"/"m'est" (elided "me" + vowel-initial verb) and killed the "même"/"mais"/noun alternatives; laisser-unique-sweep verified the condition holds today (n(82 16)=11 confirmed on the re-derived stream). No battery has proposed a word-internal re-segmentation of "82 16". The condition holds; @1477 is not re-opened.

All three clauses pass. No adverses unanswered. The claim promotes on the recorded ratification.

## Verdict: PROMOTE

The porter+envoyer eliminations are ratified and standing: R19-188's ratification is in the red-team record, confirmed by R20, its segmentation condition holds, and an independent 54.16M-char corpus check re-confirms the kill-grade ungrammaticality.

## Scope (stated, not hidden)

- **This verdict verifies; it does not ratify.** The ratification is R19-188's (red-team act). A battery cannot perform red-team ratification, and this report does not claim to.
- **Gate-independence (queue adverse, stated explicitly):** the porter/envoyer kills are gate-independent. They rest on banked 29="er", banked 82="m", 1841 French clitic grammar, and the R19-188 ratification. No open gate (16's value, 85's value, 98's value) can rescue the post-infinitive order.
- Registry: none (matches R19-188's "Registry: none"). porter and envoyer are eliminated as 33-candidates only. 33 remains unnamed; 16 and 85 remain open. 98="vient" stays LEAD; the "dire" whole-face (A10 HOLD) is untouched.
- Canonical-stream caveat stands: row a7_10's offset unvalidated (68/70).
- No standing or red-team verdict contradicted, downgraded, or re-litigated. §7 intact.

## Follow-ups

None required (promote verdict, per §4 only nulls must propose follow-ups).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-rival-elim-ratify.md` (this file).
- Queue: `rival-elim-ratify` queued → `verdict`/`promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/rival-elim-ratify.lock` created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
