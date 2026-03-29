# 🎓 Tutor - 数学教学视频制作

<p align="center">
  <img src="https://img.shields.io/badge/OpenClaw-Skill-blue" alt="OpenClaw Skill">
  <img src="https://img.shields.io/badge/version-1.0.0-green" alt="Version">
  <img src="https://img.shields.io/badge/license-MIT-yellow" alt="License">
</p>

一对一辅导老师技能，用于解答数学题，生成 HTML 讲解文档和带配音的 Manim 动画视频。

> 📝 **原创声明**: 本 Skill 基于 [xiaotianfotos/skills](https://github.com/xiaotianfotos/skills) 的原创工作，感谢原作者的贡献！

## ✨ 核心特性

- 📐 **数学建模**: 推导数学事实，建立几何模型
- 🎨 **HTML 可视化**: SVG 画图形，展示画图过程
- 🎬 **分镜脚本**: 定义幕结构，设计画面/字幕/读白
- 🔊 **TTS 配音**: 自动生成语音文件
- 🎥 **Manim 动画**: 生成专业数学教学视频
- 🔄 **完整工作流**: 从题目到视频的端到端解决方案

## 🚀 快速开始

### 安装

```bash
# 克隆仓库
git clone https://github.com/shizheh-afk/openclaw-tutor.git
cd openclaw-tutor

# 创建虚拟环境
uv venv .venv
source .venv/bin/activate

# 安装依赖
uv pip install -r requirements.txt
```

### 使用流程

```bash
# 1. 初始化项目
python init.py [项目目录]

# 2. 准备分镜脚本（参考 references/storyboard_sample.md）

# 3. 生成 TTS 音频
python scripts/generate_tts.py 分镜.md ./audio --voice xiaoxiao

# 4. 验证音频并更新分镜时长
python scripts/validate_audio.py 分镜.md ./audio

# 5. 生成脚手架代码
# 根据 templates/script_scaffold.py 生成 script.py

# 6. 检查代码结构
python scripts/check.py

# 7. 渲染视频
python scripts/render.py
```

## 📋 八步工作流

```
┌─────────────────────────────────────────────────────────────┐
│  步骤1: 数学分析                                              │
│  ├── 推导数学事实                                             │
│  ├── 建立几何模型                                             │
│  └── 确定图形构建方法                                          │
├─────────────────────────────────────────────────────────────┤
│  步骤2: HTML 可视化                                           │
│  ├── SVG 画图形                                               │
│  ├── 展示画图过程                                             │
│  └── 标注关键要素                                             │
├─────────────────────────────────────────────────────────────┤
│  步骤3: 分镜脚本                                              │
│  ├── 定义幕结构（不限制幕数）                                   │
│  ├── 设计画面/字幕/读白                                        │
│  └── 生成音频清单                                             │
├─────────────────────────────────────────────────────────────┤
│  步骤4: TTS 生成                                              │
│  └── 生成配音文件 (audio/audio_XXX_幕名.wav)                   │
├─────────────────────────────────────────────────────────────┤
│  步骤5: 验证更新                                              │
│  ├── 验证音频存在性                                           │
│  ├── 检查时长 > 0                                             │
│  └── 更新分镜时长                                             │
├─────────────────────────────────────────────────────────────┤
│  步骤6: 脚手架                                                │
│  └── 生成 script.py 伪代码框架                                │
├─────────────────────────────────────────────────────────────┤
│  步骤7: 生成代码                                              │
│  ├── 实现 calculate_geometry()                                │
│  ├── 实现 assert_geometry()                                   │
│  └── 实现每幕动画                                             │
├─────────────────────────────────────────────────────────────┤
│  步骤8: 检查与渲染                                            │
│  ├── 代码结构检查                                             │
│  ├── 几何正确性验证                                           │
│  └── 生成最终视频                                             │
└─────────────────────────────────────────────────────────────┘
```

## 📁 目录结构

```
tutor/
├── SKILL.md                    # 工作流程定义
├── README.md                   # 本文件
├── requirements.txt            # Python 依赖
├── init.py                     # 项目初始化脚本
├── tutor_telegram_trigger.py   # Telegram 集成
├── scripts/                    # 工具脚本
│   ├── generate_tts.py         # TTS 生成
│   ├── validate_audio.py       # 音频验证
│   ├── check.py                # 代码结构检查
│   └── render.py               # 渲染流水线
├── templates/                  # 模板文件
│   ├── script_scaffold.py      # Manim 脚手架
│   └── script_example.py       # 示例代码
├── references/                 # 参考资料
│   └── storyboard_sample.md    # 分镜脚本示例
└── sample/                     # 示例项目
    └── geometry_proof/         # 几何证明示例
```

## 🎯 关键原则

### ❌ 禁止使用坐标系
**绝不用坐标系来求解**，应该用各种定义和推理。

**错误示例**（坐标法）:
```
设 B=(0,0), C=(5,0), A=(1.8, 2.4)...
面积 = ½ × 底 × 高
```

**正确示例**（几何推理）:
```
1. 由勾股定理：BC = √(AB² + AC²) = 5
2. 正方形性质：BE = BC = 5
3. 等积变换：S△ABE = S△ABC × (EB/BC)
```

### ✅ 音频必填
每幕必须调用 `self.add_sound()`，否则视频无声音！

### ✅ 音画同步
画面等待音频（动画时长 >= 音频时长），确保讲解和动画同步。

### ✅ 高亮对应
配音提到什么，画面高亮什么。

## 🛠️ 依赖

- [uv](https://github.com/astral-sh/uv) - Python 包管理器
- [manim](https://github.com/ManimCommunity/manim) - 数学动画引擎
- [edge-tts](https://github.com/rany2/edge-tts) - 文本转语音

## 📝 分镜脚本示例

见 [references/storyboard_sample.md](references/storyboard_sample.md) - 第九十九题：证明四点共圆

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

本项目采用 [MIT License](LICENSE) 开源许可证。

## 🙏 致谢

- **原创作者**: [xiaotianfotos/skills](https://github.com/xiaotianfotos/skills) - 感谢原作者的优秀工作！
- [Manim Community](https://www.manim.community/) - 数学动画引擎
- [Edge TTS](https://github.com/rany2/edge-tts) - 免费文本转语音

---

<p align="center">
  Made with ❤️ for OpenClaw
</p>
