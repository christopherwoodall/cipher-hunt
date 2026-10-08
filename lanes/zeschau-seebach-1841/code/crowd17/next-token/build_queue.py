#!/usr/bin/env python3
"""Build battery-queue.json for the crowd17 next-token pipeline.
Run from the lane root: python3 code/crowd17/next-token/build_queue.py
Re-running is idempotent: it rewrites battery-queue.json from this spec,
preserving any existing verdicts already recorded (verdicts are never
downgraded by a rebuild).
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "battery-queue.json")
LANE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))

def rp(path):
    """Lane-relative report path; assert it exists."""
    full = os.path.join(LANE, path)
    assert os.path.exists(full), f"missing report: {path}"
    return path

D = "2026-10-07"
REDTEAM = rp("code/crowd15/report_inbox/next-token-redteam.md")
FOIS = rp("code/crowd14/report_inbox/fois-battery.md")
PRIN = rp("code/crowd14/report_inbox/prin81-battery.md")

def V(id, claim, result, report, evidence, adverses=None, bars=None, date=D):
    return {"id": id, "claim": claim, "status": "verdict", "priority": None,
            "evidence": evidence, "adverses": adverses, "bars": bars,
            "verdict": {"result": result, "report": report, "date": date}}

def Q(id, claim, priority, evidence, adverses, bars):
    return {"id": id, "claim": claim, "status": "queued", "priority": priority,
            "evidence": evidence, "adverses": adverses, "bars": bars,
            "verdict": None}

targets = [
# ---------------- VERDICTS (red-team adjudicated or battery-decided) ----------------
V("fois-17", '17="fois"', "promote", FOIS,
  "4 legs (@1040 flagship 'la premiere fois', @1289 'la fois', @308 'fois que', census 3.7x); zero contradictions in 15 windows"),
V("fois-20", '20="fois"', "kill", FOIS,
  "@307 gives 'fois fois que' under 20='fois' (17='fois' per Battery 1); corpus: 91/91 'X fois que' predecessors are det/adj, zero nouns"),
V("split-20-17", "20~17 homophony", "split", FOIS,
  "0/30 shared joint frames; successor permutation p=0.0148; uniformity 15/15 necessary-but-insufficient per lane law"),
V("cela-87-11", '"cela"=87+11 (compositional)', "promote", REDTEAM,
  "P1 CONFIRM: 7x @74/163/201/461/830/1242/1403; mutual top-attraction (87->11 = 87's #1 suc); 4 clean windows + 'en cela' 3/10"),
V("prin-81", '81="prin"', "kill", PRIN,
  "prin81 battery kill verdict (see report)"),
V("le-la-adverse", '"le la" adverse vs 77="le"', "null", rp("code/crowd16/report_inbox/next-token-findings-le.md"),
  "Adverse DISSOLVED: @832 misread ('cela' tail), @1034 clause boundary, @1042 subject-article+object-pronoun; zero ungrammatical French",
  bars="adverse-dissolution: all 3 co-occurrences admit natural parses"),
V("on-84", '84="on"', "promote", REDTEAM,
  "A15 GRANT-WITH-CONDITIONS: 'qu'on en'x2 kills 'en' rival; 'mon'@166; 'l'on'x7 discriminates vs 'il'; 77-84 x7 re-derived",
  "C1: 7 'l'on' legs inherit 77='le' provisional. C2: COLLIDES with standing 62='on' STRONG LEAD (62->94 x9 'on ne' vs 84->59 x4 'on est', zero crossover) -> 62/84 collision battery REQUIRED. C3: R1/R2 fenced residuals.",
  "bar was '84=clitic (frame)'; 'on'-specific legs pin the value; all 3 bar clauses met"),
V("ce-47", '47="ce" (allophone tier)', "promote", REDTEAM,
  "A4 GRANT: Fisher p=0.0069 on 24-predecessor asymmetry; 47->46 x3, 47->11 x3 mirror 87's frames; 28-window scan zero hard contradictions",
  "@548 breaks 'never after en' (parses as 'en ce que' - bonus mirror, conditional on 24='en'); @611 'ce le ce' strained (held conditional); allophone tier only - 47 does not inherit 87's individual legs",
  "bar met on <=1-shift clause"),
V("tout-79", '79="tout"', "promote", REDTEAM,
  "A5 GRANT: 79-17 x2, 79-87-11 @460, 79-87-64 @1799, 79-80 x3; 18-window scan zero hard contradictions, 2 fenced with cause",
  "'toutefois' re-framed as syllable-inventory not clerk elision (leg survives); 'tout 80' noun reading retired per A8 re-read",
  "compositional verification battery"),
V("pour-00", '00="pour"', "promote", REDTEAM,
  "A9 GRANT: 00->86 x12, 00->33 x8; 00-46 x4 ('pour que' + subjunctive); predecessor spread preposition-like, zero det/finite-verb slots",
  "Leg (1) ('dominant pour+infinitive') DOWNGRADED to class-level: A10 stem/whole HOLD means 'pour'+bare-stem would be ungrammatical; promotion stands on 'pour que' legs + profile. @1247 'pour et/veut que' residual; @864 'a ce que pour' tension.",
  "bar (a) met via @1545 ('pour que pre[12]') and @1680 ('pour que tout [65]')"),
V("kills-48", '48="ne" / 48="de" / 48="est" / {48,94} homophone-set', "kill", rp("code/crowd16/report_inbox/next-token-pre.md"),
  "Pre-beat status: 48='ne' KILLED, 48='de' (unconditioned) KILLED, 48='est' KILLED (A7 L1: zero of 59's predicative concentration at n=38), {48,94} homophone-set KILLED. NONE of these is 94='ne' or 48='e'-letter (still open).",
  bars="distributional kill standard"),
V("split-23-26", "23~26 homophony", "split", REDTEAM,
  "A2 SPLIT GRANTED: n23=8, n26=17; shared suc-types outside anchor 0; successor-class Fisher p=0.0029 EXACT; exceeds {33,86} precedent",
  "'en ce qui [verb]' formula survives; 'concerne/regarde' value open but unattached",
  "homophony bar per {33,86} precedent"),
V("hold-09-92", "09~92 relation", "null", REDTEAM,
  "A6 HOLD CONFIRMED: 5-group identical anchor + indistinguishable successor distributions (p=0.256) vs predecessor asymmetry p=0.0455 (single-class-driven); '-ere' VALUE KILLED (finder direction confirmed wrong: frame is [09/92]-qui-er-e-65)",
  "re-test homophony at 09 n>=20",
  "split/merge bar not met either way"),
V("fait-84", '84="fait"', "kill", REDTEAM,
  "SUPERSEDED by A15: F53's masc-noun value arm for 84 KILLED; 'qui le [84-noun]' -> 'qui l'on ...' re-valued (A13); the le-finder's 'le fait est que' leg re-read under 84='on'",
  bars="supersession by granted value"),
V("parce-quen-952", '"parce qu\'en" @952 frame; 85 verb-stem', "promote", REDTEAM,
  "A3 CONFIRM: 96-87-46 x3 tails; @952->24 elision; corpus 'parce qu'en' x1 reproduced EXACTLY in Guizot t2. 85 = verb-stem candidate GRANT (frame): 'en [85]'x5 + 'que [85]er'x2",
  "85 value NOT promoted - queued for verb battery",
  "bar 3/3 met"),
V("frames-predicative", "37/32/42 predicative frames after 'est'", "promote", REDTEAM,
  "A1 GRANT: 59->37 x6, 59->32 x3, 59->42 x2 re-derived; no contradictions; no merges ({33,86} standard not met). 19: HOLD (1 physical window, finder 'x2' corrected).",
  "42 weakest (bar met exactly); 37's value unnamed (verb/adj war continues - see frame-37-reexam); corpus census figures unverified exact (order confirmed)",
  "predicative-frame bar"),
V("frames-80-89", "80/89 verb-frames; 80-vs-89 DISTINCT", "promote", REDTEAM,
  "A8 GRANT (conditional on 77='le' provisional): 'ce le [80/89]' frames; 80 verb-locked (post-'er' x4); 80-vs-89 DISTINCT granted (zero shared frames/suc-classes, p=0.0021)",
  "'tout 80' noun reading retired (pronoun+verb re-read); correction to A5 recorded",
  "verb-frame bar"),
V("unit-37-01", "37-01 unit", "promote", REDTEAM,
  "A12 GRANT (unit, not value): 3x @939/@1633/@1817, twice in byte-identical '21-64-37-01' 4-gram; 'certain' (cer-tain) compatible not proof",
  bars="unit bar (not value bar)"),
V("trigram-79-82-48", '"tout me [48-verb]" frame', "promote", REDTEAM,
  "A7: L1 (48='est') KILLED distributionally; L2 ('tout me [48-verb]') GRANTED as FRAME: 'me [48]' x4 independent of trigram, verb-compatible profile; L3 EXCLUDED",
  "value NOT promoted; R1/R2 open",
  "frame bar"),
V("valency-33", "33 que-valency", "promote", REDTEAM,
  "A10 CONFIRM: 33->46 exactly 2/25; identical '67-33-46' trigram x2; narrows 33 to que-taking infinitives. 33+29 composition: HOLD (8 windows need whole, 5 need stem; forcing orphans 20-32%)",
  "'dire' recorded as leading partial, unpromoted",
  "valency bar"),
V("par-le-set", '"par le"+substantivized infinitive (set-level)', "promote", REDTEAM,
  "A14 GRANT (set-level): 96-00-92/33/86; 33 and 86 show strong INF-signal (>=2 of 3); 92 weakest (genuinely ambiguous), rides on the set",
  "values NOT named",
  "set-level bar"),
V("frame-qui-77-84", '"qui 77-84" frame re-valued', "promote", REDTEAM,
  "A13 GRANT as re-valued ('qui l'on est [X]'): frame real (3x pre=77 trigram, '77-84-59' x2); A15 substitutes the value; F53 masc-noun arm KILLED",
  bars="frame bar (value via A15)"),
V("infclass-86", "86 INF-class", "promote", REDTEAM,
  "A9 GRANT (class-level): pre=00 x12, suc=29 x4, 33-parallel solid; subject to stem/whole caveat (class-level claim only)",
  bars="class bar"),
V("ce-45", '45="ce"', "null", REDTEAM,
  "A11 HOLD CONFIRMED: 0/22 vs 10/32 complementarity; '45-64' x3 mirror; zero contradictions; but only ~1.5 mirrored frame-types (bar needs >=2); formula French NULL",
  "needs second mirror frame-type -> queued as ce-45-mirror2",
  "mirror bar (>=2 frame-types) NOT met"),
# ---------------- QUEUED — priority 1 (promotion track) ----------------
Q("ne-94", '94="ne"', 1,
  "PROMOTE battery: 6 frames zero contradictions ('n'est' x3, 'ne me/m'' x4, 62-94 x9, 'prenne' x2); forks-finder independent lead; explains ne-distributed pair (94='ne' vs 48='e')",
  "pre-beat kills were of OTHER 48 hypotheses, not 94='ne'; R1/R2 'ne on' windows fenced per A15-C3",
  "promote iff >=2 independent 'ne'-frames parse cleanly + zero board contradictions + 'n\\'' elision frames hold"),
Q("n-e-12-48", '12="n" + 48="e" (letters)', 1,
  "PROMOTE battery: GT-anchored cross-checks ('me'=82-48 x4, 'en'=40-12 @64, 'ni'=12-34, 'ne'=12-48 x7); analytic/syllabic duality with 94='ne'",
  "48='ne'/'de'/'est' all KILLED - this is the letter reading, distinct",
  "promote iff each value has >=2 GT-anchored frames + zero contradictions"),
Q("le-77", '77="le"', 1,
  "Promotion battery: 'le la' adverse DISSOLVED (3 co-occurrences all parse); 'ce le [verb]' x2; article-like follower diversity (44 windows, top follower 7/44); A15 'l'on' re-read indirectly SUPPORTS; load-bearing for A8/A13/A15",
  "@611 'ce le ce' strain (cheapest revision 77!='le' there); @1031 '80 77 11' adverse flagged",
  "promote iff adverse windows re-parse cleanly + >=3 independent article frames + 44-window scan zero hard contradictions"),
Q("dire-33", '33="dire"', 1,
  "'67 33 46' x2 works under BOTH 67 forks only for 'dire' ('et dire que' idiom, 'veut dire que'); '47 33' x2 = 'ce [inf]'; '33 21' x3 noun-shaped; vouloir KILLED, penser weak; byte-identical 5-gram repeats suggest one infinitive",
  "BLOCKER: '33 29' x5 - if 29-8X are 'erreur'-shaped, no surviving candidate takes 'erreur'; 'faire erreur' would fit but '33 que' x2 kills 'faire'. Single-vs-set open ('33 21 67 33' chains).",
  "promote iff 29-89-84/29-82-16 word-shapes resolve + 'dire' wins idiom battery vs croire/savoir + single-infinitive test passes"),
Q("ver-78", '78="ver"', 1,
  "'er' KILLED distributionally (vs 29='er' control: 16/31 det-predecessors vs 2/45; 0/31 after 33=INF vs 5/45; OR 22.9); 'ce [78]' x7 frames force 'ver'; 'ce verdict' x2 / 'verdict' x4 (78-45)",
  "la-finder: @296 'la 78-40' votes 'er' ('l'ere'-shaped) -> positional-allophone reconciliation candidate (78='er' after 'la', 'ver' after 'ce'); word identities open beyond 'verdict'",
  "promote iff 'ce [78]' x7 all parse as 'ver'-words + distributional kill of 'er' holds + @296 reconciled"),
Q("pas-30", '30="pas"', 1,
  "Battery: ne-frames @559 ('n\\'est 30') + @1716 ('ne [V-este] 30') - the two canonical 'pas' slots; 19 windows to test",
  None,
  "promote iff both ne-frames parse as 'ne...pas' + >=1 more independent ne-frame + zero contradictions"),
Q("a-39", '39="a/a"', 1,
  "Value battery: 4 frames ('qui a' 64-39, 'est a' 59-39 x2, 03-39 x3, 'pre-a-la' 70-39-11 x2); '62 n\\'est 39' @762 supports",
  None,
  "promote iff >=2 frames parse cleanly as 'a'/'a' + zero contradictions"),
Q("collision-62-84", '62/84 "on" collision', 1,
  "A15-C2 REQUIRED battery (highest-priority adjudication follow-up): 62->94 x9 ('on ne') vs 84->59 x4 ('on est'), zero crossover; both cannot be unconditioned 'on'. Leading resolution: 84='on' discriminated by elision; 62 re-examined with 'il' rival ('il ne' x9 clean)",
  "21-62 x5 wrinkle; A15 battery never mentioned the 62 lead (scope gap)",
  "resolve iff exactly one of {62,84} holds 'on' unconditioned, with the loser's frames re-read cleanly"),
# ---------------- QUEUED — priority 2 ----------------
Q("dict-45", '45="dict"?', 2,
  "'verdict' x4 (78-45); 'ce verdict' x2 @573/@982; 45's top predecessor is 78 (4/22); feeds A11 second-mirror question",
  "45='ce' HOLD (A11) - 'dict' is the syllable rival",
  "promote iff 'verdict' frames parse + 45 contact profile matches '-dict' syllable"),
Q("ce-45-mirror2", '45="ce" second mirror frame-type', 2,
  "A11 HOLD follow-up #5: find a second mirrored frame-type beyond '45-64' x3 to meet the >=2 bar",
  "bar needs >=2 frame-types, has ~1.5",
  "promote-45='ce' iff second mirror frame-type found with >=2 windows"),
Q("stem-33-86", "33/86 stem-vs-whole", 2,
  "A10 HOLD follow-up #3: 8 windows need whole-infinitive, 5 need stem; bears on A9 leg (1) and A14's 92",
  None,
  "resolve iff stem-vs-whole adjudicated per window with <=10% orphan rate"),
Q("frame-37-reexam", "37 predicative-frame re-examination", 2,
  "CONFLICT: round-15 A1 GRANTED 59->37 x6 as predicative frames; crowd16 est-finder claims all six are S5-fenced LEFTOVER per ISLET-10 (VOID). Red-team re-adjudication required - do not decide at battery level; escalate with both counts re-derived.",
  "A1 grant vs est-finder VOID claim; la-finder's 'la 52-37-43' x2 votes adjective from a different frame; verb frames ('qui 37' x3, 'en ce qui [23/26]-37', 'que 84-24-37') live",
  "escalate to red team with re-derived fencing analysis; battery may only gather the window-level evidence"),
Q("adj-32", "32 predicative adjective", 2,
  "'qui est 32' x2 (@316/@1210, granted frames); then 94/48 + 06/par; @1415 '[52] 32' third left-context; @314 '45-64-59-32' hardens via 45='ce'",
  "'qui 32' x2 verb-position tension (no 'est'); 94/48 post-predicate slot needs the ne/expletif frame",
  "promote iff est-frames hold + 94/48 followers resolve + verb-tension adjudicated"),
Q("ent-06", '06="ent/ment"', 2,
  "Lead battery: '[X]-ent la [NOUN]' x3; 06 n=44 (function-word frequency); top follower 77='le' x6; cross-confirms 'concern-ent'; 'prennent' (70-12-06)",
  "verb-ending vs '-ment' adverb fork unresolved (both grammatical at all windows); doubled 06 in 94-82-06-06 resists 'en'",
  "promote iff stem-classification of 94/14/68 followers decides verb-vs-adverb + >=3 clean frames"),
Q("noun-26", "26 noun-vs-verb", 2,
  "'...fois, la [26]' x2 = absolute 'une fois la [N]' construction -> 26 = feminine noun (2 legs); DIRECTLY tensions 26=verb in 'en ce qui 26-37' ('concerne')",
  "one reading must give; 26~23 SPLIT granted (A2) so no homophone rescue via 23",
  "resolve iff 26 assigned one class with all windows parsing, or positional rule stated"),
Q("verb-48", "48 verb-stem", 2,
  "Defuses the 79-adverse: 'm\\'[48]' x4 (elision x4 = vowel-initial evidence), 48->'er' x2; A7-L2 frame GRANT; '[48]er ce' x2 queued",
  "value NOT promoted (frame only); 'est [pred] 48' frames need the expletif/comparative reading",
  "promote-frame iff contact profile matches verb stems vs known stems; value battery only after frame holds"),
# ---------------- QUEUED — priority 3 ----------------
Q("prof-65", "65 full profile", 3,
  "'e 65 94' x2 byte-identical exclusive; '65 qui' x3; '21 65' x4; dominates '-ere' followers (3/9); '29-40-65' x3 '[X]ere [65]' direct-object slot",
  None,
  "profile iff class assigned (noun? verb?) with >=3 frame-legs"),
Q("frame-20-62-94", '"20 62 94" frame; 62 as {48,94}-selector', 3,
  "'20 62 94' x3 (@760 'la premiere [20][62][94] est[59]'); '62 94' x9 near-fixed pair; 62 also top prev of 48 (x6) - selects BOTH ne-distributed partners; 20 feminine-noun filter (paradox noun leg)",
  "20's determiner/adjective leg (@307) unresolved - paradox stands",
  "resolve iff 62's class named + 20's noun-leg frames parse"),
Q("stem-85", "85 verb-stem value", 3,
  "A3 frame GRANT: 'en [85]' x5 + 'que [85]er' x2 (7 frame-legs); 79->85 x2 forces adjective/noun IF 79='tout' (tension to watch)",
  "85->01->29 ('er') once - verbal signal vs nominal frames",
  "promote iff value named with >=2 independent verb-stem frames"),
Q("stem-86", "86 identification", 3,
  "12 windows; '00 86 56' x4 formula; '00 86 29' x2; INF-class GRANTED (A9); 86-29 x4 infinitive stems; '86-29' substantivized infinitive ('le pouvoir'-shaped)",
  "three adverses for 86='le' (@552 'pour le est', @866, @888); 'par 86' @947 ungrammatical; value NOT named",
  "promote iff all 12 windows parse under one value + adverses answered"),
Q("frame-82-16", "82-16 collocation; 16's value", 3,
  "82-16 x11 (biggest m-cluster); 16-91 x2 sharp end; doubled 'X par X qui' frame @1196 defeats 'mais'; 16 n=28 top unknown on m-beat",
  "16's 00-follower x4 conflicts with 00='pour' AND 'm\\'a'/'m\\'est' readings - one gives",
  "resolve iff 16's class named with the doubled frame parsing"),
Q("frame-qui-47", '76/68 verb-hood ("qui ce" vs "qui se")', 3,
  "'qui-47' x2: 'qui ce [76/68]' awkward vs 'qui se [76/68]' natural IF 76/68 are verbs - strongest 'se'-alternative; feeds 47='se'-after-infinitives hypothesis",
  None,
  "resolve iff 76/68 verb-hood decided by contact profiles"),
Q("frame-29-47", '"29-47" x4 cluster', 3,
  "Systematic: @23/@1231 '29-47-33' ('...er ce [inf]'), @423, @1591; alternative: word-internal '[stem]erce' (exercer/commerce/percer)",
  None,
  "resolve iff boundary real (contact profiles) with frame split tested"),
Q("frame-vient-parvenir", '"vient de me parvenir" thirds (60/62/68)', 3,
  "98-83-82-96-21-[60/62/68] byte-identical x3; 96-21 nowhere else globally (formula-bound); thirds = 3-cell homophone-set candidate; 83='de' cross-check at 2 other windows",
  "French of 98 unconfirmed",
  "resolve iff thirds profile as homophone set (permutation test) + 83='de' cross-checks"),
# ---------------- QUEUED — priority 4 ----------------
Q("adj-19", "19 predicative", 4,
  "'ce qui est 19' @1777 (1 physical window - finder 'x2' corrected); shares 48-follower with 32",
  "single leg; adjective battery keyhole",
  "promote iff >=2 independent predicative frames"),
Q("noun-81", "81 masculine abstract noun", 4,
  "'le [81] pour [INF]' @1086 ('le motif/moyen pour...'); '81-87-11' x2 only after 77 ('le [81]. Cela...'); '67 77 81' x4 et-frame",
  "81='prin' KILLED - fresh value needed",
  "promote iff noun frames parse + 'pour [INF]' complement holds"),
Q("homophone-12-30", "12~30 homophony", 4,
  "'26 12' x4 + '26 30' x3 = 7-window same-slot pair after 'fois la [26]'; permutation-test-ready",
  None,
  "merge iff successor/predecessor distributions indistinguishable (per {33,86} precedent, reversed)"),
Q("stem-08", "08 disambiguation", 4,
  "'08 31' x3 (before finite verbs); 'et 08' x2; '...e 08' x2; @60 '08-iere' spelling-letter. Candidates {ne, se, on, spelling-letter}",
  "spelling vs clitic readings pull opposite ways",
  "resolve iff contact profile decides; do not force"),
Q("frame-76-tension", "76 gender tension", 4,
  "'le [76]' x3 vs 'la [76]' x1 + identical 5-gram '06-77-76-01-98' x2; meme/premier-type candidates; red-team eyes (67 = sole polyvalence)",
  None,
  "resolve iff one class with positional rule, or second polyvalence declared by red team only"),
Q("stem-03", "03 verb-stem", 4,
  "'[03]er' infinitive frame after F-qui-par; '03 qui 31' x2 (only replicated VERBAL-class context); 29-40 census stem",
  None,
  "promote iff >=2 verb-stem frames"),
Q("noun-43", "43 feminine noun (means/purpose)", 4,
  "'la 43 en', '43 pour que' frames; candidates {suite, condition, maniere, mesure}; 'pour que'-frame discriminates; F-qui-par edge",
  "exact value unnamed",
  "promote iff value named with 'pour que' discriminator"),
Q("frame-94-82-06-06", '"94-82-06-06" 4-gram; 06 ent/en', 4,
  "4-gram formula x2; doubled 06 resists 'en' ('ne m\\'en en est' broken); 06's value decides 'concernent' reading too",
  None,
  "resolve iff 06's value named with doubled-06 parsing"),
]

doc = {"meta": {
    "version": 1,
    "created": "2026-10-07",
    "lane": "zeschau-seebach-1841",
    "stream": "repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt)",
    "note": ("Single source of truth for the next-token battery queue. "
             "Verdicts: red-team adjudicated (A-series, code/crowd15/report_inbox/next-token-redteam.md) "
             "or battery-decided (fois-battery). Queued: pre-registered bars; workers test per BATTERY-PROTOCOL.md. "
             "Nulls regenerate work: every null verdict MUST queue 1-3 follow-ups.")},
    "targets": targets}

# Preserve existing verdicts on rebuild (never downgrade)
old = {}
if os.path.exists(OUT):
    try:
        old = {t["id"]: t for t in json.load(open(OUT))["targets"] if t.get("verdict")}
    except Exception:
        pass
for t in targets:
    if t["id"] in old and t["verdict"] is None:
        t["verdict"] = old[t["id"]]["verdict"]
        t["status"] = "verdict"

json.dump(doc, open(OUT, "w"), indent=1, ensure_ascii=False)
print(f"wrote {OUT}: {len(targets)} targets")
s = {}
for t in targets:
    k = (t["status"], t["verdict"]["result"] if t["verdict"] else f'P{t["priority"]}')
    s[k] = s.get(k, 0) + 1
for k in sorted(s, key=str):
    print(" ", k, s[k])
