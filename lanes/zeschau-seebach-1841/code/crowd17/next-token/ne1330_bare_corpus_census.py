#!/usr/bin/env python3
"""Battery ne-1330-bare-corpus: census of bare 'ne' + finite verb in 1841 main clauses.

Corpus: lane's period corpus (code/side-period/corpus).
Design: sentence-level. A sentence is a CANDIDATE iff it contains a standalone
'ne' (or elided "n'") whose nearest verb-shaped head (allowing clitics) matches
finite-verb morphology, and the sentence contains NO negation partner in the
strict tier {pas, point, que, ni, jamais, plus, rien, personne, aucun, aucune,
guère, mie, goutte}. A literal tier (partners = {pas, point, que} only, per the
bar's wording) is recorded for comparison. All candidates are hand-audited for
main-clause status (expletive-ne subordinates excluded).

Finite-verb detection: common-finite-forms lexicon + distinctive finite endings
(-ait/-aient/-rai/-ras/-ra/-rons/-rez/-ront/-rais/-rait/-âmes/-âtes/-èrent/
-îmes/-îtes/-irent/-ûmes/-ûtes/-urent/-ai/-as/-a/-is/-it/-us/-ut/-ons/-ez/
-ions/-iez/-ais). Generator favors recall; hand audit establishes genuineness.
"""
import os, re, json, sys

CORP = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-period/corpus")
OUTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))

CLITICS = {"le", "la", "les", "lui", "leur", "me", "te", "se", "nous", "vous",
           "en", "y", "moi", "toi", "soi",
           "m'", "t'", "s'", "l'", "d'", "qu'", "c'", "n'", "j'"}

PARTNER_STRICT = {"pas", "point", "que", "qu'", "ni", "jamais", "plus", "rien",
                  "personne", "aucun", "aucune", "guère", "mie", "goutte"}
PARTNER_LITERAL = {"pas", "point", "que", "qu'"}

# Distinctive finite endings (recall-oriented; audit decides)
FINITE_END = re.compile(
    r"(ait|aient|aient$|rai$|ras$|ra$|rons$|rez$|ront$|rais$|rait$|rions$|riez$|raient$|"
    r"âmes$|âtes$|èrent$|îmes$|îtes$|irent$|ûmes$|ûtes$|urent$|ai$|as$|ons$|ez$|ions$|iez$|"
    r"ais$|é$)$"
)
# Common finite forms that don't end distinctively (sample; audit catches rest)
COMMON_FINITE = {
    "est", "sont", "suis", "es", "sommes", "êtes",
    "a", "as", "avons", "avez", "ont", "ai",
    "fait", "font", "fais", "faites", "faisons",
    "dit", "disent", "dis", "dites", "disons",
    "peut", "peuvent", "peux", "pouvons", "pouvez",
    "sait", "savent", "sais", "savons", "savez",
    "veut", "veulent", "veux", "voulons", "voulez",
    "doit", "doivent", "dois", "devons", "devez",
    "va", "vont", "vais", "allons", "allez",
    "vient", "viennent", "viens", "venons", "venez",
    "prend", "prennent", "prends", "prenons", "prenez",
    "met", "mettent", "mets", "mettons", "mettez",
    "voit", "voient", "vois", "voyons", "voyez",
    "croit", "croient", "crois", "croyons", "croyez",
    "faut", "fallait",
    "paraît", "paraissent", "semble", "semblent",
    "reste", "restent", "devient", "deviennent",
    "tient", "tiennent", "porte", "portent",
    "suit", "suivent", "connaît", "connaissent",
    "sent", "sentent", "rend", "rendent",
    "comprend", "comprennent", "trouve", "trouvent",
    "donne", "donnent", "laisse", "laissent",
    "ose", "osent", "cesse", "cessent",
    "empêche", "empêchent", "demeure", "demeurent",
    "règne", "règnent", "trône", "trônent",
    "passe", "passent", "importe", "importent",
    "passe", "naguère",
    "fut", "fussent", "fût", "soit", "soient",
    "ait", "aient", "eut", "eurent",
    "voulut", "voulurent", "put", "purent",
    "fit", "firent", "dit", "dirent",
    "vint", "vinrent", "prit", "prirent",
    "vit", "virent", "crut", "crurent",
}

def norm(t):
    return t.replace("’", "'").replace("‘", "'").replace("ʼ", "'")

def is_finite(w):
    w = w.lower()
    if w in COMMON_FINITE:
        return True
    return bool(FINITE_END.search(w))

def tokens(sent):
    return re.findall(r"[A-Za-zÀ-ÿâêîôûäëïöüéèç'-]+", norm(sent))

def main():
    files = sorted(f for f in os.listdir(CORP) if os.path.isfile(os.path.join(CORP, f)))
    total_chars = 0
    ne_sentences = 0
    candidates = []   # strict tier
    literal_extra = []  # literal tier minus strict tier
    stats = {"sentences": 0, "ne_hits": 0, "ne_elided_hits": 0}

    for f in files:
        p = os.path.join(CORP, f)
        with open(p, encoding="utf-8", errors="ignore") as fh:
            text = fh.read()
        total_chars += len(text)
        # normalize: single newlines -> space (prose line-wrap); keep
        # paragraph breaks. Otherwise restrictive "que" on the next line
        # is missed and fragments read as false "bare ne".
        text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)
        # sentence split; keep byte-ish offsets via running index
        for m in re.finditer(r"[^.!?…;:]+[.!?…;:]", text):
            sent = m.group(0)
            stats["sentences"] += 1
            toks = [t.lower() for t in tokens(sent)]
            if not toks:
                continue
            # find standalone 'ne' or elided n'
            hits = []
            for i, t in enumerate(toks):
                if t == "ne":
                    stats["ne_hits"] += 1
                    hits.append((i, "ne"))
                elif t.startswith("n'") and len(t) > 2:
                    stats["ne_elided_hits"] += 1
                    hits.append((i, "n'"))
            if not hits:
                continue
            ne_sentences += 1
            # partner check
            # 1) whole-sentence partners that pair with ne wherever they sit
            tset = set(toks)
            strict_hit = tset & PARTNER_STRICT
            literal_hit = tset & PARTNER_LITERAL
            # 2) restrictive que/qu' must FOLLOW the ne-hit to be its partner.
            #    Fused forms ("qu'il", "qu'une") are single tokens; "parce/puisque/
            #    lorsque/quoique + qu'" are conjunctions, not the restrictive que.
            CONJ_BEFORE_QU = {"parce", "puisque", "lorsque", "quoique", "jusqu"}
            def que_after(idx):
                for k in range(idx + 1, len(toks)):
                    t = toks[k]
                    if t == "que" or (t.startswith("qu'") and toks[k - 1] not in CONJ_BEFORE_QU):
                        return True
                return False
            # for each ne-hit, find nearest verb-shaped head
            for (i, kind) in hits:
                j = i + 1
                # if elided n', the head is fused: n' + word (e.g. "n'ose")
                head = None
                if kind == "n'":
                    w = toks[i]
                    head = w[2:]
                else:
                    k = j
                    while k < len(toks) and toks[k] in CLITICS:
                        k += 1
                    if k < len(toks):
                        head = toks[k]
                if head and is_finite(head):
                    ctx = sent.strip()
                    ctx = re.sub(r"\s+", " ", ctx)
                    if len(ctx) > 400:
                        ctx = ctx[:400]
                    q_after = que_after(i)
                    rec = {"file": f, "ne_kind": kind, "head": head,
                           "strict_partners": sorted(strict_hit),
                           "literal_partners": sorted(literal_hit),
                           "que_after_ne": q_after,
                           "sentence": ctx}
                    if not strict_hit and not q_after:
                        candidates.append(rec)
                    elif not literal_hit and not q_after:
                        literal_extra.append(rec)

    json.dump({"corpus_files": len(files), "corpus_chars": total_chars,
               "stats": stats, "ne_sentences": ne_sentences,
               "strict_candidates": len(candidates),
               "literal_extra": len(literal_extra)},
              open(os.path.join(OUTDIR, "ne1330_bare_corpus_meta.json"), "w"), indent=1)
    json.dump(candidates, open(os.path.join(OUTDIR, "ne1330_bare_corpus_candidates.json"), "w"),
              indent=1, ensure_ascii=False)
    json.dump(literal_extra, open(os.path.join(OUTDIR, "ne1330_bare_corpus_literal_extra.json"), "w"),
              indent=1, ensure_ascii=False)
    print("files:", len(files), "chars:", total_chars)
    print("ne standalone hits:", stats["ne_hits"], "| n' elided hits:", stats["ne_elided_hits"])
    print("strict candidates:", len(candidates), "| literal-tier extras:", len(literal_extra))

if __name__ == "__main__":
    main()
