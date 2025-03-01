# Ballance Mod 文档

本文档介绍适用于 Gamepiaynmo 的 [Ballance Mod Loader (简称 BML)](https://github.com/Gamepiaynmo/BallanceModLoader) 或 doyaGu 的 [Ballance Mod Loader Plus (简称 BML+ 或 BMLP)](https://github.com/doyaGu/BallanceModLoaderPlus) 的 Mod，因此你需要先安装其一才能使用。

本文档由 BallanceBug 和 yyc12345、Ghomist（Zzq_203）、doyaGu 撰写于 2024 年 10 月 7 日至 10 月 21 日。

- [在 GitHub 上查看本文档源码](https://github.com/Xenapte/ballance-mod-docs-zh)
- [查看本文档 GitHub Wiki 版](https://github.com/Xenapte/ballance-mod-docs-zh/wiki/%E6%96%87%E6%A1%A3)
- [查看本文档外部网页版](https://bcrc.site/docs/mods)（不一定及时更新）

## 使用本文档

本仓库已经可以作为 Mod 文档使用，不过最方便的分发方式仍然是将所有文档整合至一起，构建为 HTML 或者 PDF 手册进行分享。

若要构建完整的手册，请拉取本仓库，然后运行 [overview_generator](./overview_generator.py) 脚本：

```shell
git clone https://github.com/Xenapte/ballance-mod-docs-zh
cd ballance-mod-docs-zh
python overview_generator.py
```

输出文件为 `test_overview.md`。

除此之外，我们自己搭建的[网页版手册](https://bcrc.site/docs/mods)还使用了一些[自定义 CSS 样式](styles/custom.css)。

## 贡献本文档

每一个 Mod 使用独立一个 markdown 文件，详见 [docs 目录](./docs/)。

注意事项：

- 编写文档时可从[模板目录](./templates/)复制一份模板，修改后存放至 docs 目录。
- 生成脚本自带*替换规则*。
  * 需要链接至地图下载站时可直接使用 `{地图下载站}`。
  * 需要链接至其它 Mod 的文档时可使用 `[ModName](./ModName.md)`。
- 本文件（即 `README.md`）的一级标题以及紧邻的段落会保留至输出。
  * 其它 Overview 部分的内容位于 [overview_header.md](./overview_header.md) 中。
- Mod 文档的文件名与一级标题内容需保持一致，均为 Mod 正式名称。
