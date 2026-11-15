<!-- 页面 URL：https://www.palantir.com/docs/foundry/object-permissioning/multi-datasource-objects -->
<!-- 研读状态：已完成 -->

# Object permissioning • Multi-datasource object types (MDOs) • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/object-permissioning/multi-datasource-objects)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/object-permissioning/multi-datasource-objects)（配对状态：matched）
- 页面语言：英文
- 主题栏目：object-permissioning
- 相关性：direct；本体对象权限文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:28Z
- 产品状态：MDO 只适用于 Object Storage v2；目前可用 Foundry datasets 或 restricted views，支持 column-wise，不支持 row-wise 或 streaming 来源。

## 英文原文短摘录（每个来源不超过 25 词）

> “Foundry only supports column-wise MDOs and does not support row-wise MDOs.”

## 摘录译文

Foundry 仅支持按列组合的 MDO，不支持按行组合的 MDO。

## 中文要点

- Column-wise MDO 将同一对象的不同属性列映射到多个来源数据集，适用于列级访问控制；primary key 必须在每个来源中存在。
- 每个非主键属性只允许来自一个输入数据源，不支持重叠属性多来源解析；row-wise union 场景需评估 restricted view 等替代方式。
- 数据源权限不足或主键不匹配时，该来源映射出的属性显示为 null；对象类型 schema 仍可能可见，定义访问与数据访问分离。
- 支持用户编辑和 materialization；对象类型最多 70 个计入 Object Storage 的来源，不含 media/time-series sync。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| multi-datasource object type | 多数据源对象类型 | 将多个数据源的字段映射到单一对象类型。 |
| column-wise MDO | 按列组合 MDO | 不同来源补充同一对象的不同属性。 |
| row-wise MDO | 按行组合 MDO | 多来源提供完整同 schema 对象行；当前此模式不开放。 |
| primary key mapping | 主键映射 | 多数据源依据共同实体主键合并属性。 |

## 疑问与待验证项

- - 当前 MDO 能力与 Object Storage v2 绑定且不支持 streams；多来源系统不是任意 connector federation，需要先确认数据落地和索引策略。
- - 属性缺失/权限不足都会显示 null，查询方需要能区分“无数据”“无匹配行”和“无权限”。

## 复刻启示

- - 系统连接器应先将外部来源落成稳定 dataset/restricted view，再以统一业务主键映射到对象；在模型卡片标明来源和字段映射。
- - 画布应表达一个对象类型可由多数据集供给不同列的 data-lineage edge，并显示当前限制、主键和缺失原因。
