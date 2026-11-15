<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-object-sets/create-temporary-object-set -->
<!-- 研读状态：已完成 -->

# Create Temporary Object Set • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-object-sets/create-temporary-object-set)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:57:17Z
- 产品状态：预览接口；必须传 `preview=true`；创建的集合一小时后过期。

## 英文原文短摘录（每个来源不超过 25 词）

> “Creates a temporary `ObjectSet` from the given definition.”

## 摘录译文

从给定定义创建临时 Object Set。

## 中文要点

- POST `/api/v2/ontologies/{ontology}/objectSets/createTemporary` 根据请求体中的 objectSet 定义创建临时集合；OAuth 同时需要本体读写 scope。
- 接口处于 Preview，调用必须带 `preview=true`，文档提示接口可能修改或移除。返回 `objectSetRid`，临时集合一小时后到期。
- 可指定分支来源，但 branch 本身为实验性功能。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| temporary ObjectSet | 临时对象集合 | 按表达式创建、存续一小时的集合资源。 |
| objectSetRid | 对象集合 RID | 临时集合的资源标识符。 |
| preview=true | 预览参数 | 调用此预览接口所必需的参数。 |

## 疑问与待验证项

- 一小时过期后再次读取的错误类型、续期方式和后台清理延迟没有在本页说明。
- Preview 端点可能变更或移除，不宜用作稳定的持久化集合存储。

## 复刻启示

- 画布中的临时筛选结果可用短生命周期集合表达式，但 UI 明示 TTL 并支持过期重建。
- 将临时集合与保存的查询/业务视图分开建模，并让预览能力受开关控制。
