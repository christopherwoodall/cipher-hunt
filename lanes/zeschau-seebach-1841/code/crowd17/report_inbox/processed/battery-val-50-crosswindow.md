# Battery report: val-50-crosswindow — systematic value search for 50 across its 11 windows (NULL — value underdetermined, open class)

- Target id: `val-50-crosswindow`
- Claim: systematic value search for 50 across its 11 windows; the "la"+50 pair (@380/@1264) and "[71] 50 er" (@1565) are the sharpest constraints
- Date: 2026-10-09
- Worker: battery worker (subagent 3bd9903d-2f07-42cb-aca9-ea0233108a0f)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session). `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Parent: battery-frameA-50-value.md NULL 2026-10-09 (follow-up 1). Adopted, not re-litigated: the "ent ent" two-word reading is kill-grade dead; 50="ver" dead ("50-40"="vere" non-word at @942); the "ent"+X French-word enumeration found an empty intersection with the "la"+X windows.

Terms (ASD-STE100): "open class" = more than one French value fits every window, so the evidence cannot choose one. "Unstated assumption" = a premise with no lane license (granted/promoted/battery-grade) behind it.

## Bar (verbatim, pre-registered before testing)

"name 50 value iff one value parses all 11 windows with <=1 unstated assumption"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** exactly one French value parses all 11 of 50's windows → name it (PROMOTE).
2. **C2:** the naming uses ≤1 unstated assumption across the 11 windows.
3. **C3 (else-arm):** if zero values parse, or more than one value parses, → NULL (fence: 50's value stays open).

Adverses listed: none.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/val-50-crosswindow.lock` on start (agent id + 2026-10-09T18:52:00Z); no prior/stale lock; deleted on completion.
2. Re-derived the repaired stream byte-exact in-session (1,847 pairs / 96 types asserted).
3. Censused all 50 windows (n(50)=11, 0-based): @209, @331, @380, @442, @582, @662, @696, @942, @1264, @1565, @1813.
4. Standing values used as premises: pencil 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que; granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout (A5), 00=pour (A9), 84=on (A15), 47=ce (A4); conditional promote 06=ent (R17-007); LEAD 94=ne, 98=vient, 78=ver; battery 08=t; provisional 77=le, 59=est; kills: 50=ver, 48=est/ne/de.
5. 1841 diplomatic French throughout.

## Window-level evidence (0-based pair indices, ±3 context)

| # | @ | window | standing-value read |
|---|---|--------|---------------------|
| W1 | 209 | `06 77 44 50 88 19 74` | "ent le(?) [44] [50] [88]…" |
| W2 | 331 | `19 00 92 50 45 54 88` | "[19] pour [92] [50] ce [54]…" |
| W3 | 380 | `48 00 11 50 82 16 52` | "[48] pour la [50] m [16] [52]" |
| W4 | 442 | `43 98 80 50 78 41 10` | "[43] vient [80] [50] ver [41]…" |
| W5 | 582 | `82 06 06 50 10 19 18` | "m ent ent [50] [10]…" (frame-A locus) |
| W6 | 662 | `16 00 86 50 80 03 62` | "[16] pour [86] [50] [80]…" |
| W7 | 696 | `74 46 02 50 45 28 94` | "[74] que [02] [50] ce [28] ne" |
| W8 | 942 | `37 01 07 50 40 08 62` | "[37] [01] [07] [50] et [62]" (40=e, 08=t → "et") |
| W9 | 1264 | `01 09 11 50 46 69 88` | "[01] [09] la [50] que [69]…" |
| W10 | 1565 | `06 60 71 50 29 24 74` | "ent [60] [71] [50]er [24]…" ([50]+"er" infinitive) |
| W11 | 1813 | `61 15 93 50 42 06 29` | "[61] [15] [93] [50] [42] ent er" |

## Candidate enumeration

The three sharpest windows jointly force the candidate shape:

- W3/W9 ("pour la [50] m…", "la [50] que"): [50] is a feminine noun (or noun-capable word) after "la".
- W10 ("[71] [50]er"): [50] is a verb stem taking spelled -er infinitive (29=er GT).
- W8 ("[07] [50] et"): [50] is a standalone word before "et" (adopts the "40 08"="et" reading; the rival "[50]e"+"t[62]" reading is noted but the "et" reading uses two licensed values and no extra assumption).

Intersection: feminine nouns that are also -er verb stems. This is an **open class**, all members fitting W3/W8/W9/W10 identically:

tente/tenter, tonne/tonner, porte/porter, donne/donner, danse/danser, garde/garder,
demande/demander, pensée/penser, marche/marcher, montre/montrer, rencontre/rencontrer,
mesure/mesurer, figure/figurer, forme/former, force/forcer, reste/rester, chante/chanter, …

Per-window check (representative "tente"; "porte"/"donne"/"danse" verified identical):

- W1 "ent le [44] tente [88]": "tente" as 3sg verb ("[44] tente") — licensed; [88] split-shaped, no clash. Same for every candidate (all are 3sg -er verbs).
- W2 "pour [92] tente ce": "tente" as fem noun after unknown [92] — licensed if [92] is determiner-shaped. Same for all.
- W3 "pour la tente m'[16]": licensed ("la tente"). Same for all.
- W4 "[43] vient [80] tente ver…": "tente" as noun appositive after [80] — weak but unrefuted for every candidate equally.
- W5: PROBLEM (see below) — identical for every candidate.
- W6 "pour [86] tente [80]": "tente" appositive after 86-noun — weak, unrefuted, identical for all.
- W7 "que [02] tente ce": "tente" 3sg subjunctive — licensed. Same for all.
- W8 "[07] tente et [62]": clean. Same for all.
- W9 "la tente que [69]": clean ("la tente que" + relative). Same for all.
- W10 "[71] tenter [24]": clean infinitive. Same for all.
- W11 "[93] tente [42] ent er": "tente" before 42-predicative — weak, unrefuted, identical for all.

**No window discriminates among the candidates at battery grade.** W1/W4/W6/W11 are weak-but-unrefuted for the whole class; W2/W7 admit the whole class via the verb/noun arms.

## W5 (@582) — the locus problem, identical for all candidates

"82 06 06 50" = "m"+"ent"+"ent"+[50]. The parent battery exhaustively showed no "ent"+X is a French word for any profile-compatible X ("enttente", "enttonne", "entporte", … all non-words). The bytes alternatively read "94 82 06 06" = "ne"+"mentent" ("they do not lie") with [50] starting the next word — but "ne mentent" needs a 3pl subject, and none is overt in "…45 13 55 61". That reading is the queued `mentent-580-rival`'s bar, not this battery's. For THIS battery, every candidate pays the same price at W5: **1 unstated assumption** (either a subject for "ne mentent", or an unlicensed "ent"+X boundary). The assumption budget (C2) is therefore satisfiable — but it does not discriminate either.

## Sharpest lead recorded (not named)

"même" fits W3/W9 idiomatically — "pour la même m'[16]", "la même que [69]" — better than any stem candidate. But "même" is **kill-grade dead as a uniform value**: W10 needs "[71] même er" = "mêmer", a non-word (no rescue via 71+50 composition: "71 50" = "[71] même" still leaves "même"+"er" adjacent). The W3/W9-vs-W10 tension is the classic split shape (cf. 52/97/09 battery splits): word-"même" at the "la" windows vs verb-stem at the "Xer" window. Declaring it would be a second polyvalence-class claim under §7 — red-team venue, not a battery act. Recorded as the strongest lead, escalated not declared.

## Per-clause pass/fail

- **C1 — FAIL.** Not zero values parse — an open class parses (tente, porte, donne, danse, garde, …). Exactly-one-value does not hold, so no value can be named.
- **C2 — PASS (conditional).** Every surviving candidate needs exactly 1 unstated assumption (the W5 locus), within budget — but C2 cannot rescue C1's uniqueness failure.
- **C3 — FIRES.** → NULL (fence).

## Verdict: NULL (fence — value underdetermined, open class)

50's value cannot be named at battery grade: the profile admits an open class of feminine-noun/-er-stem values with no discriminating window. The "même" lead at W3/W9 is real but incompatible with W10 as a uniform value (split-shaped → §7 red-team venue). No standing/red-team verdict contradicted or downgraded; §7 intact; 50="ver" kill stands.

## Scope

- This fence covers the uniform-value question only. It does not touch the queued `mentent-580-rival` (W5 subject bar), the queued `la-50-frames` (W3/W9 frame resolution), or the parent's "ent…"-word lock.
- Canonical-stream caveat stands (rows unvalidated except a5_03).

## Follow-ups proposed (all verified ABSENT from battery-queue.json; `mentent-580-rival` and `la-50-frames` already queued — not re-proposed)

1. `val-50-209-discrim` (P3) — resolve the "le [44] [50]" frame at @209: if 44's class/value lands, the verb-vs-noun reading of 50 there may discriminate within the open class (verb arm favors frequent verbs like porter/donner; noun arm favors "le [44-adj] [50-noun]").
2. `split-50-meme-stem` (P3) — test the split shape directly: "même"-word at W3/W9 vs verb-stem at W10, with the §7 venue question packaged for red-team if the shape confirms (cf. the 52/97/09 battery splits).
3. `val-50-corpus-laXer` (P4) — corpus census: among the open-class candidates, which co-occur in "la X … Xer" collocation frames in 1841 diplomatic French; narrows by usage, not by grammar.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-50-crosswindow.md` (this file).
- `battery-queue.json`: `val-50-crosswindow` queued → verdict/null via temp-file + rename; pre-write assert confirmed `queued`/verdictless; post-write JSON re-validated; own entry only; no downgrade.
- Lock `locks/val-50-crosswindow.lock`: created on start, deleted on completion (verified gone).
- `canonical.py` never used; R5005, sealed gate instances, red-team adjudication queue untouched.
