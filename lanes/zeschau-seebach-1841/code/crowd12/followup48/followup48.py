#!/usr/bin/env python3
"""followup48 round 12: ML-1 (@1078 infinitive-ID), ML-2 (pre=12 class),
@863 second de-frame. Runs AFTER PREREG.md was written.
Repaired 1,847-pair stream. Byte-exact positions (0-based).
"""
import json, re, sys
from pathlib import Path
from collections import Counter
LANE = Path.home() / 'workspace/cipher-hunt/lanes/zeschau-seebach-1841'
sys.path.insert(0, str(LANE / 'code/crowd7/keystruct'))
sys.path.insert(0, str(LANE / 'code/crowd9/frenchman'))
from aliasing import load_stream
import corpus9

PAIRS = load_stream()
N = len(PAIRS)
assert N == 1847, N
print('N =', N)

# ---------------- era corpus ----------------
toks = corpus9.load('primary')          # v8 + levant (assert v8 token count)
tv8 = corpus9.tokenize_elision(
    open(LANE / 'code/side-period/corpus/nesselrode-v8.txt',
         encoding='utf-8', errors='replace').read())
assert len(tv8) == 92594, len(tv8)
tri = Counter(zip(tv8[:-2], tv8[1:-1], tv8[2:]))
bi = Counter(zip(tv8[:-1], tv8[1:]))
uni = Counter(tv8)
print('v8 tokens:', len(tv8))

# ---------------- by-ear syllabifier v1.2 verbatim ----------------
VOWELS = set("aàâäeéèêëiîïoôöuùûüy")
def byear_syllables(word):
    if "'" in word and len(word) <= 3:
        return [word]
    vs = [i for i, ch in enumerate(word) if ch in VOWELS]
    if not vs:
        return [word]
    nuclei = []
    for i in vs:
        if nuclei and i == nuclei[-1][-1] + 1:
            nuclei[-1].append(i)
        else:
            nuclei.append([i])
    nuc = [(n_[0], n_[-1]) for n_ in nuclei]
    cuts = []
    for (a0, a1), (b0, b1) in zip(nuc[:-1], nuc[1:]):
        c = b0 - a1 - 1
        cuts.append(a1 + 2 if c >= 1 else a1 + 1)
    parts, start = [], 0
    for cut in cuts:
        parts.append(word[start:cut])
        start = cut
    parts.append(word[start:])
    return [p for p in parts if p]
def first_syl(w):
    s = byear_syllables(w); return s[0] if s else w
def second_syl(w):
    s = byear_syllables(w); return s[1] if len(s) > 1 else None

# infinitive classification rule (pre-registered): ends er|ir|re|oir, not in NOUN-STOP
NOUN_STOP = {"france","prusse","grèce","grece","syrie","russie","guerre","paix",
  "cour","loi","mer","terre","pierre","lumière","lumiere","manière","maniere",
  "prière","priere","rivière","riviere","dernière","derniere","première","premiere",
  "affaire","misère","misere","colère","colere","misere","bannière","banniere"}
def is_inf(w):
    return bool(re.search(r'(er|ir|re|oir)$', w)) and w not in NOUN_STOP

res = {"N": N, "ml1": {}, "ml2": {}, "at863": {}}

# ================= ML-1a: "de [article] [INF]" rates =================
de_art_inf = {}
for art in ["le", "la", "l'", "les"]:
    hits = [(i, tv8[i+2]) for i in range(len(tv8)-2)
            if tv8[i]=="de" and tv8[i+1]==art and is_inf(tv8[i+2])]
    mono = [x for _,x in hits if len(byear_syllables(x))==1]
    de_art_inf[art] = {
        "n": len(hits),
        "topX": Counter(x for _,x in hits).most_common(12),
        "mono_share": round(len(mono)/len(hits),4) if hits else None,
        "mono_list": sorted(set(mono)),
    }
res["ml1"]["ML-1a_de_article_INF"] = de_art_inf
print(json.dumps({a: (v["n"], v["mono_share"], v["mono_list"]) for a,v in de_art_inf.items()}, ensure_ascii=False))

# ================= ML-1b: infinitives with by-ear 2nd syl "qui" =================
qui2 = Counter()
qui2_ex = []
for i,w in enumerate(tv8):
    if is_inf(w):
        ss = second_syl(w)
        if ss == "qui":
            qui2[w]+=1
            if len(qui2_ex)<12: qui2_ex.append((i,w))
res["ml1"]["ML-1b_inf_second_syl_qui"] = {
    "n_tokens": sum(qui2.values()), "words": dict(qui2.most_common(15)),
    "examples": qui2_ex}
print("ML-1b n:", sum(qui2.values()), dict(qui2.most_common(10)))

# ================= ML-1c: "de le [mono-INF] qui" =================
mono_inf = set()
for art in ["le","la","l'","les"]:
    for x in [x for _,x in [(i,tv8[i+2]) for i in range(len(tv8)-2)
            if tv8[i]=="de" and tv8[i+1]==art and is_inf(tv8[i+2])]]:
        if len(byear_syllables(x))==1: mono_inf.add(x)
hits_c = [(i,tv8[i+2]) for i in range(len(tv8)-3)
          if tv8[i]=="de" and tv8[i+1]=="le" and tv8[i+2] in mono_inf
          and tv8[i+3]=="qui"]
res["ml1"]["ML-1c_de_le_monoINF_qui"] = {
    "mono_inf_set": sorted(mono_inf),
    "n": len(hits_c),
    "hits": [(i, w, " ".join(tv8[max(0,i-4):i+6])) for i,w in hits_c[:10]]}
print("ML-1c n:", len(hits_c))

# ================= ML-1d: cipher-side 78 =================
p78 = [i for i,v in enumerate(PAIRS) if v==78]
res["ml1"]["ML-1d_cipher78"] = {
    "n78": len(p78),
    "foll_29": sum(1 for i in p78 if i+1<N and PAIRS[i+1]==29),
    "pre47": [i for i in p78 if i>0 and PAIRS[i-1]==47],
    "pre77_windows": [[PAIRS[j] for j in range(max(0,i-3),min(N,i+4))] for i in p78 if i>0 and PAIRS[i-1]==77],
    "suc64_count": sum(1 for i in p78 if i+1<N and PAIRS[i+1]==64),
}
print("ML-1d n78:", len(p78), "foll29:", res["ml1"]["ML-1d_cipher78"]["foll_29"])

# ================= ML-2a: L1 of "de le"+INF, hand-classified =================
l1 = Counter()
for i in range(len(tv8)-2):
    if tv8[i]=="de" and tv8[i+1]=="le" and is_inf(tv8[i+2]) and i>0:
        l1[tv8[i-1]]+=1
res["ml2"]["ML-2a_L1_counts"] = dict(l1.most_common(40))
print("ML-2a distinct L1:", len(l1), "| total:", sum(l1.values()))
for w,c in l1.most_common(40): print(f"   {w}: {c}")

# hand classification (FR-JUDGMENT) — written from the observed L1 list
def l1_class(w):
    ADJ = {"facile","chargé","chargée","donné","donnée","donne","aisé","aisée",
           "difficile","impossible","possible","nécessaire","utile","inutile",
           "heureux","heureuse","malheureux","fâché","fâchée","content","contente",
           "capable","incapable","digne","indigne","responsable","coupable",
           "libre","sûr","sûre","certain","certaine","désireux","curieux",
           "jaloux","honteux","fier","fière","las","lasse","fatigué","fatiguée"}
    NOUN = {"plaisir","courage","moyen","moyens","occasion","étonnement",
            "honneur","bonheur","malheur","peine","peines","soin","soins",
            "droit","droits","devoir","devoirs","temps","lieu","manière",
            "façon","coutume","habitude","raison","raisons","ordre","ordres",
            "dessein","projet","projets","intention","intentions","désir",
            "envie","besoin","besoins","crainte","peur","honte","gloire",
            "force","forces","pouvoir","art","métier","talent","adresse",
            "permission","défense","prière","demande","offre","promesse"}
    PART = {"regretté","regrettée","donnée","donnés","données","chargé",
            "chargée","chargés","donné","donné","obligé","obligée","forcé",
            "forcée","condamné","autorisé","autorisée","prié","priée",
            "invité","invitée","chargé","étonné","désolé","persuadé",
            "décidé","décidée","résolu","résolue","accoutumé","habitué"}
    VERB = {"veut","veux","voulait","voudrait","désire","désirait","tâche",
            "tâchait","s'efforce","efforce","cherche","cherchait","essaie",
            "essayait","demande","demandait","prie","priait","ordonne",
            "permet","défend","empêche","propose","conseille","aide",
            "vient","venait","va","allait","parvient","réussit","hésite",
            "craint","affecte","feint","entreprend","ose","daigne","plaira",
            "plait","plaît","semble","paraît"}
    if w in ADJ: return "adjective"
    if w in NOUN: return "noun"
    if w in PART: return "participle"
    if w in VERB or w.endswith(("er","ir","re")) and w not in NOUN: return "verb?"
    return "other/hand"
cls = Counter(); unclass=[]
for w,c in l1.items():
    k=l1_class(w); cls[k]+=c
    if k in ("other/hand","verb?"): unclass.append((w,c))
res["ml2"]["ML-2a_class_shares"] = dict(cls)
res["ml2"]["ML-2a_unclassified"] = sorted(unclass, key=lambda x:-x[1])[:25]
print("ML-2a class shares:", dict(cls))

# ML-2b: L2 for adj/noun/participle L1s
ADJ_NOUN_PART = {w for w in l1 if l1_class(w) in ("adjective","noun","participle")}
l2 = Counter()
for i in range(1,len(tv8)-3):
    if tv8[i]=="de" and tv8[i+1]=="le" and is_inf(tv8[i+2]) and tv8[i-1] in ADJ_NOUN_PART:
        l2[tv8[i-2]]+=1
res["ml2"]["ML-2b_L2_top"] = dict(l2.most_common(20))
print("ML-2b L2 top:", dict(l2.most_common(15)))

# ML-2c: cipher-side 12 probes
p12 = [i for i,v in enumerate(PAIRS) if v==12]
res["ml2"]["ML-2c_cipher12"] = {
    "n12": len(p12),
    "pre70": [i for i in p12 if i>0 and PAIRS[i-1]==70],
    "suc48": [i for i in p12 if i+1<N and PAIRS[i+1]==48],
    "suc33": [i for i in p12 if i+1<N and PAIRS[i+1]==33],
    "pre11": [i for i in p12 if i>0 and PAIRS[i-1]==11],
    "windows": {i: [PAIRS[j] for j in range(max(0,i-3),min(N,i+4))] for i in p12},
}
# era: (adj|noun|part, INF) bare bigrams for the L1 word set
bare = Counter()
for w in ADJ_NOUN_PART:
    for i in range(len(tv8)-1):
        if tv8[i]==w and is_inf(tv8[i+1]): bare[(w,tv8[i+1])]+=1
res["ml2"]["ML-2c_bare_class_INF_bigrams"] = {
    "n": sum(bare.values()), "top": [(a,b,c) for (a,b),c in bare.most_common(12)]}
print("ML-2c bare (class,INF):", sum(bare.values()))

# ================= @863 =================
n_de_ce_que = sum(1 for i in range(len(tv8)-2)
                 if tv8[i]=="de" and tv8[i+1]=="ce" and tv8[i+2]=="que")
kw = []
for i in range(len(tv8)-2):
    if tv8[i]=="de" and tv8[i+1]=="ce" and tv8[i+2]=="que":
        kw.append(" ".join(tv8[max(0,i-5):i+7]))
res["at863"]["863-a"] = {"n_de_ce_que": n_de_ce_que, "kwic": kw}
print("@863 n:", n_de_ce_que)
# L1 of "de ce que"
l1dcq = Counter(tv8[i-1] for i in range(1,len(tv8)-2)
               if tv8[i]=="de" and tv8[i+1]=="ce" and tv8[i+2]=="que")
res["at863"]["863-a"]["L1"] = dict(l1dcq.most_common(15))
n_de_ce_noun = sum(1 for i in range(len(tv8)-2)
                   if tv8[i]=="de" and tv8[i+1]=="ce" and tv8[i+2] not in ("que",)
                   and not is_inf(tv8[i+2]) and len(tv8[i+2])>3)
res["at863"]["863-a"]["n_de_ce_nonque"] = n_de_ce_noun
# 74 profile
p74 = [i for i,v in enumerate(PAIRS) if v==74]
res["at863"]["863-b_74"] = {
    "n74": len(p74),
    "pre": dict(Counter(PAIRS[i-1] for i in p74 if i>0).most_common(10)),
    "suc": dict(Counter(PAIRS[i+1] for i in p74 if i+1<N).most_common(10)),
    "at862_window": [PAIRS[j] for j in range(859,869)],
}
# 863-c: 48 window accounting (reuses F83 fences, not re-scored)
p48 = [i for i,v in enumerate(PAIRS) if v==48]
acct = {}
for i in p48:
    pre = PAIRS[i-1] if i>0 else None
    suc = PAIRS[i+1] if i+1<N else None
    suc2 = PAIRS[i+2] if i+2<N else None
    if i==1076: tag="narrow-path-pending(ML-1/ML-2)"
    elif i==1350: tag="OUT(R-c)"
    elif i==126: tag="OUT(left-unlicensed)"
    elif suc==47: tag="de-ce-frame"
    elif pre==62: tag="on48(PathA-fenced)"
    elif pre==82: tag="m48(PathB-fenced)"
    elif suc==52: tag="48pas(conditioning-escape)"
    else: tag="neutral"
    acct[i]=(pre,suc,suc2,tag)
res["at863"]["863-c_48_accounting"] = {str(i): {"pre":a,"suc":b,"suc2":c,"tag":d}
                                       for i,(a,b,c,d) in acct.items()}
from collections import Counter as C2
print("863-c tags:", dict(C2(d for _,_,_,d in acct.values())))

# ML-1c': token after "de le"+mono-inf (sensitivity for reading (a))
after = Counter(); after_ex = []
for i in range(len(tv8)-3):
    if tv8[i]=="de" and tv8[i+1]=="le" and is_inf(tv8[i+2]) and len(byear_syllables(tv8[i+2]))==1:
        after[tv8[i+3]]+=1
        if len(after_ex)<8: after_ex.append((tv8[i+2], " ".join(tv8[max(0,i-3):i+5])))
res["ml1"]["ML-1c_prime_after_de_le_monoINF"] = {"dist": dict(after.most_common(20)), "examples": after_ex}
print("ML-1c' after:", dict(after.most_common(10)))

# levant sensitivity for ML-1b / ML-1c (corpus9 'primary' = v8 + levant)
tlev = corpus9.load('primary')
q2 = Counter(w for w in tlev if is_inf(w) and second_syl(w)=="qui")
n_c_lev = sum(1 for i in range(len(tlev)-3)
              if tlev[i]=="de" and tlev[i+1]=="le" and tlev[i+2] in ("voir",)
              and tlev[i+3]=="qui")
res["ml1"]["levant_sensitivity"] = {
    "inf_second_syl_qui_words": dict(q2.most_common(10)),
    "de_le_voir_qui": n_c_lev}
print("levant: inf-2nd-qui:", dict(q2.most_common(5)), "| de-le-voir-qui:", n_c_lev)

out = open(LANE/'code/crowd12/followup48/followup48_results.json','w')
json.dump(res, out, indent=1, ensure_ascii=False)
out.close()
print('wrote', LANE/'code/crowd12/followup48/followup48_results.json')
