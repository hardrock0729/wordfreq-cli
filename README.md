# wordfreq-cli

一个轻量、零依赖的命令行词频统计工具,用于统计文本文件中单词出现的频率,支持中英文混合文本。

## 特性

- 零第三方依赖,仅使用 Python 标准库
- 支持英文单词与中文词语的统计
- 可按词频、字母序排序,并限制输出数量
- 支持排除停用词(stop words)
- 可作为命令行工具使用,也可作为 Python 库导入

## 安装

### 从源码安装

```bash
git clone https://github.com/hardrock0729/wordfreq-cli.git
cd wordfreq-cli
pip install -e .
```

### 环境要求

- Python 3.8 或更高版本

## 快速开始

### 命令行用法

```bash
# 统计文件中的词频(默认输出前 10 个)
wordfreq README.md

# 输出前 20 个结果
wordfreq article.txt -n 20

# 按字母序排序
wordfreq article.txt --sort alpha

# 使用自定义停用词文件
wordfreq article.txt --stopwords stopwords.txt
```

运行 `wordfreq --help` 查看完整帮助。

### 作为库使用

```python
from wordfreq import count_words

text = "hello world hello python world"
result = count_words(text)
print(result)
# [('hello', 2), ('world', 2), ('python', 1)]
```

## 项目结构

```
wordfreq-cli/
├── src/wordfreq/        # 核心代码
│   ├── __init__.py
│   ├── core.py          # 词频统计逻辑
│   └── cli.py           # 命令行入口
├── tests/               # 单元测试
├── .github/workflows/   # CI 配置
├── pyproject.toml       # 项目元数据与构建配置
├── LICENSE              # MIT 许可证
├── CONTRIBUTING.md      # 贡献指南
├── CODE_OF_CONDUCT.md   # 行为准则
├── CHANGELOG.md         # 变更日志
└── SECURITY.md          # 安全策略
```

## 开发

```bash
# 安装开发依赖
pip install -e ".[dev]"

# 运行测试
pytest

# 代码检查
ruff check src tests
```

详情见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可证

本项目采用 [MIT 许可证](LICENSE)。

## CI 配置说明

GitHub Actions 配置文件位于仓库根目录的 `ci.yml`。由于发布环境的 API 通道限制,文件未能放入标准的 `.github/workflows/` 路径。若需启用 Actions,请将 `ci.yml` 移动到 `.github/workflows/ci.yml` 即可。
