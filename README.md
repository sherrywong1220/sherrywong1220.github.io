# Xi (Sherry) Wang · Academic homepage

基于 [al-folio](https://github.com/alshedivat/al-folio) v1 starter / `al_folio_core 1.0.15` 的个人学术主页，使用 Jekyll 构建，部署目标为 GitHub Pages。

包含英文个人简介、PASA Lab 公开头像、研究方向、7 项论文记录、Google Scholar / LinkedIn / 邮箱链接、论文检索，以及响应式布局和深浅色切换。正式论文、已接收论文与预印本均标明状态。

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
| 个人简介与精选论文开关     | `_pages/about.md`               |
| 研究方向                   | `_pages/research.md`            |
| 论文信息、PDF 和代码链接   | `_bibliography/papers.bib`      |
| 论文页结构                 | `_pages/publications.md`        |
| 邮箱、Scholar、LinkedIn    | `_data/socials.yml`             |
| 姓名、站点简介、功能开关   | `_config.yml`                   |
| 头像                       | `assets/img/xi-sherry-wang.jpg` |
| 个人配色、间距、移动端样式 | `_sass/_site.scss`              |
| 事实来源与取舍记录         | `docs/CONTENT_SOURCES.md`       |

BibTeX 的 `selected = {true}` 会把论文显示在首页。`@inproceedings` 显示在会议论文区，`@misc` 显示在预印本区。新增论文也应更新 `scripts/check_site.py` 中的预期论文键。

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

已配置 `.github/workflows/deploy.yml`：PR 构建检查；推送 `main` 后构建并部署。流程使用 GitHub Pages 官方 Actions，并根据实际 Pages 地址生成 `url` / `baseurl`，支持个人站、项目站和自定义域名，不需要提前猜 GitHub 用户名。

1. 在自己的 GitHub 账号创建一个空仓库。根域名主页可命名为 `USERNAME.github.io`；项目主页可以使用 `sherryhomepage`。
2. 在仓库 **Settings → Pages → Build and deployment** 中，将 **Source** 设为 **GitHub Actions**。
3. 为本地项目添加你自己的远程并推送：

   ```bash
   git remote add origin https://github.com/USERNAME/REPOSITORY.git
   git push -u origin main
   ```

4. 在 **Actions → Build and deploy to GitHub Pages** 查看部署结果；部署任务会显示网站地址。

当前仅在本地创建，没有创建远程仓库或公开发布。`upstream` 指向 al-folio 用于溯源，推送地址已设为 `DISABLED`；发布时只使用自己的 `origin`。当前仓库的提交身份使用公开姓名及 UC Merced 邮箱，仅设置在本仓库。

部署流程参考 [GitHub Pages 官方文档](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)。`docs/` 中其余文件是保留的上游说明；本项目部署方式以本 README 为准。

## 来源与许可

个人内容依据 [PASA Lab](https://www.pasalabs.org/people.html)、[导师主页](https://faculty.ucmerced.edu/dong-li/)、会议和论文作者页面整理，核对日期为 2026-10-17。详细记录见 [内容来源](docs/CONTENT_SOURCES.md)。

al-folio 的 MIT 许可保留在 `LICENSE`。肖像和论文属于相应权利人。
