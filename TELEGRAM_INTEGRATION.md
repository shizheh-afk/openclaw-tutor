# Tutor Skill Telegram 集成指南

## 概述
通过 Telegram 接收数学题（文字或图片），自动创建 tutor 项目并启动工作流。

## 安装步骤

### 1. 确保依赖已安装
```bash
cd ~/.openclaw/workspace/skills/tutor-xiaotianfotos
source .venv/bin/activate
```

### 2. 测试触发器
```bash
# 测试文字题目
python tutor_telegram_trigger.py "求解方程 x^2 + 2x + 1 = 0"

# 测试带图片的题目（图片路径为可选）
python tutor_telegram_trigger.py "如图所示，求三角形的面积" /path/to/image.png
```

## 使用方式

### 方式一：通过 OpenClaw 配置自动触发

在 OpenClaw 配置中添加规则，当检测到数学题时自动调用触发器。

### 方式二：手动触发

在 Telegram 中发送题目，然后运行：
```bash
python tutor_telegram_trigger.py "<粘贴题目内容>"
```

### 方式三：通过 OpenClaw 会话触发

在 OpenClaw 中输入：
```
@tutor 求解方程 x^2 + 2x + 1 = 0
```

## 项目结构

创建的项目将包含：
```
~/Documents/tutor-projects/
└── 20260328_224100_求解方程_x2_2x_1/
    ├── 题目.txt              # 原始题目
    ├── problem_info.json      # 题目元数据
    ├── WORKFLOW_GUIDE.md      # 工作流指导
    ├── math_analysis.md       # (待创建) 数学分析
    ├── 数学_xxxx.html         # (待创建) HTML可视化
    └── 分镜.md                # (待创建) 分镜脚本
```

## 工作流程

1. **接收题目** → 通过 Telegram 发送文字或截图
2. **创建项目** → 自动创建项目目录和初始文件
3. **数学分析** → 创建 `math_analysis.md` 分析数学事实
4. **HTML可视化** → 生成 `数学_日期_题目.html`
5. **分镜脚本** → 生成 `日期_题目_分镜.md`
6. **TTS音频** → 生成配音文件
7. **生成视频** → 渲染最终教学视频

## 配置选项

### 修改项目保存路径
编辑 `tutor_telegram_trigger.py` 中的 `PROJECTS_DIR`：
```python
PROJECTS_DIR = Path.home() / "你的/自定义/路径"
```

### 修改默认语音
在 `scripts/generate_tts.py` 中修改 `--voice` 参数：
```bash
--voice xiaoxiao  # 中文女声
--voice xiaoyi    # 中文男声
```

## 故障排除

### 问题：提示 "command not found: python"
**解决**：使用完整路径
```bash
~/.openclaw/workspace/skills/tutor-xiaotianfotos/.venv/bin/python tutor_telegram_trigger.py "题目"
```

### 问题：无法创建项目目录
**解决**：检查权限
```bash
mkdir -p ~/Documents/tutor-projects
chmod 755 ~/Documents/tutor-projects
```

## 来源信息
- **GitHub**: https://github.com/xiaotianfotos/skills/tree/main/tutor
- **作者**: 小天fotos (xiaotianfotos)
- **B站**: https://space.bilibili.com/28554995
- **安装日期**: 2026-03-28
