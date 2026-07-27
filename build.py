#!/usr/bin/env python3
"""
Generates every edition of the site from a single source of content.

The site ships six editions. They differ only in presentation: each one owns a
hand written style.css and nothing else. This script writes the three pages of
each edition from the CONTENT dictionary below, so the editions cannot drift
apart. Edit the text here, run `python3 build.py`, commit the result.

It also writes robots.txt, sitemap.xml and the redirect stubs that keep the old
top level URLs alive now that the canonical edition lives under /main/.

House style: no em dashes and no hyphens used as punctuation anywhere in the
copy. Hyphens that belong to a word's spelling (one-dimensional, Shotokan-ryu)
stay, because removing those would misspell the word.
"""

import pathlib
import html as _html

BASE = "https://lorebagna13.github.io/"
CANONICAL_EDITION = "main"
SITE_ROOT = pathlib.Path(__file__).parent


# ---------------------------------------------------------------------------
# Content. One copy, shared by every edition.
# ---------------------------------------------------------------------------

NAME = "Lorenzo Bagnasacco"
ROLE = "PhD Student in Nanoscience"
EMAIL = "lorenzo.bagnasacco@sns.it"
ADDRESS = ["Scuola Normale Superiore, Pisa", "Office 82, Piazza dei Cavalieri 7"]

DOI = "https://doi.org/10.1088/1751-8121/ae2995"
JREF = f'<a href="{DOI}">J. Phys. A: Math. Theor. 58 (2025)</a>'

ABOUT = [
    'Welcome to my personal website! Here you can find information about my '
    '<a href="research.html">research</a> and a bit about me as a '
    '<a href="personal.html">person</a>.',

    f'Feel free to reach out at <a href="mailto:{EMAIL}">{EMAIL}</a>. I am '
    'always happy to chat about science, games, sports, or anything in between.',
]

RESEARCH_INTRO = [
    'I am a fourth-year PhD student in Nanoscience at the '
    '<a href="https://qinfo.sns.it/">Quantum Information Group</a> of the '
    'Scuola Normale Superiore in Pisa. My research focuses on mathematical '
    'methods for quantum dynamics, at the intersection of quantum information, '
    'condensed matter physics, and control theory, with the goal of unveiling '
    'the secrets of the quantum world. Here you can visit my '
    '<a href="https://scholar.google.com/citations?user=QDUpQDgAAAAJ&amp;hl=en" '
    'target="_blank" rel="noopener noreferrer">Google Scholar profile</a>.',
]

EDUCATION = [
    dict(when="2022 to present", what="Ph.D. in Nanoscience",
         sub="Scuola Normale Superiore (SNS), Pisa, Italy"),
    dict(when="2020 to 2022", what="Master&rsquo;s Degree in Physics",
         sub="University of Pisa, Pisa, Italy",
         text='Thesis: <em><a href="https://etd.adm.unipi.it/t/etd-10032022-103621">'
              'Holonomic quantum gates in two-dimensional electron gases</a></em>'),
    dict(when="2017 to 2020", what="Bachelor&rsquo;s Degree in Physics",
         sub="University of Pisa, Pisa, Italy"),
]

PUBLICATION = dict(
    title="Formal Integration of Electron Scattering Processes via Separation "
          "of Dynamical and Geometric Contributions",
    venue="Journal of Physics A: Mathematical and Theoretical, 58 (2025)",
    doi=DOI,
    doi_label="doi:10.1088/1751-8121/ae2995",
    abstract=
        "By decoupling the geometric from the dynamical contributions in the "
        "scattering processes, we develop a method to compute the scattering "
        "matrix of electrons in a one-dimensional coherent conductor connected "
        "to two electrodes. In particular, we demonstrate that, in the "
        "high-energy regime, the transmission matrix converges to the Berry "
        "operator of the system. We showcase the method through several "
        "examples featuring different in-plane magnetic field profiles. "
        "Notably, our results reveal the possibility of achieving near-perfect "
        "spin-flip transmission, highlighting potential applications in "
        "spintronics.",
)

EXPERIENCE = [
    dict(when="2026", what="Visiting period",
         sub="University College London, London, United Kingdom",
         text="One-week research stay in Prof. Sougato Bose&rsquo;s group, where I "
              "presented a talk on my latest work and engaged in scientific "
              "networking and discussions."),
    dict(when="2026", what="Quantum Science and Technology Seasonal School",
         sub="San Miniato, Italy",
         text="Participation in the Theoretical Section (May 4 to 8) of the SNS "
              "seasonal school on quantum science and technology, organized by "
              "the Scuola Normale Superiore in collaboration with Sapienza and "
              "the Universit&agrave; di Padova."),
    dict(when="2025", what="Visiting period",
         sub="Waseda University, Tokyo, Japan",
         text="Two-month research stay in Prof. Kazuya Yuasa&rsquo;s group, working "
              "on expansion methods for quantum dynamical systems and quantum "
              "control."),
    dict(when="2025", what="ISQI 2025",
         sub="B&#281;dlewo Palace, Pozna&#324;, Poland",
         text="Contributed talk at the Symposium on Spintronics and Quantum "
              f"Information, presenting results published in {JREF}."),
    dict(when="2024", what="ConQuEr 2024", sub="Erlangen, Germany",
         text=f"Poster presentation on the results published in {JREF} at the "
              "workshop on quantum control theory, focused on mathematical "
              "challenges such as infinite-dimensional systems and Lie "
              "algebraic methods."),
    dict(when="2024", what="TQC 2024", sub="Okinawa, Japan",
         text="Participation in a leading conference on theoretical quantum "
              "information, engaging with international researchers and "
              "presenting ongoing work."),
    dict(when="2024", what="SFT 2024",
         sub="Galileo Galilei Institute, Florence, Italy",
         text="Advanced lectures on statistical field theory and quantum "
              "technologies, including topics on quantum simulation and control."),
    dict(when="2016", what="PLS-Physics Summer School", sub="Vivo d&rsquo;Orcia, Italy",
         text="A summer school for selected high school students, organized "
              "within the Sienese Scientific Degree Plan, featuring "
              "experimental workshops, problem-solving sessions, and expert "
              "seminars on physics and the laws of nature."),
]

PERSONAL_INTRO = [
    "Outside of academia, I am an avid skier and mountain biker, finding solace "
    "and inspiration in the natural beauty of the outdoors. In addition, the "
    "discipline instilled by my years of practicing karate has been "
    "instrumental in achieving many of my goals. I hold a first DAN black belt, "
    "a testament to the dedication and perseverance that this martial art has "
    "taught me.",
]

SPORTS = [
    dict(when="2004 to 2017", what="Karate", sub="First DAN black belt",
         text="Thirteen years of practice in Sh&#333;t&#333;kan-ry&#363; and "
              "G&#333;j&#363;-ry&#363; styles, including participation in "
              "national and international competitions (FIJLKAM). This "
              "experience developed discipline, perseverance, and focus."),
    dict(when="2008 to 2011", what="Roller Skating", sub="Competitive athlete",
         text="Competitive activity at club level, contributing to "
              "coordination, endurance, and competitive mindset."),
    dict(when="2003 to present", what="Skiing"),
    dict(when="On sunny Sundays", what="Mountain biking"),
]

DEVELOPMENT = [
    dict(when="2017", what="National Mathematics Olympiad (Team Final)",
         sub="Cesenatico, Italy",
         text="My team and I, representing the scientific high school "
              "&ldquo;A. Poliziano&rdquo; from Montepulciano, participated in "
              "the national final of the team mathematics olympiad."),
    dict(when="2016", what="Bocconi Math Games",
         sub="Bocconi University, Milan, Italy",
         text="I qualified and participated in the international final of the "
              "Bocconi Math Games."),
    dict(when="2008 to 2013", what="Theatrical Improvisation",
         text="Five years of improvisational theatre, improving communication "
              "skills and creativity."),
    dict(when="2013", what="Diving course",
         sub="Piscine Comunali di Chianciano Terme, Virtus Buonconvento",
         text="Diving course under the guidance of coach Emanuele Marini."),
]


# ---------------------------------------------------------------------------
# Editions. Presentation only: a font stack, a body class, a portrait.
# ---------------------------------------------------------------------------

G = "https://fonts.googleapis.com/css2?"

EDITIONS = [
    dict(dir="main", label="Main", body="t-main",
         blurb="the canonical edition",
         fonts=G + "family=Cormorant+Garamond:wght@300;400;500;600&"
                   "family=Source+Sans+3:wght@300;400;600&display=swap"),

    dict(dir="paper", label="Paper", body="t-paper",
         blurb="aged stock and iron gall ink",
         fonts=G + "family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&"
                   "family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,400&display=swap"),

    dict(dir="emerald", label="Emerald", body="t-emerald",
         blurb="Pokemon Gen III interface",
         fonts=G + "family=Press+Start+2P&family=Pixelify+Sans:wght@400;500;700&display=swap"),

    dict(dir="terminal", label="Terminal", body="t-terminal",
         blurb="green phosphor CRT",
         fonts=G + "family=IBM+Plex+Mono:ital,wght@0,400;0,500;0,600;1,400&display=swap"),

    dict(dir="blueprint", label="Blueprint", body="t-blueprint",
         blurb="cyanotype drafting sheet",
         fonts=G + "family=Roboto+Condensed:wght@300;400;700&"
                   "family=IBM+Plex+Mono:wght@400;500&display=swap"),

    dict(dir="swiss", label="Swiss", body="t-swiss",
         blurb="international typographic style",
         fonts=G + "family=Inter:wght@300;400;500;600;700&display=swap"),

    dict(dir="newspaper", label="Newspaper", body="t-newspaper",
         blurb="broadsheet front page",
         fonts=G + "family=UnifrakturMaguntia&"
                   "family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&"
                   "family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&"
                   "display=swap"),

    dict(dir="neon", label="Neon", body="t-neon",
         blurb="synthwave grid and glow",
         fonts=G + "family=Orbitron:wght@500;700;900&"
                   "family=Chakra+Petch:wght@300;400;500;600&display=swap"),

    dict(dir="glass", label="Glass", body="t-glass",
         blurb="frosted panels on a mesh gradient",
         fonts=G + "family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap"),
]

PAGES = ["index", "research", "personal"]
PAGE_LABEL = {"index": "Home", "research": "Research", "personal": "Personal"}
PAGE_TITLE = {
    "index": NAME,
    "research": f"Research &middot; {NAME}",
    "personal": f"Personal &middot; {NAME}",
}
PAGE_DESC = {
    "index": f"{NAME}, {ROLE} at the Scuola Normale Superiore in Pisa.",
    "research": "Mathematical methods for quantum dynamics: education, "
                "publications and academic experience.",
    "personal": "Sports, martial arts and other pursuits outside academia.",
}


# ---------------------------------------------------------------------------
# Rendering. Every edition receives byte identical body markup.
# ---------------------------------------------------------------------------

def entry(e):
    out = ['        <article class="entry">',
           f'          <div class="when">{e["when"]}</div>',
           '          <div class="what">',
           f'            <h3>{e["what"]}</h3>']
    if e.get("sub"):
        out.append(f'            <p class="sub">{e["sub"]}</p>')
    if e.get("text"):
        out.append(f'            <p>{e["text"]}</p>')
    out += ['          </div>', '        </article>']
    return "\n".join(out)


def section(title, blocks):
    inner = "\n".join(blocks)
    return (f'      <section>\n        <h2>{title}</h2>\n'
            f'{inner}\n      </section>')


def entries(items):
    return ('        <div class="entries">\n'
            + "\n".join(entry(e) for e in items)
            + '\n        </div>')


def paragraphs(items, indent="        "):
    return "\n".join(f'{indent}<p>{p}</p>' for p in items)


def masthead(portrait):
    address = "<br>\n            ".join(ADDRESS)
    return f"""      <header class="masthead">
        <img class="portrait" src="{portrait}" alt="Portrait of {NAME}">
        <div class="ident">
          <h1 class="name">{NAME}</h1>
          <p class="role">{ROLE}</p>
          <address class="contact">
            {address}<br>
            <a href="mailto:{EMAIL}">{EMAIL}</a>
          </address>
        </div>
      </header>"""


def body_for(page, portrait):
    if page == "index":
        return "\n\n".join([masthead(portrait),
                            section("About", [paragraphs(ABOUT)])])

    if page == "research":
        return "\n\n".join([
            '      <header class="pagehead"><h1>Research</h1></header>',
            section("Overview", [paragraphs(RESEARCH_INTRO)]),
            section("Education", [entries(EDUCATION)]),
            section("Publications", [publication()]),
            section("Academic Experience", [entries(EXPERIENCE)]),
        ])

    return "\n\n".join([
        '      <header class="pagehead"><h1>Personal</h1></header>',
        section("Overview", [paragraphs(PERSONAL_INTRO)]),
        section("Sports", [entries(SPORTS)]),
        section("Personal Development", [entries(DEVELOPMENT)]),
    ])


def publication():
    p = PUBLICATION
    return f"""        <article class="pub">
          <h3 class="pub-title">{p['title']}</h3>
          <p class="pub-meta">{p['venue']} &middot; <a href="{p['doi']}">{p['doi_label']}</a></p>
          <p class="pub-abstract"><span class="runin">Abstract.</span> {p['abstract']}</p>
        </article>"""


def nav(page):
    links = []
    for p in PAGES:
        cls = ' class="active"' if p == page else ""
        links.append(f'        <a{cls} href="{p}.html">{PAGE_LABEL[p]}</a>')
    return '      <nav class="nav">\n' + "\n".join(links) + '\n      </nav>'


def foot(ed, page):
    if ed["dir"] == CANONICAL_EDITION:
        return f'      <footer class="foot"><p>{NAME}</p></footer>'
    others = []
    for other in EDITIONS:
        if other["dir"] == ed["dir"]:
            others.append(f'<span class="here">{other["label"]}</span>')
        else:
            others.append(f'<a href="../{other["dir"]}/{page}.html">{other["label"]}</a>')
    return ('      <footer class="foot">\n'
            f'        <p class="editions-label">Editions</p>\n'
            f'        <p class="editions">{" ".join(others)}</p>\n'
            '      </footer>')


def page_html(ed, page):
    portrait = ed.get("portrait", "../photo.jpg")
    canonical = ed["dir"] == CANONICAL_EDITION
    if canonical:
        target = BASE + CANONICAL_EDITION + "/"
        if page != "index":
            target += f"{page}.html"
        head_rule = f'<link rel="canonical" href="{target}">'
    else:
        head_rule = '<meta name="robots" content="noindex, nofollow">'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
{head_rule}
<title>{PAGE_TITLE[page]}</title>
<meta name="description" content="{PAGE_DESC[page]}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{ed['fonts']}" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body class="{ed['body']}">

  <div class="page">

{nav(page)}

{body_for(page, portrait)}

{foot(ed, page)}

  </div>

</body>
</html>
"""


def stub(page):
    """Top level redirect, so URLs indexed before the move keep working."""
    target = f"{CANONICAL_EDITION}/" if page == "index" else f"{CANONICAL_EDITION}/{page}.html"
    canonical = BASE + (CANONICAL_EDITION + "/" if page == "index"
                        else f"{CANONICAL_EDITION}/{page}.html")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="refresh" content="0; url={target}">
<link rel="canonical" href="{canonical}">
<title>{PAGE_TITLE[page]}</title>
</head>
<body>
<p>This page has moved to <a href="{target}">{canonical}</a>.</p>
</body>
</html>
"""


def sitemap():
    urls = []
    for page, priority in [("index", "1.0"), ("research", "0.8"), ("personal", "0.6")]:
        loc = BASE + (CANONICAL_EDITION + "/" if page == "index"
                      else f"{CANONICAL_EDITION}/{page}.html")
        urls.append(f"""    <url>
        <loc>{loc}</loc>
        <lastmod>2026-07-27</lastmod>
        <priority>{priority}</priority>
    </url>""")
    body = "\n".join(urls)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{body}
</urlset>
"""


ROBOTS = f"""# Only the /{CANONICAL_EDITION}/ edition is meant to be indexed. Every other
# edition carries <meta name="robots" content="noindex, nofollow">.
#
# Those folders are deliberately NOT disallowed here: a crawler has to be able
# to fetch a page in order to read its noindex tag. Blocking them instead would
# let the bare URLs show up in results with no content behind them.

User-agent: *
Allow: /

Sitemap: {BASE}sitemap.xml
"""


def main():
    written = []
    for ed in EDITIONS:
        folder = SITE_ROOT / ed["dir"]
        folder.mkdir(exist_ok=True)
        for page in PAGES:
            path = folder / f"{page}.html"
            path.write_text(page_html(ed, page), encoding="utf-8")
            written.append(path)

    for page in PAGES:
        path = SITE_ROOT / f"{page}.html"
        path.write_text(stub(page), encoding="utf-8")
        written.append(path)

    for name, text in [("robots.txt", ROBOTS), ("sitemap.xml", sitemap())]:
        path = SITE_ROOT / name
        path.write_text(text, encoding="utf-8")
        written.append(path)

    for path in written:
        print("wrote", path.relative_to(SITE_ROOT))
    print(f"\n{len(written)} files, {len(EDITIONS)} editions")


if __name__ == "__main__":
    main()
