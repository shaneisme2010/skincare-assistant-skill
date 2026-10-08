护肤报告与方案图片｜聊天加载包
聊天包 skincare-chat-starter 0.1.0-rc.1（公开测试版，2026-10-08）。护肤内容基线为公开包 skincare-chat-images 0.6.0-rc.20。
作者：Shane Chen。沿用原非商业许可；请保留同包 LICENSE-NONCOMMERCIAL.txt 和免责声明。

最快开始
1. 在 iPhone 用 Safari 下载本 ZIP，打开“文件”App，在“下载项”中点一下 ZIP 解压。
2. 打开 ChatGPT 新聊天，通过“＋”添加文件，只上传：开始使用.txt 和 style-reference-neutral.png。README 和许可证不用上传。
3. 发送：请完整读取开始使用.txt并查看参考图，按文件流程开始护肤评估：先检查聊天包更新，再发完整六组问卷；无法读取、联网或生图时请直说。
4. 回答六组问卷。照片可选；无照片仅按本人自述，不冒称看过照片。资料给齐后回复“已完成”。
5. 可用能力和资料齐备时，应继续核验来源、提供完整用法和医学链接，分别生成、打开检查并交付皮肤报告图和护肤方案图。某一步失败不代表整项已完成。

重要边界
这是当前聊天读取使用的资料包；下载、解压或上传不会安装 Skill、创建插件、提升账户权限或自动建立提醒。新聊天需重新提供两个文件。
本文件保留完整核心规则；只将分散的引用改为同一文本章节，将安装相关操作改成当前聊天可执行的文件读取，并增加照片可选但不得编造观察的真实自述分支。真实自述无照片与明确虚构测试分开处理。
免费版具有文件、图片、联网和生图能力，但受当时账户、地区、设置、客户端及独立额度约束。官方当前说明 Free 每天限 3 次文件上传，失败尝试有时也计数；已上传这两个文件后，是否还能添加照片以当前账户显示为准。生图额度独立，不能保证当天连续完成双图及修改。
不要依赖聊天自动解压 ZIP；先在 iPhone 解压，再上传 TXT 与 PNG。不要只上传原版 SKILL.md，也不要只让聊天读下载链接。
每次新启动护肤流程或明确说“检查更新”时，助手实际联网检查独立聊天包通道；同一流程的连续问卷回答和普通追问不逐句查，不依赖跨聊天时间记录，不创建定时任务。有已核验新版时提供 ZIP 直链、解压上传两文件步骤和启动提示词，由用户自己下载；助手不代下载、不自动覆盖。查不到或核验失败时如实说明，可继续现有文件。需要护肤提醒时，仍以实际提醒工具创建成功为准。
本包提供一般护肤信息，不构成医学诊断、处方或医疗服务。出现急症或需要医疗评估的症状时优先寻求合适医疗帮助。AI观察、研究解释和图片可能出错。请勿向公开仓库或问题反馈贴上传面部照片、健康资料、个人产品清单或完整私密聊天。

验证范围
本聊天包做了文件完整性、问卷与核心规则保留、相对路径替换、独立静态审阅，以及版本筛选逻辑的公开联网数据和合成 fixture 验证；没有在普通手机 ChatGPT／Free 新会话中做实际问卷到双图测试，不应称聊天版已跑通或四例通过。原发布版的历史测试结论不能直接算作本聊天版验收。
PNG 与公开 rc.20 包中的中性图逐字节相同；它是通用风格示例，不含真人或具体商品事实，不规定产品数量或晚间分支数量。
原版 agents/openai.yaml 仅供原生安装平台显示和调用，当前聊天不需要，未作为运行依赖；所有护肤核心流程与参考文本均已并入开始使用.txt；版本检查改为本聊天包独立通道的新启动检查，原生 Skill 的每周检查配置不再作为聊天包规则。

当前聊天包
发布通道：skincare-chat-starter-v
发布页：https://github.com/shaneisme2010/skincare-assistant-skill/releases/tag/skincare-chat-starter-v0.1.0-rc.1
本版ZIP：https://github.com/shaneisme2010/skincare-assistant-skill/releases/download/skincare-chat-starter-v0.1.0-rc.1/skincare-chat-starter-0.1.0-rc.1.zip
版本manifest：同一发布tag下的 chat-starter/manifest.json。只读公开元数据，不下载ZIP；外部manifest记录冻结ZIP校验值，避免ZIP内自引用。

原版护肤内容公开来源
发布说明：https://github.com/shaneisme2010/skincare-assistant-skill/blob/skincare-chat-images-v0.6.0-rc.20/SKINCARE_CHAT_IMAGES.md
发布页：https://github.com/shaneisme2010/skincare-assistant-skill/releases/tag/skincare-chat-images-v0.6.0-rc.20
原始附件：https://github.com/shaneisme2010/skincare-assistant-skill/releases/download/skincare-chat-images-v0.6.0-rc.20/skincare-chat-images-0.6.0-rc.20.zip
原始ZIP SHA256：639bb106520d158c80a7bde2d9144f6852447d3f2d3813cfec255f888ce1c42a
本包使用独立聊天包名称、版本、tag及manifest，不是原生Skill通道的新版本。发布链接需以GitHub实际可见结果为准；文件中出现链接不代表已完成远端发布。

官方使用说明（核验于2026-10-08；额度与界面以后可能变化）
ChatGPT文件上传：https://help.openai.com/en/articles/8555545-uploading-files-and-audio-to-chatgpt
免费版能力与独立额度：https://help.openai.com/en/articles/9275245-chatgpt-free-tier-faq
图片输入：https://help.openai.com/en/articles/8400551-chatgpt-image-inputs-faq
ChatGPT生图：https://help.openai.com/en/articles/11084440-images-in-chatgpt
iPhone下载位置：https://support.apple.com/zh-cn/102440
iPhone打开ZIP：https://support.apple.com/zh-cn/102532
