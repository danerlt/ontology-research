<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/object-permissioning/multi-datasource-objects -->
<!-- 研读状态：已完成 -->

# 对象权限管理 • 多数据源Object类型（MDOs） • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/object-permissioning/multi-datasource-objects)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/object-permissioning/multi-datasource-objects)
- 页面语言：中文
- 主题栏目：object-permissioning
- 相关性：direct；本体对象权限文档
- 官方更新时间：2026-11-12T17:46:46.936Z
- 目录核对时间：2026-11-14T15:00:01Z
- 产品状态：中文页面标注为机器翻译且准确性未验证；英文页进一步注明 MDO 只支持 Object Storage v2 的 column-wise 方案。

## 英文原文短摘录（每个来源不超过 25 词）

> “A multi-datasource object type (MDO) is backed by multiple datasources in the Ontology and is only available in Object Storage v2.”

## 摘录译文

多数据源对象类型（MDO）由 Ontology 中的多个数据源共同支持，且仅适用于 Object Storage v2。

## 中文要点

- 中文页说明 MDO 将多个数据源的列映射到同一 Object 类型，适合单一业务实体分字段治理；只支持 Foundry 数据集或受限视图。
- 每个非主键属性只能由一个输入源提供，主键必须出现在所有输入源中；权限不足或主键不匹配时相应属性显示为 null。
- 英文现行页面补充说明目前不支持 row-wise MDO、streaming source，并注明支持用户编辑/物化及最多 70 个计入对象存储的数据源。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| multi-datasource object type | 多数据源对象类型 | 多个来源数据集向一个对象类型提供字段。 |
| restricted view | 受限视图 | 在来源数据集层执行行级访问控制。 |
| object/property security policy | 对象/属性安全策略 | 在本体类型层执行行级、列级权限检查。 |

## 疑问与待验证项

- 中文页标注机器翻译且没有列出全部英文限制；以英文现行文档核对 Object Storage v2、行式/流式支持限制。
- 多来源字段缺失和权限失败都会显示 null，调用者仍需从访问诊断区分原因。

## 复刻启示

- 多系统映射应以共同业务主键汇聚到一个对象；每个属性保留 datasource lineage、映射规则和缺失状态。
- 画布同时呈现对象类型关系图和对象属性来源图，避免把来源系统错误建为重复业务类型。
