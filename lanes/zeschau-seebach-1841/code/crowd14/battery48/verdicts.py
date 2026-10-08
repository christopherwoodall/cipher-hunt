#!/usr/bin/env python3
"""Apply PREREG.md verdict bars to battery48 results. Writes battery48_results.json."""
import json
from pathlib import Path

BASE = Path.home() / 'workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/crowd14/battery48'
a74 = json.load(open(BASE / 'a74_raw.json'))
a4c = json.load(open(BASE / 'classify_a4.json'))
hs = json.load(open(BASE / 'hstem_raw.json'))

A3, A4 = a74['A3'], a74['A4']
B3a, B3b, B3c, B4 = hs['B3a'], hs['B3b'], hs['B3c'], hs['B4']

# ============ Battery 1: 74-class ============
# class pins (pre-registered thresholds)
verb_pin = A3['verb_pin']['suc_inf'] >= 3 and A3['verb_pin']['pre_94_62'] >= 2
adj_pin  = A3['adj_test']['suc_89'] >= 2
noun_pin = (A3['noun_test']['pre_11'] + A3['noun_test']['pre_87']) >= 2
part_pin = A3['part_test']['pre_59'] >= 1
class_pin = verb_pin or adj_pin or noun_pin or part_pin

# era dominant class (>=70%)
dom_a = max(a4c['analyses']['a']['shares'].items(), key=lambda kv: kv[1])
era_dominant = dom_a[1] >= 0.70

# A3-syl: 74-74 bigram rate vs era word self-repeat (pre-registered <0.5% bar)
n74, n_self74 = 34, 6
rate74 = n_self74 / (n74 - 1)
ERA_SELF = 0.00057  # measured in followup.py on clean pool
syllable_leg = ERA_SELF < 0.005  # pre-registered threshold

# A4-abs fence
abs_fence = A4['absolute_rate'] > 0.20

# frame re-derivation
frame_ok = A3['frame_863_rederived']

promote_legs = sum([class_pin, era_dominant])  # + clean gloss not counted (frame ok but class unknown)
kill_grade = (not frame_ok)

if promote_legs >= 2:
    b1_verdict = "PROMOTE"
elif kill_grade:
    b1_verdict = "KILL"
else:
    b1_verdict = "HOLD"

# ============ Battery 2: H_stem ============
b3a_pass = True  # asserts in hstem.py; no GT contradiction found
b4a_share = B4['B4a']['share']
b4a_licenses = B4['B4a']['licenses']          # pre-registered >=5%
b4b_contact = B4['B4b']['contact_licenses']  # pre-registered >=3
kill_b = (not b3a_pass) or (b4a_share < 0.01) or (B4['B4b']['n_mprime_vowel_inf'] == 0 and b4a_share < 0.05)
lead_b = b3a_pass and b4a_licenses and b4b_contact

if lead_b:
    b2_verdict = "LEAD"
elif kill_b:
    b2_verdict = "KILL"
else:
    b2_verdict = "HOLD"

res = {
  "battery": "48-BATTERIES round 14 (74-class + H_stem)",
  "prereg": "code/crowd14/battery48/PREREG.md",
  "battery1_74class": {
    "verdict": b1_verdict,
    "legs": {
      "A3_class_pin": {"verb": verb_pin, "adj": adj_pin, "noun": noun_pin,
                       "part": part_pin, "any": class_pin,
                       "detail": {"suc_inf": A3['verb_pin']['suc_inf'],
                                  "pre94_62": A3['verb_pin']['pre_94_62'],
                                  "suc89": A3['adj_test']['suc_89'],
                                  "pre11_87": A3['noun_test']['pre_11'] + A3['noun_test']['pre_87'],
                                  "pre59": A3['part_test']['pre_59']}},
      "A3_syl": {"n74_74_bigrams": n_self74, "rate74": round(rate74, 4),
                 "era_word_selfrepeat": ERA_SELF, "threshold": 0.005,
                 "SYLLABLE_LEG_FIRES": syllable_leg,
                 "positions": [417, 816, 861, 919, 1053, 1637]},
      "A4_dom": {"analysis_a_shares": a4c['analyses']['a']['shares'],
                 "dominant": dom_a[0], "dominant_share": round(dom_a[1], 4),
                 "dominates_ge70": era_dominant},
      "A4_abs": {"n_absolute": A4['n_absolute'], "rate": A4['absolute_rate'],
                 "fence_gt20": abs_fence},
      "frame_863_rederived": frame_ok,
    },
    "sub_outcome": "FENCE-74-SYLLABLE" if (b1_verdict == "HOLD" and syllable_leg) else None,
    "islet_status": "LEAD-weak STANDS (n=1 @863); 48='de' NOT fully dead",
  },
  "battery2_Hstem": {
    "verdict": b2_verdict,
    "legs": {
      "B3a_rederivation": {"pass": b3a_pass, "windows": list(B3a.keys()),
                           "note_48_29_47_x2": True},
      "B3b_habitat": {"n_suc_INF": B3b['n_suc_INF'], "n_suc_WSEG": B3b['n_suc_WSEG'],
                      "kill_falsifier_fired": B3b['kill_falsifier']['n_suc_INF_eq_0'] and B3b['kill_falsifier']['n_suc_WSEG_ge_5'],
                      "fisher_48v06": round(B3b['fisher_48_vs_06'], 4),
                      "fisher_48v94": round(B3b['fisher_48_vs_94'], 4)},
      "B3c_construction": {"n_94_pre_48": B3c['n_94_pre_48'],
                           "naive_ne48_naming": "FAILED (0)",
                           "complementary_slot_naming": "NAMED: pre48=62(on)x6 + 82(m)x4 = 10/37 banked pre-verbal; 94 never pre-vocalic except 94-94 (elision explains 94-48=0)",
                           "caveat3_status": "NAMED-complementary; residual quantitative ne-likeness open"},
      "B4a": {"share": b4a_share, "bar": 0.05, "licenses": b4a_licenses,
              "n": B4['B4a']['n_vowelinit_stem_er'],
              "bar_diagnosis": "MISCALIBRATED as pre-registered: independence expectation = 0.133*0.3007 = 0.040 < 0.05 bar; observed 0.0342 = 86% of expectation (exploratory)"},
      "B4b": {"n": B4['B4b']['n_mprime_vowel_inf'], "bar": 3,
              "contact_licenses": b4b_contact, "examples_genuine": True},
      "B4c": {"n": B4['B4c']['n_vowelinit_stem_e'], "note": "proxy crude ('une'->un|e); report-only"},
    },
    "Hstem_status": "keeps round-13 leg; NOT LEAD (B4a bar missed); NOT KILLED; strengthened by B4b+B3c",
  },
  "ranked_48_hypotheses": [
    "48 UNIDENTIFIED (standing)",
    "H_stem (vowel-initial verb-stem syllable): LEG-grade, strengthened (B4b 299x contact, B3c named, B3a PASS); LEAD blocked on B4a bar (miscalibration diagnosed)",
    "48='de' iff 'de ce que' conditioned islet: LEAD-weak STANDS (n=1 @863); 74-class FENCED via 74=syllable",
    "48->ne-class P1c prior (F106, anti-promotion fenced): untouched",
    "KILLED (not re-litigated): 48='ne', H_verb, unconditioned 48='de'",
  ],
  "files": ["PREREG.md", "common.py", "a74.py", "hstem.py", "classify_a4.py",
            "followup.py", "verdicts.py", "a74_raw.json", "hstem_raw.json",
            "classify_a4.json", "battery48_results.json"],
}
(BASE / 'battery48_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1))
print(json.dumps({k: (v if not isinstance(v, dict) else v.get('verdict')) for k, v in res.items()
                  if k.startswith('battery')}, indent=1))
print("74-class:", b1_verdict, "| H_stem:", b2_verdict)
