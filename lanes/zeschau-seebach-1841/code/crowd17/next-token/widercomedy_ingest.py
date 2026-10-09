#!/usr/bin/env python3
"""Ingest for battery disloc-reinforced-comedy-widercorpus.

Widens the Scribe/Labiche comedy corpus with more full-text comedies from
fr.wikisource via the MediaWiki parse API (same method as the earlier comedy
extension ingest). Saves raw API JSON, strips HTML to plain UTF-8 text,
computes sha256, and writes provenance entries.
"""
import json, re, os, html, hashlib, subprocess, urllib.parse

UA = "cipher-hunt-lane/1.0 (research corpus ingest)"
LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
CORPUS = os.path.join(LANE, "code/side-period/corpus")
RAWDIR = os.path.join(LANE, "code/crowd17/next-token/widercomedy-ingest-raw")
os.makedirs(RAWDIR, exist_ok=True)

# (target filename, wikisource page title)
PLAYS = [
    ("scribe-charlatanisme.txt", "Le Charlatanisme"),
    ("labiche-misanthrope-auvergnat.txt", "Le Misanthrope et l'Auvergnat"),
    ("labiche-main-leste.txt", "La Main leste"),
    ("labiche-edgard-bonne.txt", "Edgard et sa bonne"),
    ("labiche-prix-martin.txt", "Le Prix Martin"),
    ("labiche-noces-bouchencoeur.txt", "Les Noces de Bouchencœur"),
    ("labiche-baron-fourchevif.txt", "Le Baron de Fourchevif"),
    ("labiche-doit-on-le-dire.txt", "Doit-on le dire ?"),
]

def fetch(page):
    enc = urllib.parse.quote(page, safe="")
    url = (f"https://fr.wikisource.org/w/api.php?action=parse&page={enc}"
           "&prop=text&redirects=1&format=json&formatversion=2")
    out = subprocess.run(["curl", "-sSL", "-A", UA, "--max-time", "120", url],
                         capture_output=True, text=True)
    return out.stdout

def strip(htmltext):
    t = htmltext
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", t, flags=re.S | re.I)
    # drop catlinks / printfooter / jump-link chrome
    t = re.sub(r'<div[^>]*class="[^"]*(?:catlinks|printfooter|jump-to-nav|mw-jump-link)[^"]*"[^>]*>.*?</div>',
               "", t, flags=re.S | re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n\n", t)
    return t.strip() + "\n"

results = []
for fname, page in PLAYS:
    raw = fetch(page)
    rawpath = os.path.join(RAWDIR, fname + ".api.json")
    open(rawpath, "w").write(raw)
    try:
        d = json.loads(raw)
        text_raw = d.get("parse", {}).get("text", "")
        title = d.get("parse", {}).get("title", page)
    except Exception as e:
        print(f"PARSE FAIL {page}: {e}")
        results.append({"file": fname, "page": page, "status": "parse-fail"})
        continue
    if not text_raw or len(text_raw) < 5000:
        print(f"THIN {page}: {len(text_raw)} raw html bytes — skipped")
        results.append({"file": fname, "page": page, "status": "thin",
                        "raw_bytes": len(text_raw)})
        continue
    text = strip(text_raw)
    # author check from the stripped header
    head = text[:800]
    m = re.search(r"(Eugène (?:Scribe|Labiche)[^,]{0,80})", head)
    author = m.group(1).strip() if m else "unknown"
    path = os.path.join(CORPUS, fname)
    open(path, "w", encoding="utf-8").write(text)
    sha = hashlib.sha256(text.encode("utf-8")).hexdigest()
    chars = len(text)
    print(f"OK {fname}: {chars} chars, sha256 {sha[:16]}…, author={author[:60]}")
    results.append({"file": fname, "page": page, "status": "ok",
                    "chars": chars, "sha256": sha, "author": author,
                    "head": head[:400]})

json.dump(results, open(os.path.join(RAWDIR, "manifest.json"), "w"),
          ensure_ascii=False, indent=1)
print("manifest:", os.path.join(RAWDIR, "manifest.json"))
