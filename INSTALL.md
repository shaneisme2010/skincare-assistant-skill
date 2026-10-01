# 使用入口

v2.8.1 Draft 8 为预发布测试版。上传 `SKINCARE_ASSISTANT_CHATGPT.md`，发送“请加载我上传的「护肤助理」Skill，并直接开始。”

发布后可以把上传文件换成完整单文件的公开链接。所有流程、视觉与安全要求均内置，用户无需重复它们。链接加载表示在当前聊天读取并执行，不保证永久安装或跨聊天存储。

完整包中的 `SKILL.md` 与 `references/` 适合支持技能文件按需读取的环境。单文件已内嵌全部运行章节，没有需要另外寻找的规则文件；它仍会整体占用相应上下文，不能宣称自动节省到只加载某一节。

固定版本入口：
- [Draft 8 发布页](https://github.com/shaneisme2010/skincare-assistant-skill/releases/tag/v2.8.1-draft8)
- [Draft 8 单文件](https://raw.githubusercontent.com/shaneisme2010/skincare-assistant-skill/v2.8.1-draft8/SKINCARE_ASSISTANT_CHATGPT.md)

链接只有在该版本实际发布后可用。不要使用仓库的`latest`或`main`链接代替此固定测试版本，它们可能指向其他版本。

链接加载提示词：“请读取 https://raw.githubusercontent.com/shaneisme2010/skincare-assistant-skill/v2.8.1-draft8/SKINCARE_ASSISTANT_CHATGPT.md ，加载护肤助理并直接开始。”若当前ChatGPT无法读取链接，下载并上传同一单文件即可。

使用中距上次版本检查满一周时，会检查公开发布来源；有新版才提示，由用户决定是否加载。也可随时发送“检查更新”查询，或发送“更新护肤助理”手动检查并加载新版，不受一周间隔限制。草稿未发布或来源不可用时会如实说明，保留当前版本。

同意长期记录后，优先用实际可读写的私有Page维护档案；仅有文件能力时保存修订快照，无持久化能力时提供下载备份。新聊天可说“继续我的护肤档案”；不能自动访问时，只需添加原档案链接或最新文件。档案恢复、关键节点保存和上传新照片后的局部对比均已内置，无需额外提示词；是否可跨聊天自动读取，须以目标环境工具和实际测试为准。
