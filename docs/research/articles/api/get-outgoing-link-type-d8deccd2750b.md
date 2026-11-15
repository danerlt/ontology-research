<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources/object-types/get-outgoing-link-type -->
<!-- 研读状态：已完成 -->

# Get Outgoing Link Type (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources/object-types/get-outgoing-link-type)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontology-resources/object-types
- 相关性：direct；Ontology API v1 端点参考；保留作兼容性对照，并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:07Z
- 产品状态：正式 API（v1/v2 页面均未标注 Preview）

## 英文原文短摘录（每个来源不超过 25 词）

> “Get an outgoing link for an object type.”

## 摘录译文

获取某个对象类型的一条出向链接定义。

## 中文要点

- 接口以 ontology、源对象类型和 link API 名称定位一条出向链接，返回 link type side 元数据。
- 响应包含 API 名称、展示名称、发布状态、目标对象类型、基数（ONE/MANY）、可选外键属性和 RID；v2 还允许用 branch 读取分支中的链接定义。
- v1 路径以 ontology RID 定位；v2 路径接受 ontology API 名称或 RID。两版均要求读取权限范围 `api:ontologies-read`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Outgoing link | 出向链接 | 从当前对象类型指向关联对象类型的关系定义 |
| Cardinality | 基数 | 关系另一端是单个还是多个对象 |
| Foreign key property | 外键属性 | 链接底层可能使用的对象属性 |

## 疑问与待验证项

- 返回的 `objectTypeApiName` 是目标类型还是本侧类型应按 LinkTypeSide 结构语义与实际示例再核验，建边时不可只凭字段名猜测。
- 双向关系如何表达、反向边是否另有独立定义，需要结合本体用户文档验证。

## 复刻启示

- 画布边应以关系 RID/API 名称作为身份，端点绑定源/目标对象类型，并用基数、外键属性及状态驱动边标签与检查器。
- v1/v2 路由和分支读取差异应留在 API 适配层；关系定义读取与对象实例的关联结果查询分开建模。
