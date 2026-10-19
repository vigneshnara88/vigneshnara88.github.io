# Vignesh Narayanan — research and data

Source for my research portfolio at **[vigneshnara88.github.io](https://vigneshnara88.github.io/)**, published through GitHub Pages from [vigneshnara88/vigneshnara88.github.io](https://github.com/vigneshnara88/vigneshnara88.github.io).

The site presents selected research, data-science work, and developing questions. Each public project links to its own GitHub repository for code and documentation. Collaborative work on regression-discontinuity external validity and Kuwait air quality is represented by project summaries; the private AIPW_RD package and restricted research materials are not distributed here.

## Edit and rebuild

The site is plain HTML and CSS with a small standard-library Python generator. No package installation or JavaScript build is needed.

1. Edit project descriptions and repository links in `project-data.json`.
2. Edit page structure in `build_site.py` and styling in `assets/styles.css`.
3. Run the generator from this directory:

```powershell
python build_site.py
```

The generator updates the homepage, individual project pages, `sitemap.xml`, `robots.txt`, and `.nojekyll`. It assembles static files only; research code runs in the separate project repositories. Generated pages include canonical URLs and social-sharing metadata for `https://vigneshnara88.github.io/`.

## Preview

Open `index.html` directly, or serve this directory locally:

```powershell
python -m http.server 4173 --bind 127.0.0.1
```

Then visit `http://127.0.0.1:4173/`.

## GitHub Pages

Publish the repository's `main` branch from its root directory. The committed HTML is ready for static serving, and `.nojekyll` preserves the supplied directory structure. The public address is `https://vigneshnara88.github.io/`.

Project code belongs in the linked repositories. The website contains no source-code archives, research datasets, complaint narratives, licensed microdata, or private collaboration files.
