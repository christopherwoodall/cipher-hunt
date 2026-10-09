#!/usr/bin/env python3
r"""Census for battery disloc-demonstrative-quoted-drama.

Target: genuine dislocated demonstrative (cela/ceci/ca) + bare exclamatory
infinitive ("cela, voler !") inside QUOTED-DIALOGUE windows of the
revue-deux-mondes-1841 corpus (q1..q4) only.

Dialogue-window extraction (three forms):
  D1 guillemet quotes:  « ... » (non-greedy, DOTALL)
  D2 straight double quotes: " ... " (non-greedy, DOTALL, span >= 4 chars)
  D3 em-dash dialogue: paragraphs (blank-line separated) starting with
     — or – ; whole paragraph to next blank line. Dialogue continuations
     after an attribution ("répond X") stay inside the same paragraph.

On each dialogue span, the reused DEM/INF patterns from
disloc_demonstrative_census.py (verbatim):
  P1 (dislocation): DEM\s*[,;:] with DEM = cela|ceci|ça|cel[àa]|cec[iy],
     case-insensitive. Window = text from the demonstrative through the
     next [!?.], capped at 180 chars.
  P2 (exclamatory filter): window must contain "!" before its end.
  P3 (infinitive candidate): infinitive-shaped word
     [a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir) in the window.
Candidates are printed for MANUAL classification (same taxonomy as the
parent census: vocatives, finite clauses, "pour"-governed infinitives,
OCR noise excluded with cause).

Output: disloc-demonstrative-quoted-drama_census.json with per-file sizes,
dialogue-span counts, total dialogue chars, dem-comma hits in dialogue,
and every exclamatory candidate window.
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
RDM = [os.path.join(LANE, "code/side-period/corpus",
                    f"revue-deux-mondes-1841-q{n}.txt") for n in (1, 2, 3, 4)]
OUT = os.path.join(LANE, "code/crowd17/next-token",
                   "disloc-demonstrative-quoted-drama_census.json")

GUILL = re.compile(r"«(.*?)»", re.DOTALL)
DQUOTE = re.compile(r'"([^"]{4,}?)"', re.DOTALL)
DEM = re.compile(r"\b(cela|ceci|ça|cel[àa]|cec[iy])\s*[,;:]", re.IGNORECASE)
INF = re.compile(
    r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b", re.IGNORECASE)

def dialogue_spans(text):
    """Return (kind, span) dialogue spans; spans may overlap, dedup later."""
    spans = [( "guillemet", m.group(1)) for m in GUILL.finditer(text)]
    spans += [("dquote", m.group(1)) for m in DQUOTE.finditer(text)]
    for para in re.split(r"\n\s*\n", text):
        s = para.strip()
        if s[:1] in ("—", "–"):
            spans.append(("em-dash", s))
    return spans

def windows(span_text, span_kind):
    out = []
    for m in DEM.finditer(span_text):
        seg = span_text[m.start():m.start() + 180]
        end = re.search(r"[!?.]", seg)
        win = seg[: end.end()] if end else seg
        if "!" not in win:
            continue
        out.append({
            "span_kind": span_kind,
            "dem": m.group(1).lower(),
            "window": win,
            "inf_hits": sorted({w[0] + w[1] for w in INF.finditer(win)}),
        })
    return out

def main():
    files, cands = [], []
    for p in RDM:
        name = os.path.basename(p)
        text = open(p, encoding="utf-8", errors="replace").read()
        spans = dialogue_spans(text)
        dchars = sum(len(s[1]) for s in spans)
        n_dem = 0
        for kind, body in spans:
            n_dem += len(DEM.findall(body))
            for w in windows(body, kind):
                w["file"] = name
                cands.append(w)
        print(f"{name}: {len(text)} chars, {len(spans)} dialogue spans, "
              f"{dchars} dialogue chars, {n_dem} dem-comma hits in dialogue, "
              f"{sum(1 for c in cands if c['file']==name)} excl candidates")
        files.append({"file": name, "chars": len(text),
                      "dialogue_spans": len(spans),
                      "dialogue_chars": dchars,
                      "dem_comma_hits_in_dialogue": n_dem,
                      "excl_candidates": sum(1 for c in cands
                                             if c["file"] == name)})
    json.dump({"files": files, "candidates": cands}, open(OUT, "w"),
              ensure_ascii=False, indent=1)
    print("wrote", OUT, "| total candidates:", len(cands))

if __name__ == "__main__":
    main()
