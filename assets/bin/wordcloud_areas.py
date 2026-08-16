"""Word cloud grouped by research area.

Each word is assigned to SE, AI or AERO by looking at which papers it appears in
and what those papers are labelled with in papers.bib — the same labels the
publications page shows. Words that no single area dominates go to the middle.

The three clusters are laid out like the Venn diagram on the introduction page:
software engineering upper left, artificial intelligence upper right, drones
below, shared vocabulary in the overlap.

Run it from anywhere — `python3 assets/bin/wordcloud_areas.py` — and it rewrites
both SVGs in place. Titles, abstracts and area labels come from the harvested
JSON in `data/` beside this file; nothing is fetched at run time.
"""

import os
import re
import math
import json
from collections import Counter, defaultdict

BIN = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(BIN)) + "/"   # repo root
HERE = BIN + "/data/"                                # harvested inputs

W = {
    " ": 278, "-": 333, "0": 556, "1": 556, "2": 556, "3": 556, "4": 556,
    "5": 556, "6": 556, "7": 556, "8": 556, "9": 556,
    "a": 556, "b": 611, "c": 556, "d": 611, "e": 556, "f": 333, "g": 611,
    "h": 611, "i": 278, "j": 278, "k": 556, "l": 278, "m": 889, "n": 611,
    "o": 611, "p": 611, "q": 611, "r": 389, "s": 556, "t": 333, "u": 611,
    "v": 556, "w": 778, "x": 556, "y": 556, "z": 500,
    "A": 722, "B": 722, "C": 722, "D": 722, "E": 667, "F": 611, "G": 778,
    "H": 722, "I": 278, "J": 556, "K": 722, "L": 611, "M": 833, "N": 722,
    "O": 778, "P": 667, "Q": 778, "R": 722, "S": 667, "T": 611, "U": 722,
    "V": 667, "W": 944, "X": 667, "Y": 667, "Z": 611,
}


def text_width(s, size):
    return sum(W.get(c, 600) for c in s) / 1000.0 * size


STOP = set("""
a about above after again against all also am an and any are as at be because been
before being below between both but by can cannot could did do does doing down during
each few for from further had has have having he her here hers herself him himself his
how i if in into is it its itself me more most my myself no nor not of off on once only
or other ought our ours ourselves out over own same she should so some such than that
the their theirs them themselves then there these they this those through to too under
until up very was we were what when where which while who whom why with would you your
yours yourself yourselves via upon within without among across toward towards per
will shall may might must much many one two three first second third new used using use
uses useful able thus hence therefore however moreover furthermore additionally
respectively et al etc ie eg paper papers study studies research researches work works
propose proposed proposes proposal present presents presented show shows shown result
results resulting approach approaches method methods methodology technique techniques
conclusion conclusions introduction abstract keywords keyword experiment experiments
experimental evaluate evaluated evaluation evaluations find finds found provide
provides provided obtain obtained different various several existing previous recent
recently current currently high higher low lower large larger small smaller good better
best number numbers amount amounts case cases time times
""".split())

# Words frequent enough to survive the cut but which say nothing about the
# research: they are the prose around the findings rather than the findings. A
# cloud of 'based', 'help' and 'relevant' describes academic writing in general,
# not this bibliography. Removed by character rather than by frequency, because
# frequency is no guide here — 'information' occurs 30 times and 'unmanned'
# twice, yet the second is the one worth showing.
STOP |= set("""
based help name quality effort relevant view information application project
source accuracy user detection feature task according step
""".split())


def normalise(tok):
    if tok.endswith(("us", "is", "ss", "ics")):
        return tok
    if tok.endswith("ies") and len(tok) > 5:
        return tok[:-3] + "y"
    if tok.endswith("s") and len(tok) > 3:
        return tok[:-1]
    return tok


ACRONYM = {
    "api": "API", "llm": "LLM", "ai": "AI", "uav": "UAV", "nc": "NC",
    "rnn": "RNN", "cnn": "CNN", "bert": "BERT", "lime": "LIME",
    "shap": "SHAP", "stpa": "STPA", "fta": "FTA", "fmea": "FMEA",
    "yolo": "YOLO", "cad": "CAD", "github": "GitHub", "gpt": "GPT",
    "3d": "3D", "2d": "2D", "iot": "IoT", "rag": "RAG", "mcp": "MCP",
    "ide": "IDE", "arp4761": "ARP4761", "arp4754a": "ARP4754A",
}


# Pairs that name one thing and read wrong apart. The original diagram writes
# them as phrases too — 'Collision Avoidance', 'Safety Analysis' — and splitting
# them scattered the halves into different corners of their circle. A pair is
# only listed here if the corpus actually uses it: each of these occurs 4 to 19
# times as adjacent words.
PHRASES = {
    ("collision", "avoidance"): "collision avoidance",
    ("safety", "analysis"): "safety analysis",
    ("reinforcement", "learning"): "reinforcement learning",
    ("requirement", "traceability"): "requirement traceability",
    ("software", "architecture"): "software architecture",
}


def tokens(text):
    keys = []
    for tok in re.findall(r"[A-Za-z][A-Za-z0-9\-]{1,}", text):
        low = tok.lower().strip("-")
        if len(low) < 3 and low not in ("ai", "3d", "2d"):
            keys.append(None)                 # a gap, so a phrase cannot span it
            continue
        if low in STOP:
            keys.append(None)
            continue
        key = ACRONYM.get(low) or ACRONYM.get(normalise(low)) or normalise(low)
        keys.append(None if key.lower() in STOP else key)

    i = 0
    while i < len(keys):
        if keys[i] is None:
            i += 1
            continue
        pair = (keys[i], keys[i + 1]) if i + 1 < len(keys) else None
        phrase = PHRASES.get(pair) if pair and pair[1] else None
        if phrase:
            yield phrase                      # the pair is consumed as one term
            i += 2
        else:
            yield keys[i]
            i += 1


def build():
    order = json.load(open(HERE + "order.json"))
    areas = json.load(open(HERE + "areas.json"))
    abs_ = {}
    for f in ("crossref.json", "openalex.json", "s2.json", "en_abs.json",
              "tr_abs.json"):
        for k, v in json.load(open(HERE + f)).items():
            if v:
                abs_[k] = v
    for f in ("en_abs.json", "tr_abs.json"):          # these win over the rest
        abs_.update({k: v for k, v in json.load(open(HERE + f)).items() if v})
    titles = {}
    titles.update(json.load(open(HERE + "en_titles.json")))
    titles.update(json.load(open(HERE + "tr_titles.json")))

    per_area = defaultdict(Counter)   # word -> area -> weight
    total = Counter()
    for o in order:
        key = o["key"]
        text = (titles.get(key) or o["title"]) + " " + abs_.get(key, "")
        tags = areas.get(key) or []
        if not tags:
            continue
        share = 1.0 / len(tags)
        for w in tokens(text):
            total[w] += 1
            for t in tags:
                per_area[w][t] += share
    return per_area, total


# A word is assigned to the area it is *disproportionately* used in, not simply
# the area it appears in most. 117 of the 138 papers are labelled SE, so raw
# share puts almost every word in SE and leaves AI with two words. Dividing by
# each area's base rate asks a fairer question: given how much SE writing there
# is overall, is this word still unusually SE?
LIFT = 1.22


# The terms the Venn diagram on the introduction page names, which this cloud
# replaces. They are what the page has always said the research is about, so
# they are drawn larger than their raw frequency earns and are never dropped for
# being rare — 'reinforcement' appears 6 times and 'unmanned' twice, yet leaving
# them out would lose the diagram's own vocabulary.
VENN = {
    "requirement", "traceability", "software", "architecture",
    "classification", "summarization", "language", "model", "LLM",
    "issue", "data", "learning", "safety", "analysis",
    "collision", "avoidance", "unmanned", "teaming", "drone",
    # The phrase forms carry the same weight as the words they replace.
    "collision avoidance", "safety analysis", "reinforcement learning",
    "requirement traceability", "software architecture",
}
# Emphasis is a floor, not a multiplier. Multiplying inflated 'software' and
# 'issue' — already the two largest words — and their extra bulk pushed 57 other
# words off the canvas. A floor leaves those two alone and instead lifts the
# diagram's quieter terms, which is where the emphasis was actually missing:
# 'reinforcement' occurs 6 times and would otherwise be set in the smallest type.
FLOOR = 0.46      # fraction of the way from the smallest size to the largest
NUDGE = 1.10


def assign(per_area, total, top=150):
    base = Counter()
    for dist in per_area.values():
        base.update(dist)
    grand = sum(base.values()) or 1.0
    prior = {a: base[a] / grand for a in base}

    # A phrase and its own halves in the same circle read as a mistake:
    # 'collision avoidance' beside 'collision' and 'avoidance' looks like the
    # cloud could not decide. A half is kept only where it still carries
    # substantial use of its own — twice the phrase's count — so 'software'
    # stays at 106 against a phrase of 19, while 'collision' at 5 does not.
    eclipsed = set()
    for (a, b), phrase in PHRASES.items():
        n = total.get(phrase, 0)
        for part in (a, b):
            if total.get(part, 0) < 2 * n:
                eclipsed.add(part)

    chosen = [w for w, _ in total.most_common(top) if w not in eclipsed]
    chosen += [w for w in VENN
               if w in total and w not in chosen and w not in eclipsed]

    out = []
    for word in chosen:
        n = total[word]
        dist = per_area[word]
        s = sum(dist.values()) or 1.0
        lifts = {a: (v / s) / prior[a] for a, v in dist.items() if prior.get(a)}
        area, best = max(lifts.items(), key=lambda kv: kv[1])
        out.append({"word": word, "n": n,
                    "area": area if best >= LIFT else "shared",
                    "share": dist[area] / s, "lift": best,
                    "venn": word in VENN})
    out.sort(key=lambda d: -d["n"])
    return out


CANVAS = (1600, 1218)
CENTRES = {                     # mirrors the introduction page's Venn diagram
    "se":     (560, 430),
    "ai":     (1040, 430),
    "aero":   (800, 790),
    "shared": (800, 555),
}
RADIUS = 400
# Words are held inside their circle. The shared cluster sits in the middle of
# all three, so it gets a much tighter radius or it would swamp the overlaps.
LIMIT = {"area": RADIUS - 12, "shared": 168}

# The lift figure says which area a word is used in most, which is not always
# where it belongs. 'reinforcement' is short for reinforcement learning applied
# to flight, so it reads correctly only in the lens where AI and drones cross;
# statistics put it in AERO alone. These pin a word to a named region, and the
# layout then requires it to fit inside every circle listed.
#
# Centres are the middle of each lens, checked to sit at least 60px inside the
# circles named and 40px clear of the third.
LENS = {
    ("se", "ai"): (800, 300),
    ("se", "aero"): (650, 640),
    ("ai", "aero"): (950, 640),
}
PIN = {
    "reinforcement learning": ("ai", "aero"),
    "collision avoidance": ("aero",),   # a flight concern, not an SE one
    # The original diagram puts this at the centre, and the corpus agrees:
    # its use is split almost evenly between SE and drones.
    "safety analysis": ("se", "ai", "aero"),
    "teaming": ("aero",),              # manned-unmanned teaming, a flight concept
    "summarization": ("ai",),          # a technique, not a drone or SE artefact
    "recommendation": ("ai",),         # code and issue recommendation, an AI technique
}
# SE is 15% lighter than the other two on purpose: pink at equal strength reads
# heavier than blue or violet, so matching them by measurement made it the
# loudest circle on the page.
FILL = {"se": "#ff9eb2", "ai": "#7cc4f7", "aero": "#9999ff"}

# The original diagram tints each overlap rather than letting the circles simply
# stack, which is what makes the three areas legible as a Venn diagram instead
# of three discs. These are sampled from research_interests.png and painted as
# clipped regions, so only the crossings change colour and the circles keep the
# wash that lets the words sit on top of them.
OVERLAP = {
    ("se", "ai"): "#c1ebdd",       # green-grey along the top
    ("se", "aero"): "#e099e0",     # mauve on the left
    ("ai", "aero"): "#99bce0",     # steel blue on the right
    ("se", "ai", "aero"): "#c1adc1",   # the centre where all three meet
}

# The SE ink was the loudest of the three despite having the *lowest* contrast
# of them — 6.64:1 against AI's 6.81 and AERO's 8.18. Red advances where blue
# and violet recede, so matching them by measurement is not enough. Darkening
# alone would have left the saturation doing the shouting, so this drops both:
# L 39 to 30 and S 69 to 48. It now measures 9.42:1, in line with the others,
# and sits back rather than jumping forward.
INK = {"se": "#712838", "ai": "#14598f", "aero": "#4438a8", "shared": "#4a4a4a"}
LABEL = {"se": "Software Engineering", "ai": "Artificial Intelligence",
         "aero": "Drone Systems"}
LABEL_SIZE = 54
LABEL_AT = {"se": (450, 58), "ai": (1150, 58), "aero": (800, 1150)}


def label_boxes():
    """Rectangles the area captions occupy, so words are placed around them."""
    out = []
    for area, (x, y) in LABEL_AT.items():
        w = text_width(LABEL[area], LABEL_SIZE)
        out.append((x - w / 2.0 - 10, y - LABEL_SIZE, x + w / 2.0 + 10, y + 14))
    return out


def layout(words, smax=72.0, smin=12.0):
    width, height = CANVAS
    hi = max(w["n"] for w in words)
    lo = min(w["n"] for w in words)

    groups = defaultdict(list)
    for w in words:
        groups[w["area"]].append(w)
    for g in groups.values():
        g.sort(key=lambda d: (not d.get("venn"), -d["n"]))

    # Round-robin across the clusters so no one cluster claims all the room
    # near the middle before the others have placed their headline words.
    queue = []
    for rank in range(max(len(g) for g in groups.values())):
        for area in ("se", "ai", "aero", "shared"):
            if rank < len(groups[area]):
                queue.append(groups[area][rank])

    # Pinned words go first. A pin is an editorial decision about where a term
    # belongs, and the region it names is often small — the centre where all
    # three circles cross is 320px across — so it has to be claimed before the
    # statistical placements fill it. 'safety analysis' was dropped entirely
    # until this, having been queued behind words that took the middle.
    queue.sort(key=lambda d: d["word"] not in PIN)

    boxes, placed, dropped = label_boxes(), [], []
    for w in queue:
        t = 0.0 if hi == lo else (w["n"] - lo) / float(hi - lo)
        size = smin + (smax - smin) * (t ** 0.60)
        if w.get("venn"):
            size = max(size * NUDGE, smin + (smax - smin) * FLOOR)
        # A pinned word is held to the circles it is pinned to; everything else
        # keeps the cluster its lift figure earned.
        # A single-area pin also has to stay *out* of the other two, or the word
        # lands in a crossing and reads as belonging to both: 'teaming' pinned to
        # AERO alone still drifted into the SE lens.
        pin = PIN.get(w["word"])
        keep_out = ()
        if pin and len(pin) == 1:
            keep_out = tuple(a for a in ("se", "ai", "aero") if a not in pin)
        if pin and len(pin) == 3:
            cx, cy = CENTRES["shared"]        # where all three cross
            must_be_in = pin
        elif pin and len(pin) > 1:
            order = ("se", "ai", "aero")
            cx, cy = LENS[tuple(a for a in order if a in pin)]
            must_be_in = pin
        elif pin:
            cx, cy = CENTRES[pin[0]]
            must_be_in = pin
        elif w["area"] == "shared":
            cx, cy = CENTRES["shared"]
            must_be_in = ("se", "ai", "aero")
        else:
            cx, cy = CENTRES[w["area"]]
            must_be_in = (w["area"],)
        limit = LIMIT["area"]

        done = False
        # Shrink rather than spill. A word that will not fit inside its own
        # circle is retried a size smaller, so each cluster stays visually
        # contained instead of bleeding into the background — which is the
        # whole point of grouping them.
        # Shrink only so far. Below about 60% of its intended size a word stops
        # looking like part of the cloud and starts looking like a stray: at 46%
        # 'reconstruction' came out at 21px beside 100px neighbours, reading as
        # an orphan in the corner. A word that cannot fit at 0.64 is dropped
        # instead, which is the better failure — the cloud is a sample, not a
        # complete index, so a missing word costs nothing while a stray one is
        # visible.
        for shrink in (1.0, 0.88, 0.76, 0.64):
            fs = size * shrink
            bw = text_width(w["word"], fs) + fs * 0.14
            bh = fs
            step = 0.0
            # A finer angular step than the 0.30 used elsewhere: a long word in a
            # crowded circle needs the spiral to sample more positions before it
            # concludes there is no room. 'recommendation' is 455px wide and does
            # fit, but the coarser walk stepped straight past every opening.
            while step < 12000:
                ang = step * 0.11
                r = 0.78 * ang
                x = cx + r * math.cos(ang) * 1.10 - bw / 2.0
                y = cy + r * math.sin(ang) * 0.90 - bh / 2.0
                step += 1.0
                if x < 6 or y < 6 or x + bw > width - 6 or y + bh > height - 6:
                    continue
                # Every corner must sit inside every circle the word belongs to,
                # not just the centre. For a word in a lens that is two circles,
                # which is what keeps it inside the crossing rather than beside
                # it. The 'shared' cluster is also held to its tighter radius.
                corners = [(px, py) for px in (x, x + bw) for py in (y, y + bh)]
                if any(math.hypot(px - CENTRES[a][0], py - CENTRES[a][1]) > limit
                       for a in must_be_in for px, py in corners):
                    continue
                if any(math.hypot(px - CENTRES[a][0], py - CENTRES[a][1]) < RADIUS
                       for a in keep_out for px, py in corners):
                    continue
                if w["area"] == "shared" and not pin and any(
                        math.hypot(px - cx, py - cy) > LIMIT["shared"]
                        for px, py in corners):
                    continue
                box = (x, y, x + bw, y + bh)
                if any(box[0] < b[2] and b[0] < box[2] and
                       box[1] < b[3] and b[1] < box[3] for b in boxes):
                    continue
                boxes.append(box)
                placed.append(dict(w, size=fs, x=x, y=y + bh * 0.78))
                done = True
                break
            if done:
                break
        if not done:
            dropped.append(w["word"])
    if dropped:
        print("  자리 없어 제외:", ", ".join(dropped))
    return placed


def render(placed):
    width, height = CANVAS
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
         f'width="{width}" height="{height}" role="img" aria-label="Word cloud of '
         f'publications grouped by research area">',
         '<rect width="100%" height="100%" fill="#f6f6f6"/>',
         '<g>']
    for area, (cx, cy) in (("se", CENTRES["se"]), ("ai", CENTRES["ai"]),
                           ("aero", CENTRES["aero"])):
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{RADIUS}" fill="{FILL[area]}" '
                 f'fill-opacity="0.62"/>')

    # Each overlap is one circle clipped by the others it crosses, so the tint
    # covers exactly the lens where they meet. Painted in order of how many
    # circles are involved, so the three-way centre lands on top of the pairs.
    o.append('<defs>')
    for area, (cx, cy) in CENTRES.items():
        if area == "shared":
            continue
        o.append(f'<clipPath id="clip-{area}">'
                 f'<circle cx="{cx}" cy="{cy}" r="{RADIUS}"/></clipPath>')
    o.append('</defs>')
    for combo, colour in sorted(OVERLAP.items(), key=lambda kv: len(kv[0])):
        head, rest = combo[0], combo[1:]
        cx, cy = CENTRES[head]
        for other in rest:                       # nest one clip per crossing
            o.append(f'<g clip-path="url(#clip-{other})">')
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{RADIUS}" fill="{colour}" '
                 f'fill-opacity="0.62"/>')
        o.append("</g>" * len(rest))
    o.append("</g>")
    o.append('<g font-family="Helvetica,Arial,sans-serif" font-weight="700">')
    for p in sorted(placed, key=lambda d: -d["size"]):
        word = (p["word"].replace("&", "&amp;").replace("<", "&lt;")
                .replace(">", "&gt;"))
        pct = int(round(p["share"] * 100))
        note = ("shared across areas" if p["area"] == "shared"
                else f'{p["area"].upper()} {pct}%')
        o.append(f'<text x="{p["x"]:.1f}" y="{p["y"]:.1f}" '
                 f'font-size="{p["size"]:.1f}" fill="{INK[p["area"]]}">{word}'
                 f'<title>{word} — {p["n"]} occurrences, {note}</title></text>')
    o.append("</g>")
    o.append('<g font-family="Helvetica,Arial,sans-serif" font-weight="700" '
             f'font-size="{LABEL_SIZE}" fill="#2b2b2b" text-anchor="middle">')
    for a in ("se","ai","aero"):
        lx, ly = LABEL_AT[a]
        o.append(f'<text x="{lx}" y="{ly}">{LABEL[a]}</text>')
    o.append("</g></svg>")
    return "\n".join(o)


def crop(body):
    """Trim the empty margin either side of the circles."""
    return (body
            .replace(f'viewBox="0 0 {CANVAS[0]} {CANVAS[1]}"',
                     'viewBox="152 4 1296 1210"')
            .replace(f'width="{CANVAS[0]}" height="{CANVAS[1]}"',
                     'width="1296" height="1210"')
            .replace('<rect width="100%" height="100%" fill="#f6f6f6"/>',
                     '<rect x="152" y="4" width="1296" height="1210" '
                     'fill="#f6f6f6"/>'))


if __name__ == "__main__":
    per_area, total = build()

    # Standalone: as many words as the circles hold.
    full = layout(assign(per_area, total, top=120), smax=72.0, smin=12.0)
    open(ROOT + "_bibliography/papers-wordcloud-areas.svg", "w",
         encoding="utf-8").write(crop(render(full)) + "\n")

    # Page: shown at 450px in the Research Interests slot, where the standalone
    # version's smallest type would land at 4px — texture, not words. Fewer
    # words set much larger keeps every one of them readable at that size.
    page_words = assign(per_area, total, top=36)
    page = layout(page_words, smax=88.0, smin=25.0)
    open(ROOT + "assets/img/research_interests_wordcloud.svg", "w",
         encoding="utf-8").write(crop(render(page)) + "\n")

    c = Counter(w["area"] for w in page_words)
    print(f"standalone: {len(full)}개 배치")
    print(f"page:       {len(page)}개 배치  {dict(c)}")
    # A Venn term absorbed into a phrase is not missing — 'collision' is present
    # as 'collision avoidance' — so report only the ones nothing covers.
    kept = {p["word"] for p in page}
    covered = set(kept)
    for (a, b), phrase in PHRASES.items():
        if phrase in kept:
            covered |= {a, b}
    print("  page에 빠진 벤 단어:",
          [w for w in VENN if w in total and w not in covered] or "없음")
