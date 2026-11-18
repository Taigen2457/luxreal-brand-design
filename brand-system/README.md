# LuxReal Brand Design

供团队复用的 LuxReal 品牌视觉设计 Skill，适用于社媒海报、功能上新、活动物料、版式探索和成品精修。

## 获取和使用

1. 仓库所有者先在 Settings → Collaborators 中邀请需要访问的同事；同事接受邀请后即可下载或克隆此私有仓库。
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

HarmonyOS Sans SC 字体和字体许可尚未随包提供。五种版式仍为 Draft / proposed；通用深蓝和黑灰 Token 的原始冲突保留。用户确认的栏目标签底色为 #29256C，不受通用深蓝冲突影响。

本 Skill 不包含内容 Agent 服务、已完成的视觉渲染器或共享 API 凭据。正式成品还需核实本次素材、事实、字体及模板状态。

## 团队维护

更新规范和素材后重新运行资源校验，并保持引用文件与原文一致。下载副本不会自动更新；同事需要重新下载或通过 Git 拉取最新版，再更新已安装的 Skill 文件夹。品牌素材按团队内部允许的范围使用，本仓库不授予第三方素材或字体的额外许可。
