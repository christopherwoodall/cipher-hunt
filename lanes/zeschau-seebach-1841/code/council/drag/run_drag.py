#!/usr/bin/env python3
"""Systematic crib-drag runner (systematic-drag.md §§2-4).

Steps:
  1. POSITIVE CONTROL: "par ce que" must hit @224/@952/@1526 (else: broken).
  2. Main drag over the inventory (primary bar + pre-registered relaxed
     sensitivity variant -> veto_sensitive flags).
  3. Nulls: 20 seeded shuffled-stream replicates (parallel) + ~100-phrase
     anachronistic decoy inventory vs the real stream.
Outputs: drag_hits.json, null_report.json. All runs seeded + re-derivable.
"""
import json
import math
import os
import random
import sys
import time
from multiprocessing import Pool

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (load_stream, build_oracle, is_anchor_group, norm)

HERE = os.path.dirname(os.path.abspath(__file__))

# ------------------------------------------------------------- decoys
# ~100 anachronistic French phrases (post-1841 coinages / 20th-c formulae).
# Any hit here is a pure false positive calibrating bar looseness.
DECOYS = [
    "guerre froide", "société des nations", "organisation des nations unies",
    "rideau de fer", "mur de berlin", "bloc soviétique", "tiers monde",
    "décolonisation", "guerre du vietnam", "crise de cuba", "plan marshall",
    "guerre mondiale", "seconde guerre mondiale", "bombe atomique",
    "arme nucléaire", "dissuasion nucléaire", "course aux armements",
    "détente", "glasnost", "perestroïka", "pacte de varsovie",
    "communisme", "fascisme", "nazisme", "totalitarisme", "génocide",
    "crimes contre l'humanité", "tribunal de nuremberg",
    "déclaration universelle des droits de l'homme", "convention de genève",
    "croix rouge", "télévision", "internet", "ordinateur", "satellite artificiel",
    "premier homme sur la lune", "fusée spatiale", "énergie nucléaire",
    "réchauffement climatique", "couche d'ozone", "biodiversité",
    "développement durable", "mondialisation", "multinationales",
    "fonds monétaire international", "banque mondiale", "protocole de kyoto",
    "accord de paris", "union européenne", "communauté européenne",
    "brexit", "ligue arabe", "union africaine", "pandémie de covid",
    "vaccin à arn messager", "téléphone portable", "voiture automobile",
    "avion de ligne", "sous-marin nucléaire", "porte-avions",
    "guerre des étoiles", "intelligence artificielle", "réseaux sociaux",
    "téléphone intelligent", "voiture électrique", "énergie solaire",
    "éoliennes", "centrale nucléaire", "accident de tchernobyl",
    "chute du mur", "fin de la guerre froide", "nouvel ordre mondial",
    "conflit israélo-palestinien", "printemps arabe", "guerre en ukraine",
    "annexion de la crimée", "sanctions économiques", "embargo pétrolier",
    "choc pétrolier", "crise des subprimes", "dette souveraine",
    "austérité budgétaire", "relance keynésienne", "revenu universel",
    "salaire minimum", "congés payés", "sécurité sociale",
    "assurance maladie", "retraite par répartition", "syndicats ouvriers",
    "droit de grève", "négociation collective", "code du travail",
    "discrimination positive", "parité hommes femmes", "mariage pour tous",
    "adoption homoparentale", "fin de vie", "euthanasie",
    "don d'organes", "procréation médicalement assistée",
    "changement climatique", "transition énergétique", "taxe carbone",
    "commerce équitable", "agriculture biologique", "ogm",
    "nanotechnologies", "biotechnologies", "clonage",
    "génome humain", "thérapie génique", "intelligence économique",
    "guerre commerciale", "dumping social", "paradis fiscaux",
    "évasion fiscale", "blanchiment d'argent", "financement du terrorisme",
    "état islamique", "printemps de prague", "solidarnosc",
]

# ---------------------------------------------------------------- scoring
def score_alignment(syls, pos, oracle_arr, stream):
    matches, anchored, contra = 0, False, 0
    align = []
    for i, syl in enumerate(syls):
        g = stream[pos + i]
        v = oracle_arr[pos + i]
        if v is None:
            align.append([syl, g, None, 'neutral'])
            continue
        if v == syl:
            matches += 1
            if is_anchor_group(g):
                anchored = True
            align.append([syl, g, v, 'match'])
        else:
            contra += 1
            align.append([syl, g, v, 'contra'])
    return matches, anchored, contra, align


def drag_stream(stream, oracle_arr, phrases, relaxed_ok=True):
    """Run the full drag; return (primary_hits, veto_hits)."""
    n = len(stream)
    primary, veto = [], []
    for ph in phrases:
        freq = ph.get('freq', 0)
        for var in ph['variants']:
            syls = var['syls']
            k = len(syls)
            if k < 3:
                continue
            need = max(2, math.ceil(k / 2))
            for pos in range(n - k + 1):
                matches, anchored, contra, align = score_alignment(
                    syls, pos, oracle_arr, stream)
                if matches < need or not anchored:
                    continue
                rank = matches * math.log(1 + freq)
                hit = {'phrase': ph['phrase'], 'variant': var['name'],
                       'pos': pos, 'k': k, 'matches': matches,
                       'contra': contra, 'anchored': anchored,
                       'rank': rank, 'freq': freq,
                       'groups': stream[pos:pos + k], 'align': align}
                if contra == 0:
                    primary.append(hit)
                elif relaxed_ok and contra * 5 <= matches:
                    hit['veto_sensitive'] = True
                    veto.append(hit)
    primary.sort(key=lambda h: (-h['rank'], -h['k']))
    veto.sort(key=lambda h: (-h['rank'], -h['k']))
    return primary, veto


def _shuffle_job(args):
    s, phrases = args
    rng = random.Random(1000 + s)
    stream = load_stream()
    shuf = rng.sample(stream, len(stream))
    oracle_arr = build_oracle(shuf)
    primary, _ = drag_stream(shuf, oracle_arr, phrases, relaxed_ok=False)
    return len(primary)


def main():
    t0 = time.time()
    stream = load_stream()
    oracle_arr = build_oracle(stream)
    inv = json.load(open(os.path.join(HERE, 'inventory.json')))
    phrases = inv['phrases']
    print(f'stream: {len(stream)} groups; inventory: {len(phrases)} phrases',
          flush=True)

    # ---- 1. positive control
    pc = [p for p in phrases if norm(p['phrase']) == 'par ce que']
    assert pc, 'positive-control phrase "par ce que" missing from inventory'
    primary_pc, _ = drag_stream(stream, oracle_arr, pc, relaxed_ok=False)
    pc_pos = sorted(h['pos'] for h in primary_pc)
    print(f'positive control "par ce que": hits at {pc_pos}', flush=True)
    ok = all(x in pc_pos for x in (224, 952, 1526))
    print('POSITIVE CONTROL:', 'PASS' if ok else 'FAIL', flush=True)
    if not ok:
        print('implementation broken: fix before proceeding', flush=True)
        sys.exit(2)

    # ---- 2. main drag
    t1 = time.time()
    primary, veto = drag_stream(stream, oracle_arr, phrases, relaxed_ok=True)
    print(f'main drag: {len(primary)} primary hits, '
          f'{len(veto)} veto-sensitive ({time.time()-t1:.1f}s)', flush=True)

    with open(os.path.join(HERE, 'drag_hits.json'), 'w') as f:
        json.dump({'meta': {
            'stream': 'repaired_offsets.json (F32), 1847 pairs / 96 groups',
            'n_phrases': len(phrases),
            'positive_control': {'phrase': 'par ce que',
                                 'expected': [224, 952, 1526],
                                 'found': pc_pos, 'pass': ok},
            'bar': 'k>=3, contra==0, matches>=max(2,ceil(k/2)), anchored; '
                   'relaxed: contra*5<=matches -> veto_sensitive',
        }, 'primary': primary, 'veto_sensitive': veto}, f,
            ensure_ascii=False)

    # ---- 3a. shuffle null (20 seeded replicates, parallel)
    t2 = time.time()
    with Pool(2) as pool:
        h_s = pool.map(_shuffle_job, [(s, phrases) for s in range(20)])
    print(f'shuffle null hits per replicate: {h_s} ({time.time()-t2:.1f}s)',
          flush=True)
    h_real = len(primary)
    fdr = sum(h_s) / 20 / max(1, h_real)
    beats_all = h_real > max(h_s) if h_s else False
    print(f'FDR estimate: {fdr:.3f}; real beats all 20 shuffles: {beats_all}',
          flush=True)

    # ---- 3b. decoy null
    from common import tok_elision, phrase_variants
    decoy_phrases = []
    for d in DECOYS:
        toks = tok_elision(d)
        if not toks:
            continue
        decoy_phrases.append({
            'phrase': d, 'tokens': toks, 'freq': 1, 'core_freq': 0,
            'source': 'decoy',
            'variants': [{'name': n_, 'syls': s}
                         for n_, s in phrase_variants(toks)]})
    d_primary, _ = drag_stream(stream, oracle_arr, decoy_phrases,
                               relaxed_ok=False)
    print(f'decoy null: {len(d_primary)} hits on {len(decoy_phrases)} '
          f'anachronistic phrases', flush=True)
    for h in d_primary[:10]:
        print(f"  decoy hit: {h['phrase']!r} @{h['pos']} "
              f"m={h['matches']} k={h['k']}", flush=True)

    with open(os.path.join(HERE, 'null_report.json'), 'w') as f:
        json.dump({'shuffle_replicates': h_s,
                   'shuffle_seeds': [1000 + s for s in range(20)],
                   'h_real': h_real, 'fdr_estimate': fdr,
                   'real_beats_all_shuffles': beats_all,
                   'decoy_hits': len(d_primary),
                   'decoy_n': len(decoy_phrases),
                   'decoy_hit_detail': d_primary[:25]}, f, ensure_ascii=False)
    print(f'done in {time.time()-t0:.1f}s', flush=True)


if __name__ == '__main__':
    main()
