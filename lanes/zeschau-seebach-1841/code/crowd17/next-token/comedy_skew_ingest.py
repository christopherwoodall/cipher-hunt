#!/usr/bin/env python3
"""Fetch non-comic 19th-c drama (tragedies/dramas) from fr.wikisource.

For battery gov-excl-inf-drama-comedy-skew: test whether the governed
exclamatory infinitive is comedy-drama-skewed by censusing non-comic
plays NOT previously covered (parent censused: Dumas, Hugo (Ruy Blas,
Hernani, Burgraves), Musset (Comédies et proverbes), Vigny (Chatterton);
sibling n2 added Scribe+Labiche comedies).

Retrieval: https://fr.wikisource.org/w/api.php?action=parse&page=<title>&prop=text
(raw API JSON kept under hidden_files), HTML stripped, saved under
code/side-period/corpus/ with provenance + sha256 in corpus PROVENANCE.md.
"""
import hashlib, html, json, os, re, urllib.request, urllib.parse, datetime

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
CORPUS = os.path.join(LANE, "code/side-period/corpus")
RAWDIR = os.path.expanduser(
    "~/workspace/goals/cipher-hunt-cracking-lanes/hidden_files/comedy-skew-ingest")
UA = "cipher-hunt-lane/1.0 (research corpus ingest)"

PLAYS = [
    # (wikisource page title, filename, description)
    ("Le Roi s'amuse (Hugo)", "hugo-roi-samuse.txt",
     "Victor Hugo, *Le Roi s'amuse, drame en cinq actes* (1832), fr.wikisource"),
    ("Lucrèce Borgia (Hugo)", "hugo-lucrece-borgia.txt",
     "Victor Hugo, *Lucrèce Borgia, drame* (1833), fr.wikisource"),
    ("Marie Tudor (Hugo)", "hugo-marie-tudor.txt",
     "Victor Hugo, *Marie Tudor, drame* (1833), fr.wikisource"),
    ("Angelo, tyran de Padoue (Hugo)", "hugo-angelo.txt",
     "Victor Hugo, *Angelo, tyran de Padoue, drame* (1835), fr.wikisource"),
    ("Marion Delorme", "hugo-marion-delorme.txt",
     "Victor Hugo, *Marion Delorme, drame* (1831), fr.wikisource"),
    ("Lorenzaccio", "musset-lorenzaccio.txt",
     "Alfred de Musset, *Lorenzaccio, drame* (1834), fr.wikisource"),
    ("La Dame aux camélias (Dumas fils)", "dumas-fils-dame-camelias.txt",
     "Alexandre Dumas fils, *La Dame aux camélias, drame en cinq actes* (1852), fr.wikisource"),
    ("Lucrèce (Ponsard)", "ponsard-lucrece.txt",
     "François Ponsard, *Lucrèce, tragédie* (1843), fr.wikisource"),
    ("Charlotte Corday (Ponsard)", "ponsard-charlotte-corday.txt",
     "François Ponsard, *Charlotte Corday, tragédie* (1850), fr.wikisource"),
    ("Les Vêpres siciliennes (Delavigne)", "delavigne-vepres-siciliennes.txt",
     "Casimir Delavigne, *Les Vêpres siciliennes, tragédie* (1819), fr.wikisource"),
    ("Louis XI (Delavigne)", "delavigne-louis-xi.txt",
     "Casimir Delavigne, *Louis XI, tragédie* (1832), fr.wikisource"),
    ("Marino Faliero (Delavigne)", "delavigne-marino-faliero.txt",
     "Casimir Delavigne, *Marino Faliero, tragédie* (1829), fr.wikisource"),
    ("Adrienne Lecouvreur", "scribe-adrienne-lecouvreur.txt",
     "Eugène Scribe & Ernest Legouvé, *Adrienne Lecouvreur, drame* (1849), fr.wikisource"),
    ("La Tosca", "sardou-tosca.txt",
     "Victorien Sardou, *La Tosca, drame* (1887), fr.wikisource"),
    ("Pour la couronne", "coppee-pour-la-couronne.txt",
     "François Coppée, *Pour la couronne, drame* (1895), fr.wikisource"),
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
    if "error" in d:
        return url, raw, None, d["error"]
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
    prov_lines = []
    ok, failed = 0, []
    for page, fn, desc in PLAYS:
        try:
            url, raw, text_or_err, title = fetch_html(page)
        except Exception as e:
            failed.append((page, "fetch error: %s" % e))
            continue
        slug = re.sub(r"[^a-z0-9]+", "-", fn.lower())[:60]
        with open(os.path.join(RAWDIR, "raw-%s.json" % slug), "wb") as f:
            f.write(raw)
        if text_or_err is None:
            failed.append((page, "api error: %s" % title))
            continue
        text = to_text(text_or_err)
        if len(text) < 5000:
            failed.append((page, "suspiciously short (%d chars)" % len(text)))
            continue
        dest = os.path.join(CORPUS, fn)
        with open(dest, "w", encoding="utf-8") as f:
            f.write(text)
        sha = hashlib.sha256(text.encode("utf-8")).hexdigest()
        prov_lines.append(
            "- %s: %s. Retrieved %s via fr.wikisource API action=parse "
            "(%s). sha256 %s, %d chars." % (fn, desc, now, url, sha, len(text)))
        print("OK  %-36s %d chars  sha %.12s" % (fn, len(text), sha))
        ok += 1
    print("\n%d fetched, %d failed" % (ok, len(failed)))
    for page, why in failed:
        print("FAIL %-40s %s" % (page, why))
    with open(os.path.join(RAWDIR, "PROVENANCE-comedy-skew.txt"), "w",
              encoding="utf-8") as f:
        f.write("\n".join(prov_lines) + "\n")
    return failed

if __name__ == "__main__":
    failed = main()
    raise SystemExit(1 if failed else 0)
