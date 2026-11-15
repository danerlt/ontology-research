<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-object-sets/create-temporary-object-set -->
<!-- 研读状态：已完成 -->

# Create Temporary Object Set • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-object-sets/create-temporary-object-set)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/ontology-object-sets
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:54:05Z
- 产品状态：Preview API，需显式传 `preview=true`；临时集合一小时后过期。

## 英文原文短摘录（每个来源不超过 25 词）

> “Creates a temporary `ObjectSet` from the given definition. This `ObjectSet` expires after one hour.”

## 摘录译文

根据定义创建临时对象集合；该集合一小时后过期。

## 中文要点

- POST `/api/v2/ontologies/{ontology}/objectSets/createTemporary` 将请求体中的 ObjectSet 定义存成临时资源，成功响应返回 `objectSetRid`；创建的集合仅保留一小时。
- 端点处于 Preview，调用需 `preview=true`。OAuth 第三方应用必须同时申请 `api:ontologies-read` 和 `api:ontologies-write`；branch 可选，但分支流程本身仍为实验性。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| temporary ObjectSet | 临时对象集合 | 短期保存的集合资源，创建后一小时过期。 |
| objectSetRid | 集合资源 RID | 后续请求引用刚创建的临时集合。 |
| preview | 预览标志 | 启用仍处预览阶段的端点。 |

## 疑问与待验证项

- 一小时过期时间意味着临时 RID 不适合保存到长期配置或持久链接；文档未说明过期前能否续期。
- 创建权限同时要求 Ontology 读写 scope，使用“创建但不写实例”的能力时也不能仅按只读授权配置。

## 复刻启示

- 预览复杂画布查询时可保存短期集合快照并返回 RID，但界面须提示过期时间，并在过期后能由 AST 安全重算。
- 把集合资源的创建作为有权限、可审计的操作；写入和只读权限分离时，应单独定义本地 API 的授权语义。
