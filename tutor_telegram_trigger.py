#!/usr/bin/env python3
"""
Tutor Skill Telegram 触发器
通过 Telegram 接收数学题（文字或图片），自动启动 tutor skill 工作流
"""

import os
import sys
import json
import re
import subprocess
from datetime import datetime
from pathlib import Path

# 配置
TUTOR_SKILL_PATH = Path.home() / ".openclaw/workspace/skills/tutor-xiaotianfotos"
PROJECTS_DIR = Path.home() / "Documents/tutor-projects"
VENV_PYTHON = TUTOR_SKILL_PATH / ".venv/bin/python"

def sanitize_filename(text):
    """将文本转换为安全的文件名"""
    # 移除特殊字符，保留中文、英文、数字
    text = re.sub(r'[^\w\u4e00-\u9fff\s-]', '', text)
    # 替换空格为下划线
    text = re.sub(r'\s+', '_', text)
    # 限制长度
    return text[:50] if text else "math_problem"

def create_project(problem_text, image_path=None):
    """创建新的 tutor 项目"""
    # 生成项目目录名
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    problem_slug = sanitize_filename(problem_text[:30] if problem_text else "problem")
    project_name = f"{timestamp}_{problem_slug}"
    project_dir = PROJECTS_DIR / project_name
    
    # 创建项目目录
    project_dir.mkdir(parents=True, exist_ok=True)
    
    # 保存题目信息
    problem_info = {
        "timestamp": timestamp,
        "problem_text": problem_text,
        "image_path": str(image_path) if image_path else None,
        "project_dir": str(project_dir)
    }
    
    with open(project_dir / "problem_info.json", "w", encoding="utf-8") as f:
        json.dump(problem_info, f, ensure_ascii=False, indent=2)
    
    # 创建初始题目文件
    with open(project_dir / "题目.txt", "w", encoding="utf-8") as f:
        f.write(problem_text)
    
    return project_dir, problem_info

def init_tutor_project(project_dir):
    """初始化 tutor 项目结构"""
    os.chdir(TUTOR_SKILL_PATH)
    
    # 运行 init.py
    result = subprocess.run(
        [str(VENV_PYTHON), "init.py", str(project_dir)],
        capture_output=True,
        text=True
    )
    
    return result.returncode == 0, result.stdout + result.stderr

def generate_workflow_guide(project_dir, problem_info):
    """生成工作流指导文档"""
    guide = f"""# Tutor 项目工作流指导

## 项目信息
- **创建时间**: {problem_info['timestamp']}
- **项目目录**: {project_dir}

## 题目
{problem_info['problem_text']}

## 工作流步骤

### 步骤 1: 数学分析
在 `{project_dir}/math_analysis.md` 中完成数学事实分析

### 步骤 2: HTML 可视化
生成 `{project_dir}/数学_{{日期}}_{{题目}}.html`

### 步骤 3: 分镜脚本
生成 `{project_dir}/{{日期}}_{{题目}}_分镜.md`

### 步骤 4: TTS 音频
```bash
cd {TUTOR_SKILL_PATH}
{VENV_PYTHON} scripts/generate_tts.py audio_list.csv {project_dir}/audio --voice xiaoxiao
```

### 步骤 5: 验证音频
```bash
{VENV_PYTHON} scripts/validate_audio.py {project_dir}/分镜.md {project_dir}/audio
```

### 步骤 6-8: 生成视频
```bash
{VENV_PYTHON} scripts/render.py
```

## 快速开始
1. 进入项目目录: `cd {project_dir}`
2. 查看题目: `cat 题目.txt`
3. 开始数学分析，创建 `math_analysis.md`
"""
    
    with open(project_dir / "WORKFLOW_GUIDE.md", "w", encoding="utf-8") as f:
        f.write(guide)
    
    return guide

def main():
    """主函数 - 处理从命令行传入的题目"""
    if len(sys.argv) < 2:
        print("用法: python tutor_telegram_trigger.py '<题目内容>' [图片路径]")
        print("示例: python tutor_telegram_trigger.py '求解方程 x^2 + 2x + 1 = 0'")
        sys.exit(1)
    
    problem_text = sys.argv[1]
    image_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    print(f"📚 收到数学题: {problem_text[:50]}...")
    
    # 创建项目
    project_dir, problem_info = create_project(problem_text, image_path)
    print(f"📁 项目已创建: {project_dir}")
    
    # 初始化 tutor 项目
    success, output = init_tutor_project(project_dir)
    if success:
        print("✅ Tutor 项目初始化成功")
    else:
        print(f"⚠️ 初始化输出: {output}")
    
    # 生成工作流指导
    guide = generate_workflow_guide(project_dir, problem_info)
    
    print("\n" + "="*50)
    print("🎯 项目创建完成！")
    print("="*50)
    print(f"\n项目目录: {project_dir}")
    print(f"\n下一步:")
    print(f"1. 进入项目: cd {project_dir}")
    print(f"2. 查看题目: cat 题目.txt")
    print(f"3. 开始数学分析，创建 math_analysis.md")
    print(f"\n详细指导请查看: {project_dir}/WORKFLOW_GUIDE.md")

if __name__ == "__main__":
    main()
