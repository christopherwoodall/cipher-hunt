#!/usr/bin/env python3
"""Fetch non-comic 19th-c drama (tragedies/dramas) from fr.wikisource (v2).

Resolved page titles; subpage fallback for transclusion-based plays.
Same provenance pattern as comedy_skew_ingest.py v1.
"""
import hashlib, html, json, os, re, urllib.request, urllib.parse, datetime

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
CORPUS = os.path.join(LANE, "code/side-period/corpus")
RAWDIR = os.path.expanduser(
    "~/workspace/goals/cipher-hunt-cracking-lanes/hidden_files/comedy-skew-ingest")
UA = "cipher-hunt-lane/1.0 (research corpus ingest)"

PLAYS = [
    ("Le roi s’amuse", "hugo-roi-samuse.txt",
     "Victor Hugo, *Le Roi s'amuse, drame en cinq actes* (1832), fr.wikisource"),
    ("Lucrèce Borgia", "hugo-lucrece-borgia.txt",
     "Victor Hugo, *Lucrèce Borgia, drame* (1833), fr.wikisource"),
    ("Marie Tudor (Victor Hugo)", "hugo-marie-tudor.txt",
     "Victor Hugo, *Marie Tudor, drame* (1833), fr.wikisource"),
    ("Angelo, tyran de Padoue", "hugo-angelo.txt",
     "Victor Hugo, *Angelo, tyran de Padoue, drame* (1835), fr.wikisource"),
    ("Marion de Lorme", "hugo-marion-delorme.txt",
     "Victor Hugo, *Marion de Lorme, drame* (1831), fr.wikisource"),
    ("Lorenzaccio", "musset-lorenzaccio.txt",
     "Alfred de Musset, *Lorenzaccio, drame* (1834), fr.wikisource"),
    ("La Dame aux camélias (théâtre)", "dumas-fils-dame-camelias.txt",
     "Alexandre Dumas fils, *La Dame aux camélias, drame en cinq actes* (1852), fr.wikisource"),
    ("Le Fils naturel", "dumas-fils-fils-naturel.txt",
     "Alexandre Dumas fils, *Le Fils naturel, drame* (1858), fr.wikisource"),
    ("Adrienne Lecouvreur, drame de MM. Scribe et Legouve",
     "scribe-adrienne-lecouvreur.txt",
     "Eugène Scribe & Ernest Legouvé, *Adrienne Lecouvreur, drame* (1849), fr.wikisource"),
    ("Lucrèce (Ponsard)", "ponsard-lucrece.txt",
     "François Ponsard, *Lucrèce, tragédie* (1843), fr.wikisource"),
]

def api(params):
    u = "https://fr.wikisource.org/w/api.php?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(u, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        raw = r.read()
    return raw, json.loads(raw)

def parse_page(page):
    raw, d = api({"action": "parse", "page": page, "prop": "text",
                  "redirects": 1, "format": "json", "formatversion": 2})
    if "error" in d:
        return raw, None
    return raw, d["parse"]["text"]

def subpages(page):
    raw, d = api({"action": "query", "list": "allpages",
                  "apprefix": page + "/", "aplimit": 50,
                  "format": "json"})
    return [p["title"] for p in d["query"]["allpages"]]

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
    return "\n".join(l for l in lines if l)

def main():
    os.makedirs(RAWDIR, exist_ok=True)
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    prov, failed = [], []
    for page, fn, desc in PLAYS:
        dest = os.path.join(CORPUS, fn)
        if os.path.exists(dest):
            prov.append("EXISTS %s (kept)" % fn)
            continue
        slug = re.sub(r"[^a-z0-9]+", "-", fn.lower())[:60]
        try:
            raw, text = parse_page(page)
        except Exception as e:
            failed.append((page, "fetch error: %s" % e)); continue
        with open(os.path.join(RAWDIR, "raw-%s-main.json" % slug), "wb") as f:
            f.write(raw)
        if text is None:
            failed.append((page, "api error")); continue
        txt = to_text(text)
        if len(txt) < 3000:
            # subpage fallback
            try:
                subs = subpages(page)
            except Exception as e:
                failed.append((page, "subpage list error: %s" % e)); continue
            parts = []
            for sp in subs:
                try:
                    sraw, stext = parse_page(sp)
                except Exception:
                    continue
                if stext is None:
                    continue
                with open(os.path.join(RAWDIR, "raw-%s-%s.json" %
                                       (slug, re.sub(r"[^a-z0-9]+","-",sp)[:40])),
                          "wb") as f:
                    f.write(sraw)
                st = to_text(stext)
                if len(st) > 500:
                    parts.append(st)
            txt = "\n\n".join(parts)
        if len(txt) < 5000:
            failed.append((page, "too short after fallback (%d)" % len(txt)))
            continue
        with open(dest, "w", encoding="utf-8") as f:
            f.write(txt)
        sha = hashlib.sha256(txt.encode("utf-8")).hexdigest()
        prov.append("- %s: %s. Retrieved %s via fr.wikisource API "
                    "action=parse (page: %s). sha256 %s, %d chars."
                    % (fn, desc, now, page, sha, len(txt)))
        print("OK  %-32s %d chars  sha %.12s" % (fn, len(txt), sha))
    print("\nfetched/found: %d  failed: %d" % (len(prov), len(failed)))
    for page, why in failed:
        print("FAIL %-45s %s" % (page, why))
    with open(os.path.join(RAWDIR, "PROVENANCE-comedy-skew-v2.txt"), "w",
              encoding="utf-8") as f:
        f.write("\n".join(prov) + "\n")

if __name__ == "__main__":
    main()
