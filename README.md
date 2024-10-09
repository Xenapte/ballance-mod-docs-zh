# Ballance Mod 文档

本文档介绍适用于 [Ballance Mod Loader (BML)](https://github.com/Gamepiaynmo/BallanceModLoader) 或 [Ballance Mod Loader Plus (BML+)](https://github.com/doyaGu/BallanceModLoaderPlus) 的 Mod，因此你需要先安装其一才能使用。

本文档撰写于 2024 年 10 月 7 日。

## Mod 获取方式

### Ballance 地图下载站

绝大多数 Mod 均可以在 [Ballance 地图下载站](http://ballancemaps.ysepan.com)下载（虽然名称是 “地图” 下载站，但实际上也可以下载到 Mod）。

### 其他下载方式

- 有些 Mod 因为需要时常更新，或者内容不太适合正常发布，地图下载站不会收录。请参见 Mod 具体介绍内列出的下载方式。
- 有能力者自然可以直接从 Mod 源码自行编译。

## Mod 列表

### AdvancedTravelCam

#### 基础信息

改进版的 TravelCam。原 TravelCam 是 BML 自带的 Mod，用于提供脱离玩家球的自由视角，但功能有限。本 Mod 即为其进阶版。

- 作者：BallanceBug
- 发布时间：2022 年 12 月

#### 下载地址

- [地图下载站](#ballance-地图下载站)
- [GitHub](https://github.com/Xenapte/MyBMLMods)

#### 教程视频

- [作者的教程视频](https://www.bilibili.com/video/BV1XN411m7a5/)

#### 命令

- `+travel` 或 `advancedtravel` - 进入 AdvancedTravelCam。

#### 操作方式

- `W` `A` `S` `D` - 操作摄像机移动。
- `Shift` - 使摄像机下降。
- `Space` - 使摄像机上升。
- `Ctrl` - 按下时，摄像机能够以 3 倍速加速移动。和 BML 的 Cheat Mode 的倍速类似。
- `Z` - 按下时摄像头能够往前方自动缩进（**Z**oom），便于仔细观察。此按键按下时，可以同时操作鼠标滚轮以调整放缩度。
- `鼠标左键` - 按下后，鼠标可以在视图内选点传送。选择模式下使用右键可以退出。

#### 配置选项

- Quantities
  * HorizontalSpeed - 摄像机横向移动速度。
  * VerticalSpeed - 摄像头纵向移动速度。
  * MouseSensitivity - 鼠标灵敏度。
  * MaximumViewDistance - 最大视野距离。
  * RelativeDirection - 是否使用相对方向。启用后，横向移动会被理解成相对于摄像机当前方向的横向移动（所以会导致摄像机高度变化）。
  * CinematicCamera - “影院式”相机，效果是可以使摄像机移动更加平滑。
  * CinematicMotionSpeed - 影院式移动速度。必须在 0 和 1 之间，数值越小移动越平滑，但也会导致延迟越高。
  * CinematicMouseSpeed - 影院式鼠标移动速度。必须在 0 和 1 之间。
- Quantities
  * Command1, Command2 - 触发 AdvancedTravelCam 的命令。修改后必须重启游戏才能生效。
- Controls
  * 操控摄像机各种移动方式的按键。

### BallanceOptifine

Ballance 地图优化 Mod。开启后本 Mod 会自动为地图内的所有路面加上影子和音效，使地图更加仿真。

- 作者：yyc12345
- 发布时间：2021 年

#### 下载地址

- [地图下载站](#ballance-地图下载站)
- [GitHub](https://github.com/yyc12345/BMLMods)

#### 配置选项

*待施工...*

### BallanceMMO

全称 Ballance 大型多人在线（Ballance Massively Multiplayer Online）。**简称 BMMO**，俗称**联机插件**。Ballance 多人联机使用的 Mod。

完整简介请参照 Ballance Wiki：

- [BallanceMMO 简介](https://ballance.wiki/Ballance%E5%A4%A7%E5%9E%8B%E5%A4%9A%E4%BA%BA%E5%9C%A8%E7%BA%BF%E6%B8%B8%E6%88%8F)
- [BallanceMMO 客户端使用说明](https://ballance.jxpxxzj.cn/wiki/BallanceMMOClient/zh)

### BMMOAntiCheat

BMMO 联机比赛时的反作弊 Mod。

本 Mod 无需配置，联机比赛时安装上即可；若玩家未安装或安装的不是最新版，会导致无法进入比赛服务器。

### Blackout

Ballance 暗黑模式 Mod。可以移除游戏内的光源，让整个地图处于完全黑暗状态。

- 作者：BallanceBug
- 发布时间：2023 年 10 月

#### 下载地址

- [地图下载站](#ballance-地图下载站)
- [GitHub](https://github.com/Xenapte/MyBMLMods)

#### 配置选项

- Main
  * Enabled - 是否启用。
  * LightUpSurroundings - 若启用，玩家球正上方会提供一微弱光源，能够照亮玩家附近的小片区域。
  * FullDarkMode - 强制整个地图黑暗下来（默认的暗黑模式实际不很彻底）。

### BLinguist

Ballance 翻译 Mod。当前主要支持中文翻译，其他语言的支持不是很彻底

- 作者：yyc12345
- 发布时间：2021 年

#### 下载地址

- [地图下载站](#ballance-地图下载站)
- [GitHub](https://github.com/yyc12345/BMLMods)

#### 配置选项

*待施工...*

### ChangeGameSpeed

游戏全局速度调节 Mod。

**注意：本 Mod 的所有功能已经可以被 [PhysicsEditor](#PhysicsEditor) 取代，若无特殊需求请优先使用取代 Mod。**

- 作者：Onlyforyou
- 发布时间：2020-2021

#### 下载地址

- [地图下载站](#ballance-地图下载站)

### CursorClipper

鼠标锁定 Mod，在窗口化游戏中会自动锁定鼠标到窗口内，防止游戏中意外移出鼠标（例如误触触控板等）后出现操作事故。本 Mod 仅会在实际游戏过程中锁定鼠标范围；按下暂停菜单后会自动解锁。

本 Mod 无需配置。

- 作者：BallanceBug
- 发布时间：2023 年 8 月

### ExtraSector

999 小节加载器，使得游戏可以加载超过 8 小节的地图。主要用于游玩原版连体图等。

本 Mod 无需配置。

- 作者：yyc12345
- 发布时间：2022 年 6 月

### FogMode

迷雾模式 Mod。

- 作者：Ghomist (Zzq_203)
- 发布时间：2022 年

#### 配置选项

*待施工...*
