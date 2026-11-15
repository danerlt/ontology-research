<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/language-feature-support -->
<!-- 研读状态：已完成 -->

# Functions • Feature support by language • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/language-feature-support)
- 官方中文来源：尚未确认（配对状态：needs_review）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:24Z
- 产品状态：Staged writes 为 Beta；具体能力可因租户配置而异。

## 英文原文短摘录（每个来源不超过 25 词）

> Not all features are supported by all languages.

## 摘录译文

并非所有语言都支持全部功能。

## 中文要点

- 能力表按 AIP Logic、TSv1、TSv2、Python 横向比较：对象访问与本体编辑各列均支持；Ontology interfaces 仅 TSv2 支持。
- 媒体支持有明显差异：TSv1 有较完整操作；TSv2/Python 仅部分支持上传和媒体属性基础操作，不含文档专用或音频专用处理。语言模型代理调用仅列为 TSv2/Python 支持；Python 还可用于 Pipeline Builder。
- 文档推荐 TSv2 或 Python 来获得 OSDK；TSv2 提供完整 Node.js 运行环境、较强资源配置选项和 Beta staged writes。函数执行方式亦影响版本并行、成本计费和运维负担。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Feature support matrix | 功能支持矩阵 | 用具体运行语言作为能力边界，而非假定代码移植即功能等价。 |
| Ontology interface | 本体接口 | 可复用的对象/链接抽象；本页仅 TSv2 支持访问和编辑。 |
| Staged writes | 暂存写入 | TSv2/Python 的 Beta 编辑执行模型，支持函数内读后写并可嵌套调用。 |

## 疑问与待验证项

- 矩阵是随平台更新的能力说明，目标租户是否启用了 AIP、staged writes 或特定执行模式仍需查询环境配置。
- 表中 “Partial” 的细粒度边界应以媒体专页和具体 SDK 版本为准；不能把此矩阵固化成永不变化的校验规则。

## 复刻启示

- 在函数/规则配置中记录语言运行时、API 能力和状态标签，并按能力矩阵进行静态校验，明确指向支持该功能的运行时。
- 将能力可用性建模为可版本化的产品元数据，保留租户 feature flag 覆盖；用 UI 提示差异而不是隐藏能力。
