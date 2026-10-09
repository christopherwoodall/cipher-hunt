# Battery report: reinforced-head-governed-topology-drama

- Target id: `reinforced-head-governed-topology-drama`
- Claim: "full-resolution map of all 41 drama dem-comma windows (drop the '!' filter) - classify how each actually resolves"
- Date: 2026-10-09
- Worker: battery worker (subagent 55fd5591-c94b-46da-8f86-c16b92aad357)
- Stream: not applicable — corpus census against period French drama, per target charter. The 1,847-pair repaired parse was not used. R5005, sealed gate instances, and the red-team adjudication queue were not touched.

Terms (ASD-STE100): "reinforced head" = a demonstrative compound marked with -là or -ci (celui-là, ceux-là, celle-là, celles-là, celui-ci, ceux-ci, celle-ci, celles-ci), per the family glossary. "Dem-comma window" = a reinforced head followed by `[,;:]` in the 14-play drama corpus (2,939,372 chars). "Exclamatory resolution" = any phrase terminated by "!" in the window's turn whose topic/head is the reinforced demonstrative — infinitive or otherwise. Dropping the '!' filter means: audit the FULL turn (no 180-char cap, no sentence-end cap, no requirement that the window contain "!").

## Parentage

Follow-up of the NULL `reinforced-head-topology-drama` (2026-10-09), which delivered a 9-class full-resolution map of the 41 windows but could not earn its sharpening clause ("reinforced heads govern infinitives, but never exclamatory" — only 1/41 strict leg). This battery re-derives the map with full-turn context, explicitly audits every window for any exclamatory resolution the '!' filter could have hidden, and closes the grandparent's fenced recall gap (dash/parenthesis-delimited heads: "celui-là — ...").

## Bar (verbatim, pre-registered before testing)

"a complete resolution topology of the 41 windows; any undiscovered exclamatory resolution re-opens the pairing"

Numbered pass/fail clauses (restated before testing, not modified after):

1. All 41 dem-comma windows are reproduced byte-exact and each is classified into a stated resolution class with full-turn context evidence (no '!' filter, no 180-char cap).
2. Every window is explicitly audited for an exclamatory resolution tied to the reinforced head (any "!"-terminated phrase whose topic is the head, infinitive or otherwise).
3. The recall-gap extension is run: dash/parenthesis-delimited reinforced heads ("celui-là — ...", "celui-là (...)") are extracted corpus-wide and audited for exclamatory-infinitive pairing.
4. If clause 2 or 3 finds a genuine reinforced-head + exclamatory-infinitive attestation → the pairing re-opens (promote). If zero → the fenced pairing stands confirmed (null per §4: zero is an absence, not a refutation).

## Method

1. Read BATTERY-PROTOCOL.md first. Created lock `code/crowd17/next-token/locks/reinforced-head-governed-topology-drama.lock` on start (agent id + UTC timestamp 2026-10-09T17:33:07Z; no lock, stale or fresh, existed for this id).
2. Re-ran the parent's extraction script verbatim (`reinforced_head_topology_drama.py`): 41/41 windows reproduced with identical per-file counts (musset 11, ruy-blas 6, tour-de-nesle 6, kean 4, verre-d-eau 3, mariage-louis-xv 2, chatterton 2, burgraves 2, bertrand-et-raton 2, antony 1, henri-iii 1, chapeau-de-paille 1, hernani 0, poudre-aux-yeux 0).
3. New script `reinforced_head_governed_topology_drama.py`: for each window, extracted the FULL turn (to next blank line, cap 2000 chars); machine-flagged (a) governed infinitives before "!", (b) bare infinitive + "!", (c) any "!". All flags hand-audited. Dash/paren heads extracted corpus-wide with the same audit.
4. Spot-verified the parent's 9-class assignments for all 15 less-mechanical windows (classes D, F, G, H, I) against full-turn context.

## Window-level evidence: the full-turn exclamatory audit

11/41 windows contain "!" in their full turn. Every exclamation hand-classified; none is a reinforced-head + exclamatory-infinitive resolution:

| idx | file @off | head | "!" context | resolution |
|---|---|---|---|---|
| 4 | musset @2635 | celle-ci | "pleine de jeunes gens, de valets !" | exclaimed ADJECTIVAL apposition, not an infinitive (parent class H — corpus's closest approach, confirmed) |
| 6 | musset @54850 | celui-ci | "Cordiani ! Cordiani !..." | vocative (class F) |
| 10 | musset @248302 | celui-là | "Je peux si je veux !" | direct speech, finite clause (class F) |
| 24 | tour-de-nesle @20203 | celui-là | "Oh !" / "Eh bien !" | interjections; "sauver" is bare under modal "faut", not exclaimed (class C) |
| 30 | henri-iii @33211 | ceux-là | "morbleu !" / "Tête Dieu !" | interjections; "de décrocher" governed by "l'occasion", head-unrelated (class D) |
| 31 | kean @43821 | ceux-là | "ils abaissent ce qui est grand !" | finite clause; "de produire" governed by "impuissance", head-unrelated (class A) |
| 33 | kean @66336 | celui-là | "Coterie ! coterie !" | quoted noun exclamation (class D) |
| 35 | bertrand-et-raton @110103 | ceux-là | "j'aimerais mieux mourir !" | 1st-person modal wish; head is the infinitive's OBJECT ("les perdre"), not its governor (class C) |
| 38 | verre-d-eau @36952 | ceux-là | "les plaintes des nouveaux !" (finite); "pour être ma maîtresse !" (see below); "je l'ordonne moi, la reine !" (finite) | class C; "de les accueillir" embedded in finite clause, not exclaimed |
| 39 | verre-d-eau @124330 | celui-là | "N'en parlons plus, qu'elle vienne !" | quoted subjunctive (class B) |

The remaining 30/41 windows have no "!" in their full turn at all.

### New observation — idx 38: "pour être ma maîtresse !"

The full-turn audit surfaced one genuine **governed exclamatory infinitive** inside a reinforced-head turn: "Ah ! quand ne serai-je plus reine, pour être ma maîtresse !" (verre-d-eau @36952 turn). Its understood subject is "je" (the Queen) — it is NOT headed by, and has no anaphoric link to, the reinforced head "ceux-là" (whose clause closed two sentences earlier: "ceux-là, je ne suis pas libre de les accueillir…"). This is consistent with the sibling `gov-excl-inf-register-drama` PROMOTE (1 genuine governed exclamatory infinitive in drama, non-demonstrative topic): the construction exists in drama print; it never pairs with a reinforced-demonstrative topic. It hardens the fence rather than re-opening it.

### Recall-gap extension: dash/parenthesis-delimited heads

`DEM_REINF` followed by `[—–-]` or `(`: **0 hits** in the entire 14-play corpus (2,939,372 chars). The grandparent's fenced recall gap is empty — P1's `[,;:]` pattern missed nothing on this axis. No dash/parenthesis-delimited reinforced head exists to audit.

### Parent-map verification

15/15 spot-checked windows (all of classes D, F, G, H, I) confirm the parent's assignments under full-turn context; the 11 "!" windows above confirm classes A, B, C, F, H as listed. No reclassification. Adopted topology (parent's, verified): A copular/cleft 13, B clitic resumption 6, C infinitive-as-object 3, D finite anaphoric 8, E verbless appositive 4, F direct speech/vocative 2, G relative clause 2, H adjectival exclamation 1, I deictic fragment 2 = 41.

## Per-clause pass/fail

1. Complete resolution topology of all 41 windows with full-turn evidence: **PASS.** 41/41 reproduced, classified, and verified; no reclassifications.
2. Exclamatory-resolution audit of every window: **PASS (audit complete); no undiscovered exclamatory resolution.** 0/41 windows show a reinforced head heading an exclamatory infinitive. The one governed exclamatory infinitive found in a head turn (idx 38, "pour être ma maîtresse !") is not head-tied.
3. Dash/paren recall-gap extension: **PASS (extension complete); 0 heads found.** The gap is empty.
4. Re-open condition: **does not fire.** Zero genuine reinforced-head + exclamatory-infinitive attestations.

## Verdict: NULL (pairing stays fenced; map confirmed, no new delta)

The commissioned deliverable — the full-resolution topology with the '!' filter dropped — is complete and verified against full-turn context. No undiscovered exclamatory resolution exists in the 41 windows, and the dash/parenthesis recall gap is empty. Per §4 this is a null, not a kill: the zero is an absence. The reinforced-head + exclamatory-infinitive pairing stays fenced across both registers (prose 0/27.66M + drama 0/2.94M, now with full-turn and dash/paren coverage). The idx-38 "pour être ma maîtresse !" observation sharpens the fence's positive boundary: drama HAS the governed-exclamatory-infinitive construction — it just never takes a reinforced-demonstrative topic.

No standing/red-team verdict contradicted; §7 intact. No adverses pre-registered; self-check: consistent with `gov-excl-inf-register-drama` PROMOTE (1 genuine, non-demonstrative topic) and `personal-tonic-governed-interr-drama` PROMOTE (tonic-head interrogative is a different head class and force).

## Follow-ups (nulls regenerate work; all verified ABSENT from queue)

1. **reinforced-head-excl-adj-drama** (P4): census reinforced heads + exclamatory NON-infinitive phrases in the drama corpus (the idx-4 "celle-ci, pleine de jeunes gens, de valets !" shape). Bar: if exclamatory adjectives/nouns pair freely with reinforced heads (≥3 genuine), the gap is infinitive-specific; if zero, exclamation itself resists the reinforced head.
2. **pour-inf-excl-topic-census-drama** (P4): census every governed exclamatory infinitive in the 14-play drama corpus with its topic/subject. Bar: if any takes a demonstrative topic (bare or reinforced), the pairing re-opens; confirmed zero (all 1st-person/modal subjects) hardens the head-licensing fence.
3. **redteam-reinforced-head-closure** (P2, gather-only, red-team venue): package grandparent (`reinforced-pour-inf-drama`) + parent (`reinforced-head-topology-drama`) + this battery as the closure input for the reinforced-head family docket. No battery decision requested.

## Bookkeeping

- Scripts: `code/crowd17/next-token/reinforced_head_topology_drama.py` (parent's, re-ran verbatim, 41/41 reproduced); `code/crowd17/next-token/reinforced_head_governed_topology_drama.py` (this battery: full-turn extraction + exclamatory audit + dash/paren extension; outputs `reinforced-head-governed-topology-drama_windows.json`).
- Raw windows: `code/crowd17/next-token/reinforced-head-governed-topology-drama_windows.json` (41 full-turn windows + machine flags; 0 dash/paren heads).
- Report: `code/crowd17/report_inbox/battery-reinforced-head-governed-topology-drama.md` (this file).
- battery-queue.json: `reinforced-head-governed-topology-drama` queued -> verdict/null via temp-file + rename (pre-write assert confirmed queued/verdictless; JSON re-validated post-write; own entry only; claim/bars/evidence/adverses preserved).
- Lock created on start (2026-10-09T17:33:07Z, agent 55fd5591-c94b-46da-8f86-c16b92aad357), deleted on completion. No stale lock existed.
- R5005, sealed gates, red-team queue untouched. Every number traces to the named corpus files or the scripts; no invented data.
