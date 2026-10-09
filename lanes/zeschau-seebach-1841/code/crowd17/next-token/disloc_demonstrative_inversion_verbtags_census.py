#!/usr/bin/env python3
r"""POS-tagged re-census for battery disloc-demonstrative-inversion-verbtags.

Follow-up of battery-disloc-demonstrative-inversion (NULL, 2026-10-09):
37 postposed-dem candidates, of which 21 were classified as false-INF
noise (the raw INF suffix pattern \b...{2,}(er|ir|re|oir)\b hits nouns,
adjectives, possessives, finite verbs). No French POS tagger is installed
on the VM (spacy/stanza/nltk all absent), so this census applies a
DOCUMENTED rule-based infinitive-shape filter targeting the syntactic
slots a POS tagger would resolve, then manually classifies every
surviving candidate with the parent battery's taxonomy.

Corpus, dialogue-span extraction (D1/D2/D3), INF pattern, and the
postposed-demonstrative window logic are VERBATIM from
disloc_demonstrative_inversion_census.py (imported, not copied), so the
candidate universe is identical: the same 37 candidates over
revue-deux-mondes-1841-q1..q4.txt. Only an extra filter column is added.

Filter rules (each removes a noise class a POS tagger resolves as
non-infinitive; T = the INF-shaped token, L1..L3 = up to 3 word-tokens
of left context in the same dialogue span):

  F1 determiner-governed: L1 is a French determiner/possessive/article
     (le, la, l', les, un, une, des, du, de, d', mon, ma, mes, ton, ta,
     tes, son, sa, ses, notre, nos, votre, vos, leur, leurs, ce, cet,
     cette, ces, quel, quelle, quels, quelles, chaque, tout, toute,
     tous, toutes, aucun, aucune, nul, nulle, tel, telle, autre, autres,
     premier, premiers, derni[eè]re, derni[eè]res, singuli[eè]re,
     quelque, quelques) -> T sits in a noun/adjective slot, not an
     infinitive slot. Handles possessive "votre", "premier"/"dernier"/
     "singulier" adjective cases, etc.
  F2 finite-clause: any of (je, tu, il, elle, on, nous, vous, ils,
     elles) in L1..L2 -> T is a finite verb form, not an infinitive.
     Handles "je vous jure" (jure).
  F3 closed-class non-infinitive: T itself is a closed-class word the
     suffix regex can match (votre, notre, votre) -> not an infinitive.
  F4 vocative/interjection slot: L1 in (ah, oh, eh, h[eé], ha, hol[aà])
     AND T is not a recognized bare-infinitive exclamation -> T is a
     vocative noun. (Kept conservative: only fires on interjection +
     non-infinitive-lexicon token.)

Anything surviving the rules is manually classified with the parent
taxonomy (vocatives, finite clauses, OCR noise, wrong-slot
demonstrative, genuine postposed pairing).

Output: disloc-demonstrative-inversion-verbtags_census.json
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from disloc_demonstrative_inversion_census import (  # noqa: E402
    dialogue_spans, INF, DEM_POST, RDM, LANE)

OUT = os.path.join(LANE, "code/crowd17/next-token",
                   "disloc-demonstrative-inversion-verbtags_census.json")

WORD = re.compile(r"[a-zàâäçéèêëîïôöùûü']+", re.IGNORECASE)

F1_DET = {
    "le", "la", "l'", "les", "un", "une", "des", "du", "de", "d'",
    "mon", "ma", "mes", "ton", "ta", "tes", "son", "sa", "ses",
    "notre", "nos", "votre", "vos", "leur", "leurs",
    "ce", "cet", "cette", "ces", "quel", "quelle", "quels", "quelles",
    "chaque", "tout", "toute", "tous", "toutes",
    "aucun", "aucune", "nul", "nulle", "tel", "telle", "tels", "telles",
    "autre", "autres", "premier", "premiers", "première", "premieres",
    "premières", "dernier", "derniers", "dernière", "dernieres",
    "dernières", "singulier", "singulière", "singuliere",
    "quelque", "quelques",
}
F2_SUBJ = {"je", "tu", "il", "elle", "on", "nous", "vous",
           "ils", "elles"}
F3_CLOSED = {"votre", "notre", "votre"}
F4_INTERJ = {"ah", "oh", "eh", "hé", "he", "ha", "hola", "holà"}


def left_words(body, pos, n=3):
    """Last n word-tokens before char position pos (lowercased)."""
    return [w.lower() for w in WORD.findall(body[:pos])][-n:]


def filter_token(tok, left):
    """Return (keep, rule) — rule None when kept."""
    tok = tok.lower()
    if tok in F3_CLOSED:
        return False, "F3"
    if left and left[-1] in F1_DET:
        return False, "F1"
    if any(w in F2_SUBJ for w in left[-2:]):
        return False, "F2"
    if left and left[-1] in F4_INTERJ:
        return False, "F4"
    return True, None


def candidates(body, kind, span_start):
    out = []
    for im in INF.finditer(body):
        wend = im.end() + 100
        win = body[im.start():wend]
        left = left_words(body, im.start())
        keep, rule = filter_token(im.group(0), left)
        for dm in DEM_POST.finditer(win):
            if dm.start() < (im.end() - im.start()):
                continue
            if "!" not in win[:dm.end() + 20]:
                continue
            out.append({
                "span_kind": kind,
                "inf": im.group(0).lower(),
                "inf_abs_offset": span_start + im.start(),
                "left_context": left,
                "filter_keep": keep,
                "filter_rule": rule,
                "dem": dm.group(1).lower(),
                "window": win,
            })
    return out


def main():
    files, kept, dropped, seen = [], [], [], set()
    for p in RDM:
        name = os.path.basename(p)
        text = open(p, encoding="utf-8", errors="replace").read()
        spans = dialogue_spans(text)
        for kind, body, span_start in spans:
            for w in candidates(body, kind, span_start):
                key = (name, w["inf_abs_offset"])
                if key in seen:
                    continue
                seen.add(key)
                w["file"] = name
                (kept if w["filter_keep"] else dropped).append(w)
        files.append({"file": name, "chars": len(text)})
    json.dump({"files": files, "kept_candidates": kept,
               "dropped_candidates": dropped},
              open(OUT, "w"), ensure_ascii=False, indent=1)
    print("wrote", OUT)
    print("kept:", len(kept), "| dropped:", len(dropped),
          "| total:", len(kept) + len(dropped))


if __name__ == "__main__":
    main()
