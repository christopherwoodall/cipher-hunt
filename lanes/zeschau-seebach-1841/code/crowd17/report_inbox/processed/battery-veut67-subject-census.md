# Battery report: veut67-subject-census

- Target id: `veut67-subject-census`
- Claim: "census the subject slot of all five positional-rule veut-67s"
- Date: 2026-10-09
- Worker: battery worker (subagent 4c49a132-68d1-416c-8372-93d31801e173)
- Stream: repaired 1,847-pair / 96-type parse from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` (re-derived in-session; asserts: 1847 pairs, 96 types held). `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched.
- @ convention: 0-based index of the 67 pair itself.

## Bar (verbatim)

"state the subject context of @110 (pre=21), @272 (pre=06), @1390 (pre=29), @1423 (pre=21), @1476 (pre=06); if 'veut' systematically lacks an overt subject, record that as weakening the positional rule's 'if' direction"

Numbered clauses (pre-registered before testing):
1. (C1) State the subject context of each of the five windows with byte evidence.
2. (C2) Assess: does "veut" systematically lack an overt subject across the five?
3. (C3) If yes, record that as weakening the positional rule's "if" direction (follower-infinitive-shaped → 67="veut").

## Population completeness

Census of all 38 stream-wide 67 windows: exactly 5 have an infinitive-shaped follower ("X 29") — @110, @272, @1390, @1423, @1476. The five are the complete population of positional-rule veut-67s; no others exist. The target's "five-window sample" is the whole set.

## Window-level evidence

Standing premises used (not re-litigated): 11="la" (pencil GT); 21 noun-class (battery-promoted, value open); 29="er" bound morpheme (banked); 60 verb-class (battery-promoted, split red-team venue); 06 "-ent iff left neighbor is a verb stem" (battery-promoted rule); 67="veut" iff follower infinitive-shaped (standing §7 positional rule, not adjudicated here).

| Window | Left context (byte-exact) | Subject of "veut" | Verdict |
|---|---|---|---|
| 0b@110 (a1_03) | `00 46 11 21 [67] 93 29` | **"la 21"** — overt NP: det "la" + nominal 21 ("pour que la [21] veut [93]er") | OVERT ✓ |
| 0b@272 (a2_03) | `47 11 06 [67] 33 29` | **"la 06"** — overt NP-shaped: det "la" + 06 in forced nominal position ("la [06] veut [33]er"); 06's class open but "la"+verb-stem ungrammatical | OVERT ✓ |
| 0b@1390 (a7_07) | `82 16 06 29 [67] 86 29` | **None (anomalous)** — would-be subject is "06 29" = "[06]er", an infinitive-shaped word; a bare infinitive is not a grammatical subject of "vouloir" in 1841 French. No NP subject anywhere in the clause (`52 82 16` left is "m' [16-inf]"). Note: this window is independently contested — the §7 positional rule and the "et" arm both fire here (et86er-licensor-16); the anomaly is stated under the veut-arm. | SUBJECTLESS ⚠ |
| 0b@1423 (a7_08) | `15 33 21 [67] 33 29` | **"33 21"** — overt NP: nominal 21 with left modifier 33 ("[33] [21] veut [33]er") | OVERT ✓ |
| 0b@1476 (a7_10) | `41 53 60 06 [67] 33 29` | **None (anomalous)** — would-be subject "60 06": with 60 verb-class promoted, the leading parse is "[60]ent" (3pl finite verb via the ent-attachment rule), giving two adjacent finite verbs — ungrammatical. Under no parse ("41 53" as subject, 60/06 split) does a clean NP subject emerge. | SUBJECTLESS ⚠ |

## Per-clause pass/fail

- **C1 PASS** — all five subject contexts stated with byte evidence; population verified complete (5/38).
- **C2: conditional does not fire** — 3/5 windows have overt NP subjects; "veut" does NOT systematically lack an overt subject.
- **C3: no rule-level weakening recorded** — C2's antecedent is false. The positional rule's "if" direction survives the census. The 2/5 anomalous loci (@1390, @1476) are fenced as subject-anomalous under the veut-arm (stated cause above), not promoted, not killed.

## Adverses answered

- "five-window sample" — verified as the complete population (5 of 38 67-windows), not a sample; noted in the census.
- "21's value open" — acknowledged; the census is class-level (noun-class 21) and needs no value. Does not affect the subject-slot finding.

## Verdict: PROMOTE

All bar clauses pass (C2/C3 conditional, correctly assessed as not firing). No standing or red-team verdict contradicted; the §7 positional rule and its biconditional stand untouched — this battery tests only its subject-slot consequences. No §7 polyvalence declared. Canonical-stream caveat: rows a1_03/a2_03/a7_07/a7_08/a7_10 offsets are upstream (unvalidated).

No follow-ups mandated (promote, not null). Discretionary lead for the supervisor: the @1390 subject anomaly converges with the et-vs-veut contest there (et86er-licensor-16 NULL); the @1476 "[60]ent"-vs-subject tangle re-opens if the red team splits 60.
