# Ballance Mod 文档

本文档介绍适用于 [Ballance Mod Loader (简称 BML)](https://github.com/Gamepiaynmo/BallanceModLoader) 或 [Ballance Mod Loader Plus (简称 BML+ 或 BMLP)](https://github.com/doyaGu/BallanceModLoaderPlus) 的 Mod，因此你需要先安装其一才能使用。

本文档由 BallanceBug 和 yyc12345 撰写于 2024 年 10 月 7 日至 10 月 16 日。

## Mod 获取方式

### Ballance 地图下载站

绝大多数 Mod 均可以在 [Ballance 地图下载站](http://ballancemaps.ysepan.com)下载（虽然名称是 “地图” 下载站，但实际上也可以下载到 Mod）。

### 其他下载方式

- 有些 Mod 因为需要时常更新，或者内容不太适合正常发布，地图下载站不会收录。请参见 Mod 具体介绍内列出的下载方式。
- 很多 Mod 也可以从各常用 Ballance 交流群的群文件内下载。
- 有能力者自然可以直接从 Mod 源码自行编译。

## Mod 详解

### BallanceModLoader

Ballance Mod Loader（BML）的设置。游戏内 BML 以内建 Mod 的形式出现。

本章节以原 BML（或称**老 BML**）的设定为准。

#### 命令

- `/bml` - 显示 BML 的相关信息。
- `/cheat [true|false]` - 开启或关闭 Cheat Mode（作弊模式）。若不指定开关状态则会根据当前状态自动切换。
- `/clear` - 清除当前显示的所有历史消息。
- `/help` - 显示帮助。
- `/kill` - 触发掉球自杀。
- `/score add|sub|set <分数>` - 设置玩家的额外得分。**需要 Cheat Mode。**
- `/sector <小节>` - 快速跳转到对应小节。**需要 Cheat Mode。**
- `/spawn` - 设置玩家球当前所在的位置为出生点，方便竞速练习等。**需要 Cheat Mode。**
- `/speed <倍速>` - 设置玩家球当前所在的位置为出生点，方便竞速练习等。**需要 Cheat Mode。**
- `/travel` - 进入自由视角模式。
  * **注意**：BML 自带的自由视角功能很不方便，玩家应当使用其改进替代品 [AdvancedTravelCam](#advancedtravelcam)。
- `/watermark` - 切换当前 BML 水印显隐。**老 BML 专属。**
- `/win` - 直接触发通关效果。**需要 Cheat Mode。**

#### 操作方式

**默认状态下：**

- `R` - 触发掉球自杀。

**Cheat Mode 下：**

- 基础 Cheat Mode 功能
  * `F1` - 使玩家球上升。
  * `F2` - 使玩家球下降。
  * `I` - 切换玩家球为纸球。
  * `O` - 切换玩家球为木球。
  * `P` - 切换玩家球为石球。
  * `退格` - 快速重置当前小节（同时会将玩家球重置至当前出生点）。
  * `L` - 增加一个额外生命。
  * `Ctrl` - （按住时）启用 3 倍球速。
  * `F` - （按住时）跳过本帧渲染，快进游戏。
- 其他调试功能：按住以下按键时可以在玩家球正上方生成调试道具。松开按键前调试道具不会自动物理化，此时保持按下按键状态可以调整道具球位置。使用正常移动按键移动调试道具，`右Shift` 上升，`右Ctrl` 下降。
  * `J` - 生成道具纸球。
  * `K` - 生成道具木球。
  * `N` - 生成道具石球。
  * `M` - 生成箱子。

**启用自定义摄像机设置时：**

- `D` - 重置摄像机状态。
- `W` - 使摄像机旋转 45 度。
- `Q` `E` - 使摄像机向**左**或**右**（非 90 度）旋转。
- `A` `Z` `S` `X` - 使摄像机向**上、下、前、后**移动。

#### 配置选项

- Misc - 杂项选项。
  * SkipLoadingAnim - 跳过游戏开始时的加载界面（Logo 动画等）。
  * FullScreen - 切换全屏模式的快捷键。

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

Ballance **多人联机** Mod。全称 Ballance 大型多人在线（Ballance Massively Multiplayer Online）。**简称 BMMO**，俗称**联机插件**。

完整简介（包括下载地址、操作方式、命令、配置选项等）请参照 Ballance Wiki：

- [BallanceMMO 简介](https://ballance.wiki/Ballance%E5%A4%A7%E5%9E%8B%E5%A4%9A%E4%BA%BA%E5%9C%A8%E7%BA%BF%E6%B8%B8%E6%88%8F)
- [BallanceMMO 客户端使用说明](https://ballance.jxpxxzj.cn/wiki/BallanceMMOClient/zh)

### BMMOAntiCheat

BMMO 联机比赛时的反作弊 Mod，检测到玩家非法行为时自动公屏警告。

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

**注意：本 Mod 的所有功能已经可以被 [PhysicsEditor](#physicseditor) 取代，若无特殊需求请优先使用取代 Mod。**

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

#### 基础信息

由于Ballance原版脚本限制，地图被限制为最多8小节。使用Mod可解除此限制，赋予Ballance加载大于8小节关卡的能力。也就可以加载你们经常玩的1-12或1-13连体关卡了。

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

*见游戏内设置选项。*

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

### FramerateUnlocker

**注意**：BML+ 已内置本 Mod，本设置可以直接在 BML 内修改。

游戏帧率解锁工具。可以自定义是否启用垂直同步，是否解锁或手动设置游戏帧率上限。

- 作者：Swung0x48
- 发布时间：2021 年 1 月

#### 下载地址

- [地图下载站](#ballance-地图下载站)
- [GitHub](https://github.com/Swung0x48/FramerateUnlocker)

#### 配置选项

- Tweaking
  * FrameRateOverrideType - 帧率模式。
    + `0` - 开启垂直同步。
    + `1` - 完全解除所有帧率限制。
    + `2` - 自定义帧率上限。
  * FramerateCap - FPS 上限。
    + 本设置仅在 FrameRateOverrideType 被设为 `2`（自定义上限）时有效。

### FreeViewRotation

自由视角 Mod。使用后游戏内摄像机的视角（以及玩家球运动方向）会变成由鼠标而不是视角转向热键操控。

- 作者：BallanceBug
- 发布时间：2022 年 12 月

#### 下载地址

- [地图下载站](#ballance-地图下载站)
- [GitHub](https://github.com/Xenapte/MyBMLMods)

#### 配置选项

- Main
  * Enabled - 是否启用。
  * ShowCursor - 是否显示鼠标指针。Ballance 游戏内正常会自动禁用鼠标指针，但自由视角 Mod 使用鼠标控制视角，若启用可能对操控有所帮助。
  * Sensitivity - 鼠标灵敏度，越高越灵敏。

### Interference

影子球干扰 Mod。可以用来训练玩家联机时的抗干扰能力。

- 作者：Ghomist (Zzq_203)
- 发布时间：2022 年

#### 配置选项

*见游戏内设置选项。*

### KeystrokeViewer

游戏内按键显示 Mod。比外接按键显示工具稍微容易安装配置一点，但功能也更简陋。

- 作者：BallanceBug
- 发布时间：2023 年 10 月

#### 下载地址

- [地图下载站](#ballance-地图下载站)
- [GitHub](https://github.com/Xenapte/MyBMLMods)

#### 配置选项

- Main
  * X_Position - 按键显示区域最左端的 X 座标相对于整个窗口宽度的比例。用于调节按键显示的位置。
  * X_Width - 按键显示区域最大宽度。
  * Y_Position - 按键显示区域最上端的 Y 座标相对于整个窗口高度的比例。用于调节按键显示的位置。
  * Font_Size - 按键显示的字号（大小）。
  * All_Keys_Mode - 是否显示所有按下的按键。默认模式下本 Mod 只会显示游戏内最常用的按键。
- Keys
  * *按键的键位设置。本 Mod 默认情况下无法读取玩家的键位设置，因此若有非标准键位必须手动设置。*

### LanternFader

用于改善玩家在灯柱附近时的性能，增加游戏帧率。

本 Mod 无需配置。

- 作者：doyaGu
- 发布时间：2023 年 2 月

#### 下载地址

- [地图下载站](#ballance-地图下载站)

### NewSpawn

新的自定义出生点 Mod（功能类似于 BML 内建的 `/spawn` 命令）。支持重置至不同小节，或同小节不重置机关及影子球录制，方便竞速练习。

#### 下载地址

- [地图下载站](#ballance-地图下载站)
- [GitHub](https://github.com/fluorescia/BallanceNewSpawn)

#### 配置选项

*见游戏内设置选项。*

### PhysicsEditor

游戏物理参数编辑器。可以调整重力、游戏速度等。

注意事项：本 Mod 无法保证启用之后所有时刻均保持设定的物理参数不变。例如，玩家离开暂停菜单继续游戏时，游戏可能会有短暂恢复一帧正常游戏重力、速度设定。

- 作者：BallanceBug
- 发布时间：2022 年 9 月

#### 下载地址

- [地图下载站](#ballance-地图下载站)
- [GitHub](https://github.com/Xenapte/BallancePhysicsEditor)

#### 配置选项

**注意**：本 Mod 不提供启用或禁用选项，修改数值后自动启用，将所有数值调回默认值后自动禁用。

- Gravity
  * X / Y / Z - XYZ 三轴方向上各自的重力加速度。Ballance 内的重力加速度由此三维向量决定，实际上支持非垂直方向的重力。
    + 默认值为：X 和 Z 均为 `0`，Y 为 `-20`。
- Time
  * PhysicsTimeFactor - 物理时间速度。只会影响物理运算的速度，其它场景（例如关卡加载动画等）不受影响。
    + **注意：默认的物理速度实际上使用了 2 倍速**。
  * GlobalGameSpeed - 全局游戏速度。会影响所有游戏场景的速度。
    + 默认为 1 倍速；本 Mod 没有对填入数值范围进行限制，设为 0 倍速导致游戏卡死后果自负。

### PositionViewer

玩家球坐标与速度显示器。

- 作者：BallanceBug
- 发布时间：2022 年 12 月

#### 下载地址

- [地图下载站](#ballance-地图下载站)
- [GitHub](https://github.com/Xenapte/MyBMLMods)

#### 配置选项

- Main
  * Y_Position - 坐标与速度文字显示范围最顶端的位置（相对于整个游戏高度的比例，例如 0.9 相当于从上往下 90% 高度的位置）。
  * Font_Size - 字号。
  * Position_Update_Interval - 坐标更新的时间间隔，单位是毫秒。默认不会每帧都更新（游戏内连续更新文字会导致性能下降）。
  * Speed_Update_Interval - 速度更新的时间间隔，单位是毫秒。

### RealTimeMeter

现实时间计时器，用于计算竞速实际所用时间，可用于全关连打等竞速挑战中。

- 作者：BallanceBug
- 发布时间：2022 年 9 月

#### 下载地址

- [地图下载站](#ballance-地图下载站)
- [GitHub](https://github.com/Xenapte/BallanceRealTimeMeter)

#### 配置选项

- Main
  * Enabled - 是否启用。
  * StreakMode - 连打模式。设为 0 为禁用，否则效果为计时器通关后不重置，直到所设置的关卡数字号结束。
    + 例：将本选项设为 12，则玩家从第 1 关开始游戏，中间各关均连续不重置计时，直到通关 12 关为之。

### ScreenCapturer

截图器 Mod，为 Ballance 增加内置截图功能。

本 Mod 安装后，默认配置下按下 `F8`，截图将会以 PNG 格式自动保存在 Ballance 安装目录下的 Screenshots 文件夹，若截图成功则会产生文字消息提示。截图默认以截图时间（精确到秒）命名。

比起外部工具，本截图 Mod 的优点在于能一键对准游戏画面截图并直接保存。类似于 Minecraft 的 F2 按键或带 Steam Overlay 的游戏的 F12 按键等。

- 作者：BallanceBug
- 发布时间：2022 年 12 月

#### 下载地址

- [地图下载站](#ballance-地图下载站)
- [GitHub](https://github.com/Xenapte/MyBMLMods)

#### 配置选项

- Action
  * KeyBinding - 截图快捷键。默认的截图按键是 `F8`，默认选择此快捷键是因为其他常用截图快捷键和 Ballance 下的惯用设置冲突，但玩家可以自行调节。
  * Notify - 截图后是否以游戏内消息的形式对玩家进行通知。若不希望产生通知（例如需要快速多次截图时），可以关闭此选项。
- Saving
  * SaveAsJPEG - 是否以 JPEG 格式（扩展名为 .jpg）保存截图。默认的截图格式为无损压缩的 PNG，但 PNG 文件大小较大，若玩家对画质需求不大，可以改为有损压缩的 JPEG。
  * CopyToClipboard - 复制到剪贴板。默认截图器只会保存截图文件，此选项可以在保存截图同时把截图复制到剪贴板，方便快速分享截图。
  * ClipboardOnly - 仅将截图复制到剪贴板，不实际保存截图文件。若 “复制到剪贴板” 选项未启用，此选项将会被无视。适用于玩家仅需要临时截图并分享的场景。

### Sectorless

暴力移动所有游戏内机关到第一小节。方便预览地图或联机比赛旁观等。

- 作者：BallanceBug
- 发布时间：2024 年 9 月

#### 下载地址

- [地图下载站](#ballance-地图下载站)
- [GitHub](https://github.com/Xenapte/MyBMLMods)

#### 配置选项

- Main
  * Enabled - 是否启用。
  * RemoveCheckpoints - 是否移除所有盘点。默认本 Mod 只会将所有机关移动到第一小节，但所有盘点还在，如果玩家触发盘点则会进入下一小节，导致所有机关均消失。本选项会将这些盘点也移除，防止意外触碰。
  * ~~Experimental_DuplicateModules - **实验性选项，当前没有任何作用**~~。请不要尝试启用本选项。

### Segment

分段计时器 Mod，用于对同一地图不同小节竞速的用时进行分段计时。

- 作者：Swung0x48
- 发布时间：2020 年 11 月

#### 下载地址

- [地图下载站](#ballance-地图下载站)
- [GitHub](https://github.com/Swung0x48/Segment)

#### 配置选项

*见游戏内设置选项。*

### Speedometer

玩家球速度显示器。

**注意：本 Mod 的所有功能已经可以被 [PositionViewer](#positionviewer) 取代（且性能更好），若无特殊需求请优先使用取代 Mod。**

本 Mod 无需配置。

- 作者：Swung0x48
- 发布时间：2021 年 9 月

#### 下载地址

- [地图下载站](#ballance-地图下载站)
- [GitHub](https://github.com/Swung0x48/Speedometer)

### SpeedrunShortcuts

为竞速常用操作提供快捷键，例如一键切换 cheat mode、重新开始、设置出生点、切换小节等。

本 Mod 的重开关卡功能甚至可以无视游戏内的暂停菜单限制，例如玩家可以在掉球或者变球时按下本快捷键直接重开。

**注意**：由于存在公平性问题，常见[联机](#ballancemmo)比赛均严禁玩家在变球或者死球时重开。联机比赛中触发上述行为（俗称 “**非法操作**”）一般会被直接视作违规并取消成绩。此外，由于游戏掉球时存在全屏渐变动画，玩家在掉球时重开会导致渐变效果冻结，产生全屏半透明屏障干扰（俗称 “**白内障**”），需要玩家再次触发完整的掉球动画才能解除。

- 作者: BallanceBug
- 发布时间：2022 年 6 月

#### 下载地址

- [地图下载站](#ballance-地图下载站)
- [GitHub](https://github.com/Xenapte/BallanceSpeedrunShortcuts)

#### 配置选项

**注意**：以下的所有快捷键均需要配合 “修饰键” 使用。例如，默认配置内 Cheat Mode 快捷键为 `C`，修饰键为 `Alt`，则玩家需要同时按下 `Alt`+`C` 才有切换效果。

- Keys - **按键设置**  
  * CheatToggle - 切换 Cheat Mode。
  * SetSpawn - 设置出生点。
  * Restart - 重新开始当前关卡。本功能可以无视常规游戏内的暂停菜单限制。
    + 本按键可以设为和修饰键相同，这样玩家只需按下修饰键就可以重开。但是，为了防止意外重开事故，此操作需要玩家双击修饰键才能触发。
  * SetSector - 设置当前小节，需要玩家同时按下修饰键、本设置快捷键，以及键盘上的数字键才能触发。
    + 例如，默认配置下本选项快捷键为 `W`，则玩家同时按下 `Alt`+`W`+`2` 会自动切换到第 2 小节。
  * ModifierKey - **修饰键*。上述所有快捷键均需要配合修饰键使用，以防意外触发。
- BMMO - [联机 Mod](#ballancemmo) 相关功能
  * StrictMode - “严格模式”。本选项启用后，联机游戏时本 Mod 会自动禁止玩家在掉球或变球时重开，避免产生上文所述的 “非法操作”。

### SpriteTextHUD

以性能更好的方式显示 FPS 和 SR Timer，可以用于提升游戏帧率。

本 Mod 以 SpriteText 的格式重新显示 BML 自带的 FPS 和 SR Timer 提示文本。玩家需要手动关闭 BML 自带的这些元素才能使用。

- 作者：BallanceBug
- 发布时间：2023 年 11 月

#### 下载地址

- [地图下载站](#ballance-地图下载站)
- [GitHub](https://github.com/Xenapte/MyBMLMods)

#### 配置选项

- Main
  * ShowSRTimer - 是否显示 SR Timer。
  * ShowFPS - 是否显示 FPS。
  * SRTimerColor - SR Timer 的颜色（以 16 进制表示）。
  * FPSColor - FPS 的颜色（以 16 进制表示）。
  * SRTimerFont - SR Timer 的字体。
  * FPSFont - FPS 的字体。
  * SR_ZOrder - SR Timer 的 Z-order（用于判定屏幕上元素绘制时的前后覆盖顺序）。
  * FPS_ZOrder - FPS 的 Z-order

### StaticCamera

“静态摄像机”，摄像机相对于玩家球的角度和距离完全静止。

原版摄像机会根据玩家的运动去动态追逐玩家球，因此动感更为强烈；本 Mod 会直接取消这些效果，使得摄像机完全和玩家球同步。

- 作者：BallanceBug
- 发布时间：2024 年 4 月

#### 下载地址

- [地图下载站](#ballance-地图下载站)
- [GitHub](https://github.com/Xenapte/MyBMLMods)

#### 配置选项

- Main
  * Enabled - 是否启用本 Mod。
  * CameraRotateKey - 摄像机旋转按键。
  * LeftRotateKey / RightRotateKey - 摄像机左/右转按键。
  * CameraSyncKey - 摄像机同步键。将本静态摄像机和游戏默认的动态摄像机同步。
  * AlternativeKeyCheck - 使用备用按键检测方式。

### SysInfoDisplay

游戏内叠加显示系统状态信息（现在时间、电量等）。

- 作者：BallanceBug
- 发布时间：2022 年 11 月

#### 下载地址

- [地图下载站](#ballance-地图下载站)
- [GitHub](https://github.com/Xenapte/BallanceSysInfoDisplay)

#### 配置选项

- Main
  * Enabled - 是否启用本 Mod。
  * DisplayBatteryStatus - 是否显示电池状态。台式机等设备不存在电池供电选项，此时可以将此禁用。
- Text
  * BatterySameLine - 是否将电池数据和系统时间显示在同一行。
  * TextColor - 文字颜色，以 16 进制表示。
  * FontSize - 字号。

### TASSupport

TAS 支持。本 Mod 为 BML 常见捆绑自带 Mod 之一。

- 作者：Gamepiaynmo
- 发布时间：2021 年 4 月

#### 下载地址

- [地图下载站](#ballance-地图下载站)
- [GitHub](https://github.com/Gamepiaynmo/BML-Mods)

#### 配置选项

*见游戏内配置选项。*

### Unhider

隐藏物体显示器。可以用于显示隐形墙、死亡区等原本隐藏的物体。

- 作者：BallanceBug
- 发布时间：2023 年 11 月

#### 下载地址

- [地图下载站](#ballance-地图下载站)
- [GitHub](https://github.com/Xenapte/MyBMLMods)

#### 配置选项

- Main
  * Enabled - 是否启用本 Mod。
  * AddShadows - 是否为隐藏物体增加影子，方便辨识。
  * UnhideEverything - 显示所有物体。默认情况下本 Mod 只会重新显示死亡区。
- Style
  * DepthCubeColor - 死亡区颜色，以 16 进制表示。
  * DepthCubeOpacity - 死亡区不透明度。0 为完全透明，1 为不透明。
  * OtherColor - 其他被重新显示的物体的颜色，以 16 进制表示。
  * OtherOpacity - 其他被重新显示的物体的不透明度。0 为完全透明，1 为不透明。

### ViewDistanceEditor

游戏摄像机最大视距修改器。也同时支持调节命和分的显示距离。

Ballance 默认摄像机的最大视野是 1200 单位，命和分的最大显示距离分别是 60 和 80 单位。本 Mod 可以用于修改这些数值。

- 作者：BallanceBug
- 发布时间：2023 年 2 月

#### 下载地址

- [地图下载站](#ballance-地图下载站)
- [GitHub](https://github.com/Xenapte/MyBMLMods)

#### 配置选项

**注意**：本 Mod 不提供启用或禁用选项，修改数值后自动启用，将所有数值调回默认值后自动禁用。

- Main
  * ViewDistance - 摄像机视距。默认为 `1200`。
  * ExtraLifeDistance - 生命球最大显示距离。默认为 `60`。
  * ExtraPointDistance - 生命球最大显示距离。默认为 `80`。
