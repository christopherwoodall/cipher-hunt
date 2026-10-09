# Battery verdict: frame-42-94-leftward

**Target:** `frame-42-94-leftward` (P3)
**Date:** 2026-10-09
**Worker:** battery worker (subagent 04a177d0-4691-447a-b349-54c33278b884)
**Claim:** Test '42 94' as leftward composition "[42]ne" (word-final 'ne' syllable).
**Stream:** repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847 pairs / 96 types held). `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

## Bar (verbatim from battery-queue.json)

"promote iff \"[42ne]\" takes ONE stated word-class parsing all three windows ('[42ne] [59=est] [37]' @1794, '[42ne] [02] tout [88]...' @493, '[42ne] [74] [65] on...' @786) with the X-slots resolved or fenced; kill iff it contradicts R17-001's 'n\\'est' legs (@558 '86 94 59 30', @762 '62 94 59 39') or requires §7 polyvalence on 94 (escalate to the red team; a battery declares no polyvalence)"

## Numbered clauses (restated before testing; not modified after)

1. **C1 (promote):** "[42ne]" takes ONE stated word-class parsing all three windows — W3 (@1794: '[42ne] [59=est] [37]'), W1 (@493: '[42ne] [02] tout [88]...'), W2 (@786: '[42ne] [74] [65] on...') — with the X-slots resolved or fenced.
2. **C2 (kill):** the composition contradicts R17-001's 'n'est' legs (@558 '86 94 59 30', @762 '62 94 59 39') — kill-grade contradiction — OR requires §7 polyvalence on 94 (escalate; a battery declares no polyvalence).
3. **C3 (else):** if neither C1 nor C2 fires, the verdict is NULL with 1–3 follow-ups per §4.

## Method

1. Read BATTERY-PROTOCOL.md first; created `locks/frame-42-94-leftward.lock` on start (2026-10-09T08:52:14Z), no prior lockfile present.
2. Re-derived the repaired stream in-session (asserts held).
3. Byte-verified the '42 94' census: exactly x3. 0-based indices of the bigram: W1 = 42@493/94@494 (row a2_11), W2 = 42@784/94@785 (row a5_04), W3 = 42@1794/94@1795 (row a8_09). (Queue's '@493/@786' mix 42-index and 94-index conventions; my indices are the 42-index, 0-based, byte-verified.)
4. Adopted (not re-litigated): R17-001 (94='ne' STRONG LEAD); seg-62-94-wordfinal KILL (x9 word-claim dead); seg-62-94-wordless6 PROMOTE (word-final-'ne' scoped to the 6 D3-un-attachable 62-94 windows, 4/6 noun-class, segmentation not value); ne-94-right-context census; ne-24-profile (24 = finite-modal, battery-promoted); 59='est' provisional (est-59-frame-census KILL of the 80% harden — 74.1% copular, stays provisional); 37/32/42 predicative frames granted (A1); 79="tout" (A5); R17-018 (94 duality, red-team venue); 67 positional rule.

## Window-level evidence (all 0-based)

### W3: 42@1794, 94@1795, row a8_09
`1790:56 [42 94] 1796:59(est,prov) 1797:37(pred,A1) 1798:91`
- [42ne]-as-noun: "X est [37-pred]" — noun subject of copula, clean under provisional 59='est' and granted A1. ("la sienne est [belle]"-shaped; 42's value stays open.)
- Cost: displaces ne-94-right-context's CONDITIONAL 'ne est' leg at this window. That leg was conditional on provisional 59='est' and never kill-grade; est-59-frame-census (74.1% < 80%) keeps it conditional. Low-cost trade, not a kill-grade loss.
- X-slots: resolved (59 provisional-stated, 37 granted A1).

### W1: 42@493, 94@494, row a2_11
`490:67(et?/veut) 491:78 [42 94] 495:02 496:79(tout,A5) 497:88 498:47`
- [42ne]-as-noun: "[78] [noun] [02] tout [88]..." — 78's class is open (78+45='verdict' killed; no class standing). If 78 is determiner/adjective, "[det] [noun]" is clean; if 78 is noun, noun+noun is dead. 02's value is open. → X-slots 78/02 are FENCED with cause (class-open), not resolved.
- Verb/adjective/adverb/pronoun: no French verb or adjective ends in "-ne" as one word; adverb has no slot here; possessive-pronoun (mienne/sienne) needs invented 42 value. → noun is the only live class.

### W2: 42@784, 94@785, row a5_04
`782:24 [42 94] 786:74 787:65 788:84(on,A15) 789:06`
- [42ne]-as-noun under STANDING values: 24 is finite-modal (ne-24-profile, battery-promoted). Modal + noun = ungrammatical ("doit [noun]"). Modal + infinitive is impossible for a "-ne"-final word (no French infinitive ends in "-ne"). → noun FAILS under standing values.
- [42ne]-as-noun under DOCKETED 24='en': "en [42ne] [74]..." — preposition + noun parses formally, conditional on the unresolved 24 red-team docket (24-en-verb-conflict). → live ONLY under the docket.
- No other class: verb impossible (no "-ne" verb form); adjective/adverb unlicensed at this slot.

## Per-clause pass/fail

1. **C1: FAIL.** Noun is the only live class, but it does NOT parse all three windows under standing values: W3 parses clean, W1 parses only with 78/02 X-slots fenced, and W2 actively fails (modal + noun ungrammatical) — its only escape is the docketed 24='en' arm. "With the X-slots resolved or fenced" cannot fence W2's 24 slot: modal-noun is a kill-grade contradiction, not an open value. A docketed conditional is not a battery promote.
2. **C2: FAIL (does not fire).**
   - Leg (a): no kill-grade contradiction of R17-001's 'n'est' legs. @558 ('86 94 59 30') and @762 ('62 94 59 39') are different windows; [42ne] touches neither. @762 is anyway already word-final-'ne' per wordless6. The only cost is the CONDITIONAL 'ne est' leg at W3 itself (@1795), which was never kill-grade (est-59-frame-census: 59='est' stays provisional at 74.1%).
   - Leg (b): no §7 polyvalence is declared. Per the wordless6 precedent (battery-promoted, scoped), word-final-'ne' is SEGMENTATION, not a value claim — "No §7 polyvalence declared (segmentation, not value)"; R17-001 stays 'ne' as syllable; the duality declaration belongs to R17-018 (red-team venue). The compositional reading is fenced to that escalation, not promoted.
3. **C3 fires → NULL.**

## Verdict: NULL

The [42ne] composition is a live conditioned hypothesis (noun-class: clean at W3, fenced-X-slot at W1) but it is docket-gated at W2 (needs 24='en') and cannot be promoted under standing values. Nothing is killed: no 'n'est' leg is contradicted, and no polyvalence is declared (segmentation framing per wordless6; R17-018 owns the duality).

## Follow-ups (for supervisor queuing; all verified absent from battery-queue.json)

1. **w2-42-94-24en-gate** (P3) — re-test W2's "[42ne] as noun" under the docketed 24='en' arm once the 24 red-team docket (24-en-verb-conflict) resolves; if 24 resolves modal, the noun-[42ne] promote is dead at W2.
2. **val-42-ne-noun** (P3) — search 42's n=20 windows for a noun value compatible with a -ne-final French word (peine/haine/donne-family); kill [42ne]-noun if no compatible value exists.
3. **poly-94-r17018-input** (P2) — package the [42ne]/[62ne] word-final-'ne' segmentation family (wordless6 + this report) as ruling-ready input for the R17-018 red-team docket; no battery-level duality declaration.

## Adverses

"Deciding it implicates 94's function and is §7-adjacent; a battery declares no polyvalence." — ANSWERED. No polyvalence is declared: [42ne] is framed as segmentation (94 stays 'ne' as syllable, per the wordless6 precedent); the duality question is escalated to the R17-018 red-team docket. No §7 rule is breached at battery grade.

## Standing verdicts (checked, none downgraded)

- R17-001 (94='ne' STRONG LEAD): untouched (segmentation framing).
- R17-018 (94 duality): escalation venue — untouched, not pre-empted.
- seg-62-94-wordfinal KILL / wordless6 PROMOTE: upheld; [42ne] is outside wordless6's 6-window scope; no scope re-claim made.
- ne-94-right-context: its conditional @1795 'ne est' leg is displaced by the W3 composition — recorded as a battery-level trade (conditional leg, never kill-grade), not a downgrade.
- est-59-frame-census (59='est' provisional, 74.1%): used as premise; W3's cleanliness is load-bearing on it — stated.
- ne-24-profile (24 = finite-modal): used as premise; W2's failure is scoped to standing values.

## Canonicality caveat

Rows a2_11, a5_04, a8_09 carry unvalidated upstream offsets; all three '42 94' windows are canonical-offset objects per protocol.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/frame-42-94-leftward.lock` created on start (2026-10-09T08:52:14Z), no prior lockfile; deleted on completion (verified gone).
- `battery-queue.json`: `frame-42-94-leftward` status `queued` -> `verdict`, `verdict: {"result": "null", "report": "code/crowd17/report_inbox/battery-frame-42-94-leftward.md", "date": "2026-10-09"}` (temp-file + rename; pre-write assert confirmed queued/verdictless — no downgrade; JSON re-validated; only this entry touched).
- R5005, sealed gates, red-team adjudication queue untouched. No invented numbers: every @-offset traces to the repaired stream re-derived in-session.
