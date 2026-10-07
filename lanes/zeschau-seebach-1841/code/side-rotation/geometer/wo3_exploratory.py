#!/usr/bin/env python3
"""GEOMETER WO3-E (POST-HOC, not pre-registered) — boundary mapping.

Q: can ANY column process be both (i) recoverable by Jaccard-k12 contact
clustering (ARI>=0.5) and (ii) as soft as observed? Two extreme behaviors:
  B6 DETERMINISTIC: column = t mod 3 strictly (maximal column signal).
  B7 STRONG-SOFT: p_same=0.05, p_next=0.80, p_prev=0.15 (stronger than B2).
If even B6 fails ARI>=0.5, arbitrary columns are unrecoverable in principle.
If B6 recovers but B7 doesn't, recoverability needs near-determinism, which
contradicts the observed soft rotation (self-trans exist, cycle 1.35-1.52x).
Reuses wo3_clerk_sim.py machinery. 20 replicates, T=1847.
"""
import sys, os, math, random, re, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wo3_clerk_sim as W

def encipher_ext(stream_sylls, table, var_of, cell, nrows, behavior, rng):
    if behavior in ('B6', 'B7'):
        cols_out, gids_out = [], []
        c_prev = rng.randrange(3)
        for t, s in enumerate(stream_sylls):
            variants = var_of.get(s)
            if not variants:
                continue
            vcols = {c: g for g, c in variants}
            if behavior == 'B6':
                c = t % 3
            else:
                r = rng.random()
                c = c_prev if r < 0.05 else ((c_prev + 1) % 3 if r < 0.85 else (c_prev + 2) % 3)
                c_prev = c
            g = vcols.get(c)
            if g is None:
                for d in (1, 2):
                    for cc in ((c + d) % 3, (c - d) % 3):
                        if cc in vcols:
                            g, c = vcols[cc], cc
                            break
                    if g:
                        break
            cols_out.append(c)
            gids_out.append(g)
        return cols_out, gids_out
    raise ValueError(behavior)

def main():
    text = W.load_text()
    words = re.findall(r"[a-zàâäéèêëîïôöùûüç']+", text)
    words = [w for w in words if w.strip("'")]
    sylls = []
    for w in words:
        sylls.extend(W.syllabify(w.strip("'")))
    freq = collections.Counter(sylls)
    out = {}
    for b in ('B6', 'B7'):
        aris, dm1, dm2, dm3, tm2 = [], [], [], [], []
        for rep in range(20):
            rng = random.Random(7000 + {'B6':0,'B7':1}[b] * 100 + rep)
            table, var_of, cell, nrows = W.build_table(rng, freq)
            start = rng.randrange(0, max(1, len(sylls) - W.T_STREAM - 1))
            cols_out, gids_out = encipher_ext(sylls[start:start + W.T_STREAM],
                                              table, var_of, cell, nrows, b, rng)
            tm = W.true_measures(cols_out)
            block = W.derive_phases(gids_out)
            dm = W.derived_measures(gids_out, block)
            gs = sorted(set(gids_out))
            a = W.ari([table[g][1] for g in gs], [block[g] for g in gs])
            aris.append(a); dm1.append(dm['M1']); dm2.append(dm['M2_z']); dm3.append(dm['M3'])
            tm2.append(tm['M2_z'])
        med = lambda v: sorted(v)[10]
        out[b] = {'ARI_med': round(med(aris), 3), 'derived_M1_med': round(med(dm1), 1),
                  'derived_z_med': round(med(dm2), 2), 'derived_M3_med': round(med(dm3), 3),
                  'true_z_med': round(med(tm2), 2)}
        print(b, out[b])
    import json
    json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                     'wo3_exploratory.json'), 'w'), indent=1)

if __name__ == '__main__':
    main()
