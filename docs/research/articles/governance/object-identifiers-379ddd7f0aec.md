<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/object-identifiers -->
<!-- 研读状态：已完成 -->

# 函数 • Functions on objects • Object标识符 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/object-identifiers)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/object-identifiers)
- 页面语言：中文（官方 AIP 机器翻译，需与英文原文交叉核对）
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:26Z
- 产品状态：本页描述 TypeScript v1 对象标识；RID 对尚未持久化的新建对象可能为空，TSv1 应用对象类型 ID 与主键共同识别对象。

## 英文原文短摘录（每个来源不超过 25 词）

> “This page covers TSv1, which identifies objects with typeId and primaryKey.”

## 摘录译文

本页介绍 TSv1；该版本通过 typeId 和 primaryKey 标识对象。

## 中文要点

- 对象有 RID、主键和对象类型标识等表示方式。已索引或经 Action 创建的对象可有 RID；函数中新建但尚未持久化的对象 RID 为 undefined。
- 主键由唯一属性及其值组成，但只在对象类型范围内唯一，因此稳定身份应使用 typeId 与 primaryKey 的组合。
- 两次加载同一对象可能产生不同 JavaScript 实例；不能依赖 `==`、`===` 或未定义 RID 判断对象相等。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| RID | 资源标识符 | 已创建 Ontology 对象的资源身份标识 |
| primary key | 主键 | 对象类型内唯一的属性 ID/值组合 |
| object specifier | 对象标识说明符 | TSv1 中由 typeId 与 primaryKey 组成的身份描述 |

## 疑问与待验证项

- 此页明确限定 TSv1；TSv2 的 `Identify objects` 字段映射需单独核对，不能把旧 API 字段名称直接视为跨版本契约。
- 主键属性变更、复合主键规范化及跨来源系统重复主键的冲突处理不在本页覆盖范围。

## 复刻启示

- 数据库唯一约束至少采用 `(project_id, ontology_id, object_type_id, primary_key)` 复合键；外部源 RID 另存为带命名空间的别名。
- 前端对象引用与计算路径统一传输规范身份，不依赖对象快照的内存引用相等；新对象提交前也必须有稳定临时身份。
- 同一业务主键来自多个连接器时显式建模身份映射/合并规则，避免将来源 RID 当成全局主键。
