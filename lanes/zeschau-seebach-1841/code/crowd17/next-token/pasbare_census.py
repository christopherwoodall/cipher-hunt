#!/usr/bin/env python3
"""Battery pas-bare-corpus: census of bare 'pas' (no 'ne') as clause negator.

Corpus: lane's period corpus (code/side-period/corpus).
Design: sentence-level. A token 'pas' is a CANDIDATE iff no 'ne' or "n'"
occurs anywhere to its left within the same sentence. All candidates are
hand-audited in context for: genuine clause negator (pas negates a finite
verb, no ne) vs noun/aside uses ("un pas", "pas de X", "pas à pas", "non pas",
answer fragments, exclamations) vs OCR junk.

Normalization: curly apostrophes (U+2019) -> "'"; text lowered. Word-boundary
token match for 'pas'. "né"/"nee" irrelevant here; "n'" elision forms are
checked in both straight and curly quote variants post-normalization.
"""
import os, re, json

CORP = os.path.expanduser(
    "~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-period/corpus")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "pasbare_candidates.json")

DET_LIKE = {"non","un","une","le","la","les","des","de","du","ses","mes","tes","ces",
    "premier","premiers","grand","petit","chaque","aucun","quelque","quelques",
    "son","sa","leur","leurs","notre","nos","votre","vos","mon","ma","ce","cet",
    "cette","tout","toute","tous","toutes","autre","autres","quel","quelle",
    "quels","quelles","deux","trois","dernier","derniers","quatre","cinq",
    "premier","mille","cent"}
PREP_NOUN_PAS = {"à","au","aux","en","sur","dans","par","avec","sans","sous","vers"}
FUSED_NE = {"dene","quene","dené"}  # OCR fusions of "de ne"/"que ne"
QUOTE = re.compile(r"[\u2018\u2019\u201b\u2032\u00b4]")

def norm(t):
    return QUOTE.sub("'", t).lower()

def sentences_of(text):
    # Split ONLY on strong terminals. Never split on newlines: "ne\npas"
    # across a line break is one sentence (the old newline split created
    # false bare-pas candidates by stranding "ne" in the previous chunk).
    parts = re.split(r"[.!?…]+", text)
    return [p for p in (s.strip() for s in parts) if p]

CLAUSE_BOUND = re.compile(r"[;:]")

def ne_left_of(toks, i):
    """True iff 'ne'/'n\'' occurs in the same clause to the left of toks[i].
    Clause = back to nearest ';' or ':', or at most 120 tokens."""
    j = i - 1
    scanned = 0
    while j >= 0 and scanned < 120:
        x = toks[j]
        if x == ";" or x == ":":
            return False
        if x in ("ne", "ne'", "n'", "n") or x.startswith("n'") or x in FUSED_NE:
            return True
        j -= 1
        scanned += 1
    return False

def tokenize(s):
    # keep ';' and ':' as tokens so ne_left_of can stop at clause bounds
    return re.findall(r"[a-zàâäéèêëîïôöùûüçœæ']+|[0-9]+|[;:]", s)

def main():
    files = sorted(f for f in os.listdir(CORP)
                   if f.endswith(".txt") and "provenance" not in f.lower())
    total_chars = 0
    pas_total = 0
    candidates = []  # (file, line_excerpt, pas_index, left_context, right_context)
    for fn in files:
        with open(os.path.join(CORP, fn), encoding="utf-8", errors="replace") as fh:
            raw = fh.read()
        total_chars += len(raw)
        t = norm(raw)
        for sent in sentences_of(t):
            toks = tokenize(sent)
            if "pas" not in toks:
                continue
            for i, w in enumerate(toks):
                if w != "pas":
                    continue
                pas_total += 1
                left = toks[:i]
                if ne_left_of(toks, i):
                    continue  # partnered: not a candidate
                # candidate: no ne/n' leftward in sentence
                candidates.append({
                    "file": fn,
                    "sent": sent[:400],
                    "left": " ".join(toks[max(0, i-8):i]),
                    "right": " ".join(toks[i+1:i+9]),
                })
    out = {
        "files": len(files),
        "chars": total_chars,
        "pas_tokens": pas_total,
        "bare_candidates": len(candidates),
        "candidates": candidates,
    }
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False)
    print(json.dumps({k: v for k, v in out.items() if k != "candidates"},
                     ensure_ascii=False))

if __name__ == "__main__":
    main()
