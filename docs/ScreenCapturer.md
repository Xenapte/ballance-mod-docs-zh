# ScreenCapturer

截图器 Mod，为 Ballance 增加内置截图功能。

本 Mod 安装后，默认配置下按下 `F8`，截图将会以 PNG 格式自动保存在 Ballance 安装目录下的 Screenshots 文件夹，若截图成功则会产生文字消息提示。截图默认以截图时间（精确到秒）命名。

比起外部工具，本截图 Mod 的优点在于能一键对准游戏画面截图并直接保存。类似于 Minecraft 的 F2 按键或带 Steam Overlay 的游戏的 F12 按键等。

- 作者：BallanceBug
- 发布时间：2022 年 12 月

## 下载地址

- [地图下载站]
- [GitHub](https://github.com/Xenapte/MyBMLMods)

## 配置选项

- Action
  * KeyBinding - 截图快捷键。默认的截图按键是 `F8`，默认选择此快捷键是因为其他常用截图快捷键和 Ballance 下的惯用设置冲突，但玩家可以自行调节。
  * Notify - 截图后是否以游戏内消息的形式对玩家进行通知。若不希望产生通知（例如需要快速多次截图时），可以关闭此选项。
- Saving
  * SaveAsJPEG - 是否以 JPEG 格式（扩展名为 .jpg）保存截图。默认的截图格式为无损压缩的 PNG，但 PNG 文件大小较大，若玩家对画质需求不大，可以改为有损压缩的 JPEG。
  * CopyToClipboard - 复制到剪贴板。默认截图器只会保存截图文件，此选项可以在保存截图同时把截图复制到剪贴板，方便快速分享截图。
  * ClipboardOnly - 仅将截图复制到剪贴板，不实际保存截图文件。若 “复制到剪贴板” 选项未启用，此选项将会被无视。适用于玩家仅需要临时截图并分享的场景。
