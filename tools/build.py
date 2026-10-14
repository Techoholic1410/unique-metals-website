#!/usr/bin/env python3
"""Generates the static pages. Run: python3 tools/build.py  (from repo root)."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import art
ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://techoholic1410.github.io/unique-metals-website/"
EMAIL = "askus@uniquedecorativemetals.com"
ADDRESS = "Srinivasa Complex, 145-C, Raju Naidu Street,<br>Tatabad, Sivananda Colony,<br>Coimbatore - 641012, Tamil Nadu, India"

NAV = [("index.html","Home"),("about.html","About"),("products.html","Products"),
       ("finishes.html","Finishes"),("applications.html","Applications"),("contact.html","Contact")]

def page(fname, title, desc, body, hero=None):
    nav = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h==fname else ""}>{t}</a>' for h,t in NAV)
    herohtml = ""
    if hero:
        herohtml = f'''<section class="page-hero"><div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span>{hero[0]}</nav><p class="eyebrow">{hero[1]}</p><h1>{hero[2]}</h1><p class="lead">{hero[3]}</p></div></section>'''
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#111111">
<link rel="canonical" href="{BASE}{'' if fname=='index.html' else fname}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website"><meta property="og:image" content="{BASE}assets/logo.png">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"LocalBusiness","name":"Unique Decorative Metals","url":"{BASE}","foundingDate":"2026","description":"Trader and supplier of decorative interior metal solutions across India.","address":{{"@type":"PostalAddress","streetAddress":"Srinivasa Complex, 145-C, Raju Naidu Street, Tatabad, Sivananda Colony","addressLocality":"Coimbatore","addressRegion":"Tamil Nadu","postalCode":"641012","addressCountry":"IN"}}}}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="wrap"><span>Coimbatore · Supplying interior professionals across India</span><span><a href="mailto:{EMAIL}">{EMAIL}</a></span></div></div>
<header class="site-header"><div class="wrap nav">
<a href="index.html" class="brand" aria-label="Unique Decorative Metals home"><img src="assets/logo.png" alt="Unique Decorative Metals" width="222" height="96"></a>
<button class="menu-btn" aria-label="Menu" aria-expanded="false" aria-controls="menu"><span></span><span></span><span></span></button>
<nav id="menu" class="menu" aria-label="Main">{nav}<a href="contact.html#enquiry" class="btn btn-sm">Get a Quote</a></nav>
</div></header>
<main id="main">
{herohtml}{body}
</main>
<section class="cta-band"><div class="wrap"><div><h2>Planning an interior project?</h2><p>Share your requirement and we'll respond with pricing, availability and samples.</p></div><a class="btn" href="contact.html#enquiry">Request a Quote</a></div></section>
<footer class="site-footer"><div class="wrap foot-grid">
<div><img src="assets/logo-reverse.png" alt="Unique Decorative Metals" width="217" height="88"><p>Decorative interior metal solutions for designers, architects, contractors and dealers across India.</p></div>
<div><h4>Explore</h4>{"".join(f'<a href="{h}">{t}</a>' for h,t in NAV)}</div>
<div><h4>Contact</h4><address>{ADDRESS}</address><a href="mailto:{EMAIL}">{EMAIL}</a></div>
</div><div class="wrap legal"><span>© <span id="yr">2026</span> Unique Decorative Metals. All rights reserved.</span><span>Coimbatore, Tamil Nadu, India</span></div></footer>
<script src="script.js"></script>
</body>
</html>
'''


swatches=art.swatches
# ---------------- HOME ----------------
home = f'''
<section class="hero"><div class="wrap hero-grid">
<div><p class="eyebrow">Decorative Metals · Est. 2026 · Coimbatore</p>
<h1>Metal finishes that give <em>interiors</em> their signature.</h1>
<p class="lead">We trade and supply PVD / pad coated sheets, mirror frames and decorative metal solutions to interior designers, architects, contractors and dealers across India.</p>
<div class="cta-row"><a href="contact.html#enquiry" class="btn">Request a Quote</a><a href="products.html" class="btn btn-ghost">Explore Products</a></div></div>
<div class="hero-art" aria-hidden="true">{"".join(f'<figure style="--o:{n}">{art.sheet(k)}<figcaption>{t}</figcaption></figure>' for n,(k,t) in enumerate([("gold","Gold"),("rose","Rose Gold"),("black","Black"),("champagne","Champagne")]))}</div>
</div></section>

<section class="trust"><div class="wrap trust-grid">
<div><b>Pan-India</b><span>Supply &amp; dispatch</span></div><div><b>Trade pricing</b><span>For designers &amp; dealers</span></div>
<div><b>Samples</b><span>Available on request</span></div><div><b>Custom sizes</b><span>Sourced to your brief</span></div></div></section>

<section class="section"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Our Range</p><h2>Decorative solutions for every interior</h2><p>From wall cladding to mirror frames, one dependable source for the finishes your designs call for.</p></div>
<div class="grid cards">
<article class="card"><div class="thumb">{art.sheet("gold")}</div><div class="card-body"><h3>PVD / Pad Coated Sheets</h3><p>Durable coloured stainless steel sheets for walls, lifts, furniture and ceilings.</p><a class="link" href="products.html#sheets">View details →</a></div></article>
<article class="card"><div class="thumb">{art.mirror()}</div><div class="card-body"><h3>Mirror Frames</h3><p>Premium metal frames and profiles for decorative and bathroom mirrors.</p><a class="link" href="products.html#frames">View details →</a></div></article>
<article class="card"><div class="thumb">{art.tex("hair")}</div><div class="card-body"><h3>Etched &amp; Textured Sheets</h3><p>Hairline, etched and embossed surfaces that add depth to feature walls.</p><a class="link" href="products.html#textured">View details →</a></div></article>
<article class="card"><div class="thumb">{art.profiles()}</div><div class="card-body"><h3>Profiles &amp; Accessories</h3><p>Trims, inlays and fittings matched to your sheet finish.</p><a class="link" href="products.html#profiles">View details →</a></div></article>
</div></div></section>

<section class="section dark"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Finishes</p><h2>A palette to match every design</h2></div>
{swatches()}
<p class="center"><a class="btn btn-ghost" href="finishes.html">See all finishes</a></p>
</div></section>

<section class="section"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Why Unique</p><h2>Built for the interior trade</h2></div>
<div class="grid feats">
<div class="feat"><span class="num">01</span><h3>Consistent quality</h3><p>Uniform coating and finish so large projects match from first panel to last.</p></div>
<div class="feat"><span class="num">02</span><h3>One-stop range</h3><p>Sheets, frames and accessories from a single trusted supplier.</p></div>
<div class="feat"><span class="num">03</span><h3>Pan-India logistics</h3><p>Reliable dispatch to designers, dealers and project sites nationwide.</p></div>
<div class="feat"><span class="num">04</span><h3>Trade support</h3><p>Samples, bulk pricing and guidance on the right finish for each application.</p></div>
</div></div></section>
'''

# ---------------- ABOUT ----------------
about = '''
<section class="section"><div class="wrap split">
<div><p class="eyebrow">Who We Are</p><h2>Unique by name, by finish</h2></div>
<div class="prose"><p>Unique Decorative Metals is a Coimbatore-based trading and supply house for decorative interior metal solutions, established in 2026.</p>
<p>We work with interior designers, architects, contractors and dealers across India, helping them source premium metal finishes without the usual hassle of searching, comparing and waiting.</p>
<p>From PVD and pad coated sheets to mirror frames and accessories, we focus on the details that make a space feel finished.</p></div></div></section>

<section class="section alt"><div class="wrap">
<div class="sec-head"><p class="eyebrow">What We Stand For</p><h2>Our principles</h2></div>
<div class="grid feats">
<div class="feat"><span class="num">01</span><h3>Quality first</h3><p>We supply materials we are confident will perform and look right for years.</p></div>
<div class="feat"><span class="num">02</span><h3>Transparent dealings</h3><p>Clear quotations, honest lead times and no surprises on delivery.</p></div>
<div class="feat"><span class="num">03</span><h3>Design-minded service</h3><p>We understand finishes and help you choose what suits the brief.</p></div>
<div class="feat"><span class="num">04</span><h3>Long-term relationships</h3><p>We want to be the supplier you return to on every project.</p></div>
</div></div></section>

<section class="section"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Who We Serve</p><h2>Partners across the interior industry</h2></div>
<div class="grid cards-3">
<div class="info"><h3>Interior designers &amp; architects</h3><p>Specify finishes with confidence and get samples before you commit.</p></div>
<div class="info"><h3>Contractors &amp; fabricators</h3><p>Dependable supply in the sizes and quantities your sites need.</p></div>
<div class="info"><h3>Dealers &amp; retailers</h3><p>Trade pricing and a wide range to stock for your customers.</p></div>
</div></div></section>
'''

# ---------------- PRODUCTS ----------------
def prod(id_, cls, title, body, points, finishes, alt=False):
    li = "".join(f"<li>{p}</li>" for p in points)
    tg = "".join(f"<li>{f}</li>" for f in finishes)
    return f'''<section id="{id_}" class="section{' alt' if alt else ''}"><div class="wrap prod{' rev' if alt else ''}">
<div class="thumb big">{ART[cls]}</div>
<div><p class="eyebrow">Product</p><h2>{title}</h2><p>{body}</p><ul class="ticks">{li}</ul><ul class="tags">{tg}</ul>
<a class="btn" href="contact.html?product={title.replace(' ','%20').replace('&amp;','%26')}#enquiry">Enquire about this</a></div></div></section>'''

ART={'t-gold':art.sheet('gold'),'t-mirror':art.mirror(),'t-brush':art.tex('hair'),'t-profile':art.profiles()}
products = (
 prod("sheets","t-gold","PVD / Pad Coated Sheets","Coloured stainless steel sheets finished with PVD or pad coating for a rich, lasting metallic look. A favourite for premium interiors.",
      ["Wall cladding, lift cabins, column wraps and ceilings","Furniture, partitions and door panels","Wide choice of colours and surface patterns","Sizes and thicknesses on request"],["Gold","Rose Gold","Black","Bronze","Champagne"]) +
 prod("frames","t-mirror","Mirror Frames","Metal frames and profiles that turn a plain mirror into a design statement, for living spaces, bathrooms, salons and hospitality.",
      ["Round, rectangular, arch and custom shapes","Finishes matched to your sheet range","Standard and made-to-order sizes","Suitable for residential and commercial projects"],["Round","Rectangle","Arch","Custom"],True) +
 prod("textured","t-brush","Etched &amp; Textured Sheets","Hairline, brushed, etched, embossed and patterned sheets that give feature walls and furniture visual depth and character.",
      ["Hairline and satin brushed surfaces","Etched and embossed designs","Mirror-polished options","Ideal for accents and statement surfaces"],["Hairline","Etched","Embossed","Mirror"]) +
 prod("profiles","t-profile","Profiles &amp; Accessories","The finishing touches: decorative profiles, trims, inlays and fittings, matched to your chosen finish for a seamless result.",
      ["Trims, edge profiles and inlays","Matching fittings and accessories","Coordinated with sheet colours","Supplied to specification"],["Trims","Inlays","Fittings"],True) +
 '''<section class="section"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Specifications</p><h2>Typical supply details</h2></div>
<div class="table-wrap"><table><thead><tr><th>Item</th><th>Details</th></tr></thead><tbody>
<tr><td>Base material</td><td>Stainless steel (other metals on request)</td></tr>
<tr><td>Coating</td><td>PVD / pad coating</td></tr>
<tr><td>Sheet sizes</td><td>Standard and custom sizes available</td></tr>
<tr><td>Thickness</td><td>Available in a range of gauges</td></tr>
<tr><td>Surface</td><td>Mirror, hairline, brushed, etched, embossed</td></tr>
<tr><td>Supply</td><td>Bulk and trade quantities, pan-India</td></tr>
</tbody></table></div>
<p class="note">Exact sizes, gauges and availability vary. Contact us with your requirement for a confirmed specification and quotation.</p>
</div></section>''')

# ---------------- FINISHES ----------------
finishes = f'''
<section class="section dark"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Colour Palette</p><h2>Signature colours</h2></div>
{swatches()}
<p class="note">Colours shown are illustrative; screens vary. Request physical samples for exact shades.</p></div></section>
<section class="section"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Surface Textures</p><h2>Choose the feel as well as the colour</h2></div>
<div class="grid cards-3">
<div class="info"><div class="tex">{art.tex("mirror")}</div><h3>Mirror</h3><p>High-gloss, reflective surface that amplifies light and luxury.</p></div>
<div class="info"><div class="tex">{art.tex("hair")}</div><h3>Hairline / Brushed</h3><p>Fine linear grain with a soft satin look that hides fingerprints.</p></div>
<div class="info"><div class="tex">{art.tex("etch")}</div><h3>Etched &amp; Embossed</h3><p>Patterned surfaces for dramatic feature walls and furniture.</p></div>
</div></div></section>
<section class="section alt"><div class="wrap split">
<div><p class="eyebrow">Samples</p><h2>See it before you specify it</h2></div>
<div class="prose"><p>Finishes always look different in person. Ask for physical samples and we'll arrange them for your project team or client presentation.</p><p><a class="btn" href="contact.html#enquiry">Request samples</a></p></div></div></section>
'''

# ---------------- APPLICATIONS ----------------
apps = [("Wall cladding","Feature walls and accent panels in reception, lobby and living spaces."),("Lift interiors","Durable, premium finishes for cabin walls, doors and thresholds."),
        ("Furniture &amp; joinery","Metal accents on tables, cabinets, wardrobes and shutters."),("Ceilings &amp; partitions","Metallic ceilings and partitions that define and elevate a space."),
        ("Mirrors &amp; frames","Statement frames for homes, salons, hotels and showrooms."),("Retail &amp; hospitality","Signature surfaces for stores, restaurants, hotels and offices.")]
applications = f'''
<section class="section"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Where It Goes</p><h2>Applications across residential and commercial spaces</h2></div>
<div class="grid cards-3">{"".join(f'<div class="info app"><h3>{t}</h3><p>{d}</p></div>' for t,d in apps)}</div></div></section>
<section class="section alt"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Process</p><h2>How we work with you</h2></div>
<ol class="steps">
<li><b>Share your brief</b><span>Tell us the application, finish, size and quantity.</span></li>
<li><b>Get samples &amp; quote</b><span>We send options, samples and a clear quotation.</span></li>
<li><b>Confirm order</b><span>Approve finish, specification and schedule.</span></li>
<li><b>Dispatch</b><span>Careful packing and delivery to your site or store.</span></li>
</ol></div></section>
'''

# ---------------- CONTACT ----------------
contact = f'''
<section class="section"><div class="wrap contact-grid">
<div>
<p class="eyebrow">Reach Us</p><h2>Contact details</h2>
<ul class="clist">
<li><b>Email</b><a href="mailto:{EMAIL}">{EMAIL}</a></li>
<li><b>Address</b><address>{ADDRESS}</address></li>
</ul>
<div class="map"><iframe title="Map to Unique Decorative Metals, Coimbatore" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=Srinivasa+Complex+Raju+Naidu+Street+Tatabad+Coimbatore+641012&amp;output=embed"></iframe></div>
</div>
<div id="enquiry" class="formcard"><h2>Request a quote</h2><p>Share your requirement. This opens your email app with your details filled in.</p>
<form id="enquiry-form" novalidate>
<div class="row2"><label>Name<input name="name" required autocomplete="name"></label><label>Phone<input name="phone" type="tel" required autocomplete="tel"></label></div>
<div class="row2"><label>City<input name="city" autocomplete="address-level2"></label>
<label>Product<select name="product"><option>PVD / Pad Coated Sheets</option><option>Mirror Frames</option><option>Etched &amp; Textured Sheets</option><option>Profiles &amp; Accessories</option><option>Other</option></select></label></div>
<label>Requirement (finish, size, quantity)<textarea name="msg" rows="4"></textarea></label>
<button class="btn" type="submit">Send Enquiry</button><p class="form-err" role="alert" hidden>Please enter your name and phone.</p>
</form></div></div></section>
<section class="section alt"><div class="wrap narrow">
<div class="sec-head"><p class="eyebrow">FAQ</p><h2>Common questions</h2></div>
<details><summary>Do you supply across India?</summary><p>Yes. We supply and dispatch to designers, dealers and project sites across India.</p></details>
<details><summary>Can I get samples before ordering?</summary><p>Yes. Contact us with the finishes you are considering and we will arrange samples.</p></details>
<details><summary>Do you offer custom sizes and finishes?</summary><p>We source custom sizes and finishes against your requirement. Share the details for a quotation.</p></details>
<details><summary>Do you sell to individuals or only the trade?</summary><p>We primarily serve designers, architects, contractors and dealers. Contact us to discuss your requirement.</p></details>
<details><summary>How do I get a price?</summary><p>Send your requirement through the form or by email and we will respond with a quotation.</p></details>
</div></section>
'''

pages = {
 "index.html": ("Unique Decorative Metals | PVD Coated Sheets, Mirror Frames, Interior Metals","PVD / pad coated sheets, mirror frames and decorative interior metal solutions supplied across India from Coimbatore.",home,None),
 "about.html": ("About Us | Unique Decorative Metals","Unique Decorative Metals is a Coimbatore-based supplier of decorative interior metal solutions for designers, architects and contractors.",about,("About","About Us","Unique by name, by finish","A Coimbatore trading and supply house serving the interior industry across India.")),
 "products.html": ("Products | PVD Coated Sheets & Mirror Frames | Unique Decorative Metals","Explore PVD / pad coated sheets, mirror frames, etched and textured sheets, profiles and accessories.",products,("Products","Our Range","Products","Decorative metal sheets, frames and accessories for premium interiors.")),
 "finishes.html": ("Finishes & Colours | Unique Decorative Metals","Gold, rose gold, black, bronze, champagne, silver, copper and mirror finishes in a range of textures.",finishes,("Finishes","Finishes","Finishes &amp; Colours","Colours and textures to match every design language.")),
 "applications.html": ("Applications | Unique Decorative Metals","Decorative metals for wall cladding, lift interiors, furniture, ceilings, partitions, mirrors, retail and hospitality.",applications,("Applications","Applications","Where our metals go","Residential and commercial uses across the interior industry.")),
 "contact.html": ("Contact & Quote | Unique Decorative Metals","Contact Unique Decorative Metals in Coimbatore for pricing, samples and enquiries. Request a quote by form or email.",contact,("Contact","Contact","Let's talk about your project","Request a quote, samples or advice from our Coimbatore team.")),
}
for f,(t,d,b,h) in pages.items():
    (ROOT/f).write_text(page(f,t,d,b,h), encoding="utf-8")
(ROOT/"sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f'<url><loc>{BASE}{"" if f=="index.html" else f}</loc></url>\n' for f in pages)+'</urlset>\n')
(ROOT/"robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n")
(ROOT/"assets/favicon.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#111"/><text x="32" y="46" font-family="Georgia,serif" font-style="italic" font-weight="700" font-size="44" text-anchor="middle" fill="#c9a44a">U</text></svg>')
print("built", len(pages), "pages")
