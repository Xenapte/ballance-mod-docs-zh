# BLinguist

## 基础信息

Ballance中文版插件。可以完全替代旧版Ballance汉化补丁。

该Mod所能做的不仅仅是复刻旧版中文补丁。它还可以为Ballance提供任一语言的显示。目前它支持4种语言：英语（作为默认回退语言），中文，日语（机翻），阿拉伯语（机翻。由于历史原因加入）。它还可以自动识别用户当前系统所用语言，并自动切换对应语言（如果有的话）。

BLinguist和旧版中文补丁一致，汉化了教程和多数界面菜单。可以使得一些完全看不懂Ballance英文的玩家快速进行游戏。但对于Ballance Mod Loader提供的页面没有汉化能力。同时BLinguist不需要修改游戏文件，只需要在Mod设置中简单开关BLinguist的全局设置，即可打开或关闭BLinguist，为之后玩家转型成竞速党提供便利。

- 作者：yyc12345
- 发布时间：2023 年 3 月

## 下载地址

- {地图下载站}
- [GitHub](https://github.com/yyc12345/BMLMods)

## 操作方式

在配置选项中选择合适的语言，或调整Mod启用与否后，重启游戏即可更改游戏显示语言。

## 配置选项

- Core
  * Enable - 启用当前Mod。不启用此Mod时，所有文本将退回Ballance默认的渲染模式。然而这并不能阻止本Mod创建一些必须的内容，如果想彻底消除本Mod的影响，请删除本Mod。
  * Language - 决定要显示的语言，重启游戏生效。目前支持填写进去的文本（区分大小写）：`English`（英语），`Chinese`（简体中文），`Arabic`（阿拉伯语），`Japanese`（日语）
- Font
  * FontName - 显示文本用的字体名称，详细请参考FontCraft。重启游戏生效。
  * FontSize - 显示文本用的字体大小，详细请参考FontCraft。重启游戏生效。
  * FontCraft - 启用后，会在Mod加载时，尝试寻找FontCraft，如果找到，则从FontCraft中读取字体设置，同时忽略上述两个字体选项。如果不启用此选项，或没有找到FontCraft，则使用上述两个字体选项来显示文字。该选项主要是为了和FontCraft配合使用，以使得整个游戏界面的字体更加地统一。重启游戏生效。
