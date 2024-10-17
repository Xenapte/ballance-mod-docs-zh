# AdvancedTravelCam

## 基础信息

改进版的 TravelCam。原 TravelCam 是 BML 自带的 Mod，用于提供脱离玩家球的自由视角，但功能有限。本 Mod 即为其进阶版。

- 作者：BallanceBug
- 发布时间：2022 年 12 月

## 下载地址

- {地图下载站}
- [GitHub](https://github.com/Xenapte/MyBMLMods)

## 教程视频

- [作者的教程视频](https://www.bilibili.com/video/BV1XN411m7a5/)

## 命令

- `+travel` 或 `advancedtravel` - 进入 AdvancedTravelCam。

## 操作方式

- `W` `A` `S` `D` - 操作摄像机移动。
- `Shift` - 使摄像机下降。
- `Space` - 使摄像机上升。
- `Ctrl` - 按下时，摄像机能够以 3 倍速加速移动。和 BML 的 Cheat Mode 的倍速类似。
- `Z` - 按下时摄像头能够往前方自动缩进（**Z**oom），便于仔细观察。此按键按下时，可以同时操作鼠标滚轮以调整放缩度。
- `鼠标左键` - 按下后，鼠标可以在视图内选点传送。选择模式下使用右键可以退出。

## 配置选项

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
