<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/resource-imports-sidebar -->
<!-- 研读状态：已完成 -->

# 函数 • 将资源导入代码库 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/resource-imports-sidebar)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/resource-imports-sidebar)
- 页面语言：中文（官方 AIP 机器翻译，需与英文原文交叉核对）
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:40Z
- 产品状态：该中文路由介绍 TypeScript v1 仓库的 Resource Imports 侧栏；它可管理本体类型、语言模型、部署和外部 source，但所有仓库导入资源须归属于同一 Ontology。

## 英文原文短摘录（每个来源不超过 25 词）

> “The following documentation is specific to TypeScript v1 functions.”

## 摘录译文

以下文档专门介绍 TypeScript v1 函数。

## 中文要点

- Resource Imports 在一个侧栏内集中添加、移除、查看对象/链接/接口、语言模型、实时部署和 REST source 等资源。
- TSv1 现代模板把导入状态保存为代码仓库中的 `resources.json`；确认变更后 Code Assist 重启并重新生成对应代码包。
- 每项资源都要有可用于代码的 API name；链接依赖会随资源列出，某些依赖值类型冲突会导致编译错误。
- 该仓库所有导入资源必须属于同一个 Ontology；切换 Ontology 会覆盖来自其他本体的现有导入。文档建议更强能力走 TSv2。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Resource Imports sidebar | 资源导入侧栏 | 维护仓库外部 Foundry 资源引用的界面 |
| `resources.json` | 资源清单 | TSv1 仓库中记录导入状态的受版本控制文件 |
| API name | API 名称 | Functions 代码访问资源所需的稳定标识 |
| value type dependency | 值类型依赖 | 资源 schema 依赖的本体值类型版本 |

## 疑问与待验证项

- 此页仅对应 TSv1；TSv2/Ontology SDK 的资源请求与生成机制不同，不能把 `resources.json` 当成统一的本体依赖契约。
- 一个仓库一次只关联一个 Ontology，切换本体可能重置导入；多个跨域本体依赖需拆分项目或改用受支持的共享模式。
- 相同 Value Type 的不同版本不能并存，依赖冲突可能让编译失败；更新共享 schema 前需要评估下游仓库。

## 复刻启示

- 将资源导入保存为版本化 manifest，显式记录本体 ID/版本、对象/链接/API 名、值类型依赖及数据源授权。
- schema 更新生成依赖差异和受影响函数清单，经评审再刷新生成客户端；针对一套仓库跨多系统需求，采用多连接器目录和明确 ontology scope。
- 借鉴侧栏的类型过滤、搜索、预览和依赖展开，让工程师能看见某个函数依赖了哪些业务资源。
