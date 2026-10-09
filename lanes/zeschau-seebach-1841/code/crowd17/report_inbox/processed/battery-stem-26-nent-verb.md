# Battery verdict: stem-26-nent-verb

- Target: `stem-26-nent-verb` (battery-queue.json, priority 3, status queued)
- Claim: "Decide 26's class at @1707 via its 17-window distributional profile (followers 12x4/30x4/00x3; predecessors 69x3/11x2/64x2/24x2). The '[26]nent' 3pl-verb word-shape at @1707-1709 ('viennent'-shaped) is live iff 26 is verb-stem-class; kill the verb fork on the profile if 26 is noun-class."
- Adverses: profile must be the full 17 windows.

## Bar (verbatim, pre-registered)

"26 takes a verb-stem value making '[26]n-ent' a grammatical 3pl French verb, or the fork is killed on 26's distributional profile"

## Bar restated as numbered pass/fail clauses

1. C1 — 26 takes a verb-stem value making "[26]n-ent" a grammatical 3pl French verb (value NAMED, selected over rivals).
2. C2 — else, the verb fork is killed on 26's distributional profile.

## Method

Read BATTERY-PROTOCOL.md first; created `locks/stem-26-nent-verb.lock` on start (agent 19aa602e, 2026-10-09T19:50Z). Re-derived the repaired stream in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (1,847 pairs / 96 types verified via repair_parse.py); `canonical.py` never touched.

Cited, not re-litigated: battery-noun-26 (NULL — one-class resolution falsified at kill grade on both sides; positional rule stated but undeclared per §7), battery-26-class-1754 (PROMOTE, finding grade — 26 verb-class at @1754, conditional on the positional rule), battery-noun26-26n-exclude (NULL — "26n" one-word rival excluded at 2 of 3 la-windows by contact, fenced at the third).

Standing values used: 11="la" (banked GT), 12="n" (promoted letter tier), 06="ent" (R17-007 granted 3pl ending), 88 governor-class, 26=["noun","lead"] (registry).

## Window-level evidence

Full 17-window profile rendered with standing values (0-based offsets):

| @ | window |
|---|---|
| 129 | 11(la) 02 26 32(verb) 96(par) |
| 155 | 66 84(on) 26 35(noun) 58(nominal) |
| 240 | 17(fois) 11(la) 26 12(n) 16 |
| 406 | 34(i) 69(noun) 26 00(pour) 33(INF) |
| 531 | 37 64(qui) 26 32(verb) 16 |
| 601 | 03(verb-stem) 39(a/à) 26 96(par) 45(ce) |
| 655 | 49 24(verb) 26 30(pas) 03(verb-stem) |
| 842 | 62 94(ne) 26 12(n) 16 00(pour) |
| 934 | 56 69(noun) 26 00(pour) 33(INF) 21(noun) |
| 992 | 49 24(verb) 26 30(pas) 03(verb-stem) 60 |
| 1250 | 67 46(que) 26 30(pas) 06(ent) 65(noun) |
| 1470 | 62 38(verb) 26 12(n) 41 53 |
| 1560 | 17(fois) 11(la) 26 30(pas) 06(ent) 60 |
| 1628 | 56 69(noun) 26 00(pour) 33(INF) 21(noun) |
| 1707 | 94(ne) 88(gov) 26 12(n) 06(ent) 29(er) 40(e) |
| 1753 | 28 89(noun) 26 24(verb) 85 58(nominal) |
| 1769 | 87(ce) 64(qui) 26 37 78(ver) |

### C1 — no verb-stem value is nameable: FAIL

The "26 12 06" trigram is exactly 1× stream-wide (@1707). At @1707, "88(gov) [26]n-ent" is a grammatically licensed governor + 3pl-verb frame — the SHAPE is live. But a VALUE must be selected over rivals (lane naming bar: zero new assumptions, selective legs). Every 3pl "-nent" verb parses the window identically: viennent, tiennent, deviennent, reviennent, souviennent, appartiennent, contiennent, maintiennent, retiennent, obtiennent, soutiennent… 88's governor class selects none of them; no neighbor discriminates. Naming any one would be arbitrary (precedent: masc-noun-86-name, stem-86-29-value). C1 FAIL.

### C2 — uniform verb-stem 26 is killed on the profile: PASS

Three windows force noun-class at kill grade, contradicting a uniform verb-stem 26:

- **@240 "la 26"**: article directly before 26 — a verb-stem cannot follow "la". (The "26n" one-word rival at this window was separately fenced in noun26-26n-exclude; it is a NOUN reading, not a verb rescue.)
- **@1560 "la 26"**: same kill, independent window.
- **@129 "la 02 26"**: 26 as finite verb after "la [02]" is ungrammatical under every 02 class.

Supporting noun legs: @406/@934/@1628 "69(noun) 26 pour" (noun-noun contact), @531 "qui [26] 32(verb)" (relative pronoun + nominal subject + verb is the grammatical parse; "qui [V] [V]" is not), @601 "à [26] par" (preposition + noun).

A uniform verb-stem 26 is therefore dead at kill grade. The only rescue is a conditioned split (verb-stem at @1707 vs noun elsewhere) — but 67 et/veut is the sole ratified polyvalence, and declaring a second is §7 red-team venue, which the battery cannot do (the positional rule already stands undeclared per battery-noun-26).

## Verdict: KILL

The uniform verb-stem fork for 26 is killed on the distributional profile (C1 FAIL, C2 PASS).

## Scope

Kills only the UNIFORM verb-stem reading of 26. Explicitly NOT killed: the locus-level verb reading at @1707 ("88 [26]n-ent" remains a licensed frame) — it survives as the standing conditioned-split question, consistent with the @1754 verb-class promote, and stays red-team venue under §7. Untouched: 26's noun LEAD, battery-noun-26's positional rule, 26-class-1754, noun26-26n-exclude, all standing/red-team verdicts. No §7 declaration made. Canonical-stream caveat stands (row offsets unvalidated).

No follow-ups required (kill, not null). The locus-level question is already owned by the standing red-team §7 venue (noun-26 positional rule).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-stem-26-nent-verb.md`
- Queue: `stem-26-nent-verb` queued → `verdict`/`kill`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.stem-26-nent-verb.tmp` + rename; disk re-validated; own entry only; no downgrade)
- Lock `locks/stem-26-nent-verb.lock`: created on start, deleted on completion (verified gone)
- R5005, sealed gates, red-team adjudication queue untouched
