# Google Scholar 在 Google Search 中的可发现性

排查日期：2026-11-02。目标是让普通 Google Search 直接返回本人的 Scholar 资料页；个人主页的可发现性只是辅助。本文是维护记录，不发布到网站。

目标 URL：<https://scholar.google.com/citations?user=JHXk0gcAAAAJ>。

## 已确认的事实与边界

- 用户报告：Scholar 站内搜索 `xi wang ucmerced` 可以找到本人；普通 Google Search 搜索 `xi wang ucmerced google scholar` 或 `sherry wang ucmerced google scholar` 长期找不到。个人主页已经能在 Google Search 找到。
- 本次通用网页检索没有返回目标 Scholar URL，但这不是直接观察 Google 搜索结果，也不能证明页面完全未被收录。浏览器控制服务不可用，无法独立复现 Google 搜索或查看 Scholar 设置。
- 本次无法读取在线个人主页和 Scholar 资料页。下面的 HTML 结论来自当前仓库以正式域名构建的结果，不冒充线上抓取结论。
- Google 的 [Scholar 帮助](https://scholar.google.com/intl/en/scholar/citations.html) 将公开资料、验证机构邮箱列为 **Scholar 搜索**的资格要求，并未承诺普通 Google Search 一定收录。
- [Search Console 的重新抓取申请](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl)要求拥有相应网站属性的所有者或完整用户权限。拥有 Scholar 资料的编辑权，不等于拥有 `scholar.google.com` 的 Search Console 权限；不能从 `xisherry.wang` 属性直接申请收录 Scholar URL。

## 已落实的本地修复

### 1. 删除对可信外链一律添加的 `nofollow`

`_config.yml` 原配置：

```yaml
external_links:
  enabled: true
  rel: external nofollow noopener
```

以 `url: https://xisherry.wang`、`JEKYLL_ENV=production` 构建后，主页图标入口和 Publications 页文字入口都变成：

```html
<a href="https://scholar.google.com/citations?user=JHXk0gcAAAAJ" rel="external nofollow noopener" target="_blank">...</a>
```

原因来自已安装的 `jekyll-link-attributes 2.0.1`：它按 `site.url` 判断外链。开发配置的 URL 是空字符串，所有 URL 都以空字符串开头，因此本地构建未加该属性，掩盖了正式构建的行为差异。

现改为 `rel: external noopener`。这作用于本站人工选择的外链，包括 Scholar、LinkedIn、学校和论文来源；今后若添加广告或不可信链接，应逐个标记合适的 `rel`。

[Google 的外链说明](https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links)不要求普通可信链接带 `nofollow`。但 Google 将它视为[提示，而非绝对命令](https://developers.google.com/search/blog/2019/09/evolving-nofollow-new-ways-to-identify)，所以本问题是一个可修正的不利信号，**不是已证明的唯一根因，删除后也不保证收录**。尤其不能据此解释当前网站建立之前的全部历史问题。

### 2. 提供明确的文字入口

主页简介下方增加一行 `Email | LinkedIn | Google Scholar` 文字链接，分别指向邮箱、LinkedIn 和 Scholar 资料；不在 Publications 标题旁重复添加。原导航图标保留。Publications 页已有文字链接，保留其功能。所有新增链接及 Publications 页的 Scholar ID 均读取自 `_data/socials.yml`。

[Google 链接指南](https://developers.google.com/search/docs/crawling-indexing/links-crawlable)说明，普通 `a[href]` 链接和自然、明确的链接文字有助于发现和理解目标页面。现有图标链接本来就可被解析，新增文字并不是“修复完全不可抓取”。

### 3. 将 Scholar 明确关联到本人

原主题在 `WebSite` 对象上生成 `sameAs`，而主页另一个 `Person` 对象只有姓名别名和主页 URL。现在将 Scholar、LinkedIn、UC Merced affiliation、职衔和照片加入该 `Person` 对象，保留 `Xi Wang`、`Sherry Wang` 两个别名。

这些事实遵循 [内容来源记录](CONTENT_SOURCES.md)。这提高身份表达的明确程度，不是向 Google 提交收录，也不能改变 Scholar 页自身的抓取或索引策略。Google 的[个人资料结构化数据文档](https://developers.google.com/search/docs/appearance/structured-data/profile-page)展示了在人物实体上关联外部资料的方式。

## 接下来按优先级执行

| 优先级 | 动作                                                            | 作用与限制                                                       | 当前状态                                |
| ------ | --------------------------------------------------------------- | ---------------------------------------------------------------- | --------------------------------------- |
| 1      | 浏览器复核后，按 AGENTS.md 发布本次修复                         | 使正式网页提供修正后的链接；本地改动本身没有线上效果             | 构建通过；浏览器和网络不可用，尚未发布  |
| 2      | 在 Scholar 本人资料核查姓名、单位、机构邮箱验证和 Homepage      | 统一身份信息，确认资料公开且可以匿名访问                         | 账户字段尚未独立读取，不能假定有误      |
| 3      | 在 Search Console 检查个人主页，申请重新抓取                    | 让 Google 有机会看到修正后的链接；申请对象是自己的主页           | 尚未执行                                |
| 4      | 在 PASA 成员页、导师学生列表增加 Scholar 直链                   | 增加与本人和学校相关的独立发现路径                               | 已准备 HTML；未联系管理员或修改他人网站 |
| 5      | 在已有 ORCID、GitHub 个人介绍、LinkedIn 资料中补充 Scholar 链接 | 改善真实身份的相互关联；平台可能自行使用 nofollow 或限制公开访问 | 尚未执行；不新建重复身份账号            |
| 6      | 提交 Google Search 搜索结果反馈                                 | 报告可复现的缺失结果，不是保证响应的收录工单                     | 文案在下方；尚未提交                    |

Scholar 字段核查时，优先保持资料 ID 不变。建议姓名与公开使用的 `Xi (Sherry) Wang` 一致，单位为 `University of California, Merced (UC Merced)`，Homepage 为 `https://xisherry.wang/`；若现有信息已经准确完整，就无需为了“触发抓取”反复编辑。机构邮箱验证状态需实际查看，不能仅因 Scholar 站内可搜到就当作已经验证。

在 Search Console 中，检查 `https://xisherry.wang/` 的索引状态、Google 选择的 canonical 和最近抓取时间；有权限时查看已抓取页面中是否出现新文字链接。发布后可对主页申请一次重新抓取，并确认站点地图 `https://xisherry.wang/sitemap.xml` 的处理情况。Google 明确说明反复提交同一个 URL 不会加快抓取，也不保证最终收录。

## 实验室和导师页面的具体改进

本次读取的 [PASA 成员页](https://www.pasalabs.org/people.html)中，Sherry 已链接个人主页，但本人介绍旁没有 Scholar 直链。[导师主页](https://faculty.ucmerced.edu/dong-li/)也列出本人。这两个页面是相关且真实的身份来源；优先补充这里的链接，是基于相关性的工程判断，不是声称 `.edu` 域名天然保证排名。

可以在本人条目旁加入以下片段，保留原个人主页链接：

```html
<a href="https://scholar.google.com/citations?user=JHXk0gcAAAAJ">Xi (Sherry) Wang — Google Scholar</a>
```

管理员沟通草稿（未发送）：

> Could you add a direct Google Scholar link next to my entry on the lab people page / student list? My homepage is already linked, but colleagues have trouble finding my Scholar profile through Google Search. The profile URL is https://scholar.google.com/citations?user=JHXk0gcAAAAJ and the suggested link text is “Xi (Sherry) Wang — Google Scholar”. Thank you!

第三方身份记录：[DBLP Xi Wang 0027](https://dblp.org/pid/08/5760-27.html)列出 UC Merced、相关论文和一个 ORCID ID。其“Google Scholar”入口是检索功能，不能当作已存在的本人资料直链。未独立核实 ORCID 本人记录前，不将该 ID 写入本站或认领账号。

## Google Search 反馈草稿

在 Google Search 中复现搜索，再使用页面反馈入口。官方[反馈说明](https://support.google.com/websearch/answer/6223687?hl=en)只承诺可供审阅，不保证回复、人工加白或收录。以下只包含已知事实；提交前应在当前浏览器复现查询。

```text
My Google Scholar author profile is discoverable inside Google Scholar, but I have been unable to find the profile itself in regular Google Search for these queries:

xi wang ucmerced google scholar
sherry wang ucmerced google scholar

Name: Xi (Sherry) Wang, also known as Xi Wang and Sherry Wang
Affiliation: University of California, Merced
Scholar profile: https://scholar.google.com/citations?user=JHXk0gcAAAAJ
Personal website: https://xisherry.wang/

Searching Google Scholar for "xi wang ucmerced" finds my profile, and my personal website can be found in Google Search. This has been an ongoing problem for colleagues and recruiters trying to locate my Scholar profile. Please investigate whether the profile is being omitted from regular Google Search. I understand that indexing and ranking are not guaranteed.
```

## 验证与观察

本地已通过 `npm run lint:prettier`、两个 al-folio audit、默认 Jekyll 构建与 `scripts/check_site.py`。另以正式域名构建并检查了：

- 修复前：首页和 Publications 的 Scholar 入口均带 `nofollow`。
- 修复后：主页两个入口、Publications 一个入口均不带 `nofollow`，两页均有可见的 `Google Scholar` 链接文字。
- `Person.sameAs` 含正确 Scholar ID，别名和学校一致；canonical、robots 中的 sitemap URL 和 sitemap 首页 URL 均使用正式域名。

构建前后文件及 `verification.json` 保存在被 Git 忽略的 `output/scholar-discoverability/`。尚未做浏览器视觉检查；工具分别返回浏览器不可用、`Sky Computer Use service startup request failed`。本地访问 GitHub 返回 `Could not resolve host: github.com`，因此未推送、未部署，也未在账户中提交任何请求。

发布后的第 7、14、28 天可手动复查以下查询，记录日期、语言/地区和实际返回的 Scholar URL。这只是观察节奏，不是 Google 的处理时限：

```text
xi wang ucmerced google scholar
sherry wang ucmerced google scholar
"Xi (Sherry) Wang" "Google Scholar"
"JHXk0gcAAAAJ"
site:scholar.google.com/citations "Xi Wang" "Merced"
```

如果目标 Scholar URL 在某些查询出现，但在两条常用查询中不出现，至少说明存在搜索可见性，后续重点是姓名和学校的相关性。如果均未出现，仍不能仅凭搜索结果断言没有收录：Google 说明 [`site:` 结果不完整](https://developers.google.com/search/docs/monitor-debug/search-operators/all-search-site)。由于没有 Scholar 网站的 Search Console 权限，无法直接读取其权威索引状态。

避免使用付费“强制收录”、批量垃圾外链、重复 Scholar 账号或关键词堆砌。也不把 Scholar URL 塞进自己域名的站点地图冒充本站页面。Google 的 [Indexing API](https://developers.google.com/search/apis/indexing-api/v3/using-api)仅适用于规定的招聘/直播页面，不适用于个人学者资料。当前没有证据需要建立一个只有跳转按钮的 `/google-scholar/` 页面；那不能使 Scholar 自身被收录。
