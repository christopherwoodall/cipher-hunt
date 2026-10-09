# Battery report: x29-80-1596-nominal

- Target id: `x29-80-1596-nominal`
- Claim: "@1596 '80' closes as nominal object via 81's class ('[03]er [80] et le [81]')"
- Date: 2026-10-09
- Worker: battery worker (session 769e1c3a)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py). n(81)=14, n(80)=17 re-derived in-session.
  `canonical.py` never used. R5005 not touched. Sealed gates and red-team adjudication queue untouched.
- Lock: code/crowd17/next-token/locks/x29-80-1596-nominal.lock (created at start, deleted on completion; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"name 81's class from its windows and show @1594-1597 parsing as '[03]er [80-nominal] et le [81]' with <=1 ungranted assumption; else fence"

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1) 81's class is named from its stream windows (with the standing battery promote adopted as an explicitly stated premise, corroborated on the repaired stream).
2. (C2) @1594-1597 (extending to @1599 for the full claimed parse) parses as '[03]er [80-nominal] et le [81]' with <=1 ungranted assumption. An ungranted assumption = any value, class, boundary, or re-segmentation not in the banked/granted/promoted/provisional set. The parse must also be grammatical 1841 French.
3. (C3) Adverses answered: imperative and determiner readings of 80 stay excluded (not re-litigated, not revived).

## Window (re-derived, 0-based @-offsets)

@1590-1602 (row a8_02): `29 47 08 81 03 29 80 67 77 81 82 98 00`
Target span @1594-1599: `03 29 80 67 77 81` = "[03]er [80] et(67) le(77) [81]".

67="et" by the §7 positional rule (follower 77='le' provisional is not infinitive-shaped — firm). 29="er" banked. 77="le" provisional. 82='m' banked letter.

## 81's class (C1)

81 census, n=14: @26, 44, 93, 524, 551, 745, 1086, 1095, 1241, 1402, 1513, 1593, 1599, 1672.

- "77 81" x3 (@745, @1241, @1402): "le [81]" under provisional 77='le' — article-adjacent nominal slot. @1241/@1402 byte-identical ("40 67 77 81 87 11 00").
- "55 81" x5 (@26, @524, @551, @1086, @1095): 55 is "ver"-shaped (45-78 "ver" family lead; "11 78 55 81" @1672 = "la ver [55 81]").
- @44 "43 81 30": "[43] [81] pas(30)" — nominal subject position before the promoted negation cell (30='pas' battery-promote).
- @1599 "67 77 81": "et le [81]" — the claimed window's own tail.

C1: PASS. 81 = noun class. Adopted premise: battery-promote noun-81 (2026-10-09, "masculine abstract noun class"), corroborated on the stream by the article-adjacent and subject-position frames above. No re-litigation of the promote; used as stated battery-grade premise.

## The nominal-80 parse (C2)

Assumption budget under standing values:
- "03 29" = "[03]er" infinitive: 29="er" banked; 03 verb-stem class is a standing battery promote — stated premise, 0 ungranted.
- 67="et": §7 positional rule — granted, 0 ungranted.
- 77="le": provisional — standing, 0 ungranted.
- 81 noun-class: battery-premise — stated, 0 ungranted.
- 80 = nominal at this locus: A8 grants 80 verb-frames only; no nominal shape for 80 is granted anywhere. = 1 ungranted assumption.

The budget has exactly 1 spent so far. But the parse must also be grammatical 1841 French, and here it breaks:

- Reading (a), NP-coordination: "[Vinf] [80] et [le 81]" — the infinitive "[03]er" takes the coordinated direct object "80 et le [81]". A bare singular nominal cannot coordinate with a determined NP in French: "prendre pain et le fromage" is ungrammatical (needs "prendre le pain et le fromage" / "prendre du pain et du fromage"). For the coordination to parse, 80 must be pronoun-like (cf. "prendre tout et le reste") or otherwise license bare-nominal behavior.
- Reading (b), bare DO + clausal "et": "[Vinf] [80]" then "et le [81] ..." as a coordinated clause. A bare singular/common noun cannot be a bare direct object in standard French ("prendre pain" needs the partitive: "prendre du pain"). And the clausal route fails independently: "le [81] m(82) vient(98) pour(00)" would need "m vient" = "me vient", which is letter-strict impossible (82='m' is a banked letter; "me" = 82+48; "m'" cannot elide before the consonant "vient").

Either reading requires a second ungranted assumption about 80's nominal subtype (pronoun-like/determined) — over the bar's budget of 1. 80's value and class are fully open and its only standing shape is verb-frame (A8), so no standing license supplies it.

Corroborating distributional note (not a verdict-driver): the "03 29 80" trigram occurs x3 stream-wide (@1032, @1322, @1596). A uniform nominal-80 reading would also have to parse @1032 ("[03]er [80] le la pre") and @1322 ("[03]er [80] [08] [62]"), where the nominal frame is at least as strained. No 80 window is nominal-shaped; all 17 are verb-frame-compatible (e.g. "24 80 03" @565, "98 80 10" @768, "21 80 77" @720).

Phase caveat (stated, not hidden): row a8_02's upstream offset (0) is unvalidated. Under its rival offset-1 the row re-pairs completely differently (['31','24','40','03','67',...]) and the "03 29 80 67 77 81" sequence dissolves — the window is a canonical-offset object. This fence holds on the canonical stream per protocol.

C2: FAIL. The claimed parse is demonstrable only with >=2 ungranted assumptions (nominal-80 + pronoun-like/determined subtype), exceeding the budget.

## Adverses (C3)

- Imperative 80: stays excluded — "[Vimp] et le [N]" is ungrammatical (adverse's own reasoning adopted; additionally the left "03 29" infinitive frame does not license an imperative). Not revived.
- Determiner 80: stays excluded — no following noun after 80 (adverse's reasoning adopted). Not revived.

Neither excluded rival rescues the nominal parse; the bar's else-branch fires.

C3: PASS (adverses answered — adopted, not ignored).

## Verdict: NULL (fence executed per the bar's else-branch)

Not promote (C2 fails within budget). Not kill (the grammaticality strain is conditional on 80's open value/class — a pronoun-like 80 rescues both readings; no window forces nominal-80 false and no cleaner rival was demonstrated on these frames).

@1596's nominal-80 reading is fenced, not decided. 81's noun class is untouched (C1 passes; feeds no change to noun-81).

## Follow-up targets (null regenerates work)

1. **nom-80-census** (P3): census 80's 17 windows for any nominal-shaped locus (priority frames: "03 29 80" x3 @1032/@1322/@1596, "21 80 77" @720). Bar: name a nominal 80 leg with <=1 unstated assumption; a pronoun-like or determined leg re-opens @1596 within the x29-80-1596-nominal budget.
2. **bare-noun-1841** (P4): 1841-French corpus check — can a bare singular nominal head a direct-object coordination ("[Vinf] N et le N'") or stand as a bare direct object? Decides whether the grammaticality objection above is kill-grade or merely budget-grade.
3. **stem-03-at-1594** (P3): test 03's class at @1594 — is "03 29" infinitive-shaped here, or is 03 noun-shaped (per 03's noun-shaped loci)? If 03 is nominal, the infinitive+DO frame dissolves and @1596's question re-opens in a different form.

## Bookkeeping

- Queue update: temp-file + rename on battery-queue.json, own entry only; pre-write assert confirmed status `queued`/verdictless; JSON re-validated after write; `x29-80-1596-nominal` -> status `verdict`, result `null`, date 2026-10-09.
- Lock deleted on completion. No other queue entry touched; no verdict downgraded; no red-team verdict contradicted or downgraded; §7 intact.
