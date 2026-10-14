"""Inline-SVG metal surfaces used in place of product photos (replace with real photography later)."""
_n = [0]
def _id(p):
    _n[0] += 1
    return f"{p}{_n[0]}"

METALS = {
    "gold":      ["#7a5a1a", "#e9cf86", "#b8902f", "#f6e4a6", "#9a7424"],
    "rose":      ["#a8664d", "#f4cdbd", "#c98467", "#f9dccd", "#b3705a"],
    "black":     ["#0a0a0a", "#4a4a4a", "#111111", "#3a3a3a", "#050505"],
    "bronze":    ["#5e4226", "#d1ad80", "#8a643a", "#e0c096", "#6b4a2a"],
    "champagne": ["#bfa874", "#f8efd7", "#d6c28f", "#fff8e6", "#c8b27c"],
    "silver":    ["#8c8c8c", "#fafafa", "#b4b4b4", "#ffffff", "#9e9e9e"],
    "copper":    ["#4a2a16", "#c98a60", "#7a4528", "#d9a07a", "#55311b"],
}

def _defs(k, grain):
    i = _id("m")
    c = METALS[k]
    stops = "".join(f'<stop offset="{o}" stop-color="{col}"/>' for o, col in zip((0, .28, .52, .78, 1), c))
    fx = {"hair": 'baseFrequency="0.004 0.9" numOctaves="2"',
          "fine": 'baseFrequency="0.7" numOctaves="2"',
          "none": 'baseFrequency="0.02" numOctaves="1"'}[grain]
    amt = {"hair": .30, "fine": .14, "none": .0}[grain]
    d = (f'<linearGradient id="{i}g" x1="0" y1="0" x2="1" y2="1">{stops}</linearGradient>'
         f'<filter id="{i}f" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" {fx} seed="3"/>'
         f'<feColorMatrix values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 {amt*3} -{amt}"/></filter>')
    return i, d

def sheet(k, grain="hair"):
    i, d = _defs(k, grain)
    return (f'<svg class="art" viewBox="0 0 400 320" preserveAspectRatio="xMidYMid slice" role="img" aria-label="{k} metal sheet">'
            f'<defs>{d}<linearGradient id="{i}s" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#000" stop-opacity=".18"/>'
            f'<stop offset=".5" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".22"/></linearGradient></defs>'
            f'<rect width="400" height="320" fill="url(#{i}g)"/>'
            f'<rect width="400" height="320" filter="url(#{i}f)" style="mix-blend-mode:overlay"/>'
            f'<rect width="400" height="320" fill="url(#{i}s)"/></svg>')

def disc(k):
    i, d = _defs(k, "fine")
    return (f'<svg class="disc" viewBox="0 0 100 100" role="img" aria-label="{k}"><defs>{d}'
            f'<clipPath id="{i}k"><circle cx="50" cy="50" r="49"/></clipPath><radialGradient id="{i}r" cx=".3" cy=".25" r=".9"><stop offset="0" stop-color="#fff" stop-opacity=".35"/>'
            f'<stop offset=".5" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".28"/></radialGradient></defs>'
            f'<circle cx="50" cy="50" r="49" fill="url(#{i}g)"/>'
            f'<g clip-path="url(#{i}k)"><rect width="100" height="100" filter="url(#{i}f)" style="mix-blend-mode:overlay"/></g>'
            f'<circle cx="50" cy="50" r="49" fill="url(#{i}r)"/></svg>')

def mirror():
    i, d = _defs("gold", "fine")
    return (f'<svg class="art" viewBox="0 0 400 320" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Round metal mirror frame"><defs>{d}'
            f'<radialGradient id="{i}w" cx=".35" cy=".3" r=".9"><stop offset="0" stop-color="#f4f7f9"/><stop offset=".6" stop-color="#cfd8de"/><stop offset="1" stop-color="#9eaab2"/></radialGradient>'
            f'<linearGradient id="{i}b" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1ece2"/><stop offset="1" stop-color="#ddd5c4"/></linearGradient>'
            f'<filter id="{i}sh" x="-30%" y="-30%" width="160%" height="170%"><feDropShadow dx="0" dy="14" stdDeviation="12" flood-color="#000" flood-opacity=".28"/></filter>'
            f'<clipPath id="{i}c"><circle cx="200" cy="160" r="104"/></clipPath></defs>'
            f'<rect width="400" height="320" fill="url(#{i}b)"/>'
            f'<g filter="url(#{i}sh)"><circle cx="200" cy="160" r="124" fill="url(#{i}g)"/></g>'
            f'<circle cx="200" cy="160" r="124" fill="none" stroke="#fff" stroke-opacity=".35" stroke-width="2"/>'
            f'<circle cx="200" cy="160" r="106" fill="#6b4c14"/><circle cx="200" cy="160" r="104" fill="url(#{i}w)"/>'
            f'<g clip-path="url(#{i}c)"><polygon points="90,40 150,40 70,300 10,300" fill="#fff" opacity=".35"/>'
            f'<polygon points="170,40 190,40 110,300 90,300" fill="#fff" opacity=".22"/></g></svg>')

def profiles():
    i = _id("p")
    defs = rects = ""
    for x, w, k in [(46, 34, "gold"), (100, 22, "rose"), (142, 46, "black"), (208, 26, "champagne"), (254, 38, "bronze"), (312, 22, "silver")]:
        c = METALS[k]
        gid = f"{i}{k}"
        defs += (f'<linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{c[0]}"/><stop offset=".22" stop-color="{c[3]}"/>'
                 f'<stop offset=".5" stop-color="{c[2]}"/><stop offset=".8" stop-color="{c[1]}"/><stop offset="1" stop-color="{c[4]}"/></linearGradient>')
        rects += f'<rect x="{x}" y="28" width="{w}" height="264" rx="3" fill="url(#{gid})"/>'
    return (f'<svg class="art" viewBox="0 0 400 320" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Decorative metal profiles"><defs>{defs}'
            f'<linearGradient id="{i}b" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a2a2a"/><stop offset="1" stop-color="#121212"/></linearGradient></defs>'
            f'<rect width="400" height="320" fill="url(#{i}b)"/>{rects}</svg>')

def etched():
    i, d = _defs("silver", "hair")
    return (f'<svg class="art" viewBox="0 0 400 320" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Etched and hairline metal"><defs>{d}'
            f'<pattern id="{i}p" width="28" height="28" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><path d="M14 2 L26 14 L14 26 L2 14Z" fill="none" stroke="#000" stroke-opacity=".22" stroke-width="1.2"/></pattern></defs>'
            f'<rect width="400" height="320" fill="url(#{i}g)"/><rect width="400" height="320" filter="url(#{i}f)" style="mix-blend-mode:overlay"/>'
            f'<rect width="400" height="320" fill="url(#{i}p)"/></svg>')

def tex(kind):
    return {"mirror": sheet("silver", "none"), "hair": sheet("champagne", "hair"), "etch": etched()}[kind]

SW = [("Gold", "gold"), ("Rose Gold", "rose"), ("Black", "black"), ("Bronze", "bronze"),
      ("Champagne", "champagne"), ("Silver", "silver"), ("Copper", "copper")]
def swatches():
    return '<div class="swatches">' + "".join(f'<div class="sw">{disc(k)}<b>{n}</b></div>' for n, k in SW) + '</div>'
