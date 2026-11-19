# 贡献指南

感谢你愿意为 wordfreq-cli 做出贡献!本项目欢迎任何形式的参与:报告 Bug、提出功能建议、改进文档或提交代码。

## 行为准则

参与本项目即表示你同意遵守 [行为准则](CODE_OF_CONDUCT.md)。

## 报告 Bug

提交 Issue 时,请包含以下信息以减少往返沟通:

- 问题的清晰描述
- 复现步骤(尽可能精简)
- 期望行为与实际行为
- 运行环境:操作系统、Python 版本、wordfreq-cli 版本

## 提出功能建议

请先通过 Issue 讨论设计的合理性,再开始编码,避免重复劳动。

## 开发环境搭建

```bash
git clone https://github.com/hardrock0729/wordfreq-cli.git
cd wordfreq-cli
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

## 提交 Pull Request 的流程

1. Fork 本仓库并创建分支:`git checkout -b feature/your-feature`
2. 编写代码,并为新增功能补充单元测试
3. 运行测试与代码检查,确保全部通过:
   ```bash
   pytest
   ruff check src tests
   ```
4. 提交变更,写清楚提交信息(遵循 [Conventional Commits](https://www.conventionalcommits.org/) 规范)
5. Push 到你的 Fork,并向本仓库提交 Pull Request

## 代码规范

- 遵循 PEP 8,使用 4 空格缩进
- 公开函数需有 docstring
- 新增功能需有对应测试,测试覆盖关键分支
- 保持向后兼容,除非有充分理由并在 CHANGELOG 中说明

## 提交信息格式

```
<type>(<scope>): <subject>
```

例如:`feat(core): 支持自定义停用词文件`

类型包括:`feat`、`fix`、`docs`、`test`、`refactor`、`chore`。
