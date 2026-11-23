# LuxReal Brand Design

供团队复用的 LuxReal 品牌视觉设计 Skill。

将品牌规范、官方 Logo、视觉设计流程和验收标准整理为 AI 可读取的资源，帮助设计与运营同学制作风格一致、信息准确的品牌物料。

## 适用场景

- 社交媒体海报与封面设计
- 功能上新、优惠活动、共创计划、用户案例及资讯更新
- 多种版式探索与方案比较
- 现有物料的层级、留白、裁切和细节精修
- 品牌一致性检查
- 品牌规则向设计组件与代码参数的映射

## 文件说明

| 路径 | 内容 |
| --- | --- |
| `brand-system/LuxReal_Brand_System.md` | 完整品牌视觉与内容设计规范 |
| `brand-system/luxreal-brand-design/SKILL.md` | Skill 入口与执行指令 |
| `brand-system/luxreal-brand-design/references/` | 品牌规则、设计流程、验收标准、Tokens、模板插槽及 VIS |
| `brand-system/luxreal-brand-design/assets/logos/` | 官方 Logo 原始文件 |
| `brand-system/luxreal-brand-design/assets/fonts/` | 字体文件 |
| `brand-system/luxreal-brand-design/agents/` | Skill 展示信息与默认调用提示 |
| `brand-system/luxreal-brand-design/scripts/` | 资源完整性校验脚本 |


## 如何使用

### 1. 获取文件

本仓库为公开仓库，可以直接提供链接给能够读取 GitHub 文件的 AI：

```text
请读取 https://github.com/Taigen2457/luxreal-brand-design/blob/main/brand-system/luxreal-brand-design/SKILL.md
并按当前任务读取其中链接的品牌规则、流程与素材，为 LuxReal 制作海报。
尺寸：1080×1440；主题与正式文案：[填写]；素材：[提供]。
社媒标题可自由创作，栏目 Tag 按内容类型分色。
```

需要下载字体、Logo 或安装 Skill 时，下载或克隆完整仓库。仅提供链接不会自动安装 Skill；具体读取与制作能力取决于使用的 AI 工具。

### 2. 安装 Skill

将完整的 `brand-system/luxreal-brand-design/` 文件夹导入所使用 AI 工具的 Skill 功能，或放入该工具指定的 Skill 目录。

具体安装方式以工具提供的入口为准。安装后的 Skill 根目录应直接包含 `SKILL.md`。

请保留整个文件夹，不要只复制入口文件，否则品牌引用、Logo 和校验脚本将无法正常使用。

### 3. 提供任务材料

每次制作时，尽量提供：

- 传播目标与目标受众
- 发布渠道、画布尺寸和输出格式
- 已确认的正式文案与产品事实
- 可使用的截图、作品或其他素材
- 本次需要保留或修改的内容

### 4. 发起任务

在支持 `$skill-name` 调用语法的工具中，可以使用：

```text
请使用 $luxreal-brand-design，为 LuxReal 制作一张功能上新海报。

尺寸：1080×1440
主标题：[填写正式文案]
副标题：[填写已确认的用户收益]
素材：[提供图片或文件]
输出：PNG 和独立设计说明

请比较至少三种适合当前内容的构图，选出一种完成，
并检查标题层级、字体、网格、留白、Logo 和实际导出效果。
```

精修已有作品时：

```text
请使用 $luxreal-brand-design，精修这张海报。

保留现有主体和正式文案，重点调整裁切、间距、
文字层级与对比度，并核对品牌规范。
```

## 设计原则

- 按 v0.4（2026-11-19）规范保持 LuxReal 品牌名称、Logo 和文字角色准确。
- 使用官方 Logo 原文件，保留比例和安全留白。
- 社媒标题可自主选择字体、字重、混排、定制字形和文字效果；正文与辅助信息默认 HarmonyOS Sans SC。
- 栏目 Tag 按五类内容成对读取底色与文字色，不再统一使用一个底色。
- 以主视觉、空间关系和信息层级建立表达。
- 根据内容选择版式，避免只换背景或颜色。
- 产品能力、价格、日期、权益和成果必须有来源。
- 区分概念生成图与真实产品效果。
- 查看实际输出并精修后再交付。

## 字体与制作能力

社媒标题不限定 HarmonyOS Sans 系列，可根据主题自由创作，无须逐次请求字体确认；选用其他字体本身不影响正式输出资格。需要核对实际字体或字形资产可用、文案准确与用途许可，并重新测量换行与槽位。

正文、副标题、规则、日期、来源与 Tag 默认 HarmonyOS Sans SC。SC 和 TC 字体分别位于 `assets/fonts/HarmonyOS_Sans_SC/` 与 `assets/fonts/HarmonyOS_Sans_TC/`（相对 Skill 根目录），TC 供繁体内容使用。两个目录各保留 LICENSE.txt；文件随包提供不代表所有用途已获批准。

| 内容类型 | Tag 底色 | Tag 文字色 |
| --- | --- | --- |
| 功能上新 | `#3ED2FF` | `#29256C` |
| 优惠活动 | `#6456B8` | `#FFFFFF` |
| 共创计划 | `#29256C` | `#FFFFFF` |
| 用户案例展示 | `#DCEFF5` | `#29256C` |
| 资讯更新 | `#535455` | `#FFFFFF` |

以上扩展色仅用于小面积栏目标签，不扩展为整张海报的主色。历史“用户案例”名称兼容映射到“用户案例展示”。

本 Skill 提供品牌知识、素材与执行流程。图片生成、视觉渲染和文件导出依赖使用者自己的 AI 工具、运行环境与账号能力。

## 资源校验

在仓库根目录运行：

```bash
python3 brand-system/luxreal-brand-design/scripts/verify_assets.py
```

脚本检查随包 Logo、VIS、字体及许可文件的指纹、PNG 尺寸与清单映射。

该校验不代表字体、素材授权、产品事实或视觉质量已经通过审核。

## 当前状态

五种版式及其插槽保留为 Draft / proposed 设计提案，不代表所有模板都已实现或获准用于正式生产。

规范中已有的色值冲突与来源状态继续保留。正式输出需按本次任务实际引用的字体、素材、事实、模板及 Token 状态进行检查。

## 团队共享与更新

本仓库公开可读，可直接分享仓库链接；写入权限仍由仓库所有者管理。

修改 `brand-system/LuxReal_Brand_System.md` 后，在仓库根目录运行：

```bash
python3 brand-system/luxreal-brand-design/scripts/sync_brand_system.py
python3 brand-system/luxreal-brand-design/scripts/sync_brand_system.py --check
python3 brand-system/luxreal-brand-design/scripts/verify_assets.py
```

同步脚本重新生成拆分规则、流程、验收标准、Tokens、Logo 清单、模板插槽和资源状态；另检查 SKILL.md 与本说明中的摘要是否需要更新。脚本保留原文版本、来源与提案状态，不代表模板已实现或已发布。

品牌规范或素材更新后，使用者需要拉取或重新下载最新版，并更新已安装的 Skill。已下载的副本不会自动同步。

品牌资产、第三方素材及字体均按各自许可和团队授权范围使用。

