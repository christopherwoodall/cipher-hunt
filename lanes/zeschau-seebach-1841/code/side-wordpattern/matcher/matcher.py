#!/usr/bin/env python3
"""Seebach side-fleet PATTERN MATCHER (coordinator session 2418001f).

Instrument: segment the cipher pair stream into words (segmenter STRUCT
boundary probs), compute each word's group-repetition pattern, look up
(n_syllables, pattern) in the French pattern lexicon (orth + phonetic),
filter by anchor consistency, rank by era frequency.

Writes ONLY to code/side-wordpattern/matcher/ (this dir).
Stdlib only.

Anchor statuses (marked everywhere):
  GT                 11=la 70=pre 82=m 34=i 29=er 40=e 46=que   (pencil cribs)
  PROV-STRONG        87=ce 64=qui 96=par 94=ne
  PROV              67=veut ; 06=verb-stem-CLASS (not a syllable -> unusable as anchor)
  LEAD              62=on 78=me 52=pas 24=en
Polyvalent groups (flag any proposal touching them): 06, 94, 52.
"""
import json, os, re, sys, collections

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
DATA = os.path.join(LANE, 'data')
LEXD = os.path.join(LANE, 'code', 'side-wordpattern', 'lexicon')
OUTD = os.path.join(LANE, 'code', 'side-wordpattern', 'matcher')
sys.path.insert(0, LEXD)
from build_lexicon import phon_syllable  # noqa: E402  (same normalizer as the lexicon)

# ---------------------------------------------------------------- anchors
# group -> (orth value, status)
ANCHORS = {
    '11': ('la', 'GT'), '70': ('pre', 'GT'), '82': ('m', 'GT'),
    '34': ('i', 'GT'), '29': ('er', 'GT'), '40': ('e', 'GT'), '46': ('que', 'GT'),
    '87': ('ce', 'PROV-STRONG'), '64': ('qui', 'PROV-STRONG'),
    '96': ('par', 'PROV-STRONG'), '94': ('ne', 'PROV-STRONG'),
    '67': ('veut', 'PROV'),
    '62': ('on', 'LEAD'), '78': ('me', 'LEAD'), '52': ('pas', 'LEAD'), '24': ('en', 'LEAD'),
}
# 06 = verb-stem CLASS (F25): not a single syllable value -> cannot anchor-match.
CLASS_ONLY = {'06': 'verb-stem class (PROV, unusable as syllable anchor)'}
POLYVALENT = {'06', '94', '52'}  # 06 /a~/ vs /ma~/ ; 94 ne/en islets ; 52 pas/se (K5)

TIERS = [  # cumulative
    ('T0', {'GT'}),
    ('T1', {'GT', 'PROV-STRONG'}),
    ('T2', {'GT', 'PROV-STRONG', 'PROV'}),
    ('T3', {'GT', 'PROV-STRONG', 'PROV', 'LEAD'}),
]

def pattern(seq):
    seen, out, nxt = {}, [], 0
    for x in seq:
        if x not in seen:
            seen[x] = nxt; nxt += 1
        k = seen[x]
        out.append(chr(65 + k) if k < 26 else chr(97 + k - 26))
    return ''.join(out)

VOWELS = set('aeiouy')

def variants(entry):
    """Yield (alphabet, tag, syllables) by-ear variants for one lexicon entry."""
    syl, ph = entry['syl'], entry['phon']
    outs = [('orth', 'V-orth', syl), ('phon', 'V-phon', ph)]
    # -ent kept vs dropped (par-lent -> parl): orth + phon
    if len(syl) >= 2 and syl[-1] == 'ent':
        outs.append(('orth', 'V-orth-entdrop', syl[:-2] + [syl[-2] + syl[-1]]))
    if len(ph) >= 2 and ph[-1] in ('ant', 'ent', 'int', 'ont'):
        outs.append(('phon', 'V-phon-entdrop', ph[:-2] + [ph[-2] + ph[-1]]))
    # -ier collapsed vs split (ou-blier -> ou-bli-er): orth + phon
    if len(syl) >= 2 and syl[-1].endswith('ier') and len(syl[-1]) > 3:
        outs.append(('orth', 'V-orth-iersplit',
                     syl[:-1] + [syl[-1][:-2], 'er']))
    if len(ph) >= 2 and ph[-1].endswith('ier') and len(ph[-1]) > 3:
        outs.append(('phon', 'V-phon-iersplit',
                     ph[:-1] + [ph[-1][:-2], 'er']))
    # pierre -> pier-re vs 1 syllable: final vowelless syllable merges (phon mostly)
    if len(ph) >= 2 and not (set(ph[-1]) & VOWELS):
        outs.append(('phon', 'V-phon-finalmerge', ph[:-2] + [ph[-2] + ph[-1]]))
    if len(syl) >= 2 and not (set(syl[-1]) & VOWELS):
        outs.append(('orth', 'V-orth-finalmerge', syl[:-2] + [syl[-2] + syl[-1]]))
    # NOTE: interior schwa kept vs dropped is already covered by orth-vs-phon
    # (phon_syllable drops schwa: petit -> p|tit, revenir -> r|v|nir).
    # NOTE: no CV-split variant (pre|mi -> pre|m|i): the ground-truth "premiere"
    # is written pre|m|i|er|e (5 groups) while the lexicon has pre|mi|e|re (4).
    # The 4 spec'd variants cannot express it; recorded as an instrument limit.
    return outs

# ---------------------------------------------------------------- stream load
def load_pairs():
    """Reproduce the pair stream exactly as code/crib_attack.py Phase A."""
    offsets = json.load(open(os.path.join(DATA, 'upstream-offsets.json')))
    pairs, odd_lines, off1 = [], 0, 0
    rawdigits = []
    for line in open(os.path.join(DATA, 'upstream-ct_R5005.txt')):
        line = line.strip()
        if not line:
            continue
        lid, digits = line.split()
        digits = re.sub(r'\D', '', digits)
        rawdigits.append(digits)
        if len(digits) % 2 == 1:
            odd_lines += 1
        off = offsets.get(lid, 0)
        if off == 1:
            off1 += 1
        d = digits[off:]
        for i in range(0, len(d) - 1, 2):
            pairs.append(d[i:i + 2])
    return pairs, odd_lines, off1, ''.join(rawdigits)

def main():
    os.makedirs(OUTD, exist_ok=True)
    pairs, odd_lines, off1, rawdigits = load_pairs()

    # --- byte checks -----------------------------------------------------
    assert len(pairs) == 1846, f'pairs={len(pairs)}'
    assert len(set(pairs)) == 96, f'distinct={len(set(pairs))}'
    assert odd_lines == 28 and off1 == 32, f'odd={odd_lines} off1={off1}'
    digfile = open(os.path.join(DATA, 'upstream-ct_R5005.digits.txt')).read()
    digfile_digits = re.sub(r'\D', '', digfile)
    assert digfile_digits == rawdigits, 'digits.txt mismatch vs ct_R5005.txt digits'
    assert len(digfile_digits) == 3764, f'digits={len(digfile_digits)}'
    # la|premiere span @1033-1038 must reproduce exactly
    span = pairs[1033:1039]
    assert span == ['11', '70', '82', '34', '29', '40'], f'span={span}'
    # segmenter checkpoint cross-check
    seg = json.load(open(os.path.join(LANE, 'code', 'crowd3', 'segmenter_results.json')))
    assert seg['la_premiere_checkpoint']['context_pairs_1028_1043'] == pairs[1028:1044]
    bc = seg['boundary_confidence_STRUCT']
    assert len(bc) == 1845
    assert abs(bc[1033] - 0.9365) < 1e-4, f'la|premiere boundary={bc[1033]}'
    print(f'[verify] pairs=1846 distinct=96 digits=3764 odd={odd_lines} off1={off1}')
    print(f'[verify] la|premiere @1033-1038 = {"-".join(span)} ; la|premiere boundary={bc[1033]:.4f}')

    # --- segmentation ----------------------------------------------------
    def segment(cut):
        words, start = [], 0
        for i in range(len(pairs) - 1):
            if bc[i] >= cut:
                words.append((start, i, pairs[start:i + 1]))
                start = i + 1
        words.append((start, len(pairs) - 1, pairs[start:]))
        return words

    words05 = segment(0.5)
    words07 = segment(0.7)
    print(f'[seg] cut>=0.5: {len(words05)} words ; cut>=0.7: {len(words07)} words')

    # --- lexicon + variant index -----------------------------------------
    lex = {}
    for line in open(os.path.join(LEXD, 'lexicon.jsonl')):
        e = json.loads(line)
        lex[e['w']] = e
    # (alphabet, n, pattern) -> [(word, tag, syllables)]
    vidx = collections.defaultdict(list)
    for w, e in lex.items():
        for alpha, tag, vsyl in variants(e):
            if not vsyl or any(not s for s in vsyl):
                continue
            vidx[(alpha, len(vsyl), pattern(vsyl))].append((w, tag, vsyl))
    n_var_entries = sum(len(v) for v in vidx.values())
    print(f'[lex] {len(lex)} words -> {n_var_entries} variant entries, {len(vidx)} keys')

    orth_anchor = {g: v for g, (v, s) in ANCHORS.items()}
    phon_anchor = {g: phon_syllable(v) for g, (v, s) in ANCHORS.items()}
    tier_groups = {}
    for tname, tstatus in TIERS:
        tier_groups[tname] = {g for g, (v, s) in ANCHORS.items() if s in tstatus}

    # The inner loop above lost the word name; redo cleanly.
    def match_word2(groups):
        n = len(groups)
        cpat = pattern(groups)
        anchored_pos = {i: g for i, g in enumerate(groups) if g in ANCHORS}
        out = {}
        for tname, tstatus in TIERS:
            pos = {i: g for i, g in anchored_pos.items() if ANCHORS[g][1] in tstatus}
            cand = {}  # word -> best (freq, tag, vsyl, alpha, ev)
            for alpha in ('orth', 'phon'):
                aval = orth_anchor if alpha == 'orth' else phon_anchor
                for wname, tag, vsyl in vidx.get((alpha, n, cpat), []):
                    ev = []
                    ok = True
                    for i, g in pos.items():
                        if vsyl[i] != aval[g]:
                            ok = False
                            break
                        ev.append({'pos': i, 'group': g,
                                   'anchor_value': aval[g],
                                   'anchor_status': ANCHORS[g][1],
                                   'cand_syll': vsyl[i]})
                    if not ok:
                        continue
                    e = lex[wname]
                    prev = cand.get(wname)
                    if prev is None or e['freq'] > prev[0]:
                        cand[wname] = (e['freq'], tag, list(vsyl), alpha, ev)
            ranked = sorted(cand.items(), key=lambda kv: (-kv[1][0], kv[0]))
            out[tname] = {'n_anchored': len(pos),
                          'survivors': [{'word': w, 'freq': f, 'variant': tag,
                                         'syllables': vs, 'alphabet': al,
                                         'anchor_evidence': ev}
                                        for w, (f, tag, vs, al, ev) in ranked]}
        return out

    # --- word selection --------------------------------------------------
    anchor_groups = set(ANCHORS)  # 06 excluded (class-only)
    targets = seg['crib_drag_targets_STRUCT']
    print(f'[targets] {len(targets)} segmenter crib-drag targets')

    def word_record(s, e_idx, groups, cut, source):
        cpat = pattern(groups)
        tiers = match_word2(groups)
        # polyvalence flag
        pv = sorted(set(groups) & POLYVALENT)
        # trivial anchor restatement: 1-group anchored words
        trivial = (len(groups) == 1 and groups[0] in ANCHORS)
        # promotion evaluation at T3 (all constraints)
        t3 = tiers['T3']['survivors']
        t0 = tiers['T0']['survivors']
        prop, status = None, 'LEAD-or-null'
        n_anch_t3 = tiers['T3']['n_anchored']
        if trivial:
            status = 'ANCHOR-RESTATEMENT'
        elif not t3:
            status = 'NULL'
        elif len(t3) == 1:
            prop, status = t3[0], 'CRIB-PROPOSAL-unique'
        elif (len(t3) >= 2 and t3[0]['freq'] >= 2 * t3[1]['freq']
                and n_anch_t3 >= 2):
            prop, status = t3[0], 'CRIB-PROPOSAL-freqgap+2anchors'
        else:
            status = 'LEAD'
        # ground-truth-only survival note
        t0_top = [s_['word'] for s_ in t0[:3]]
        rec = {
            'span': [s, e_idx], 'groups': groups, 'n': len(groups),
            'pattern': cpat, 'cut': cut, 'source': source,
            'polyvalent_groups': pv,
            'tiers': {t: {'n_anchored': v['n_anchored'],
                          'n_survivors': len(v['survivors']),
                          'top3': [x['word'] for x in v['survivors'][:3]]}
                      for t, v in tiers.items()},
            'status': status,
            'proposal': prop,
            'leads_top10': t3[:10] if status == 'LEAD' else [],
            'T0_top3': t0_top,
        }
        return rec

    # A) the 25 segmenter targets (as given spans), at both cuts' context
    results = {'A_targets': [], 'B_anchored_words_05': [], 'B_anchored_words_07': []}
    for t in targets:
        s, e_idx, groups = t['start_pair'], t['end_pair'], t['groups']
        assert pairs[s:e_idx + 1] == groups, f'target span mismatch @{s}'
        results['A_targets'].append(word_record(s, e_idx, groups, 'given-span', 'segmenter-target'))

    # B) all words (both cuts) containing >=1 anchored group
    for cut, words, key in ((0.5, words05, 'B_anchored_words_05'),
                            (0.7, words07, 'B_anchored_words_07')):
        for s, e_idx, groups in words:
            if any(g in anchor_groups for g in groups):
                results[key].append(word_record(s, e_idx, groups, cut, 'anchor-sweep'))
        print(f'[sweep] cut {cut}: {len(results[key])} words with >=1 anchored group')

    # --- summarize -------------------------------------------------------
    def summarize(recs):
        props = [r for r in recs if r['status'].startswith('CRIB-PROPOSAL')]
        leads = [r for r in recs if r['status'] == 'LEAD']
        nulls = [r for r in recs if r['status'] == 'NULL']
        triv = [r for r in recs if r['status'] == 'ANCHOR-RESTATEMENT']
        return props, leads, nulls, triv

    summary = {}
    for key, recs in results.items():
        p, l, n, t = summarize(recs)
        summary[key] = {'n_words': len(recs), 'proposals': len(p),
                        'leads': len(l), 'nulls': len(n), 'restatements': len(t)}
    print('[summary]', json.dumps(summary))

    out = {
        'meta': {
            'pairs': 1846, 'distinct_groups': 96, 'digits': 3764,
            'byte_checks': 'pairs==1846, distinct==96, digits.txt==3764, '
                           'odd_lines==28, off1==32, la|premiere span @1033-1038 '
                           '== 11-70-82-34-29-40, segmenter checkpoint pairs '
                           '1028-1043 match, la|premiere boundary bc[1033]==0.9365',
            'polyvalence_verdict': 'PENDING - all proposals marked '
                                   'PROVISIONAL-PENDING-POLYVALENCE-VERDICT',
            'variants': ['V-orth', 'V-phon', 'V-orth-entdrop', 'V-phon-entdrop',
                         'V-orth-iersplit', 'V-phon-iersplit',
                         'V-phon-finalmerge', 'V-orth-finalmerge'],
            'anchor_statuses': {g: s for g, (v, s) in ANCHORS.items()},
            'class_only': CLASS_ONLY,
            'instrument_limits': [
                'no CV-split variant: ground-truth "premiere" written '
                'pre|m|i|er|e (5 groups, ABCDE) vs lexicon pre|mi|e|re '
                '(4, ABCD) cannot match by (n,pattern)',
                'interior schwa kept/dropped covered by orth-vs-phon '
                '(phon_syllable drops schwa: petit->p|tit)',
                'promotion bar: unique survivor, or top freq >=2x next AND '
                '>=2 anchor-fixed positions',
            ],
        },
        'summary': summary,
        'results': results,
    }
    # proposals get the pending-polyvalence stamp
    for recs in results.values():
        for r in recs:
            if r['status'].startswith('CRIB-PROPOSAL'):
                r['proposal']['status_note'] = 'PROVISIONAL-PENDING-POLYVALENCE-VERDICT'
    with open(os.path.join(OUTD, 'match_results.json'), 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print('[wrote] match_results.json')

    # console detail for the report
    for key in ('A_targets', 'B_anchored_words_05'):
        print(f'=== {key} ===')
        for r in results[key]:
            if r['status'].startswith('CRIB-PROPOSAL') or r['status'] == 'LEAD':
                p = r['proposal']
                tag = p['word'] if p else r['tiers']['T3']['top3'][:4]
                print(f"@{r['span'][0]}-{r['span'][1]} {'-'.join(r['groups'])} "
                      f"pat={r['pattern']} n_anch_T3={r['tiers']['T3']['n_anchored']} "
                      f"pv={r['polyvalent_groups']} {r['status']} -> {tag}")

if __name__ == '__main__':
    main()
