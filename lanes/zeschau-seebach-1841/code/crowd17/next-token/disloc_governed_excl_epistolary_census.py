#!/usr/bin/env python3
r"""Census for battery disloc-governed-excl-epistolary.

Target: targeted correspondence sub-corpus census for governed
exclamatory infinitives under dislocated heads.

Bar (pre-registered): ">=1 genuine re-opens the epistolary register;
confirmed zero fences the last live prose hunting ground".

Parent: battery-disloc-governed-excl-prose-recall NULL (2026-10-09):
4 prose candidates, 2 of them Nesselrode letters (anaphoric finite
declarative; OCR-artifact "en es!"); correspondence was never censused
at battery level. Its follow-up #2 pins this battery: the
correspondence sub-corpus = Nesselrode (v7-v10), Pozzo-di-Borgo (v1),
Talleyrand (memoires v1), Guizot (memoires t1/t2/t3/t5-t6), Metternich
(papiere v4/v6) — byte-pinned below. The levant-correspondence-1841-p3
file (1,714,311 chars) is NOT in this battery's set with cause: it was
not in the parent's pinned list; a recall pass can cover it later.

Head inventory (same P1/P2 taxonomy as the parent, P3b clitic-tolerant):
  H1 (primary, mirrors parent): reinforced demonstrative heads
      (celui|ceux|celle|celles)[-là/ci] , ça[-là/ci]
  H2 (extension): plain tonic demonstratives cela, ceci, ça — widened
      within "dislocated heads" since epistolary letters run rich in them.
  Tonic personal heads (moi/toi/lui...) are EXCLUDED with cause: the
      queued personal-tonic-governed-excl-prose battery owns them; not
      duplicated here.

Patterns:
  P1 (dislocation): HEAD\s*[,;:]; window = head through next [!?.]
      (inclusive), capped at 180 chars.
  P2 (exclamatory filter): window must contain "!" before its end.
  P3 (governed-infinitive, strict):
      \b(?:pour|de|d'|d\u2019|\u00e0)\s+[inf-shaped](er|ir|re|oir)\b
  P3b (clitic-tolerant): up to 2 short words between prep and infinitive.

Output: JSON with per-file counts + candidates for hand classification.
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
CORPUS = os.path.join(LANE, "code/side-period/corpus")
NT = os.path.join(LANE, "code/crowd17/next-token")

FILES = [
    "nesselrode-v7.txt", "nesselrode-v8.txt",
    "nesselrode-v9.txt", "nesselrode-v10.txt",
    "pozzo-di-borgo-correspondance-v1.txt",
    "talleyrand-memoires-v1.txt",
    "guizot-memoires-t1-gutenberg.txt", "guizot-memoires-t2-gutenberg.txt",
    "guizot-memoires-t3-gutenberg.txt", "guizot-memoires-t5-t6.txt",
    "metternich-papiere-v4.txt", "metternich-papiere-v6.txt",
]

DEM_REINF = re.compile(
    r"\b((?:celui|ceux|celle|celles)[-\u2011\u2013 ]?(?:l[àa]|ci)|"
    r"ça[-\u2011\u2013 ]?(?:l[àa]|ci))\s*[,;:]", re.IGNORECASE)
DEM_PLAIN = re.compile(
    r"\b(cela|ceci|ça)\s*[,;:]", re.IGNORECASE)
GOV_INF = re.compile(
    r"\b(?:pour|de|d'|d’|à)\s+"
    r"[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b", re.IGNORECASE)
GOV_INF_CLITIC = re.compile(
    r"\b(?:pour|de|d'|d’|à)\s+"
    r"(?:[a-zàâäçéèêëîïôöùûü']{1,5}\s+){0,2}"
    r"[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b", re.IGNORECASE)
CTRL = re.compile(
    r"\b(?:pour|de)\s+[a-zàâäçéèêëîïôöùûü']{2,}(?:er|ir|re|oir)\b[^!?.]{0,60}!",
    re.IGNORECASE)


def windows(text, fname, dem_re, tag):
    out = []
    for m in dem_re.finditer(text):
        seg = text[m.start():m.start() + 180]
        end = re.search(r"[!?.]", seg)
        win = seg[:end.end()] if end else seg
        if "!" not in win:
            continue
        g = sorted({w.group(0).lower() for w in GOV_INF.finditer(win)})
        g2 = sorted({w.group(0).lower() for w in GOV_INF_CLITIC.finditer(win)})
        if not g and not g2:
            continue
        ctx_start = max(0, m.start() - 300)
        ctx = text[ctx_start:m.start() + 380].replace("\n", "/")
        out.append({"file": fname, "head_class": tag, "offset": m.start(),
                    "head": m.group(1).lower(), "window": win,
                    "gov_inf_strict": g, "gov_inf_clitic": g2,
                    "context": ctx})
    return out


def main():
    files, cands, ctrls = [], [], []
    total, n1, n2 = 0, 0, 0
    for fname in FILES:
        p = os.path.join(CORPUS, fname)
        assert os.path.exists(p), "GATE FAIL: missing " + p
        text = open(p, encoding="utf-8", errors="replace").read()
        total += len(text)
        h1 = len(DEM_REINF.findall(text)); h2 = len(DEM_PLAIN.findall(text))
        n1 += h1; n2 += h2
        c1 = windows(text, fname, DEM_REINF, "reinforced")
        c2 = windows(text, fname, DEM_PLAIN, "plain")
        cands.extend(c1); cands.extend(c2)
        ctrl = sorted({w.group(0).lower() for w in CTRL.finditer(text)})
        ctrls.append({"file": fname, "pour_de_inf_excl_hits": len(ctrl),
                      "sample": ctrl[:5]})
        files.append({"file": fname, "chars": len(text),
                      "reinforced_head_hits": h1, "plain_head_hits": h2,
                      "gov_excl_candidates": len(c1) + len(c2)})
        print(f"{fname}: {len(text)} chars, {h1} reinf / {h2} plain head hits, "
              f"{len(c1) + len(c2)} candidates, {len(ctrl)} 'pour/de [inf] !'")
    print(f"TOTAL: {len(files)} files, {total} chars, {n1} reinforced + "
          f"{n2} plain head hits, {len(cands)} candidates")
    out = os.path.join(NT, "disloc-governed-excl-epistolary_census.json")
    json.dump({"corpus_files": files, "total_chars": total,
               "reinforced_head_hits": n1, "plain_head_hits": n2,
               "register_control": ctrls, "candidates": cands,
               "note": "correspondence sub-corpus pinned per parent "
                       "battery's follow-up #2; levant-correspondence-1841-p3 "
                       "excluded (not in parent's list); tonic-personal heads "
                       "excluded (personal-tonic-governed-excl-prose's venue)"},
              open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)


if __name__ == "__main__":
    main()
