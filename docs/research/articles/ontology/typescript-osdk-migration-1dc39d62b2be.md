<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology-sdk/typescript-osdk-migration -->
<!-- 研读状态：已完成 -->

# Ontology SDK • TypeScript • TypeScript OSDK migration guide • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-sdk/typescript-osdk-migration)
- 官方中文来源：[官方中文页面（AIP 机器翻译）](https://www.palantir.com/docs/zh/foundry/ontology-sdk/typescript-osdk-migration)（目录配对状态：matched）
- 页面语言：英文
- 主题栏目：ontology-sdk
- 相关性：direct；TypeScript OSDK 1.x 到 2.0 迁移
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:41Z
- 产品状态：新应用使用 2.0 generator；1.x 的维护窗口按 2.0 发布日起至少一年计算

## 英文原文短摘录（不超过 25 词）

> “In TypeScript OSDK 2.0, object RIDs are not included by default when fetching objects.”

## 摘录译文

TypeScript OSDK 2.0 获取对象时默认不包含对象 RID。

## 中文要点

- TypeScript OSDK 2.0 将 SDK client 与生成代码分离，减少依赖升级必须重新生成 SDK 的耦合；接口、Media Set 等新能力需要 2.0。
- 从 Developer Console SDK versions 使用 2.0 generator 生成新版本，并更新项目依赖、对象/查询调用和 Action 调用；新应用默认生成 2.0。
- 对象实例类型改为 `Osdk.Instance<Type>`；RID 不再默认返回，只有通过 `$includeRid: true` 请求并按返回类型声明时才可访问。
- 对象加载从旧的深层属性 API 改为 `client(Type).fetchOne/fetchPage/asyncIter`；链接用 `$link`，过滤用对象 DSL，排序参数移动到 `fetchPage`。
- Action 校验/编辑响应与批量执行方法变化；旧版 1.x 仍有至少一年支持期，但该承诺与 2.0 发布日期相关。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| client/code separation | 客户端与生成代码分离 | 2.0 支持独立更新通用运行时和应用 SDK |
| `Osdk.Instance<Type>` | OSDK 对象实例类型 | 2.0 的类型化本体对象返回值 |
| `$includeRid` | RID 显式投影参数 | 在 fetch 请求中选择是否返回 RID |
| SDK generator | SDK 生成器 | Developer Console 生成应用专属 SDK 的版本化工具 |

## 疑问与待验证项

- 支持期限是相对承诺且文档不在此处给出 OSDK 2.0 的发布日期；当前支持窗口需结合发布记录。
- 迁移指南涉及多个 API 类别，生产升级仍应逐项核对聚合、链接基数、Action 返回值和错误处理。
- RID 默认省略会影响依赖全局资源标识的代码；调用方应检查是否真的需要该字段。

## 复刻启示

- SDK 主版本升级以生成器和客户端运行时为两个显式依赖，生成迁移报告并呈现 schema/调用层的兼容差异。
- 对象读取采用字段投影原则，资源 RID 等内部元数据默认不下发，需要显式选择且经过授权。
- 迁移工作台提供按对象、链接、查询和 Action 分类的检查项，并保留源 SDK 版本用于回滚。