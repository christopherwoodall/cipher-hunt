# Battery report: compound-62-vient

**Target:** `compound-62-vient` (P2)
**Date:** 2026-10-09
**Verdict:** KILL (the prefix hypothesis)

## Bar (verbatim from queue)

"name the compound verb at all five windows with stated prefixes, or kill the prefix hypothesis"

## Bar restated as numbered clauses

1. At each of @11, @802, @945, @1136, @1324 ("62 98"), the bigram parses as ONE French word: a compound-venir verb, with 62 named as the prefix and 98 as the venir-family stem.
2. The five namings are mutually consistent (one prefix value for 62, or stated conditioning that does not violate §7).
3. If clause 1 or 2 fails, the prefix hypothesis is killed.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
(byte-exact tokenizer per `repair_parse.py`; asserts held: 1,847 pairs, 96 types).
`canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
Lock `locks/compound-62-vient.lock` created on start, deleted on completion.
Standing values used as premises only (§7): 98='vient' battery-PROMOTE
(finite semi-auxiliary, 3sg; battery-vient-98-name), 62='il' demonstrated-not-promoted
on 62-94 x9 (collision-62-84 kill), 06='ent' standalone word-initial
(ent-right-attach-sweep kill), 00='pour' (A9), 47='ce' (A4), 77='le' (provisional).

"62 98" occurs exactly 5x stream-wide (@11, @802, @945, @1136, @1324) — confirmed;
the five windows ARE the whole population. n(62)=35, n(98)=40.

## Window-level evidence

Finite 3sg compound-venir candidates: revient, devient, parvient, survient,
intervient, contrevient, convient, disconvient, prévient, advient, provient,
circonvient, subvient, souvient. (Infinitive compounds "revenir"-shaped are
fenced: 98='vient' is finite, and vient/venir alternation is a red-team act
per §7 — vient-98-name clause 4.) French finite verbs require an overt
subject (no pro-drop).

**@11 (a1_00):** `5:41 6:06 7:77 8:78 9:18 10:93 | 11:62 12:98 | 13:76 14:45 15:91 16:53 17:17 18:64`
Compound parse needs a subject left of 62. Immediate left 93 is class-open
(ratification candidate, unratified); 06='ent' stands alone word-initial;
77='le' provisional article needs a noun; 78/18 open. No subject licensable
under standing values. Rival: "[62=il] vient [76] ce … fois qui" — grammatical,
subject built in. C1 FAIL.

**@802 (a5_05):** `800:44 801:74 | 802:62 803:98 | 804:53 805:69 806:24`
Immediate left 74 is class-open (noun-74-census NULL — fenced, not nameable).
"44" is two groups back; "44 74 [compound]" would need 74 as the subject —
invents data. Rival: "il vient [53]" — clean. C1 FAIL.

**@945 (a5_10):** `939:37 940:01 941:07 942:50 943:40 944:08 | 945:62 946:98 | 947:96 948:86`
Immediate left 08 open; 37 predicative (A1), 01/07/50/40 open. No subject.
Rival: "[62] vient par [86-subst-inf]" via the A14 set-level grant (vient-98-name
read this window exactly so). C1 FAIL.

**@1136 (a6_08):** `1133:77 1134:86 1135:20 | 1136:62 1137:98 | 1138:00 1139:98`
Immediate left 20 (split with 17, open); 77='le' provisional; 86 INF-class.
No subject. Right edge "00 98" = "pour [98]" is the semi-auxiliary frame:
rival "il vient pour [venir]" parses; compound "revient pour [venir]" is
subjectless AND redundant. C1 FAIL.

**@1324 (a7_04):** `1318:15 1319:24 1320:03 1321:29 1322:80 1323:08 | 1324:62 1325:98 | 1326:56 1327:30`
24 is a finite modal whose complement slot is already filled by "03 29" =
"[03]er" (faire-complement-field census); 08 open. No subject for a compound
verb. Rival: "il vient [56] pas" — subject supplied. C1 FAIL.

Impersonal rescues ("advient que", "convient de/il convient") fail at all five:
no dummy "il" present and no "46=que"/"de"-complement in the required
positions (@11 right has no 46; @802/@945/@1136/@1324 likewise).

## Per-clause pass/fail

1. **FAIL (kill grade).** At all five windows the compound parse is
   ungrammatical under standing values: a finite compound verb with no
   licensable subject. French has no pro-drop; every candidate subject
   (93/@11, 74/@802, 08/@945, 20/@1136, 08/@1324) is class-open — naming one
   invents data.
2. **FAIL (independent).** No single French prefix yields a grammatical parse
   at all five windows (clause-1 failure is value-independent). Per-window
   prefixes would give 62 two or more distinct values at battery level —
   homophony, which is red-team venue per §7 (67 is the sole true polyvalence);
   and 62='il' is already demonstrated on the nine 62-94 windows, so a
   prefix value cannot extend beyond these five windows without a second
   62 value.
3. **FIRES.** The prefix hypothesis is killed.

## Cleaner rival (demonstrated on the same frames)

"[62=il] vient": vient-98-name (battery PROMOTE) read all five 62-98 windows
as "[62] vient"; 62='il' is demonstrated on 62-94 x9 (collision-62-84 kill).
The rival supplies the subject the compound parse lacks, and parses cleanly
at all five windows. Per protocol, a cleaner rival demonstrated on the same
frames independently supports the kill.

## Adverses

- "Does not name 62 globally; redteam-62-conditioned already queued":
  RESPECTED. This battery kills only the verb-prefix hypothesis at the five
  62-98 windows. 62's global/conditioned value ('il' demonstrated, règne/trône
  battery-narrowed, formula "venir"-tail syllable at @1065) stays with the
  red-team docket. No polyvalence declared; §7 intact.
- 98='vient' (battery-promoted) is adopted as premise, not re-litigated;
  vient-98-name's five "[62] vient" reads are cited, not duplicated.

## Verdict: KILL

62 is not a verb-prefix at the five "62 98" windows. "62 98" does not form a
compound-venir word at any of them; the two-word "[62=il] vient" reading
stands as the battery-grade parse. No standing or red-team verdict
contradicted or downgraded.

No follow-ups required (kill, not null).

## Bookkeeping

- Lock `code/crowd17/next-token/locks/compound-62-vient.lock` created on start,
  deleted on completion.
- `battery-queue.json`: `compound-62-vient` queued -> verdict/kill
  (temp-file + rename; pre-write assert confirmed no prior verdict).
- R5005, sealed gate instances, red-team adjudication queue untouched.
