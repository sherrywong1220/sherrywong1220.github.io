# Agent Guidelines · Xi (Sherry) Wang's homepage

Read this file before making changes. This repository is a personal academic website built from the al-folio v1 starter. These site-specific instructions take precedence over upstream starter documentation.

## Scope and ownership

- See [README.md](README.md) for dependency setup and local preview. The local `baseurl` is empty; do not use the upstream starter's `/al-folio` path.
- `origin` is `sherrywong1220/sherrywong1220.github.io`. `upstream` is read-only for al-folio provenance. Never push or open a PR to upstream for personal-site changes.
- Keep generated output, dependencies, and local preview state out of Git. No remote publication is authorized by an ordinary local content edit.
- Verify biographical and publication facts against [docs/CONTENT_SOURCES.md](docs/CONTENT_SOURCES.md).
- Runtime layouts, includes, Liquid tags, and feature code live in versioned gems. Check the owning gem before changing runtime behavior.
- `_sass/_site.scss` and the one-line addition to `assets/css/main.scss` are intentional site customizations. Preserve `.al-folio-overrides.yml` and review the override when upgrading the theme.
- Plugin dependency and activation changes must stay aligned in both `Gemfile` and `_config.yml`. A feature may also require a site flag and page opt-in.
- Do not introduce a separate Tailwind or CSS build pipeline.

## Content files

| Content                                 | File                            |
| --------------------------------------- | ------------------------------- |
| Homepage biography and sections         | `_pages/about.md`               |
| Research                                | `_pages/research.md`            |
| Industry experience                     | `_data/experience.yml`          |
| Publication metadata, links, and BibTeX | `_bibliography/papers.bib`      |
| Publications page structure             | `_pages/publications.md`        |
| Email, Scholar, and LinkedIn            | `_data/socials.yml`             |
| Site configuration                      | `_config.yml`                   |
| Portrait                                | `assets/img/xi-sherry-wang.jpg` |
| Colors and layout                       | `_sass/_site.scss`              |

The homepage and Publications page share the same bibliography and display entries in `papers.bib` order. When adding a paper, update the expected publication keys in `scripts/check_site.py`.

## 排版原则

采用居中窄版、桌面左文右图的结构，阅读宽度为 860px。浅色模式使用白底与酒红色 `#8c1515`，正文使用 Inter，辅助信息使用 Ubuntu Mono。保留 al-folio 的导航、论文管理、深浅色切换和响应式布局。

## Validation

Run from the repository root with the project Ruby environment configured as described in README:

```bash
npm run lint:prettier
bundle exec al-folio upgrade audit --no-fail
bundle exec al-folio upgrade overrides audit
bundle exec jekyll build
python3 scripts/check_site.py _site
```

Review affected pages in the browser before publishing; for layout changes, check desktop and mobile views. Upstream demo integration and screenshot tests were removed because they depend on demo content. Do not run upstream commands such as `lint:style-contract` or `test:visual`, which are not defined in this site's `package.json`.

For documentation-only changes, check formatting and referenced local paths. README, AGENTS, and `docs/` are excluded from the website build, so these changes do not require a site rebuild or Pages deployment.

## Publishing and hosting

Source lives on `main`; static output lives on `gh-pages`. Once publication is authorized, commit and push source changes, then publish:

```bash
git push origin main
./scripts/publish
```

The script requires a clean `main` branch whose HEAD matches GitHub. It builds with the production URL, checks pages and local links, and updates `gh-pages` with a normal Git commit. Check the final deployment in [GitHub Actions](https://github.com/sherrywong1220/sherrywong1220.github.io/actions).

- GitHub Pages source: **Deploy from a branch → `gh-pages` → `/ (root)`**.
- The custom build workflow in `.github/workflows/deploy.yml` is disabled. Pushing `main` alone does not deploy the website.
- For documentation-only updates, synchronize source when authorized; do not run `scripts/publish`.
- The production domain is `xisherry.wang`; Porkbun manages DNS. Preserve the root `CNAME` file and GitHub Pages **Enforce HTTPS**.
- Keep the production URL in `scripts/publish` consistent with the custom domain. The local `_config.yml` uses an empty URL and baseurl.
- The previous homepage is preserved in the [archive repository](https://github.com/sherrywong1220/sherrywong1220.github.io-archive).

## Further reading

- [Architecture](docs/ARCHITECTURE.md): runtime ownership, feature activation, and local overrides.
- [Boundaries](docs/BOUNDARIES.md): which gem owns each feature.
- [Content sources](docs/CONTENT_SOURCES.md): biographical and publication provenance.
- `.agents/skills/al-folio-bootstrap/SKILL.md`: new-site setup.
- `.agents/skills/al-folio-v1-migration/SKILL.md`: migration and override auditing.

Keep maintenance rules here and user-facing setup in README. Link to shared details instead of duplicating them.
