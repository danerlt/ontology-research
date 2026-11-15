<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontology-sdk/typescript-osdk-migration -->
<!-- 研读状态：已完成 -->

# OSDK • TypeScript OSDK 迁移指南（1.x 到 2.0） • Palantir

- 英文来源：[现行英文原文](https://www.palantir.com/docs/foundry/ontology-sdk/typescript-osdk-migration)
- 官方中文来源：[官方中文页（AIP 机器翻译）](https://www.palantir.com/docs/zh/foundry/ontology-sdk/typescript-osdk-migration)
- 页面语言：中文（官方机器翻译，准确性未验证）
- 主题栏目：ontology-sdk
- 相关性：direct；TypeScript OSDK 主要版本升级与 API 迁移
- 官方更新时间：2026-11-12T17:46:46.932Z
- 目录核对时间：2026-11-14T15:01:03Z
- 产品状态：新应用默认使用 2.0 generator；1.x 支持承诺按 2.0 发布日起至少一年计算

## 英文原文短摘录（不超过 25 词）

> “Palantir will maintain support for the TypeScript version 1.x of OSDK for at least one year after the release of TypeScript OSDK 2.0.”

## 摘录译文

TypeScript OSDK 2.0 发布后，Palantir 将至少一年继续支持 1.x 版本。

## 中文要点

- 2.0 引入新的客户端/生成代码分离方式以便独立更新依赖，并提升大型本体下的生成迭代；接口和媒体集等新能力要求 TypeScript OSDK 2.0。
- 迁移通过 Developer Console 的 SDK versions 生成新 2.0 版本，再更新依赖和应用代码；新建应用默认使用 2.0 generator。
- 结果类型从 1.x 生成的类型改为 `Osdk.Instance<Type>`；对象 RID 默认不再返回，需显式传 `$includeRid: true`。
- 对象访问改为 `client(Type).fetchOne/fetchPage/asyncIter`，链接通过 `$link`；过滤器改为对象 DSL，`orderBy` 放入 `fetchPage` 参数；Action 校验/编辑返回值及批量调用 API 也有变化。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| generated SDK | 生成式 SDK | 依照应用所选本体资源生成的类型化客户端包 |
| `Osdk.Instance<Type>` | OSDK 对象实例类型 | 2.0 对象读取结果的类型表达 |
| `$includeRid` | RID 显式投影选项 | 控制读取结果是否附带对象 RID |
| `$link` | 链接访问器 | 通过对象实例访问其本体关系 |

## 疑问与待验证项

- “至少一年”是相对 2.0 发布日的支持承诺；本文未在摘录处给出发布日期，应通过正式发布信息判断当前支持窗口。
- 不同 1.x 项目所用生成器和 API 可能不同，迁移前需盘点筛选、分页、链接、Action 响应和 RID 依赖。
- 2.0 的 Action/查询细节分布在同指南后续章节和 API 文档中，不能仅按对象读取示例完成迁移。

## 复刻启示

- 生成 SDK 应带 schema 版本和生成器版本，升级先生成差异报告，按对象、链接、查询、Action 分类迁移。
- 资源投影采用显式字段策略：默认不返回标识或敏感字段，需要时由调用方声明并经权限过滤。
- 主要版本支持期限与弃用窗口应显示为有日期来源的策略数据，不硬编码为永久规则。