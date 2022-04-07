# 内容农场网站清单

Google 中文搜索结果包含了相当一部分的内容农场式条目，比如「小 X 知识网」「小 X 百科网」。此种链接常会 302 重定向其主站，页面内容为自动生成，大量堆叠关键字，揉杂一些爬取到的内容，完全不具可读性和参考价值。

尤为过分的是，该类网站可能有成千上万个分身域名被 Google 收录，严重影响搜索体验。详见 2021 年 10 初的社区反馈：

1. [Github: 如何屏蔽“小搭百科网”？](https://github.com/cobaltdisco/Google-Chinese-Results-Blocklist/issues/50)
2. [V2EX: 请问在 google 搜索时，频繁遇到小 X 知识网等内容农场式结果，怎么办？](https://www.v2ex.com/t/806025)
3. [V2EX: google 搜中文太毒了吧，是不是已经放弃中文搜索了](https://www.v2ex.com/t/806592)
4. [HOSTLOC: 这采集站群太强了吧](https://hostloc.com/thread-902528-1-1.html)
5. [HOSTLOC: 小*知识网站群是哪位大佬的杰作](https://hostloc.com/thread-902496-1-1.html)

使用正则匹配标题的方式不能完全屏蔽，所以为方便广大网友过滤搜索结果，特整理此清单。

由于此次事件主角「小搭百科网」在造成影响后[主动关站](https://www.v2ex.com/t/807150 )，所以接下来也将关注、收录其他的类似内容农场站。

## 使用方式

### uBlacklist
安装 [uBlacklist](https://github.com/iorate/uBlacklist)：

[Chrome Web Store](https://chrome.google.com/webstore/detail/ublacklist/pncfbmialoiaghdehhbnbhkkgmjanfhe) / [Firefox Add-ons](https://addons.mozilla.org/en-US/firefox/addon/ublacklist/) / [App Store](https://apps.apple.com/us/app/ublacklist-for-safari/id1547912640) (for macOS and iOS)

后进入 `Option` 菜单，点击 `Add a subscription`，输入如下内容：

* `Name`: `content-farm-list`
* `URL`: `https://raw.githubusercontent.com/wdmpa/content-farm-list/main/uBlacklist.txt`

或

* `Name`: `content-farm-list`
* `URL`: `https://wdmpa.org/content-farm-list/uBlacklist.txt`

单击 'Add' 按钮。

### Google Hit Hider

<http://www.jeffersonscher.com/gm/google-hit-hider/>

#### Install

[Grease Fork](https://greasyfork.org/scripts/1682-google-hit-hider-by-domain-search-filter-block-sites) / [OpenUserJS.org](https://openuserjs.org/scripts/jscher2000/Google_Hit_Hider_by_Domain_%28Search_Filter_Block_Sites%29)

#### Manage lists

<http://www.jeffersonscher.com/gm/google-hit-hider/manage-lists.php>

## 订阅说明

| 文件 | 说明 |  
| -- | -- |  
| `uBlacklist.txt` | uBlacklist 规则集合 |  
| `Surge.txt` | Surge 规则集合 |
| `uBlacklist/spam/g.penzai.com.txt` | uBlacklist 专用小搭百科网域名集合|  
| `Surge/spam/g.penzai.com.txt` | Surge 专用小搭百科网域名集合|
| `uBlacklist/machine-translated/stackoverflow.txt` | uBlacklist 专用机翻 StackOverflow 域名集合|  
| `Surge/machine-translated/stackoverflow.txt` | Surge 专用机翻 StackOverflow 域名集合|

## 设置搜索引擎

因与清单中域名匹配的结果会被移除，所以搜索引擎的结果页剩余条目太少，不便浏览，建议登录后设置搜索结果显示为每页面 100 条。

## 我们能做什么？

### 一、发 PR 添加域名

1. 从本地插件 uBlacklist 中导出域名列表
2. 在搜索引擎中尝试长尾关键词，以发现更多目前权重尚低的农场域名

按结构在 `domains` 目录中添加新的分类集合文件。参考文件中已有内容的格式，在任意位置添加即可。（Fork 本仓库后编辑再 Push，或在页面中编辑均可。）

| 文件 | 说明 |  
| -- | -- |  
| `domains/spam/g.penzai.com.txt` | 小搭百科网域名集合| 
| `domains/machine-translated/stackoverflow.txt` | 机翻 StackOverflow 域名集合| 

提交后，脚本会自动更新订阅文件中的内容。

### 二、举报

向其使用的云服务提供商举报其滥用行为。
