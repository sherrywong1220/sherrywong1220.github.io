# Xi (Sherry) Wang · Academic homepage

个人学术主页：**[xisherry.wang](https://xisherry.wang/)**。基于 [al-folio](https://github.com/alshedivat/al-folio)，使用 Jekyll 构建，托管于 GitHub Pages。

## 本地预览

需要 Ruby 3.3、Bundler、Node.js 和 Python 3。macOS 使用 Homebrew Ruby 时，先执行 `export PATH="$(brew --prefix ruby@3.3)/bin:$PATH"`。

在项目根目录安装依赖并启动：

```bash
bundle config set --local path vendor/bundle
bundle install
npm ci
./scripts/preview
```

打开 <http://127.0.0.1:4000/>。内容修改后自动重建，修改 `_config.yml` 后需重启。按 `Ctrl+C` 停止；端口被占用时使用 `PORT=4001 ./scripts/preview`。

## 编辑内容

| 内容                    | 文件                            |
| ----------------------- | ------------------------------- |
| 首页简介与版块          | `_pages/about.md`               |
| 研究方向                | `_pages/research.md`            |
| 工作经历                | `_data/experience.yml`          |
| 论文信息、链接与 BibTeX | `_bibliography/papers.bib`      |
| 论文页结构              | `_pages/publications.md`        |
| 邮箱、Scholar、LinkedIn | `_data/socials.yml`             |
| 站点配置                | `_config.yml`                   |
| 头像                    | `assets/img/xi-sherry-wang.jpg` |
| 配色与布局              | `_sass/_site.scss`              |

首页和 Publications 页共用论文数据，按 `papers.bib` 中的条目顺序显示。新增论文时，同步更新 `scripts/check_site.py` 中的预期论文键。内容依据见 [来源记录](docs/CONTENT_SOURCES.md)。

## 验证

```bash
npm run lint:prettier
bundle exec al-folio upgrade audit --no-fail
bundle exec al-folio upgrade overrides audit
bundle exec jekyll build
python3 scripts/check_site.py _site
```

发布前在浏览器检查页面。主题样式覆盖记录在 `.al-folio-overrides.yml`，升级主题时需复查。

## 发布

源码保存在 `main`，构建产物发布到 `gh-pages`。提交修改后执行：

```bash
git push origin main
./scripts/publish
```

发布脚本要求 `main` 工作区干净且已推送，会构建生产版本、检查页面和链接，再更新 `gh-pages`。部署进度见 [GitHub Actions](https://github.com/sherrywong1220/sherrywong1220.github.io/actions)。仅修改 README 等非网站文件时，只需推送源码。

- GitHub Pages：**Deploy from a branch → `gh-pages` → `/ (root)`**。自定义构建工作流目前停用，推送 `main` 不会自动发布网站。
- 域名：`xisherry.wang`，由 Porkbun 管理 DNS。保留根目录 `CNAME`，GitHub Pages 启用 **Enforce HTTPS**。
- `origin` 指向个人主页仓库；`upstream` 仅用于 al-folio 溯源，禁止向其推送。
- 旧主页保存在 [归档仓库](https://github.com/sherrywong1220/sherrywong1220.github.io-archive)。

## 许可

al-folio 的 MIT 许可见 [LICENSE](LICENSE)。肖像和论文属于相应权利人。
