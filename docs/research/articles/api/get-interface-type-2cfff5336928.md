<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-interfaces/get-interface-type -->
<!-- 研读状态：已完成 -->

# Get Interface Type • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-interfaces/get-interface-type)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/ontology-interfaces
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:54:00Z
- 产品状态：Preview 兼容路由；调用需传 `preview=true`

## 英文原文短摘录（每个来源不超过 25 词）

> “Gets a specific interface type with the given API name.”

## 摘录译文

获取指定 API 名对应的接口类型。

## 中文要点

该 v2 Ontology REST API 按本体标识与接口类型 API 名读取单个接口。调用必须启用 `preview=true`，可选择实验性分支和生成 SDK 的版本参数；第三方 OAuth2 调用要求 `api:ontologies-read`。响应结构包括接口自身/继承的属性、扩展接口、实现该接口的对象类型和接口链接。页面的 canonical URL 位于 `/api/v2/...`；本卡保留目录里的兼容路由。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Interface Type | 接口类型 | 按 API 名读取的本体契约定义 |
| `extendsInterfaces` | 扩展接口 | 当前接口直接继承的接口 |
| `allExtendsInterfaces` | 全部父接口 | 直接与间接继承的接口 |
| `api:ontologies-read` | 本体读取范围 | 第三方 OAuth2 所需 operation scope |

## 疑问与待验证项

- 分支支持不完整；需要对照目标实例验证请求的 branch 能否读取此类定义。
- API 处于 Preview，字段兼容策略及正式稳定时间在文档中没有承诺。

## 复刻启示

- 给本地 SDK/Agent 工具暴露接口读取时，工具 schema 标注只读作用域和预览能力，同时限制项目/本体范围。
- 画布详情需要将继承属性、当前接口直接属性与接口链接分区展示，避免把继承字段误看成重复定义。
