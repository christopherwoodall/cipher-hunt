#!/usr/bin/env python3
"""Fetch remaining public-domain Scribe/Labiche comedies from fr.wikisource.

For battery disloc-reinforced-comedy-extension. Retrieval method:
  https://fr.wikisource.org/w/api.php?action=parse&page=<title>&prop=text&redirects=1&format=json&formatversion=2
(raw API JSON kept in the goal workspace hidden_files dir), HTML stripped to
plain UTF-8 text, wikisource header-nav chrome trimmed, saved under
code/side-period/corpus/ with provenance (source URL, retrieval time,
sha256) in PROVENANCE.md.
"""
import hashlib, html, json, os, re, sys, urllib.request, urllib.parse, datetime

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
CORPUS = os.path.join(LANE, "code/side-period/corpus")
RAWDIR = os.path.expanduser(
    "~/workspace/goals/cipher-hunt-cracking-lanes/hidden_files/comedy-extension-ingest")
UA = "cipher-hunt-lane/1.0 (research corpus ingest)"

PLAYS = [
    ("Le Savant (Scribe)", "scribe-le-savant.txt",
     "Eugène Scribe, *Le Savant, comédie en cinq actes* (1832), from the "
     "Dentu *Théâtre complet* transcription on fr.wikisource"),
    ("Le Lorgnon (Scribe)", "scribe-le-lorgnon.txt",
     "Eugène Scribe, *Le Lorgnon, comédie en deux actes* (1833), from the "
     "Dentu *Théâtre complet* transcription on fr.wikisource"),
    ("Le Voyage de monsieur Perrichon", "labiche-voyage-perrichon.txt",
     "Eugène Labiche & Édouard Martin, *Le Voyage de monsieur Perrichon, "
     "comédie en quatre actes* (1860), Calmann-Lévy *Théâtre complet* "
     "transcription on fr.wikisource"),
    ("La Cagnotte", "labiche-la-cagnotte.txt",
     "Eugène Labiche & Alfred Delacour, *La Cagnotte, comédie-vaudeville "
     "en cinq actes* (1864), Calmann-Lévy *Théâtre complet* (1898) "
     "transcription on fr.wikisource"),
    ("29 degrés à l'ombre", "labiche-29-degres-ombre.txt",
     "Eugène Labiche, *29 degrés à l'ombre, comédie en un acte* (1873), "
     "Calmann-Lévy *Théâtre complet*, t. 7 (1898) transcription on "
     "fr.wikisource"),
    ("L'Affaire de la rue de Lourcine", "labiche-affaire-rue-lourcine.txt",
     "Eugène Labiche, Albert Monnier & Édouard Martin, *L'Affaire de la "
     "rue de Lourcine, comédie en un acte* (1857), Calmann-Lévy "
     "*Théâtre complet* transcription on fr.wikisource"),
]

def fetch_html(page):
    q = urllib.parse.urlencode({"action": "parse", "page": page,
                                "prop": "text", "redirects": 1,
                                "format": "json", "formatversion": 2})
    url = "https://fr.wikisource.org/w/api.php?" + q
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        raw = r.read()
    d = json.loads(raw)
    return url, raw, d["parse"]["text"], d["parse"]["title"]

def to_text(html_str):
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html_str,
               flags=re.S | re.I)
    t = re.sub(r"<div class=\"(?:catlinks|printfooter|mw-jump-link)[^>]*>.*?</div>",
               " ", t, flags=re.S | re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n[ \t]*\n[ \t]*\n+", "\n\n", t)
    lines = [l.strip() for l in t.splitlines()]
    lines = [l for l in lines if l]
    return "\n".join(lines)

def main():
    os.makedirs(RAWDIR, exist_ok=True)
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    report = []
    for page, fname, desc in PLAYS:
        url, raw, html_text, title = fetch_html(page)
        raw_path = os.path.join(RAWDIR, fname + ".api.json")
        open(raw_path, "wb").write(raw)
        text = to_text(html_text)
        p = os.path.join(CORPUS, fname)
        open(p, "w", encoding="utf-8").write(text + "\n")
        sha = hashlib.sha256(open(p, "rb").read()).hexdigest()
        report.append((fname, desc, url, len(text), sha, raw_path))
        print(f"{fname}: {len(text)} chars, sha256={sha[:16]}...")
    open(os.path.join(RAWDIR, "ingest-log.txt"), "w").write(
        f"Retrieved {now} by battery worker disloc-reinforced-comedy-extension "
        f"via fr.wikisource MediaWiki parse API, User-Agent: {UA}\n")
    print("retrieval:", now)
    with open(os.path.join(LANE, "code/crowd17/next-token",
                           "comedy_extension_ingest.json"), "w") as f:
        json.dump([{"file": n, "desc": d, "url": u, "chars": c, "sha256": s,
                    "raw_api_json": r} for n, d, u, c, s, r in report],
                  f, ensure_ascii=False, indent=1)
    return report

if __name__ == "__main__":
    main()
