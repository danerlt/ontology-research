<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-value-types/list-ontology-value-types -->
<!-- 研读状态：已完成 -->

# List Ontology Value Types • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-value-types/list-ontology-value-types)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/ontology-value-types
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:54:24Z
- 产品状态：预览（Preview；请求需显式启用 `preview=true`）

## 英文原文短摘录（每个来源不超过 25 词）

> “Lists the latest versions of the value types for the given Ontology.”

## 摘录译文

列出指定本体中值类型的最新版本。

## 中文要点

- 列表接口返回指定本体所有可用值类型的最新版本，每个条目可包含 API 名称、展示名、状态、RID、基础 fieldType 与约束。
- 该端点处于 Preview，需要显式 `preview=true`；OAuth 应用需要 `api:ontologies-read`。文档未给出分页参数。
- 列表最新版本与单个值类型端点的版本字段结合使用，可构建类型目录及字段设计器候选项。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Latest version | 最新版本 | 列表只列各值类型的最新版本 |
| Value type catalog | 值类型目录 | 本体字段设计器可选类型 |
| Constraint | 约束 | 字段值校验规则 |

## 疑问与待验证项

- 文档没有分页参数，未说明大量值类型时的结果上限或排序保证。
- 列表暴露的状态与约束是否遵循字段使用者权限或本体读取权限，需结合权限模型验证。

## 复刻启示

- 字段编辑器可缓存值类型目录，但缓存键要包含 ontology、用户权限上下文和版本时间，并允许刷新。
- 仅列最新版本意味着需另设版本审计端点/历史模型，不能把此列表当成完整版本历史。
