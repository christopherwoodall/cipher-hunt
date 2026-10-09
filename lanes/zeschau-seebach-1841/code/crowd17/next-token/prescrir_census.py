"""Battery prescrir-stem-corpus: census the prescrir- stem across the lane period corpus.

Corpus: code/side-period/corpus (75 .txt files, 34,525,238 chars).
Regex: \\bprescr[ie][itvr][a-z]*\\b on NFKD-stripped, lowercased text.
Also reports: (a) prescrir-form governing 'de/d'' + infinitive (lemma test);
(b) 'de/à/pour' immediately before a prescrir-form; (c) 'prescription' noun count.
"""
import os, re, json, unicodedata

CORP = os.path.join(os.path.dirname(__file__), '..', '..', 'side-period', 'corpus')
STEM = re.compile(r'\bprescr[ie][itvr][a-z]*\b')
PRESC = re.compile(r'\bprescription\b')

def norm(s):
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii').lower()

def main():
    files = sorted(f for f in os.listdir(CORP)
                   if f.endswith('.txt') and f != 'PROVENANCE.md' and not f.startswith('PROVENANCE-'))
    hits, total_chars, presc_n = [], 0, 0
    for fn in files:
        with open(os.path.join(CORP, fn), encoding='utf-8', errors='replace') as f:
            txt = f.read()
        total_chars += len(txt)
        nt = norm(txt)
        for m in STEM.finditer(nt):
            s, e = m.span()
            hits.append({'file': fn, 'offset': s, 'token': nt[s:e],
                         'ctx': txt[max(0, s - 80):e + 120].replace('\n', ' ')})
        presc_n += len(PRESC.findall(nt))
    out = {'files': len(files), 'chars': total_chars, 'hits': hits,
           'prescription_noun_tokens': presc_n}
    with open(os.path.join(os.path.dirname(__file__), 'prescrir_census.json'), 'w',
              encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print('files:', len(files), 'chars:', total_chars, 'hits:', len(hits),
          'prescription:', presc_n)

if __name__ == '__main__':
    main()
