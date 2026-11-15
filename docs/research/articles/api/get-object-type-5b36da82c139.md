<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/object-types/get-object-type -->
<!-- 研读状态：已完成 -->

# Get Object Type (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/object-types/get-object-type)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/object-types
- 相关性：direct；对象类型与本体建模文档
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:53:52Z
- 产品状态：按当前 API 参考整理；列表一致性、分支和部分媒体能力有明确限制。

## 英文原文短摘录（每个来源不超过 25 词）

> “Gets a specific object type with the given API name.”

## 摘录译文

按 API 名称读取指定对象类型。

## 中文要点

- GET `/api/v2/ontologies/{ontology}/objectTypes/{objectType}` 返回对象类型定义。响应含 camelCase API 名称、显示/复数名称、状态、主键、属性 map、RID、标题属性、可见性和同义词别名。
- 状态枚举为 ACTIVE、ENDORSED、EXPERIMENTAL、DEPRECATED；可选 includeDatasources=true 才返回当前用户有权查看的数据来源，默认 false。
- datasources 为空也可能表示当前用户无权查看来源；aliases 仅在 get-by-RID 读取路径填充，List Object Types 总为空。
- 可选 branch 读取分支定义，分支为实验能力且支持范围有限；OAuth scope 为 `api:ontologies-read`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| apiName | API 名称 | 对象类型的 camelCase 稳定接口名。 |
| titleProperty | 标题属性 | 实例列表/节点显示标题使用的属性。 |
| datasources | 数据来源 | 当前调用用户有权查看的支撑来源列表。 |

## 疑问与待验证项

- aliases 在部分读取路径填充不一致，搜索需依赖适当的 get-by-RID 或单独索引。
- 来源列表为空不能证明对象类型没有底层来源，权限可能过滤了该信息。

## 复刻启示

- 对象类型检查器同时展示 RID/API 名称、主键、标题字段、属性、生命周期状态、可见性和可见来源。
- 多项目系统复用 schema 模型，但每条连接与每个源列表必须做项目和用户权限过滤。
