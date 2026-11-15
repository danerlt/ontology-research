<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontologies/list-ontologies -->
<!-- 研读状态：已完成 -->

# List Ontologies (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontologies/list-ontologies)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/ontologies
- 相关性：direct；本体管理与治理文档
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:54:00Z
- 产品状态：正式 API（v1/v2 页面均未标注 Preview）

## 英文原文短摘录（每个来源不超过 25 词）

> “Lists the Ontologies visible to the current user.”

## 摘录译文

列出当前用户可见的本体。

## 中文要点

- v1 与 v2 的列表端点均返回当前用户可访问的本体数组；每项包括 API 名称、显示名称、描述和 RID。
- 该页面没有分页参数或分页令牌，OAuth 应用需要 `api:ontologies-read`。
- 列表的可见性由当前用户权限限定；“列表中没有”不应直接解释为全平台不存在。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Visible to current user | 当前用户可见 | 返回范围受访问权限约束 |
| Ontology list | 本体列表 | 包含标识、名称和描述的目录项 |
| RID | 资源标识符 | 本体的唯一资源身份 |

## 疑问与待验证项

- 文档没有说明大型租户的列表规模上限、排序保证或分页方式。
- 同一用户在不同组织/安全域中是否会看到不同列表，取决于平台权限上下文，需结合授权文档验证。

## 复刻启示

- 本体切换器应展示授权范围内的目录，并在接口层执行成员身份校验；前端隐藏选项不能替代服务端项目隔离。
- 如果本地支持项目与多个本体，应明确区分“本地项目清单”和“当前凭证可见的外部本体清单”，避免混用实体。
