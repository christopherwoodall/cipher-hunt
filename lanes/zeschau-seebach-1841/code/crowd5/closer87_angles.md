# 87=ce new angles — closer round 5 (A)

Stream: repaired 1,847-pair parse. n(87)=32, n(47)=28, n(84)=25, n(24)=52.
Dead legs NOT recycled: cela-rate, register-subset, ci/te, 24="est".

## A1 — "c'est" word-space rate (joint with 01="est" MEDIUM lead)
- cipher: 87->01 x[344, 1028], 47->01 x[194] = 3 "c'est"-bigrams / 958 words = 0.00313/word
- era tocqueville: n("c","est")=361, rate=0.00168, cipher/era = 1.86x
- era lesmis: n("c","est")=416, rate=0.00348, cipher/era = 0.90x
- complements after the 3: {'344': ['06', '70', '12'], '1028': ['03', '29', '80'], '194': ['21', '60', '08']}
- Read: the conditional P(01|87)=2/32 looks low only because 87 conflates "ce"+"c'"; in word space the "c'est"-bigram rate is in-band on BOTH corpora. Supports (87=ce ^ 01=est) jointly.

## A2 — 87/47 distributional homology
- follower Jaccard(87,47) = 0.435 (null median 0.111, 95th 0.321, percentile 0.97)
- shared followers: 01, 08, 11, 14, 46, 76, 77, 78, 86, 98
- predecessor Jaccard = 0.240; shared: 24, 29, 56, 74, 76, 96
- DIVERGENCE: P(64|47) = 0.0000 (0/28) vs era P(qui|ce) = 0.1878; binom P(0/28) = 0.0030
- "ce que": 87: 0.0938, 47: 0.1071, era 0.1076, lesmis 0.1403
- 47 mini-inversion (P(que|W)~0.107, P(qui|W)~0, n>50): [('ainsi', 369, 0.1355, 0.0027), ('bien', 295, 0.0712, 0.0), ('sorte', 148, 0.0743, 0.0), ('peine', 137, 0.0803, 0.0146), ('fois', 131, 0.0992, 0.0), ('cependant', 129, 0.0853, 0.0078), ('dit', 122, 0.1066, 0.0), ('avant', 93, 0.1075, 0.0)]; 'ce' rank in list: None
- Read: homology on followers ("que", "la" both) but 47 NEVER takes "qui" (p=0.0032) -- 47 is not the same "ce" as 87, or 47="ce" needs conditioning. This BOUNDS the 47="ce" LEAD and sharpens 87=ce by contrast (87 takes "qui" at era rate 5/32).

## A3 — 24->87 x10: continuations are "ce"-canonical
- n(24->87) = 10; continuations: {'11': 3, '64': 3, '98': 1, '61': 1, '59': 1, '08': 1}
- 24-87-64 ("24, ce qui") x3 @ [179, 1766, 1774]; 24-87-11 ("24 cela") x3 @ [73, 162, 829]; 24-87-46 x[] (0 -- F13 re-verified on repaired parse)
- P(64|24-87) = 0.300 vs era P(qui|ce) = 0.188; wilson(3/10) = [0.108, 0.603]
- contexts: {'179': ['86', '21', '69', '14', '24', '87', '64', '23', '37', '06', '00', '33'], '1766': ['06', '77', '84', '09', '24', '87', '64', '26', '37', '78', '62', '94'], '1774': ['37', '78', '62', '94', '24', '87', '64', '59', '19', '48', '74', '65']}
- Read: the old 24->87 tension (24="en" lead) is reframed -- whatever 24 is, after it 87 behaves exactly like "ce" in its two most characteristic frames ("ce qui", "cela"-shape). Positive leg for 87=ce, independent of 24's value.

## A4 — 84 bounding (for the @1800 "ce qui [verbe] 84" thread)
- P(84) = 0.0135 (rank 26); P(84|46="que") = 0.0690 (x2 @ [309, 472]); P(84|77) = 0.1591 (x7 @ [145, 259, 1057, 1446, 1484, 1763, 1802])
- 84="fait" KILLED on unigram: cipher 0.0135 vs era 0.0020 = 6.7x
- inversion top candidates (unigram 4x-band, after "que" and "le"): [('plus', 0.0024, 0.0361), ('même', 0.0003, 0.019), ('leur', 0.0087, 0.0022), ('sur', 0.0094, 0.0002), ('n', 0.0028, 0.0004)]
- predecessors: {'77': 7, '66': 2, '89': 2, '46': 2, '53': 2, '82': 1, '91': 1, '65': 1, '48': 1, '06': 1}; followers: {'59': 4, '24': 3, '02': 2, '92': 2, '09': 2, '29': 1, '26': 1, '53': 1, '74': 1, '91': 1}
- Read: 84 unresolved but bounded; "que 84" x2 is GT-anchored (46=que). The @1800 corroboration stays corroboration-only until 84 resolves. Refinement (verified on repaired stream): two of the three 64-77-84 trigrams extend to an identical 4-gram **64-77-84-59 x2** (@1445-1448 and @1801-1804; the third @144-147 ends 84-29). So the @1800 thread reads "ce qui 77 84 59" with 84->59 itself a repeated bigram (x4, 84's top follower) - n_eff=1 for rate purposes, unchanged.

## A5 — 87->11 x7 structural (cela-adjacent observation, NOT a rate leg)
- positions: [74, 163, 201, 461, 830, 1242, 1403]
- followers of 87-11: [('00', 3), ('24', 1), ('92', 1), ('59', 1), ('77', 1)] ("87-11-00" x3)
- repeated 5-gram 77-81-87-11-00: x2
- pre2 grams: [('14', '24'), ('94', '24'), ('67', '76'), ('02', '79'), ('01', '24'), ('77', '81'), ('77', '81')]
- Read: structural only. The dead cela-RATE leg is not rebuilt; the bigram fact (7/32) and the "87-11-00" x3 frame are banked for the 00-identification work.

## Verdict

- 87=ce: HOLDS provisional-strengthened; A1 (c'est word-space, in-band both corpora) and A3 ("ce"-canonical continuations after 24) are two NEW positive legs, both F30-legal and non-circular. A2 bounds the 47="ce" rival (qui-divergence p=0.0032) rather than supporting it.
- 84: NOT resolved (fait killed, inversion inconclusive) -- the @1800 thread stays corroboration.
- No promotion claimed; red-team adjudication required per standing rule.
