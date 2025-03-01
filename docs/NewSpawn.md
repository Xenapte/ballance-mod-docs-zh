# NewSpawn

新的自定义出生点 Mod（功能类似于 BML 内建的 `/spawn` 命令但更加强大）。支持重置至不同小节、同小节但不重置机关及影子球录制，方便竞速练习。

## 下载地址

- {地图下载站}
- [GitHub](https://github.com/fluorescia/BallanceNewSpawn)

## 命令

- `/nsp` 或 `/newspawn` - 设置玩家球当前所在的位置为出生点，方便竞速练习等。类似于 [BML](BallanceModLoader.md) 的 `/spawn` 命令，但功能更加强大（详见下文 “操作方式” 和 “配置选项”）。

## 操作方式

**重置玩家球：**

- 输入 `/nsp` 即可记录玩家球当前坐标为新的出生点。
- 不同于 BML 的 `/spawn` 命令，本命令同时会记录玩家当前所在的小节和球的种类。
- 默认配置下，按下 `C` 键玩家就会自动被传送回设置的出生点，并切换为正确的小节和球种。
- 此外，若玩家在同小节进行传送，则可以在设置界面中选择是否重置道具、机关状态（跨小节传送时必会重置道具状态）。若启用，则玩家重置时就相当于是简单的传送，比如推过的栅栏道具会保持推过的状态。否则和 BML 自带的退格重置相同。

**影子球的使用：**（本功能需要在配置中启用）

- 启用后，本 Mod 会在玩家按下 `C` 键重置球时开始录制球的轨迹，同时播放已保存的轨迹的影子球。
- 按下 `V` 键时游戏会保存本次（从按下 `C` 键开始至按下 `V` 键结束）球的运动轨迹，覆盖已保存的轨迹。

**注意：**

- 本 Mod 会在玩家变球时自动禁用 `C` 键重置功能（不然会引发各种 bug）。
- 重开关卡不会重置本 Mod 设置的点位。
- 未设置点位，或设置的点位不在当前关卡时自然也无法按 C 键传送。

## 配置选项

- Main
  * Enabled - 是否启用本 Mod。
  * Prop_Reset - 是否在按下传送快捷键时重置道具状态（仅同小节传送有效）。
  * Spirit_Record - 是否启用影子球。
  * Transport - 传送/重置快捷键（请勿设置为和 BML 的退格重置快捷键相同，这是两个不同的功能）。默认为 `C` 键。
  * Record - 保存本次录制的快捷键。默认为 `V` 键。
