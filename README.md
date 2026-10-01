# 护肤助理 v2.8.1 Draft 9

本分支为预发布分发快照，供外部试用。完整流程、视觉要求、存档与提醒规则已内置。

## Draft 9 流程修复

Draft 9 基于 Draft 8，使用独立的 `v2.8.1-draft9` 标签，历史 `v2.8.1-draft8` 标签及附件保持不变。发布前可上传当前分支的 `SKINCARE_ASSISTANT_CHATGPT.md` 试用；下方固定链接仅在版本实际发布后可用。

本修订修复过敏记录后主流程推进、插问返回、三种产品入口、已有产品逐件评估与用法，以及问题到方案和眼周步骤的对应关系；欢迎词同时说明证据与长期管理如何减少营销干扰。

维护者检查（Python 3 标准库，无第三方依赖）：
- `python3 scripts/build_distribution.py`：从 `SKILL.md` 和 `references/` 同步单文件及当前校验值
- `python3 scripts/build_distribution.py --check`：检查生成产物是否过期
- `python3 -m unittest discover -s tests -v`：静态契约与产物检查，不运行真实 ChatGPT
- `python3 scripts/build_distribution.py --check --package`：在 `dist/` 构建 `skincare-assistant-v2.8.1-draft9.zip` 完整包、单文件及二者校验值；不会发布或改标签

行为验收见 `tests/onboarding_regressions.md`，其中 27 个合成案例仍待真实 ChatGPT 测试。源码是 `SKILL.md` 与 `references/`，不要只改单文件。

## 快速开始

从[版本发布页](https://github.com/shaneisme2010/skincare-assistant-skill/releases/tag/v2.8.1-draft9)下载 `SKINCARE_ASSISTANT_CHATGPT.md`，上传到ChatGPT后发送：

> 请加载我上传的「护肤助理」Skill，并直接开始。

支持网页读取时，也可使用[固定版本单文件链接](https://raw.githubusercontent.com/shaneisme2010/skincare-assistant-skill/v2.8.1-draft9/SKINCARE_ASSISTANT_CHATGPT.md)。无法读取链接时上传文件即可。加载表示在当前聊天使用；不保证永久安装或自动取得联网、出图、存储和提醒工具。

## 文件

- `SKINCARE_ASSISTANT_CHATGPT.md`：自包含的ChatGPT分发版。
- `SKILL.md`与`references/`：支持按需读取技能文件的环境使用。
- `INSTALL.md`：加载、更新与继续档案的方法。
- `RELEASE_NOTES.md`：本版变更与验证范围。
- `SHA256SUMS.txt`：当前分支单文件的校验值；本地打包后二者校验值位于 `dist/SHA256SUMS.txt`，不沿用历史 ZIP 的校验值。

结构检查已通过；真实对话、出图与跨聊天恢复仍需试用验证。软件问题请通过[Issues](https://github.com/shaneisme2010/skincare-assistant-skill/issues)反馈，不包含照片、私人档案或完整聊天。

作者：Shane Chen。按[非商业许可](LICENSE-NONCOMMERCIAL.txt)使用。
