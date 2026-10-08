# Next-token findings: followers of 40="e"

Beat: all 21 windows of 40="e" in the repaired 1,847-pair stream. 40 is rare
(21×) — nearly every window is a word-final "e", so followers are word-boundary
onsets: the next word's first syllable. High value per window.

Dominant pre-pattern: 29-40 ("er-e" → "-ère") ×9 — feminine "-ière/-ère" words
(première, manière, lumière, dernière…).

## Ranked predictions

**P1 (HIGH). "e 65 94" ×2 — exclusive two-leg constraint.**
Byte-identical bigram after 40 at @686 and @1711, occurring NOWHERE else in the
stream (65-94 total = 2, both post-40). Both windows have 29-40 ("-ère") before:
"…ère 65 94…" ×2, two independent windows, same two groups. A fixed collocation
after feminine "-ère" nouns. French hypotheses (not verdicts): "manière
[dont/de] [94]", "lumière [sur/de] [94]". 65 is separately interesting: "65 qui"
×3, "21 65" ×4, 25 total.
Testable: profile 65 fully (esp. "65 64=qui" ×3 — what single group precedes
"qui" three times?); test 65-94 as a fixed phrase; check 94's subject behavior
(see P2).

**P2 (HIGH). "20 62 94" ×3 — formula; "la première 20" ≠ fois.**
"20 62" ×4 (@760, @839, @1135, @1703); "20 62 94" ×3 (@760, @839, @1703).
@760 = "la première [20] [62] [94] [59=est]" — "la première [20-62-94] est…".
Since 20="fois" is KILLED and 20~17 SPLIT, "la première 20" needs a feminine
singular noun ≠ fois: partie, occasion, année, place, moitié (per the census).
"62 94" ×9 overall is a near-fixed pair, and "62 94 59" shows 62-94 as a
subject before "est". Further: 62 is ALSO the top prev of 48 (×6) — 62 selects
BOTH members of the ne-distributed {48,94} class pair. 62 is a high-value
unknown: "de"? "des"? Testable: 62's contact profile vs {48,94}; "62 94" ×9
frame battery; 20's feminine-noun frames (the paradox's noun leg).

**P3 (HIGH). "67 77 81" ×4 — formula-grade; frame favors 67="et".**
After 40: @1239, @1400 ("…e [67] [77=le] [81]…" ×2, byte-identical trigram).
Stream-wide: 4× (@743, @1239, @1400, @1597) with varied prev {30, 80, 03, 48}
and next {85, 82, 92, 98} — independent of 40, a genuine formula:
"et/veut le [81]" ×4. 81="prin" is KILLED → 81 returns to NULL; "et le [81]"
needs 81 = noun. The et/veut fork is the lane's sole true polyvalence, but in
THIS frame 4/4 windows read naturally as "et le [noun]" while "veut le [noun]"
×4 is strained (no subject, no complement structure). Frame-conditioned
evidence for 67="et" here — not a global resolution.
Testable: 81 noun-profile battery; check @743/@1597 for veut-incompatible
subjects.

**P4 (MEDIUM-HIGH). 08 — top battery target from this beat.**
18 total. "08 31" ×3 (@881, @1488, @1520; 31=VERBAL) — 08 directly before finite
verbs. "et/veut 08" ×2 (@631, @1520). "…e 08" ×2 (@922, @944 — this beat's
cluster). @60: "08 34 29 40" = "[08]ière" — 08 as spelling letter before
"-ière"! Candidates: "ne" ("et ne [verb]", "…e ne [verb]"), "se" ("et se
[verb]"), "on" ("et on [verb]" — @1520 reads cleanly), or a spelling letter
("n" → "…nière"). The "08-ière" window pulls toward spelling-letter; the three
"08 [verb]" windows pull toward ne/se/on. Do NOT force — this needs a real
battery: 08's full contact profile, "08 31" verbal-frame test, "et 08"
disambiguation.

**P5 (MEDIUM). 65 dominates the "-ère" follower set.**
After 29-40 ×9, followers = {12, 65×3, 56, 03, 20, 29, 17}. 65 is 3/9 — the
only repeat. Combined with P1 (65-94 exclusive) and 65's own profile ("65 qui"
×3, "21 65" ×4), 65 is the single highest-value unknown to profile next.

**P6 (MEDIUM, weak). @1557: "61-40 17-11-26" = "…e fois la [26]".**
"61-40" occurs only here. Feminine "-e" word + "fois" + "la": "une/cette/
nouvelle/dernière fois, la [26]"? If the cipher splits "une" as "un"+"e",
61="un"-stem. Singleton — hypothesis only. Testable: 61's distribution
(18 total; note "61 59=est" ×2 at @447, @1510 — 61 as subject before "est").

**P7 (FLAG). @848: 96-40 — "par e", anomalous.**
Only "96-40" bigram in the stream. 96="par" is promoted; 40="e" after it has no
clean reading. Full window: "33=INF 96 40 62 21 67" = "[infinitive] par e
[62][21] et/veut". Weak hypothesis: "finir par être"-shaped ("par"+"être" =
96-40-62-21?). Flag for red team: does "33 96 40" recur anywhere? Is 96's
"par" reading strained here (cf. the "parle" strain note)?

## Confirmations / nulls
- @1039 = "la première fois, le m…" (70 82 34 29 40 17 77 82): flagship
  confirmation of 17="fois" in place. Already banked; no action.
- @335 "…e 03 qui [31=VERBAL]": supports 31=VERBAL, adds nothing new. Null.
- @752 "…e et/veut la pre[70]…": "…e et/veut la pre[mière/preuve]" — weak,
  recorded only.
- @921/@943 "…e 08 [65/62]": folded into P4.

## Battery priority from this beat
1. 65 full profile (P1+P5: "e 65 94"×2 exclusive, "-ère" top follower, "65 qui"×3).
2. "20 62 94"×3 frame + 62 as {48,94}-selector (P2).
3. "67 77 81"×4 et-frame + 81 noun profile (P3).
4. 08 disambiguation: ne/se/on vs spelling-letter (P4).
5. P7 anomaly review (red team): "33 96 40" @848.
