#!/usr/bin/env python3
"""Build the French word-pattern lexicon for the Seebach side fleet.

Source: Tocqueville t1+t2 (Gutenberg 30513/30514), era+register matched to the
1841 diplomatic cipher. Emits per distinct word: syllables (orthographic),
orthographic repetition pattern, phonetic-normalized syllables + pattern,
corpus frequency, syllable count. Indexes by (n_syllables, pattern).

Syllabifier choice: custom rule-based ORTHOGRAPHIC French syllabifier
(syllabify()). Rejected pyphen/fr hyphenation: hyphenation glues final mute-e
("premiere" -> "pre-miere", "parce" unsplit) whereas a syllabary cipher cuts
mute-e syllables ("pre-miE-re", units like "re","ere","ment","tion" in the
upstream UNITS inventory, data/upstream-syll.py). The cipher's encipherer also
spells by ear and cuts inconsistently, so the lexicon records a canonical
orthographic cut plus a phonetic-normalized cut; variant-tolerant matching is
the Pattern Matcher's job.
"""
import json, re, hashlib, random
from collections import Counter, defaultdict
from pathlib import Path

LANE = Path.home() / 'workspace/cipher-hunt/lanes/zeschau-seebach-1841'
DATA = LANE / 'data'
OUT = LANE / 'code' / 'side-wordpattern' / 'lexicon'
CORPUS_FILES = ['gutenberg-30513-tocqueville-t1.txt', 'gutenberg-30514-tocqueville-t2.txt']

# ---------------------------------------------------------------- syllabifier
VOWEL1 = set('aeiouyàâäéèêëîïôöùûüÿæœ')
# two/three-char consonant units (single onset consonants)
C2 = {'qu': 'q', 'ch': 'C', 'ph': 'f', 'th': 't', 'gn': 'G'}
# consonant pairs that stay together as an onset (maximal onset, French)
ONSET2 = {'bl', 'br', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr',
          'tr', 'vr', 'st', 'sp', 'sc'}
ONSET3TAIL = {'str', 'scr', 'spl', 'spr'}
NASALS = {'an', 'en', 'on', 'in', 'un', 'am', 'em', 'im', 'om',
          'ain', 'ein', 'oin'}
GLIDE_V = {'ien', 'ier', 'iez', 'iel', 'ail', 'eil', 'ouil', 'ui', 'ieu'}  # 1 nucleus
ACCENT_V = {'ée', 'ées', 'aie'}


def unitize(word):
    """Split word into units: list of (text, kind) with kind in {'V','C'}.
    V = vowel nucleus (incl. nasal vowels, diphthongs, glide+vowel)."""
    units = []
    i, n = 0, len(word)
    while i < n:
        # 3-char vowel units
        if word[i:i+3] in ('eau', 'oeu'):
            units.append((word[i:i+3], 'V')); i += 3; continue
        # consonant digraphs first (ch before h-deletion matters)
        c2 = word[i:i+2]
        if c2 in C2:
            units.append((c2, 'C')); i += 2; continue
        if c2 == 'gu' and i + 2 < n and word[i+2] in 'eéèêëiîï':
            units.append(('gu', 'C')); i += 2; continue
        if word[i] == 'h':
            i += 1; continue  # silent h: transparent
        # nasal vowels: nasal only if n/m NOT followed by vowel or n/m
        if c2 in NASALS:
            nxt = word[i+2:i+3]
            if nxt == '' or (nxt not in VOWEL1 and nxt not in 'nm'):
                units.append((c2, 'V')); i += 2; continue
            # oral: emit vowel alone, n/m becomes a consonant unit
            units.append((c2[0], 'V')); i += 1; continue
        # word-final -ille/-aille/-eille/-ouille/-eue: 1 nucleus
        # (checked before GLIDE_V so 'eille' isn't split as eil+le)
        if i > 0 and word[i:] in ('ille', 'aille', 'eille', 'ouille', 'eue'):
            units.append((word[i:], 'V')); i = n; continue
        # glide+vowel nuclei (check final 'uie' before 'ui' eats the i)
        if i > 0 and word[i:] == 'uie':
            units.append(('uie', 'V')); i = n; continue
        if word[i:i+3] in GLIDE_V or word[i:i+2] in GLIDE_V:
            t = word[i:i+3] if word[i:i+3] in GLIDE_V else word[i:i+2]
            units.append((t, 'V')); i += len(t); continue
        if c2 == 'ie' and (i + 2 == n or word[i:] == 'ies'):
            # word-final 'ie'/'ies' after consonant: vie, vies, étudie
            units.append((word[i:], 'V')); i = n; continue
        if c2 == 'ie' and i + 2 < n and word[i+2] not in VOWEL1 \
                and word[i+2:i+4] != 'rr':
            # pied, fier: 'ie' + consonant -> 1 nucleus (dierese matcher-side)
            units.append(('ie', 'V')); i += 2; continue
        if word[i:i+3] == 'ill' and i > 0 and word[i-1] in 'aeiou':
            # fille, -aille/-eille/-ouille handled via ail/eil/ouil above;
            # remaining 'ill' after vowel -> part of nucleus
            units.append(('ill', 'V')); i += 3; continue
        if word[i:i+2] in ACCENT_V or word[i:i+3] in ACCENT_V:
            t = word[i:i+3] if word[i:i+3] in ACCENT_V else word[i:i+2]
            units.append((t, 'V')); i += len(t); continue
        if c2 in ('ai', 'au', 'ei', 'eu', 'ou', 'oi', 'oe', 'au'):
            units.append((c2, 'V')); i += 2; continue
        if c2 == 'ie' and word[i+2:i+4] == 'rr':
            # pierre, guerre: 'ie' nucleus, 'rre' mute tail (orthographic cut)
            units.append(('ie', 'V')); i += 2; continue
        ch = word[i]
        if ch == 'y':
            prev_v = i > 0 and word[i-1] in VOWEL1
            nxt = word[i+1:i+2]
            nxt_v = nxt in VOWEL1
            if prev_v and nxt_v:
                units.append(('y', 'C'))          # pa-yer, ci-to-yen
            elif nxt_v:
                # initial y+vowel: yeux -> 1 nucleus; take y+vowel(s)
                j = i + 1
                while j < n and word[j] in VOWEL1:
                    j += 1
                units.append((word[i:j], 'V')); i = j; continue
            elif prev_v:
                units.append(('y', 'V'))          # pays -> pa-ys
            else:
                units.append(('y', 'C'))
            i += 1; continue
        if ch in VOWEL1:
            units.append((ch, 'V')); i += 1; continue
        units.append((ch, 'C')); i += 1
    return units


def _split_gap(cluster):
    """cluster: list of consonant-unit texts between two nuclei.
    Returns (coda_units, onset_units) per maximal-onset French rules."""
    if not cluster:
        return [], []                       # hiatus
    if len(cluster) == 1:
        if cluster[0] == 'x':
            return cluster, []              # ex-a-men
        return [], cluster                  # V-CV
    if len(cluster) == 2:
        if cluster[0] == cluster[1]:
            return [cluster[0]], [cluster[1]]   # per-sonne, ter-re
        if ''.join(cluster) in ONSET2:
            return [], cluster
        return [cluster[0]], [cluster[1]]
    coda, rest = [cluster[0]], cluster[1:]
    rc, ro = _split_gap(rest)
    return coda + rc, ro


def _mute_steal(syl_units):
    """syl_units: unit list of the pre-final syllable. Returns
    (kept_units, stolen_units) for the mute-e tail syllable."""
    cons = []
    for t, kind in reversed(syl_units):
        if kind == 'C':
            cons.append(t)
        else:
            break
    cons = cons[::-1]
    if len(cons) >= 3 and ''.join(cons[-3:]) in ONSET3TAIL:
        n = 2
    elif len(cons) >= 2 and ''.join(cons[-2:]) in ONSET2:
        n = 2
    elif cons:
        n = 1
    else:
        n = 0
    if n == 0:
        return syl_units, []
    return syl_units[:-n], syl_units[-n:]


def syllabify(word):
    """Orthographic French syllabification -> list of syllable strings.

    Maximal onset; mute final -e/-es takes its own syllable with a maximal
    onset steal ('ta-ble', 'pre-miE-re'); interior schwa kept as nucleus;
    -ier (masc) one nucleus, -iEre split iE|re (lane spec: 'pre-miE-re').
    """
    w = word.lower()
    units = unitize(w)
    # mute tail detection on units: final ('e',V) or ('e',V),('s',C)
    # preceded by a consonant unit, and core has another nucleus
    mute = []
    core = units
    if len(units) >= 2 and units[-1] == ('e', 'V') and units[-2][1] == 'C':
        mute, core = [('e', 'V')], units[:-1]
    elif (len(units) >= 3 and units[-1] == ('s', 'C')
          and units[-2] == ('e', 'V') and units[-3][1] == 'C'):
        mute, core = [('e', 'V'), ('s', 'C')], units[:-2]
    if mute and not any(k == 'V' for _, k in core):
        mute, core = [], units  # que, le, de: 1 syllable
    nuclei = [k for k, (t, kind) in enumerate(core) if kind == 'V']
    syls = []
    if not nuclei:
        if core:
            syls = [[t for t, _ in core]]
    else:
        cur = [t for t, _ in core[:nuclei[0]]]
        for ni, nk in enumerate(nuclei):
            cur.append(core[nk][0])
            nxt = nuclei[ni + 1] if ni + 1 < len(nuclei) else len(core)
            cluster = [t for t, kind in core[nk + 1:nxt]]
            if ni + 1 < len(nuclei):
                coda, onset = _split_gap(cluster)
                cur.extend(coda)
                syls.append(cur)
                cur = list(onset)
            else:
                cur.extend(cluster)
        syls.append(cur)
    if mute:
        kept, stolen = _mute_steal(unitize(''.join(syls[-1]))) if syls else ([], [])
        syls[-1] = [t for t, _ in kept]
        syls.append([t for t, _ in stolen] + [t for t, _ in mute])
    return [''.join(s) for s in syls if s]


# ------------------------------------------------------- phonetic normalization
_ACCT = str.maketrans({'à': 'a', 'â': 'a', 'ä': 'a', 'é': 'e', 'è': 'e',
                       'ê': 'e', 'ë': 'e', 'î': 'i', 'ï': 'i', 'ô': 'o',
                       'ö': 'o', 'ù': 'u', 'û': 'u', 'ü': 'u', 'ÿ': 'y',
                       'ç': 'c', 'æ': 'a', 'œ': 'o'})


def phon_syllable(s):
    """By-ear normalization of one orthographic syllable (documented classes)."""
    s = s.translate(_ACCT)
    s = s.replace('qu', 'k')
    s = s.replace('eue', 'eu')              # queue -> keu
    # final mute e dropped (before ai->e can forge one)
    if len(s) > 1 and s.endswith('e') and s[-2] not in 'aeiouy':
        s = s[:-1]
    s = s.replace('eau', 'o').replace('au', 'o')
    s = s.replace('ai', 'e').replace('ei', 'e')
    s = s.replace('ou', 'u').replace('oi', 'wa')
    s = s.replace('ch', 'sh').replace('ph', 'f').replace('th', 't')
    s = s.replace('gn', 'ny')
    s = re.sub(r'c([eiy])', r's\1', s)
    s = s.replace('c', 'k')
    s = s.replace('ç', 's')
    s = re.sub(r'g([eiy])', r'j\1', s)
    s = s.replace('en', 'an').replace('ain', 'in').replace('ein', 'in')
    s = re.sub(r'(.)\1', r'\1', s)          # by-ear: personne == persone
    return s


def pattern(seq):
    """First-occurrence repetition pattern, e.g. [a,b,a] -> 'ABA'."""
    seen, out, nxt = {}, [], 0
    for x in seq:
        if x not in seen:
            seen[x] = nxt; nxt += 1
        seen[x]  # noqa
        k = seen[x]
        out.append(chr(65 + k) if k < 26 else chr(97 + k - 26))
    return ''.join(out)


# ------------------------------------------------------------------ corpus load
def load_corpus():
    text = []
    for f in CORPUS_FILES:
        p = DATA / f
        t = p.read_text(encoding='utf-8')
        a = t.find('*** START OF THE PROJECT GUTENBERG EBOOK')
        b = t.find('*** END OF THE PROJECT GUTENBERG EBOOK')
        if a != -1 and b != -1:
            t = t[t.index('\n', a):b]
        text.append(t)
    text = '\n'.join(text)
    toks = re.findall(r"[A-Za-zÀÂÄÉÈÊËÎÏÔÖÙÛÜŸÇÆŒàâäéèêëîïôöùûüÿçæœ]+", text)
    toks = [w.lower() for w in toks]
    # split elisions: l'homme -> l, homme
    out = []
    for w in toks:
        out.extend(w.split("'"))
    return [w for w in out if w]


def main():
    words = load_corpus()
    freq = Counter(words)
    print(f'tokens={len(words)} distinct={len(freq)}')
    entries = []
    for w in sorted(freq, key=lambda w: (-freq[w], w)):
        syl = syllabify(w)
        ph = [phon_syllable(s) for s in syl]
        entries.append({
            'w': w, 'syl': syl, 'pat': pattern(syl),
            'phon': ph, 'ppat': pattern(ph),
            'freq': freq[w], 'nsyl': len(syl),
        })
    # indexes
    idx_o = defaultdict(list)
    idx_p = defaultdict(list)
    for e in entries:
        idx_o[f"{e['nsyl']}|{e['pat']}"].append(e['w'])
        idx_p[f"{e['nsyl']}|{e['ppat']}"].append(e['w'])
    index = {
        'orth': dict(idx_o), 'phon': dict(idx_p),
        'stats': {
            'entries': len(entries),
            'orth_keys': len(idx_o), 'phon_keys': len(idx_p),
            'tokens': len(words),
        },
    }
    OUT.mkdir(parents=True, exist_ok=True)
    with open(OUT / 'lexicon.jsonl', 'w', encoding='utf-8') as f:
        for e in entries:
            f.write(json.dumps(e, ensure_ascii=False) + '\n')
    with open(OUT / 'index.json', 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False)
    print(f"wrote {OUT/'lexicon.jsonl'} entries={len(entries)} "
          f"orth_keys={len(idx_o)} phon_keys={len(idx_p)}")
    # collision stats
    import statistics
    co = [len(v) for v in idx_o.values()]
    cp = [len(v) for v in idx_p.values()]
    print(f"orth key size: mean={statistics.mean(co):.1f} max={max(co)} "
          f"singleton={sum(1 for v in co if v==1)}")
    print(f"phon key size: mean={statistics.mean(cp):.1f} max={max(cp)} "
          f"singleton={sum(1 for v in cp if v==1)}")
    return entries, index


if __name__ == '__main__':
    main()
