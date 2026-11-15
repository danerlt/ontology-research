<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology/search-syntax -->
<!-- 研读状态：已完成 -->

# Search syntax • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology/search-syntax)
- 官方中文来源：尚未确认（目录配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：ontology
- 相关性：direct；Ontology 中字符串属性正则搜索语法
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:03Z
- 产品状态：regex 搜索需先对字符串属性启用索引；语法与常见 regex 有差异

## 英文原文短摘录（不超过 25 词）

> “Patterns match the full value, not substrings.”

## 摘录译文

模式匹配整个属性值，而不是任意子字符串。

## 中文要点

- 页面说明 Workshop 筛选列表和 Object Explorer 搜索栏中的本体搜索语法，具体覆盖正则表达式查询。
- 对字符串属性做 regex 搜索前，必须在 Ontology Manager 的 Properties→Interaction 启用 regex queries 索引。
- 模式默认从完整字符串开头匹配到结尾；搜索 `cat` 只匹配完整值 `cat`，要匹配子串需显式加 `.*cat.*`。
- `^`、`$` 锚点不支持，因为完整字段匹配已经隐式覆盖首尾；`.`、`?`、`+`、`*`、`{}`、`|`、`()`、`[]` 支持各自的通配、重复、分组和选择语义。
- 双引号把字符当作字面文本，反斜线用于转义 regex 操作符并提供快捷字符类；例如 `"v2.0"` 让点按字面量处理。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| regular expression (regex) | 正则表达式 | 在已索引字符串属性上执行模式匹配 |
| full-value match | 全值匹配 | regex 默认匹配完整属性值 |
| literal string | 字面字符串 | 用引号将正则运算符作为普通字符搜索 |
| regex query index | 正则查询索引 | 在属性交互设置中开启的搜索能力 |

## 疑问与待验证项

- 文档仅覆盖 regex 子集；不能假设支持 JavaScript/Python 完整 regex 语法或回溯特性。
- 启用索引是否产生资源成本、多久生效和大小写/Unicode 规则需核对索引设置与数据类型参考。
- 该语法面向显式正则搜索，与 OSDK `contains` 仅支持整词/前缀的限制不是同一个 API。

## 复刻启示

- 搜索 UI 应区分精确匹配、前缀/全文检索与正则查询，并在启用正则前检查属性索引能力。
- 用语法提示/示例解释全值匹配、点号通配与转义，避免用户误把 regex 输入当成普通子串。
- 查询计划记录搜索字段、索引类型和匹配模式；缺少 regex 索引时返回可操作的配置错误。