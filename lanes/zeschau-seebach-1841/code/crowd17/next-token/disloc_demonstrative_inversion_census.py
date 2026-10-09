#!/usr/bin/env python3
r"""Census for battery disloc-demonstrative-inversion.

Target: POSTPOSED demonstratives ("[inf] !, cela/ceci/ca" word order) inside
QUOTED-DIALOGUE windows of the revue-deux-mondes-1841 corpus (q1..q4) only.
The inversion test of the fenced pairing "dislocated demonstrative + bare
exclamatory infinitive": if the tonic head licenses the pairing from
post-topic position, the bar construction never shows up in the preposed
order already fenced by batteries disloc-demonstrative-inf /
-disloc-demonstrative-quoted-drama.

Dialogue-window extraction (verbatim from
disloc_demonstrative_quoted_drama_census.py):
  D1 guillemet quotes:  « ... » (non-greedy, DOTALL)
  D2 straight double quotes: " ... " (non-greedy, DOTALL, span >= 4 chars)
  D3 em-dash dialogue: paragraphs (blank-line separated) starting with
     — or – ; whole paragraph to next blank line.

Inversion search on each dialogue span:
  INF (verbatim reused): \b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b
  DEM_POST (tonic set, postposed): \b(cela|ceci|ça|ca|cel[àa]|cec[iy])\b
  For each INF match: window = INF start .. INF end + 100 chars.
  Candidate iff a DEM_POST match starts AFTER the infinitive inside the
  window AND "!" occurs between the INF start and 20 chars past the DEM
  match end. This covers all postposed shapes:
    "Voler !, cela" / "Voler, cela !" / "Voler ! cela" / "Voler cela !"
  Candidates printed for MANUAL classification (same taxonomy as the
  parent censuses: vocatives, finite clauses, OCR noise, noun false-INF
  excluded with cause).

Output: disloc-demonstrative-inversion_census.json with per-file sizes,
dialogue-span counts, postposed dem-with-! candidate counts, and every
candidate window. Dedup by (file, window) since spans may overlap.
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
RDM = [os.path.join(LANE, "code/side-period/corpus",
                    f"revue-deux-mondes-1841-q{n}.txt") for n in (1, 2, 3, 4)]
OUT = os.path.join(LANE, "code/crowd17/next-token",
                   "disloc-demonstrative-inversion_census.json")

GUILL = re.compile(r"«(.*?)»", re.DOTALL)
DQUOTE = re.compile(r'"([^"]{4,}?)"', re.DOTALL)
PARASPLIT = re.compile(r"\n\s*\n")
INF = re.compile(
    r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b", re.IGNORECASE)
DEM_POST = re.compile(r"\b(cela|ceci|ça|ca|cel[àa]|cec[iy])\b", re.IGNORECASE)


def dialogue_spans(text):
    """Return (kind, span, abs_start) dialogue spans; may overlap, dedup later."""
    spans = [( "guillemet", m.group(1), m.start(1))
             for m in GUILL.finditer(text)]
    spans += [("dquote", m.group(1), m.start(1))
              for m in DQUOTE.finditer(text)]
    pos = 0
    for m in PARASPLIT.finditer(text):
        para = text[pos:m.start()]
        s = para.strip()
        if s[:1] in ("—", "–"):
            spans.append(("em-dash", s,
                          pos + para.index(s)))
        pos = m.end()
    tail, s = text[pos:], text[pos:].strip()
    if s[:1] in ("—", "–"):
        spans.append(("em-dash", s, pos + tail.index(s)))
    return spans


def windows(span_text, span_kind, span_start):
    out = []
    for im in INF.finditer(span_text):
        wend = im.end() + 100
        win = span_text[im.start():wend]
        for dm in DEM_POST.finditer(win):
            if dm.start() < (im.end() - im.start()):
                continue  # demonstrative precedes the infinitive: not inversion
            bang_zone = win[:dm.end() + 20]
            if "!" not in bang_zone:
                continue  # exclamatory link not local to the construction
            out.append({
                "span_kind": span_kind,
                "inf": im.group(0).lower(),
                "inf_abs_offset": span_start + im.start(),
                "dem": dm.group(1).lower(),
                "window": win,
            })
    return out


def main():
    files, cands, seen = [], [], set()
    for p in RDM:
        name = os.path.basename(p)
        text = open(p, encoding="utf-8", errors="replace").read()
        spans = dialogue_spans(text)
        dchars = sum(len(s[1]) for s in spans)
        n_new = 0
        for kind, body, span_start in spans:
            for w in windows(body, kind, span_start):
                key = (name, w["inf_abs_offset"])
                if key in seen:
                    continue
                seen.add(key)
                w["file"] = name
                cands.append(w)
                n_new += 1
        print(f"{name}: {len(text)} chars, {len(spans)} dialogue spans, "
              f"{dchars} dialogue chars, {n_new} postposed-dem candidates")
        files.append({"file": name, "chars": len(text),
                      "dialogue_spans": len(spans),
                      "dialogue_chars": dchars,
                      "postposed_dem_candidates": n_new})
    json.dump({"files": files, "candidates": cands}, open(OUT, "w"),
              ensure_ascii=False, indent=1)
    print("wrote", OUT, "| total unique candidates:", len(cands))


if __name__ == "__main__":
    main()
