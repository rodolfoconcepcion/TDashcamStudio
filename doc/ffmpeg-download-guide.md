# FFmpeg Binaries Download Guide

TeslaCam Player requires FFmpeg binaries for each platform in the `src-tauri/binaries/` directory.

## Tauri Naming Convention

According to Tauri's `externalBin` configuration, the binaries must be named specifically as follows:

| Platform | Filename |
|------|--------|
| Windows x64 | `ffmpeg-x86_64-pc-windows-msvc.exe` |
| Linux x64 | `ffmpeg-x86_64-unknown-linux-gnu` |
| macOS Intel | `ffmpeg-x86_64-apple-darwin` |
| macOS Apple Silicon | `ffmpeg-aarch64-apple-darwin` |

## Download Links

### Windows x64
- **Download Address**: https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip
- **After extracting**: Find `bin/ffmpeg.exe`
- **Rename to**: `ffmpeg-x86_64-pc-windows-msvc.exe`

### Linux x64
- **Download Address**: https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-linux64-gpl.tar.xz
- **After extracting**: Find `bin/ffmpeg`
- **Rename to**: `ffmpeg-x86_64-unknown-linux-gnu`
- **Note**: Ensure the file has execution permissions (`chmod +x`)

### macOS (Intel & Apple Silicon)
- **Download Address**: https://evermeet.cx/ffmpeg/getrelease/zip
- **After extracting**: Find `ffmpeg`
- **Copy twice as**:
  - `ffmpeg-x86_64-apple-darwin` (Intel)
  - `ffmpeg-aarch64-apple-darwin` (Apple Silicon)
- **Note**: evermeet.cx provides a universal binary that supports both Intel and Apple Silicon.

**Alternative macOS download**:
- https://ffmpeg.org/download.html#build-mac

## Auto-download Scripts

### Windows (PowerShell)
```powershell
cd TDashcamStudio
.\scripts\download-ffmpeg.ps1
```

### macOS / Linux (Bash)
```bash
cd TDashcamStudio
chmod +x scripts/download-ffmpeg.sh
./scripts/download-ffmpeg.sh
```

### Download by Platform
```bash
# Linux only
./scripts/download-ffmpeg.sh --linux

# macOS only
./scripts/download-ffmpeg.sh --macos

# Windows only
./scripts/download-ffmpeg.sh --windows
```

## Validation

Once the download completes, your `src-tauri/binaries/` directory should look like this:

```
src-tauri/binaries/
├── .gitkeep
├── ffmpeg-x86_64-pc-windows-msvc.exe   (~130 MB)
├── ffmpeg-x86_64-unknown-linux-gnu     (~100 MB)
├── ffmpeg-x86_64-apple-darwin          (~80 MB)
└── ffmpeg-aarch64-apple-darwin         (~80 MB)
```

## Notes

1. **File Size**: FFmpeg binaries are large, so they are added to `.gitignore`.
2. **CI/CD**: Use the provided scripts in your CI/CD pipelines to download them automatically.
3. **Version**: We recommend using the latest stable version of FFmpeg.
4. **License**: Use the GPL version to obtain full feature support.
