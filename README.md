# Ballance Mod 文档

本文档介绍适用于 [Ballance Mod Loader (简称 BML)](https://github.com/Gamepiaynmo/BallanceModLoader) 或 [Ballance Mod Loader Plus (简称 BML+ 或 BMLP)](https://github.com/doyaGu/BallanceModLoaderPlus) 的 Mod，因此你需要先安装其一才能使用。

本文档撰写于 2024 年 10 月 9 日。

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


### BallanceBBOR

#### 基础信息

**这是一个未完成的 Mod。如果您发现您的 Mod 列表中有这个 Mod，请立即卸载，因为它可能会导致游戏不稳定。**

这是一个可以在 Ballance 中显示变球器，风扇，死亡区等物体作用范围的 Mod。

其名称来自 Minecraft 的同名Mod，Bounding Box Outline Reloaded，该Mod在Minecraft中承担相同功能，即显示游戏中具有特定功能的结构的边框。该Mod与竞速无关，竞速玩家请立即卸载。

- 作者：yyc12345
- 发布时间：2023 年 11 月

#### 下载地址

- [GitHub](https://github.com/yyc12345/BMLMods)

#### 操作方式

在配置选项中配置需要显示的结构，进入关卡后即可观察到指定结构。

#### 配置选项

- Global
  * Enabled - 全局启用Mod。关闭此选项将完全禁用Mod支持的作用范围显示，但并不会阻止Mod创建一些额外的物体（Mod本身使用需要）。如需彻底禁用此Mod，请移除此Mod。
- DepthCubes
  * Enabled - 单独启用死亡区作用范围的显示
  * Display Color - 死亡区显示用的颜色。颜色格式请参考FontCraft。
- Transformer
  * Enabled - 单独启用变球器作用范围的显示
  * Display Color - 作用区域显示用的颜色。颜色格式请参考FontCraft。
- VentilatorActiveArea
  * Enabled - 单独启用风扇为球施加向上作用力的区域的显示
  * Display Color - 作用区域显示用的颜色。颜色格式请参考FontCraft。
- VentilatorDeactiveArea
  * Enabled - 单独启用风扇取消向球施加向上作用力的区域的显示
  * Display Color - 作用区域显示用的颜色。颜色格式请参考FontCraft。
- PhysHiddenFloor
  * Enabled - 单独启用被隐藏的，物理化为Floor类型的物体的显示（4-3的石球滚下来的隐藏钢轨）
  * Display Color - 物体形状显示用的颜色。颜色格式请参考FontCraft。
- PhysHiddenStopper
  * Enabled - 单独启用被隐藏的，物理化为Stopper类型的物体的显示（一些自制图中用的，只允许道具球走的，玩家球一走上去就掉下去的）
  * Display Color - 物体形状显示用的颜色。颜色格式请参考FontCraft。

### BallanceOptifine

#### 基础信息

Ballance 高清修复，为一些老旧地图添加阴影，渐变柱子等。效果不一定是最佳，且可能会因为开启而破坏了关卡原有体验。对于旧版渐变柱子（通过拉伸 UV 来实现柱子渐变的柱子）甚至会破坏其不断状态。

名称取自 Minecraft 同名Mod，Optifine，高清修复，其为旧版 Minecraft 加速其图形性能。

- 作者：yyc12345
- 发布时间：2020 年 12 月

#### 下载地址

- [地图下载站](#ballance-地图下载站)
- [GitHub](https://github.com/yyc12345/BMLMods)

#### 操作方式

在配置选项中配置需要处理的内容，然后加载老旧地图，即可享受修复成果。

#### 配置选项

- OptiFine
  * GlobalEnable - 此Mod的全局启用键，方便整体开关Mod
  * Shadow - 启用阴影修复，启用后将按照一定规则（参见Shadow分类选项）来自动为地图加上阴影
  * Material - 启用材质修复，启用后按照一定规则（参见Material分类选项）修复材质错误，渐变柱子的修复在这里
  * CK2_3DOverride - 启用CK2_3D设置覆盖，启用后，将会把CK2_3D设置强制改为`32bit ARGB8888`模式，这与直接修改`CK2_3D.ini`等价。此选项的启用和关闭需要重新启动游戏来应用。启用此选项后会自动解决材质问题，并且Ballance界面将会变得更加平滑。
- Shadow
  * Shadow - 被归入Shadow组的物体将被强制产生阴影
  * Phys_Floors - 被归入Phys_Floors组的物体将被强制产生阴影
  * Phys_FloorRails - 被归入Phys_FloorRails组的物体将被强制产生阴影
- Material
  * Column_beige_fade.tga - 修复柱子渐变材质
  * Laterne_Schatten.tga - 修复灯阴影材质
  * Laterne_Verlauf.tga - 修复灯光线散射材质
  * Modul18_Gitter.tga - 修复风扇网格材质
  * Stick_Bottom.tga - 修复终点彩柱渐变材质

### BallanceMMO

全称 Ballance 大型多人在线（Ballance Massively Multiplayer Online）。**简称 BMMO**，俗称**联机插件**。Ballance 多人联机使用的 Mod。

完整简介请参照 Ballance Wiki：

- [BallanceMMO 简介](https://ballance.wiki/Ballance%E5%A4%A7%E5%9E%8B%E5%A4%9A%E4%BA%BA%E5%9C%A8%E7%BA%BF%E6%B8%B8%E6%88%8F)
- [BallanceMMO 客户端使用说明](https://ballance.jxpxxzj.cn/wiki/BallanceMMOClient/zh)

### BMMOAntiCheat

BMMO 联机比赛时的反作弊 Mod。

本 Mod 无需配置，联机比赛时安装上即可；若玩家未安装或安装的不是最新版，会导致无法进入比赛服务器。

### BaseCmoCfg

#### 基础信息

本 Mod 通过在游戏加载 `base.cmo` 时，篡改其中数据，使得在不修改文件的情况下，启用 Ballance **制作组**用于测试游戏所用的 Godmode 和 Debug 模式。

注意，这里的 Debug 模式和 BML 以及 BMLP 中的 Debug 模式是两个概念，切不可混淆！该 Mod 与竞速无关，竞速玩家请立即卸载。

- 作者：yyc12345
- 发布时间：2021 年 10 月

#### 下载地址

- [GitHub](https://github.com/yyc12345/BMLMods)

#### 教程视频

该Mod没有教程视频。

#### 命令

该Mod没有命令。

#### 操作方式

在配置中调整选项，重启游戏后即可完成更改。

#### 配置选项

- Core
  * Godmod - 选中后开启Godmode，重启游戏后生效。
  * Debug - 选中后开启Debug模式，重启游戏后生效。

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

#### 基础信息

Ballance中文版插件。可以完全替代旧版Ballance汉化补丁。

该Mod所能做的不仅仅是复刻旧版中文补丁。它还可以为Ballance提供任一语言的显示。目前它支持4种语言：英语（作为默认回退语言），中文，日语（机翻），阿拉伯语（机翻。由于历史原因加入）。它还可以自动识别用户当前系统所用语言，并自动切换对应语言（如果有的话）。

BLinguist和旧版中文补丁一致，汉化了教程和多数界面菜单。可以使得一些完全看不懂Ballance英文的玩家快速进行游戏。但对于Ballance Mod Loader提供的页面没有汉化能力。同时BLinguist不需要修改游戏文件，只需要在Mod设置中简单开关BLinguist的全局设置，即可打开或关闭BLinguist，为之后玩家转型成竞速党提供便利。

- 作者：yyc12345
- 发布时间：2023 年 3 月

#### 下载地址

- [地图下载站](#ballance-地图下载站)
- [GitHub](https://github.com/yyc12345/BMLMods)

#### 操作方式

在配置选项中选择合适的语言，或调整Mod启用与否后，重启游戏即可更改游戏显示语言。

#### 配置选项

- Core
  * Enable - 启用当前Mod。不启用此Mod时，所有文本将退回Ballance默认的渲染模式。然而这并不能阻止本Mod创建一些必须的内容，如果想彻底消除本Mod的影响，请删除本Mod。
  * Language - 决定要显示的语言，重启游戏生效。目前支持填写进去的文本（区分大小写）：`English`（英语），`Chinese`（简体中文），`Arabic`（阿拉伯语），`Japanese`（日语）
- Font
  * FontName - 显示文本用的字体名称，详细请参考FontCraft。重启游戏生效。
  * FontSize - 显示文本用的字体大小，详细请参考FontCraft。重启游戏生效。
  * FontCraft - 启用后，会在Mod加载时，尝试寻找FontCraft，如果找到，则从FontCraft中读取字体设置，同时忽略上述两个字体选项。如果不启用此选项，或没有找到FontCraft，则使用上述两个字体选项来显示文字。该选项主要是为了和FontCraft配合使用，以使得整个游戏界面的字体更加地统一。重启游戏生效。

### ChangeGameSpeed

游戏全局速度调节 Mod。

**注意：本 Mod 的所有功能已经可以被 [PhysicsEditor](#PhysicsEditor) 取代，若无特殊需求请优先使用取代 Mod。**

- 作者：Onlyforyou
- 发布时间：2020-2021

#### 下载地址

- [地图下载站](#ballance-地图下载站)

### Coredump

#### 基础信息

**这是一个未完成的Mod。如果您发现您的Mod列表中有这个Mod，请立即卸载，因为它可能会导致游戏不稳定。**

这是一个原本意图在Ballance运行的任意时刻，通过命令行输入命令，将当前Ballance的运行状态保存为CMO文件的Mod。主要是为了对BML用代码修改后的脚本连线进行分析。由于技术上的原因，这个Mod没有完成，也无法完成既定任务。

该Mod与竞速无关，竞速玩家请立即卸载！

- 作者：yyc12345
- 发布时间：2021 年 11 月

#### 下载地址

- [GitHub](https://github.com/yyc12345/BMLMods)

#### 教程视频

该Mod没有教程视频。

#### 命令

- `coredump` 或 `breakpoint` - 将当前Ballance状态保存到一个名为`runtime_context.nmo`的文件中。

#### 操作方式

在游戏中打开命令输入窗口，输入`coredump` 或 `breakpoint`，导出Ballance当前状态。

#### 配置选项

该Mod没有配置选项。

### CursorClipper

鼠标锁定 Mod，在窗口化游戏中会自动锁定鼠标到窗口内，防止游戏中意外移出鼠标（例如误触触控板等）后出现操作事故。本 Mod 仅会在实际游戏过程中锁定鼠标范围；按下暂停菜单后会自动解锁。

本 Mod 无需配置。

- 作者：BallanceBug
- 发布时间：2023 年 8 月

### ExtraSector

999 小节加载器，使得游戏可以加载超过 8 小节的地图。主要用于游玩原版连体图等。


### ExtraSector

#### 基础信息

由于Ballance原版脚本限制，地图最多被限制为8小节。使用Mod可解除此限制，赋予Ballance加载大于8小节关卡的能力。也就可以加载你们经常玩的1-12或1-13连体关卡了。

对于制图者而言，只需继续正确命名小节即可，`Sector_08`后是`Sector_9`（不是`Sector_09`！），然后接着是`Sector_10`，以此类推。

此Mod最初来源于2jjy所作999小节加载器。

本 Mod 无需配置，安装该Mod后即可正确加载超过8小节的关卡。

- 作者：yyc12345
- 发布时间：2022 年 6 月

#### 下载地址

- [地图下载站](#ballance-地图下载站)
- [GitHub](https://github.com/yyc12345/BMLMods)

### FogMode

迷雾模式 Mod。

- 作者：Ghomist (Zzq_203)
- 发布时间：2022 年

#### 配置选项

*待施工...*

### FontCraft

修改Ballance显示字体的Mod。

#### 基础信息

- 作者：yyc12345
- 发布时间：2021 年 1 月

#### 下载地址

- [地图下载站](#ballance-地图下载站)
- [GitHub](https://github.com/yyc12345/BMLMods)

#### 操作方式

在配置选项中配置希望更换字体的各种属性，重启游戏后应用。

#### 配置选项

- Core
  * Enable - 全局开启此Mod，关闭此选项后将不再修改游戏字体。开关此选项后重启游戏生效。
  * FontName - 字体的名称。需要注意的是，这个名称是字体的英文名称。在Windows系统里双击你想更改的字体后，即可在弹出的字体查看器左上角看到它的英文名称，例如思源黑体的名称是`Source Han Sans`。重启游戏生效。
  * FontSize - 字体的大小。单位为px（像素）。重启游戏生效。
  * FontItalic - 开启后字体将显示为斜体。重启游戏生效。
  * FontBold - 开启后字体将显示为粗体。重启游戏生效。
  * FontUnderLine - 开启后字体将被加上下划线。重启游戏生效。
  * FontColor - 字体颜色，重启游戏生效。支持的颜色有两种：第一种格式是`RRR,GGG,BBB,AAA`格式，其中`RRR,GGG,BBB`是颜色的红绿蓝分量，`AAA`（透明度）部分是可选的，例如`0,0,0`是黑色，`0,0,0,127`是半透明黑色；第二种格式是`#rrggbbaa`（类似于HTML颜色代码，不区分大小写），每一个颜色分量由2位十六进制数字表示，其中透明度分量也是可选的，例如`#000000`是纯黑色，`#1e90ff`是天蓝色，而`#0000007f`则是半透明黑色。
