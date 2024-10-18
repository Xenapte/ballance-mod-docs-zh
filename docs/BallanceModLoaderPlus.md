# BallanceModLoaderPlus

Ballance Mod Loader Plus（BML+）是基于原版 BML 的改进版本。最初为适配新 Player 所制作的移植版本，经过数次更新，目前与原版 BML 存在较大差异。

本章节以目前最新版本（0.3.4）为准。

相较于原版 BML，BML+ 主要有如下差异：

- 不兼容原版 BML 的 mod（BML+ 基于原生 VirtoolsSDK，难以实现 ABI 层面的向前兼容），为作区分，BML+ 的 mod 扩展名为`.bmodp`。

- GUI 部分基于 ImGui 实现，提升了渲染性能，支持中文文本显示输入。（为了保持向前兼容性，目前仍然保留原有 BGui ，计划将于下一个大版本更新移除）。

- 尽可能使用 UTF- 8 编码，支持在非中文系统下加载文件名含有中文的自制地图。

- 在命令行输入的命令不再以`/`开始并区分大小写。

- 保存并加载历史命令记录。

- 支持游戏内禁用 mod。

- 可以加载位于 `Maps` 子目录的自制地图，并支持中文搜索。

- 移除了与新 Player 重叠的内置功能，并集成 FramerateUnlocker 与 LanternFader 的全部功能。另外对大部分内置功能进行了分离，将调试功能，摄像机自定义功能，自由视角模式分离为以下三个独立 mod：

  - DebugUtilities

  - CameraUtilities

  - TravelMode

## 命令

- `bml` - 显示 BML 的相关信息。
- `help` - 显示帮助。
- `cheat [true|false]` - 开启或关闭 Cheat Mode（作弊模式）。若不指定开关状态则会根据当前状态自动切换。
- `echo <消息>` - 输出消息，效果等同于在原版 BML 命令行直接键入文本。
- `clear` - 清除当前显示的所有历史消息。
- `history [clear]` - 输出历史命令记录。当指定 `clear` 选项时清除历史记录。
- `exit` - 退出游戏。
- `hud [title|fps|sr] [on|off]` - 显示或隐藏 BML 标题，FPS，SR Timer，未指定操作对象时对所有操作对象生效。

## 操作方式

**默认状态下：**

- `/` - 显示命令行， 按`Enter` 执行所键入命令，按 `Esc` 退出命令行。

**Mod 菜单界面下**：

在 mod 名称上单击鼠标右键或按退格键文本颜色变为黑色，表示该 mod 将会被禁用，在被禁用 mod 上再次单击鼠标右键或按退格键重新启用。以上操作均为重启游戏后生效。

## 配置选项

- `GUI` - 图形界面选项。
  * `FontFilename` - 自定义字体文件名，请键入完整文件名称（带扩展名），添加新字体请将文件放入 `ModLoader\Fonts` 目录下。重启游戏后生效。
  * `FontSize` - 自定义字体大小。重启游戏后生效。
  * `FontRanges` - 自定义字体 Unicode 码点范围。需要显示中文时将值修改为 `ChineseFull`。重启游戏后生效。
  * `EnableSecondaryFont` - 启用补充字体。重启游戏后生效。
  * `SecondaryFontFilename` - 自定义补充字体文件名。重启游戏后生效。
  * `SecondaryFontSize` - 自定义补充字体大小。重启游戏后生效。
  * `SecondaryFontRanges` - 自定义补充字体 Unicode 码点范围。重启游戏后生效。
  * `EnableIniSettings` - 保存并加载 ImGui 设置参数。重启游戏后生效。
- `HUD` - HUD 选项。
  - `ShowTitle` - 在游戏窗口上中央叠加显示 BML+ 标题。立即生效。
  - `ShowFPS` - 在游戏窗口左上角叠加显示当前 FPS。立即生效。
  - `ShowSRTimer` - 在游戏窗口左下角叠加显示 SR Timer（竞速计时器）。立即生效。
- `Graphics` - 图形选项。
  - `UnlockFrameRate` - 解锁帧率。立即生效。
  - `SetMaxFrameRate` - 设置帧率上限。设置为 0 时垂直同步。启用解锁帧率后该选项无效。立即生效。
  - `WidescreenFix` - 宽屏修复。立即生效。
- `Tweak` - 优化选项。
  - `LanternAlphaTest` - 为灯柱贴图启用透明度测试。可大幅提升在出现灯柱的场景下的渲染性能。立即生效。
  - `FixLifeBallFreeze` - 修复加命时游戏卡死问题（Windows 10 之后常见的兼容性问题）。重启游戏后生效。
  - `Overclock` - 移除球出生或重生时的动画效果，使球无延迟瞬间出生。立即生效。
- `CommandBar` - 命令行选项。
  - `MessageCapability` - BML 提示消息的最大显示行数。立即生效。
  - MessageDuration - BML 提示消息的最大显示时长，以秒为单位。超时后会自动渐变隐藏。立即生效。
- `CustomMap` - 自制地图选项。
  - `LevelNumber` - 自制图关卡号。BML 加载自制图的原理是将自制图随机填入一原版关卡的位置后加载，本选项可以自定义加载入的关卡号（会影响天空背景以及通关后的奖励分）。加载地图时生效。
    + 本选项值必须位于 1 和 13 之间。
    + 使用 1 会导致自制图内出现帮助提示，12 导致光照变暗并配有闪电效果，13 则会导致石球开局。
    + 填入 0 时游戏采取默认策略，将自制图随机填入第 2 至 11 关中的一关。
  - `ShowTooltip` - 以提示信息形式显示完整地图名称。立即生效。
  - `MaxDepth` - 最大子目录深度。重启游戏后生效。
