#!/usr/bin/env python3
"""True-POS re-pass for disloc-demonstrative-inversion-verbtags.

Loads disloc-demonstrative-inversion-verbtags_census.json (37 candidates,
identical universe to the parent inversion battery), re-derives each
candidate's dialogue-span context, and tags the INF-shaped token with
spaCy fr_core_news_sm (v3.8.0, installed on the VM 2026-10-09 for this
battery). A candidate counts as "POS-tagged genuine infinitive" iff the
token aligned to the INF regex match is tagged VERB with
VerbForm=Inf.

Method details:
- Context fed to the tagger: span body [inf_start-120 : inf_start+100],
  so the token is disambiguated in sentence context (not isolated —
  isolated bare infinitives mis-tag as PROPN).
- Alignment: the spaCy token whose character span covers the INF regex
  match start (offset translated into the context slice).
- INF regex matches can include a clitic prefix (e.g. "l'arracher"):
  the INF verb stem is the LAST token of the match; we tag that token.

Output: disloc-demonstrative-inversion-verbtags_spacy.json listing each
candidate with pos/tag/morph of the infinitive-shaped token.
"""
import json, os, sys
import spacy

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from disloc_demonstrative_inversion_census import (  # noqa: E402
    dialogue_spans, RDM, LANE)

CENSUS = os.path.join(LANE, "code/crowd17/next-token",
                      "disloc-demonstrative-inversion-verbtags_census.json")
OUT = os.path.join(LANE, "code/crowd17/next-token",
                   "disloc-demonstrative-inversion-verbtags_spacy.json")


def find_span_context(fname, abs_off, pad_before=120, pad_after=100):
    """Return (context_text, inf_start_in_context) for the span body
    containing the absolute INF offset."""
    path = next(p for p in RDM if os.path.basename(p) == fname)
    text = open(path, encoding="utf-8", errors="replace").read()
    for kind, body, span_start in dialogue_spans(text):
        rel = abs_off - span_start
        if 0 <= rel < len(body):
            s = max(0, rel - pad_before)
            ctx = body[s:rel + pad_after]
            return ctx, rel - s
    return None, None


def tag_candidates(nlp, cands):
    rows = []
    for c in cands:
        ctx, rel = find_span_context(c["file"], c["inf_abs_offset"])
        if ctx is None:
            rows.append({**c, "spacy_pos": None,
                         "spacy_note": "span not found"})
            continue
        doc = nlp(ctx)
        # token whose span covers the INF match start
        match_len = len(c["inf"])
        target = None
        for tok in doc:
            ts = tok.idx
            if ts <= rel < ts + len(tok.text_with_ws.rstrip()):
                target = tok
                break
        if target is None:
            rows.append({**c, "spacy_pos": None,
                         "spacy_note": "no token aligned"})
            continue
        rows.append({
            **c,
            "spacy_token": target.text,
            "spacy_pos": target.pos_,
            "spacy_tag": target.tag_,
            "spacy_morph": str(target.morph),
            "genuine_inf": (target.pos_ == "VERB"
                            and "VerbForm=Inf" in target.morph),
        })
    return rows


def main():
    nlp = spacy.load("fr_core_news_sm")
    d = json.load(open(CENSUS))
    cands = d["kept_candidates"] + d["dropped_candidates"]
    rows = tag_candidates(nlp, cands)
    json.dump({"rows": rows, "model": "fr_core_news_sm-3.8.0",
               "tagger": "spacy 3.8.16"},
              open(OUT, "w"), ensure_ascii=False, indent=1)
    gi = sum(1 for r in rows if r.get("genuine_inf"))
    print("wrote", OUT)
    print(f"candidates: {len(rows)} | POS-tagged genuine infinitive: {gi}")
    for r in rows:
        flag = "GEN-INF" if r.get("genuine_inf") else "noise  "
        print(f"{flag} {r['file']}@{r['inf_abs_offset']} "
              f"inf={r['inf']!r} tok={r.get('spacy_token')!r} "
              f"pos={r.get('spacy_pos')} morph={r.get('spacy_morph')}")


if __name__ == "__main__":
    main()
