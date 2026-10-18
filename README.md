# Xi (Sherry) Wang · Academic homepage

基于 [al-folio](https://github.com/alshedivat/al-folio) v1 starter / `al_folio_core 1.0.15` 的个人学术主页，使用 Jekyll 构建，部署目标为 GitHub Pages。

包含英文个人简介、PASA Lab 公开头像、研究方向、7 项论文记录、Google Scholar / LinkedIn / 邮箱链接、论文检索，以及响应式布局和深浅色切换。正式论文、已接收论文与预印本均标明状态。

排版参考 [Haobo Yuan](https://yuanhaobo.me/) 的居中窄版、左文右图结构，配色与字体参考 [Tal Zussman](https://talzussman.com/)：860px 阅读宽度、白底、酒红色 `#8c1515`、Inter 正文与 Ubuntu Mono 辅助信息。保留 al-folio 的导航、论文管理和深浅色切换。

## 本地预览

当前电脑已安装 Homebrew Ruby 3.3，依赖在项目的 `vendor/bundle`，没有修改 macOS 自带 Ruby。

```bash
cd /Users/sherry/Documents/github/sherryhomepage
./scripts/preview
```

打开 <http://127.0.0.1:4000/>。内容文件修改后自动重建；修改 `_config.yml` 后需要重启。前台运行时在终端按 `Ctrl+C` 停止。本次预览在后台运行，PID 记录在 `output/preview.pid`，可用 `kill "$(cat output/preview.pid)"` 停止。如果端口已占用，使用 `PORT=4001 ./scripts/preview`。

另一台 macOS 电脑首次使用：

```bash
brew install ruby@3.3 node
export PATH="$(brew --prefix ruby@3.3)/bin:$PATH"
bundle config set --local path vendor/bundle
bundle install
npm ci
./scripts/preview
```

其他操作系统需要 Ruby 3.3、Bundler 和 Node.js，然后执行相同的依赖安装步骤。`.ruby-version` 用于支持 rbenv/asdf 的环境。

## 编辑内容

| 内容                       | 文件                            |
| -------------------------- | ------------------------------- |
| 个人简介与完整论文列表     | `_pages/about.md`               |
| 研究方向                   | `_pages/research.md`            |
| Industry Experience        | `_data/experience.yml`          |
| 论文信息、PDF 和代码链接   | `_bibliography/papers.bib`      |
| 论文页结构                 | `_pages/publications.md`        |
| 邮箱、Scholar、LinkedIn    | `_data/socials.yml`             |
| 姓名、站点简介、功能开关   | `_config.yml`                   |
| 头像                       | `assets/img/xi-sherry-wang.jpg` |
| 个人配色、间距、移动端样式 | `_sass/_site.scss`              |
| 事实来源与取舍记录         | `docs/CONTENT_SOURCES.md`       |

首页与 Publications 页面均将全部论文合并在一个 `Publications` 列表中，按 `papers.bib` 中的条目顺序排列：cMPI → CXL characterization → HybridGen → OCEAN → mLR → TierBPF → Hybrid Adaptive Tuning。会议论文标签保留会议名和年份，SC 与 IPDPS 统一使用酒红色；预印本标签显示为 `arXiv`。BibTeX 中仍保留正确的 `@inproceedings` 与 `@misc` 类型。新增论文也应更新 `scripts/check_site.py` 中的预期论文键。

没有虚构本科／硕士学历、预计毕业日期、引用次数或 CV 下载。需要补充时直接编辑这些源文件。

## 验证

```bash
export PATH="/opt/homebrew/opt/ruby@3.3/bin:$PATH"
npm ci
npm run lint:prettier
bundle exec al-folio upgrade audit --no-fail
bundle exec al-folio upgrade overrides audit
bundle exec jekyll build
python3 scripts/check_site.py _site
```

本次已验证生产构建的根路径、`/sherryhomepage` 子路径及完整 Pages URL；4 个页面、7 项论文和全部站内资源链接通过检查。Chrome 桌面与 iPhone 393px 预览中已检查导航、深浅色切换、论文过滤和 BibTeX 展开。

`assets/css/main.scss` 是唯一有意保留的主题覆盖：沿用上游样式入口并追加 `@use "site"`。覆盖关系记录在 `.al-folio-overrides.yml`。升级主题后需重新检查这个小差异。

## 发布到 GitHub Pages

生产地址：<https://xisherry.wang/>。源码仓库：[sherrywong1220/sherrywong1220.github.io](https://github.com/sherrywong1220/sherrywong1220.github.io)。

当前使用 **本地生产构建 → `gh-pages` 分支 → GitHub Pages**。仓库 **Settings → Pages → Build and deployment → Source** 为 **Deploy from a branch**，分支为 **`gh-pages`**，目录为 **`/ (root)`**。`main` 保留可编辑源码，`gh-pages` 保存构建后的静态网站及 `.nojekyll`；个人主页的 `baseurl` 为空。

后续更新：修改内容、执行上面的验证命令，将修改提交到本地 Git，然后运行：

```bash
git push origin main
./scripts/publish
```

`scripts/publish` 要求 `main` 工作区干净，且本地提交已推送到源码仓库。脚本使用正式网址构建、检查页面和站内链接，然后以普通 Git 提交更新 `gh-pages`，保留发布历史。在 [Actions → pages build and deployment](https://github.com/sherrywong1220/sherrywong1220.github.io/actions) 查看最终部署结果。

首次发布时，自定义 Actions 因 GitHub 账户的 billing issue 未能启动；GitHub 内置的 Pages 分支部署已成功。为避免每次推送源码触发同样的失败，暂时停用自定义 `Build and deploy to GitHub Pages` 工作流，其配置仍保留在 `.github/workflows/deploy.yml`。账户限制解除后，可将 Pages Source 改回 **GitHub Actions**、启用该工作流并手动运行一次，以恢复推送 `main` 后自动构建发布。

### 自定义域名

域名 `xisherry.wang` 在 Porkbun 管理，GitHub Pages 的 Custom domain 使用 `xisherry.wang`。根目录的 `CNAME` 文件随每次构建发布到 `gh-pages`，`scripts/publish` 使用 `https://xisherry.wang` 生成 canonical、sitemap 和 feed 中的网址。原 `sherrywong1220.github.io` 地址由 GitHub Pages 重定向到自定义域名。

Porkbun DNS 配置使用 GitHub Pages 的四条根域名 A 记录，以及指向 `sherrywong1220.github.io` 的 `www` CNAME；`www.xisherry.wang` 重定向到主域名。DNS 指向 GitHub 后，由 GitHub Pages 签发 HTTPS 证书并启用 Enforce HTTPS。

### 旧主页归档

2026-10-17，原仓库改名为 [sherrywong1220.github.io-archive](https://github.com/sherrywong1220/sherrywong1220.github.io-archive)，保留原仓库及全部提交历史，并设为只读归档。归档时 `master` 的提交为 `b8921305d9f7a1b32a44d555f892e74041b3217e`。旧仓库的 Pages 已停用，新版使用原来的主页网址。

本机另有完整 Git 备份 `output/deployment/old-homepage-2026-10-17.bundle`，以及发布前的新版备份 `output/deployment/new-homepage-before-publish.bundle`。这些文件只保存在本地，不上传到源码仓库或网站。

`origin` 指向自己的新主页仓库。`upstream` 指向 al-folio 用于溯源，推送地址已设为 `DISABLED`；发布时只使用 `origin`。当前仓库的提交身份使用公开姓名及 UC Merced 邮箱，仅设置在本仓库。

部署流程参考 [GitHub Pages 官方文档](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)。`docs/` 中其余文件是保留的上游说明；本项目部署方式以本 README 为准。

## 来源与许可

个人内容依据 [PASA Lab](https://www.pasalabs.org/people.html)、[导师主页](https://faculty.ucmerced.edu/dong-li/)、会议和论文作者页面整理，核对日期为 2026-10-17。详细记录见 [内容来源](docs/CONTENT_SOURCES.md)。

al-folio 的 MIT 许可保留在 `LICENSE`。肖像和论文属于相应权利人。
