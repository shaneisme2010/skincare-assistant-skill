# 护肤助理 Universal Skill v2.0

这是一个平台无关的 AI 护肤工作流包，创建人：Shane Chen。

## 使用方式
- 支持 Agent Skills / skills 目录的平台：导入整个目录或 `skills/skincare-assistant/SKILL.md`。
- 只有“系统提示词 / 智能体指令”的平台：把 `SKILL.md` 全文粘贴到系统指令。
- 支持知识库的平台：把本目录 Markdown 文件上传为知识文件，并把 `SKILL.md` 设为最高优先级行为说明。
- 不支持工具调用的平台仍可运行文字版流程；遇到最新文献、配方、价格或库存时必须明确要求联网/由用户提供资料。

## 平台示例
豆包、DeepSeek、Grok、Claude、ChatGPT、Gemini、Kimi、通义、文心及其他支持自定义智能体/系统提示词的 AI，均可使用核心 Markdown 工作流；具体“安装按钮”和工具能力因平台而异。

## 不包含
不包含任何创建人的个人肤质、照片、病史、地点或护肤库存。


## v2.1 模板系统
所有平台先填 `OUTPUT_SCHEMA.json`，再套用固定的 Skin Report / Product Fit / Skincare Plan 模板，确保不同 AI 输出风格、模块和配色语义一致。


## v2.3 长期管理
新增：8–12周标准照片复评、分阶段护理提醒、可选月度版本检查（仅有更新时提示）、用户同意后的 GitHub Issues 反馈引导，以及统一免责声明。正式发布 GitHub 时需把 `https://github.com/shaneisme2010/skincare-assistant-skill` 替换为仓库真实地址。


## v2.4 安全入口、快捷问答与许可
新增首次自由输入过敏/不耐受采集；允许用户不完成全套测肤即可询问独立护肤问题；加入自定义非商业许可：未经 Shane Chen 书面授权禁止商业使用。详见 `LICENSE-NONCOMMERCIAL.txt`。


## v2.5 中国大陆护肤品牌候选池
根据创建人提供的市场榜单建立国货护肤检索提示池，剔除彩妆为主品牌，并加入毕生之研。该列表只用于扩大候选搜索，不参与疗效排名；所有具体产品仍需核对文献、官方/NMPA资料、完整INCI和用户现有方案。


## v2.6 现有产品优先与准确产品图
新增强制规则：允许用户上传现有护肤品并优先使用；只有用户想换/要求新品、现有方案有缺口或不适配时才推荐新产品。所有可视化具体产品图必须核实为准确产品/版本，无法核实时使用文字卡而非伪造包装图。

## GitHub Flat Release

此仓库发布版采用扁平目录，以便手机浏览器直接上传并兼容更多 AI 平台。

### 主要入口
- `SKILL.md` — 核心行为与安全规则
- `SYSTEM_PROMPT.txt` — 不支持 Skill 标准的平台可直接作为系统提示词
- `VISUAL_SYSTEM.md` — 统一视觉设计系统
- `OUTPUT_SCHEMA.json` — 跨模型统一输出结构
- `TEMPLATE_SKIN_REPORT.md` — 皮肤评估模板
- `TEMPLATE_PRODUCT_FIT.md` — 单品适配模板
- `TEMPLATE_SKINCARE_PLAN.md` — 护肤方案模板
- `CN_SKINCARE_BRAND_HINTS.md` — 中国大陆护肤品牌检索提示池
- `LICENSE-NONCOMMERCIAL.txt` — 非商业许可

作者：Shane Chen
