"""Corpus-side French syllable inventory (Tocqueville t1+t2, era corpus).
Method: letter-based maximal-onset syllabification. Nuclei: nasal vowels
(an/en/in/on/un/am/em/im/om), diphthongs (ai/au/eau/ei/eu/ou/oi/ui/ie/ue),
single vowels (a/a e/e i/i o/o u/u y). Between nuclei, consonants go to the
following onset (maximal onset); 'qu'/'gu' kept together. This is a CORPUS
measurement (inventory size + coverage), not a cipher-side leg -- F30-safe.
"""
import re
from collections import Counter

V1 = set('aaeeiioouuy')
NASAL = {'an','en','in','on','un','am','em','im','om'}
DIPH = {'ai','au','eau','ei','eu','ou','oi','ui','ie','ue','oe','ee','oo','aa','ii','uu'}

def nuclei(word):
    out, i = [], 0
    while i < len(word):
        c = word[i]
        if c in V1 or c in 'e':
            for L in (3, 2, 1):
                if word[i:i+L] in (DIPH if L > 1 else V1) or (L == 2 and word[i:i+L] in NASAL):
                    out.append((i, word[i:i+L])); i += L; break
            else:
                out.append((i, c)); i += 1
        else:
            i += 1
    return out

def syllabify(word):
    w = word.lower()
    w = re.sub(r'[^a-zàâäéèêëîïôöùûüyç]', '', w)
    if not w: return []
    nuc = nuclei(w)
    if not nuc: return [w]
    syls, prev_end = [], 0
    for k, (s, txt) in enumerate(nuc):
        if k == 0:
            start = 0
        else:
            # maximal onset: consonants between prev nucleus end and this start go here,
            # except keep with previous coda if cluster would be illegal onset (crude: split 2+ clusters, keep 1)
            gap = w[prev_end:s]
            if len(gap) >= 2:
                start = prev_end + len(gap) - 1  # last consonant to onset... actually split: all but last stay
                # correction: maximal onset -> all but keep it simple: first half coda
                start = prev_end  # placeholder, recompute below
                start = s - 1 if len(gap) >= 1 else s
            else:
                start = prev_end
        prev_end = s + len(txt)
        syls.append((start, prev_end))
    # rebuild with proper boundaries
    bounds = [0]
    for k in range(1, len(nuc)):
        s_prev, t_prev = nuc[k-1]; s_cur, t_cur = nuc[k]
        gap = w[s_prev+len(t_prev):s_cur]
        # maximal onset: give as many as possible to onset, but French avoids >2-consonant onsets
        # and s+consonant splits. Crude: onset = last min(2, len(gap)) consonants, except 'qu'/'gu' stay
        m = re.search(r'(qu|gu)$', gap)
        if m and len(gap) > 2:
            onset_len = 2
        else:
            onset_len = min(2, len(gap))
        bounds.append(s_cur - onset_len)
    bounds.append(len(w))
    return [w[bounds[k]:bounds[k+1]] for k in range(len(bounds)-1)]

if __name__ == '__main__':
    import sys
    files = ['/home/hatch/workspace/cipher-hunt/lanes/zeschau-seebach-1841/data/gutenberg-30513-tocqueville-t1.txt',
             '/home/hatch/workspace/cipher-hunt/lanes/zeschau-seebach-1841/data/gutenberg-30514-tocqueville-t2.txt']
    tok = Counter(); typ = Counter(); nwords = 0
    for f in files:
        for line in open(f, encoding='utf-8', errors='replace'):
            for word in re.findall(r"[A-Za-zàâäéèêëîïôöùûüyç']+", line.lower()):
                word = word.strip("'")
                if not word: continue
                nwords += 1
                for s in syllabify(word):
                    tok[s] += 1
    S = len(tok)
    total = sum(tok.values())
    top = tok.most_common()
    for K in (24, 72, 96, 176):
        cov = sum(c for _, c in top[:K]) / total
        print(f'top-{K} syllables cover {cov:.3f} of {total} syllable tokens')
    print(f'distinct syllable types S={S} over {nwords} words')
    print('top-20:', [s for s, _ in top[:20]])
