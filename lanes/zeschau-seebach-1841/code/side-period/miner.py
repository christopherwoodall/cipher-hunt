#!/usr/bin/env python3
"""Crib miner for the Seebach cipher lane's PERIOD-SOURCES fleet.
Mines the Nesselrode *Lettres et papiers* volumes for:
  - content-word frequencies (topical crib vocabulary)
  - proper nouns: people / places / titles / institutions (capitalized runs)
  - diplomatic formula openings, closings, and set phrases
  - topic-keyword concordances ("what was in the air", Jan 1841)
  - bigram/trigram collocations of content words
Outputs JSON + human-readable tables to stdout/work dir.
Usage: python3 miner.py [corpus_dir] [out_dir]
"""
import json, re, sys, unicodedata
from collections import Counter, defaultdict
from pathlib import Path

CORPUS = Path(sys.argv[1] if len(sys.argv) > 1 else
              str(Path(__file__).parent / "corpus"))
OUT = Path(sys.argv[2] if len(sys.argv) > 2 else "/tmp/cribminer")
OUT.mkdir(parents=True, exist_ok=True)

FR_STOP = set("""de la le les des du un une et est en dans que qui ne pas pour
au aux ce cette ces il ils elle elles on nous vous ils se son sa ses leur leurs
avec comme mais ou où donc or ni car par sur entre après avant pendant depuis
jusque tout toute tous toutes même autres autre aussi bien plus moins très
si toutfois cependant toutefois lorsque dont ainsi alors déjà encore jamais
toujours peut peux peuvent être avoir fait font faites faire dit disent dont
cela ceci celui celle ceux celles dont""".split())

# "What was in the air" seeds (Jan 1841) -> topic keyword groups for concordance
TOPICS = {
    "levant_mehemet": ["mehemet", "méhémet", "mehmet", "ali", "ibrahim",
                       "egypte", "égypte", "syrie", "firman", "investiture",
                       "héréditaire", "hereditaire", "évacuation", "evacuation"],
    "straits": ["détroits", "detroits", "dardanelles", "bosphore",
                "unkia", "unkiar", "skelessi", "convention", "traité", "traite"],
    "powers_people": ["guizot", "thiers", "louis-philippe", "louis philippe",
                      "palmerston", "metternich", "nicholas", "nicolas",
                      "frederic", "frédéric", "espartero", "ponsonby",
                      "abder", "abdoul", "sultan", "mahmoud", "mahmud"],
    "capitals": ["constantinople", "londres", "paris", "vienne", "berlin",
                 "pétersbourg", "petersbourg", "dresde", "saxe", "prusse",
                 "autriche", "angleterre", "france", "russie", "turquie"],
    "other_1841": ["kossuth", "hong", "kong", "opium", "polonais", "pologne",
                   "zollverein", "douane"],
}

FORMULA_PATTERNS = [
    r"j'?ai l'?honneur de [^.;!?]{0,80}",
    r"j'?ai l'?honneur d'?ê?tre[^.;!?]{0,60}",
    r"agréez [^.;!?]{0,90}",
    r"veuillez agréer [^.;!?]{0,90}",
    r"l'?assurance de (ma|mes) [^.;!?]{0,60}",
    r"haute considération[^.;!?]{0,30}",
    r"considération (la plus |très )?distinguée[^.;!?]{0,20}",
    r"profond respect[^.;!?]{0,40}",
    r"très humble [^.;!?]{0,60}",
    r"obéissant serviteur[^.;!?]{0,20}",
    r"monsieur le (comte|baron|prince|duc|marquis)[^.;!?]{0,60}",
    r"mon (cher|très cher) [^.;!?]{0,40}",
    r"votre (très |plus )?dévoué [^.;!?]{0,40}",
    r"sa majesté (impériale|le roi|l'?empereur)?[^.;!?]{0,50}",
    r"l'?empereur [^.;!?]{0,60}",
    r"j'?ai reçu [^.;!?]{0,90}",
    r"j'?ai appris [^.;!?]{0,90}",
    r"permettez-moi [^.;!?]{0,60}",
    r"je me fais un devoir [^.;!?]{0,80}",
    r"je m'?empresse [^.;!?]{0,80}",
    r"en réponse à [^.;!?]{0,80}",
    r"d'?ordre de [^.;!?]{0,60}",
    r"par ordre de [^.;!?]{0,60}",
    r"je vous prie [^.;!?]{0,80}",
    r"daignez [^.;!?]{0,80}",
    r"à l'?égard de [^.;!?]{0,60}",
    r"à l'?occasion de [^.;!?]{0,60}",
    r"prendre connaissance [^.;!?]{0,40}",
    r"porter à la connaissance [^.;!?]{0,60}",
    r"donner connaissance [^.;!?]{0,40}",
    r"rendre compte [^.;!?]{0,50}",
    r"faire part [^.;!?]{0,50}",
    r"je suis [^.;!?]{0,40}",
    r"avec les sentiments [^.;!?]{0,80}",
    r"les sentiments de [^.;!?]{0,80}",
    r"profond attachement[^.;!?]{0,30}",
    r"respectueux attachement[^.;!?]{0,30}",
]

SENT_END = re.compile(r"[.!?…;:»”\"]\s*$")

def load():
    texts = {}
    for f in sorted(CORPUS.glob("*.txt")):
        if f.name.lower().startswith("provenance"):
            continue
        texts[f.name] = f.read_text(encoding="utf-8", errors="replace")
    return texts

def normalize(t):
    t = t.replace("’", "'").replace("‘", "'").replace("«", " ").replace("»", " ")
    t = re.sub(r"\s+", " ", t)
    return t

TOK = re.compile(r"[A-Za-zÀ-ÿŒœÆæ]+(?:'[A-Za-zÀ-ÿ]+)?|[0-9]+")

def tokens(t):
    return TOK.findall(t)

def strip_acc(s):
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn")

def main():
    texts = load()
    print("volumes:", {k: len(v) for k, v in texts.items()}, file=sys.stderr)

    word_all, word_by_vol = Counter(), defaultdict(Counter)
    cap_runs_all, cap_runs_by_vol = Counter(), defaultdict(Counter)
    cap1_all = Counter()          # capitalized unigrams
    cap1_sentinit = Counter()     # ...of which sentence-initial
    bigrams, trigrams = Counter(), Counter()
    formulas = defaultdict(Counter)  # pattern -> Counter(context)
    topic_conc = defaultdict(lambda: defaultdict(Counter))  # topic -> kw -> Counter(co-word)
    topic_vol = defaultdict(Counter)  # topic -> vol -> hits

    flat = {k: strip_acc(v.lower()) for k, v in texts.items()}
    flat_case = {k: strip_acc(normalize(v)) for k, v in texts.items()}
    topic_re = {}
    for topic, kws in TOPICS.items():
        topic_re[topic] = [re.compile(r"\b" + re.escape(strip_acc(k))
                                      .replace("\\ ", "\\s+") + r"\b") for k in kws]

    for vol, raw in texts.items():
        t = normalize(raw)
        toks = tokens(t)
        low = [w.lower() for w in toks]
        prev_end = True  # start of text counts as sentence start
        i = 0
        run = []
        for w, l in zip(toks, low):
            # sentence boundary tracking (rough: check raw context)
            # word frequency
            if l not in FR_STOP and len(l) > 2 and not l[0].isdigit():
                word_all[l] += 1
                word_by_vol[vol][l] += 1
            # capitalized run
            if w and w[0].isupper() and w[0].isalpha() and not w.isupper():
                if l in FR_STOP and len(run) == 0:
                    cap1_sentinit[l] += 1  # sentence-initial common word
                    run = []
                else:
                    run.append(w)
            else:
                if run:
                    key = " ".join(run)
                    if len(key) > 2 and not any(ch.isdigit() for ch in key):
                        cap_runs_all[key] += 1
                        cap_runs_by_vol[vol][key] += 1
                        for r in run:
                            cap1_all[r.lower()] += 1
                            # crude: mark first of text as sentence-initial
                    run = []
            i += 1
        if run:
            key = " ".join(run)
            cap_runs_all[key] += 1
            cap_runs_by_vol[vol][key] += 1

        # bigrams/trigrams of content words
        cw = [w for w in low if w not in FR_STOP and len(w) > 2 and w[0].isalpha()]
        for a, b in zip(cw, cw[1:]):
            bigrams[a + " " + b] += 1
        for a, b, c_ in zip(cw, cw[1:], cw[2:]):
            trigrams[a + " " + b + " " + c_] += 1

        # formulas on the flat (accent-stripped, lowered) text
        ftext = flat[vol]
        for pat in FORMULA_PATTERNS:
            pat2 = strip_acc(pat)
            for m in re.finditer(pat2, ftext):
                ctx = m.group(0).strip()
                if len(ctx) > 3:
                    formulas[pat][ctx] += 1

        # topic concordances: co-occurring capitalized/content words within ±300 chars
        fcase = flat_case[vol]
        for topic, res in topic_re.items():
            for r in res:
                for m in r.finditer(ftext):
                    topic_vol[topic][vol] += 1
                    win = fcase[max(0, m.start() - 300):m.end() + 300]
                    for w in TOK.findall(win):
                        if w and w[0].isupper() and w[0].isalpha() \
                                and w.lower() not in FR_STOP and len(w) > 2 \
                                and not w.isupper():
                            topic_conc[topic][m.group(0)][w] += 1

    out = {
        "top_words": word_all.most_common(400),
        "top_cap_runs": cap_runs_all.most_common(500),
        "top_cap1": cap1_all.most_common(300),
        "bigrams": bigrams.most_common(400),
        "trigrams": trigrams.most_common(300),
        "formulas": {p: c.most_common(25) for p, c in formulas.items()},
        "topic_concordance": {t: {k: c.most_common(20)
                                  for k, c in kw.items()}
                              for t, kw in topic_conc.items()},
        "topic_vol": {t: dict(v) for t, v in topic_vol.items()},
        "words_by_vol": {v: dict(c.most_common(200)) for v, c in word_by_vol.items()},
    }
    (OUT / "mine.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
    print("wrote", OUT / "mine.json", file=sys.stderr)
    return out

if __name__ == "__main__":
    main()
