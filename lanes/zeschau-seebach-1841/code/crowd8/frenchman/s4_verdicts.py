#!/usr/bin/env python3
"""Round-8 FRENCHMAN step 4: final quantified verdicts -> results.json."""
import json, math, re, glob, os, collections
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import util
from util import PAIRS, N, UNI, GT, followers, predecessors, positions

def log_tail(N_, p_, k_, upper=True):
    ls = []
    rng = range(k_, N_+1) if upper else range(0, k_+1)
    for k in rng:
        ls.append(math.lgamma(N_+1)-math.lgamma(k+1)-math.lgamma(N_-k+1)
                  + k*math.log(p_)+(N_-k)*math.log(1-p_))
    m = max(ls)
    return math.exp(m)*math.fsum(math.exp(l-m) for l in ls)

CORP = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-period/corpus')
def tok_elision(text):
    text = text.replace('-\n','').replace('-\r\n','').lower()
    text = re.sub(r"[’‘`]", "'", text)
    text = re.sub(r"\b([a-zàâäéèêëîïôöùûüçœæ]+)'([a-zàâäéèêëîïôöùûüçœæ]+)", r"\1' \2", text)
    return re.findall(r"[a-zàâäéèêëîïôöùûüçœæ]+'?|[a-zàâäéèêëîïôöùûüçœæ]+", text)
D = []
for f in sorted(glob.glob(os.path.join(CORP, '*.txt'))):
    if os.path.basename(f) in ('PROVENANCE.md','harvest-log.txt'): continue
    D.extend(tok_elision(open(f, encoding='utf-8', errors='replace').read()))
ND = len(D); DU = collections.Counter(D)
p_l = DU["l'"]/ND

out = {'N_pairs': N, 'diplo_tokens': ND, 'diplo_P_l': round(p_l, 6)}

# 1. 93-alone rate kill (diplo)
out['kill_93_alone'] = {'n': UNI[93], 'E_diplo': round(p_l*N, 2),
    'P_le_14': log_tail(N, p_l, UNI[93], False)}
# 2. M_hom {93,8}
n_hom = UNI[93]+UNI[8]
out['M_hom_93_8'] = {'n': n_hom, 'E_diplo': round(p_l*N, 2),
    'P_le': log_tail(N, p_l, n_hom, False), 'P_ge': log_tail(N, p_l, n_hom, True)}
# ratio test vs que (46 GT)
p_que = DU['que']/ND
n61 = n_hom+UNI[46]; p_star = p_l/(p_l+p_que)
out['ratio_test'] = {'cipher_l': n_hom, 'cipher_que': UNI[46],
    'diplo_P_l_over_que': round(p_l/p_que, 3),
    'P_le_binom': log_tail(n61, p_star, n_hom, False)}
# 3-partite kill: {93,8,3}
out['kill_3cell'] = {'n': n_hom+UNI[3], 'P_ge': log_tail(N, p_l, n_hom+UNI[3], True)}
# runner-up {8,14}
n_814 = UNI[8]+UNI[14]
out['runnerup_8_14'] = {'n': n_814, 'P_le': log_tail(N, p_l, n_814, False),
    'P_ge': log_tail(N, p_l, n_814, True)}

# 3. L_B: qu'on vs qu'il likelihood ratio on 46->62=0
p_quon = sum(1 for i in range(ND-2) if D[i]=="qu'" and D[i+1]=='on')/ND
p_quil = sum(1 for i in range(ND-2) if D[i]=="qu'" and D[i+1]=='il')/ND
E_quon, E_quil = p_quon*N, p_quil*N
P0_on = math.exp(-E_quon); P0_il = math.exp(-E_quil)
out['L_B_qu'] = {'E_quon': round(E_quon,2), 'E_quil': round(E_quil,2),
    'P0_given_on': round(P0_on,4), 'P0_given_il': round(P0_il,5),
    'LR_on_over_il': round(P0_on/P0_il, 1),
    'obs_46_to_62': sum(1 for i in range(N-1) if PAIRS[i]==46 and PAIRS[i+1]==62)}
# v8-slice robustness of the ratio
Tv8 = tok_elision(open(os.path.join(CORP,'nesselrode-v8.txt'), encoding='utf-8', errors='replace').read())
n8 = len(Tv8)
n_qil_v8 = sum(1 for i in range(n8-2) if Tv8[i]=="qu'" and Tv8[i+1]=='il')
n_qon_v8 = sum(1 for i in range(n8-2) if Tv8[i]=="qu'" and Tv8[i+1]=='on')
r_v8 = n_qil_v8/max(1, n_qon_v8)
out['L_B_qu']['quil_over_quon_v8'] = round(r_v8, 2)
out['L_B_qu']['quil_over_quon_full'] = round(p_quil/p_quon, 2)

# 4. L_A: l'on chain
n_l62 = sum(1 for i in range(N-1) if PAIRS[i] in (93,8) and PAIRS[i+1]==62)
n_lil = sum(1 for i in range(ND-1) if D[i]=="l'" and D[i+1]=='il')
n_lon = sum(1 for i in range(ND-1) if D[i]=="l'" and D[i+1]=='on')
out['L_A_lon'] = {'cipher_93or8_to_62': n_l62, 'n62': UNI[62],
    'diplo_l_il': n_lil, 'diplo_l_on': n_lon,
    'E_to62_given_on_full': round(n_lon/DU['on']*UNI[62], 2)}
# 5. 93->52 adverse windows
out['adverse_93_to_52'] = {'n': sum(1 for i in range(N-1) if PAIRS[i]==93 and PAIRS[i+1]==52),
    'at': [i for i in range(N-1) if PAIRS[i]==93 and PAIRS[i+1]==52]}
# 6. 06='ent' iff pre=82 islet
islet = [i for i in range(N-1) if PAIRS[i]==82 and PAIRS[i+1]==6]
out['islet_06_ent'] = {'windows': islet, 'n': len(islet)}
# 7. gouvernement diplo rate
n_gouv = DU['gouvernement']
out['gouvernement'] = {'diplo_n': n_gouv, 'P': n_gouv/ND,
    'E_per_1400w': round(n_gouv/ND*1400, 2),
    'P_left_le': round(sum(1 for i in range(1,ND) if D[i]=='gouvernement' and D[i-1]=='le')/n_gouv, 3)}

json.dump(out, open('results.json','w'), indent=1)
print(json.dumps(out, indent=1))
