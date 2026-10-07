# LM build stats — Seebach homophonic solver (Track A, register-matched)

- corpus: guizot-memoires-t5-t6.txt; nesselrode-v7.txt; nesselrode-v8.txt; nesselrode-v9.txt; nesselrode-v10.txt; revue-deux-mondes-1841-q1.txt; revue-deux-mondes-1841-q2.txt; revue-deux-mondes-1841-q3.txt; revue-deux-mondes-1841-q4.txt
- exclude_span: [[100000, 104000], [200000, 204000]] (Track-A instance truth)
- subsample: {'method': 'deterministic shuffle', 'seed': 184101, 'n_words': 215000}
- words: 215000 (distinct 23961)
- projected chars: 756241; alphabet (30): ACINOSUabcdefghijklmnopqrstuvz
- n-gram order: 5
- held-out per-char logp: -2.6133 (perplexity 13.64)
- lexicon: 4776 words (minlen 4, top 40000)
- built: 2026-10-07T19:22:10Z

## Register note
1840-42 diplomatic French (Guizot despatches, Nesselrode correspondence, Revue des Deux Mondes 1841). Register-MATCHED to the 1841 diplomatic task; register-GAPPED from the Les Mis 1862 control plaintext (deliberate: Les Mis is sealed-truth text and off-limits for training).

## Top lexicon words (projected forms)
avec(6.6695), cete(6.6399), meme(6.4998), come(6.3244), leur(6.157), tute(6.1291), otre(6.0845), etre(6.0638), fere(5.9054), Acore(5.8805), frAce(5.8608), kelke(5.8377), mOde(5.7236), leurs(5.6058), Atre(5.5872), apre(5.5452), cOte(5.5053), notre(5.5013), guvernemA(5.4553), cOtre(5.3891), dire(5.3706), avoir(5.366), lord(5.3083), afere(5.2523), grAde(5.2417), kestiO(5.1985), politike(5.1818), parti(5.1533), tujurs(5.1299), porte(5.124), espri(5.118), Agletere(5.118), cele(5.112), Cose(5.1059), depui(5.0999), etaI(5.0938), revue(5.0814), guere(5.0752), sere(5.0689), votre(5.0689)
