<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources/objects/search -->
<!-- 研读状态：已完成 -->

# Search Objects Details • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources/objects/search)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v1/ontology-resources
- 相关性：direct；Ontology API v1 搜索语法详情，保留兼容性对照并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:53Z
- 产品状态：文档语法页；词法解析规则可能变化

## 英文原文短摘录（每个来源不超过 25 词）

> “Queries can be at most three levels deep.”

## 摘录译文

查询最多嵌套三层。

## 中文要点

- 本页说明 `POST /api/v1/ontologies/{ontologyRid}/objects/{objectType}/search` 的查询语法：比较 (`lt/gt/lte/gte/eq`)、null、数组包含、`not/and/or` 组合，以及面向字符串的 `prefix/phrase/anyTerm/allTerms`。
- 各操作支持属性类型不同；布尔子查询最多三层。文本查询依赖词语解析和标点拆分，官方提示解析规则可能变化，不能假设其等同于固定标准全文搜索。
- OSv1 搜索结果最多 10,000 个对象；null 属性不返回。端点排序与 groupBy 的响应契约也在这篇详情页列出。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| query operator | 查询操作符 | 描述过滤、比较和文本匹配行为 |
| prefix | 前缀匹配 | 有序词语中最后一项按前缀处理 |
| phrase | 短语匹配 | 按指定词序匹配文本 |
| anyTerm / allTerms | 任意词 / 全部词 | 对字符串中的词集合执行匹配 |
| query depth | 查询嵌套深度 | and/or/not 查询结构的层数上限 |

## 疑问与待验证项

- 文本解析行为明示可能变化；需对大小写、连字符、单独句点和标点空格建立实际环境验收样例。
- 空条件、未知字段、不支持属性类型、超深查询的错误形状应通过 API Error 文档确认。
- 搜索详情页是否保证与对应 endpoint 页同样的分页/一致性规则，应结合接口文档复核。

## 复刻启示

- 构造按 schema 校验的查询 AST，校验属性类型、操作符兼容性和三层上限，再编译为 SQL/搜索后端条件。
- UI Builder 按类型显示允许操作并解释文本匹配的词法语义；Agent 只能提交同一 AST，不可逃逸到任意查询。
- 查询规则变更应版本化，保证已发布查询和历史执行记录能复现旧语义。
