<p align="center">
  <img src="src/logo-small.png" alt="TeslaCam Studio Logo" width="80" height="80">
</p>
<h1 align="center">TeslaCam Studio</h1>

<p align="center"><a href="README.md">English</a> | <a href="README_ES.md">Español</a> | 简体中文</p>

<p align="center">
  <a href="https://github.com/rodolfoconcepcion/TDashcamStudio/releases"><img src="https://img.shields.io/github/v/release/rodolfoconcepcion/TDashcamStudio?style=flat-square&color=blue" alt="Release"></a>
  <a href="https://github.com/rodolfoconcepcion/TDashcamStudio/releases"><img src="https://img.shields.io/github/downloads/rodolfoconcepcion/TDashcamStudio/total?style=flat-square&color=green" alt="Downloads"></a>
  <a href="https://github.com/rodolfoconcepcion/TDashcamStudio/blob/main/LICENSE"><img src="https://img.shields.io/github/license/rodolfoconcepcion/TDashcamStudio?style=flat-square" alt="License"></a>
  <a href="https://github.com/rodolfoconcepcion/TDashcamStudio/stargazers"><img src="https://img.shields.io/github/stars/rodolfoconcepcion/TDashcamStudio?style=flat-square" alt="Stars"></a>
  <a href="https://github.com/rodolfoconcepcion/TDashcamStudio/actions/workflows/build.yml"><img src="https://img.shields.io/github/actions/workflow/status/rodolfoconcepcion/TDashcamStudio/build.yml?style=flat-square&label=CI" alt="CI"></a>
</p>

专为特斯拉行车记录仪（Tesla Dashcam）打造的现代化多路视频播放与剪辑工具。支持 6 视角（前置、后置、左侧、右侧、左 B 柱、右 B 柱）完美同步播放，现已全面支持**桌面客户端**与**本地 Web / Docker 部署**！

## 🆚 为什么选择 TeslaCam Studio？

相比特斯拉车机自带播放器和传统电脑端视频播放器，本项目提供更强大的功能与更出色的使用体验：

| 功能特性 | 特斯拉车机播放器 | 电脑普通播放器 | TeslaCam Studio (本项目) |
| :--- | :--- | :--- | :--- |
| **多路同步播放** | ✅ 支持 6 摄像头 | ❌ 需逐个打开，无法同步 | ✅ **完美 6 画面毫秒级同步，支持多种排版布局** |
| **大屏浏览体验** | 受限于车机屏幕与车内场景 | 屏幕虽大但文件混乱 | **全平台大屏支持**，事件分类清晰，查找便捷 |
| **智能事件过滤** | 仅基础分类 | ❌ 需在海量文件夹中手动翻找 | ✅ **按日期、时间、事件类型智能筛选** |
| **驾驶数据解析** | ✅ 支持仪表盘显示 | ❌ 仅显示画面，无隐藏数据 | ✅ **可视化仪表盘：车速、踏板、AP/FSD、转向等** |
| **视频可视化剪辑** | ❌ 不支持 | ❌ 需复杂专业软件 (FFmpeg/PR) | ✅ **拖拽式精准裁剪，自动合并多分钟片段** |
| **便捷网格导出** | ❌ 无法快捷导出合成视频 | ❌ 仅能拷贝原始 1 分钟分段 | ✅ **一键导出多视角网格视频，自带行车数据水印** |
| **地图与位置信息** | 基础地图显示 | ❌ 无地理位置信息 | ✅ **显示街道名称，支持一键跳转 Google 地图** |
| **数据与隐私安全** | - | ✅ 本地查看 | ✅ **100% 本地处理**，无任何追踪或数据上传 |

![Screenshot](./.github/assets/home.webp)

## 📺 功能演示

| 功能 | 演示效果 |
| :--- | :--- |
| **极速开启**: 支持文件夹拖拽，即插即用 | ![Quick Start](.github/assets/GIF/drop-open.webp) |
| **现代界面**: 深色/浅色模式自适应，流畅动效 | ![Modern UI](.github/assets/GIF/ui.gif) |
| **智能筛选**: 快速按日期与事件类型精准定位 | ![Smart Filtering](.github/assets/GIF/filter.gif) |
| **地图集成**: 显示实际街道名称与地图跳转 | ![Map Integration](.github/assets/GIF/map.webp) |
| **倍速调节**: 0.5x - 2.0x 自由变速播放 | ![Playback Speed](.github/assets/GIF/speed.gif) |
| **驾驶数据**: 实时呈现车速、转向灯、油门深度、刹车、AP/FSD 状态 | ![Driving Data](.github/assets/GIF/meta-data.webp) |
| **速度曲线**: 进度条背景实时绘制速度曲线，快速定位急加速/急刹 | ![Speed Curve](.github/assets/GIF/speed-curve.webp) |
| **数据导出**: 一键将事件完整驾驶元数据导出为 CSV | ![Data Export](.github/assets/GIF/csv-export.webp) |
| **同步播放**: 完美同步 6 视角，多种排版随心切换 | ![Sync Playback](.github/assets/GIF/play.webp) |
| **可视化剪辑**: 拖拽手柄精准裁剪，跨分钟无缝衔接 | ![Visual Clipping](.github/assets/GIF/export.webp) |
| **导出成片**: 一键生成带时间戳与驾驶数据水印的网格视频 | ![Export Results](.github/assets/GIF/6-exported-play.webp) |

## ✨ 核心特性

### 🎥 视频播放与数据可视化
*   **多视角同步播放**：完美同步 6 摄像头画面，支持 6 宫格全景、新 4 宫格、经典 4 宫格及单镜头全屏模式。
*   **支持 B 柱摄像头**：全面覆盖特斯拉车身 B 柱广角视野。
*   **实时仪表盘**：自动解析 SEI 元数据，实时显示车速、挡位、转向角度、油门/刹车踏板、Autopilot (AP/FSD) 状态及 GPS 坐标。
*   **进度条速度曲线**：在进度条背景绘制连续速度波形，一眼辨识急加速与紧急制动瞬间。
*   **驾驶数据导出**：支持一键将当前事件所有时间戳的驾驶元数据导出为 CSV 表格。
*   **智能事件筛选**：按日期、时间戳和事件分类（Recent、Saved、Sentry 哨兵）快速检索。
*   **地图定位**：提取坐标显示真实街道名称，点击即可在地图中查看具体位置。

> **说明：** 车辆行车元数据仅适用于车机固件版本 **2025.44.25.11** 及以上录制的视频。

![Metadata Display 1](.github/assets/screenshot1.webp)
![Metadata Display 2](.github/assets/screenshot2.webp)

### ✂️ 视频剪辑与网格导出
*   **可视化精准裁剪**：在进度条上拖拽蓝色选区手柄，自由设定导出起止时间。
*   **跨分钟自动无缝合并**：自动处理跨越多个 1 分钟原始录像片段的剪辑并平滑拼合。
*   **多镜头网格合成**：支持将选中的摄像头角度合成 2x2 或 2x3 网格视频，带有大字号清晰标记。
*   **行车信息水印**：在导出视频画面上实时烧录时间戳与行车数据（车速、挡位、AP 状态等）。
*   **自由组合镜头**：可按需自由勾选需要导出的摄像头视角。

### 🎨 现代化交互设计
*   **深色 / 浅色模式**：支持手动切换与系统偏好自动同步。
*   **多语言支持**：原生内置 English（默认）、Español（西班牙语）、简体中文，支持一键切换。
*   **极速本地处理**：基于现代浏览器 Canvas 与 WebCodecs / MediaRecorder 技术，所有处理均在本地完成。

## 🚀 使用方法

### 🖥️ 桌面客户端（推荐）

前往 [Releases 发布页面](https://github.com/rodolfoconcepcion/TDashcamStudio/releases) 下载适配您操作系统的桌面安装包：

| 平台 | 安装包格式 |
|---|---|
| **Windows** | `.exe` (安装程序) / `.msi` |
| **macOS (Apple Silicon M1/M2/M3/M4)** | `.dmg` (aarch64) |
| **macOS (Intel)** | `.dmg` (x64) |
| **Linux** | `.deb` / `.AppImage` / `.rpm` |

> **macOS 用户特别提示：**
> 若打开应用提示“已损坏，无法打开”，是由于 macOS 隔离安全机制导致。请在终端执行以下命令解除隔离：
> ```bash
> sudo xattr -rd com.apple.quarantine /Applications/TeslaCam\ Studio.app
> ```

---

### 💻 本地与 Docker 部署

由于现代浏览器针对本地文件访问的安全策略（CORS / Origin 限制），建议通过本地 Web 服务器或 Docker 容器运行。

**方法一：使用 Docker Compose（推荐）**

1.  **启动服务：**
    ```bash
    docker compose up -d
    ```

2.  **访问应用：**
    在浏览器中打开 `http://localhost:8188`。

3.  **停止服务：**
    ```bash
    docker compose down
    ```

**方法二：使用 Docker CLI**

```bash
docker run -d -p 8188:80 --name tdashcam-studio --restart unless-stopped ghcr.io/rodolfoconcepcion/tdashcamstudio:latest
```

**方法三：使用 Node.js 本地运行**

```bash
npx http-server -p 8188 src
```

然后在浏览器中访问 `http://localhost:8188`。

---

## 🔒 隐私承诺

本工具将用户隐私安全置于首位：
- **100% 本地运算**：所有视频解码、拼接、仪表盘解析与导出操作完全在您的本地设备（浏览器或本地客户端）中运行。
- **零数据上传**：您的行车记录仪视频、GPS 定位及驾驶数据绝不会上传至任何远程服务器或第三方平台。
- **无追踪与分析**：彻底移除所有分析打点与用户追踪代码。

## 🛠️ 技术栈

*   **前端核心**：纯原生 HTML5, CSS3, JavaScript (ES6+)，零框架开销，极速响应。
*   **视频与元数据**：Canvas API, WebCodecs, MediaRecorder, EBML 结构解析。
*   **桌面端封装**：Tauri 2 (Rust 后端 + WebView)，轻量高效，原生打包。

## 📄 开源许可证

本项目基于 AGPL-3.0 许可证开源。
