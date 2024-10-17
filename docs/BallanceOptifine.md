# BallanceOptifine

## 基础信息

Ballance 高清修复，为一些老旧地图添加阴影，渐变柱子等。效果不一定是最佳，且可能会因为开启而破坏了关卡原有体验。对于旧版渐变柱子（通过拉伸 UV 来实现柱子渐变的柱子）甚至会破坏其不断状态。

名称取自 Minecraft 同名Mod，Optifine，高清修复，其为旧版 Minecraft 加速其图形性能。

- 作者：yyc12345
- 发布时间：2020 年 12 月

## 下载地址

- {地图下载站}
- [GitHub](https://github.com/yyc12345/BMLMods)

## 操作方式

在配置选项中配置需要处理的内容，然后加载老旧地图，即可享受修复成果。

## 配置选项

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
