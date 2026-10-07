#!/usr/bin/env python3
"""Harvest Allgemeine Zeitung Jan 1841 OCR text from digiPress (BSB).
Usage: digipress_harvest.py <month> <day_start> <day_end> <outdir>
Public domain (1841). Polite delays. Uses curl via subprocess."""
import json, os, re, subprocess, sys, time, html

BASE = "https://digipress.digitale-sammlungen.de"
API = "https://api.digitale-sammlungen.de"

def curl(url, out=None, retries=3):
    cmd = ["curl", "-s", "--max-time", "45", url]
    if out:
        cmd += ["-o", out]
    for i in range(retries):
        r = subprocess.run(cmd, capture_output=not out)
        if r.returncode == 0:
            if out:
                return True
            return r.stdout.decode("utf-8", "replace")
        time.sleep(5)
    return None

def hocr_to_text(h):
    h = re.sub(r'<span class="ocr_line"[^>]*>', '\n', h)
    h = re.sub(r'<[^>]+>', ' ', h)
    h = re.sub(r'[ \t]+', ' ', h)
    h = re.sub(r'\n\s*\n+', '\n', h)
    return h.strip()

def main():
    month, d0, d1, outdir = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    os.makedirs(outdir, exist_ok=True)
    log = []
    for d in range(d0, d1 + 1):
        day_url = f"{BASE}/calendar/1841/{month}/{d}/newspaper/bsbmult00000002"
        page = curl(day_url)
        if not page:
            log.append(f"1841-{month:02d}-{d:02d}: day page FAILED"); continue
        m = re.search(r'href="(/view/[^"]+)"', page)
        if not m:
            log.append(f"1841-{month:02d}-{d:02d}: no issue link"); continue
        view_id = m.group(1).split("/view/")[1]
        man = curl(f"{API}/iiif/presentation/v2/{view_id}/manifest")
        if not man:
            log.append(f"1841-{month:02d}-{d:02d}: manifest FAILED"); continue
        try:
            doc = json.loads(man)
        except Exception:
            log.append(f"1841-{month:02d}-{d:02d}: manifest parse FAILED"); continue
        pages = []
        for c in doc["sequences"][0]["canvases"]:
            sa = c.get("seeAlso") or {}
            oid = sa.get("@id")
            if oid:
                pages.append(oid)
        texts = []
        for oid in pages:
            h = curl(oid)
            if h:
                texts.append(hocr_to_text(h))
            time.sleep(0.3)
        date = f"1841-{month:02d}-{d:02d}"
        fn = os.path.join(outdir, f"allgemeine-zeitung-augsburg-{date}.txt")
        with open(fn, "w", encoding="utf-8") as f:
            f.write(f"=== Allgemeine Zeitung (Augsburg), {d}. {month}. 1841 ===\n")
            f.write(f"=== source: digipress.digitale-sammlungen.de issue {view_id}, BSB OCR (hOCR) ===\n\n")
            f.write("\n\n".join(texts))
        log.append(f"{date}: {len(pages)} pages -> {fn} ({os.path.getsize(fn)} bytes)")
        print(log[-1], flush=True)
        time.sleep(0.5)
    with open(os.path.join(outdir, "harvest-log.txt"), "a", encoding="utf-8") as f:
        f.write("\n".join(log) + "\n")

main()
