---
name: luxreal-brand-design
description: 为 LuxReal 制作和精修品牌社媒海报、功能上新视觉、活动物料及版式方案，并检查品牌一致性。用户提及 LuxReal 品牌规范、海报设计、视觉探索、成品精修，或在 LuxReal 项目中要求将品牌规则映射到视觉组件时使用。
---

# LuxReal 品牌视觉设计

将品牌规则、事实与素材转换为可交付的视觉作品。按任务范围选择制作、精修、审查或规则映射；仅修改规范时只更新文档。

## 读取与资源定位

以本 SKILL.md 所在目录为资源根目录，不依赖调用者工作目录或原项目路径。

当前基线为 `LuxReal_Brand_System.md` v0.4（2026-11-19）。按下述拆分引用执行；社媒标题创作自由与五类 Tag 配色覆盖旧版统一字体、统一标签底色限制。

- 每次视觉任务先读取 [品牌规则](references/brand-rules.md)，了解来源状态、Logo、色彩、字体、网格及栏目限制。
- 新构图、方案比较或精修时读取 [视觉理念与执行流程](references/design-workflow.md)，按内容选用 Cinematic、Studio、Editorial、Gallery 或 Metric。
- 制作和审查最终输出时读取 [验收标准](references/acceptance.md)。
- 选择 Logo 时读取 [Logo 清单](references/logo-manifest.json)，从 `assets/logos/` 引用原始文件。path 相对本 Skill 根目录；sourcePath 仅记录历史来源。
- 代码化颜色、字重、网格或模板时，分别读取 [Design Tokens](references/design-tokens.json) 与 [模板插槽](references/template-slots.json)。保留字段、ID、来源与状态；这些是项目自定义 JSON。
- 查询缺失资源、指纹或来源时读取 [资源状态](references/resource-status.json)；核对 VIS 图示时查看 [原始 VIS](references/vis-manual.pdf)，使用物理页码。

只加载当前任务需要的引用。

## 执行任务

1. 提取传播目标、受众、栏目、尺寸、正式文案与可用素材，区分事实、创作线索和缺项。保留本次修改范围及应保留内容。
2. 区分概念探索和受控生产。遵循“用户明确确认的品牌规则与本次明确变更 → VIS → 已批准项目约束 → 设计提案 → 推断线索”的优先级，沿用已有授权推进常规细化。
3. 制作新视觉前，提炼“原始线索 → 抽象关系 → 可见决策”；命名方向，按视觉流程撰写 4–6 段设计理念，另存 `design-philosophy.md`。在至少三种兼容构图间内部比较，选择一种；仅在用户要求时交付多个方案或多页。
4. 先确定主视觉与负空间，再安置标题、必要条件、栏目标签和 Logo。使用可用的生成或渲染工具实际完成文件；不足时如实说明交付边界。
5. 查看实际输出的完整尺寸及缩略图，按验收标准定位问题并精修，再查看修改后的文件。优先校准裁切、间距、对比和字距；首次即通过时记录具体理由。
6. 交付实际文件、简短选型说明及影响本次交付的限制。区分草稿、概念图、未完成视觉复核与正式输出。

审查任务直接检查现有作品，给出可定位问题；仅在用户要求时改文件。窄范围文字或规则修改不自动触发海报制作及多方案交付。

## 保持品牌与事实准确

- 品牌名写作 LuxReal；用官方图片呈现 Logo，不重新输入字标、重绘、变形、旋转、重着色或加特效。
- 浅底默认 `logo-standard-horizontal`，深底默认 `logo-standard-horizontal-inverse`。竖版、单色和玻璃扩展素材按限定用途选用；未分类资源不得自动作为正式 Logo。
- 按 visibleBounds 计算 Logo 可见尺寸，以可见图形高度为 X 预留四周 1X，线上可见高度不低于 20 px；不能将源 PNG 的透明边当作已满足留白。
- 社媒主标题、封面主题字和标题数字可按主题自由选择字体、真实字重、中英混排、定制字形及文字效果，无须逐次确认；HarmonyOS Sans 是可选项。选用其他标题字体本身不构成草稿或不合规理由。更换后重新测量换行、行高与槽位，保持文字准确可读。
- 副标题、正文、规则、日期、来源与栏目标签默认使用 HarmonyOS Sans SC；默认品牌字重按品牌规则第 5 节执行，不套用于创意标题。SC／TC 字体位于 `assets/fonts/HarmonyOS_Sans_SC/` 与 `assets/fonts/HarmonyOS_Sans_TC/`，TC 用于繁体内容；核对实际文件、字重与各目录 LICENSE.txt，不无意合成粗体。
- 栏目 Tag 按 `categoryTagPolicy` 解析内容类型，同时读取 `color.categoryTags.<key>.background` 与 `foreground`，不能只改栏目文案。功能上新、优惠活动、共创计划、用户案例展示、资讯更新使用五类映射；历史“用户案例”映射到“用户案例展示”。扩展色仅用于小面积实色 Tag，不扩展为整页主色；文字对比度 ≥4.5:1。旧 `color.semantic.categoryTagBackground` 仅兼容历史标签，不作新模板默认值。
- 品牌强调色为 `#3ED2FF`，品牌蓝设计色块面积不超过 50%。保留通用深蓝、黑灰 Token 的来源冲突，不因 Tag 已分色而解除其他冲突。
- 使用 VIS 的短边 5% 边距、12 列及 margin/5 栏间距规则，采用 half-up 取整。网格边距与关键内容安全区分开管理；具体尺寸及提案参数查品牌规则。
- 仅使用有来源的功能、收益、价格、日期、权益与成绩。将生成概念图与真实截图/效果区分，不将想象的产品界面或渲染效果称为已上线能力。
- 保留 vis_explicit、user_confirmed、proposed、provisional、conflict 等来源状态。五种排版及插槽是提案，不是已经实现或发布的渲染器。
- 受控生产只检查实际引用的依赖。缺少正式字体、关键事实、可用素材、已发布模板或所需 Token 批准记录时，继续交付明确标识的草稿；不由模型自行宣布批准、授权或发布。

## 输出与对接

默认视觉交付一张指定尺寸的 sRGB PNG 或单页 PDF，加独立 `design-philosophy.md`；默认 PNG 不透明、矩形四角为 0。遵照用户指定的格式与数量。

对接内容 Agent 时沿用 category、templateId、templateStatus、variant、reason、copy、factRefs、media、missingFields、warnings、formalExportReady 等字段及实际应用协议。保留既有 category 枚举，用适配器映射栏目名称；视觉阶段可选记录 typography 配置，只有渲染器实际应用后才声称支持。结构化文案和推荐结果不等于完成绘图。正式导出资格以验证过的素材、字体、事实、模板和引用 Token 状态判定；不自行将 Draft 改为 Published。

交付前可运行 `python3 <skill-root>/scripts/verify_assets.py` 校验随包 Logo、VIS、字体和许可文件的指纹、PNG 尺寸及清单映射。该检查不验证用途许可、事实授权、可见边界测量或画面质量，不能替代实际输出复核。

维护源文档时，先运行 `python3 <skill-root>/scripts/sync_brand_system.py`，再运行同命令加 `--check` 与资源校验。脚本从相邻的 `LuxReal_Brand_System.md` 同步拆分规则与 JSON，保留 Logo 路径适配及实际资源状态；另核对本入口与仓库说明是否需要相应更新。单独安装 Skill 后没有源文档时，不运行同步脚本。
