<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/object-types/get-outgoing-link-types-by-object-type-rid-batch -->
<!-- 研读状态：已完成 -->

# Get Outgoing Link Types By Object Type Rid Batch • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/object-types/get-outgoing-link-types-by-object-type-rid-batch)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；对象类型与本体建模文档
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:57:02Z
- 产品状态：预览（Preview；请求需显式启用 `preview=true`）

## 英文原文短摘录（每个来源不超过 25 词）

> “Gets outgoing link types for a batch of object types, identified by their RIDs.”

## 摘录译文

按对象类型 RID 批量获取出向链接类型。

## 中文要点

- 接口对一批对象类型分别返回当前令牌可见的出向链接，可选 `filterLinkTypeRids` 将结果限制到给定链接 RID。
- 不存在或调用方无权访问的对象类型会被静默省略；每批最多 100 个对象类型。
- 该端点处于 Preview，需传 `preview=true`；可指定 branch；OAuth 应用需要 `api:ontologies-read`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Batch request | 批量请求 | 以多个对象类型 RID 作为输入 |
| Filter link type RIDs | 链接 RID 过滤器 | 仅返回命中的链接定义 |
| Visible links | 可见链接 | 响应受请求令牌权限范围约束 |

## 疑问与待验证项

- 被静默省略的对象类型是否能区分无权限与资源不存在，文档没有提供信号。
- 不同对象类型的链接列表在响应中如何与请求 RID 关联，应核查响应元素结构，避免批量重排导致错连。

## 复刻启示

- 适合画布布局初始化时按批拉取邻接边定义；客户端需按对象类型 RID 分组，同时处理缺项和部分授权。
- 可把链接 RID 过滤器用于局部展开，避免每次展开节点都加载全图边，但 Preview 状态要求适配层可回退到逐类型列表接口。
