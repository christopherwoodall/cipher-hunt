# Lane state — charles-i-wight-1648
status: cracking
checkpoint: work order "test the Titus cipher against the unknown cipher's tokens"
  (2026-10-07 05:55-06:00Z) COMPLETE.
  (a) Hillier 1852 (Narrative of the attempted escapes..., London: Richard Bentley,
  1852) full text fetched from IA (narrativeattemp00hillgoog, strike 1, 413533 B);
  verbatim excerpts -> data/hillier1852-titus-cipher.txt. CORRECTION to F12's
  provenance: the 103-420/453-608/634-705 ranges are Tomokiyo's reconstruction
  (from Hillier + Poynting p.134), NOT a table printed in Hillier.
  (b) code/titus_test.py (exit 0) -> data/titus-range-test.txt: 199/200 (99.5%)
  unknown tokens fall in Titus defined zones vs 192/200 (96.0%) solved-2021 —
  ranges CANNOT discriminate (shared bipartite architecture); top-13 undefined
  tokens: 10 in series1(103-420), 3 in the assumed 1-102 letter zone.
  (c) "Life of John Barwick" (1724) fetched from IA (lifeofjohnbarwic00barw, strike 1,
  979810 B); the fuller name-code list = item "10. A Key to the foregoing Letters.",
  Appendix pp. 395-396 -> data/barwick-name-codes.txt (verbatim OCR + normalized
  reading + overlap check).
  VERDICT: Titus cipher == "The Cypher" (the unknown nomenclator) is REFUTED at
  assignment level (N19): Hillier verbatim "the numbers were changed for the use of
  every correspondent" — the Titus cipher was Titus-specific, while the unknown
  nomenclator is shared by Worsley and Prince Charles (20 shared tokens, both
  letters calling it "The Cypher"); none of the attested Titus/Hopkins figure
  numbers (315/457/546/193/714/715/688/560/351) occurs in the unknown corpus.
  The two belong to the SAME cipher FAMILY: the letter-code layer (J=King, W=Titus,
  Z=Worsley, L=Osborne, N=Whorwood) is stable across the Firebrace key (F16),
  Hillier's Titus letters, and the Hopkins letters (F10), while numbers are
  per-correspondent. Barwick explains NEITHER token 395 NOR the W-g2 group (N20);
  395's person-hood rests solely on F6's Letter-B cleartext.
  BONUS correction (F17): Hillier's printed Titus letters contain 714 (Dr. Fraizer)
  and 715 (Mrs. Whorwood) — above Tomokiyo's stated 634-705 zone; treat that bound
  as approximate.
next: (1) HIGHEST VALUE: eyes on BL Egerton MS 1788 ff.51/53/54 (the
  holograph cipher + name-code list) — in-person visit (letter of
  introduction required) or BL remote reprographics enquiry; if the
  f.53 cipher is "The Cypher", it breaks the 1 Aug / 22 May letters.
  (2) RP 9319: in-person/remote enquiry — the 66 Hopkins letters may contain an
  actual figure-name list (king sent "an addition of some Figures, with
  Names" 26 July 1648). (3) Lincolnshire YARB deposit: email enquiry
  re 17th-c. Worsley correspondence (the 1781-printed letters'
  manuscripts). (4) Only re-run cribs.py if multi-token cribbable groups surface.
  (5) NEW: the family-level architecture is now verified — letter codes stable,
  numbers per-correspondent. If any per-correspondent figure-number list surfaces
  (Egerton f.53/f.54, RP 9319, Add MS 46501), test it against the unknown tokens'
  cleartext constraints (esp. 395 = male person, the repeated bigram "230 388").
  Standing weak hypotheses: token 5->'e' (unchanged); token 395 = male
  person-code (F6, attributed); the cover note's cypher-written
  name = unrecovered token (F8); Z = Edward Worsley (F11, confirmed by F16).
blockers: []
data:
  - data/letter-worsley-1648-05-22-cipher.txt (112 cipher tokens)
  - data/letter-prince-charles-1648-08-01-cipher.txt (88 cipher tokens, verified vs manuscript)
  - data/letter-prince-charles-1648-10-03-solved-control.txt (positive control)
  - data/nomenclator-charles-i-1648-solved-key.json (+ .png source image)
  - data/letter-prince-charles-1648-08-01-manuscript.png
  - code/apply.py, code/apply-output.txt
  - code/derive.py, data/freq-analysis.txt (work order a)
  - code/cribs.py, data/crib-attempts.txt (run 2, +Phase 3), data/crib-attempts-run1-200tok.txt (run 1 archive)
  - data/letter-worsley-1648-southampton-cover-ocr.txt (run-2 sharpened reconstruction, 6253 B — NOT verbatim)
  - data/gb-tiling-2026-10-07.json (17 GB snippet queries, raw responses, 26806 B)
  - data/catalogue-hunt-2026-10-07.json (manuscript catalogue hunt search log, 11877 B)
  - data/charlesi-ciphers-tomokiyo.html (Tomokiyo "King Charles I's Ciphers", 83011 B)
  - data/a2a-worsley-cat189-top.html, -cid7.html, -cid9.html, -cid10.html (Wayback A2A Worsley catalogue evidence)
  - data/hillier1852-titus-cipher.txt (NEW: verbatim Hillier 1852 excerpts, 9276 B)
  - code/titus_test.py (NEW: Titus-range fit test, 9059 B), data/titus-range-test.txt (NEW: output, 3750 B)
  - data/barwick-name-codes.txt (NEW: Barwick 1724 key + overlap check, 6743 B)
updated: 2026-10-07T06:00:00Z
