## A. Global next-cell accuracy (held-out, n=20,000)

| mode | top-1 | top-3 | top-5 | MRR |
|---|---|---|---|---|
| standard | 32.1% | 45.8% | 52.2% | 0.418 |
| byear | 33.4% | 47.2% | 53.7% | 0.432 |

By available context length (cells):

| mode | ctx len | n | top-1 | top-3 | top-5 |
|---|---|---|---|---|---|
| standard | 5 | 19998 | 32.1% | 45.8% | 52.2% |
| byear | 5 | 19999 | 33.4% | 47.2% | 53.7% |

## B. Targeted solved contexts (held-out)

| phrase | mode | cells | occ | next-cell top-1/3/5 | next-word top-1/3/5 (beam, n) |
|---|---|---|---|---|---|
| la première | standard | la|pre|mie|re | 198 | 26.3%/35.9%/41.9% | 32.5%/45.0%/47.5% (n=40) |
| la première | byear | la|pre|m|i|er|e | 198 | 24.2%/33.3%/38.4% | 30.0%/32.5%/35.0% (n=40) |
| par ce que | standard | par|ce|que | 77 | 13.0%/31.2%/51.9% | 15.0%/37.5%/62.5% (n=40) |
| par ce que | byear | par|ce|que | 77 | 14.3%/31.2%/50.6% | 15.0%/40.0%/57.5% (n=40) |
| par le | standard | par|le | 820 | 24.5%/31.2%/35.4% | 22.5%/25.0%/35.0% (n=40) |
| par le | byear | par|le | 820 | 24.8%/32.0%/35.9% | 22.5%/25.0%/35.0% (n=40) |
| qui | standard | qui | 7359 | 10.6%/21.9%/30.7% | 5.0%/20.0%/32.5% (n=40) |
| qui | byear | qui | 7363 | 10.8%/22.1%/30.8% | 5.0%/20.0%/32.5% (n=40) |
| que | standard | que | 17027 | 17.5%/32.9%/42.1% | 22.5%/35.0%/55.0% (n=40) |
| que | byear | que | 17030 | 17.5%/32.9%/42.2% | 22.5%/35.0%/55.0% (n=40) |
| ce qui | standard | ce|qui | 637 | 14.1%/26.8%/34.2% | 15.0%/20.0%/30.0% (n=40) |
| ce qui | byear | ce|qui | 637 | 14.8%/27.9%/35.6% | 17.5%/22.5%/32.5% (n=40) |
| en ce | standard | en|ce | 117 | 29.9%/48.7%/54.7% | 35.0%/50.0%/57.5% (n=40) |
| en ce | byear | en|ce | 117 | 29.9%/48.7%/53.8% | 35.0%/47.5%/57.5% (n=40) |
| m'en | standard | m|en | 95 | 8.4%/17.9%/24.2% | 17.5%/20.0%/22.5% (n=40) |
| m'en | byear | m|en | 93 | 8.6%/18.3%/24.7% | 17.5%/20.0%/22.5% (n=40) |
| ne | standard | ne | 12585 | 32.0%/42.9%/48.4% | 40.0%/52.5%/60.0% (n=40) |
| ne | byear | ne | 15609 | 23.6%/35.1%/41.9% | 30.0%/45.0%/55.0% (n=40) |

### la première [standard] — examples (true next 3 cells vs model top-5 beam)

- true: `nou|vel|le`
  beam#1: `fois`
  beam#2: `de`
  beam#3: `re`
  beam#4: `fois|que`
  beam#5: `et`
- true: `te|nue|le`
  beam#1: `par`
  beam#2: `par|tie`
  beam#3: `par|tie|de`
  beam#4: `an`
  beam#5: `e`
- true: `pen|see|du`
  beam#1: `fois`
  beam#2: `de`
  beam#3: `re`
  beam#4: `fois|que`
  beam#5: `et`

### la première [byear] — examples (true next 3 cells vs model top-5 beam)

- true: `nou|vel|le`
  beam#1: `fois`
  beam#2: `de`
  beam#3: `et`
  beam#4: `re`
  beam#5: `par`
- true: `te|nue|le`
  beam#1: `fois`
  beam#2: `de`
  beam#3: `et`
  beam#4: `re`
  beam#5: `par`
- true: `pen|see|du`
  beam#1: `fois`
  beam#2: `de`
  beam#3: `et`
  beam#4: `re`
  beam#5: `par`

### par ce que [standard] — examples (true next 3 cells vs model top-5 beam)

- true: `la|re|for`
  beam#1: `les`
  beam#2: `la`
  beam#3: `nous`
  beam#4: `le`
  beam#5: `l`
- true: `nous|a|vons`
  beam#1: `les`
  beam#2: `la`
  beam#3: `nous`
  beam#4: `le`
  beam#5: `l`
- true: `j|y|vois`
  beam#1: `les`
  beam#2: `la`
  beam#3: `nous`
  beam#4: `le`
  beam#5: `l`

### par ce que [byear] — examples (true next 3 cells vs model top-5 beam)

- true: `la|re|form`
  beam#1: `les`
  beam#2: `la`
  beam#3: `nous`
  beam#4: `le`
  beam#5: `l`
- true: `nous|a|vons`
  beam#1: `les`
  beam#2: `la`
  beam#3: `nous`
  beam#4: `le`
  beam#5: `l`
- true: `j|y|vois`
  beam#1: `les`
  beam#2: `la`
  beam#3: `nous`
  beam#4: `le`
  beam#5: `l`

### "ne X" → "pas" frames (25 most frequent held-out bigrams)

| mode | ne X | count | rank of "pas" |
|---|---|---|---|
| standard | `ne|ment` | 1249 | 69 |
| standard | `ne|ral` | 513 | 63 |
| standard | `ne|ces` | 469 | 145 |
| standard | `ne|se` | 453 | 20 |
| standard | `ne|ra` | 363 | 10 |
| standard | `ne|de` | 330 | 14 |
| standard | `ne|a` | 302 | 60 |
| standard | `ne|pou` | 276 | 116 |
| standard | `ne|go` | 237 | 135 |
| standard | `ne|s` | 235 | 93 |
| standard | `ne|peut` | 232 | 1 |
| standard | `ne|pas` | 227 | 176 |
| standard | `ne|en` | 216 | 102 |
| standard | `ne|re` | 216 | 127 |
| standard | `ne|l` | 194 | 120 |
| standard | `ne|le` | 194 | 121 |
| standard | `ne|et` | 159 | 108 |
| standard | `ne|raux` | 159 | 128 |
| standard | `ne|sont` | 149 | 1 |
| standard | `ne|con` | 143 | 246 |
| standard | `ne|sau` | 140 | 103 |
| standard | `ne|lui` | 132 | 179 |
| standard | `ne|mens` | 129 | 281 |
| standard | `ne|pour` | 121 | 115 |
| standard | `ne|ments` | 114 | 50 |
| byear | `ne|m` | 1538 | 55 |
| byear | `ne|de` | 811 | 35 |
| byear | `ne|a` | 586 | 66 |
| byear | `ne|et` | 491 | 159 |
| byear | `ne|se` | 488 | 24 |
| byear | `ne|ces` | 473 | 147 |
| byear | `ne|pou` | 354 | 126 |
| byear | `ne|en` | 349 | 127 |
| byear | `ne|le` | 308 | 67 |
| byear | `ne|s` | 256 | 99 |
| byear | `ne|re` | 249 | 140 |
| byear | `ne|l` | 242 | 128 |
| byear | `ne|pas` | 239 | 178 |
| byear | `ne|peut` | 238 | 1 |
| byear | `ne|go` | 237 | 133 |
| byear | `ne|son` | 206 | 1 |
| byear | `ne|la` | 176 | 41 |
| byear | `ne|d` | 170 | 142 |
| byear | `ne|les` | 152 | 97 |
| byear | `ne|par` | 150 | 250 |
| byear | `ne|sau` | 141 | 101 |
| byear | `ne|lui` | 140 | 184 |
| byear | `ne|des` | 139 | 111 |
| byear | `ne|e` | 131 | 111 |
| byear | `ne|con` | 127 | 282 |

## C. Verb-stem inflection prediction (held-out)

| stem | mode | cells | occ | top-1 | top-3 | top-5 | MRR |
|---|---|---|---|---|---|---|---|
| enco | standard | en|co | 602 | 99.0% | 99.0% | 99.2% | 0.991 |
| not | standard | not | 42 | 78.6% | 78.6% | 81.0% | 0.794 |
| fai | standard | fai | 602 | 78.1% | 87.9% | 91.9% | 0.845 |
| quelqu | standard | quel|qu | 42 | 73.8% | 100.0% | 100.0% | 0.845 |
| avo | standard | a|vo | 90 | 67.8% | 80.0% | 90.0% | 0.760 |
| vot | standard | vot | 5 | 60.0% | 60.0% | 60.0% | 0.605 |
| éta | standard | e|ta | 335 | 58.2% | 79.7% | 86.6% | 0.694 |
| cell | standard | cell | 2 | 50.0% | 50.0% | 50.0% | 0.501 |
| ser | standard | ser | 602 | 42.5% | 57.6% | 62.6% | 0.520 |
| port | standard | port | 134 | 34.3% | 53.7% | 54.5% | 0.452 |
| ent | standard | ent | 20 | 25.0% | 25.0% | 25.0% | 0.265 |
| ava | standard | a|va | 58 | 20.7% | 29.3% | 55.2% | 0.320 |
| grand | standard | grand | 601 | 16.6% | 25.1% | 30.3% | 0.242 |
| tout | standard | tout | 602 | 15.9% | 36.0% | 46.7% | 0.298 |
| franc | standard | franc | 54 | 3.7% | 11.1% | 11.1% | 0.079 |
| cett | standard | cett | 1 | 0.0% | 0.0% | 0.0% | 0.111 |
| comm | standard | comm | 2 | 0.0% | 0.0% | 0.0% | 0.004 |
| aut | standard | aut | 3 | 0.0% | 0.0% | 0.0% | 0.009 |
| mond | standard | mond | 12 | 0.0% | 16.7% | 16.7% | 0.110 |
| cont | standard | cont | 1 | 0.0% | 0.0% | 0.0% | 0.021 |
| autr | standard | autr | 1 | 0.0% | 0.0% | 0.0% | 0.004 |
| ell | standard | ell | 1 | 0.0% | 0.0% | 0.0% | 0.077 |
| trouv | standard | trouv | 1 | 0.0% | 100.0% | 100.0% | 0.333 |
| dev | standard | dev | 1 | 0.0% | 0.0% | 0.0% | 0.067 |
| homm | byear | homm | 576 | 100.0% | 100.0% | 100.0% | 1.000 |
| comm | byear | comm | 602 | 99.7% | 99.7% | 99.7% | 0.997 |
| enco | byear | en|co | 602 | 97.7% | 97.8% | 97.8% | 0.979 |
| fai | byear | fai | 602 | 78.4% | 88.2% | 91.9% | 0.847 |
| not | byear | not | 37 | 78.4% | 78.4% | 81.1% | 0.793 |
| quelqu | byear | quel|qu | 42 | 73.8% | 100.0% | 100.0% | 0.845 |
| avo | byear | a|vo | 90 | 67.8% | 76.7% | 86.7% | 0.746 |
| vot | byear | vot | 5 | 60.0% | 60.0% | 60.0% | 0.605 |
| éta | byear | e|ta | 344 | 55.5% | 77.0% | 84.3% | 0.670 |
| cell | byear | cell | 2 | 50.0% | 50.0% | 50.0% | 0.500 |
| grand | byear | gran | 602 | 49.3% | 62.3% | 66.3% | 0.579 |
| ser | byear | ser | 602 | 43.9% | 58.8% | 63.5% | 0.532 |
| mond | byear | mon | 602 | 37.4% | 47.5% | 51.8% | 0.448 |
| port | byear | port | 134 | 35.1% | 53.7% | 54.5% | 0.456 |
| cont | byear | con | 603 | 35.0% | 53.1% | 59.5% | 0.467 |
| ava | byear | a|va | 58 | 24.1% | 32.8% | 58.6% | 0.354 |
| ent | byear | en | 603 | 19.4% | 29.7% | 36.7% | 0.283 |
| donn | byear | don | 602 | 15.6% | 34.1% | 52.0% | 0.309 |
| tout | byear | tout | 602 | 15.4% | 35.7% | 46.8% | 0.295 |
| franc | byear | franc | 54 | 3.7% | 11.1% | 11.1% | 0.077 |
| cett | byear | cett | 1 | 0.0% | 100.0% | 100.0% | 0.500 |
| aut | byear | aut | 3 | 0.0% | 0.0% | 0.0% | 0.009 |
| autr | byear | autr | 1 | 0.0% | 0.0% | 0.0% | 0.004 |
| ell | byear | ell | 1 | 0.0% | 0.0% | 0.0% | 0.167 |
| trouv | byear | trouv | 1 | 0.0% | 0.0% | 100.0% | 0.250 |
| dev | byear | dev | 1 | 0.0% | 0.0% | 0.0% | 0.067 |

## D. By-ear mismatch quantification (TRAIN)

- word disagreement rate (200k-word sample): 11.1%
- cells/word: standard 1.659, byear 1.700
- vocab: standard 16742, byear 16754, Jaccard 0.887
- by-ear-only cells: 1006; standard-only cells: 994

| banked cell | std rank (count) | byear rank (count) |
|---|---|---|
| la | 5 (79722) | 6 (79732) |
| pre | 57 (13581) | 62 (13514) |
| m | 71 (10492) | 18 (39762) |
| i | 82 (9518) | 16 (42764) |
| er | 731 (544) | 14 (48759) |
| e | 9 (55181) | 2 (130524) |
| que | 10 (53466) | 10 (53472) |
| ce | 11 (52965) | 11 (52965) |
| qui | 28 (23536) | 30 (23571) |
| par | 27 (24448) | 28 (24375) |
| est | 34 (21680) | 35 (21680) |
| le | 3 (101406) | 4 (101311) |

