# FogMode

迷雾模式 Mod。为 Ballance 添加线性雾效果。

**注意**：由于游戏内使用黑色为透明色，所以仅保证雾为**黑色**（`black`）时透明贴图正常，设置为彩色雾可能导致预期以外的视觉效果。含有透明贴图的物体包括但不限于：分数球、生命球、存档点火焰、渐变柱子等。

- 作者：Ghomist (Zzq_203)
- 发布时间：2022 年 4 月

## 下载地址

- {地图下载站}
- [GitHub](https://github.com/Ghomist/FogMode4Ballance)

## 配置选项

- `Fog` - 迷雾配置。
  * `Enable` - 是否启用迷雾。默认为关闭。
  * `Start` - 雾的模拟起始距离，起始距离内不会有雾。默认为 30。
  * `End` - 雾的模拟结束距离，大于结束距离的所有物体都会被雾完全掩盖且不可见。默认为 65。
  * `Color` - 雾的颜色。可以使用 HEX 颜色值如 `#008000`。也可以使用预设的已命名的颜色。默认为 `black`。
    + 预设颜色列表：`black`, `gray`, `green`, `orange`, `pink`, `silver`, `aqua`, `cyan`, `purple`, `iris`, `red`, `white`, `yellow`。
