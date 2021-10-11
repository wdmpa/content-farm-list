####「小 X 知识百科网」清单

Google 中文搜索结果包含了相当一部分的内容农场式条目，其中多为「小 X 知识网」「小 X 百科网」。访问此种链接会 302 重定向至 g.penzai.com，页面内容为自动生成，大量堆叠关键字，揉杂一些爬取到的内容，完全不具可读性和参考价值。

尤为过分的是，该网站有成千上万个域名被 Google 收录，严重影响搜索体验。详见社区反馈：

1. [Github: 如何屏蔽“小搭百科网”？](https://github.com/cobaltdisco/Google-Chinese-Results-Blocklist/issues/50)
2. [V2EX: 请问在 google 搜索时，频繁遇到小 X 知识网等内容农场式结果，怎么办？](https://www.v2ex.com/t/806025)
3. [V2EX: google 搜中文太毒了吧，是不是已经放弃中文搜索了](https://www.v2ex.com/t/806592)
4. [HOSTLOC: 这采集站群太强了吧](https://hostloc.com/thread-902528-1-1.html)
5. [HOSTLOC: 小*知识网站群是哪位大佬的杰作](https://hostloc.com/thread-902496-1-1.html)

该站群中的站点并不都在标题中包含「百科网」「知识网」的字样，所以为方便广大网友过滤搜索结果，特整理此清单。

## 使用方式

安装 [uBlacklist](https://github.com/iorate/uBlacklist)：

[Chrome Web Store](https://chrome.google.com/webstore/detail/ublacklist/pncfbmialoiaghdehhbnbhkkgmjanfhe) / [Firefox Add-ons](https://addons.mozilla.org/en-US/firefox/addon/ublacklist/) / [App Store](https://apps.apple.com/us/app/ublacklist-for-safari/id1547912640) (for macOS and iOS)

后进入 'Option' 菜单，点击 'Add a subscription'，输入如下内容：

* `Name`: `penzai-list`
* `URL`: `https://raw.githubusercontent.com/dallaslu/penzai-list/main/uBlacklist.txt`

单击 'Add' 按钮。

### 设置搜索引擎

因与清单中域名匹配的结果会被移除，所以搜索引擎的结果页剩余条目太少，不便浏览，建议登录后设置搜索结果显示为每页面 100 条。

##  我们能做什么？

### 一、发 PR 添加域名

1. 从本地插件 uBlacklist 中导出域名列表
2. 在搜索引擎中尝试长尾关键词，以发现更多目前权重尚低的农场域名

### 二、举报

向其使用的云服务提供商举报其滥用行为。
