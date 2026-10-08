# Digit hunt

Low-n groups (n<5): 04, 22, 27, 54, 57, 90, 95, 99

Digit-digit adjacent pairs observed: 0 vs null mean 0.10 / max 2 (200 permutations).

## 04 (n=3, phase R)
- positions: [957, 1296, 1809]
- start-5%: 0, end-5%: 1
- distinct pre/suc: 2/3; pre=['80', '85'], suc=['20', '61', '62']
- contacts with top-20 core: 1; adjacent to other low-n: 0

## 22 (n=3, phase R)
- positions: [770, 1663, 1837]
- start-5%: 0, end-5%: 1
- distinct pre/suc: 3/2; pre=['10', '64', '80'], suc=['42', '94']
- contacts with top-20 core: 2; adjacent to other low-n: 0

## 27 (n=1, phase R)
- positions: [1691]
- start-5%: 0, end-5%: 0
- distinct pre/suc: 1/1; pre=['60'], suc=['46']
- contacts with top-20 core: 1; adjacent to other low-n: 0

## 54 (n=3, phase R)
- positions: [333, 605, 908]
- start-5%: 0, end-5%: 0
- distinct pre/suc: 3/3; pre=['45', '83', '93'], suc=['49', '64', '88']
- contacts with top-20 core: 1; adjacent to other low-n: 0

## 57 (n=1, phase R)
- positions: [1225]
- start-5%: 0, end-5%: 0
- distinct pre/suc: 1/1; pre=['20'], suc=['64']
- contacts with top-20 core: 1; adjacent to other low-n: 0

## 90 (n=1, phase R)
- positions: [120]
- start-5%: 0, end-5%: 0
- distinct pre/suc: 1/1; pre=['60'], suc=['19']
- contacts with top-20 core: 0; adjacent to other low-n: 0

## 95 (n=2, phase R)
- positions: [821, 1407]
- start-5%: 0, end-5%: 0
- distinct pre/suc: 2/2; pre=['11', '40'], suc=['13', '46']
- contacts with top-20 core: 2; adjacent to other low-n: 0

## 99 (n=1, phase R)
- positions: [1553]
- start-5%: 0, end-5%: 0
- distinct pre/suc: 1/1; pre=['23'], suc=['13']
- contacts with top-20 core: 0; adjacent to other low-n: 0

## Verdict: NEGATIVE (falsifier fired)

- T1 digit-digit adjacency: 0 observed vs null mean 0.10 / max 2 — no signal either way (power ~nil at n=1–3).
- T2/T4 falsifier (syllable-like contact profiles): **FIRED.** 95 sits between 11=la/40=e and 46=que (grammatical frame slot); 22→94/←64=qui; 27→46=que; 57→64=qui; 54→64=qui; 04→62("on"-fenced). Hapax-vocabulary cells embedded in grammar, not isolated digits.
- T3 date-position clustering: 2/15 occurrences at stream edges — chance-consistent.
- Residual (not a finding): 27 and 90 share predecessor 60 (60→27→46, 60→90→19); 60 (n=18) unidentified.
**Recommendation: retire the digit hunt; reclassify the 8 as rare-vocabulary cells.** If the despatch carries dates they are likelier spelled out.
