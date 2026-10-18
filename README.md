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

## 维护

内容文件位置、排版原则、验证和发布流程见 [AGENTS.md](AGENTS.md)。旧主页保存在 [归档仓库](https://github.com/sherrywong1220/sherrywong1220.github.io-archive)。

## 许可

al-folio 的 MIT 许可见 [LICENSE](LICENSE)。肖像和论文属于相应权利人。
