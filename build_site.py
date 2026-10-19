"""Build the public static portfolio from project-data.json.

This assembles HTML and search metadata. It does not execute research code,
contact services, or publish the website.
"""
from pathlib import Path
from html import escape
import json

SITE = Path(__file__).resolve().parent
SITE_URL = "https://vigneshnara88.github.io/"
PROJECTS = json.loads((SITE / "project-data.json").read_text(encoding="utf-8"))


def layout(title, description, body, prefix="", path=""):
    page_title = escape(f"{title} · Vignesh Narayanan", quote=True)
    page_description = escape(description, quote=True)
    canonical_url = escape(SITE_URL + path, quote=True)
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{page_description}"><meta name="author" content="Vignesh Narayanan"><title>{page_title}</title>
<link rel="canonical" href="{canonical_url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Vignesh Narayanan">
<meta property="og:title" content="{page_title}"><meta property="og:description" content="{page_description}"><meta property="og:url" content="{canonical_url}">
<meta name="twitter:card" content="summary"><meta name="twitter:title" content="{page_title}"><meta name="twitter:description" content="{page_description}">
<link rel="stylesheet" href="{prefix}assets/styles.css"></head><body>
<a class="skip-link" href="#main">Skip to content</a><div class="site">
<header class="site-header"><a class="site-name" href="{prefix}index.html">Vignesh Narayanan<span aria-hidden="true">.</span></a>
<nav aria-label="Main navigation"><a href="{prefix}index.html#research">Research</a><a href="{prefix}index.html#data-science">Data science</a><a href="{prefix}index.html#questions">Questions</a><a href="{prefix}index.html#about">About</a><a href="https://github.com/vigneshnara88">GitHub ↗</a></nav></header>
<main id="main">{body}</main><footer class="site-footer"><span>Vignesh Narayanan · Research &amp; data</span><a href="#main">Back to top ↑</a></footer></div></body></html>'''


def write_project(project):
    actions = ""
    if project.get("external"):
        actions += f'<a class="button primary" href="{escape(project["external"], quote=True)}">View code on GitHub ↗</a>'
    body = f'''<div class="breadcrumb"><a href="../../index.html">Portfolio</a><span aria-hidden="true">/</span><span>{escape(project['category'])}</span></div>
<header class="project-header"><p class="label">{escape(project['status'])}</p><h1>{escape(project['title'])}</h1><p class="lead">{escape(project['summary'])}</p>
<dl class="project-meta"><div><dt>Area</dt><dd>{escape(project['category'])}</dd></div><div><dt>Methods &amp; tools</dt><dd>{escape(project['tools'])}</dd></div></dl>
<div class="project-actions">{actions}</div></header><div class="project-content">'''
    for section in project["sections"]:
        body += f'<section><h2>{escape(section["title"])}</h2>'
        body += "".join(f"<p>{escape(p)}</p>" for p in section.get("paragraphs", []))
        if section.get("links"):
            body += "<ul>" + "".join(f'<li><a href="{escape(link["url"], quote=True)}">{escape(link["label"])}</a></li>' for link in section["links"]) + "</ul>"
        body += "</section>"
    body += '<div class="project-bottom"><a href="../../index.html#research">← All projects</a></div></div>'
    directory = SITE / "projects" / project["slug"]
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "index.html").write_text(
        layout(project["title"], project["summary"], body, "../../", f"projects/{project['slug']}/"),
        encoding="utf-8",
    )


def project_list(category):
    cards = []
    for n, p in enumerate((p for p in PROJECTS if p["category"] == category), 1):
        cards.append(f'''<li><span class="project-number" aria-hidden="true">{n:02}</span><div><h3><a href="projects/{escape(p['slug'])}/index.html">{escape(p['title'])} <span aria-hidden="true">↗</span></a></h3><p>{escape(p['summary'])}</p><div class="project-tools">{escape(p['tools'])}</div></div><span class="project-status">{escape(p['status'])}</span></li>''')
    return '<ul class="project-list">' + "".join(cards) + '</ul>'


def build():
    for project in PROJECTS:
        write_project(project)
    body = '''<section class="intro" aria-labelledby="intro-title"><div><p class="label">Econometrics &amp; Mathematical Economics · LSE</p><h1 id="intro-title">Questions first.<br>Evidence, carefully.</h1><p class="lead">Hi, I'm Vignesh. I'm interested in causal inference, data science, and using empirical evidence to understand policy questions.</p><p class="quiet">I study how we move from patterns in data to credible conclusions—and build tools that help make that work possible.</p><a class="text-link" href="#research">Explore selected work <span aria-hidden="true">↓</span></a></div><aside class="research-note" aria-label="Research interests"><p class="eyebrow">CURRENT INTERESTS</p><p>Policy evaluation</p><p>Language &amp; measurement</p><p>Statistical learning</p><p>Research software</p></aside></section>'''
    sections = [
        ("research", "Selected research", "01 / questions & evidence", "Policy questions, empirical designs, and the limits of what a dataset can tell us.", "Selected research"),
        ("data-science", "Data science & language", "02 / methods & tools", "Building useful tools and investigating how data are generated, measured and interpreted.", "Data science"),
        ("questions", "Questions I'm developing", "03 / work in progress", "Proposals and exploratory projects that I want to take further.", "Developing research"),
        ("independent", "Independent explorations", "04 / curiosity", "Smaller investigations motivated by questions that emerged while working with data.", "Independent projects"),
    ]
    for ident, title, eyebrow, intro, category in sections:
        body += f'<section class="section" id="{ident}" aria-labelledby="{ident}-title"><div class="section-heading"><h2 id="{ident}-title">{title}</h2><span class="eyebrow">{eyebrow}</span></div><p class="section-intro">{intro}</p>{project_list(category)}</section>'
    body += '''<section class="section" id="about" aria-labelledby="about-title"><div class="section-heading"><h2 id="about-title">A little about me</h2><span class="eyebrow">05 / beyond the results</span></div><div class="about-grid"><div><p>I'm an Econometrics &amp; Mathematical Economics student at the London School of Economics, interested in further study in statistics, econometrics, machine learning or data science.</p><p>I enjoy independent exploration as much as formal research: following an identification problem, trying an unfamiliar method, or writing a small tool to make a difficult workflow easier.</p></div><div><h3>Tools I work with</h3><p class="skills">Python · R · Stata · SQL<br>Statistical modelling · NLP<br>Data preparation · Research workflows</p><a class="text-link" href="https://github.com/vigneshnara88">Find me on GitHub ↗</a></div></div><div class="folder"><h3>Personal &amp; creative</h3><p>Alongside research, I enjoy small coding projects inspired by games, family occasions and practical problems. This side of my work is kept separate from the research collection.</p></div></section>'''
    (SITE / "index.html").write_text(layout("Research & data", "Vignesh Narayanan — an LSE student exploring causal inference, data science and policy questions.", body), encoding="utf-8")
    (SITE / ".nojekyll").touch()
    urls = [SITE_URL] + [f"{SITE_URL}projects/{project['slug']}/" for project in PROJECTS]
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sitemap += "".join(f"  <url><loc>{escape(url)}</loc></url>\n" for url in urls)
    sitemap += "</urlset>\n"
    (SITE / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    (SITE / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}sitemap.xml\n", encoding="utf-8")
    print(f"Prepared {len(PROJECTS) + 1} static pages in {SITE}")


if __name__ == "__main__":
    build()
