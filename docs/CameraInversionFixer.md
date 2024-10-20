# CameraInversionFixer

视角颠倒问题修复器。

Ballance 游戏内的摄像机向后移动过快时，有一定概率由于计算错误，导致整个视角颠倒过来，影响游玩体验。本 Mod 会根据玩家设置，尝试修复此问题。

- 作者：BallanceBug
- 发布时间：2024 年 10 月

## 下载地址

- {地图下载站}
- [GitHub](https://github.com/Xenapte/MyBMLMods)

## 配置选项

- Main
  * Enabled - 是否启用本 Mod。
  * EnsureFix - 是否保证修复视角倒置问题。本选项启用时，Mod 将会每游戏帧均检测是否存在视角倒置，并尝试修复。可能会有游戏体验上的影响。若禁用，则玩家需要手动触发修复快捷键（见下文）。
  * FixKey - 修复快捷键。出现视角倒置时按下本快捷键即可尝试修复。默认是 `B` 键。
  * Debug_ToggleInversion - **调试设置**。启用后，按下修复快捷键时会根据当前状态，手动触发或解除视角倒置。
