<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/version-range-dependencies-for-functions -->
<!-- 研读状态：已完成 -->

# Functions • Function consumption • Version range dependencies • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/version-range-dependencies-for-functions)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:42Z
- 产品状态：页面当前未标注特定 Beta/预览/弃用状态；关联功能状态按引用子页复核。

## 英文原文短摘录（每个来源不超过 25 词）

> “A version range enables automatic runtime upgrades, which can reduce development work and allow deployed functions to upgrade without downtime.”

## 摘录译文

版本范围支持自动运行时升级，可减少维护工作，并允许已部署函数无停机升级。

## 中文要点

- Workshop、Actions 和 Automate 可依赖固定函数版本，也可依赖版本范围；范围按 SemVer/NPM 兼容规则表达，当前只允许包含向后兼容的小版本或补丁升级。
- 非部署函数的具体版本会在运行时最终解析为满足范围的最高版本，新的发布可能延迟几分钟生效；部署函数则使用当前部署版本，若该版本不满足范围会报错。
- 自动升级有风险：即使遵循 SemVer，非主版本也可能意外破坏兼容性。消费者对稳定性要求严格时应固定版本；发布者可把稳定标签限制在受保护分支并要求代码评审。
- Function-backed Action 的范围升级还涉及权限和来源归属；自动升级后的函数不能只按接口兼容性判断安全。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| version range | 版本范围 | 满足一组版本约束的依赖选择规则。 |
| pinned version | 固定版本 | 消费者显式指定不自动变化的函数版本。 |
| semantic versioning (SemVer) | 语义化版本 | 用主/次/补丁版本表达兼容性意图的规范。 |
| eventual resolution | 最终解析 | 发布后经过传播时间再选择最新满足版本。 |

## 疑问与待验证项

- 平台称范围依赖自动选择兼容版本，但 SemVer 兼容性依赖发布者正确标注；是否有回滚和版本冻结能力要结合宿主配置验证。
- 部署执行使用当前部署版本而非一般运行时解析结果，是版本范围行为的重要例外。

## 复刻启示

- 依赖字段需要支持固定版本与版本范围，并显示当前解析版本、更新候选、影响范围、权限变化和回滚点。
- 对生产本体 Action 与 Agent 写工具默认锁定已评审版本；允许自动升级时采用兼容检查、灰度试算和告警。
