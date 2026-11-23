# LuxReal Brand Design

供团队复用的 LuxReal 品牌视觉设计 Skill，适用于社媒海报、功能上新、活动物料、版式探索和成品精修。

## 获取和使用

1. 仓库公开可读，可以直接分享 [仓库链接](https://github.com/Taigen2457/luxreal-brand-design)，或下载、克隆完整仓库。AI 需要支持读取 GitHub 及相对引用；提供链接本身不会自动安装 Skill。
2. 将完整的 `luxreal-brand-design/` 文件夹安装到所使用 AI 工具的 Skill 目录，或通过该工具提供的 Skill 导入入口安装。请保留 references、assets、scripts 和 agents，不要只复制 SKILL.md。具体安装入口取决于工具是否支持本目录格式。
3. 在支持本调用语法的工具中使用 `$luxreal-brand-design`，例如：“请使用 $luxreal-brand-design，根据我提供的文案和素材，制作一张 1080×1440 的 LuxReal 功能上新海报。”
4. 提供本次确认的文案、真实产品素材和输出要求。Skill 提供规则和工作流程；图片生成、渲染、文件导出依赖使用者自己的工具与账号能力。

## 包含内容

- 品牌规则、视觉理念与制作流程、五种版式提案、输出验收标准。
- Design Tokens、Logo 选用清单、模板插槽 JSON。
- 12 个原始官方 Logo PNG，以及原始 VIS 手册。
- 标准库 Python 资源校验脚本：`python3 luxreal-brand-design/scripts/verify_assets.py`。

完整品牌源文档保留在 `LuxReal_Brand_System.md`。Skill 随包引用按主题拆分，以减少每次加载的内容。

## 当前边界

当前规范为 v0.4（2026-11-19）。社媒标题允许自由选择字体、真实字重、混排及定制字形，无须逐次确认；正文与辅助信息默认 HarmonyOS Sans SC。SC／TC 字体和许可文件分别保留于 `assets/fonts/HarmonyOS_Sans_SC/` 与 `assets/fonts/HarmonyOS_Sans_TC/`，TC 供繁体内容使用。实际用途按对应许可核对。

栏目 Tag 使用五类底色／文字色：功能上新 `#3ED2FF / #29256C`、优惠活动 `#6456B8 / #FFFFFF`、共创计划 `#29256C / #FFFFFF`、用户案例展示 `#DCEFF5 / #29256C`、资讯更新 `#535455 / #FFFFFF`；扩展色只用于小面积 Tag。五种版式仍为 Draft / proposed；通用深蓝和黑灰 Token 的原始冲突保留。

本 Skill 不包含内容 Agent 服务、已完成的视觉渲染器或共享 API 凭据。正式成品还需核实本次素材、事实、字体及模板状态。

## 团队维护

更新本目录的 `LuxReal_Brand_System.md` 后，运行 `python3 luxreal-brand-design/scripts/sync_brand_system.py`，再运行同命令加 `--check` 及资源校验；另核对 Skill 入口与仓库说明的摘要。下载副本不会自动更新；同事需要重新下载或通过 Git 拉取最新版，再更新已安装的 Skill 文件夹。品牌素材按团队内部允许的范围使用，本仓库不授予第三方素材或字体的额外许可。
