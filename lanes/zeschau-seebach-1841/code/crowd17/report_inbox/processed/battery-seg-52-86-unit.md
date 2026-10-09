# Battery report: seg-52-86-unit

- Target id: `seg-52-86-unit` (priority 3)
- Claim: rival re-segmentation — '52-86' as one infinitive (52 = prefix syllable) at @1738
- Date: 2026-10-09
- Worker: battery worker (subagent 3622b7e5-1dc1-4c7b-8366-4e917ca043cd)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; 1,847 pairs / 96 types re-derived in-session, asserts held). `canonical.py` never used. R5005, sealed gate instances, and the red-team adjudication queue untouched.

## Parentage

Follow-up F2 of the NULL `leftedge-52-86-1736` (2026-10-09): the 'ne [52] [86]' frame (x3: @1294/@1736/@1807) is locally coherent but 52 is unnameable at battery grade; F2 proposed the escape that '52-86' is ONE infinitive (52 = prefix syllable, 86 = stem), making @1736–1739 read '[60] ne [INF]' on a corpus-attested 'de ne [INF]' pattern.

## Bar (verbatim from battery-queue.json)

"parse @1736-1739 as '[60] ne [INF]' on the corpus-attested 'de ne [INF]' pattern (x7 in Misérables/Tocqueville) with stated word boundaries; else fence"

Restated as numbered pass/fail clauses (pre-registered before testing; F2's conjunction made explicit):

- **C1:** 60 takes 'de'/de-class value at @1735 (the pattern's left edge).
- **C2:** 52-86 parses as one infinitive (52 = prefix syllable, 86 = stem) with zero contradiction under standing values.
- **C3:** A9's class-level 86 INF-class grant survives (86 stays INF-class).
- **Verdict rule:** the unit reading holds iff C1 AND C2 AND C3; else kill the unit reading with the failing clause stated.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/seg-52-86-unit.lock` on start (agent id + 2026-10-09T10:45:26Z); no stale lock present.
2. Re-derived the repaired stream byte-exact per `repair_parse.py`; verified 1,847 pairs / 96 types.
3. Locus re-derived: 0b @1733–1745 = `30 06 60 | 12 48 52 86 | 12 34 94 82 46 56` (row a8_07). Target slice @1735–1739 = `60 12 48 52 86`; the bar's @1736–1739 = `12 48 52 86` = analytic 'ne' (12-48) + 52 + 86.
4. Adopted (never re-litigated): `leftedge-60-value` KILL (2026-10-09), `seg-52-80-unit` KILL (2026-10-09), `ne52inf-adverb` NULL (2026-10-09), `leftedge-52-86-1736` NULL (2026-10-09), `ni-1740-1742` KILL, A9 86 INF-class grant, §7 sole-polyvalence rule.
5. Bigram censuses and 52/86 profiles re-derived byte-exact in-session (numbers below are mine, not inherited).
6. Corpus spot-check of the parent's x7 'de ne [INF]' pattern against the lane's period texts.

## Window-level evidence (@-offsets, 0-based)

- **Locus:** @1735=`60`, @1736=`12`, @1737=`48`, @1738=`52`, @1739=`86`, @1740=`12`, @1741=`34`. Right edge is the fenced ni-1740-1742 debris (adopted).
- **Bigram census (byte-exact):** "12 48" x5 (@169/@709/@809/@1075/@1736); "48 52" x2 (@283/@1737); "60 12" x2 (@700/@1735); "86 12" x1 (@1739, hapax); "12 34" x1 (@1740, hapax); **"52 86" x1** (@1738, hapax).
- **52's profile (n=27):** 18 distinct predecessors, 16 distinct followers — free-word signature, anti-correlated with a bound prefix syllable.
- **86's profile (n=32):** pre=00 x12 (A9 "pour [86]" leg), fol=29 x4 (the "86er" stem leg), fol=12 x1. The A9 infinitive shape with byte support is stem-"86" + 29='er', not bare "86".
- **60's contradiction:** "60 03" x4 (the verb-stem successors from leftedge-60-value Leg B).

## Per-clause pass/fail

**C1 — FAIL at kill grade (adopted standing verdict).** `leftedge-60-value` (2026-10-09) KILLED the 'de' arm of F2 at @1736–1739's left edge at kill grade:
- Leg A: 06='ent' cannot stand or attach left, so 60 is word-internal under the standing ent-60 arm and cannot be free "de".
- Leg B: 60="de" as a uniform value is contradicted by the 03 x4 verb-stem successors ("60 03" x4 re-verified byte-exact in-session).
The 'de ne [INF]' pattern's left edge cannot be 'de'. C1 is forced false; the conjunction dies here.

**C2 — FAIL independently (two kill-grade legs, stated for the record).**
- (a) The unit reading needs 52 as a bound prefix syllable. 52 is a free word (n=27; 18 pre / 16 fol, re-derived). A group that is a free word at 27 windows cannot be a bound prefix at @1738 without §7-barred polyvalence (67 et/veut is the sole true polyvalence). The lane's "word-internal iff bound" standard forces the negative.
- (b) Under the claim's own terms (86 = stem), the unit "[52][86]" has no infinitive ending at @1739: 86 is followed by 12, not 29='er', and the only byte-supported infinitive shape for 86 is the A9 "86er" leg (fol=29 x4). A [prefix][stem] with no ending is not an infinitive. (The whole-infinitive-86 alternative has zero compositional evidence: no letter values exist for 52 or 86, and "52 86" is a hapax.)
- Zero repetition leverage anywhere: "52 86" x1 stream-wide.

**C3 — moot.** The conjunction already failed; A9's class-level grant is untouched by this verdict (no claim about 86's class is made or needed).

**Corpus note (evidence-level, not load-bearing):** the parent's x7 'de ne [lexical-INF]' pattern re-checked against the lane's period texts resolves mostly as restrictive "ne...que", not bare "de ne + INF": "de ne voir attaquer le traité que par", "de ne voir à Lyon qu'une lutte", "de ne faire l'acte de renonciation qu'i[l]", "de ne parler que pendant que", "de ne signaler que les points". The pattern premise was weaker than stated — but the verdict does not depend on it.

## Verdict: KILL (of the '52-86'-as-one-infinitive unit reading)

Failing clauses: **C1** (kill grade, adopted standing verdict) and independently **C2** (kill grade, free-word contradiction + missing ending). The window itself stays fenced under the parent's standing 'ne [52] [86]' frame (leftedge-52-86-1736 NULL: frame coherent, 52 unnameable). Per §4, kills regenerate no follow-ups.

## Adverses

- **"86 stem/whole caveat (A10 HOLD)"** — answered, not violated: this verdict makes no stem/whole claim about 86; A9's class-level grant survives intact. The caveat stands exactly as before.
- **"60's value open (no 'de' signal in its 18-window profile yet)"** — superseded and hardened: leftedge-60-value's KILL closed the 'de' arm at kill grade; it is not merely open.
- **"52-86 bigram x1"** — confirmed byte-exact; zero repetition leverage, consistent with the kill.

## Red-team consistency check

- No standing verdict contradicted or downgraded. `leftedge-60-value` KILL, `seg-52-80-unit` KILL, `ne52inf-adverb` NULL, `leftedge-52-86-1736` NULL, `ni-1740-1742` KILL all adopted as premises.
- §7 honored: no polyvalence declared; the unit reading's need for one is stated as part of the kill.
- Canonical-stream caveat stands (row a8_07 offset unvalidated).
- No red-team docket item touched.

## Supervisor observations (not findings; no follow-ups per §4)

1. The 'ne [52] [86]' frame's three instances (@1294/@1736/@1807) survive this kill untouched — the kill is scoped to the unit re-segmentation only.
2. The corpus re-check suggests future 'de ne [INF]' pattern claims should pre-filter "ne...que" restrictive hits before counting.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-seg-52-86-unit.md` (this file).
- Queue: `seg-52-86-unit` queued → verdict/kill via temp-file + rename (pre-write assert confirmed no prior verdict; JSON re-validated post-write; own entry only; no downgrade).
- Lock `locks/seg-52-86-unit.lock`: created on start, deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
