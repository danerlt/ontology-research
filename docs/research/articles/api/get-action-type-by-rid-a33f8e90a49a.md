<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/action-types/get-action-type-by-rid -->
<!-- 研读状态：已完成 -->

# Get Action Type By Rid • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/action-types/get-action-type-by-rid)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/action-types
- 相关性：direct；本体动作文档
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:53:29Z
- 产品状态：按页面现行表述整理；涉及分支/事务的能力以 Preview 或实验性限制为准。

## 英文原文短摘录（每个来源不超过 25 词）

> “Gets a specific action type with the given RID.”

## 摘录译文

按指定 RID 获取一个 Action Type。

## 中文要点

- GET `/api/v2/ontologies/{ontology}/actionTypes/byRid/{actionTypeRid}` 通过唯一资源标识读取动作定义，适合其他 Foundry API 或跨服务稳定引用。
- 返回结构与按 API 名称读取基本一致，包括名称、描述、状态、参数、逻辑规则、工具描述和返回类型。
- 可选指定 branch；第三方 OAuth 客户端需要 `api:ontologies-read`，分支能力受实验支持范围限制。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| RID | 资源标识符 | Action Type 在平台中的唯一标识。 |
| by RID | 按资源标识查询 | 不依赖显示名或 API 名称定位资源。 |
| branch | 分支 | 可选的本体定义版本上下文。 |

## 疑问与待验证项

- 页面没有阐释 RID 在本体复制、导入或跨项目迁移后的稳定性。
- 需要确认 RID 查询与 API 名称查询在分支发布后的解析差异。

## 复刻启示

- 数据库内部使用不可变主键关联动作定义；对外展示 API 名称，服务间调用传稳定资源 ID。
- 项目复制/导入时显式维护旧 RID 到新 RID 的映射，并校验动作节点引用仍有效。
