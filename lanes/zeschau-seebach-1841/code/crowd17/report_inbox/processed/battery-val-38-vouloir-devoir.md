# Battery report: val-38-vouloir-devoir

- Target id: `val-38-vouloir-devoir` (P3)
- Claim: "Discriminate \"vouloir\" vs \"devoir\" at battery grade: name iff a 38 window (or 65 value once named, fixing @1113 \"cela\" as wanted vs owed) forces volition-only or obligation/owe-only; \"vouloir\" takes \"que\"+subjunctive, \"devoir\"-modal takes bare infinitive — a \"38 46\"-family window would discriminate"
- Date: 2026-10-09
- Worker: battery worker (subagent 1f158f8a-2073-422e-97d4-be123e49a2bb)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session). `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

Terms (ASD-STE100): "discriminator window" = a 38 window where one of the two candidates is grammatically or semantically forced and the other is excluded at battery grade. "Owe sense" = "devoir" meaning "to owe" ("il doit cela" = "he owes that"), as distinct from modal "devoir" ("must").

## Bar (verbatim, pre-registered before testing)

"name iff a discriminator window forces one"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** A discriminator window forces "vouloir" (volition-only) at battery grade → name "vouloir".
2. **C2:** A discriminator window forces "devoir" (obligation/owe-only) at battery grade → name "devoir".
3. **C3 (else-arm):** If no window forces one → NULL with 1–3 follow-ups (§4).

Adverses listed: none (parent `val-38-verb` NULL, 2026-10-09, adopted).

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/val-38-vouloir-devoir.lock` on start (agent id + 2026-10-09T18:26:30Z); no prior/stale lock.
2. Adopted (never re-litigated) from parent `val-38-verb` (NULL, today): 38 = verb-form uniform; the candidate set is {"vouloir" (veut/voulu), "devoir" (doit/dû)}; @1113 finite-3sg ("[65] [V] pas cela"), @826 pp ("c'est [pp]", conditional on provisional 59='est'), @1469 modal + bare infinitive, @1650 governor ("veut me voir"-shaped); W1/W4/W7 fenced for both classes; 23~26 SPLIT, §7 intact.
3. Census of all 7 38 windows, byte-exact (0-based offsets): @384, @826, @1113, @1343, @1469, @1650, @1828.
4. Discriminator tests applied to each window: (a) "38 46"-family ("vouloir" + "que" signature; 46="que" granted ground truth); (b) 65's value fixing "cela" as wanted vs owed @1113; (c) selectional/complement frames excluding one candidate.

## Window-level evidence (byte-exact)

- **@384 (a2_07):** `11 50 82 16 52 38 37 43 91 36 62` — W1 indeterminate (52 split-shaped, dead as verb); no complement frame present for either candidate. No discrimination.
- **@826 (a5_06):** `95 13 24 87 59 38 82 01 24 87 11` = "[24] ce est [38-pp] m [01] [24]" — "c'est voulu" and "c'est dû" both grammatical and natural. No discrimination.
- **@1113 (a6_07):** `00 66 73 41 65 38 30 69 11 88 70` = "[73] qui [65-N] [38-V-3sg] pas cela [88-V]" — "ne veut pas cela" (volition) vs "ne doit pas cela" (owe). The bar's own mechanism ("65's value once named") is still armed: 65's value is NOT named (sel-65-1745-pressure NULL today: 65 animate-compatible, value open). "Cela" as wanted vs owed remains unresolved. No discrimination.
- **@1343 (a7_05):** `60 08 65 64 52 38 47 86 66 73 34` — W4 fenced for both classes per parent; adopted. No discrimination.
- **@1469 (a7_09):** `62 48 21 02 62 38 26 12 41 53 60` = "[62] [38-modal] [26-inf]" — modal + bare infinitive: "doit [inf]" ✓ AND "veut [inf]" ✓ ("vouloir" takes bare infinitive as freely as "devoir"-modal). No discrimination.
- **@1650 (a8_04):** `03 64 31 10 03 38 82 16 01 56 37` = "[03] [38-V-fin] me [16-inf]" — "veut me voir"-shaped ✓; "doit me [inf]" ("il doit me voir" = "he must see me") ✓. No discrimination.
- **@1828 (a8_11):** `97 00 86 29 82 38 83 24 82 16 59` — W7 fenced for both classes per parent; adopted. No discrimination.

## The "38 46" census (the parent's named discriminator)

- n(46) = 29 stream-wide (46="que" ground truth). In all 7 38 windows, **zero** occurrences of 46 within +1..+4 pairs after 38.
- 38's actual follower census (+1..+3): {82×3, 01×2, 24×2, 37, 43, 91, 30, 69, 11, 47, 86, 66 ×1} — no 46 anywhere.
- The "veut que"-shaped window the parent hoped for does not exist on the stream. However: this absence is NOT a discriminator against "vouloir" — "vouloir" takes bare infinitives as freely as "que"-clauses, so a "que"-less 38 is fully compatible with "vouloir". It removes the parent's best hoped-for pro-vouloir leg; it does not kill "vouloir".

## Per-clause pass/fail

- **C1 — FAIL.** No window forces volition-only. The strongest pro-vouloir arm ("38 46" "que"+subjunctive signature) is absent; the remaining windows (@1113, @1650, @1469) all admit "devoir".
- **C2 — FAIL.** No window forces obligation/owe-only. @1113's owe reading is conditional on the still-unnamed 65 value; @1469's modal reading admits "vouloir".
- **C3 — FIRES.** No discriminator window found → NULL.

## Scope (stated, not hidden)

- The parent's 2-way tie {"vouloir", "devoir"} stands unbroken. The "vouloir" parsimony edge (uniform volition sense) noted by the parent is not upgraded — parsimony is not battery grade.
- No window forces the pair false; no kill of either candidate. The uniform verb-form PROMOTE (noun26-38-profile) stands.
- If "vouloir" is eventually named, the 38/67 "veut" surface-sharing implication needs red-team §7 adjudication (parent caveat 1, homophone-38-67-veut already queued).
- Caveats carried: @826 conditional on provisional 59='est'; @1113 conditional on battery-promoted 30='pas'; 65's value unnamed; canonical-stream caveat (68/70 offsets unvalidated).

## Verdict: NULL (tie unbroken — no discriminator window)

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `vouloir-devoir-rearm-65` (P3, gated on 65's value being named) — re-run this target's bars once 65's value lands: "cela" @1113 resolves to wanted vs owed; owe-sense forces "devoir", volition-sense forces "vouloir". This is the bar's own re-arm mechanism.
2. `val-38-que-signature-widen` (P4) — widen the "38 46" search to non-adjacent 46 (intervening clitics/adverbs, longer clause spans); if the zero holds, record the vouloir-"que"-signature absence as stated-weight lean, never as a discriminator.
3. `val-38-corpus-modal-owe` (P4) — corpus check in 1841 diplomatic French: is "devoir" in the owe sense with a "cela"-shaped object attested, and do "vouloir"/"devoir"-modal with "me + inf" show any selectional difference? Corpus arms for the tie.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-38-vouloir-devoir.md` (this file).
- Queue: `val-38-vouloir-devoir` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/val-38-vouloir-devoir.lock` created on start, deleted on completion (verified below).
- R5005, sealed gates, red-team adjudication queue untouched. No standing/red-team verdict contradicted; §7 intact.
