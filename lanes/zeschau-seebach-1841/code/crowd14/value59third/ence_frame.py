#!/usr/bin/env python3
"""@825 'en ce'+noun frame corpus battery (VALUE59-THIRD, round 14).
Pool: code/side-period/corpus/*.txt EXCLUDING nesselrode-v8.txt (OCR caution).
Tokenizer: lane tok_elision verbatim.
"""
import os, re, glob, json, collections

LANE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/.."
CORP = os.path.join(LANE, "code/side-period/corpus")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ence_frame_results.json")

def tok_elision(text):
    text = text.replace('-\n','').replace('-\r\n','').lower()
    text = re.sub(r"[’‘`]", "'", text)
    text = re.sub(r"\b([a-zàâäéèêëîïôöùûüçœæ]+)'([a-zàâäéèêëîïôöùûüçœæ]+)", r"\1' \2", text)
    return re.findall(r"[a-zàâäéèêëîïôöùûüçœæ]+'?|[a-zàâäéèêëîïôöùûüçœæ]+", text)

D = []
files = 0
for f in sorted(glob.glob(os.path.join(CORP, '*.txt'))):
    bn = os.path.basename(f)
    if bn in ('PROVENANCE.md', 'harvest-log.txt', 'nesselrode-v8.txt'):
        continue
    D.extend(tok_elision(open(f, encoding='utf-8', errors='replace').read()))
    files += 1
N = len(D)
print(f"pool: {files} files, {N} tokens")

BIG = collections.Counter(zip(D, D[1:]))
TRI = collections.Counter(zip(D, D[1:], D[2:]))

def ngram(*toks):
    if len(toks) == 2:
        return BIG[tuple(toks)]
    return TRI[tuple(toks)]

res = {"pool_tokens": N}

# 1. 'en ce' followers
fol = collections.Counter()
for i in range(N - 2):
    if D[i] == "en" and D[i+1] == "ce":
        fol[D[i+2]] += 1
res["en_ce_total"] = sum(fol.values())
res["en_ce_top30"] = fol.most_common(30)

# 2. noun-ish followers of 'en ce' (exclude qui/que/pronouns) and their first syllables
stop = {"qui", "que", "qu'", "ce", "c'", "le", "la", "les", "l'", "un", "une",
        "des", "du", "de", "d'", "il", "elle", "ils", "elles", "on", "nous",
        "vous", "je", "j'", "tu", "ne", "n'", "se", "s'", "en", "y", "m'", "t'",
        "mon", "ma", "mes", "son", "sa", "ses", "notre", "votre", "leur",
        "aux", "au", "dans", "sur", "pour", "par", "avec", "sans", "sous",
        "entre", "vers", "chez", "est", "sont", "était", "a", "ont", "sera"}
noun_fol = [(w, c) for w, c in fol.most_common() if w not in stop]
res["en_ce_noun_top20"] = noun_fol[:20]

# 3. elided 'c'est' bigram (the R2 reading: 87-59 = c'+est)
res["c_prime_est"] = ngram("c'", "est")
res["ce_est_literal"] = ngram("ce", "est")

# 4. 'en cela'
res["en_cela"] = ngram("en", "cela")

# 5. followers of "c' est" (predicate after c'est)
cest_fol = collections.Counter()
for i in range(N - 2):
    if D[i] == "c'" and D[i+1] == "est":
        cest_fol[D[i+2]] += 1
res["cest_total"] = sum(cest_fol.values())
res["cest_top25"] = cest_fol.most_common(25)

# 6. 'de ce' followers (R4: 24='de' alternative)
dece_fol = collections.Counter()
for i in range(N - 2):
    if D[i] == "de" and D[i+1] == "ce":
        dece_fol[D[i+2]] += 1
res["de_ce_total"] = sum(dece_fol.values())
res["de_ce_top20"] = dece_fol.most_common(20)

# 7. 'en ce' + word starting with est- (any): scan raw
est_words = [(w, c) for w, c in fol.items() if w.startswith("est")]
res["en_ce_est_initial"] = est_words

# 8. X + "c'est" trigrams: what precedes "c' est" (for the clause-boundary reading)
pre_cest = collections.Counter()
for i in range(1, N - 2):
    if D[i] == "c'" and D[i+1] == "est":
        pre_cest[D[i-1]] += 1
res["pre_cest_top20"] = pre_cest.most_common(20)
res["pre_cest_en"] = pre_cest["en"]

# 9. 'en' + 'ce' as separate check: P(ce|en)
res["en_total"] = D.count("en")
res["P_ce_given_en"] = round(sum(fol.values()) / D.count("en"), 5) if D.count("en") else 0

json.dump(res, open(OUT, "w"), ensure_ascii=False, indent=1)
print(json.dumps(res, ensure_ascii=False, indent=1)[:6000])
print("wrote", OUT)
