<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-object-sets/load-object-set -->
<!-- 研读状态：已完成 -->

# Load Object Set • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-object-sets/load-object-set)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:57:19Z
- 产品状态：常规 v2 查询接口；OTDP、分支与事务选项有实验性限制。

## 英文原文短摘录（每个来源不超过 25 词）

> “Load the ontology objects present in the `ObjectSet` from the provided object set definition.”

## 摘录译文

依据给定的 Object Set 定义，加载集合中的 Ontology 对象。

## 中文要点

- POST `/api/v2/ontologies/{ontology}/objectSets/loadObjects` 根据 Object Set 表达式读取对象；可指定属性投影、排序、分页、情景、分支与事务上下文。
- 对象存储 v1 最多返回 10,000 条，v2 无此上限；null 属性不返回，Vector 属性须显式加入 `select`。`pageSize` 是上限，因内部内存限制实际页可能更小，不能据此认为已到末页。
- `executeInMemoryOnly=true` 会在无法以内存计算时快速失败。OTDP 默认启用，但仅在没有显式属性选择时生效，且该功能实验性、尚未普遍开放。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| ObjectSet | 对象集合 | 作为输入的集合表达式。 |
| pageSize | 页大小上限 | 返回页最大条数，内存限制可使实际数量更少。 |
| executeInMemoryOnly | 仅内存执行 | 无法以内存计算时直接失败。 |
| Vector property | 向量属性 | 需显式选择后才会返回的属性。 |

## 疑问与待验证项

- 页面未说明集合结果是否默认稳定排序；依赖顺序的消费方应明确提供排序条件。
- OTDP 生成属性与集合计算的成本、缓存及跨对象权限传播要另行确认。
- 内部内存限制造成短页时，客户端必须依 nextPageToken 判断是否还有后续页。

## 复刻启示

- 以结构化 Object Set 表达式支持画布框选、过滤、关系扩展和批量操作，并将表达式保存为可审计查询。
- 读取预览显示分页令牌、数据源上限、实际精度/成本与短页原因。
- 将派生属性作为集合读取可选投影，在试算面板记录每跳依赖、来源对象和权限决策。
